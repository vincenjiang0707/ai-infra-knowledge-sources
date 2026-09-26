# [Issue #4786] [RayService] Incremental upgrade - error handling discussion

source: https://github.com/ray-project/kuberay/issues/4786
state: open | updated: 2026-09-23T04:42:54Z
labels: discussion, stale

## 正文

This issue tracks the discussion on error handling during incremental upgrades, including whether **auto rollback** should be supported in various failure scenarios:

- **Upgrade timeout:** Support timeout configuration (see [here](https://github.com/ray-project/kuberay/pull/4601#issuecomment-4061622847))
- **Controller error:** Take no action so far (see [here](https://github.com/ray-project/kuberay/pull/4601#issuecomment-4061509384))

> Per the REP: A controller error during an upgrade should result in rolling back to state A.

- **Crashed pending cluster:** Pause traffic migration and return the current traffic weights as-is

### Open Questions

- Should auto rollback be the default, or opt-in via a field in spec?
- Are there other failure scenarios not listed above?

More edge cases will be added to the discussion thread as they are identified.

## 评论 (2)

### Future-Outlier · 2026-04-30

let's wait for user feedback

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
