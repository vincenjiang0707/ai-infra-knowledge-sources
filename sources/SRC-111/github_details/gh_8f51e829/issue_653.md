# [Issue #653] Eval Hub integration via SDK

source: https://github.com/vllm-project/guidellm/issues/653
state: closed | updated: 2026-09-17T15:32:38Z
labels: 

## 正文

### Problem Statement

We need GuideLLM to integrate with the Eval Hub system.

### Proposed Solution

We can start from scratch or embrace / update the prototype adapter module at https://github.com/eval-hub/eval-hub-contrib/tree/main/adapters/guidellm, ensuring a production-ready and supportable implementation.

This additionally needs to be built through the official AIPCC process.

### Alternatives Considered

#90 proposed building `lm-eval` into GuideLLM. At this time, we prefer the Eval Hub integration.

### Usage Examples

```markdown

```

### Additional Context

_No response_

## 评论 (2)

### dbutenhof · 2026-03-26

Additional context in Jira https://redhat.atlassian.net/browse/RHAIRFE-795

### dbutenhof · 2026-09-17

We expect the Eval HUB people to own this entirely based on discussions with developers.
