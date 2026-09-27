# [Issue #656] [DeepEPv2] test_agrs.py failed due to CUDA_ERROR_NOT_SUPPORTED, operation not supported

source: https://github.com/deepseek-ai/DeepEP/issues/656
state: open | updated: 2026-07-13T06:44:54Z
labels: 

## 正文

Hi, 

we tested the test_agrs.py and found it will be failed on H20:

-- Process 0 terminated with the following error:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torch/multiprocessing/spawn.py", line 87, in _wrap
    fn(i, *args)
  File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/DeepEP/tests/elastic/test_agrs.py", line 125, in test
    buffer.destroy_agrs_session()
  File "/usr/local/lib/python3.12/dist-packages/deep_ep/buffers/elastic.py", line 503, in destroy_agrs_session
    self.runtime.destroy_agrs_session()
RuntimeError: CUDA driver exception (/workspace/DeepEP/csrc/kernels/backend/cuda_driver.cu:51): 801 (CUDA_ERROR_NOT_SUPPORTED, operation not supported)

https://github.com/deepseek-ai/DeepEP/blob/d4f41e4e93602a15e95f55f6ee8df8f1aaa0e4bb/csrc/kernels/backend/cuda_driver.cu#L51



## 评论 (0)
