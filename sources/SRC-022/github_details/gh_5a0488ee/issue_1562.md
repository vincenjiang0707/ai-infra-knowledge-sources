# [Issue #1562] [Issue]: Two half-chunk allreduce takes Twice the time of one full-chunk tensor allreduce

source: https://github.com/ROCm/rccl/issues/1562
state: closed | updated: 2025-03-13T00:19:53Z
labels: Under Investigation

## 正文

### Problem Description

Hi RCCL Team,

I am doing some benchmarking on AllReduce. My settings are as follows:

case1: 
Baseline (single chunk tensor): size 6400*6400. bf16/fp16. doing allreduce over 8 MI300 within a node. which takes around 0.1 ms. Pseudocode as below:
```
rows = 6400
cols = 6400
inputs = torch.ones((rows,cols), dtype=torch.bfloat16).cuda(int(rank))
for _ in range(trials):
    dist.all_reduce(inputs)
```


case2: 
two-split ( two chunk tensor partitions): here we have 2 chunks of tensors, where each size is 3200*6400, bf16/fp16. For each half tensor, we doing allreduce over 8 MI300 within a node. which takes around 0.22 ms. Pseudocode as below:

```
rows = 6400
cols = 6400
new_input = torch.ones((rows,cols), dtype=torch.bfloat16).cuda(int(rank))
input1, input2 = new_input.chunk(2)
for _ in range(trials):
    dist.all_reduce(input1)
    dist.all_reduce(input2)
```



In theory, case1 and case 2 should have similar allreduce time, since they are communicating same total amount of data. Given kernel launching overhead of 1 (case1) vs. 2 (case2), we saw case2 allreduce is 20% slower than case 1 on Nvidia H100s, which kind of make sense. However, on MI300s, the time of case2 is **doubled** compared with case1. 

A full python script can be found here: https://gist.github.com/GuanhuaWang/418cecedb7150304475918444c18bd1a

### Operating System

Ubuntu 22.04.5 LTS

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

AMD MI300X

### ROCm Version

6.2.3.60203-124~22.04

### ROCm Component

_No response_

### Steps to Reproduce

Using docker image: `rocm/pytorch:latest`

Pytorch version: `2.4.0a0+git3ae0438`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

RCCL ver `2.20.5.60201-112~20.04`

## 评论 (7)

### ppanchad-amd · 2025-02-21

Hi @GuanhuaWang. Internal ticket has been created to investigate your issue. Thanks!

### huanrwan-amd · 2025-02-21

Hi @GuanhuaWang , Thanks for posting questions. 
To make sure the hardware is correct and the driver are updated:

1.  Can you please provide the driver version of the machine?
`dkms status`

2. And can you please also provide the rccl allreduce tests result using: https://github.com/ROCm/rccl-tests
`$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 8` 
The tensor size in the scripts falls in the range of the test above. 

### GuanhuaWang · 2025-02-22

Hi @huanrwan-amd and @ppanchad-amd, 

thx for the timely response. Please find the results as below 
  
> 1. dkms status

`amdgpu, 6.8.5-2038383.20.04, 5.15.0-1078-azure, x86_64: installed`

> 2. And can you please also provide the rccl allreduce tests result using: https://github.com/ROCm/rccl-tests
>    `$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 8`

below is the results:

```
# nThread 1 nGpus 8 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
rccl-tests: Version :+
# Using devices
#   Rank  0 Pid  56417 on c42f4555f685 device  0 [0002:00:00.0] AMD Instinct MI300X VF
#   Rank  1 Pid  56417 on c42f4555f685 device  1 [0003:00:00.0] AMD Instinct MI300X VF
#   Rank  2 Pid  56417 on c42f4555f685 device  2 [0004:00:00.0] AMD Instinct MI300X VF
#   Rank  3 Pid  56417 on c42f4555f685 device  3 [0005:00:00.0] AMD Instinct MI300X VF
#   Rank  4 Pid  56417 on c42f4555f685 device  4 [0006:00:00.0] AMD Instinct MI300X VF
#   Rank  5 Pid  56417 on c42f4555f685 device  5 [0007:00:00.0] AMD Instinct MI300X VF
#   Rank  6 Pid  56417 on c42f4555f685 device  6 [0008:00:00.0] AMD Instinct MI300X VF
#   Rank  7 Pid  56417 on c42f4555f685 device  7 [0009:00:00.0] AMD Instinct MI300X VF
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    45.92    0.00    0.00      0    46.12    0.00    0.00      0
          16             4     float     sum      -1    48.87    0.00    0.00      0    48.60    0.00    0.00      0
          32             8     float     sum      -1    47.33    0.00    0.00      0    48.16    0.00    0.00      0
          64            16     float     sum      -1    50.03    0.00    0.00      0    55.74    0.00    0.00      0
         128            32     float     sum      -1    50.35    0.00    0.00      0    50.42    0.00    0.00      0
         256            64     float     sum      -1    51.52    0.00    0.01      0    51.64    0.00    0.01      0
         512           128     float     sum      -1    52.16    0.01    0.02      0    50.40    0.01    0.02      0
        1024           256     float     sum      -1    52.41    0.02    0.03      0    55.34    0.02    0.03      0
        2048           512     float     sum      -1    56.85    0.04    0.06      0    61.02    0.03    0.06      0
        4096          1024     float     sum      -1    54.51    0.08    0.13      0    54.52    0.08    0.13      0
        8192          2048     float     sum      -1    50.05    0.16    0.29      0    50.22    0.16    0.29      0
       16384          4096     float     sum      -1    54.82    0.30    0.52      0    52.96    0.31    0.54      0
       32768          8192     float     sum      -1    53.79    0.61    1.07      0    53.08    0.62    1.08      0
       65536         16384     float     sum      -1    55.40    1.18    2.07      0    52.54    1.25    2.18      0
      131072         32768     float     sum      -1    66.85    1.96    3.43      0    69.47    1.89    3.30      0
      262144         65536     float     sum      -1    68.55    3.82    6.69      0    63.73    4.11    7.20      0
      524288        131072     float     sum      -1    66.14    7.93   13.87      0    68.39    7.67   13.42      0
     1048576        262144     float     sum      -1    65.38   16.04   28.07      0    62.18   16.86   29.51      0
     2097152        524288     float     sum      -1    68.80   30.48   53.34      0    66.96   31.32   54.81      0
     4194304       1048576     float     sum      -1    65.52   64.01  112.03      0    66.36   63.21  110.61      0
     8388608       2097152     float     sum      -1    88.10   95.22  166.63      0    90.19   93.01  162.77      0
    16777216       4194304     float     sum      -1    152.7  109.84  192.22      0    159.0  105.53  184.67      0
    33554432       8388608     float     sum      -1    244.8  137.06  239.86      0    254.4  131.88  230.79      0
    67108864      16777216     float     sum      -1    431.9  155.39  271.93      0    440.7  152.29  266.50      0
   134217728      33554432     float     sum      -1    801.4  167.47  293.07      0    811.1  165.48  289.60      0
# Errors with asterisks indicate errors that have exceeded the maximum threshold.
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 54.8575 
```

```bash
> Hi [@GuanhuaWang](https://github.com/GuanhuaWang) , Thanks for posting questions. To make sure the hardware is correct and the driver are updated:
> 
> 1. Can you please provide the driver version of the machine?
>    `dkms status`
> 2. And can you please also provide the rccl allreduce tests result using: https://github.com/ROCm/rccl-tests
>    `$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 8`
>    The tensor size in the scripts falls in the range of the test above.
```



### functionstackx · 2025-03-08

@GuanhuaWang it makes sense that 2 "half-chunks" take more time than one "full-chunk" as networking algoBW is depend on msg size

### huanrwan-amd · 2025-03-10

Hi @GuanhuaWang , Based on the test results, it appears your machine is functioning correctly. Comparing NCCL and RCCL directly is challenging due to differences in hardware and software. 

On the software side, RCCL integrates other collective communication libraries, such as msccl, to enhance performance for specific message sizes. For more details, you can check out this link: https://github.com/ROCm/rccl/pull/1231


### ashwinma · 2025-03-11

Please make sure you have turned NUMA auto balancing off and try again

https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#disable-numa-auto-balancing

### GuanhuaWang · 2025-03-13

> Please make sure you have turned NUMA auto balancing off and try again
> 
> https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#disable-numa-auto-balancing

Hi @ashwinma , @huanrwan-amd @OrenLeung ,

Thanks for all your help and timely response. @ashwinma suggestions on disable NUMA balancing seems significantly improve 2 half chunk data transfer throughput. What I saw is throughput improvement of 50% for half-half two allreduce cases, which now on par with Nvidia's NCCL stats(i.e. 80% tput of single full chunk transfer). 

Will to more end-to-end training benchmarking, but I think we can close this simple allreduce benchmark issue now.

Really appreciated!


