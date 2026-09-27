# [Issue #4453] [Bug] Turbomind random crash when handle batch request

source: https://github.com/InternLM/lmdeploy/issues/4453
state: closed | updated: 2026-03-27T04:50:22Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

Crash with log:
`[TM][FATAL] kernels/apply_token_bitmask_inplace_cuda.cu(212): Check failed: logits_shape.first ==bitmask_shape.first logits and bitmask must have the same batch size.`

### Reproduction

Sending a batch of approximately 10 requests or higher.
Randomly, TM will crash.

### Environment

```Shell
*
```

### Error traceback

```Shell

```

## 评论 (2)

### windreamer · 2026-03-24

@tuilakhanh Could you kindly try #4456 to check if it fixes the issue?

### tuilakhanh · 2026-03-25

Fixed with https://github.com/InternLM/lmdeploy/pull/4456
