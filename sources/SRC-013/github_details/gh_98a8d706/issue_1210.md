# [Issue #1210] [Cleanup] Remove upstream update from llm-d repo and get rid of images

source: https://github.com/llm-d/llm-d/issues/1210
state: open | updated: 2026-09-13T01:22:51Z
labels: CI/CD, lifecycle/rotten

## 正文

This workflow applies too much bloat, many of these issues are not helpful. Lets drop the scanning of upstream version in main and automated issue creation.

cc @llm-d/release-crew 

## 评论 (3)

### Gregory-Pereira · 2026-04-20

This is the workflow: https://github.com/llm-d/llm-d-infra/blob/main/.github/workflows/nightly-org-checks.yml

### ManishSharma1609 · 2026-04-21

Hi @Gregory-Pereira, I can pick this up!

### github-actions[bot] · 2026-08-28

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
