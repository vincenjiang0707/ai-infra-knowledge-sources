# [Issue #2799] [Bug] Prefix matching ignores /v1/messages `system` and /v1/responses `instructions`/`tools`

source: https://github.com/vllm-project/aibrix/issues/2799
state: open | updated: 2026-09-24T07:09:49Z
labels: kind/bug, area/gateway, triage/needs-information

## 正文

### 🐛 Describe the bug

Follow-up to #2782 / #2784. The prefix-match text is built from the request messages, plus `tools` for chat requests after #2784. Some fields that chat templates render into the prompt ahead of the conversation are still left out:

- `/v1/messages` (Anthropic style): the top-level `system` is never read, because `chatReqMinimal` has no `system` field. It can be a string or a list of content blocks.
- `/v1/responses`: `instructions` and `tools` are not read. Only `input` goes into the routing text.

Two requests that differ only in these fields therefore look like a full prefix match, even though their engine prompts diverge early.

### Steps to Reproduce

Send two `/v1/messages` requests with identical `messages` but different `system` prompts, using a prefix-aware routing policy. Both get the same routing text and are treated as a 100% prefix match.

### Expected behavior

These fields contribute to the prefix-match text (`RoutingContext.PrefixMatchText`, from #2784), the same way `tools` does for chat requests. `Message` and the size estimates stay unchanged. The `/v1/responses` `tools` can reuse the canonical rendering and the `AIBRIX_PREFIX_CACHE_INCLUDE_TOOLS` flag.

Reported by @bolubo in https://github.com/vllm-project/aibrix/issues/2782#issuecomment-5805724900.


## 评论 (2)

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-needs-info -->
Please complete these required sections: `Environment`.

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

