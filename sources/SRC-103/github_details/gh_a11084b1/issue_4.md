# [Issue #4] [Feature]: filtering

source: https://github.com/ROCm/rocprofiler-sdk/issues/4
state: closed | updated: 2024-12-16T21:11:22Z
labels: 

## 正文

### Suggestion Description

The doc for `rocprofv3` gives a clear overview of the features. However, notably, it appears that "filtering" is not/no longer a feature. By filtering, I mean restricting the profiling e.g. to a kernel with a specific name, to a region identified with roctx markers, to a region identified with start/stop markers, ... I just wanted to ask the question whether support for such filtering is not planned for `rocprofv3` or whether it is planned to be added at a later stage?

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_

## 评论 (2)

### jrmadsen · 2024-04-18

Hi @maartenarnst, if you use the new `rocprofiler-sdk-roctx`, there are new ROCTx functions: `roctxProfilerPause` and `roctxProfilerResume`. This will completely shut off data collection of everything in `rocprofv3`.

## Sample

```cpp
#include <rocprofiler-sdk-roctx/roctx.h>

__global__ void
transpose(const int* in, int* out, int M, int N);

int main()
{
    auto tid = roctx_thread_id_t{};
    // get the thread id recognized by rocprofiler-sdk from roctx
    roctxGetThreadId(&tid);

    for(size_t i = 0; i < 100; ++i)
    {
        transpose<<<256, 64>>>(...);
        if(i == 0)
        {
            // first kernel will be profiled, all subsequent kernel launchs and/or API calls will not be collected
            // NOTE: there is no need for any device/stream "sync" here
            roctxProfilerPause(tid);
        }
    }
    hipDeviceSynchronize();

    return 0;
}
```

You are welcome to test out this feature. Anything command-line based will probably be supported eventually but we have rewritten the rocprofiler library from scratch so `rocprofv3` is a secondary focus while this foundational work is still under development (i.e. it's hard to build a full-featured tool when the library that the tool is built on top of is still being written/designed).

### darren-amd · 2024-12-16

Hi @maartenarnst,

Going to close this ticket, please see above for the response to your question. Please feel free to create another ticket if you have any future concerns, thanks!
