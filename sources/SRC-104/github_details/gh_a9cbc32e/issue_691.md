# [Issue #691] Discrepancies in spec and roofline

source: https://github.com/ROCm/rocprofiler-compute/issues/691
state: closed | updated: 2025-04-30T20:08:09Z
labels: question, Under Investigation

## 正文

### Describe your question

The MI300A spec gives 61 TFlop/s Binary64 throughput on an MI300A. https://www.amd.com/en/products/accelerators/instinct/mi300/mi300a.html
The roofline is placed at 81 TFlop/s.

![Image](https://github.com/user-attachments/assets/c57de8f2-d0e1-46d2-a35e-0855040e58be)

Is there an explanation ? Could we get access to the sources of the AMD tools used to produce these rooflines ?

Aren't you extrapolating too far on the perf, for isntance using the MI300X CU count ?

### Additional context

_No response_

## 评论 (3)

### etiennemlb · 2025-04-30

Also, the MI300A throttles soo much that the expected performance seems completely out of reach.

### ppanchad-amd · 2025-04-30

Hi @etiennemlb. Internal ticket has been created to investigate this issue. Thanks!

### benrichard-amd · 2025-04-30

Hi @etiennemlb,

What you are seeing is a quirk in the roofline that will be fixed in a future release.

The numbers on the spec sheet assume no dual-issue for FP64 vector instructions. Typically this is the case, but there are a few cases where FP64 instructions can be dual-issued, resulting in higher throughput than what's listed on the spec sheet. Our roofline implementation happens to run into one of those cases, specifically the operation `x * x + 1.0`, where there is 1 source register and a constant.

The roofline code is available here: https://github.com/ROCm/rocm-amdgpu-bench/

