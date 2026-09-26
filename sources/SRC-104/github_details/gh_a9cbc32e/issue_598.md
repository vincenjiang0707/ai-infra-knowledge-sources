# [Issue #598] Question on TCP_TOTAL_CACHE_ACCESSES_sum and L1cache_data

source: https://github.com/ROCm/rocprofiler-compute/issues/598
state: closed | updated: 2025-05-14T15:18:12Z
labels: question, Under Investigation

## 正文

### Describe your question

For a simple memory bound kernel (e.g., matrix linear combination) I would expect to have HBM accesses as L1 (hit+miss) accesses, since most of the accesses are "miss". However, I found that L1cache_data is twice the HBM value. In roofline_calc.py L1 data is computed as:

`L1cache_data += df["TCP_TOTAL_CACHE_ACCESSES_sum"][idx] * 64`

Is it correct to have 64 as units of accesses? I am using MI250X GCD.



### Additional context

_No response_

## 评论 (2)

### ppanchad-amd · 2025-03-10

Hi @francescosalvadore. Internal ticket has been created to assist with your question. Thanks!

### benrichard-amd · 2025-05-14

Hi @francescosalvadore,

`TCP_TOTAL_CACHE_ACCESSES_sum` is the total number of lines loaded from cache per unit time, so we need to count hits and misses. It's multiplied by 64 because the cache line on MI250X is 64 bytes. 
