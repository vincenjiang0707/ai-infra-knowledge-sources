source: https://github.com/vllm-project/guidellm/pull/898

# docs(developing): add a proper Logging guide (#881) - #898

## Conversation

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I think this is close to ready. I have one comment.

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated


**suggested changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 6, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

Also seems mostly good to me. In addition to Jared's suggestion:

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 6, 2026

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated

|
Thanks all for the review. Addressed the feedback:
Let me know if the consolidation went too far or if you'd like the defaults restated inline. |

|
Hi |


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 6, 2026

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated

[DEVELOPING.md](https://github.com/vllm-project/guidellm/pull/898/files#diff-8822179a8da757fde968cf80a9162e1c1d6f8cc170509cfbdea10be03b7e7d20)Outdated

[Anai-Guo](https://github.com/Anai-Guo)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ff21b6281076ca2c5f5333bba4dacc63cb5652f2..f6170d59047f7d7d8c560068e9f720ac7bc0664c)the docs/logging-guide-881 branch from

[to](https://github.com/vllm-project/guidellm/commit/ff21b6281076ca2c5f5333bba4dacc63cb5652f2)

`ff21b62`


`f6170d5`

[Compare](https://github.com/vllm-project/guidellm/compare/ff21b6281076ca2c5f5333bba4dacc63cb5652f2..f6170d59047f7d7d8c560068e9f720ac7bc0664c)

July 6, 2026 22:15

|
Fixed the DCO check (the follow-up commit was missing a sign-off). Heads-up on the merge conflict: Happy to redo this however is easiest for you: I can re-open a fresh branch with just the Logging edits layered on top of the current |

[Anai-Guo](https://github.com/Anai-Guo)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d32f265c016affca64e2f4e74f797f53c877e92f..500fb25c8dd42a342a2e661d3c447273754ab250)the docs/logging-guide-881 branch 4 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/d32f265c016affca64e2f4e74f797f53c877e92f)

`d32f265`


`500fb25`

[Compare](https://github.com/vllm-project/guidellm/compare/d32f265c016affca64e2f4e74f797f53c877e92f..500fb25c8dd42a342a2e661d3c447273754ab250)

July 8, 2026 01:25

Append two runnable examples to the existing Logging section: verbose console output (with --disable-progress) and structured DEBUG file logging. Keeps the maintainer's concise section intact and only adds the examples. Signed-off-by: Tai An <antai12232931@outlook.com>

[Anai-Guo](https://github.com/Anai-Guo)

[force-pushed](https://github.com/vllm-project/guidellm/compare/500fb25c8dd42a342a2e661d3c447273754ab250..4018aa4cee079245e9b63a361e459fc27275afb3)the docs/logging-guide-881 branch from

[to](https://github.com/vllm-project/guidellm/commit/500fb25c8dd42a342a2e661d3c447273754ab250)

`500fb25`


`4018aa4`

[Compare](https://github.com/vllm-project/guidellm/compare/500fb25c8dd42a342a2e661d3c447273754ab250..4018aa4cee079245e9b63a361e459fc27275afb3)

July 8, 2026 01:27

|
Thanks all — the feedback made clear the prose rewrite was adding redundancy rather than value. I've reworked the PR to be minimal:
This keeps the diff to a +14 pure addition. Happy to adjust wording on the two examples if you'd prefer them phrased differently. |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 8, 2026

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 8, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

`docs/guides/troubleshooting.md`

(Debug Logging) links to`developer/developing.md#logging`

for the full logging guide, but that anchor pointed at a bare list of environment variables nested underDeveloping the Web UI— not the standalone guide the link implies. Fixes #881.## Changes

`### Logging`

to a top-level`## Logging`

section, keeping the`#logging`

anchor that the two troubleshooting links depend on.Console— human-readable output to`stdout`

, controlled by`GUIDELLM__LOGGING__CONSOLE_LOG_LEVEL`

(default`WARNING`

).File— structured JSON, enabled by`GUIDELLM__LOGGING__LOG_FILE`

/`GUIDELLM__LOGGING__LOG_FILE_LEVEL`

(default file`guidellm.log`

, default level`INFO`

).`GUIDELLM__LOGGING__*`

variables with defaults taken from`LoggingSettings`

in`src/guidellm/settings.py`

and the sink behavior in`src/guidellm/logger.py`

.Docs-only; no code changes.

🤖 Generated with Claude Code

## git log

commit

4018aa4Author: Tai An antai12232931@outlook.com

Date: Tue Jul 7 18:21:28 2026 -0700

Signed-off-by: Tai An antai12232931@outlook.com