# [Issue #1506] [Doc]: add how to add x-gateway-inference-objective and x-gateway-inference-fairness-id for gRPC request

source: https://github.com/llm-d/llm-d/issues/1506
state: closed | updated: 2026-09-20T01:23:09Z
labels: lifecycle/rotten

## 正文

xRef: https://github.com/kubernetes-sigs/gateway-api-inference-extension/issues/2646

we should add how to add gRPC headers here: https://github.com/llm-d/llm-d/blob/615961e8e304a3e6f8af54893de95a974b73aff7/docs/api-reference/epp-http-headers.md?plain=1#L11



## 评论 (5)

### ahg-g · 2026-05-14

we need to use a `x-llm-d` prefix to all headers managed by epp

### thilak007 · 2026-05-15

Hi @zetxqx @ahg-g , I have added an example gRPC request along with the suggested headers in this [PR](https://github.com/llm-d/llm-d/pull/1514). Let me know if you have any code review changes that need to be done.

### zetxqx · 2026-05-15

@thilak007  I believe change the doc is not enough, we also need to change the code in llm-d-router here: https://github.com/llm-d/llm-d-router/blob/9f53ccc14f915591c6de735736eeb8dad08fc3c9/pkg/epp/metadata/consts.go#L19-L42

### thilak007 · 2026-05-17

> [@thilak007](https://github.com/thilak007) I believe change the doc is not enough, we also need to change the code in llm-d-router here: https://github.com/llm-d/llm-d-router/blob/9f53ccc14f915591c6de735736eeb8dad08fc3c9/pkg/epp/metadata/consts.go#L19-L42

@zetxqx , Sure, I'll go ahead and make the changes in `llm-d-router` repo. Just to understand a bit more and to avoid downstream services from breaking, is `llm-d-router` service the only place which calls the API with these headers?

### github-actions[bot] · 2026-08-20

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
