# [Issue #212] How to inject XID errors using DCGMI

source: https://github.com/NVIDIA/DCGM/issues/212
state: open | updated: 2025-02-14T09:07:15Z
labels: 

## 正文

I am currently working with NVIDIA DCGM and would like to know how to inject XID errors using DCGMI. I have been looking through the documentation and some online resources, but I am still unclear on the exact steps and parameters required for this process.
Specifically, I am interested in the following:

- Steps to inject XID errors:

  - What are the exact steps to inject an XID error using DCGMI?
  - Are there any specific commands or parameters that need to be used?

- Example Commands:

  - Can you provide an example command to inject a specific XID error?
  - How can I verify that the error has been successfully injected?

## 评论 (2)

### nikkon-dev · 2025-02-14

@yangchou19,

Do you need to inject some specific XID? DCGM testing framework uses [this kernel](https://github.com/NVIDIA/DCGM/blob/master/testing/python3/apps/cuda_ctx_create/cuda_assert.cu) to generate XID 43.

If you inject an XID (or any other metric) into DCGM, it will be only placed into DCGM's internal cache and will not affect any other software. For example, such an XID will not trigger any NVML event.

If you still want to inject XID into DCGM, you may take a look at this [test](https://github.com/NVIDIA/DCGM/blob/master/testing/python3/tests/test_injection.py)

### yangchou19 · 2025-02-14

Thank you for the answer!
