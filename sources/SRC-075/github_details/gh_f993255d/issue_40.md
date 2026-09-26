# [Issue #40] Improved Problem Tensor Size

source: https://github.com/ScalingIntelligence/KernelBench/issues/40
state: closed | updated: 2025-10-28T07:58:55Z
labels: 

## 正文

KernelBench problems include tensor sizes in the problem definition.

Some of those are too small right now. This has benchmarking implications: if the time to process a tensor is not significant compared to the kernel launch overhead, then CPU overhead might dominate.

Thanks to Tri Dao and the Kevin team for the suggestion.

I suggest we increase the tensor size for problems that suffer from this problem. 

## 评论 (1)

### AffectionateCurry · 2025-10-28

Problems from all levels were timed and the tensor sizes for these problems were tweaked until all problems fell in the range of 1ms - 15ms of wall clock runtime. This was to ensure that kernel launch overhead didn't dominate the runtime of kernel as kindly pointed out by Tridao. 

More about this can be read in the KernelBench v0.1 blog:

https://scalingintelligence.stanford.edu/blogs/kernelbenchv01/
