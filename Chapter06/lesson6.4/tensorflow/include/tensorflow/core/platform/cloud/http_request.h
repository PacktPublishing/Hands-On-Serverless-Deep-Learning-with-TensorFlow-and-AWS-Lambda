/* Copyright 2016 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_CORE_PLATFORM_HTTP_REQUEST_H_
#define TENSORFLOW_CORE_PLATFORM_HTTP_REQUEST_H_

#include <string>
#include <unordered_map>
#include <vector>
#include "tensorflow/core/lib/core/errors.h"
#include "tensorflow/core/lib/core/status.h"
#include "tensorflow/core/lib/core/stringpiece.h"
#include "tensorflow/core/platform/env.h"
#include "tensorflow/core/platform/macros.h"
#include "tensorflow/core/platform/protobuf.h"
#include "tensorflow/core/platform/types.h"

namespace tensorflow {

/// \brief An abstract basic HTTP client.
///
/// The usage pattern for the class is based on the libcurl library:
/// create a request object, set request parameters and call Send().
///
/// For example:
///   HttpRequest request;
///   request.SetUri("http://www.google.com");
///   request.SetResultsBuffer(out_buffer);
///   request.Send();
class HttpRequest {
 public:
  class Factory {
   public:
    virtual ~Factory() {}
    virtual HttpRequest* Create() = 0;
  };

  HttpRequest() {}
  virtual ~HttpRequest() {}

  virtual Status Init() = 0;

  /// Sets the request URI.
  virtual Status SetUri(const string& uri) = 0;

  /// \brief Sets the Range header.
  ///
  /// Used for random seeks, for example "0-999" returns the first 1000 bytes
  /// (note that the right border is included).
  virtual Status SetRange(uint64 start, uint64 end) = 0;

  /// Sets a request header.
  virtual Status AddHeader(const string& name, const string& value) = 0;

  /// Sets the 'Authorization' header to the value of 'Bearer ' + auth_token.
  virtual Status AddAuthBearerHeader(const string& auth_token) = 0;

  /// Makes the request a DELETE request.
  virtual Status SetDeleteRequest() = 0;

  /// \brief Makes the request a PUT request.
  ///
  /// The request body will be taken from the specified file starting from
  /// the given offset.
  virtual Status SetPutFromFile(const string& body_filepath, size_t offset) = 0;

  /// Makes the request a PUT request with an empty body.
  virtual Status SetPutEmptyBody() = 0;

  /// \brief Makes the request a POST request.
  ///
  /// The request body will be taken from the specified buffer.
  virtual Status SetPostFromBuffer(const char* buffer, size_t size) = 0;

  /// Makes the request a POST request with an empty body.
  virtual Status SetPostEmptyBody() = 0;

  /// \brief Specifies the buffer for receiving the response body.
  ///
  /// Size of out_buffer after an access will be exactly the number of bytes
  /// read. Existing content of the vector will be cleared.
  virtual Status SetResultBuffer(std::vector<char>* out_buffer) = 0;

  /// \brief Returns the response headers of a completed request.
  ///
  /// If the header is not found, returns an empty string.
  virtual string GetResponseHeader(const string& name) const = 0;

  /// Returns the response code of a completed request.
  virtual uint64 GetResponseCode() const = 0;

  /// \brief Sends the formed request.
  ///
  /// If the result buffer was defined, the response will be written there.
  /// The object is not designed to be re-used after Send() is executed.
  virtual Status Send() = 0;

  // Url encodes str and returns a new string.
  virtual string EscapeString(const string& str) = 0;

  TF_DISALLOW_COPY_AND_ASSIGN(HttpRequest);
};

}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_PLATFORM_HTTP_REQUEST_H_
