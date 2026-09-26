# [Issue #1230] Compliance TEST01 failure reasoning

source: https://github.com/mlcommons/inference/issues/1230
state: closed | updated: 2026-05-16T00:40:28Z
labels: Stale

## 正文

Compliance TEST01 can fail for some systems due to non-determinism and an additional [non-determinism test](https://github.com/mlcommons/inference/tree/master/compliance/nvidia/TEST01#non-determinism) can let this pass. In case of such a scenario, it would be good to add "accuracy_failure.txt" as a mandatory file along with the current mandatory ones- `baseline_accuracy.txt` and `compliance_accuracy.txt`, describing the reason of failure. 

## 评论 (1)

### github-actions[bot] · 2026-05-16

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
