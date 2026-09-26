# [Issue #2747] [Feature] Allow disabling all gateway rate limiting while Redis remains configured

source: https://github.com/vllm-project/aibrix/issues/2747
state: closed | updated: 2026-09-21T23:07:23Z
labels: area/gateway, kind/feature

## 正文

## Feature Description and Motivation

The gateway currently couples Redis availability to rate limiting. Deployments can need Redis for gateway startup or routing state while delegating rate limits and quotas to an upstream gateway. With Redis configured, the AIBrix-specific `user` HTTP header can trigger user-record lookup and per-user RPM/TPM checks, and a configuration profile's `requestsPerSecond` can activate per-model RPS limiting.

Please add one explicit gateway setting that disables **all gateway rate limiting independently of Redis**. Its default should preserve existing behavior.

## Use Case

An operator keeps Redis connected for the gateway and its selected routing features, but uses a separate customer-facing gateway for rate limits and quotas. Requests carrying an arbitrary `user` HTTP header should still route normally, and a profile with `requestsPerSecond` should not impose a limit when rate limiting is disabled (`AIBRIX_DISABLE_RATE_LIMITING=true`).

## Proposed Solution

When the setting disables rate limiting:

- Do not look up a user record because of the AIBrix-specific `user` HTTP header; the header must not affect routing or admission.
- Skip per-user RPM/TPM and per-model RPS admission and accounting, including streaming usage requirements and rate-limit counters, errors, and response headers.
- Preserve the standard OpenAI `user` field in the JSON request body.
- Preserve the Redis connection and its non-rate-limit uses, model listing, profile translation and routing, and state synchronization.

Please test the disabled mode with Redis configured: an unknown `user` header must not cause a user lookup or error; a profile containing `requestsPerSecond` must not limit requests; rate-limit counters and headers must remain absent; the JSON body field must pass through; and the gateway must still start, list models, and route requests.

Related work: #1874 and #1979 cover disabling a limiter when Redis is absent or unavailable. This request covers an explicit opt-out **while Redis remains configured**.

## 评论 (1)

### github-actions[bot] · 2026-09-18

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

