# [Issue #7] [Documentation]: erroneous git clone command

source: https://github.com/ROCm/rocprofiler-sdk/issues/7
state: closed | updated: 2025-01-20T20:22:43Z
labels: documentation

## 正文

### Description of errors

The link in the git clone command seems to contain an error.

- https://github.com/ROCm/rocprofiler-sdk/blob/27fa45520172ab2e0a056a423f34ef6b5299549e/README.md?plain=1#L40

It seems it should be

```
git clone https://github.com/ROCm/rocprofiler-sdk.git rocprofiler-sdk-source
```

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_

## 评论 (1)

### harkgill-amd · 2025-01-20

Fixed in https://github.com/ROCm/rocprofiler-sdk/commit/95b3fead0e317462fbb424ad9247313ce8ee6f66. Thanks!
