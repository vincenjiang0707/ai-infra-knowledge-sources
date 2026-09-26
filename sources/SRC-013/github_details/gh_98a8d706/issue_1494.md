# [Issue #1494] [refactor] refactor E2E approach

source: https://github.com/llm-d/llm-d/issues/1494
state: closed | updated: 2026-09-23T01:19:13Z
labels: help wanted, lifecycle/rotten

## 正文

We did a good job instituting and fixing E2Es with regard to the `helm` --> `kustomize` refactor. However now we need to make our E2E and CI setup more robust. This includes two core issues:
- [ ] E2Es have lots of duplicate code for deployment, they should be refactored to consume scripts with different paramters to configure anything specific to different guides / env
- [ ] E2Es currently generate branchs on the main repo, this can lead to clutter and makes the project come off as not as professional

## 评论 (3)

### ahg-g · 2026-05-13

Can we add a ruleset to limit creating branches to members with maintain role now? or will this break current CI?

### ahg-g · 2026-05-13

Note that the above two can be worked on independently, ideally the second issue first since it should be easier to do.

### github-actions[bot] · 2026-08-23

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
