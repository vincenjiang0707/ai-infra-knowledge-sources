# [Issue #560] Is a roofline binary a possibilty for gfx908

source: https://github.com/ROCm/rocprofiler-compute/issues/560
state: closed | updated: 2025-02-18T21:02:53Z
labels: question, Under Investigation

## 正文

### Describe your question

Is the fact that roofline support is currently restricted to gfx90a and gfx942 impossible due to lack of a piece of HW support on gfx908 or is it simply not implemented at this time and could be in the future?


## 评论 (5)

### tcgu-amd · 2025-02-13

@IMbackK Thanks for reaching out! Technically, it is possible to implement roofline support for gfx908; unfortunately, it is currently not on our roadmap, and I can't really say if/when it will be..

### IMbackK · 2025-02-13

hi @tcgu-amd,

Thank you for the quick and frank response. Following up on that i have further question:
Where is the source corresponding to the binary artifacts found in: https://github.com/ROCm/rocprofiler-compute/tree/develop/src/utils/rooflines

### tcgu-amd · 2025-02-14

@IMbackK I believe they are found here https://github.com/rocm/rocm-amdgpu-bench

### tcgu-amd · 2025-02-18

Hey @IMbackK, is the above what you are looking for?

### IMbackK · 2025-02-18

yes, thank you.
