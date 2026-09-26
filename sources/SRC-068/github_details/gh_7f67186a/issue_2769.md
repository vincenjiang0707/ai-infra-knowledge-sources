# [Issue #2769] publish.yml: create trigger has no tag filter, so branch pushes fail the workflow and new matrix entries never build

source: https://github.com/Dao-AILab/flash-attention/issues/2769
state: open | updated: 2026-08-12T00:20:23Z
labels: 

## 正文

## Summary

`.github/workflows/publish.yml` triggers on:

```yaml
on:
  create:
    tags:
      - v*
```

The `create` event does not support filters, so the `tags:` key is silently ignored and the workflow also fires on **branch** creation. `setup_release` then runs:

```bash
gh release create ${GITHUB_REF#refs/tags/} --repo $GITHUB_REPOSITORY --title ... --generate-notes
```

For a branch, `refs/heads/...` does not match the `refs/tags/` prefix, so the ref is passed through unstripped and the step fails:

```
HTTP 422: Validation Failed (https://api.github.com/repos/Dao-AILab/flash-attention/releases)
pre_receive Sorry, branch or tag names starting with 'refs/' are not allowed.
Published releases must have a valid tag
```

`build_wheels` and `publish_package` are `needs:`-dependent, so both are skipped.

## Impact

Almost every run of "Build wheels and deploy" is a failure triggered by an ordinary branch push — e.g. [run 31060582771](https://github.com/Dao-AILab/flash-attention/actions/runs/31060582771) on `refs/heads/drisspg/stack/60`. Of the last 100 runs, 99 are branch refs (95 failed, 4 cancelled) and the single success is the tag run `v2.8.3.post1`. The real signal is buried in that noise.

Worth noting the compute cost is near zero — every one of those runs dies in `setup_release` within seconds and the matrix never starts. The cost is signal: the workflow reads as permanently broken, and a genuine release failure would be indistinguishable from the background.

## A separate problem: the current matrix has never run

This is **not** caused by the trigger bug, and I want to be precise about that since the two are easy to conflate. The tag path works correctly under `create` — [run 27279915131](https://github.com/Dao-AILab/flash-attention/actions/runs/27279915131) is the `v2.8.3.post1` run and it succeeded and published.

A tag-triggered run uses the workflow *as it exists at that tag*, and `v2.8.3.post1` points at a commit off a line that diverged from `main` well before the matrix was updated:

```
v2.8.3.post1...main      status: diverged, ahead_by 558, behind_by 2
v2.8.3.post1...c04a808   status: diverged, ahead_by 357, behind_by 2
```

So c04a808 (adds torch 2.9.1 / 2.10.0 and CUDA 13) is not in the tag's tree. Reading `publish.yml` at the tag confirms it still carries `python-version: ['3.9' … '3.13']` and `torch-version: ['2.4.0' … '2.8.0']` — which is why the newest tag has *older* torch coverage than `main` declares.

The practical consequence: fixing the trigger does not by itself build any wheels, and a tag cut from current `main` would run the current matrix with or without the trigger fix. Both changes are worth making; neither substitutes for the other.

Net result today: no cp310 / cp311 / cp313 wheels exist for torch >= 2.9. The only ones published are cp312 — five on `v2.8.3` (uploaded 2025-12-17, 2026-06-02, 2026-06-11, 2026-06-12) and two on `v2.8.3.post1` (2026-06-11) — and those scattered individual timestamps suggest they were added by hand rather than by a matrix run.

## Suggested fix

Move to a trigger that supports filtering:

```yaml
on:
  push:
    tags:
      - 'v*'
```

`publish-fa4.yml` already uses exactly this form (with `fa4-v*`), and the globs do not collide since the pattern is anchored at the start.

Gating the first job instead would also stop the failures:

```yaml
jobs:
  setup_release:
    if: startsWith(github.ref, 'refs/tags/')
```

but it is the weaker option — it still creates a workflow run per branch, just one where every job is skipped. The `push` trigger creates no run at all.

One behavioural difference to be aware of with `push`: `create` fires only on ref creation, while `push` also fires on ref *update*, so force-moving an existing `v*` tag would re-run the workflow and `gh release create` would fail on the already-existing release. `if: github.event.created` on `setup_release` guards it if that matters.

## Question

Is a release cut from current `main` the intended path to torch 2.9.1 / 2.10.0 wheels for python 3.10 / 3.11 / 3.13, or is the cp312-only set deliberate? We're on cp311 with torch 2.9, and the answer decides whether we build the wheel ourselves — happy to do that, just would rather not duplicate work you already intend to publish.

---

*Edit 2026-08-11: corrected the framing of the matrix section. It originally called this a "second-order effect" of the trigger bug, which implies a causal link that does not exist — the tag path works fine under `create`, and the matrix gap is caused solely by the tag pointing at older code. Also corrected the run statistics to the full 100-run sample and fixed asset timestamps that were misattributed between `v2.8.3` and `v2.8.3.post1`.*


## 评论 (1)

### joanfabregat · 2026-08-10

Following up with a data point that may be useful, plus wheels for anyone blocked by this in the meantime.

## The matrix in `main` builds further than it has published

Since the `create`-trigger bug means no tag-triggered run has executed the current matrix, it was unclear whether the newer torch entries actually compile. They do — and further than the matrix goes.

I built **2.8.3.post1 from the unmodified PyPI sdist** (no patches, only build parameters) against:

| torch | result |
|---|---|
| 2.9.1 | builds |
| 2.10.0 | builds |
| **2.11.0** | builds — beyond the matrix |
| **2.12.1** | builds — beyond the matrix |
| **2.13.0** (CUDA 13) | builds — beyond the matrix |

24 builds, zero failures, across CPython 3.10–3.13 and `sm_80`/`sm_90`/`sm_100`/`sm_120`. So whenever the pipeline is fixed, extending `torch-version` past 2.10.0 looks safe.

Two practical notes for whoever picks this up:

- The PyPI sdist bundles `csrc/cutlass`, so it builds standalone — no clone or submodule init needed.
- `NVCC_THREADS=1` with a higher `MAX_JOBS` is both faster and lighter than the reverse. Architectures then compile sequentially *inside* each job, so peak memory is roughly `MAX_JOBS × ~8 GB` regardless of arch count, instead of `MAX_JOBS × archs × ~8 GB`. Four archs at `MAX_JOBS=8` peaked near 64 GB and took ~50 min; that may let the runner cap rise above `MAX_JOBS=1`.

## Wheels, if they help anyone

Published at [fogandfrog/flash-attn-wheels](https://github.com/fogandfrog/flash-attn-wheels). All are 2.8.3.post1, `cxx11abiTRUE`, glibc floor 2.32, each release carrying a `SHA256SUMS`.

| torch | Python | CUDA | GPU architectures | release |
|---|---|---|---|---|
| 2.9 | 3.10 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.9-cp310-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.9-cp310-allarch) |
| 2.9 | 3.11 | 12.x | `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.9-cp311`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.9-cp311) |
| 2.9 | 3.11 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.9-cp311-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.9-cp311-allarch) |
| 2.9 | 3.13 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.9-cp313-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.9-cp313-allarch) |
| 2.10 | 3.10 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.10-cp310-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.10-cp310-allarch) |
| 2.10 | 3.11 | 12.x | `sm_80` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.10-cp311`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.10-cp311) |
| 2.10 | 3.11 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.10-cp311-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.10-cp311-allarch) |
| 2.10 | 3.12 | 12.x | `sm_80` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.10-cp312`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.10-cp312) |
| 2.10 | 3.12 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.10-cp312-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.10-cp312-allarch) |
| 2.10 | 3.13 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.10-cp313-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.10-cp313-allarch) |
| 2.11 | 3.10 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.11-cp310-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.11-cp310-allarch) |
| 2.11 | 3.11 | 12.x | `sm_80` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.11-cp311`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.11-cp311) |
| 2.11 | 3.11 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.11-cp311-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.11-cp311-allarch) |
| 2.11 | 3.12 | 12.x | `sm_80` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.11-cp312`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.11-cp312) |
| 2.11 | 3.12 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.11-cp312-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.11-cp312-allarch) |
| 2.11 | 3.13 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.11-cp313-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.11-cp313-allarch) |
| 2.12 | 3.10 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.12-cp310-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.12-cp310-allarch) |
| 2.12 | 3.11 | 12.x | `sm_80` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.12-cp311`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.12-cp311) |
| 2.12 | 3.11 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.12-cp311-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.12-cp311-allarch) |
| 2.12 | 3.12 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.12-cp312-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.12-cp312-allarch) |
| 2.12 | 3.13 | 12.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu12torch2.12-cp313-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu12torch2.12-cp313-allarch) |
| 2.13 | 3.10 | 13.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu13torch2.13-cp310-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu13torch2.13-cp310-allarch) |
| 2.13 | 3.11 | 13.x | `sm_80` `sm_120` | [`flash-attn-2.8.3.post1-cu13torch2.13-cp311`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu13torch2.13-cp311) |
| 2.13 | 3.11 | 13.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu13torch2.13-cp311-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu13torch2.13-cp311-allarch) |
| 2.13 | 3.12 | 13.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu13torch2.13-cp312-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu13torch2.13-cp312-allarch) |
| 2.13 | 3.13 | 13.x | `sm_80` `sm_90` `sm_100` `sm_120` | [`flash-attn-2.8.3.post1-cu13torch2.13-cp313-allarch`](https://github.com/fogandfrog/flash-attn-wheels/releases/tag/flash-attn-2.8.3.post1-cu13torch2.13-cp313-allarch) |

**Caveats, stated plainly:**

- `sm_90` and `sm_100` are **compiled but never executed by us** — we own no H100 or B200. Cubin generation is deterministic, but we are not claiming verification we did not perform. `sm_80` and `sm_120` run in our production daily.
- Architecture lists above were read from each built artifact with `cuobjdump --list-elf`, not from build logs.
- Unofficial and unaffiliated. Report FlashAttention bugs here, not to us. If the pipeline is fixed and these combinations get published upstream, these become redundant and we would rather use yours.

