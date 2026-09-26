# [Issue #68] [Feature]: Metrics accessor for constructing a roofline model

source: https://github.com/ROCm/rocprofiler-sdk/issues/68
state: closed | updated: 2025-08-07T18:25:40Z
labels: Under Investigation, Feature Request

## 正文

### Suggestion Description

Hello all, 

I have been playing with rocprofv3 to construct different roofline models of algorithms on various recent GPUs (mi250 and mi300). 
While I can place an algorithm, or part of it, on such graph by getting the FETCH_SIZE, WRITE_SIZE, TOTAL_16_OPS, TOTAL_32_OPS, TOTAL_64_OPS metrics; I struggle getting the necessary information to get a measure of the peak performance for 16, 32, and 64 precision operations alongside the max bandwidth for DRAM, L1, and L2 caches. I know that the theoretical values of these metrics are published but I would want to get a measure of them on the devices. 

For example, with ncu , I can gather the "derived__sm__sass_thread_inst_executed_op_hfma_pred_on_x2", "derived__sm__sass_thread_inst_executed_op_hfma_pred_on_x4", and "sm__cycles_elapsed.avg.per_second" to compute the peak performance for half precision. 

What would be the metrics that I can gather from rocprofv3 to get the peak measurements I have mentioned ? What would be the equation to compute the peak performance from these metrics ? Would you add derived metrics like TOTAL_64_OPS to rocprofv3 to provide users the peak measurements ?

Thank you in advance for your time!

### Operating System

_No response_

### GPU

MI200 MI300

### ROCm Component

_No response_

## 评论 (4)

### ppanchad-amd · 2025-05-26

Hi @ABardakoff. Internal ticket has been created to assist with your questions. Thanks!

### huanrwan-amd · 2025-07-18

Hi @ABardakoff , Sorry of the late reply. 

First of all, have you check the available pmc on your hardward with rocprofv3-avail? 
[https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/amd-mainline/how-to/using-rocprofv3-avail.html](url)

### ABardakoff · 2025-07-22

Hello @huanrwan-amd, No worry ! 

Of course I did ! 
My goal is with scripting be enable to get enough info through rocprofv3 to draw roofline models of kernels delimited with ROCTx markers. 
I will probably rephrase my question, I would like to get out of the profiler: 
_Metrics that will exists on recent and future hardware to place them in a roofline model, 
_If possible, a measure of the peak performance of the current device without benchmarking a specific kernel / applications. 

So far I do something like: 
`
metrics = {
    "FETCH" : "FETCH_SIZE",
    "WRITE" : "WRITE_SIZE",
    "OP16" : "TOTAL_16_OPS",
    "OP32" : "TOTAL_32_OPS",
    "OP64" : "TOTAL_64_OPS",
    "BANDWIDTH": "BANDWIDTH_EA"
}

for metric_name, metric_tag in metrics.items():
  command  = ("rocprofv3_path --marker-trace --pmc metric_tag -d o_dir -o o_name -- my_kernel"
`
But this approach:
_Hangs sometime for no obvious reason to me, 
_Limited: No data about l1/l2 caches, peak of the card, ai related performance, 
_Tedious: For each of the metrics 2/3 files are created, and while I have tried to combine them in one run: that fails. I understand the profiler has limitations by the fact that the counters need to be captured in one go, but it is not obvious to me which one are "compatible", and why TOTAL_16_OPS is not compatible with TOTAL_32_OPS for example,
_Seems like more a hack to me than the correct way to do things.

So I was wondering if you had a better and more robust approach to 1) measure the arithmetic intensity (dram/l1/l2) of a given kernel, 2) the performance (double/single/half/AI specific precision) of a given kernel, 3) the peak bandwidth performance (dram/l1/l2), and 4) the peak computational (double/single/half/AI specific precision) performance the card. 

Thank you in advance for your help and time. 

Best, 

Alexandre

### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/132
