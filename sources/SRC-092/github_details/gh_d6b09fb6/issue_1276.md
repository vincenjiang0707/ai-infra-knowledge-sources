# [Issue #1276] [Feature Requests] Known Issue Lists

source: https://github.com/kvcache-ai/Mooncake/issues/1276
state: closed | updated: 2026-09-23T03:15:55Z
labels: stale, auto-closed

## 正文

🚀 Welcome to the Mooncake community! Mooncake is an open-source project driven by collaboration, and your contributions—whether code, ideas, or feedback—will help shape its future.

## Production Feedback

Here, we maintain this issue list to record and track feedback from production-level users.

- [x] #1322
- [ ] Release Period & Release Notes
- [ ] Troubleshooting Doc
- [x] writeBody panic issue #1267 

---

## CI & Infrastructure Tracking
This section tracks CI test failures, flaky tests, and infrastructure issues across Mooncake's CI pipeline. We focus on failures in the `main` branch and PR CI that are NOT caused by the PR itself.

### Quick Links
- [CI Workflow: ci.yml](https://github.com/kvcache-ai/Mooncake/blob/main/.github/workflows/ci.yml)
- [Integration Test (T-one)](https://github.com/kvcache-ai/Mooncake/blob/main/.github/workflows/integration-test.yml)
- [CI CUDA 13](https://github.com/kvcache-ai/Mooncake/blob/main/.github/workflows/ci_cu13.yml)
- [CI Ascend](https://github.com/kvcache-ai/Mooncake/blob/main/.github/workflows/ci_ascend.yml)

### Ongoing Issues

| Date | Test | Job | Error | Category | Status | Assignee | Link |
|------|------|-----|-------|----------|--------|----------|------|
| 2026-04-16 | `ub_transport_test` | build (3.10) | Test hung; no progress for 4h+ before job canceled | timeout | Enabled | - | [Failure](https://github.com/kvcache-ai/Mooncake/actions/runs/24490137429/job/71573411150?pr=1677) |
| 2026-04-03 | `TestMooncakeStress.test_stress_consistency_fixed` | test-wheel (3.12) | Data mismatch on key `stress_fixed_t5_14` | flaky | Enabled | - | [Failure](https://github.com/kvcache-ai/Mooncake/actions/runs/23883620269/job/69643888109?pr=1800) |

### Recently Fixed
| Date | Test | Fix | Related |
|------|------|-----|---------|
| 2026-04-16 | `HealthCheckTest.ReturnsTwoWhenMasterDown` / `HealthCheckTest.HttpReturns503WhenMasterDown` | Replace fixed 3s sleep with polling (`WaitForHealthCode`, 100ms × 10s) | #1868 |

### Infrastructure
| Issue | Status | Assignee | Related |
|-------|--------|----------|---------|
| - | - | - | - |

### Reporting a new failure
Comment with:
1. **Date** of failure
2. **Test name** (e.g., `health_check_test.HealthCheckTest.ReturnsTwoWhenMasterDown`)
3. **Job name** (e.g., `build (3.10)`)
4. **Error summary** (one line)
5. **Category**: `flaky` / `bug` / `environment` / `timeout` / `infrastructure`
6. **Link** to the failed CI run

### When a failure is fixed
Move the entry from "Ongoing Issues" to "Recently Fixed" with a link to the fix PR.

---

**Any feedback and contributions are appreciated.**


## 评论 (2)

### github-actions[bot] · 2026-09-16

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-23

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.
