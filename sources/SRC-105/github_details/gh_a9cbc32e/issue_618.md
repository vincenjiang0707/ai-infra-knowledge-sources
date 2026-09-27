# [Issue #618] [Req]: Find traced binary in PATH

source: https://github.com/ROCm/rocprofiler-compute/issues/618
state: closed | updated: 2025-03-19T21:44:35Z
labels: enhancement, triage

## 正文

### Is your feature request related to a problem?

It is counterintuitive that when I run `rocprof-compute` on a Python script I have to use 
```
rocprof-compute ... -- `which python` args...
```
instead of simply calling `rocprof-compute -- python args...`.

### Describe the solution you'd like

Have rocprofiler-compute look up the binary in the execution context (e.g., `shutil.which`) for the application I am calling.

### Describe any alternatives you've considered

_No response_

### Additional context

_No response_

## 评论 (2)

### coleramos425 · 2025-03-19

That complication should be solved via #578. @tbennun if I understand the request properly, this request is addressed in issue #577 

### tbennun · 2025-03-19

Perfect, I had run develop but in a different context. Thanks!
