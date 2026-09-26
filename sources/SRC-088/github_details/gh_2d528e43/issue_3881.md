# [Issue #3881] Request cache key ignores generation_kwargs -> silently reuses cached instances across different sampling parameters

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3881
state: open | updated: 2026-08-14T13:47:23Z
labels: 

## 正文

# Request cache key ignores `generation_kwargs` → silently reuses cached instances across different sampling parameters

## Summary

When `--cache_requests` is enabled, the request-cache key for a task is built
from task name, fewshot count, rank, world size, system prompt, chat-template
flags, and tokenizer — but **not** from `generation_kwargs` (temperature,
`do_sample`, `top_p`, `max_gen_toks`, `until`, ...).

This means two runs of the same `generate_until` task with **different sampling
parameters produce the same cache key**, so the second run loads the first
run's cached instances. Because `generate_until` instances bake
`generation_kwargs` into their `arguments` (see `build_request`), the second
run **silently evaluates at the first run's sampling settings**.

This is a reproducibility / eval-integrity issue, not a crash: an evaluator
who runs the same task at `temperature=0.7` after a cached `temperature=0`
run gets `temperature=0` results with no warning.

## Reproduction

```python
# Reconstructs the exact cache-key logic from lm_eval/api/task.py (build_all_requests)
def build_cache_key(task, num_fewshot, rank, world_size,
                    apply_chat_template, fewshot_as_multiturn,
                    system_instruction, tokenizer_name):
    cache_key = f"requests-{task}-{num_fewshot}shot-rank{rank}-world_size{world_size}"
    cache_key += "-chat_template" if apply_chat_template else ""
    cache_key += "-fewshot_as_multiturn" if fewshot_as_multiturn else ""
    cache_key += f"-system_prompt_hash{system_instruction}" if system_instruction else ""
    cache_key += f"-tokenizer{tokenizer_name}"
    return cache_key

common = dict(task="mmlu", num_fewshot=5, rank=0, world_size=1,
              apply_chat_template=False, fewshot_as_multiturn=False,
              system_instruction=None, tokenizer_name="meta-llama/Llama-3-8B")

# Run A: greedy/deterministic
keyA = build_cache_key(**common)
# Run B: sampling at temperature 0.7 — SAME cache key!
keyB = build_cache_key(**common)

assert keyA == keyB   # <-- collision: different sampling, identical key
```

Both keys are:
```
requests-mmlu-5shot-rank0-world_size1-tokenizermeta-llama/Llama-3-8B
```

## Impact

- **Affected config:** any `generate_until` task run with `--cache_requests`.
- **Affected component:** `ConfigurableTask.build_all_requests` (cache key
  construction at `lm_eval/api/task.py` ~line 288).
- **Behavioral effect:** changing `generation_kwargs` (temperature, sampling,
  `until`, `max_gen_tok`) between cached runs is silently ignored for the
  request-build stage. The model is still queried with the new params at
  generation time, but the *instance set* (which docs, which prompts) is
  reused — and for `generate_until`, the `arguments` tuple embeds
  `generation_kwargs`, so cached instances carry the *old* sampling config.
- **Severity:** medium. Requires `--cache_requests` (opt-in, off by default).
  No security impact; this is a silent-reuse reproducibility gap.

## Proposed fix

Fold a stable hash of `generation_kwargs` into the cache key, and extract the
key construction into a testable method. Minimal diff against current `main`:

```python
def _cache_key(self, *, rank, world_size, system_instruction,
               apply_chat_template, fewshot_as_multiturn, tokenizer_name):
    cache_key = (
        f"requests-{self._config.task}-{self.config.num_fewshot}shot"
        f"-rank{rank}-world_size{world_size}"
    )
    cache_key += "-chat_template" if apply_chat_template else ""
    cache_key += "-fewshot_as_multiturn" if fewshot_as_multiturn else ""
    cache_key += (
        f"-system_prompt_hash{utils.hash_string(system_instruction)}"
        if system_instruction is not None else ""
    )
    cache_key += f"-tokenizer{tokenizer_name}"
    # NEW: fold in sampling config so different generation_kwargs don't collide
    if self.config.generation_kwargs:
        gen_repr = json.dumps(self.config.generation_kwargs, sort_keys=True)
        cache_key += f"-gen_kwargs{utils.hash_string(gen_repr)}"
    return cache_key
```

(`utils.hash_string` already exists and is used for the system-prompt hash a
few lines above; `json` is a new stdlib import.)

**Backward compatibility:** `multiple_choice` tasks have no
`generation_kwargs`, so their keys are unchanged. `generate_until` tasks gain
a `-gen_kwargs...` suffix, causing a one-time cache miss on first run after
the change (stale cache entries are ignored) — acceptable and correct.

## Tests

I verified the proposed fix with 6 tests covering: different sampling params
produce different keys; identical params produce identical keys; dict-key order
independence (`sort_keys=True`); temperature-only changes detected;
`multiple_choice` tasks keep suffix-free keys (backward compat); existing
run-config components (tokenizer, rank) still reflected.

Happy to open a PR with this fix + tests. Note: `lm_eval/api/task.py`
currently has 16 pre-existing `ruff` errors (unrelated to this change) that
cause the `Linters` CI job to fail on any PR touching the file (see merged PR
#3817, which also has a failing `Linters` check). I can include a separate
mechanical lint-cleanup commit, or leave that to the maintainers' preference.


## 评论 (1)

### arrdel · 2026-08-14

Both open PRs (#3891 and #3951) implement the fix @AUTHENSOR proposed; consolidating the substantive divergences here so maintainers don't have to diff them by hand.

**1. Empty-dict handling**

- #3891 (Robby955): `if generation_kwargs:` — matches your proposal exactly. Empty dict `{}` is falsy, so no suffix is added.
- #3951 (AbdullahRasheed45): `if self.config.generation_kwargs is not None:` — empty dict `{}` produces a stable `-gen_kwargs_hash<hash-of-"{}">` suffix.

For any real `generate_until` task these behave identically (`generation_kwargs` is either a non-empty dict or `None` — a quick grep of `lm_eval/tasks/` turns up no task with an explicit `generation_kwargs: {}` today), but if a task ever set an empty dict — legal YAML — Robby drops the marker and Abdullah keeps a stable one. Your proposal drops it.

**2. Method visibility and test surface**

- #3891 extracts a `@staticmethod` `_build_request_cache_key`, called with all inputs passed in. Tests use a `BASE` dict + `key(**overrides)` helper against the static method directly — clean, but doesn't touch the class-config path.
- #3951 extracts an instance `request_cache_key` that reads `self._config.task`, `self.config.num_fewshot`, `self.config.generation_kwargs`. Tests build a `ConfigurableTask` via `__new__(...)` + `TaskConfig(**config)` — heavier setup but exercises the actual attribute chain a real task hits.

Both are defensible: the static version is easier to reuse elsewhere and easier to unit-test in isolation; the instance version reads more idiomatically alongside other `Task`-scoped methods and catches config-path drift.

**3. Suffix naming**

- #3891 uses `-gen_kwargs<hash>` (matches your proposal).
- #3951 uses `-gen_kwargs_hash<hash>`.

Cosmetic, but whichever lands is what future cached filenames will use forever, so worth picking one before merge.

**4. Both PRs add `default=str` to `json.dumps` — small improvement over the proposal**

Neither PR follows your proposal exactly on this point: both fold in `default=str` as a fallback for non-JSON-serializable values in `generation_kwargs` (e.g. a `torch.dtype` sneaking in programmatically). This lands identically in both PRs and is arguably strictly better than the pure `json.dumps(..., sort_keys=True)` in the proposal.

**5. Pre-existing lint noise (unaddressed in either PR)**

Confirmed your flag: `Linters` is currently failing on #3891 with the same pre-existing ruff errors #3817 merged through in June, so neither PR clears `Linters` today. As #3817 shows, that check hasn't been treated as a merge gate — but the mechanical lint-cleanup commit you offered would let the winning PR land green (either folded into it or as a separate prep PR).

Not a maintainer, no vote on which lands; happy to review either once one is picked.

