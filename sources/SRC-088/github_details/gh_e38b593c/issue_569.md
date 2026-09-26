# [Issue #569] [RFC]: Explicit draft-model config contract for training and vLLM launch

source: https://github.com/vllm-project/speculators/issues/569
state: open | updated: 2026-09-06T18:45:39Z
labels: stale, RFC

## 正文

### Motivation.



## Motivation.
Today the draft decoder architecture is derived implicitly from the verifier, so there is no supported way to train a draft whose decoder differs from the target (e.g. a Qwen3-style DFlash draft for a Qwen3 verifier). Several sharp edges cause silent, hard-to-debug failures:

- **MoE verifiers have no sensible default draft width**, so training picks a wrong dense width or fails obscurely.
- **`--target-layer-ids` means different things** in `launch_vllm.py` vs `train.py` (auxiliary-only vs auxiliary + verifier-final). Worse, published configs disagree by an off-by-one: DFlash stores `dflash_config.target_layer_ids`, while Eagle/speculator configs store `aux_hidden_state_layer_ids` / `eagle_aux_hidden_state_layer_ids` one index higher. A mismatch silently corrupts training targets — the last auxiliary layer gets consumed as the verifier-final hidden state.
- **Nothing validates** that the hidden-state files a run consumes contain the expected number of layers, so a wrong `--target-layer-ids` (or a `--no-include-last-layer` launch) fails deep in training, if at all.


### Proposed Change.

## Proposed Change.
Introduce one "draft-config contract" shared by training and serving:

- Add `--draft-config` (HF model id or local config path) to `train.py` and `launch_vllm.py`. Draft decoder parameters (intermediate size, head dim, attention heads, hidden layers) are read from it; explicit CLI flags (`--num-layers`, `--draft-hidden-act`, …) then override. The draft hidden size must match the verifier (the mismatch case is deferred — see below).
- Define the default draft width when `--draft-config` is absent: dense verifiers reuse `intermediate_size`; MoE verifiers infer a dense width from active-expert capacity (`num_experts_per_tok * moe_intermediate_size + shared_expert_intermediate_size`); otherwise `--draft-config` is required, with a clear error.
- Establish a **single canonical "capture" convention** for auxiliary layer ids — 0-based verifier decoder-layer indices, excluding the verifier-final layer. `aux_hidden_state_layer_ids` and `eagle_aux_hidden_state_layer_ids` are already canonical; `dflash_config.target_layer_ids` is `canonical - 1`, matching vLLM's speculators loader (vllm-project/vllm#40727). Resolution converts every present field to canonical *before* comparing, so the two real-world config flavors are treated as equivalent and only genuine disagreements warn.
- Make verifier-final-layer handling explicit: `--target-layer-ids` is auxiliary-only everywhere; `launch_vllm.py --include-last-layer` (default on) appends the verifier-final layer for extraction; training validates that each hidden-state sample carries `len(aux) + 1` layers and fails loudly otherwise, with docs/warnings guarding the silent-mismatch case.
- Allow the draft architecture to differ from the target (`--draft-arch qwen3`, usable for DFlash Qwen3 serving).
- Rename the model factory argument `verifier_config` → `draft_config` (it always described the draft), keeping `verifier_config=` as a deprecated alias and threading real verifier metadata through `target_model_config`. Vocab mapping (`t2d`/`d2t`) becomes a no-op when draft and verifier vocab sizes match, and is required (both together) when they differ.


### Any Other Things.

## Any Other Things.
- **Out of scope (deferred):** training with a draft hidden size that differs from the verifier. The contract currently **fails fast on a hidden-size mismatch**; supporting it via input/output projection adapters is a separate decision and is a possible follow-up RFC.
- **Scope:** `scripts/{train,launch_vllm}.py`, `src/speculators/model.py`, `models/{dflash,eagle3,peagle}/core.py`, `models/utils.py`, `train/data.py`, plus docs and tests. This is the foundational change in the series — the data-safety issue builds on it (draft-config serialization), and the workflow/examples issues reference its CLI flags.
- I have a complete, tested implementation ready to open as the first PR once greenlit.

## 评论 (7)

### fynnsu · 2026-06-03

> Today the draft decoder architecture is derived implicitly from the verifier, so there is no supported way to train a draft whose decoder differs from the target (e.g. a Qwen3-style DFlash draft for a Qwen3 verifier)

This is not true. The architectures are generally fixed for specific draft algorithms. Eagle-3 and P-Eagle use llama draft layers and DFlash uses qwen draft layers, regardless of the verifier model. This is what vLLM supports serving currently. There is some exploratory work being done on adding qwen draft layer support for Eagle-3 and P-Eagle, but beyond that we aren't currently looking into expanding the number of draft architecture layers.

> MoE verifiers have no sensible default draft width, so training picks a wrong dense width or fails obscurely

Yeah, MoE verifier support isn't perfect, especially because the drafters are currently always dense.

> --target-layer-ids means different things in launch_vllm.py vs train.py (auxiliary-only vs auxiliary + verifier-final). 

Yes, this is intentional. `--include-last-layer` is enabled by default so that users can specify the same list of `--target-layer-ids` to both `launch_vllm.py` and `train.py`. We need the first script to also run with the last layer (which is used for training targets), but don't want to save that to the model config. 

> Worse, published configs disagree by an off-by-one: DFlash stores dflash_config.target_layer_ids, while Eagle/speculator configs store aux_hidden_state_layer_ids / eagle_aux_hidden_state_layer_ids one index higher. A mismatch silently corrupts training targets — the last auxiliary layer gets consumed as the verifier-final hidden state.

Not entirely sure I understand what is meant by this. 

> Nothing validates that the hidden-state files a run consumes contain the expected number of layers, so a wrong --target-layer-ids (or a --no-include-last-layer launch) fails deep in training, if at all.

Yes, the user has to pass the same `--target-layer-ids` to both scripts, otherwise this is likely to fail. Unfortunately it's difficult to get around this with the current hidden states extraction system. That being said, if the hidden states file has the run number of layers (with maybe one exception), the training will immediately crash due to a shape mismatch. It wouldn't fail deep in training.

> Add --draft-config (HF model id or local config path) to train.py and launch_vllm.py. Draft decoder parameters (intermediate size, head dim, attention heads, hidden layers) are read from it; explicit CLI flags (--num-layers, --draft-hidden-act, …) then override. The draft hidden size must match the verifier (the mismatch case is deferred — see below).

I sorta support this move. However, I think the user should be able to pass in a path to a fully ready speculative draft model config. (e.g. the thing that gets saved to checkpoints when training ends). We sorta support this already with the `--from-pretrained` arg, but the difference there is that we expect the weights to exist already. We could look into expanding `--from-pretrained` to also work if it receives a path that just contains a config file. 

I would probably argue that we should ignore/fail if the user passes in other `--num-layers` (and similar) flags. If we're loading from a pre-existing config, we should just use the values directly and if the user wants different values they can edit the config file.

> Define the default draft width when --draft-config is absent: dense verifiers reuse intermediate_size; MoE verifiers infer a dense width from active-expert capacity (num_experts_per_tok * moe_intermediate_size + shared_expert_intermediate_size); otherwise --draft-config is required, with a clear error.

We can update the MoE defaults but I think this is a separate unrelated change from the draft config one, and I'd prefer a separate pr so we can evaluate the change independently. 

> Establish a single canonical "capture" convention for auxiliary layer ids — 0-based verifier decoder-layer indices, excluding the verifier-final layer. aux_hidden_state_layer_ids and eagle_aux_hidden_state_layer_ids are already canonical; dflash_config.target_layer_ids is canonical - 1, matching vLLM's speculators loader (https://github.com/vllm-project/vllm/pull/40727). Resolution converts every present field to canonical before comparing, so the two real-world config flavors are treated as equivalent and only genuine disagreements warn.

I'm not sure what this actually looks like. We don't do any comparisons locally.

> Make verifier-final-layer handling explicit: --target-layer-ids is auxiliary-only everywhere; launch_vllm.py --include-last-layer (default on) appends the verifier-final layer for extraction; training validates that each hidden-state sample carries len(aux) + 1 layers and fails loudly otherwise, with docs/warnings guarding the silent-mismatch case.

We can add a check when loading to the data loading to make sure the shapes match. The one thing to be mindful of is that if the user is using the last-layer as input to the drafter (and also to generate targets), we need to handle that case. Because then we won't have `len(aux) + 1`, but just `len(aux)`. So maybe we have to check for that somehow. We might not being handling this case super well currently, so we should look into how we can improve it.

> Allow the draft architecture to differ from the target (--draft-arch qwen3, usable for DFlash Qwen3 serving).

Already supported, see first note.

> Rename the model factory argument verifier_config → draft_config (it always described the draft), keeping verifier_config= as a deprecated alias and threading real verifier metadata through target_model_config. Vocab mapping (t2d/d2t) becomes a no-op when draft and verifier vocab sizes match, and is required (both together) when they differ.

This sounds like the current behavior. Is this just a variable rename? We can do that if it makes sense in the context. 

> I have a complete, tested implementation ready to open as the first PR once greenlit.

Please review the comments above. I also think some of these changes are independent and can be landed separately. 




### shanjiaz · 2026-06-03

> Establish a single canonical "capture" convention for auxiliary layer ids — 0-based verifier decoder-layer indices, excluding the verifier-final layer. aux_hidden_state_layer_ids and eagle_aux_hidden_state_layer_ids are already canonical; dflash_config.target_layer_ids is canonical - 1, matching vLLM's speculators loader (https://github.com/vllm-project/vllm/pull/40727). Resolution converts every present field to canonical before comparing, so the two real-world config flavors are treated as equivalent and only genuine disagreements warn.

On this point specifically. What you are referencing are not models published by us. Only dflash models published by zlab have the `dflash_config` field, see [here](https://huggingface.co/z-lab/gemma-4-31B-it-DFlash/blob/main/config.json). We use `aux_hidden_state_layer_ids`, see [here](https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.dflash/blob/main/config.json). 

If you had read the PR description you linked here, it mentioned "It is unfortunate that the DFlash and EAGLE layer indexing semantics are different, but we're stuck with this for now". Z-lab does not follow the convention that EAGLE3 established and hence the off-by-one indexing error, but all speculators models us consistent indexing and should be serving correctly. The PR was just intended to fix z-lab checkpoints in vllm. Z-lab team is aware of this issue, see [here](https://github.com/vllm-project/vllm/pull/41703/changes#diff-99a026e9541cc4c876db35b7fb2c9cd2282b639441a88e5b17eed754dba564a8). 

Lots of good points here, per Fynn's request, let's work out a plan to get them in in separated PRs.

### imargulis · 2026-06-04

@fynnsu @shanjiaz Thanks a lot for your detailed comments.
To give you  some background, my goal was to enable the online training of a speculator for the Qwen3.5-3B-A3B target model.
Along the way I made some changes (lots of other proposals are in the pipeline) that might be worth upstreaming.

> > Today the draft decoder architecture is derived implicitly from the verifier, so there is no supported way to train a draft whose decoder differs from the target (e.g. a Qwen3-style DFlash draft for a Qwen3 verifier)
> 
> This is not true. The architectures are generally fixed for specific draft algorithms. Eagle-3 and P-Eagle use llama draft layers and DFlash uses qwen draft layers, regardless of the verifier model. This is what vLLM supports serving currently. There is some exploratory work being done on adding qwen draft layer support for Eagle-3 and P-Eagle, but beyond that we aren't currently looking into expanding the number of draft architecture layers.

I was not precise in the framing of what I consider worth addressing. When saying architecture I really meant configuration rather than architecture type. As speculator's architecture config is perceived as independent of verifier's (except for compatibility requirements), current [dependence  ](https://github.com/vllm-project/speculators/blob/4c7240fbc310f5170f1a8e4879cb33d78ac5c03c/scripts/train.py#L175) seems artificial and out of user's control. So my general proposal is to disentangle the draft configuration and derive it from the verifier in the case user does not provide any signal. So as long as an architecture type is supported give a user the agency to specify its configuration via config file or cli parameters.

> > Add --draft-config (HF model id or local config path) to train.py and launch_vllm.py. Draft decoder parameters (intermediate size, head dim, attention heads, hidden layers) are read from it; explicit CLI flags (--num-layers, --draft-hidden-act, …) then override. The draft hidden size must match the verifier (the mismatch case is deferred — see below).
> 
> I sorta support this move. However, I think the user should be able to pass in a path to a fully ready speculative draft model config. (e.g. the thing that gets saved to checkpoints when training ends). We sorta support this already with the --from-pretrained arg, but the difference there is that we expect the weights to exist already. We could look into expanding --from-pretrained to also work if it receives a path that just contains a config file.
> 
> I would probably argue that we should ignore/fail if the user passes in other --num-layers (and similar) flags. If we're loading from a pre-existing config, we should just use the values directly and if the user wants different values they can edit the config file.

I agree with your proposition, either config file or flags, ignoring the latter when a file is provided.

> > MoE verifiers have no sensible default draft width, so training picks a wrong dense width or fails obscurely
> 
> Yeah, MoE verifier support isn't perfect, especially because the drafters are currently always dense.

Putting aside the fact that drafters are dense only, switching to:

> > Define the default draft width when --draft-config is absent: dense verifiers reuse intermediate_size; MoE verifiers infer a dense width from active-expert capacity (num_experts_per_tok * moe_intermediate_size + shared_expert_intermediate_size); otherwise --draft-config is required, with a clear error.
> 
> We can update the MoE defaults but I think this is a separate unrelated change from the draft config one, and I'd prefer a separate pr so we can evaluate the change independently.

Agree, could be a separate PR.


> > Allow the draft architecture to differ from the target (--draft-arch qwen3, usable for DFlash Qwen3 serving).
> 
> Already supported, see first note.

Clarified earlier by distinguishing between architecture and its configuration.

> > Rename the model factory argument verifier_config → draft_config (it always described the draft), keeping verifier_config= as a deprecated alias and threading real verifier metadata through target_model_config. Vocab mapping (t2d/d2t) becomes a no-op when draft and verifier vocab sizes match, and is required (both together) when they differ.
> 
> This sounds like the current behavior. Is this just a variable rename? We can do that if it makes sense in the context.

Yes, pure rename for clarity.

> > Establish a single canonical "capture" convention for auxiliary layer ids — 0-based verifier decoder-layer indices, excluding the verifier-final layer. aux_hidden_state_layer_ids and eagle_aux_hidden_state_layer_ids are already canonical; dflash_config.target_layer_ids is canonical - 1, matching vLLM's speculators loader (vllm-project/vllm#40727). Resolution converts every present field to canonical before comparing, so the two real-world config flavors are treated as equivalent and only genuine disagreements warn.
> 
> 1. I'm not sure what this actually looks like. We don't do any comparisons locally.
> 
> 2. On this point specifically. What you are referencing are not models published by us. Only dflash models published by zlab have the dflash_config field, see [here](https://huggingface.co/z-lab/gemma-4-31B-it-DFlash/blob/main/config.json). We use aux_hidden_state_layer_ids, see [here](https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.dflash/blob/main/config.json).
> If you had read the PR description you linked here, it mentioned "It is unfortunate that the DFlash and EAGLE layer indexing semantics are different, but we're stuck with this for now". Z-lab does not follow the convention that EAGLE3 established and hence the off-by-one indexing error, but all speculators models us consistent indexing and should be serving correctly. The PR was just intended to fix z-lab checkpoints in vllm. Z-lab team is aware of this issue, see [here](https://github.com/vllm-project/vllm/pull/41703/changes#diff-99a026e9541cc4c876db35b7fb2c9cd2282b639441a88e5b17eed754dba564a8).

Please ignore this (and related comments) overcomplication. This zlab's format ad-hoc treatment should be dismissed if the (zlab's) config file and cli params mixture is not allowed. Simple index conversion on load is absolutely fine.


> > Make verifier-final-layer handling explicit: --target-layer-ids is auxiliary-only everywhere; launch_vllm.py --include-last-layer (default on) appends the verifier-final layer for extraction; training validates that each hidden-state sample carries len(aux) + 1 layers and fails loudly otherwise, with docs/warnings guarding the silent-mismatch case.
> 
> We can add a check when loading to the data loading to make sure the shapes match. The one thing to be mindful of is that if the user is using the last-layer as input to the drafter (and also to generate targets), we need to handle that case. Because then we won't have len(aux) + 1, but just len(aux). So maybe we have to check for that somehow. We might not being handling this case super well currently, so we should look into how we can improve it.

Matching shapes seems to be a fair safeguard. And good point regarding the last layer as an input to draft. I presume metadata can hold a flag indicating that appending last layer (during extraction) did not change the set of all layers selected for extraction, this way training process can infer (len(aux) + 1*int(flag) == len(aux)) that last layer has a dual use.

Please, let me know which points are worth addressing in your opinion and I will prepare corresponding PR(s).

P.S. I have several other proposals for improvements (I used), please give your thoughts:
1. Training workflow: draft export (dropping unnecessary weights from safetensors to save space), introduce warmup ratio, ensure correct resumable trainer state.
2. Response-regeneration package enhancements (including bug fix in resume).
3. Prepare-data multi-source ingestion & normalization.
4.  vLLM endpoint health monitoring 
to name a few. If it sounds relevant I will file separate RFCs. Thanks.

### shanjiaz · 2026-06-04

@imargulis Thanks for the quick response!

Would you be able to create RFCs for:

1. Response regeneration enhancements
2. Data preprocessing: multi-source ingestion and normalization

We're working on a plan for the other points you suggested and will reach out as we make progress. In the meantime, feel free to ping us on the vLLM Slack if you have any questions.

Also, could you share a bit more detail about the `Qwen3.5-3B-A3B` training setup? Are you training a dFlash model, fine-tuning an MTP model, or using a different algorithm? Let us know if there's anything we can help with.

### imargulis · 2026-06-08

@shanjiaz Thanks a lot for your message.

I will file the corresponding RFCs shortly.
I'll be happy to continue the interaction on Slack (I presume via DM as I do not see #speculators channel on vLLM's Slack)

Regarding the `Qwen3.5-3B-A3B` training setup. As a starting point I'm trying to produce a DFlash draft model at least as capable as the one published by the z-lab team. My first attempt did not produce a strong enough model so I decided to verify the pipeline 
by producing a DFlash model for `Qwen3-8B`. The training is still in progress but here are the intermediate results which I believe won't change drastically upon training completion.

Speculative-decoding **acceptance length (AL)** by dataset (averaged over 100 samples or 80 for MT-Bench). 
Target:`Qwen/Qwen3-8B`
Block_size: `8`

| Draft | mt-bench | gsm8k | humaneval |
|-------|:--------:|:-----:|:---------:|
| z-lab/Qwen3-8B-Dflash-bf16 | 2.64 | 3.15 | 3.07 |
| **RedHatAI/Qwen3-8B-speculator.dflash** | **3.04** | **3.90** | **3.50** |
| Qwen3-8B-Dflash-local (z-lab-based config) | 2.79 | 3.65 | 3.20 |
| **Qwen3-8B-Dflash-local (RHAI-based config)** | **3.28** | **4.21** | **3.75** |

Looking at the results I can conclude that the pipeline is fine and I will retry creating dflash for `Qwen3.5-3B-A3B` or `Qwen3.6-3B-A3B` with similar config.

### fynnsu · 2026-06-08

@imargulis Thanks for providing the context and results. 

Also btw, we've been using sliding window attention layers for our DFlash models lately and found that they generalize better to long context workflows. [#523 ](https://github.com/vllm-project/speculators/pull/523#issuecomment-4616973028) shows the usage for this if you're curious. 

Going back to the draft model config option:

> > > Add --draft-config (HF model id or local config path) to train.py and launch_vllm.py. Draft decoder parameters (intermediate size, head dim, attention heads, hidden layers) are read from it; explicit CLI flags (--num-layers, --draft-hidden-act, …) then override. The draft hidden size must match the verifier (the mismatch case is deferred — see below).
> > 
> > 
> > I sorta support this move. However, I think the user should be able to pass in a path to a fully ready speculative draft model config. (e.g. the thing that gets saved to checkpoints when training ends). We sorta support this already with the --from-pretrained arg, but the difference there is that we expect the weights to exist already. We could look into expanding --from-pretrained to also work if it receives a path that just contains a config file.
> > I would probably argue that we should ignore/fail if the user passes in other --num-layers (and similar) flags. If we're loading from a pre-existing config, we should just use the values directly and if the user wants different values they can edit the config file.
> 
> I agree with your proposition, either config file or flags, ignoring the latter when a file is provided.

We've had a chance to discuss and think the following usage makes the most sense:

```bash
scripts/train.py --draft-config ./config.json
```
This loads a config for just the `transformer_layer_config` (i.e. draft layer definition) part of the model. The rest of the config/model is set up using the other args as expected. `config.json` is expected to contain a valid LlamaConfig (if using eagle3/peagle) and a valid Qwen3Config for dflash.

```bash
scripts/train.py --dry-run
```
This arg (can be combined with above), sets up the full speculator model config, initializes the model weights, sets up vocab mappings etc, and then saves a checkpoint and exits. This can be used to create a checkpoint before spending any time actually training the model. The checkpoint can then be validated in vLLM to make sure the config / weights are valid and runnable.

```bash
scripts/train.py --from-pretrained ./checkpoint_path
```
This can be used instead of `--draft-config` / other args. It will load an existing checkpoint and start training from there. This is already supported, but works well with `--dry-run` because the output from `--dry-run` can be used directly to start training. 

I would also like to add to new behavior to this option, where if a path is provided that only contains the `--config.json` file but no weights, we load the config file, but initialize the weights from scratch as normal.


This way users will have two options for providing pre-existing configs `--draft-config` (more common, user friendly approach) where they just pass in a regular LlamaConfig/Qwen3Config to set the model up with. We then set up the rest of the speculator config for them. Or advanced users can also use the existing `--from-pretrained` option to load a full config, which might be useful for reproducibility related reasons.

And then either way, there is the option to provide `--dry-run` which will allow the user to create a checkpoint that they can validate to make sure the config is supported by vLLM before they begin training. 


LMK if you have any thoughts on this! Otherwise, if you're able to help with the implementation, you should be good to get started. 

### github-actions[bot] · 2026-09-06

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
