# [Issue #1511] Open Division Rule Clarification Request

source: https://github.com/mlcommons/inference/issues/1511
state: closed | updated: 2026-05-10T00:42:56Z
labels: Stale

## 正文

According to https://github.com/mlcommons/inference/blob/master/Submission_Guidelines.md#expected-time-to-do-benchmark-runs 

There is no constraint on the model used also except that the model must be trained on the dataset used in the corresponding MLPerf inference task.

By "the dataset used in the corresponding MLPerf inference task", does it mean the validation set used for accuracy testing in the closed division's same workload? It does not quite make sense to enforce this so that retraining of the open division model can be overfitted to the validation dataset.

If it means the original dataset used to train the closed division model, what would the submitters use if the original dataset is not publicly available? In this case this rule needs to be relaxed, such as the submitters can choose their own training dataset except the validation dataset and have to publish the dataset they used for training as a complementary material for open division submission.

## 评论 (3)

### nv-ananjappa · 2023-11-13

@mrmhodak We need to discuss this ASAP in WGM.

### psyhtest · 2023-11-13

>  except that the model must be trained 

I think "trained" should be replaced with "validated".

> such as the submitters can choose their own training dataset except the validation dataset and have to publish the dataset they used for training as a complementary material for open division submission.

Requiring to publish the training dataset may be a step too far?

### github-actions[bot] · 2026-05-10

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
