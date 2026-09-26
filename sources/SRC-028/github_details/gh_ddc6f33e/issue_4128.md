# [Issue #4128] Region Info is hardcoded in maxtext MLRun initialization

source: https://github.com/AI-Hypercomputer/maxtext/issues/4128
state: closed | updated: 2026-06-15T09:14:23Z
labels: bug

## 正文

### Bug report

[Region Info](https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/common/managed_mldiagnostics.py#L76) (us-central1) is hardcoded in maxtext MLRun initialization.

Allow customer to pass in an optional runtime argument for region and default to us-central1 if not passed for backward compatibility

### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (2)

### rapatchi · 2026-06-10

I am working on fixing this. 

### rapatchi · 2026-06-15

this is now fixed
