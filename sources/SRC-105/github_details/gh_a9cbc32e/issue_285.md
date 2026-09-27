# [Issue #285] Enable Mi300 Roofline

source: https://github.com/ROCm/rocprofiler-compute/issues/285
state: closed | updated: 2025-03-26T10:46:52Z
labels: enhancement, Roofline, Customer Req

## 正文

**Is your feature request related to a problem? Please describe.**
Both national labs, internal customers, and others are asking for a Mi300 based roofline analysis. In v2.0 release this was temporarily disabled.

The microbenchmark has been adjusted with help from @rwvo . However, I still want to stress test the arithmetic intensity calculation and put the model through the wringer with some test applications.

**Describe the solution you'd like**

1. Start by working with @nwolfey21 to check in on status. His expertise could help inform any adjustments required on arithmetic intensity
2. Initial tests on the beta-version, iterate, and adjust
3. Select test suite and verify results



## 评论 (21)

### nwolfey21 · 2024-02-29

Happy to help. Let me know what you need.
I'm good at breaking things ;)

### skyreflectedinmirrors · 2024-03-01

Add me to this as well.  @coleramos425 you want to set something up ?

### coleramos425 · 2024-03-01

I'll add you to the meeting @skyreflectedinmirrors 

### lizamd · 2024-06-04

hi @coleramos425 is mi300 roofline enabled in omniperf? get similar request, thanks!

### coleramos425 · 2024-06-04

@lizamd we're still developing roofline support. If you ping me on Teams I can provide more detail.

### lizamd · 2024-06-04

cool, thanks for the quick response, will ping you!


### itej89 · 2024-07-15

Hi @coleramos425, I am also trying to use roofline for bench-marking llama.cpp. Any workarounds or temporary solutions to get it to work would be of great help. Thanks in advance!!

### coleramos425 · 2024-08-16

# Update 8/16
Just received a beta version of microbenchmark from Rene. @cfallows-amd will be working to validate that work while myself and others work on adjustments to the arithmetic intensity calculation

### yiakwy-xpu-ml-framework-team · 2025-03-17

@lizamd @coleramos425  Roofline is still not enabled by default. Is there any udpates ?

```
   INFO    |-> [rocprof] File '/workspace/benchmark/kernels/fused_moe_triton/workloads/moe_align_1_to_16384x256/MI300/timestamps.csv' is generating
   INFO    |-> [rocprof] 
   INFO [roofline] Roofline temporarily disabled in MI300
```

SDK version : 6.3.3
rocProfiler version : 3.0.0


### yiakwy-xpu-ml-framework-team · 2025-03-19

@rwvo @coleramos425 Hi, Mi300X/Mi300A is an essentailly a multi-die chip. L2 cache Fabric will play a great important role and workload among XCDs will be also important.

And our rocProfiler-compute actually does not relfect the fact. Is there any plan working on this problem ?

### rwvo · 2025-03-19

@yiakwy-xpu-ml-framework-team I don't work on this project; I only made a small contribution a while ago. I was under the impression that MI300 is supported by now, but I'm not sure. @cfallows-amd can probably answer your question.

Rooflines won't show the workload distribution among XCD's though.

### yiakwy-xpu-ml-framework-team · 2025-03-19

Let's work on it! @rwvo 

### yiakwy-xpu-ml-framework-team · 2025-03-19

Previously I have experiences working closely with Graphcore Profiler team (Popvision) . We used sqllite to record data and rebuilt model by walking program tree. Let me know if I can help.

For visualization part, we need a multi-die tab to show the hotkeys (with color) of data visiting pressure.

I aso  recommend our team to add sample wave computing in 2-D chart to wishlist : x is the program steps (I guess we can obtain this with LLVM API), y is threads numbers.

Also need to track how the inputs flow through porgram. I know we are not data flowing software architecture. But it really help. We can do it first for HipGraph, then general program later.

For data sampling, we need rebuild AMD chip models, program structures, waves structures...


### yiakwy-xpu-ml-framework-team · 2025-03-19

I would like to hear some feedback from core team.

### rwvo · 2025-03-19

@yiakwy-xpu-ml-framework-team Ping me on Teams (you should be able to see my full name here, and then find me on Teams), and I can get you in touch with the right people.

### skyreflectedinmirrors · 2025-03-19

>Hi, Mi300X/Mi300A is an essentailly a multi-die chip. L2 cache Fabric will play a great important role and workload among XCDs will be also important.

I'm not sure that this issue (specifically: on roofline support for MI300) is the relevant place to discuss, tbh.  I suspect that this issue can actually be _closed_, because AFAIK, roofline support on MI300 is already in develop, e.g.:

https://github.com/ROCm/rocprofiler-compute/blob/develop/src/utils/rooflines/roofline-ubuntu20_04-mi300-rocm6

I am not sure how this corresponds to the versions from your comment however.  I think it's perfectly reasonable to ask about the LLC/Fabric support on MI300 in a new issue however.

(cc: @feizheng10)

### rwvo · 2025-03-19

@skyreflectedinmirrors Indeed, this doesn't seem the right place to discuss the topics @yiakwy-xpu-ml-framework-team brings up; that's why I asked them to ping me on Teams. I assumed they were internal AMD and could find me on Teams, but that may not be the case.

Edit: their profile says they are at Graphcore in Bristol, so not AMD. I'll reach out.

### rwvo · 2025-03-19

@yiakwy-xpu-ml-framework-team: please open a new issue to discuss feature requests/suggestions.

### yiakwy-xpu-ml-framework-team · 2025-03-26

@rwvo sorry for late reply. I was working on this aritcle last week : 

https://huggingface.co/blog/yiakwy-xpu-team/efficient-moe-align-sort-design-for-sglang

As far as I understand, it is first article which used **rocProfiler-compute** to benchmark a newly proposed (by us) AMD friendly CUDA kernel algorithm in an open source community.

I did use MI300X/MI300A extensively. They are good machines I believe strong sales is going to be happen in this , and next quarter.

So it is worthy of time and effort to invest in ROCm tech once again.

I really appreciated AMD coorporate-wise open source strategy. So we can be collabrating on the open source software!



### yiakwy-xpu-ml-framework-team · 2025-03-26

> [@yiakwy-xpu-ml-framework-team](https://github.com/yiakwy-xpu-ml-framework-team): please open a new issue to discuss feature requests/suggestions.

Yep, I will do it tonight.

### yiakwy-xpu-ml-framework-team · 2025-03-26

Hi @coleramos425 is the roofline model resolved in the new (upcoming) release ? Should I try it ?
