/* Copyright 2016 Google Inc.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. */

#ifndef NSYNC_PLATFORM_MACOS_PLATFORM_H_
#define NSYNC_PLATFORM_MACOS_PLATFORM_H_

#define _DARWIN_C_SOURCE

#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <inttypes.h>
#include <limits.h>
#include <sys/time.h>

#include <pthread.h>
#include <stdio.h>
#include <stdarg.h>

#define CLOCK_REALTIME 0
typedef int clockid_t;
int clock_gettime (clockid_t clk_id, struct timespec *tp);
#define TIMER_ABSTIME 1

#endif /*NSYNC_PLATFORM_MACOS_PLATFORM_H_*/
