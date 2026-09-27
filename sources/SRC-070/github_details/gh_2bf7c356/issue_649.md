# [Issue #649] DeepEP v2 hybrid mode runs out of QPs with the recommended QPS configuration

source: https://github.com/deepseek-ai/DeepEP/issues/649
state: closed | updated: 2026-07-07T08:01:12Z
labels: 

## 正文

Hi,

When running DeepEP v2 in hybrid mode with the recommended QPS configuration from the following code:

https://github.com/deepseek-ai/DeepEP/blob/723716fc11ee44cbd87035fe9c3a360feca33528/deep_ep/buffers/elastic.py#L206

we encounter the following error:

<img width="805" height="187" alt="Image" src="https://github.com/user-attachments/assets/268be46c-1684-456d-9b2c-c7955bca239c" />

It seems that the process may be exhausting RDMA/NIC resources while creating QPs.

Could this issue be related to host-side RDMA driver or firmware configurations, such as BFREG/UAR limits or other mlx5 resource constraints?

Any suggestions or insights would be greatly appreciated. Thanks in advance!

## 评论 (0)
