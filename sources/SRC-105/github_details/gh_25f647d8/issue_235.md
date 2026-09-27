# [Issue #235] Some XID errors (e.g. XID 62) are not exported via DCGM_FI_DEV_XID_ERRORS metric

source: https://github.com/NVIDIA/DCGM/issues/235
state: open | updated: 2025-06-09T17:22:41Z
labels: 

## 正文

hi guys,
We found that some GPU XID errors (such as XID 62 and potentially others) are not being reported through the DCGM_FI_DEV_XID_ERRORS metric when using dcgm-exporter. According to the documentation and metric design, we expect all XID errors should be exported via this metric for proper hardware monitoring and alerting.
**Expected behavior:**
All XID errors, including XID 62, should be exported and visible in the value of DCGM_FI_DEV_XID_ERRORS in dcgm-exporter metrics output.
**Actual behavior:**

![Image](https://github.com/user-attachments/assets/bba8946c-23e4-4084-97df-0ae25145ed22)

There is only one metric as below:
`DCGM_FI_DEV_XID_ERRORS{err_code="45", err_msg="Preemptive cleanup, due to previous errors -- Most likely to see when running multiple cuda", job="dcgm-exporter"}`
**Steps to reproduce**:
Cause or wait for an XID 62 error on a GPU.
Observe that the error appears in dmesg logs.
Query the DCGM_FI_DEV_XID_ERRORS metric via dcgm-exporter — the metric does not reflect the occurrence of this error.
**Environment:**
dcgm-exporter version: dcgm-exporter-3.3.7-3.5.0-ubuntu20.04
Driver version: 550.127.08
CUDA Version: 12.4 
BTW, this issue occurs on various GPU models.

## 评论 (1)

### bstollenvidia · 2025-06-09

Use a DCGM Exporter that is version 4.0.0 or higher:
https://docs.nvidia.com/datacenter/dcgm/latest/release-notes/changelog.html

_/dev/kmsg is now parsed to detect some XIDs that were previously undetected._
