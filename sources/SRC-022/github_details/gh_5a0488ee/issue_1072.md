# [Issue #1072] rccl_test reports those alarm always: Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd

source: https://github.com/ROCm/rccl/issues/1072
state: closed | updated: 2024-03-14T03:14:17Z
labels: 

## 正文

Hi Developer,

We running rccl_test, there are always such alarms, I have modified the marco but the alarms still happens.
Could you give me some advices why this alarms happens?
Thank you.

**#define NCCL_MAX_NTHREADS 512**

all_reduce_perf -g 1 -n 20 -b 1M -e 1G -f 2
#                                                       out-of-place                       in-place          
#       size         count      type   redop     time   algbw   busbw  error     time   algbw   busbw  error
#        (B)    (elements)                       (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 
Launch params (512, 1, 1) are larger than launch bounds (256) for kernel _Z9deltaKernIfLi512EEvPvS0_mPd please add __launch_bounds__ to kernel define or use --gpu-max-threads-per-block recompile program ! 

## 评论 (2)

### BertanDogancay · 2024-03-12

NCCL_MAX_NTHREADS should not be more than 256 as can be seen from the logs. Usually global variables defined by RCCL should 't be modified. They are either set to max or specifically tuned for optimization.

### shanleo2024 · 2024-03-13

> NCCL_MAX_NTHREADS should not be more than 256 as can be seen from the logs. Usually global variables defined by RCCL should 't be modified. They are either set to max or specifically tuned for optimization.

Thank you for your reminder, I have figured out the root cause of this warning.
I tested with rccl_test, in rccl_test source code, the following function deltaKern use the dim 512, which is bigger than the default threads definde by NCCL_MAX_NTHREADS, so just modify the second param to 256, the warning dispared.

The original source code:
testResult_t CheckDelta(void* results, void* expected, size_t count, ncclDataType_t type, double* devmax) {
  switch (type) {
#if NCCL_MAJOR >= 2 && RCCL_BFLOAT16 == 1
    case ncclBfloat16:
      hipLaunchKernelGGL((deltaKern<rccl_bfloat16, 512>), dim3(1), dim3(**512**), 0, 0, results, expected, count, devmax); break;
#endif

The modified source code:
testResult_t CheckDelta(void* results, void* expected, size_t count, ncclDataType_t type, double* devmax) {
  switch (type) {
#if NCCL_MAJOR >= 2 && RCCL_BFLOAT16 == 1
    case ncclBfloat16:
      hipLaunchKernelGGL((deltaKern<rccl_bfloat16, 512>), dim3(1), dim3(**256**), 0, 0, results, expected, count, devmax); break;
#endif
