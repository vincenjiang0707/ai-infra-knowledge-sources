# [Issue #1351] Inconsistency in the system desc required fields for cloud systems

source: https://github.com/mlcommons/inference/issues/1351
state: closed | updated: 2026-05-14T00:45:50Z
labels: Stale

## 正文

The [submission rules](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#57-system_desc_idjson-metadata) say that we should use `vcpu_count` for cloud systems but the [submission checker](https://github.com/mlcommons/inference/blob/master/tools/submission/submission_checker.py#L1260) is making `core_count` as mandatory. I think these should be made consistent. 


## 评论 (1)

### github-actions[bot] · 2026-05-14

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
