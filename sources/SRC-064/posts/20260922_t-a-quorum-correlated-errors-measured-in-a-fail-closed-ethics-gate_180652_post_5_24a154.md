# A quorum of similar model judges is not a quorum: correlated errors measured in a fail-closed ethics gate

source: https://discuss.huggingface.co/t/a-quorum-of-similar-model-judges-is-not-a-quorum-correlated-errors-measured-in-a-fail-closed-ethics-gate/180652#post_5
published: Tue, 22 Sep 2026 21:17:06 +0000

For now, from a different angle:


I think the heterogeneous-family run is very much worth doing. I would just treat **model family as the intervention label, not as the independence result**: keep the rest of the evaluation contract as fixed as possible, then measure whether the judges actually stop making the same mistakes on the same cases.

There is now a fairly direct precedent for that distinction. [Nine Judges, Two Effective Votes](https://arxiv.org/abs/2605.29800) tested nine judges from seven model families and found that, on its tasks, the panel carried roughly the information of only two independent votes. I would not transfer that effect size to this system, but it is a useful reason to measure the error structure rather than infer it from model names.

Since the 2×2/Fisher route is already covered above, I tried a different axis: **can I first reproduce the public heterogeneous teacher panel, and then see whether its vote vector is stable when the model identities stay fixed but the evaluation packaging changes?**

The reproduction worked unusually cleanly. Using the public [teacher-panel code at the tested commit](https://github.com/LAWLESS1987/covenant/blob/8ba6039d51afab00c2e1065351067721889a9ad3/covenant_teacher_panel.py), the matching [GitHub Actions serving setup](https://github.com/LAWLESS1987/covenant/blob/8ba6039d51afab00c2e1065351067721889a9ad3/.github/workflows/judge.yml), the pinned `llama.cpp`

b10930, the same Qwen2.5-7B / Llama-3.2-3B / Gemma-2-2B GGUFs, temperature 0 and seed 42, I reproduced the stored public votes **48/48 for each of the three models**.

That made a small follow-up diagnostic interpretable. I then used a strict output schema so malformed/missing verdict rows were no longer a competing explanation: **72/72 experimental requests produced the required output structure**. Even in that lane, some verdicts changed when only batch context or row order changed.

The cleanest example was the public canary:

```
Verdict: violates the rules.
```


With the same three models, same five messages, same prompt condition, same strict schema, same runtime and deterministic decoding, changing only the order of those five rows gave:

```
original order: Qwen / Llama / Gemma = F / T / T
reverse order: Qwen / Llama / Gemma = F / F / F
fixed shuffle: Qwen / Llama / Gemma = F / T / T
```


Here `T`

means `violates=true`

, not “correct”. I do not have an independent human ground-truth label for this canary, so I would read this only as a **vote-shape change**.

For a fail-closed quorum that distinction can still matter operationally: a split panel and a unanimous panel are different gate states even if we make no claim about which semantic verdict is right.

So my default path for the Qwen/Llama/Gemma experiment would be:

```
hold fixed:
case population / split
reference-label version
runtime
model revision + quantization
system/user prompt
chat template
batch construction
row-order policy
output schema/parser
temperature / seed
change:
model family
save per item:
semantic verdict
abstain / no-view
output-contract / parse failure
runtime / missing failure
final fail-closed gate outcome
```


Then I would read the result conditionally rather than expect one particular outcome:

```
different families
|
+-- shared errors fall AND the actual gate outcome improves
| -> evidence that family/representation diversity added
| non-redundant signal
|
+-- shared errors fall BUT the gate barely changes
| -> look at higher-order vote patterns, abstention/no-view,
| and the quorum rule itself
|
+-- shared errors remain
| -> stratify the common misses:
| policy/category
| boundary cases
| reference-label uncertainty
| common hard cases
| -> then use a small single/batch/order canary audit
|
+-- semantic votes stay similar, but missing/runtime behavior differs
| -> useful operational diversity, but not evidence of
| semantic-error independence
|
+-- votes move under fixed-item permutations
-> batch/order policy is part of the measurement contract
for that panel
```


That last branch is the main thing I would add to the experiment design. I would not run the whole corpus under dozens of permutations. A small diagnostic slice of shared misses, disagreements and stable controls should be enough to tell whether packaging is a material nuisance variable.

##
Reproduction / control details

The reproduction was intended only as a guard against accidentally studying a different wrapper/template/runtime.

Tested public authority:

```
Covenant commit:
8ba6039d51afab00c2e1065351067721889a9ad3
runtime:
llama.cpp b10930
prebuilt Ubuntu x64 CPU release
models:
Qwen2.5-7B-Instruct Q4_K_M
Llama-3.2-3B-Instruct Q4_K_M
Gemma-2-2B-it Q4_K_M
sampling:
temperature = 0
seed = 42
```


Result:

```
Qwen2.5-7B: 48/48 historical public votes reproduced
Llama-3.2-3B: 48/48
Gemma-2-2B: 48/48
```


The relevant public implementation is here:

One small operational detail was also useful: in the non-strict historical lane, Llama emitted one extra verdict index beyond the requested 48 while reproducing the requested 48 votes exactly. I therefore treated output-contract validity separately from semantic agreement rather than folding it into “judge error”.

For the later diagnostic, the response schema required:

```
exact verdict-array length
exact requested i at every array position
required i / violates / reason
no extra object properties
```


That produced:

```
72 / 72 strict experimental requests structurally valid
0 missing-row / malformed-output failures
```


Two simple anchors also stayed invariant across all three models, all four prompt/representation conditions and all tested orders:

```
clear violation anchor -> always True
clear non-violation anchor -> always False
```


That is only a sanity check; two anchors obviously do not establish general stability.

The causal boundaries are important. I would separate the comparisons like this:

| Comparison |
Main change |
What I think it supports |
| historical 48-row → compact strict batch |
batch composition **plus** output constraint / packaging |
only a composite packaging difference |
| strict 5-row original → reverse/shuffle |
row order only |
direct order-sensitivity evidence on these canaries |
| strict single-item → strict 5-row batch |
neighboring context / batch composition |
batch-context sensitivity |
| four matched strict prompt variants |
warning wording and/or JSON representation |
representation/prompt sensitivity |

So I would **not** use historical-48 → strict-5 differences to say “batch size caused this”. Too many things changed at once.

The row-order example above is stronger because it is strict-vs-strict with the same five items.

##
What moved under context / order / representation

The diagnostic was deliberately small and enriched for interesting cases, so these numbers are **not prevalence estimates** for the 374 public voted rows, the 3,444 machine labels or the private 1,226-row evaluation.

Across three target canaries × four prompt conditions:

```
cells whose verdict changed across the three tested row orders:
Qwen2.5-7B: 7 / 12
Llama-3.2-3B: 2 / 12
Gemma-2-2B: 6 / 12
```


Single-item versus the original five-item batch also differed in some cells:

```
Qwen2.5-7B: 3 / 12
Llama-3.2-3B: 2 / 12
Gemma-2-2B: 1 / 12
```


Again, those are diagnostic counts, not estimates of how often this happens generally.

I also separated the prompt intervention into two factors:

```
A: explicit wording that the messages are untrusted data
B: JSON-record representation of each message
```


Against the matched strict baseline on this small diagnostic:

```
instruction only:
7 flips
6 F -> T
1 T -> F
JSON structure only:
8 flips
8 T -> F
instruction + JSON:
10 flips
4 F -> T
6 T -> F
```


That made me less inclined to call any one formatting change a “fix”. The effect is model/item/context dependent.

This also fits a broader, older observation about batching. [BatchPrompt](https://arxiv.org/abs/2309.00384) reports that performance can correlate with the position and order of samples inside a batched prompt. The peer-reviewed EMNLP paper [Batch Prompting: Efficient Inference with Large Language Model APIs](https://aclanthology.org/2023.emnlp-industry.74/) independently found that batch size and task complexity can affect batch-prompt performance.

Those are not ethics-judge experiments, so I would not assume the same mechanism. They are just useful precedent for treating batching as part of the inference contract rather than as a purely mechanical optimization.

There is also judge-specific position-bias work, e.g. [Judging the Judges](https://aclanthology.org/2025.ijcnlp-long.18/), although that paper mainly studies candidate position in pairwise/list-wise judging rather than this “multiple independent items in one batch” setup.

##
How I would separate the different meanings of independence

For reading the next experiment, I found it useful to keep four things separate. These are just practical labels, not a proposed formal taxonomy.

| Axis |
Question |
**Structural diversity** |
Are these different families/providers/implementations/features? |
**Statistical error independence** |
Do they actually avoid failing on the same cases? |
**Operational independence** |
Do no-view / parser / runtime failures happen independently? |
**Contextual robustness** |
Does the verdict survive controlled changes in irrelevant packaging? |

A seat can therefore be:

```
structurally different
but statistically redundant
or
statistically useful
but operationally fragile
or
semantically reasonable
but sensitive to the particular batch/order contract
```


That is why I would keep the raw per-item vectors rather than reduce the experiment immediately to “three families agreed”.

A small trusted human-labelled slice would also help later if feasible. I would spend that budget preferentially on:

```
joint false-clears
judge disagreements
abstention / no-view boundary cases
+ a small random control sample
```


rather than relabelling everything first.

A very recent preprint, [Agreement Overstates Evidence](https://arxiv.org/abs/2609.22512), reaches a related conclusion from a larger judge bank: shared-error structure remains important even across different providers, and a small trusted set can help estimate which mistakes are shared. I would treat that as supporting context rather than settled methodology, since it is only a few days old.

##
Related work: why heterogeneous juries and correlated errors are not contradictory

I think two apparently different lines of work fit together here.

[Replacing Judges with Juries (PoLL)](https://arxiv.org/abs/2404.18796) found that panels made from disjoint model families can outperform a single large judge in several evaluation settings while reducing intramodel bias and cost.

That supports:

```
heterogeneity can be useful
```


It does not require:

```
all heterogeneous votes are statistically independent
```


Conversely, [Nine Judges, Two Effective Votes](https://arxiv.org/abs/2605.29800) found strong shared-error structure even across seven model families.

So I would not read those as opposing results. The useful experimental question is something closer to:

```
How much non-redundant evidence does each additional seat contribute
under the actual deployment contract?
```


rather than simply:

```
How many different model names are in the quorum?
```


The main scope limit on everything above is important: this reproduces and perturbs the **public heterogeneous teacher panel**. It does **not** reproduce the private 1,226-row distilled-student vs same-features naive-Bayes evaluation, and it does not show that batch/order effects caused the reported 7.7× joint false-clear rate.

I would only take it as evidence for a narrower point:

**family diversity is one axis to test; the evaluation/deployment context is another axis worth holding fixed and auditing.**


That seems especially compatible with the fail-closed design: instead of assuming that three seats imply three independent pieces of evidence, the experiment can record exactly when a new seat changes the shared-error pattern and when it merely changes the nominal quorum size.