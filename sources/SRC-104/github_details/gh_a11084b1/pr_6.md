# [PR #6] draft: remove failing assertions

source: https://github.com/ROCm/rocprofiler-sdk/pull/6
state: open | updated: 2025-08-07T18:33:11Z
labels: 

## 正文

we compiled the 'develop' versions of clr and hip as Ben recommended. the HIP and HSA assertions 

  ROCP_FATAL_IF(external_corr_ids.size() < (callback_contexts.size() + buffered_contexts.size()))

that I commented out out trip with each of external_corr_ids.size(), (callback_contexts.size(), and  buffered_contexts.size() == 1. omitting them, our incomplete draft of rocprofiler-sdk support in hpctoolkit is being exercised as expected.

## 评论 (3)

### jrmadsen · 2024-06-11

Actually, I was mistaken. It appears this condition can arise if you are using both callback and buffer tracing of an API in the same context:

https://github.com/ROCm/rocprofiler-sdk/blob/2f3a8b05b3ab16a4ba9737830763681ddfa8a438/source/lib/rocprofiler-sdk/tracing/tracing.hpp#L177

https://github.com/ROCm/rocprofiler-sdk/blob/2f3a8b05b3ab16a4ba9737830763681ddfa8a438/source/lib/rocprofiler-sdk/tracing/tracing.hpp#L184

which ends up with one external correlation id map entry, one callback entry, and one buffer entry. Are you intentionally doing this?

### jmellorcrummey · 2024-06-11

We are intentionally doing this at present. It should be allowed. That's why I think the assertion should be deleted.

For the future, we aim to switch to the external correlation id support rather than using the callback. 

### jayhawk-commits · 2025-08-07

This pull request has merge conflicts that need to be resolved. It cannot be imported to the ROCm/rocm-systems repo automatically.

## Review (1)

### jrmadsen · 2024-06-11 · CHANGES_REQUESTED

Hi @jmellorcrummey, I think these should just move down below the `tracing::populate_external_correlation_ids(…)` function call that is a little further down in the code. 
