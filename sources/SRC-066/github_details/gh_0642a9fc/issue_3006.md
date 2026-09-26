# [Issue #3006] [BUG] Cute example crashes

source: https://github.com/NVIDIA/cutlass/issues/3006
state: open | updated: 2026-09-13T03:12:42Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CUTLASS C++

## 正文

### Which component has the problem?

CUTLASS C++

### Bug Report

**cute example crashes**

Cute example  "examples/cute/tutorial/blackwell/cute_tutorial_02_mma_tma_sm100" in crashes with abort message. This is on B200 (SM100) GPU. 

**Steps/Code to reproduce bug**

 ./cute_tutorial_02_mma_tma_sm100

host_tensor_A:  ptr[16b](0x7894690ee010) o (512,256):(256,_1)
host_tensor_B:  ptr[16b](0x789468d7f010) o (1024,256):(256,_1)
host_tensor_C:  ptr[32b](0x789460d4a010) o (512,1024):(1024,_1)
terminate called after throwing an instance of 'thrust::THRUST_300001_SM_900_NS::system::system_error'
  what():  parallel_for failed: cudaErrorNoKernelImageForDevice: no kernel image is available for execution on the device
Aborted (core dumped)

**Expected behavior**
It should not abort.

**Environment details (please complete the following information):**
 - Cloud.

**Additional context**
Add any other context about the problem here.


## 评论 (5)

### hwu36 · 2026-02-06

could you please provide your command line to build and run the cute example?

### bikshand · 2026-02-06

claude-code fixed it. don't know what is the fix, but it works now.

### github-actions[bot] · 2026-03-08

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-06-06

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### XFDG · 2026-09-13

I reran the reported cute_tutorial_02_mma_tma_sm100 example from current main (147295a3d4b75f3aeff247c25b8927cea9a7006a) on an NVIDIA B200 with CUDA 13.1, compiling explicitly for sm_100a. It now builds and runs successfully, with an infinity-norm difference of 0 and 'Execution is successful.' The original no-kernel-image failure appears resolved.
