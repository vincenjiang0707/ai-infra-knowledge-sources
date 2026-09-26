# [Issue #664] [RFC]: Add Domino support as a DFlash-based speculator

source: https://github.com/vllm-project/speculators/issues/664
state: open | updated: 2026-07-08T14:28:47Z
labels: RFC

## 正文

### Motivation.

## Motivation

I would like to propose adding Domino support to `vllm-project/speculators`.

Domino has already been integrated in SpecForge, and the implementation can be used as a reference:

https://github.com/sgl-project/SpecForge/pull/571

## What is Domino?

Domino can be viewed as a DFlash extension rather than a completely new speculator family.

DFlash drafts a whole block of tokens in parallel, which gives low drafting overhead. However, because the tokens inside the block are generated in parallel, DFlash has weaker modeling of causal dependencies among draft tokens.

Domino keeps the DFlash-style parallel draft backbone, but adds a lightweight causal correction head. The head uses previous draft tokens to refine the base logits, improving the quality of the drafted tokens while keeping most of DFlash's parallel drafting efficiency.

In short:

- DFlash: parallel draft backbone → base logits → draft tokens
- Domino: parallel draft backbone → causal correction head → refined logits → draft tokens

## Difference from DFlash

The main difference is that Domino adds causal refinement on top of DFlash.

DFlash mainly optimizes drafting speed by generating the whole block in parallel. Domino keeps this advantage, but improves intra-block dependency modeling with a lightweight head. This should lead to higher acceptance length with only small extra overhead.

## Benefits

1. Reuses the existing DFlash infrastructure in speculators.
2. Improves draft quality and acceptance length compared with plain DFlash.
3. Keeps the main drafting computation parallel, so the additional cost should be small.
4. SpecForge already has a working implementation, which can be used as a reference.

## References

- SpecForge Domino PR: https://github.com/sgl-project/SpecForge/pull/571
- Domino paper: https://arxiv.org/abs/2605.29707
- Domino code: https://github.com/jianuo-huang/Domino

### Proposed Change.

## Possible implementation direction

Domino could be added as a DFlash submode, for example:

- `projector_type = "domino"`
- reuse the existing DFlash backbone
- add a lightweight causal correction head
- train with both base DFlash logits and Domino-refined logits
- report both base acceptance length and final Domino acceptance length


### Any Other Things.

_No response_

## 评论 (8)

### fynnsu · 2026-06-26

Yes, I agree with this approach of extending the current DFlash module to support this option.

A couple things to add:
1. We'll need to incorporate the $L = (1 − λ_t) L_{final} + λ_t L_{base}$ loss function schedule. I think this can be done [here](https://github.com/vllm-project/speculators/blob/aba50b049c6e7bf0cf13e67fe240766105fcefa6/src/speculators/models/dflash/metrics.py#L47) by calling the loss function twice on the two outputs (base & final), rather than trying to modify the `loss_function` logic to support this. We'll also need to determine how to best parameterize this decay schedule in the cli args.
2. We should try to align our model config with the author's Domino config ([example](https://huggingface.co/Huang2020/Qwen3-4B-Domino-b16/blob/main/config.json)). Note: we have a different config structure in speculators which we'll follow, but we should make sure the keys mostly line up (we can remap for clarity).

```
    "projector_type": "domino",
    "mask_token_id": 151669,
    "shift_label": true,
    "target_layer_ids": [
      1,
      9,
      17,
      25,
      33
    ],
    "pure_draft_prefix_len": 1,
    "gru_hidden_dim": 1024,
    "emb_dim": 256
```

### fynnsu · 2026-06-26

@HaizhouPeng are you interested/do you have time to implement this yourself?

### arnabwithab · 2026-06-27

@fynnsu @HaizhouPeng 
would like to work on it myself! been deep into spec decoding for a bit, and this paper was really interesting. want to see if we can reflect the same gains on vllm (gives me an excuse to try it out from a non-transformer backend locally :))) )

### HaizhouPeng · 2026-06-28

Thanks @Eros483, great to hear you are interested in working on this!

I think Domino is a meaningful direction for speculators. It is not just a standalone DFlash variant; recent DeepSeek-related speculative decoding work also seems to be moving in a similar direction: starting from DFlash-style one-pass block drafting, then adding lightweight, model-aligned refinement/training signals to improve draft quality and accepted length.

In that sense, adding Domino support here should also help us build reusable infrastructure for future DeepSeek-style speculators, instead of only supporting plain DFlash. I am happy to help with testing and reviewing the implementation, especially around the DFlash integration path and config compatibility.

### shanjiaz · 2026-06-28

@Eros483 Assigning this to you. Feel free to reach out on vLLM slack with any questions/concerns!

### arnabwithab · 2026-06-28

hehe, excited to get started! will keep this thread updated with what im looking at. Feel free to let me know your thoughts!
@HaizhouPeng thanks for the support, ill keep a branch updated for you to play around with!

### arnabwithab · 2026-06-28

Used the specforge implementation as a reference, and reviewed the author's implementation, and yeah the core philosophy i want to adhere to in this implementation will be a simple extension of dflash's capabilities.

Here is how I intend on structuring the addition

| Component | Path | Extension or New file | Purpose
| ---- | ---- | ---- | ----
| core module | `src/speculators/models/dflash/domino.py` | New file | Implement domino head module, i.e the causal GRU, embedding look up, bottleneck MLP, and logit computation|
| config | `src/speculators/models/dflash/config.py` | Extension | Add hyperparameters to trigger Domino usage, primarily via `projector_type` | 
orchestrator | `src/speculators/models/dflash/core.py` | Extension | Conditionally initialise dominohead, pass inputs during forward pass, manage the decay schedule and calculate dual loss |
| loss and metrics | `src/speculators/models/dflash/metrics.py` | N/A | Simply call compute metrics logic twice within core |
| trainer | `src/speculators/train/trainer.py`| Extension | just pass the global step parameter to the model components |
| cli entrypoint for trainer | `scripts/train.py` | Extension | Extend parsing logic to accept domino hyperparameters for the training runs|

cc: @HaizhouPeng for your reference. Also let me know if you're okay with occasional pings for such updates :)

### arnabwithab · 2026-07-08

Hi @HaizhouPeng , would appreciate it if you could review the implementation, just in case I'm missing something :)
There are changes on both the training side and the inference side. We're post iteration 6 of testing (after bug fixes and getting some ideas straight).
Inference side: https://github.com/vllm-project/vllm/pull/47627
Training side: https://github.com/vllm-project/speculators/pull/685
