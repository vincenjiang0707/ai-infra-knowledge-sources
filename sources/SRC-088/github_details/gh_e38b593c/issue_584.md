# [Issue #584] [RFC]: Response-regeneration refactor — resumable, multi-split, quality-filtered training data (related to RFC#583)

source: https://github.com/vllm-project/speculators/issues/584
state: open | updated: 2026-07-01T17:03:27Z
labels: RFC

## 正文

### Motivation.


`scripts/response_regeneration/script.py` regenerates assistant responses in existing
datasets against a vLLM-served model, producing the conversation JSONL that
`prepare_data.py` turns into draft-training data. As the datasets and models grew, the
original tool hit several limitations:

1. **Resume is unreliable.** Resume is keyed on a per-row `id` that is the source UUID
   *or* a positional `sample_{idx}` fallback. Index-based ids shift whenever the source is
   re-ordered, filtered, or re-split, so a crashed multi-hour job could not be trusted to
   skip exactly what it had already written — it could re-do or, worse, skip the wrong rows.
   There is no single stable identity across the different source schemas the pipeline is proposed to
   ingests.

2. **One split, one file.** Multi-split datasets (e.g. `nemotron` with `stem`/`code`/`chat`/
   `math`) have no first-class handling, and there is no way to fan results out into a tidy
   per-split bundle.

3. **Rows with no utility for training.** On a failed generation it still emitts a
   *user-only* conversation (no assistant turn), and it writes responses that hit `--max-tokens`
   (`finish_reason="length"`, i.e. likely truncated) with no way to filter them. Both pollute
   the downstream SFT/draft data.

4. **Single-turn only.** There is no way to regenerate *multi-turn* assistant responses by
   walking a conversation and regenerating each assistant turn from the regenerated prefix.

5. **Fragile requests, thin observability.** vLLM calls have no bounded retry/backoff/timeout
   policy, and the run gives little accounting of what happened to each row.

### Proposed Change.

Refactor the regenerator around three goals — **safe resume**, **output quality**, and
**multi-split awareness** . The user-facing contract
changes are:

- **Stable identity + resume.** Each output row carries `metadata.primary_id`, chosen
  deterministically from the source (`id` / `uuid` / selected metadata fields, else a stable
  content hash of the source row) with a `primary_id_source` recording which. `--resume` skips
  rows already present **by `primary_id`**, and still understands the legacy key so outputs
  from the old tool can be continued. A `secondary_id` (currently the row index) is kept for
  monitoring only.

- **Output modes.** `--output-mode single` writes one JSONL (`--outfile`, or an auto-named
  file under `--output-dir`); `--output-mode bundle` writes one
  `{dataset}_{split}_{model}.jsonl` per split under a directory.

- **Turn modes.** `--turn-mode single` (default) regenerates the first turn;
  `--turn-mode multi` iteratively regenerates assistant turns from the regenerated
  conversation prefix and stops at the first undesirable generation.

- **Quality filtering.** Rows that never produce a valid assistant response are **dropped**
  (no user-only conversations leak into the training data). Length-finished responses are
  **dropped by default** because they may be truncated; `--keep-length-finished` keeps them
  (and, in multi-turn mode, writes the prefix and stops after the length-finished turn).

- **Multi-split presets.** Presets that expose multiple splits process each one; `--limit`
  counts **new** rows queued *per split* (rows skipped by resume, language filtering, or
  source validation don't count against it).

- **Robustness + accounting.** `--max-retries` / `--retry-backoff` / `--request-timeout` bound
  every vLLM request. Each sample logs exactly one terminal outcome (`skipping`,
  `new_written`, `new_written_partial`, `new_skipped`), and each split plus the whole run
  print reconciled counters where `processed = pre_existing + written + dropped`.

### Any Other Things.

- **drop length-finished by default.** Dropping by default is the safe choice for general training, but can be flipped in case of speculators.

## 评论 (10)

### WindChimeRan · 2026-06-30

On-policy training — I'll take the lead on this.

Quick framing: 
* In **off-policy** training the draft model learns from the dataset's original assistant responses (human- or other-model-written). 
* In **on-policy** training we first regenerate those responses with the target/verifier model, so the draft trains on the distribution the target actually produces at inference. Off-policy introduces train/infer misalignment (exposure bias) that lowers acceptance rate, so on-policy should be the default for both training and eval.

Three tasks (PRs):

- **[Data]** Response regeneration should support multi-turn (currently single-turn only). The driver is exposure bias: off-policy multi-turn data conditions each turn on the dataset's responses rather than the target's, so every turn past the first is misaligned. Regenerating turn-by-turn against the on-policy prefix fixes this — and yields longer, more realistic context as a bonus.
- **[Doc]** Make on-policy the documented default for training and eval. Keep off-policy as a cheaper fallback (it skips a full target-model pass over the data) with its acceptance penalty called out, so the tradeoff is explicit.
- **[Eval]** Evaluation must be on-policy; the current fixed last-10% split is off-policy ground truth. Two options:
  - **Option A** — verifier generates on-policy ground truth online during evaluation.
  - **Option B** — verifier generates on-policy ground truth offline during data prep, carved into the eval split.

cc: @shanjiaz 

### shanjiaz · 2026-06-30

@imargulis Thanks for putting out this RFC. We are interested in the following changes:

1. **Reliable resume**: adding and saving a `primary_id`. Not sure if we would need a `secondary_id` tho, what would it be for?
2. **Quality filtering**: drop rows that never produce a valid assistant response, but keeping length-finished responses by default.
3. **Robustness**: --max-retries / --retry-backoff / --request-timeout are all good practice. Not too sure about the labeling skipping, new_written, new_written_partial, new_skipped, but a summarization on the regeneration run on what's dropped/kept/skipped could be helpful.
4. **Multi-turn generation**: We definitely should implement multi-turn generation. Please work with @WindChimeRan on this bit. 
Let us know what you think and feel free to reach out with any questions! Thanks.

### shanjiaz · 2026-06-30

@WindChimeRan Thanks for the thoughtful RFC. Definitely start working on multi-turn generation. I think updating out docs/examples with regenerated data makes a lot of sense too. For the validation bit, I'm not sure it's worth the complication. Let me know what you think! Other features I think might be worth looking into is this [PR](https://github.com/vllm-project/speculators/pull/510)
1. We want to potentially add a concurrency sweep step that runs the regeneration at different concurrency levels (64, 128, 256, 512, 1024), and reports throughput. This needs some validation but maybe before we kick off a long run it would be worth finding out the optimal throughput.
2. Dataset shuffling — adds --shuffle / --shuffle-seed / --shuffle-buffer-size to script.py because some datasets are ordered by topic, which can bias throughput measurements.

### imargulis · 2026-07-01

@shanjiaz @WindChimeRan Thanks a lot for looking into this.

@shanjiaz 

1. **Resume / primary_id** — Agree. On secondary_id: it's only the source row index kept for monitoring; it has no role in resume or output identity. Since you (rightly) question its value, I'll drop it and keep only primary_id (+ primary_id_source) as it serve me for monitoring only.

2. **Quality filtering** — Agree, including your stance on: keep length-finished responses by default. My RFC dropped them by default but I mentioned the opposite approach as viable; The decision — always drop rows with no valid assistant turn, but keep finish_reason="length" rows by default.

3. **Robustness** — Agree on --max-retries/--retry-backoff/--request-timeout. On accounting: I'll drop the per-row terminal labels (new_written/new_written_partial/new_skipped) and replace them with a summary you proposed.

5. **Multi-turn** — Agree it's essential; I'll coordinate with @WindChimeRan, who's leading it. 



### shanjiaz · 2026-07-01

@imargulis Awesome! Thanks for the quick response. @WindChimeRan Just opened up a [PR](https://github.com/vllm-project/speculators/pull/693) on multi-turn, please take a look! Thanks.

### imargulis · 2026-07-01

@shanjiaz Before proceeding further would you give some feedback on 

> - **Output modes**. --output-mode single writes one JSONL (--outfile, or an auto-named
> file under --output-dir); --output-mode bundle writes one
> {dataset}_{split}_{model}.jsonl per split under a directory.
> 
> - **Turn modes**. --turn-mode single (default) regenerates the first turn;
> --turn-mode multi iteratively regenerates assistant turns from the regenerated
> conversation prefix and stops at the first undesirable generation.

I have a ready implementation addressing all 4 points in your previous message but with `--output-mode` and `--turn-mode` implemented.
I think `--turn-mode` can be easily dropped and defaulted to multiturn always. As for `--output-mode`, it might be a valuable addition.

I will update my implementation depending on the feedback and will coordinate with @WindChimeRan to find the best way to move forward.

Thanks
 

### shanjiaz · 2026-07-01

@imargulis Could we break it up into different PRs since they're relatively independent? Let's drop turn modes for now and make multi-turn the default. I'm not sure output modes would matter much since now we have updated the data preprocessing pipeline to be able to consume both a directory and single jsonl file. Is there a specific use case you have in mind?

### imargulis · 2026-07-01

> [@imargulis](https://github.com/imargulis) Could we break it up into different PRs since they're relatively independent? Let's drop turn modes for now and make multi-turn the default. 

@shanjiaz I think we can break it up into several PRs. 

> I'm not sure output modes would matter much since now we have updated the data preprocessing pipeline to be able to consume both a directory and single jsonl file. Is there a specific use case you have in mind?

To the best of my recollection the regenerated data is flushed into a single file (I'm thinking of nemotron multi split dataset for example). I found it inconvenient and not only due to the resulting file-size. I'd prefer to keep regenerated data subdivided into splits. But obviously it a matter of preferences. And BTW I left a comment regarding the  updated preprocessing pipeline [here](https://github.com/vllm-project/speculators/pull/675#issuecomment-4844139339)




### WindChimeRan · 2026-07-01



> For the validation bit, I'm not sure it's worth the complication.

Agree. After we set multi-turn regen as the default, the on policy val will come for free. My concern was just that off policy validation is not very meaningful. Will make it clear on the doc PR. 

> Dataset shuffling ... 

Agree. And this sounds easy to implement. Maybe I'll include it in #693

---

Followup PR, out of scope of #693: 

- Reliable resume: `primary_id`. `secondary_id`  ... --> not sure if we already have already implemented a resume mechanism. If we really need one, we can open a separated PR. 
- Quality filtering &  Robustness: Prefer to open a separated PR on these. Because it would be more solid if we can report some dataset statistic on our supported presets. what's dropped/kept/skipped. Need to run real experiments. 
- concurrency sweep: please check the comments in the next reply. 

---

I opened up a roadmap: #694 . will revise it & implement some high-value & low-effort ones soon. 

### WindChimeRan · 2026-07-01

For concurrency sweep #510

I think regen is just a standard vllm offline inference task. And the user should pick the concurrency number according to the recipe, e.g., https://recipes.vllm.ai/zai-org/GLM-5.2 `--max-num-seqs 32 — the single knob for fitting 1M context; start at 32 and tune it to your VRAM (up on headroom, down on OOM).`


