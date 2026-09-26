# [Issue #3361] [FEA] nvidia-cutlass-dsl-libs-base / nvidia-cutlass-dsl-libs-cu13 release for Windows

source: https://github.com/NVIDIA/cutlass/issues/3361
state: closed | updated: 2026-09-23T12:59:53Z
labels: feature request, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

### Which component requires the feature?

CuTe DSL

### Feature Request

I manage FlashInfer Windows support on [SystemPanic/flashinfer-windows](https://github.com/SystemPanic/flashinfer-windows) since March 2025 for vLLM project.

Starting with FlashInfer v0.6.12, nvidia-cutlass-dsl is not avoidable anymore, as the project now deeply relies on it. 

The problem is: NVIDIA didn't released Windows support yet for nvidia-cutlass-dsl-libs-base (closed source).

This is not a FlashInfer issue itself, but rather that the required NVIDIA package is currently only distributed for Linux.

After talking with an NVIDIA contact, it requested me to open this issue to coordinate the support for nvidia-cutlass-dsl-libs-base on Windows, so he can push it internally.

Having nvidia-cutlass-dsl Windows wheels available would allow FlashInfer to continue supporting Windows users.

Related issue to track: [https://github.com/flashinfer-ai/flashinfer/issues/3786](https://github.com/flashinfer-ai/flashinfer/issues/3786)

Thank you for your work,

Javier.

## 评论 (3)

### brandon-yujie-sun · 2026-07-02

Thanks @SystemPanic for reporting this issue. Windows support is on our radar and we expect Windows support this summer.

### github-actions[bot] · 2026-08-01

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### brandon-yujie-sun · 2026-09-23

@SystemPanic Windows support is now available in 4.8. Let us know if you see any issues with that :-)
