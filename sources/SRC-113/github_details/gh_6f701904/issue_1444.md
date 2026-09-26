# [Issue #1444] Optional field for closed division marked as required

source: https://github.com/mlcommons/inference/issues/1444
state: closed | updated: 2026-05-12T00:39:44Z
labels: Stale

## 正文

```
[2023-07-16 01:20:48,197 submission_checker.py:2872 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field host_memory_configuration requires a meaningful response but is empty
[2023-07-16 01:20:48,197 submission_checker.py:2872 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field host_networking requires a meaningful response but is empty
[2023-07-16 01:20:48,197 submission_checker.py:2872 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field host_networking_topology requires a meaningful response but is empty
[2023-07-16 01:20:48,197 submission_checker.py:2872 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field accelerator_host_interconnect requires a meaningful response but is empty
[2023-07-16 01:20:48,197 submission_checker.py:2872 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field accelerator_interconnect requires a meaningful response but is empty
[2023-07-16 01:20:48,197 submission_checker.py:2872 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field cooling requires a meaningful response but is empty
[2023-07-16 01:20:48,198 submission_checker.py:2865 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field host_networking_card_count is missing
[2023-07-16 01:20:48,198 submission_checker.py:2865 ERROR] closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx1_TRT, field system_type_detail is missing 
```
These field are reported as missing by the submission checker.

## 评论 (2)

### arjunsuresh · 2023-07-19

@nvyihengz All these fields are mandatory as per the rules [here](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#system_desc_id-json-metadata). Except [system_type_detail](https://github.com/mlcommons/policies/pull/151/files) all others need a meaningful response. But if any field does not make sense on a given system, "N/A" is enough to satisfy the submission checker. 

### github-actions[bot] · 2026-05-12

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
