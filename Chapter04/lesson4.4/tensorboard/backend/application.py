# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""TensorBoard WSGI Application Logic.

TensorBoardApplication constructs TensorBoard as a WSGI application.
It handles serving static assets, and implements TensorBoard data APIs.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import json
import os
import re
import sqlite3
import threading
import time

import six
from six.moves.urllib import parse as urlparse
import tensorflow as tf
from werkzeug import wrappers

from tensorboard import db
from tensorboard.backend import http_util
from tensorboard.backend.event_processing import plugin_event_accumulator as event_accumulator  # pylint: disable=line-too-long
from tensorboard.backend.event_processing import plugin_event_multiplexer as event_multiplexer  # pylint: disable=line-too-long
from tensorboard.plugins import base_plugin
from tensorboard.plugins.audio import metadata as audio_metadata
from tensorboard.plugins.core import core_plugin
from tensorboard.plugins.histogram import metadata as histogram_metadata
from tensorboard.plugins.image import metadata as image_metadata
from tensorboard.plugins.scalar import metadata as scalar_metadata


DEFAULT_SIZE_GUIDANCE = {
    event_accumulator.TENSORS: 10,
}

# TODO(@wchargin): Once SQL mode is in play, replace this with an
# alternative that does not privilege first-party plugins.
DEFAULT_TENSOR_SIZE_GUIDANCE = {
    scalar_metadata.PLUGIN_NAME: 1000,
    image_metadata.PLUGIN_NAME: 10,
    audio_metadata.PLUGIN_NAME: 10,
    histogram_metadata.PLUGIN_NAME: 500,
}

DATA_PREFIX = '/data'
PLUGIN_PREFIX = '/plugin'
PLUGINS_LISTING_ROUTE = '/plugins_listing'

# Slashes in a plugin name could throw the router for a loop. An empty
# name would be confusing, too. To be safe, let's restrict the valid
# names as follows.
_VALID_PLUGIN_RE = re.compile(r'^[A-Za-z0-9_.-]+$')


def standard_tensorboard_wsgi(
    logdir,
    purge_orphaned_data,
    reload_interval,
    plugins,
    db_uri="",
    assets_zip_provider=None,
    path_prefix=""):
  """Construct a TensorBoardWSGIApp with standard plugins and multiplexer.

  Args:
    logdir: The path to the directory containing events files.
    purge_orphaned_data: Whether to purge orphaned data.
    reload_interval: The interval at which the backend reloads more data in
        seconds.
    plugins: A list of constructor functions for TBPlugin subclasses.
    path_prefix: A prefix of the path when app isn't served from root.
    db_uri: A String containing the URI of the SQL database for persisting
        data, or empty for memory-only mode.
    assets_zip_provider: See TBContext documentation for more information.
        If this value is not specified, this function will attempt to load
        the `tensorboard.default` module to use the default. This behavior
        might be removed in the future.

  Returns:
    The new TensorBoard WSGI application.
  """
  if assets_zip_provider is None:
    from tensorboard import default
    assets_zip_provider = default.get_assets_zip_provider()
  multiplexer = event_multiplexer.EventMultiplexer(
      size_guidance=DEFAULT_SIZE_GUIDANCE,
      tensor_size_guidance=DEFAULT_TENSOR_SIZE_GUIDANCE,
      purge_orphaned_data=purge_orphaned_data)
  db_module, db_connection_provider = get_database_info(db_uri)
  if db_connection_provider is not None:
    with contextlib.closing(db_connection_provider()) as db_conn:
      schema = db.Schema(db_conn)
      schema.create_tables()
      schema.create_indexes()
  context = base_plugin.TBContext(
      db_module=db_module,
      db_connection_provider=db_connection_provider,
      logdir=logdir,
      multiplexer=multiplexer,
      assets_zip_provider=assets_zip_provider)
  plugins = [constructor(context) for constructor in plugins]
  return TensorBoardWSGIApp(logdir, plugins, multiplexer, reload_interval,
                            path_prefix)


def TensorBoardWSGIApp(logdir, plugins, multiplexer, reload_interval,
                       path_prefix):
  """Constructs the TensorBoard application.

  Args:
    logdir: the logdir spec that describes where data will be loaded.
      may be a directory, or comma,separated list of directories, or colons
      can be used to provide named directories
    plugins: A list of base_plugin.TBPlugin subclass instances.
    multiplexer: The EventMultiplexer with TensorBoard data to serve
    reload_interval: How often (in seconds) to reload the Multiplexer
    path_prefix: A prefix of the path when app isn't served from root.

  Returns:
    A WSGI application that implements the TensorBoard backend.

  Raises:
    ValueError: If something is wrong with the plugin configuration.
  """
  path_to_run = parse_event_files_spec(logdir)
  if reload_interval:
    start_reloading_multiplexer(multiplexer, path_to_run, reload_interval)
  else:
    reload_multiplexer(multiplexer, path_to_run)
  return TensorBoardWSGI(plugins, path_prefix)


class TensorBoardWSGI(object):
  """The TensorBoard WSGI app that delegates to a set of TBPlugin."""

  def __init__(self, plugins, path_prefix=""):
    """Constructs TensorBoardWSGI instance.

    Args:
      plugins: A list of base_plugin.TBPlugin subclass instances.
      path_prefix: A prefix of the path when app isn't served from root.

    Returns:
      A WSGI application for the set of all TBPlugin instances.

    Raises:
      ValueError: If some plugin has no plugin_name
      ValueError: If some plugin has an invalid plugin_name (plugin
          names must only contain [A-Za-z0-9_.-])
      ValueError: If two plugins have the same plugin_name
      ValueError: If some plugin handles a route that does not start
          with a slash
    """
    self._plugins = plugins
    if path_prefix.endswith('/'):
      self._path_prefix = path_prefix[:-1]
    else:
      self._path_prefix = path_prefix

    self.data_applications = {
        # TODO(@chihuahua): Delete this RPC once we have skylark rules that
        # obviate the need for the frontend to determine which plugins are
        # active.
        self._path_prefix + DATA_PREFIX + PLUGINS_LISTING_ROUTE:
            self._serve_plugins_listing,
    }

    # Serve the routes from the registered plugins using their name as the route
    # prefix. For example if plugin z has two routes /a and /b, they will be
    # served as /data/plugin/z/a and /data/plugin/z/b.
    plugin_names_encountered = set()
    for plugin in self._plugins:
      if plugin.plugin_name is None:
        raise ValueError('Plugin %s has no plugin_name' % plugin)
      if not _VALID_PLUGIN_RE.match(plugin.plugin_name):
        raise ValueError('Plugin %s has invalid name %r' % (plugin,
                                                            plugin.plugin_name))
      if plugin.plugin_name in plugin_names_encountered:
        raise ValueError('Duplicate plugins for name %s' % plugin.plugin_name)
      plugin_names_encountered.add(plugin.plugin_name)

      try:
        plugin_apps = plugin.get_plugin_apps()
      except Exception as e:  # pylint: disable=broad-except
        if type(plugin) is core_plugin.CorePlugin:  # pylint: disable=unidiomatic-typecheck
          raise
        tf.logging.warning('Plugin %s failed. Exception: %s',
                           plugin.plugin_name, str(e))
        continue
      for route, app in plugin_apps.items():
        if not route.startswith('/'):
          raise ValueError('Plugin named %r handles invalid route %r: '
                           'route does not start with a slash' %
                           (plugin.plugin_name, route))
        if type(plugin) is core_plugin.CorePlugin:  # pylint: disable=unidiomatic-typecheck
          path = self._path_prefix + route
        else:
          path = self._path_prefix + DATA_PREFIX + PLUGIN_PREFIX + '/' + \
                    plugin.plugin_name + route
        self.data_applications[path] = app

  @wrappers.Request.application
  def _serve_plugins_listing(self, request):
    """Serves an object mapping plugin name to whether it is enabled.

    Args:
      request: The werkzeug.Request object.

    Returns:
      A werkzeug.Response object.
    """
    response = {}
    for plugin in self._plugins:
      start = time.time()
      response[plugin.plugin_name] = plugin.is_active()
      elapsed = time.time() - start
      tf.logging.info(
          'Plugin listing: is_active() for %s took %0.3f seconds',
          plugin.plugin_name, elapsed)
    return http_util.Respond(request, response, 'application/json')

  def __call__(self, environ, start_response):  # pylint: disable=invalid-name
    """Central entry point for the TensorBoard application.

    This method handles routing to sub-applications. It does simple routing
    using regular expression matching.

    This __call__ method conforms to the WSGI spec, so that instances of this
    class are WSGI applications.

    Args:
      environ: See WSGI spec.
      start_response: See WSGI spec.

    Returns:
      A werkzeug Response.
    """
    request = wrappers.Request(environ)
    parsed_url = urlparse.urlparse(request.path)
    clean_path = _clean_path(parsed_url.path, self._path_prefix)

    # pylint: disable=too-many-function-args
    if clean_path in self.data_applications:
      return self.data_applications[clean_path](environ, start_response)
    else:
      tf.logging.warning('path %s not found, sending 404', clean_path)
      return http_util.Respond(request, 'Not found', 'text/plain', code=404)(
          environ, start_response)
    # pylint: enable=too-many-function-args


def parse_event_files_spec(logdir):
  """Parses `logdir` into a map from paths to run group names.

  The events files flag format is a comma-separated list of path specifications.
  A path specification either looks like 'group_name:/path/to/directory' or
  '/path/to/directory'; in the latter case, the group is unnamed. Group names
  cannot start with a forward slash: /foo:bar/baz will be interpreted as a
  spec with no name and path '/foo:bar/baz'.

  Globs are not supported.

  Args:
    logdir: A comma-separated list of run specifications.
  Returns:
    A dict mapping directory paths to names like {'/path/to/directory': 'name'}.
    Groups without an explicit name are named after their path. If logdir is
    None, returns an empty dict, which is helpful for testing things that don't
    require any valid runs.
  """
  files = {}
  if logdir is None:
    return files
  # Make sure keeping consistent with ParseURI in core/lib/io/path.cc
  uri_pattern = re.compile('[a-zA-Z][0-9a-zA-Z.]*://.*')
  for specification in logdir.split(','):
    # Check if the spec contains group. A spec start with xyz:// is regarded as
    # URI path spec instead of group spec. If the spec looks like /foo:bar/baz,
    # then we assume it's a path with a colon.
    if (uri_pattern.match(specification) is None and ':' in specification and
        specification[0] != '/'):
      # We split at most once so run_name:/path:with/a/colon will work.
      run_name, _, path = specification.partition(':')
    else:
      run_name = None
      path = specification
    if uri_pattern.match(path) is None:
      path = os.path.realpath(path)
    files[path] = run_name
  return files


def reload_multiplexer(multiplexer, path_to_run):
  """Loads all runs into the multiplexer.

  Args:
    multiplexer: The `EventMultiplexer` to add runs to and reload.
    path_to_run: A dict mapping from paths to run names, where `None` as the run
      name is interpreted as a run name equal to the path.
  """
  start = time.time()
  tf.logging.info('TensorBoard reload process beginning')
  for (path, name) in six.iteritems(path_to_run):
    multiplexer.AddRunsFromDirectory(path, name)
  tf.logging.info('TensorBoard reload process: Reload the whole Multiplexer')
  multiplexer.Reload()
  duration = time.time() - start
  tf.logging.info('TensorBoard done reloading. Load took %0.3f secs', duration)


def start_reloading_multiplexer(multiplexer, path_to_run, load_interval):
  """Starts a thread to automatically reload the given multiplexer.

  The thread will reload the multiplexer by calling `ReloadMultiplexer` every
  `load_interval` seconds, starting immediately.

  Args:
    multiplexer: The `EventMultiplexer` to add runs to and reload.
    path_to_run: A dict mapping from paths to run names, where `None` as the run
      name is interpreted as a run name equal to the path.
    load_interval: How many seconds to wait after one load before starting the
      next load.

  Returns:
    A started `threading.Thread` that reloads the multiplexer.
  """

  # We don't call multiplexer.Reload() here because that would make
  # AddRunsFromDirectory block until the runs have all loaded.
  def _reload_forever():
    while True:
      reload_multiplexer(multiplexer, path_to_run)
      time.sleep(load_interval)

  thread = threading.Thread(target=_reload_forever, name='Reloader')
  thread.daemon = True
  thread.start()
  return thread


def get_database_info(db_uri):
  """Returns TBContext fields relating to SQL database.

  Args:
    db_uri: A string URI expressing the DB file, e.g. "sqlite:~/tb.db".

  Returns:
    A tuple with the db_module and db_connection_provider TBContext fields. If
    db_uri was empty, then (None, None) is returned.

  Raises:
    ValueError: If db_uri scheme is not supported.
  """
  if not db_uri:
    return None, None
  scheme = urlparse.urlparse(db_uri).scheme
  if scheme == 'sqlite':
    return sqlite3, create_sqlite_connection_provider(db_uri)
  else:
    raise ValueError('Only sqlite DB URIs are supported now: ' + db_uri)


def create_sqlite_connection_provider(db_uri):
  """Returns function that returns SQLite Connection objects.

  Args:
    db_uri: A string URI expressing the DB file, e.g. "sqlite:~/tb.db".

  Returns:
    A function that returns a new PEP-249 DB Connection, which must be closed,
    each time it is called.

  Raises:
    ValueError: If db_uri is not a valid sqlite file URI.
  """
  uri = urlparse.urlparse(db_uri)
  if uri.scheme != 'sqlite':
    raise ValueError('Scheme is not sqlite: ' + db_uri)
  if uri.netloc:
    raise ValueError('Can not connect to SQLite over network: ' + db_uri)
  if uri.path == ':memory:':
    raise ValueError('Memory mode SQLite not supported: ' + db_uri)
  path = os.path.expanduser(uri.path)
  params = _get_connect_params(uri.query)
  # TODO(@jart): Add thread-local pooling.
  return lambda: db.Connection(sqlite3.connect(path, **params))


def _get_connect_params(query):
  params = urlparse.parse_qs(query)
  if any(len(v) > 2 for v in params.values()):
    raise ValueError('DB URI params list has duplicate keys: ' + query)
  return {k: json.loads(v[0]) for k, v in params.items()}


def _clean_path(path, path_prefix=""):
  """Cleans the path of the request.

  Removes the ending '/' if the request begins with the path prefix and pings a
  non-empty route.

  Arguments:
    path: The path of a request.
    path_prefix: The prefix string that every route of this TensorBoard instance
    starts with.

  Returns:
    The route to use to serve the request (with the path prefix stripped if
    applicable).
  """
  if path != path_prefix + '/' and path.endswith('/'):
    return path[:-1]
  return path
