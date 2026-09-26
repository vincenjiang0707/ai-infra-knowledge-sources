# [Issue #2586] [FEA] Add Windows support in CuTe wheels on Pipy

source: https://github.com/NVIDIA/cutlass/issues/2586
state: closed | updated: 2026-09-23T12:58:13Z
labels: feature request, ? - Needs Triage, CuTe DSL

## 正文

### Which component requires the feature?

CuTe DSL

### Feature Request

Hi,

pip install nvidia-cutlass-dsl fails on Windows
as seeing latest 4.1.0:
https://pypi.org/project/nvidia-cutlass-dsl/#files
only supports manylinux..

so requesting Windows support..

EDIT: on a related note also Python 3.13 support would be nice both Windows and Linux so I requested here:
 https://github.com/NVIDIA/cutlass/issues/2585

thanks..

## 评论 (12)

### fengxie · 2025-09-10

Thanks for reporting. We don't support windows build yet. Would WSL help your problem in short term?

### oscarbg · 2025-09-25

yes "in short term".. forgot about WSL..  keeping open for possible Windows support..

### github-actions[bot] · 2025-10-25

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### oscarbg · 2025-10-26

Still wished/needed.. better than WSl..

### github-actions[bot] · 2025-11-25

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### fengxie · 2025-11-26

@brandon-yujie-sun to keep track

### oscarbg · 2025-12-08

@fengxie thanks..
nice, new cutile 1.0 (needs CUDA 13.1 SDK) on pipy also ships for Windows (altough only Blackwell support ATM)..

### github-actions[bot] · 2026-03-08

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### oscarbg · 2026-03-08

Still interest on this..

### zzlol63 · 2026-07-01

+1, more libraries like Flash-Attention 4 are adopting the CuTe DSL and lack of a CUTLASS DSL library Windows build make it impossible to adopt outside of Linux environments.

### brandon-yujie-sun · 2026-07-02

Thanks folks for making the request. Windows is on radar, expect Windows support this summer.

### brandon-yujie-sun · 2026-09-23

@oscarbg Windows is now supported in 4.8, please try out and let us know if you see any issues.
