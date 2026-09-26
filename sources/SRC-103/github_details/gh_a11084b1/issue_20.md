# [Issue #20] [FYI]: OTF2 3.1 comes with limited CMake support

source: https://github.com/ROCm/rocprofiler-sdk/issues/20
state: closed | updated: 2025-01-16T21:14:22Z
labels: Under Investigation

## 正文

### Suggestion Description

See the `contrib/CMakeFile.txt` in the latest rc3: https://perftools.pages.jsc.fz-juelich.de/cicd/otf2/tags/otf2-3.1-rc3/otf2-3.1-rc3.tar.gz

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_

## 评论 (3)

### jrmadsen · 2025-01-15

@bertwesarg presently we just build OTF2 from source as a static library. By “limited” I’m guessing you just support `find_package(otf2)`? 

### bertwesarg · 2025-01-15

by limited I mean, there is no support and it works when we build Vampir. There we also only need a static library and no tools on Linux/mac/win. So your use case could be covered too.

### jrmadsen · 2025-01-16

Excellent, thanks for the info. 
