# [Issue #1607] Proposal: Change all module/folder name from hyphen to underscore

source: https://github.com/mlcommons/inference/issues/1607
state: closed | updated: 2026-05-08T00:40:44Z
labels: inference v5.0, Stale

## 正文

Python module disallows usage of hyphen ('-') in module name, and it makes importing and module run very complicated. We should change the naming of folder and module (e.g. llama2-70b) to use underscore.
@pgmpablo157321 FYI


## 评论 (3)

### mrmhodak · 2024-04-02

Affects 3D-UNet, Llama2-70B, DLRM-v2
Leaving open for now, can affect workflow
@arjunsuresh and @gfursin : Any comments?

### gfursin · 2024-04-02

@nvzhihanj and @mrmhodak - we should be able to support such changes in CM. Please ping us if/when this change is done so that we could test all our workflows. Thanks! 

### github-actions[bot] · 2026-05-08

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
