# [Issue #2411] setup-sccache.sh always logs "AWS credentials: set" regardless of whether they are

source: https://github.com/llm-d/llm-d/issues/2411
state: open | updated: 2026-09-02T09:47:03Z
labels: 

## 正文

## Summary

`docker/scripts/common/setup-sccache.sh` prints a diagnostic line reporting whether AWS credentials were detected for the sccache S3 backend, but the check is broken and always reports `set`, even when `AWS_ACCESS_KEY_ID` is empty/unset.

## Where

`docker/scripts/common/setup-sccache.sh:57`:

```bash
echo "  - AWS credentials: $([ -n \"${AWS_ACCESS_KEY_ID:-}\" ] && echo 'set' || echo 'NOT SET')"
```

## Why it is wrong

The `\"` sequences are inside a double-quoted string that also contains a `$(...)` command substitution. The outer double quotes already unescape `\"` to a literal `"` character before the substitution's command is parsed, so by the time `[ -n ... ]` actually runs, its argument is the literal string `"${AWS_ACCESS_KEY_ID:-}"` *including the quote characters* — which is always non-empty, so `-n` is always true.

`shellcheck` flags this directly:

```
docker/scripts/common/setup-sccache.sh:57:39: error: -n doesn't work with unquoted arguments. Quote or use [[ ]]. [SC2070]
docker/scripts/common/setup-sccache.sh:57:39: error: Argument to -n is always true due to literal strings. [SC2157]
```

Reproduction:

```bash
$ unset AWS_ACCESS_KEY_ID
$ echo "  - AWS credentials: $([ -n \"${AWS_ACCESS_KEY_ID:-}\" ] && echo 'set' || echo 'NOT SET')"
  - AWS credentials: set   # wrong — the variable is unset
```

## Impact

This is a small piece of the puzzle behind #2225 (sccache S3 credentials being invalid on every CUDA build): the build log's own self-reported credential status is unconditionally wrong, so this diagnostic line gives false confidence that credentials were present even when they were missing entirely, making the real breakage harder to notice from the logs.

## Suggested fix

Drop the unnecessary backslash-escaping — the `$(...)` already opens a fresh quoting context, so a plain `"..."` inside it works correctly:

```diff
-    echo "  - AWS credentials: $([ -n \"${AWS_ACCESS_KEY_ID:-}\" ] && echo 'set' || echo 'NOT SET')"
+    echo "  - AWS credentials: $([ -n "${AWS_ACCESS_KEY_ID:-}" ] && echo 'set' || echo 'NOT SET')"
```

Verified this reports correctly in both states after the fix, and `shellcheck` passes clean.

## 评论 (1)

### AlSh007 · 2026-09-02

This is fixed on `main` by #2413 (commit 28f432b1), which landed without referencing this issue, so it stayed open. Safe to close.
