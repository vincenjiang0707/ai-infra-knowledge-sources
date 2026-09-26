# [Issue #1461] Submission checker is not counting "No results" for not truncated accuracy logs

source: https://github.com/mlcommons/inference/issues/1461
state: closed | updated: 2026-05-12T00:39:42Z
labels: Stale

## 正文

If accuracy logs are not truncated, submission checker is outputting an error but not including this in "No Results". So, this error can be missed by the submitters. 

## 评论 (2)

### rakshithvasudev · 2023-08-25

The checker also mentions that file size is large. That's a possible hint. I Don't remember there is an explicit fix it recommends. 

### github-actions[bot] · 2026-05-12

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
