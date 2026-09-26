# [Issue #1182] [Feature]: Check Validity of a Shared Multimedia and Model Download Service

source: https://github.com/llm-d/llm-d/issues/1182
state: open | updated: 2026-09-23T01:19:06Z
labels: enhancement, lifecycle/rotten

## 正文

### Feature Area

Other

### Problem Statement

**Description**
Currently, the llm-d ecosystem lacks a centralized mechanism for handling external assets. As we move toward complex multi-modal benchmarks (e.g., Qwen-VL with multiple images) and larger model deployments, individual components are redundantly downloading the same content, leading to inefficiencies.

**Why is this needed**:

- Centralized Caching: To prevent unnecessary network traffic by caching frequently accessed assets.
- Protocol Support: To provide native support for both http:// and https:// endpoints.
- Performance Optimization: To improve Time to First Token (TTFT) by ensuring multimedia content is cached locally before the inference request reaches the engine.


### Proposed Solution

**What would you like to be added**:
I propose the implementation of a Shared Download Service, as an **optional** component. This service will act as a centralized gateway for fetching and caching multimedia content (images and videos) and, optionally, model weights.

**Suggested implementation**:
The proposed solution is to deploy an existing open-source forward proxy (such as Squid) as a local service. We can leverage the fact that vLLM’s download logic relies on the Python requests library, which natively supports standard environment variables like `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY`. By configuring these variables, the caching layer remains transparent to vLLM, allowing us to implement centralized caching with zero code changes to the inference engine itself.

### Alternatives Considered

_No response_

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

_No response_

## 评论 (2)

### revit13 · 2026-04-20

Does it makes sense to first create a PR in `docs/proposals` based on `docs/proposals/PROPOSAL_TEMPLATE.md`  following the guidelines in `CONTRIBUTING.md`? Thanks

### github-actions[bot] · 2026-09-08

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
