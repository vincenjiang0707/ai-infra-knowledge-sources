# [Issue #2782] [Bug] Prefix-match routing ignores tools, so requests with different tool sets count as a full prefix match

source: https://github.com/vllm-project/aibrix/issues/2782
state: open | updated: 2026-09-24T05:57:21Z
labels: kind/bug, area/gateway

## 正文

### 🐛 Describe the bug

The prefix-match text the gateway builds for a chat request (`routingCtx.Message`, from `parseChatMessages` in `pkg/plugins/gateway/util.go`) contains only `messages[].content`. The request's `tools` array is ignored.

Most chat templates render the tool definitions *before* the conversation, so two requests with the same messages but different `tools` produce engine prompts that differ from the first tokens. The gateway still sees a 100% prefix match for them and pins both to the same pod. The pod has no reusable KV for the second request, and the router has given up load balancing to get a cache hit that does not exist.

This matters most for agentic traffic, where many clients share a system prompt and opening turns but send different tool sets.

It affects every policy that matches on the routing message: `prefix-cache`, `prefix-cache-preble`, and the PD prefill policies `prefix_cache`, `conductor` and `hybrid_cache_load`.

### Steps to Reproduce

1. Route with `prefix-cache` (or PD with `hybrid_cache_load`) across two or more pods.
2. Send a chat request with messages M and tools T1.
3. Send a second request with the same messages M and a different tool set T2.
4. The second request reports a 100% prefix match on the first request's pod and is routed there, although its prompt prefix differs.

### Expected behavior

Requests with different tool definitions should not count as the same prefix. Requests with the same tools should still match fully, whatever key order or whitespace the client uses.

### Environment

Current `main`. The behavior is independent of engine and deployment.

### Area

Gateway (routing)


## 评论 (3)

### github-actions[bot] · 2026-09-23

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### bolubo · 2026-09-24

For `/v1/messages` the system prompt is a top-level field, and `chatReqMinimal` has no `system` field, so it never reaches the routing message. Two Anthropic-style requests that differ only in the system prompt get the same routing message, and the prefix matcher counts them as a full prefix match while the engine renders a different prompt from the start. On `/v1/chat/completions` a system prompt is an ordinary message and is matched today.

`/v1/responses` has the same shape: the routing message only sees `input` content, so top-level `instructions` and `tools` are outside the match as well. #2784 leaves that path unchanged.

The system field takes a string or a list of content blocks, so a canonical rendering needs to cover both shapes. Does this belong in #2784, or would a follow-up for the remaining leading fields (responses included) fit better?

### qidaye · 2026-09-24

@bolubo Thanks, good catch. Both are real gaps of the same kind:

- `/v1/messages`: the top-level `system` (a string or a list of content blocks) never reaches the routing text, because `chatReqMinimal` has no `system` field.
- `/v1/responses`: `instructions` and `tools` sit outside the match too.

I'd keep them out of #2784 so it stays focused on `tools`. #2784 now puts the extra text in a separate `RoutingContext.PrefixMatchText`, which leaves `Message` and the size estimates alone. Both gaps can then be closed in a follow-up by adding those fields to the same prefix-match text. Opened #2799 to track it.

