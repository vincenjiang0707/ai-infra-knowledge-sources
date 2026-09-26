# [Issue #2198] [Bug]: 在华为昇腾上进行dummy -client方式ssd卸载，大概率出现和real-client之间断链。dummy_client_live_ttl_sec_ 心跳超时10s建议可配置，默认60s

source: https://github.com/kvcache-ai/Mooncake/issues/2198
state: closed | updated: 2026-09-18T08:18:28Z
labels: bug, stale, auto-closed

## 正文

### Bug Report

[Bug]: 在华为昇腾上进行dummy -client方式ssd卸载，大概率出现和real-client之间断链。dummy_client_live_ttl_sec_ 心跳超时10s建议可配置，默认60s

dummy_client_live_ttl_sec_ 太短现象：RealClient 内部 Dummy 监控 TTL=10s，SSD batch_get 3.5s 堵心跳 → expired根因：硬编码 DEFAULT_CLIENT_LIVE_TTL_SEC=10修复：改为 60位置：/data/Mooncake/mooncake-store/include/types.h 第 93 行

### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (4)

### Copilot · 2026-05-27

The agent encountered an error and was unable to start working on this issue: This may be caused by a repository ruleset violation. See [granting bypass permissions for the agent](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#granting-bypass-permissions-for-your-branch-or-tag-ruleset), or please contact support if the issue persists. (Request id: 9E7D:F4451:617320:623E02:6A170D9D)

### github-actions[bot] · 2026-08-26

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-03

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.

### zuozhubinge · 2026-09-18

We hit the same root cause in a different scenario and have a fix ready, but I'd
like to check whether anyone is already working on this before opening a PR —
the issue is assigned, so please tell me if this overlaps with work in progress.

### Same root cause, different blocking source

The reporter's trigger is a 3.5s SSD `batch_get` blocking the ping. Ours is
buffer registration: registering a large L2 pool segment takes ~20s per 192GB,
and it monopolizes the single-threaded UDS channel. Other dummy clients sharing
that channel cannot get their pings through, so they cross the hardcoded 10s
deadline and `dummy_client_monitor_func` evicts segments that are still in
active use.

So the 10s `DEFAULT_CLIENT_LIVE_TTL_SEC` (`mooncake-store/include/types.h`) is
not just too short for slow SSD reads — any long-running operation that occupies
the UDS channel starves every other client on it. #2937 is a third instance of
the same deadline (`client_expired` exactly 10s after the first shm map).

### On the proposed fix: configurable rather than a new default

The issue title suggests both "make it configurable" and "default 60". We
implemented the configurable half only, and deliberately kept the default at
10s:

- Raising the default to 60s delays detection of genuinely dead clients by 6x
  for **every** deployment, including small ones where 10s is correct and
  useful.
- The blocking duration is a function of pool size and storage latency, which
  the project cannot know in advance. 60s is right for a 192GB L2 pool and
  wrong for something else.

Our change adds `MC_DUMMY_CLIENT_TTL_SEC`. Unset, empty, or invalid values fall
back to the existing default with an error log, so behaviour is unchanged unless
an operator opts in. The effective value is logged once at monitor startup so a
deployment can confirm the override took effect.

If maintainers prefer changing the default as well, that is a one-line follow-up
on top of this — but I'd argue the two decisions should be separate.

Validated on a two-node PD-disaggregated deployment, plus a regression test that
reproduces the pre-fix behaviour in-process.

### A second, related failure this also fixes

Once the monitor has evicted a client's segments, that client currently cannot
recover. `RealClient` returns `INVALID_PARAMS` for the missing shm context,
which is indistinguishable from a genuine bad argument, and the dummy client's
local `registered` flag stays `true` — so the next `register_buffer()` is a
silent no-op and the client loops on `shm_not_mapped` forever. This is the
symptom from #1711.

#1734 (merged) reduced how often the eviction is triggered by making the offload
RPC async. It did not make the post-eviction state recoverable: on current `main`
the silent-no-op path is still reachable, and we have a regression test that
reproduces it. Our fix adds a dedicated `DUMMY_BUFFER_NOT_MAPPED` error code and
clears the stale local flag so the next `register_buffer()` performs a real
re-registration.

Happy to split this into two PRs if reviewers prefer to keep the TTL knob and the
recovery path separate.

