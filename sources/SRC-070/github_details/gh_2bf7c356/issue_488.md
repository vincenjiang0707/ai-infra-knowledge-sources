# [Issue #488] Question About num_rc_per_pe in Normal Dispatch

source: https://github.com/deepseek-ai/DeepEP/issues/488
state: closed | updated: 2026-09-20T01:56:54Z
labels: 

## 正文

https://github.com/deepseek-ai/DeepEP/pull/181 fixed a timeout problem by forbidding concurrent submissions of QP.

However, in normal dispatch
```
EP_DEVICE_ASSERT(ibgda_get_state()->num_rc_per_pe == num_channels or ibgda_get_state()->num_rc_per_pe >= num_sms);
```

Why is `num_rc_per_pe == num_channels` still allowed?

Thank you!

## 评论 (1)

### sphish · 2025-11-12

This PR does not actually fix the underlying issue; it only increases the number of QPs, which leads to better performance. The original QP configuration is still functional, and to maintain forward compatibility, we have kept the original QP settings in the assertions.
