# [Issue #1137] [Issue]: Algorithm and protocol selection

source: https://github.com/ROCm/rccl/issues/1137
state: closed | updated: 2024-06-10T06:05:40Z
labels: 

## 正文

### Problem Description

Want to check the Algorithm and protocol  being selected for all_reduce_perf. Uncommented line 1520 in enqueue.cc, but none print statements were seen. How do we check the algorithm and protocol selection

### Operating System

SLES15.4

### CPU

AMD EPYC 7A53

### GPU

AMD Instinct MI250

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (16)

### tks2004 · 2024-04-10

Tried modifying enqueue.cc at line no: 1273) as well. did not get the algo or communication protocol

### wenkaidu · 2024-04-10

How many logical GPUs on single node? 8 or 16? If there are 16 GPUs, it is possible MSCCL path is taken.

### tks2004 · 2024-04-11

It is 4 GPUs and was run using all 8 GCD. Message sizes are from 2MB to 2GB;
NCCL INFO Connected all trees
NCCL INFO threadThresholds 8/8/64 | 128/8/64 | 256 | 256
NCCL INFO 8 coll channels, 0 nvls channels, 8 p2p channels, 1 p2p channels per peer
NCCL INFO MSCCL: No external scheduler found, using internal implementation
NCCL INFO Using MSCCL files from /opt/rocm-6.0.0/lib/../share/rccl/msccl-algorithms
NCCL INFO MSCCL: Initialization finished, localSize 400



### wenkaidu · 2024-04-11

There are 2 possibilities:
1. NCCL_DEBUG_SUBSYS=INIT,TUNING is missing from environment;
2. Default RCCL build from ROCm release is used. Please commit your change and build, then confirm commit hash matching "RCCL version" in log;

### haripriyaayyalasomayajula · 2024-04-29

@tks2004  - Did you get a chance to implement @wenkaidu's suggestions?

### tks2004 · 2024-04-30

@haripriya-amd, rccl-tests are failing if CUSTOM_RCCL_LIB is used. 

### wenkaidu · 2024-05-01

Can you share failure message?

### tks2004 · 2024-05-08

Was able to work around this issue. How does MSCCL is selected, I now dont see it being selected,

### wenkaidu · 2024-05-08

MSCCL is only supported on very limited hardware platforms. It also only supports limited collectives and data sizes. It will be automatically activated when possible.

### tks2004 · 2024-05-08

Is there an option to force use MSCCL algorithms 

### wenkaidu · 2024-05-08

Can you share more details on targeted hardware platform and application? MSCCL algorithm only works well when GPU have all to all connectivity. Currently it only supports small data sizes in one GPU per process mode.

### tks2004 · 2024-05-08

This is on MI250x (4 GPUs; 8GCDs) using Slingshot interconnect. Had used latest rccl, rccl-tests and aws-ofi-rccl from master branch. 

### wenkaidu · 2024-05-08

MSCCL can be force enabled by RCCL_MSCCL_FORCE_ENABLE=1:
https://github.com/ROCm/rccl/blob/develop/src/misc/msccl/msccl_lifecycle.cc#L26
This will pickup xmls for 8 GPUs. You may need to adjust min/max bytes to see what data sizes it may help.

### wenkaidu · 2024-05-08

Please use rccl/rccl-tests develop branches, not master which may not be updated promptly.

### tks2004 · 2024-05-22

RCCL_MSCCL_FORCE_ENABLE=1 did not force MSCCL algorithm

### tks2004 · 2024-06-10

Was able to get the protocol and algorithm info.
