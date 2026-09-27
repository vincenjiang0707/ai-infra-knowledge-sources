# [Issue #5118] [Proposal] Enforce lazy %-format logging (ruff G004) so the f-string logging migration stops regressing

source: https://github.com/LMCache/LMCache/issues/5118
state: open | updated: 2026-09-18T02:29:27Z
labels: 

## 正文

## Summary

The f-string → `%`-format logging migration is a **permanent source of good-first-issue
PRs** because nothing enforces it: `[tool.ruff.lint].select` in `pyproject.toml` still
has `#"G"` commented out. Every file that is converted by hand can regress, and the
queue never drains.

I am not asking for a code change here — just a decision on how to close the class.
I am happy to drive whichever option you pick.

## Context: the direction is already settled

In #3372 @ApostaC answered the style question explicitly:

> "I think we should use `%d/%s` style instead of f-string. This will have performance
> benefits (i.e., the string will not be evaluated if it won't be logged)"

and @maobaolong has been pointing newcomers at "similar issues related to f-string
formatting" ever since. That has produced a steady stream of one-file PRs, e.g.
#5014 (`vllm_v1_adapter.py`), #5094 (`eic_connector.py`), #4970 (`hf3fs_adapter.py`),
#4785 (`gds_backend.py`), #4727, #4650, #4479, #4357, #4290, #4142, #4124, #4102,
#3977, #3975, #3973 … with more still open: #4937, #4506, #5106, #5110, #5112.

## What is left (dev @ `5001a52c`)

```console
$ ruff check --select G --statistics lmcache tests benchmarks tools
223  G004  logging-f-string
 24  G201  logging-exc-info
  1  G002  logging-percent-format
Found 248 errors.
```

* 62 files still contain `G004`. Under `lmcache/` alone there are **52 of 795** files
  (743 files are already clean) — so the codebase is mostly there.
* Largest remaining: `mooncakestore_connector.py` (23), `hf3fs_adapter.py` (14),
  `nixl_storage_backend.py` (10), `server/__main__.py` (7).
* The two directories that already enforce the SLF rule are nearly clean:
  `lmcache/v1/multiprocess/` (1 site) and `lmcache/v1/distributed/` (10 sites).

## Why it keeps coming back

`pyproject.toml:90-91`:

```toml
    # flake8-logging-format
    #"G",
```

So `ruff check` passes for new f-string logging calls; the only way this issue class
shrinks is manual conversion, and it grows again with every new `logger.info(f"...")`.
Note that `PLE1205` is already enabled in `select` (and `PLE1206` was proposed in #4539),
so lint-level enforcement of logging hygiene is already accepted in this repo.

## Options

**A. Enable `G004` and finish the migration in one pass.**
Enable the rule and convert the remaining 223 call sites (mechanical; the message plus
its arguments, no behaviour change). Can be split per directory if you prefer smaller
PRs. After this, the rule is enforced everywhere and no further GFI issues of this
shape are needed.

**B. Enable `G004` incrementally with `per-file-ignores` (low-risk).**
Use the same negation trick that already scopes SLF:

```toml
[tool.ruff.lint.per-file-ignores]
# Ignore G004 everywhere except the directories that are already clean
"!lmcache/v1/multiprocess/**" = ["SLF", "G004"]
"!lmcache/v1/distributed/**" = ["SLF", "G004"]
```

Starting with `lmcache/v1/multiprocess/` + `lmcache/v1/distributed/` costs an 11-site
cleanup and then those directories can never regress; more `!` patterns can be added
(or removed) directory by directory. This keeps every PR tiny, at the cost of a
growing ignore list in the config.

**C. Keep the current file-by-file flow** — then it would help to keep a checklist
somewhere (e.g. in #3372) of the remaining files, since the umbrella's sub-issues are
all closed (#3372 currently has no open sub-issue, which is why newcomers keep asking
what is left to do — see the comments from `sanjayy0612`, `meghana-madhyastha`,
`alany85`, `Rudra-G-23`).

`G201` (24 sites: prefer `logger.exception(...)` inside `except`) and `G002` (1 site)
are adjacent, but they change the log *content* rather than defer formatting, so they
may deserve a separate decision.

## Ask

Which option do you want? If B is acceptable I can prepare the two-directory cleanup
plus the config change as the first step; if A is preferred I can send the mechanical
conversion in per-directory PRs. I can also open the remaining per-file issues if that
is how you want the work handed out.


## 评论 (5)

### maobaolong · 2026-09-15

@LiRunGuo Thank you for raising this and for thinking through the problem more carefully and deeply. This is a very good direction.

I agree that we should move toward enforcing G004. As a first step, I would like to see a PR that enables G004 and adds temporary per-directory ignores for the areas that are not migrated yet. After that, we can remove those ignores directory by directory as each area is cleaned up.

The follow-up directory-by-directory cleanup work can be a good fit for new contributors, while the initial PR gives us a clear enforcement path and prevents already-cleaned areas from regressing.

Would you like to create a PR for the motioned first step?

### LiRunGuo · 2026-09-15

Yes — here is the first step: #5125.

It enables `G004` and adds temporary `per-file-ignores` for the 72 files that are not migrated yet, so the rule is enforced everywhere else from now on (1265 of 1337 lintable files), and entries can be deleted one by one as the cleanup proceeds.

One thing worth flagging for the directory-by-directory plan: ruff matches `per-file-ignores` patterns with `*` **crossing directory separators**, so `"lmcache/*.py" = ["G004"]` quietly ignores the whole package subtree. A naive per-directory list (`lmcache/*.py`, `lmcache/v1/*.py`, `lmcache/v1/storage_backend/*.py`, …) also ignores **771 already-migrated files** and leaves only 494 of 1337 files protected. So the list uses `"<dir>/**"` only where every file below the directory still violates the rule (4 entries) and an explicit file entry otherwise (66 entries). The result is audited: exactly the 72 violating files are ignored, zero clean files are.

`G201`/`G002` are left out as separate decisions, as noted above.

### sanjayrohith · 2026-09-17

Picking up the directory-by-directory follow-up for `lmcache/v1/distributed/` — converted its last 9 f-string log calls (`bigtable_l2_adapter.py`, `mooncake_te_impl.py`) and removed those two `per-file-ignores` entries so the directory is G004-enforced: #5167. @LiRunGuo, shout if you already had this slice queued locally and I'll drop it.

### LiRunGuo · 2026-09-18

@sanjayrohith Nothing queued on my side for `lmcache/v1/distributed/` — it's yours, thanks for picking it up.

One note for whoever takes the next slice: the ignore list is 4 `"<dir>/**"` entries plus explicit per-file entries. `distributed/` was two explicit file entries, so deleting exactly those two is right. The four `**` entries (`benchmarks/storage_backend_io/`, `examples/disagg_prefill/`, `examples/disagg_prefill_mp/`, `examples/token_dropping/rkv_variants/`) are different: if a directory still has unmigrated files after your pass, the `**` entry has to be replaced with explicit file entries rather than deleted, otherwise the leftovers start failing G004.

### maobaolong · 2026-09-18

The first step is now complete in #5125, so I organized the remaining G004 cleanup into claimable sub-issues under this tracker.

Existing related open issues are now linked as children here:

- #4506 - `mooncakestore_connector.py`
- #4737 - `nixl_channel.py`
- #4937 - `cachegen_basics.py`
- #5106 - three small LMCache modules
- #5110 - `eic_adapter.py` + `s3_adapter.py`
- #5112 - `azure_adapter.py` + `audit_adapter.py`

Newly filed child issues from the #5125 ignore map:

- #5178 - Buildkite async request logging
- #5179 - `benchmarks/multi_round_qa/`
- #5180 - `benchmarks/rag/`
- #5181 - `benchmarks/storage_backend_io/`
- #5182 - `examples/disagg_prefill/`
- #5183 - `examples/disagg_prefill_mp/`
- #5184 - token-dropping top-level notebooks
- #5185 - token-dropping experiment notebooks
- #5186 - `examples/token_dropping/rkv_variants/`
- #5187 - top-level LMCache utility logging
- #5188 - v1 API/server entrypoints
- #5189 - v1 cache-controller files
- #5190 - v1 config/cache-engine/memory-management files
- #5191 - v1 compute attention files
- #5192 - v1 compute blend/model files
- #5193 - health monitor + lookup client
- #5194 - storage backend package/root files
- #5195 - PD backend files
- #5196 - NIXL backend file
- #5197 - common connector files
- #5198 - backend connector files
- #5199 - helper connector files
- #5200 - HF3FS adapter
- #5201 - SageMaker HyperPod adapter
- #5202 - disagg cache-engine tests
- #5203 - disagg channel tests
- #5204 - v1 storage/shm tests
- #5205 - stale clean-file `G004` ignores for `infinistore_adapter.py` and `redis_adapter.py`

In flight: #5167 is already handling the `lmcache/v1/distributed/` slice, so I did not duplicate it.

For contributors: please pick one unassigned child issue and comment `/claim` there before opening a PR, so we avoid duplicate work. Each PR should remove the matching `G004` ignore entry from `pyproject.toml` once its file(s) are clean.

