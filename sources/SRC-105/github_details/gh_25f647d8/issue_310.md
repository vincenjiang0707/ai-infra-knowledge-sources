# [Issue #310] Can DCGM Profiling Metrics retrieve metrics at a frequency of less than 100 ms?

source: https://github.com/NVIDIA/DCGM/issues/310
state: open | updated: 2026-08-26T15:31:58Z
labels: 

## 正文

As stated in the [documentation](https://docs.nvidia.com/datacenter/dcgm/latest/learn/modules/profiling.html#metrics), DCGM Profiling Metrics have a minimum sampling interval requirement of 100 ms. However, `dcgmi dmon` allows for a minimum sampling interval of 1 ms (possibly because non-profiling metrics are designed to support this).

Testing has shown that `dcgmi dmon` can indeed use a 1ms sampling interval and produce values that appear reasonable. However, we want to confirm: Is this metric reliable? Are these continuous results truly taken every 1ms? Or is it a sliding window that returns the result from the most recent 100ms every 1ms? Or is it simply the most recent cached value?

Thank you.


## 评论 (1)

### nvidia-aalsudani · 2026-08-26

Assuming it's a Hopper GPU, the values retrieved at a 1ms interval are invalid. 100ms is a hard limitation. A future release of DCGM will return an error when a user tries to watch the profiling metrics at >10Hz.
