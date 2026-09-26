# [Issue #344] NVL/RDMA tuning process (auto tune)

source: https://github.com/deepseek-ai/DeepEP/issues/344
state: closed | updated: 2026-09-01T10:38:07Z
labels: 

## 正文

Regarding the tuning process mentioned in README:
under: Auto-tuning on your cluster:

For better performance on your cluster, we recommend to run all the tests and use the best auto-tuned configuration. The default configurations are optimized on the DeepSeek's internal cluster

Can you elaborate on tuning process? 
for example, if i get a certain optimal nvl chunk size and rdma chunk size, should that go to into buffer.py -> get_dispatch/combine_config

Currently the number are for example:
Config(Buffer.num_sms, 24, 256, 6, 128)

What is each number here, and what is the relation to the nvl chunk numbers i see in test_internode.py results
Example from test_internode.py:
[tuning] Best dispatch (BF16): SMs 24, NVL chunk 12, RDMA chunk 32: 42.36 GB/s (RDMA), 138.25 GB/s (NVL)


## 评论 (1)

### sphish · 2025-08-05

You can refer to this.
https://github.com/deepseek-ai/DeepEP/blob/26cf250a3388c770ee628d2fd0271e1c6c52157a/tests/test_internode.py#L186
