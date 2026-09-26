# [Issue #4167] Nightly build/test failure - 2026-09-16

source: https://github.com/kvcache-ai/Mooncake/issues/4167
state: open | updated: 2026-09-17T16:49:44Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/34993501189
**Branch**: refs/heads/main
**Timestamp**: 2026-09-16T16:13:21.430Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (7)

### PushpakAg · 2026-09-16

I'd start by checking the logs of the failed jobs in the linked workflow run to see if there's any recurring error or pattern.


### ykwd · 2026-09-17

Seems like the CI was not executed on the tone platform

### PushpakAg · 2026-09-17

Could you clarify what you mean by "tone platform"? Are you referring to a specific environment or configuration that wasn't used?


### ykwd · 2026-09-17

@PushpakAg Thanks for looking into this issue together. Our SGLang integration test runs on Tone: [https://github.com/kvcache-ai/Mooncake/actions/runs/34993501189/job/104535195045](https://github.com/kvcache-ai/Mooncake/actions/runs/34993501189/job/104535195045)

The other failing cases are Go-related. I’m not sure whether this PR addresses the Go-related issues: [https://github.com/kvcache-ai/Mooncake/pull/4150](https://github.com/kvcache-ai/Mooncake/pull/4150)


### PushpakAg · 2026-09-17

I'll take a look at the SGLang integration test on Tone and see if there's anything specific causing the failure. As for the Go-related issues, I'll review the mentioned PR to determine if it addresses those problems. Thanks for the links!


### ykwd · 2026-09-17

I contacted the admin of the Tone platform, and they were able to identify the issue. It looks like the machine was configured to automatically restart when a GPU drops, but in this case it didn't come back up within the 8-minute timeout, which caused the machine to become unreachable.

The community T-One platform just rolled out a feature that allows the machine restart timeout to be customized, and the admin has also updated the template configuration accordingly. We can keep an eye on it for a while and see if the issue happens again.


### PushpakAg · 2026-09-17

That sounds like a good plan. Let's monitor the situation and see if the updated configuration resolves the issue. If the problem persists, we might need to explore other solutions.

