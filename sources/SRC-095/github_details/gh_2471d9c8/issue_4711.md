# [Issue #4711] [History Server] Data Retention Policy

source: https://github.com/ray-project/kuberay/issues/4711
state: open | updated: 2026-09-23T04:42:32Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Part of History Server Beta #4706.

- **Storage retention:** Clean up outdated data in the persistence layer and sync up to the cache layer
- **Memory retention:** Evict excessive in-memory cluster session snapshots (e.g., LRU)

### Use case

_No response_

### Related issues

Memory retention part is related to #4709


### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (3)

### chiayi · 2026-04-15

To add on, we will need to set a TTL for the data and store when we "start" persisting the data. 

Session termination timestamp could be used as the "start" of the TTL.

### chiayi · 2026-05-11

For blob storage data retention, we will suggest users to utilize cloud native data retention policies and features. 
1. Most blob storage providers are industry standard and trying to support data retention on our side will just be reinventing the wheel. 
2. Additionally, storage solutions provide features and guardrails for data retention already, and if users want to use those features, they would still have to manually implement them. Many of the features are not manageable programmatically. 
3. If we don't have our own "cleaner", we won't be introducing additional complexity to the the history server. ex: no need to take care of crashes or purge failures. 

Instead, we will have documentation for GKE, EKS, and AKS. 

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
