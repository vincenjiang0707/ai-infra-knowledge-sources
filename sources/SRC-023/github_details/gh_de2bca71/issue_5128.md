# [Issue #5128] [skills] Make kernel-review tooling measurable: corpus, growth mechanism, promotion bar

source: https://github.com/ROCm/aiter/issues/5128
state: closed | updated: 2026-08-31T05:57:21Z
labels: 

## 正文

Follow-up to #4870, filed before it merges so the sequence after it is on the record rather than
promised.

#4870 lands a review/validation layer at the **advisory tier**, which is the right tier for its
evidence — and also where the evidence stops. Its own description states the historical campaign is
local and makes no durable recall or consistency claim. The PR also demonstrates why that matters:
the original D9 rule missed 0 of 3 seeded index-width defects across three revisions, and that was
only visible because someone measured it. Prose edits to review rules cannot be scored by reading
them.

This issue covers the three steps that make the tooling improvable instead of static. They are one
programme with one dependency chain, so they are one issue.

---

### Step 1 — Commit the corpus as a replayable asset

The durable part of #4870 is not the skill text, it is the labelling methodology behind it: 14 PRs,
17 defects, each pinned to its merge commit, labels taken from the `[Fix]`/revert PRs. Today that
lives in a PR description and evaporates on merge.

- `corpus/defects.jsonl` — one record per labelled defect: introducing PR, merge SHA, file/line,
  family, severity, fixing PR, one-line description.
- `corpus/replay.sh` — checks out each case at its merge commit, time-boxes `gh`, runs the skill
  under test, scores against the labels, repeats n times.
- `corpus/metrics.json` — committed: corpus version, skill SHA, per-family recall@5, false-clearance
  rate, findings/PR, n, variance.
- **`train`/`holdout` split from the first commit.** Retrofitting it once numbers are quoted is
  expensive, and without it the ratchet overfits — #4870's production-scale table already shows the
  risk, since the scale facts came from the same fix PRs that define the labels.

Seed data: four reports from an independent gfx942 run of head `706eafafc` against ROCm/aiter#5089
are available as the first holdout records — as-shipped, instrumented, a seeded positive control
that correctly returned `BLOCK`, and a post-fix run. Details in #4870.

**Done when** one command reproduces the reported numbers, so any rule edit can be scored before and
after.

### Step 2 — Make the corpus grow for free

A corpus that only grows when someone remembers to grow it is a one-off engineering project, not an
asset. The mechanism already exists in this repo's workflow: every `[Fix]` and revert PR is by
construction a labelled defect with a known introducing commit, a known fixing commit, and a
maintainer who has just finished understanding it.

Add one step to the contributing guidance for `[Fix]`/revert PRs: append the record to
`corpus/defects.jsonl`. The fixing author is the cheapest possible labeller — they already hold
every field.

**Done when** the step is documented and at least one `[Fix]` PR merges with its record attached.

This is the step that decides whether any of this compounds. Steps 1 and 3 without it produce a
snapshot that decays.

### Step 3 — Pay the measurement debt, and fix the promotion bar in advance

Promotion above advisory — where a clean verdict means a human skims, or where a verdict blocks —
needs evidence that does not exist yet:

| | Gap |
|---|---|
| 1 | **recall@5 unmeasured.** The finding cap is 5; reported recall is uncapped. Per-family recall *after* truncation is the number the cap should be read off. |
| 2 | **n=1 everywhere.** Nothing separates a single result from sampling noise — including the independent run reported in #4870. |
| 3 | **False clearance never scored.** `report_schema.json` was designed for exactly this (`degraded_mode`, `arch_coverage`, `isolation`); nothing measures it. |
| 4 | **No adversarial measurement.** Seeded mutants are non-adversarial — planted by the rules' author to match the rules. The skill ships in-repo, so it is detector and evasion guide at once. Suggested measure: agent A holds the skill and writes a patch with a real defect that passes; agent B reviews with the same skill; evasion rate = pass rate. |

**Promotion bar (tier B, triage):** false clearance measured and near zero for families that raise a
red verdict; no per-family recall@5 at zero; run-to-run modal agreement on red verdicts ≥ 0.8; any
"this is better" claim carrying n≥5 with variance.

**Ratchet, once the corpus exists:** no per-family recall@5 may regress and false clearance may not
rise. This also settles the finding-cap question by plotting recall@k instead of arguing it.

**Kill criteria:** if false clearance cannot be driven near zero for red-verdict families, the tool
stays advisory permanently and the mandatory-report language stays out of `review-pr`.

---

### Sequencing

Step 1 unblocks 2 and 3. Step 2 is small and should not wait for 3. None of it blocks #4870, which
should merge at advisory tier once its outstanding changes land.

## 评论 (1)

### zufayu · 2026-08-31

Closing as premature.

The measurement work described here only has a trigger when someone proposes to change the review
rules, or proposes to let the tool gate a merge. Neither has happened: #4870 is still unmerged and
explicitly advisory-tier, and nobody is currently editing the rules. Building a scoring harness for
a tool that is not yet in use would produce infrastructure that decays before it is needed. When
someone does want to argue that a rule change is an improvement, that is the right moment to build
the corpus, and the person making the claim is the right owner for it.

One part of this issue should survive, and it does not need an issue. The promotion bar belongs in
the skill's own header rather than here, because a header is read every time the tool is used while
an issue sinks:

> The tool stays advisory until false clearance is measured and near zero for the families that
> raise a red verdict. An LLM judgement never gates a merge; only a deterministic executor may.

I have asked for that to be recorded in `SKILL.md` as part of #4870 review.

For the record, so the reasoning is not lost: the original motivation was that the D9 index-width
rule was rewritten three times, each revision believed to be an improvement, and all three caught
0 of 3 seeded defects. That was only visible because the author measured it by hand and reported it
against his own interest. The concern is real; the response was simply premature. Will reopen when
there is a rule change to score.

