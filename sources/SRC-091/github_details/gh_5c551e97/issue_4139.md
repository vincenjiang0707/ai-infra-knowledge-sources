# [Issue #4139] CI: add precise XPU path filtering and expand XPU test coverage

source: https://github.com/LMCache/LMCache/issues/4139
state: open | updated: 2026-09-20T01:49:04Z
labels: stale

## 正文

## Background

We want XPU support in LMCache CI to become broader and more reliable. The current work should move in layers:

- activate and improve XPU coverage in unit tests first
- design a precise path filter so `unit-test-xpu` runs only when relevant changes land
- add XPU paths to the MP test suite next
- expand XPU coverage to more tests within the current CI architecture

This should be done incrementally so each layer can be validated before moving to the next one.

## Proposal

### 1. Design precise path-based triggering for `unit-test-xpu`
Before expanding test coverage, we need a path filter that can accurately decide when the XPU unit test job should run.

Goals:
- trigger `unit-test-xpu` only for changes that can affect XPU behavior or related test logic
- make the filter easy to extend as new XPU-related paths are added

#### Steps:
- Reduce the likelihood of unrelated code changes triggering k3s tests by refining the classification.
- Add path filters for XPU-related content to avoid running tests for unnecessary changes.

### 2. Start with unit tests
Identify the unit tests that can and should run with XPU coverage.

Goals:
- add XPU-aware test cases where device behavior matters
- refactor tests that are currently hard-coded for a single device
- reduce duplicated logic across CPU and XPU paths
- make it easy to extend the same test structure to future devices

#### Steps:
- refine existing XPU-aware test and reduce duplicated checks
- enable XPU-aware favors for fundamental tests under benchmarks/cli/frontend/disaggregated
- enable XPU-aware favors for v1 fundamental tests
- add more XPU tests if needed
 
### 3. Add XPU paths to MP tests
After the unit-test layer is in place, extend the MP test suite so it can exercise XPU behavior.

Goals:
- introduce XPU-specific MP test paths
- keep the MP test flow stable and maintainable

### 4. Expand XPU coverage to more tests
Once unit tests and MP tests can handle XPU cleanly, expand XPU coverage to more test categories within the current CI architecture.

Goals:
- add more XPU test cases without redesigning the CI system
- keep test selection and execution precise

### 5. Gate nightly vLLM before using it as the baseline
Nightly vLLM builds should be treated as a gate, not as an assumed stable baseline.

Following the approach in [#3861](https://github.com/LMCache/LMCache/issues/3861):
- run a daily gate job against the latest vLLM nightly
- record the nightly version only when the gate passes
- keep the previous known-good version when the gate fails

This prevents unrelated upstream nightly breakage from causing false CI failures in LMCache.

## 评论 (3)

### VincyZhang · 2026-07-17

@hlin99  @zxue2 @XinyuYe-Intel Please review the proposals above.

### zxue2 · 2026-07-20

Hi @VincyZhang  thx for follow-up!

- Filter xpu test cases under  ```pytest tests/v1/```  ,   ```pytest tests/benchmarks/```, etc.   ->  I'll raise a separate PR to address/discuss it.
- Not sure how much extra efforts nightly xpu vLLM will bring to us if it is not as stable as we expect.  -> Could you pls reach xpu vLLM team for recommendation?


### github-actions[bot] · 2026-09-20

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
