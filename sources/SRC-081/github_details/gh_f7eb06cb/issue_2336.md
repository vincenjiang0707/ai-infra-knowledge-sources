# [Issue #2336] [BUG] AWQ Regression due to PR 2235 `bypass` lifecycle changes

source: https://github.com/ModelCloud/GPTQModel/issues/2336
state: closed | updated: 2026-01-08T11:04:50Z
labels: bug

## 正文

There is confirmed `awq` regression caused by https://github.com/ModelCloud/GPTQModel/pull/2235. Investigating. 

## 评论 (3)

### Qubitium · 2026-01-08

Not directly related to this issue but related to PR #2235. https://github.com/ModelCloud/GPTQModel/pull/2337/changes

### Qubitium · 2026-01-08

@avtc  We may need to temp revert 2235 and reapply it later after `awq` fix. The regression for `awq` moe is major blocker.  Something small but hard to track in the life cycle change (even when moe bypass is not enabled ) is blowing up most of our awq moe tests with multiple fail points: as we fix one fail point, we get hit with more fail points. It will be much easier for us to  keep `main` clean and reapply the pr as new/modified PR. 

### Qubitium · 2026-01-08

Fixed with https://github.com/ModelCloud/GPTQModel/pull/2343
