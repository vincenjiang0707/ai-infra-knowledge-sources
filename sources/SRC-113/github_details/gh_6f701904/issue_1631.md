# [Issue #1631] host_processor_vcpu_count in <system_desc_id>.json

source: https://github.com/mlcommons/inference/issues/1631
state: closed | updated: 2026-05-07T00:40:01Z
labels: Stale

## 正文

According to https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#57-system_desc_idjson-metadata it's required to provide field host_processor_vcpu_count.

I see that relevant checks are missing in https://github.com/mlcommons/inference/blob/master/tools/submission/submission_checker.py so the submitter get 
`submission_checker.py:3240 WARNING] <redacted>, field host_processor_vcpu_count is unknown`.

My proposal is to remove `host_processor_vcpu_count` from the submission rules because this rule is not enforced anyway. In inference_results_v3.1 this field is present only in `closed/Intel-HabanaLabs/systems/HLS-Gaudi2-PT.json`.

## 评论 (3)

### szutenberg · 2024-02-20

If we provide only host_processor_vcpu_count instead of host_processor_core_count then submission checker fails:
```
submission_checker.py:3220 ERROR] <REDACTED>, field host_processor_core_count is missing
submission_checker.py:3240 WARNING] <REDACTED>, field host_processor_vcpu_count is unknown
```

### arjunsuresh · 2024-02-20

A related issue: https://github.com/mlcommons/inference/issues/1351

### github-actions[bot] · 2026-05-07

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
