# [Issue #4419] Document and automate the AITER release plan

source: https://github.com/ROCm/aiter/issues/4419
state: closed | updated: 2026-08-31T09:59:14Z
labels: 

## 正文

  ## Summary

  Define and automate the AITER release plan so scheduled releases and hotfix post releases follow a predictable process.

  ## Tasks

  - [ ] Document the AITER release plan in `README.md`.
    - Scheduled releases should happen every two weeks.
    - Each scheduled release should use a release branch named like `release/v0.1.19`.
    - Each scheduled release should publish a matching tag, such as `v0.1.19`, following the normal version progression, for example
  `v0.1.18` -> `v0.1.19`.

  - [ ] Add release CI that runs every two weeks to validate the release branch/tag and build/upload release artifacts.
    - The release artifacts should be published to GitHub Releases in the same style as the existing releases:
  https://github.com/ROCm/aiter/releases

  - [ ] Support hotfix post-release tags.
    - Hotfixes should be cherry-picked onto the corresponding release branch.
    - When a post-release tag is pushed, such as `v0.1.16.post5`, CI should automatically build and upload artifacts to the corresp
  onding GitHub Release, matching the existing post-release flow: https://github.com/ROCm/aiter/releases#release-v0.1.16.post5

  ## Acceptance Criteria

  - The release cadence and branch/tag naming rules are documented in `README.md`.
  - Scheduled release CI can be triggered every two weeks and publishes release artifacts to GitHub Releases.
  - Hotfix post-release tags automatically publish artifacts to the appropriate GitHub Release.
  - The process is consistent with existing AITER release pages and artifact naming.

## 评论 (1)

### zufayu · 2026-07-28

Some measurements from the current state of the repo, in case they are useful for scoping this. Everything below is from the GitHub API today; the numbers are `compare` totals, not estimates.

### The cadence rule is mostly being followed, with one gap

Mainline tags, dated by their **commit** date rather than the publish date (publish dates are out of order for the `.post` line and make the sequence look stranger than it is):

| tag | commit date | gap | commits vs previous | release branch |
|---|---|---|---|---|
| `v0.1.17` | 2026-07-08 | — | — | ✅ `release/v0.1.17` |
| `v0.1.18` | 2026-07-20 | 11 days | 139 | ❌ **missing** |
| `v0.1.19` | 2026-07-27 | **7 days** | 50 | ✅ `release/v0.1.19` |

So the branch convention this issue proposes already exists for 15 versions back to `v0.1.12` — `v0.1.18` is the one that skipped it. And `v0.1.19` landed a week after `v0.1.18` while its notes still say "bi-weekly release", so the cadence slipped rather than the rule being absent. Both look like exactly the kind of thing CI enforcement would catch, which supports the proposal.

### `v0.1.17` has diverged from `main`

```
compare main...v0.1.17 -> diverged, ahead_by=7, behind_by=196
```

Seven fixes live only on the release line and were never merged back:

```
94f2034f [opus] gate TDM/named-barrier on clang>=22 so clang-20 (ROCm 7.x) ...
ac247859 [Gluon] [MI35X] Fix mqa CI failure (#4064)
892d228e fix(moe): keep fp32 per-token scale layout for 2-stage asm stage ...
27fa9d92 Fix int32 overflow in batched _gemm_bf16 (#4075)
1f0fa2d0 [BugFix] Fix get_dtype_fp8 to always return the correct fp8 dtype ...
5dede1da fix the adress over 32bit and radom nan error (#3988)
32214c29 fix max_fp8 from 240 to 448 for gfx950 (#4070)
```

`v0.1.18` and `v0.1.19` are both clean ancestors of `main` (`ahead_by=0`), so the divergence is isolated to `v0.1.17` — but nothing currently detects it. Worth considering an acceptance criterion that a hotfix cherry-picked onto a release branch either lands on `main` too, or is flagged. Otherwise a fix like `fix max_fp8 from 240 to 448 for gfx950` silently exists in one release line and not the next.

### The gap this issue does not cover: release notes content

The tasks here are about *building and uploading artifacts*. The artifacts are fine — six wheels on `v0.1.19`, correct naming, ROCm 7.0/7.1/7.2 × cp310/cp312. What is thin is what the release *says*:

| tag | commits included | body length | PRs listed |
|---|---:|---:|---:|
| `v0.1.18` | 139 | 74 chars | **0** |
| `v0.1.19` | 50 | 296 chars | **1** |

`v0.1.19` lists `#4397`, which is the tip commit the tag points at. The other 49 are undocumented, and they are not minor — eleven touch attention paths:

```
#4321 [GFX950] opus fmha d128 kernel optimization
#3732 HD256 FMHA FP8 GFX950
#3890 [gluon][mla][gfx950] support MTP for mla
#4337 bf16 asm mha: enhance kernel to avoid corner issue
#4311 / #4345 / #4310  MLA v4 changes
#4347 [GFX942] Triton blockscale preshuffle tuned configs for DeepSeek-V4-Flash-FP8 decode
#3915 perf(unified_attention): use 8 warps for gfx1151 3D decode
#4317 tune: a8w8 gemm tuning for Qwen3.5 MXFP4-AttnFP8
#4375 [Bug Fix] fix flyDSL MoE sorting graph capture break with dp attn + ep
```

plus `#4313`, a revert of a CK repin. A downstream consumer reading the `v0.1.19` notes would reasonably conclude only MoE changed, and would not think to look at attention if they saw a perf or accuracy shift after upgrading.

`v0.1.17` did this well — it stated the base cut commit and listed the release-line cherry-picks explicitly. So this is not a missing standard, just one that was not applied to the last two.

### Suggested addition

Since the release CI is being built anyway, generating the notes costs one API call and removes the manual step entirely:

```bash
gh api --method POST repos/ROCm/aiter/releases/generate-notes \
  -f tag_name=v0.1.19 -f previous_tag_name=v0.1.18
```

Proposed extra acceptance criteria:

- Release notes list every PR between the previous scheduled tag and this one, generated rather than hand-written.
- The notes state which tag they are diffed against, so "what changed" is unambiguous when `.post` releases are interleaved.
- CI fails if a scheduled release has no `release/vX.Y.Z` branch, or if the gap since the previous scheduled tag is not ~2 weeks.
- A release branch that has diverged from `main` is reported.

Happy to open a PR for the `README.md` part if that is useful.

