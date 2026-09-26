# [Issue #1520] Open division rule on validation dataset is confusing

source: https://github.com/mlcommons/inference/issues/1520
state: closed | updated: 2026-05-10T00:42:54Z
labels: Stale

## 正文

https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc#412-relaxed-constraints-for-the-open-division

Rule 2 states that: 

> The accuracy dataset must be the same as used in an existing Closed benchmark, or must be pre-approved and added to the following list: ImageNet 2012 validation dataset for Image Classification; COCO 2017 validation dataset for Object Detection. From v3.0, if a submitter provides any results with any models trained on a pre-approved dataset, the submitter must also provide at least one result with the corresponding Closed model trained (or finetuned) on the same pre-approved dataset, and instructions to reproduce the training (or finetuning) process.

There are some problems with this rule:

- The sentences mix up the validation dataset with the training dataset. It is not clear in some places how or why validation/training dataset would be applicable in that sentence.
- Probably the rule introduced for v3.0 could be simplified to be generic across all benchmarks that will be in 4.0.

I am requesting @psyhtest and @rnaidu02 to help in formulating a simpler rule 2 for Open.

## 评论 (2)

### nv-ananjappa · 2023-11-14

Based on the WGM discussion, @psyhtest will look at removing/simplifying the "v3.0" sentence. I will try to add a new rule to cover the training dataset. Discussion on these changes can be done in next week's WGM.

### github-actions[bot] · 2026-05-10

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
