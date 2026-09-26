# [Issue #1675] Submission checker forces to have “gptj-99” and “gpt-99.9” in the code dir

source: https://github.com/mlcommons/inference/issues/1675
state: closed | updated: 2026-05-05T00:38:30Z
labels: Stale

## 正文

It ends up that we have even three identical directories (see NVIDIA submission) which does not help with the review and understanding the repo by someone not involved in the WG.

Solution:
there should be one directory per model

if needed, the submitter can create 99 & 99.9 directories

Now:
- gptj-99.9
- gptj-99
- gptj

After:
- gptj

After - optionally, directories per accuracy category:
- gptj/99.9
- gptj/99

## 评论 (2)

### arjunsuresh · 2024-04-10

I think we can discuss further on this. The problem with the proposal is that we no longer have the same model names inside the results/measurements directory (like [this](https://github.com/mlcommons/inference_results_v4.0/tree/main/closed/NVIDIA/measurements/DGX-H100_H100-SXM-80GBx1_TRT) ) and the ones inside the code directory. Also to avoid duplicates in the code directory we can have softlinks as done [here](https://github.com/mlcommons/inference_results_v4.0/tree/main/closed/CTuning/code) though this can be tricky on some filesystems. 

### github-actions[bot] · 2026-05-05

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
