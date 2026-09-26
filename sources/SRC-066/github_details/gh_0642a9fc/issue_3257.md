# [Issue #3257] [FEA] Documentation for building `nvidia-cutlass-dsl-libs-base` package

source: https://github.com/NVIDIA/cutlass/issues/3257
state: open | updated: 2026-09-08T06:55:18Z
labels: feature request, ? - Needs Triage, CuTe DSL

## 正文

### Which component requires the feature?

CUTLASS C++

### Feature Request

We need `nvidia-cutlass-dsl` which depends on `nvidia-cutlass-dsl-libs-base` for a different Python version and/or architecture than available on PYPI.

However there is no source release and no instructions on how to build this.

Is it possible to build that package manually? If so how? Could that be documented?

## 评论 (6)

### github-actions[bot] · 2026-06-20

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### hwu36 · 2026-08-07

@brandon-yujie-sun 

### github-actions[bot] · 2026-09-06

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### Flamefire · 2026-09-07

ping here

### brandon-yujie-sun · 2026-09-08

> for a different Python version and/or architecture than available on PYPI.

Would you mind elaborating more on the target use cases?


### Flamefire · 2026-09-08

We are installing software for HPC systems using [EasyBuild](https://docs.easybuild.io/. Each stack needs to have matching versions, so we decide at some point for e.g. a fixed GCC and CUDA version, then for a Python version and stack things on top. As (almost) everything is built from source we can be (reasonably) sure it works together.
At some point we encountered this package which is a dependency for some other software.
But as it was not available for the Python-CUDA version combination we used for dozens of other software packages installed already we could not provide it and its dependents for users (mainly researches).
The only other solution is then to wait for a new stack to be built which have matching versions of (especially) Python and CUDA or integrate it with a stack based on older versions. But it might not make sense to.e.g build a whole separate stack just because the existing CUDA version didn't match
