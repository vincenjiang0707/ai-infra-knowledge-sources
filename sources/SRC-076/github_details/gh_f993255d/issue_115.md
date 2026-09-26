# [Issue #115] Max Perf / Speedup Modeling

source: https://github.com/ScalingIntelligence/KernelBench/issues/115
state: open | updated: 2026-01-02T16:46:32Z
labels: 

## 正文

Starting this issue to gather ideas and start working on this 

For a given KernelBench problem, it would be very nice to model the maximum speedup possible / speed-of-light  (to avoid hacking, aka unrealistic speedups, and understand the limit of max speedup for a problem on specified hardware).

Take in 
* Pytorch problem (KernelBench problem style) 
* Hardware Specs (which we outlined in the prompts folder for various hardware), mostly peak FLOPs and memory bandwidth

Concretely, this might involve modeling a roofline model using profiler tools.

## 评论 (2)

### aryatschand · 2026-01-01

Definitely agree with having some roofline-type model to set an upper bound performance. The easiest way to do it is just get the roofline for the gpu architecture and use ncu profiling to plot the generated kernel (I think [this paper](https://arxiv.org/pdf/2511.15915) did it). Taking this a step further, maybe we can use properties of the workload (data locality, achievable tensorcore usage, etc.) to make a more realistic upper bound like the [orojenesis](https://people.csail.mit.edu/emer/media/papers/2024.06.isca.orojenesis.pdf) paper. Curious to hear thoughts from others on how to best implement this!

### aryatschand · 2026-01-01

Also some other problems that I've been interested in that take our work in kernel optimization a step further and hopefully set the stage for robust AI compilers!

- fusing kernels and writing megakernels
- benchmarking and optimizing communication collective kernels
- numerically stable kernels (to improve fine tuning performance)

