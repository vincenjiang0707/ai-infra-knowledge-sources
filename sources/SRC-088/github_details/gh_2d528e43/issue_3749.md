# [Issue #3749] Feature request: canonical reproducibility-bundle export in scripts/

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3749
state: open | updated: 2026-08-22T10:20:08Z
labels: 

## 正文

## What's already there

\`--output_path\` already saves \`git_hash\`, task versions, model config, and per-sample outputs via \`--log_samples\`. \`--check_integrity\` validates task definitions. \`scripts/model_comparator.py\` and \`scripts/regression.py\` show the existing pattern for post-processing tools.

## What's missing

A lightweight canonical hash of results for cross-run comparison. The hashing utilities in \`utils.py\` (SHA256, deterministic ordering) exist but aren't surfaced in the output for external verification. Per-sample logs can be very large; a compact fingerprint of the outputs would let two parties confirm they got the same answers without shipping multi-GB files.

## Proposal

A \`scripts/export_attestation.py\` post-processing tool — consuming the existing \`--output_path --log_samples\` outputs — that emits a small, self-describing JSON document:

\`\`\`json
{
  "model_id": "<provider/name>",
  "tasks": ["<task_id>", "..."],
  "results": [
    {"task_id": "...", "metric": "...", "value": 0.847, "stderr": 0.025}
  ],
  "results_sha256": "<sha256 of canonical encoding of model_id + tasks + results>",
  "outputs_sha256": "<sha256 of per-sample outputs>"
}
\`\`\`

The metadata fields are included alongside the hashes so the bundle is independently interpretable — a reader can see what was attested and recompute the hashes themselves to verify. Two hashes, doing different work:

- **\`results_sha256\`** — an independent re-run reaching identical headline scores produces the same digest, enabling cross-run comparison without exchanging full log files.
- **\`outputs_sha256\`** — catches divergent outputs that roll up to the same headline score (compensating errors, filter differences). If \`results_sha256\` matches but \`outputs_sha256\` doesn't, that's a flag worth investigating.

Intentionally minimal: stdlib only, no new dependencies, consumes files already on disk.

## Why it'd be useful

- **Audit trails.** When eval scores are cited, the bundle lets readers ask for the artefact and verify it matches.
- **Cross-org reproduction.** Two labs running the same eval can compare bundles without shipping logs.
- **Drift detection.** \`outputs_sha256\` diverging while \`results_sha256\` holds is a signal the existing tooling doesn't surface.

## Where this came up

While building [Valichord](https://github.com/topeuph-ai/ValiChord), a decentralised verification protocol for AI eval claims — we needed a canonical attestation format covering runs from multiple harnesses. An analogous tool is currently open as a PR against [UKGovernmentBEIS/inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals/pull/1610). Happy to draft a PR here in the same shape if there's interest.

## 评论 (12)

### wanyixu199 · 2026-05-12

You mean something like this tool?
https://benchscope.ai/compare/runs?left=59dedcad-55cc-45dd-8db0-0aa1d0d70b4d&right=f531dcc0-2c8e-407a-ba0d-daaf79621f9b

### topeuph-ai · 2026-05-13

Thanks @wanyixu199 — Benchscope's a neat tool, hadn't come across it. Useful for the "which provider runs this benchmark best?" question.

It's solving a related-but-distinct problem from what this issue proposes, though. Benchscope , if I understand it correctly, is a centralised registry: runs are hosted on their infrastructure, scores and raw outputs are inspectable through their UI, the trust model is "Benchscope faithfully reports what was run." That works well for comparison and leaderboard purposes.

The proposal here (and the work in PR #3752) is about cryptographic attestation — a small artefact a third party can verify against their own re-run without trusting a hosting party. Roughly:

- Benchscope: "trust us, here's the data" — centralised, fast for comparison
- Attestation export: "here's a hash you can verify against your own run" — decentralised, useful for audit trails and tamper-evidence

The two are complementary rather than competing. A Benchscope run could carry an attestation hash; the bundle handles the audit-trail property, Benchscope handles comparison. Different layers, different purposes.

Worth knowing about — thanks for the pointer.

### KeilerHirsch · 2026-08-14

This is very close to one of the problems we're tackling in BRONCO: treating eval output as measurement evidence, not just as a score.

We're looking at canonical manifests, provenance, hashes, repeatability/reproducibility and uncertainty before worrying about yet another leaderboard.

I'd especially like to avoid independently inventing a second incompatible attestation format. Comparing requirements or collaborating here would make a lot of sense.

BRONCO:
https://github.com/KeilerHirsch-Labs/BRONCO-AI-Metrology-Benchmarks-DIN-ISO-IEC

The ruler should probably have a serial number before we argue about millimeters. :)


### topeuph-ai · 2026-08-16

Thanks, and agreed we should compare rather than end up with two formats.

There's a working one already: valichord_attestation, v1.2, MIT.

Spec: https://github.com/ValiChord/ValiChord/blob/main/valichord_attestation/spec/attestation_format_v1.md
lm-eval adapter: https://github.com/ValiChord/ValiChord/blob/main/valichord_attestation/valichord_attestation/adapters/lm_eval_adapter.py

It reads results_*.json plus --log_samples output, so the same input #3752 is dealing
with. Canonical JSON is RFC 8785, with a SHA-256 over the content and a Merkle root over
per-sample outputs so you can disclose a subset without shipping the whole log. Six
adapters so far.

Your standards register is more careful than anything we have. We've been describing the
core check as "can someone else get the same result", which is ISO 5725 reproducibility
said badly. I'd rather use the proper terminology, assuming I've read the mapping right.

Pull the spec apart if you want to, it's been running a while.

One question though, because it changes what I'd work on next: have you got anyone lined
up who'd actually use this? A lab, PTB, a Fraunhofer institute, a DIN group? That's the
bit we haven't got.

### KeilerHirsch · 2026-08-17

Thanks — this is exactly the kind of overlap I'd rather reuse than fork into another schema.

Short answer to the institutional question: **no, I do not currently have PTB / Fraunhofer / DIN / lab adoption lined up**, and I don't want to imply otherwise. BRONCO is still in the research-first / measurement-model stage, not an adopted standard or institutional program.

That said, `valichord_attestation` looks like the right thing to evaluate as an existing implementation rather than inventing another bundle. Reusing existing field names where the semantics match is strongly preferable.

What I'd propose next is a concrete compatibility review rather than a new format:

1. take the v1.2 attestation spec as the baseline;
2. map BRONCO's provenance / repeatability / reproducibility / uncertainty requirements onto it;
3. keep fields that already cover the requirement;
4. identify only genuine gaps — judge-model parameters, prompt/rubric versions, thresholds and aggregation are obvious candidates;
5. distinguish identity/provenance fields from comparison-sensitive measurement claims so a hash doesn't accidentally become a claim of reproducibility by itself.

If the result is "ValiChord already solves 80% of this and BRONCO should just reference it", that's a good outcome, not a failure.

And yes: your ISO 5725 reading is directionally where we're going, but I'd be careful with the terminology. "Same result again" can mean repeatability or reproducibility depending on which conditions changed; I'd rather encode those conditions than use either word as a generic synonym for rerun consistency.

If you're good with that, I'll treat the v1.2 spec as the baseline artifact for the crosswalk.


### topeuph-ai · 2026-08-17

Yes, baseline on v1.2.
One caveat before you start, because it'll save you redoing a section. The Merkle
construction is moving in v2. Two things: there's no leaf/node domain separation, it's
sha256(left + right) with no tags, and odd levels pad by duplicating the last node so
[A,B,C] and [A,B,C,C] hash to the same root. The first has been a deferred item since a
security audit on 2026-07-05. The second I found this week. Both land in the same bump
because our spec treats any Merkle change as breaking.
Everything else is stable. JCS canonicalisation, the field set, the two-hash split. Map
against v1.2 as it stands and treat the tree as provisional.
Your point 5 already exists, which is worth knowing before you spend time on it.
bundle_hash covers the whole artifact. content_hash excludes a free-form meta block, so
provenance that legitimately varies between runs doesn't make two identical measurements
compare unequal. That's the identity-versus-claim split you're describing.
On your gap list: someone working on a different eval platform landed on the same three
last week without seeing your comment. Judge-model parameters, prompt and rubric
versions, thresholds and aggregation. Two people finding the same holes separately is
worth more than either of us reasoning about it alone.
You're right about ISO 5725 and I'll drop the sloppier phrasing. Encoding which
conditions changed is more useful than picking one of the two words anyway, and it maps
onto what a bundle already carries.
Noted on the institutional side, and it doesn't change anything from my end.



### topeuph-ai · 2026-08-18

Heads up in case it changes your baseline: format v2 shipped yesterday.

Short version, it shouldn't. v2 changes the Merkle construction to RFC 6962 §2.1
and nothing else. The field set you're crosswalking against is identical, both
hashes are computed the same way, and the challenge-response protocol is
unchanged. The v1.2 spec stays normative for v1.x bundles, so your mapping work
holds as-is — just cite v2 as current, spec/attestation_format_v2.md.

The three gaps you identified are still gaps and are not addressed by v2:
judge-model parameters, prompt and rubric versions, thresholds and aggregation.
If your crosswalk lands on a concrete field proposal for any of them, that's the
useful input, and it would be arriving at the right moment.

### KeilerHirsch · 2026-08-19

This is exactly the overlap I wanted to find before BRONCO freezes a schema.

ValiChord already having RFC 8785 canonicalization, content/bundle hashes, per-sample Merkle commitments, repo/harness provenance and manifest binding changes the design question substantially. I do not want BRONCO to rename working concepts just to manufacture another format.

My current instinct is:

- reuse compatible ValiChord field names and semantics where they already cover the requirement;
- let BRONCO specify the measurement layer that is still missing: requested vs observed model identity, judge configuration, prompt/rubric revision, thresholds/aggregation, repeatability/reproducibility conditions, uncertainty and comparison validity;
- treat attestation as evidence transport/binding, not as proof that the measurement design itself is valid.

And the honest answer on institutional adoption: no, I don't currently have PTB, Fraunhofer or a DIN group lined up. BRONCO is deliberately research-first at this stage. I'd rather arrive with a technically attacked measurement model and interoperable prototype than ask a metrology institute to bless a PowerPoint. :)

Your offer to review a manifest draft is very useful. I'll take you up on that, and I'll read the ValiChord spec as a compatibility target rather than a competing schema.

If we can make the ruler share a serial-number format before anyone starts selling rulers, that's already progress.


### topeuph-ai · 2026-08-19

Your third bullet is the invariant, better put than our own spec puts it. ValiChord
is the envelope: independent, blind, tamper-evident verdicts. The check itself
always lives outside the protocol, in an instrument or a person. That's why it's
domain-agnostic, and it's also why "reproduced" never means "correct" — it means
someone who wasn't involved got the same answer. If BRONCO specifies the
measurement layer and treats attestation as transport and binding, the split is
right and neither of us is doing the other's job badly.

The practical thing before you freeze anything: everything on your middle list can
land as optional fields without breaking a version. The spec's rule is that new
optional fields are additive within a version family, absent optional fields are
omitted from canonical encoding rather than serialised as null, and readers ignore
what they don't recognise. So a bundle without judge configuration hashes exactly
as it does today, and one with it is still a conforming bundle. You don't need us
to cut a release, and you don't inherit a migration.

Worth knowing you're not guessing about the gaps. Two other people building
against this format in the last week — different projects, no contact with each
other or with your comment — independently landed on the same three: judge-model
parameters, prompt and rubric versions, thresholds and aggregation. Three
independent readings converging on the same absence is better evidence than any of
us reasoning about it alone, and it's a reasonable basis for you to specify that
layer rather than wonder whether it's wanted.

Yes to the manifest draft — send it whenever. The thing I'd look hardest at is your
first item, requested versus observed model identity. We have one model_id field
and it quietly assumes those are the same, which is fine until a provider silently
routes you elsewhere, and then it's the field that was wrong all along.

On the institutional answer: that's the right way round, and I'd have thought less
of the opposite. A technically attacked model is worth more than an endorsement of
something nobody has tried to break.

### KeilerHirsch · 2026-08-20

That requested-vs-observed identity point is probably the best concrete place to start the manifest crosswalk.

I would avoid overloading `model_id` and make the distinction explicit, roughly:

- requested_model_id
- observed_model_id
- routing/fallback evidence
- identity_observation_method
- provider/runtime identity if available
- unknown/not_exposed as a legitimate state rather than silently copying requested -> observed

The important part is that "observed" must mean evidence actually exposed by the serving system or an auditable runtime field, not what the client assumes it received.

The convergence on judge configuration, prompt/rubric revision and thresholds/aggregation is also strong enough now that I think BRONCO should specify that layer rather than merely list it as an open question.

I'll make the first artifact a compatibility crosswalk rather than a competing manifest. Then we have something concrete for you to attack.


### topeuph-ai · 2026-08-20

Adopted as the working shape, and your constraint on "observed" is the part I'd keep
even if the field names change. Evidence exposed by the serving system rather than
what the client assumes it received is the same rule we arrived at from a different
direction — don't decide from the summary written by the party with an interest —
and a Holochain project I'm working with landed on it independently a third time
last month. Worth stating once in the spec rather than rediscovering per field.

It's written up as item 01 here, with your name on it:
https://github.com/ValiChord/ValiChord/tree/main/valichord_attestation/spec/format-backlog

One thing your list doesn't settle, and it decides whether the field set works.
Which of the six does content_hash cover?

content_hash exists to answer "are these the same claim", and deliberately excludes
the free-form provenance block so two reruns differing only in who triggered them
compare as equivalent. If observed_model_id sits outside it, two runs against
genuinely different actual models also compare as equivalent — the exact failure the
field exists to prevent. If it sits inside, a provider silently upgrading a point
release changes the hash of an otherwise identical rerun. That's correct, and it
will surprise someone, so the spec should say it out loud rather than let them find
out.

My instinct is observed inside, routing evidence outside, and identity_observation_method
inside because it changes how much the observation is worth. But that's an instinct,
and it's the same question hanging over judge configuration and rubric versions, so
it may be one decision rather than four.

Routing/fallback evidence is the item I'd watch. It's the one that can balloon — a
provider-opaque blob is honest and unverifiable, a schema won't survive the next
provider.

Crosswalk-before-manifest is the right call. Send it when it's ready and I'll attack
it properly rather than politely.

### topeuph-ai · 2026-08-22

@KeilerHirsch — the conformance document exists now: https://github.com/ValiChord/ValiChord/blob/main/valichord_attestation/spec/conformance.md

You said you'd rather treat this format as a compatibility target than fork it. Until today there wasn't much to conform to — a line saying an implementation "should" reproduce the vectors, and no requirements anywhere. Now there are 23 numbered ones, and §6 says that if any of them isn't supported by the format specs, that's a bug in the conformance document rather than something you have to work around.

The repeatability/reproducibility distinction you raised is in there as §3.15–3.16. The field is still open; only the vocabulary is settled.

Discussion here, which is where format design should have been happening all along rather than on this tracker: https://github.com/ValiChord/ValiChord/discussions

Apologies to the lm-eval maintainers for the drift — the ValiChord schema conversation moves off your issue tracker as of now. This issue stays open for the original request, which is still unanswered and has PR #3752 sitting against it.
