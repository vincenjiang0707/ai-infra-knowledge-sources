# [Issue #1961] Refactor aibrix-gateway plugins configuration to adapt to routing-profile

source: https://github.com/vllm-project/aibrix/issues/1961
state: open | updated: 2026-09-24T00:28:02Z
labels: 

## 正文

### 🚀 Feature Description and Motivation

TODO: list the configurations to refactor to routing-profile and split them into two categories, ones which need backward compatibility and ones which do not.

### Use Case

NA

### Proposed Solution

_No response_

## 评论 (2)

### bolubo · 2026-09-21

Hi @varungup90, I'd like to pick this up. Before I start: is this still the direction you want, and is anyone already on it internally? It's been quiet since filing, so I wanted to check rather than jump straight into a PR.

First pass on the TODO above, from the gateway plugin's config surface (`pkg/plugins/gateway`, non-test code): 53 `AIBRIX_*` env vars plus `ROUTING_ALGORITHM` / `POD_NAME`, mostly read once at startup into package-level globals.

The split it asks for:
- 41 look like routing-semantics knobs that could live in the profile: auto-blend weights (4), VTC basic plus token tracker (9), Preble (4), prefix-cache std-dev (1), load-imbalance gate (2), TTFT (1), PD score policies (2), decode LB weights (2), spreads/ratio (4), abort/timeouts (3), prompt bucketing (1), token-load (5), hybrid-cache-load (1), min-match (1), session affinity (1).
- Of those, 33 are documented in `ENV_VARS.md`: keep env as the default and let a profile value override it, same convention the PD path already uses (`parsePDAlgorithmConfig` / `effectiveScorePolicies`). The other 8 are undocumented/internal (`TOKEN_LOAD_*` and friends) and can move without a compat path.
- The remaining 11 look deployment-level and I'd leave global (tokenizer pool, statesync, KV connector, TRT machine ID, auth, HTTPRoute cache TTL, router string-cache). One more is already dead.

Two questions before I start:
1. Schema: extend the profile's existing `routingConfig`, or a dedicated section for plugin/algorithm config? I'd default to `routingConfig` to avoid a second mechanism.
2. Split: anything above you'd move the other way?

If this direction works, I'll send one PR (profile-first plumbing with env fallback, no behavior change unless a profile overrides something) with tests and `ENV_VARS.md` updates. Happy to post the full per-variable table first if that's easier to review.

### bolubo · 2026-09-24

Follow-up now that the profile-override plumbing from #2786 is in: #2796 covers the rest of the knobs above by scoping the state they configure, instead of applying a per-request value to shared state.

- The VTC token tracker now follows the profile. `vtc.tokenTrackerWindowSize`, `vtc.tokenTrackerTimeUnit`, `vtc.tokenTrackerMinTokens`, `vtc.tokenTrackerMaxTokens` and the two token weights resolve to a tracker per configuration: profiles that agree share one, a process keeps at most 16 of them, and a request past that bound keeps the shared tracker instead of failing.
- `sessionAffinity.maxLocalKeys`, `router.maxCachedAlgorithmStrings` and `pd.tokenLoadMaxSessions` bound what a profile's own requests may add to the shared session-key cache, to the routing string caches and to the session table, as a share of the environment cap that they never raise.

A profile that sets none of them keeps the shared instances and the environment values, so existing deployments are unchanged. The last two knobs of this issue, `preble.slidingWindowPeriodMinutes` and `preble.evictionLoopIntervalMilliseconds`, are process-wide timers: they need per-profile histograms and eviction schedules rather than a scoped instance, so they follow in their own PR.
