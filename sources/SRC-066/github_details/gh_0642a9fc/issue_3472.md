# [Issue #3472] [BUG] Installed headers return CMake / configure_file placeholders for version numbers

source: https://github.com/NVIDIA/cutlass/issues/3472
state: open | updated: 2026-09-22T18:19:19Z
labels: bug, ? - Needs Triage, CUTLASS C++

## 正文

### Which component has the problem?

CUTLASS C++

### Bug Report

https://github.com/NVIDIA/cutlass/commit/bbe579a9e3beb6ea6626d9227ec32d0dae119a49#diff-1e7de1ae2d059d21e1dd75d5812d5a34b0222cef273b7c3a2af62eb747f9d20aR54-R612 removed `configure_file` for `version.h`, but `version.h` still has `@Replacements@` in `getVersionString` and `getGitRevision`:

https://github.com/NVIDIA/cutlass/blob/564d267e4c992c456d12ad02665f9acedf7708f1/include/cutlass/version.h#L73-L83

In vcpkg we patched this in https://github.com/microsoft/vcpkg/pull/53412

## 评论 (2)

### github-actions[bot] · 2026-09-16

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### BillyONeal · 2026-09-22

Looks like there are already 2 outstanding fix attempts.
