# [Issue #52] Why is it possible to disable congestion control?

source: https://github.com/deepseek-ai/DeepEP/issues/52
state: closed | updated: 2026-09-18T10:03:20Z
labels: 

## 正文

![Image](https://github.com/user-attachments/assets/6072dce4-53a1-46ca-9c5e-daf34e5244ae)

Which congestion control was disabled, and why？

## 评论 (3)

### sphish · 2025-03-07

Congestion control is a configurable setting on NICs and switches. If there is no congestion, you do not need to enable it, as doing so may reduce bandwidth.

### JJBM123 · 2025-03-07

There are two types of congestion control mechanisms: credit-based flow control and ECN. If congestion does not occur, there is no need to disable ECN？
is it the flow control that is being disabled?

### sphish · 2025-03-09

The congestion control algorithms I'm referring to are DCQCN, RTTCC, and similar protocols. What you mentioned, CBFC and ECN, are not congestion control algorithms.
