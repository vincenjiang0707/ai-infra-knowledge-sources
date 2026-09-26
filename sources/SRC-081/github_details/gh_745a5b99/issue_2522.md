# [Issue #2522] [Bug]: Evaluate AWQ and GPTQ for Gemma

source: https://github.com/vllm-project/llm-compressor/issues/2522
state: closed | updated: 2026-08-18T17:48:01Z
labels: bug, stale

## 正文

### ⚙️ Your current environment

### Environment Information ###
Operating System: `Linux-6.8.0-100-generic-x86_64-with-glibc2.39`
Python Version: `3.12.11 | packaged by Anaconda, Inc. | (main, Jun  5 2025, 13:09:17) [GCC 11.2.0]`
llm-compressor Version: `0.10.0.1`
compressed-tensors Version: `0.14.0.1`
transformers Version: `4.57.6`
torch Version: `2.10.0`
CUDA Devices: `['NVIDIA A100-SXM4-80GB', 'NVIDIA A100-SXM4-80GB']`
AMD Devices: `None`
NPU Devices: `None`




### 🐛 Describe the bug

AWQ W4A16 quantization via llm-compressor produces catastrophically degraded output quality on Gemma 3-based models (tested on `google/medgemma-27b-it`). Accuracy drops from **85.6%** (FP16 baseline) to **69.2%** on the CareQA medical benchmark — a ~16 point degradation. In contrast, GPTQ W4A16 on the same model retains **83.6%**, demonstrating that the issue is specific to AWQ's scaling mechanism, not a general quantization sensitivity.

https://github.com/vllm-project/llm-compressor/pull/2500#issuecomment-4128173409

### 🛠️ Steps to reproduce

```python
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier, AWQMapping
from llmcompressor.modifiers.quantization import QuantizationModifier

# Select calibration dataset
DATASET_ID = "FreedomIntelligence/medical-o1-reasoning-SFT"
DATASET_SPLIT = "train"
language = "en"



# Select model and load it.
MODEL_ID = "google/medgemma-27b-text-it"

model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)

# Increasing the number of calib samples to 256 or higher can improve accuracy.
NUM_CALIBRATION_SAMPLES = 512
MAX_SEQUENCE_LENGTH = 2048

# Load dataset and preprocess.
ds = load_dataset(DATASET_ID, language, split=f"{DATASET_SPLIT}[:{NUM_CALIBRATION_SAMPLES}]")
ds = ds.shuffle(seed=42)
print(f"Dataset size: {len(ds)} samples")


# Preprocess: apply chat template and tokenize properly
def preprocess(example):
    text = tokenizer.apply_chat_template(
        [{"role": "user", "content": example["Question"]}],
        tokenize=False,
        #add_generation_prompt=True,
    )
    return tokenizer(
        text,
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
        add_special_tokens=False,
    )


ds = ds.map(preprocess, remove_columns=ds.column_names)

# Gemma 3 specific mappings (GQA-aware: skip v_proj -> o_proj due to dimension mismatch)
gemma3_mappings = [
    # 1. Smooth Input Norm against Q, K, V
    AWQMapping(
        smooth_layer="re:.*input_layernorm$",
        balance_layers=["re:.*q_proj$", "re:.*k_proj$", "re:.*v_proj$"]
    ),


    AWQMapping("re:.*v_proj$", ["re:.*o_proj$"]),
    # 2. Smooth the MLP using the pre-feedforward norm
    AWQMapping(
        smooth_layer="re:.*pre_feedforward_layernorm$",
        balance_layers=["re:.*gate_proj$", "re:.*up_proj$"]
    ),
    # 3. Smooth Up-proj against Down-proj
    AWQMapping(
        smooth_layer="re:.*up_proj$",
        balance_layers=["re:.*down_proj$"]
    ),
]

# Initialize the modifier with these mappings
recipe = [
    AWQModifier(
        targets=["Linear"],
        scheme="W4A16_ASYM",
        ignore=["lm_head"],
        #mappings=gemma3_mappings,
        duo_scaling="both"
    )
]

"""
 recipe = QuantizationModifier(
     targets="Linear",
     scheme="FP8_DYNAMIC",
     ignore=["lm_head"],
     duo_scaling="both"
 )
"""


#Run quantization algorithm
oneshot(
    model=model,
    dataset=ds,
    recipe=recipe,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
)
```

## 评论 (31)

### brian-dellabetta · 2026-03-26

Hi @Jeevi10 , are you trying on latest main? The fix you linked in #2500 is on main but not on the llm-compressor version (0.10.0.1) you listed you are using

### Jeevi10 · 2026-03-26

@brian-dellabetta  Thanks for the swift reply, let me check. I might have missed something let me test it.

### Jeevi10 · 2026-03-26

@brian-dellabetta  I installed from the source. is this correct?

### Environment Information ###
Operating System: `Linux-6.8.0-100-generic-x86_64-with-glibc2.39`
Python Version: `3.12.11 | packaged by Anaconda, Inc. | (main, Jun  5 2025, 13:09:17) [GCC 11.2.0]`
llm-compressor Version: `0.10.1.dev34+gcf3bd646`
compressed-tensors Version: `0.14.1a20260325`
transformers Version: `4.57.6`
torch Version: `2.10.0`
CUDA Devices: `['NVIDIA A100-SXM4-80GB', 'NVIDIA A100-SXM4-80GB']`
AMD Devices: `None`
NPU Devices: `None`

### brian-dellabetta · 2026-03-26

Hard to confirm just from the version number but that looks better. does it work for you now? You should see a line like this in the logs

```
2026-03-25T21:24:11.1687 | norm_calibration_context | INFO - Found 101 offset-norm modules to convert
```

### Jeevi10 · 2026-03-26

2026-03-26T15:38:04.139058+0000 | norm_calibration_context | INFO - Found 373 offset-norm modules to convert 
is this correct? I am running it on 27b model btw. I am running the script again.
 

### Jeevi10 · 2026-03-26

This is the results, still the accuracy drop is significant compare to GPTQ or 
FP8 
<img width="505" height="67" alt="Image" src="https://github.com/user-attachments/assets/49d352cd-6e5b-4a59-874e-5e4754959e03" />

### brian-dellabetta · 2026-03-26

I don't see any issue with the mappings. You'll have to compare against the same scheme, W4A16 can perform very differently than FP8.
Your results are the following?
- Baseline fp16 -> 85.6%
- GPTQ W4A16 -> 83.6%
- AWQ W4A16  -> 71.2%
- RTN (using QuantizationModifier) W4A16 -> (?)

If RTN performs better than AWQ, there may be an issue. If AWQ performs better than RTN, but worse than GPTQ, that can happen. You may also want to experiment with `W4A16_ASYM`, which can improve recovery without much additional overhead


### dsikka · 2026-03-26

Tracked in JIRA: https://issues.redhat.com/browse/INFERENG-5600

**JIRA Details:**
- Issue Type: Bug
- Priority: Critical
- Component: LLM Compressor
- Team: INFERENG Model Optimizations
- Status: Backlog

### Jeevi10 · 2026-03-27

@dsikka Thanks for sharing this, I was not able to check the issues in jira due to access restriction. is there  anything i could do at this moment ? 
@brian-dellabetta Thanks for sharing this insight, I will do the testing with RTN (using QuantizationModifier) W4A16  and post the results.

### Jeevi10 · 2026-03-27


Hi @brian-dellabetta,

Sharing the W4A16 quantization results (rounded to nearest), which point to an issue with AWQ:
<img width="528" height="60" alt="Image" src="https://github.com/user-attachments/assets/95e1cb75-fd3e-4eac-a211-1208a01608ad" />

• Baseline (FP16): 85.6%
• RTN (Quantization Modifier)-W4A16: 84.0%
• GPTQ-W4A16: 83.6%
• AWQ-W4A16: 71.2%

AWQ shows a significant accuracy drop (~14.4 pp) compared to baseline, while both RTN and GPTQ remain within ~2 pp. I also tried W4A16_ASYM with AWQ, but it didn't yield any meaningful improvement over the symmetric results.

This confirms there's likely a problem on the AWQ side. Happy to share further details or run additional experiments if needed.



### brian-dellabetta · 2026-03-27

Hi @Jeevi10 , thanks for sharing the results. it's weird that RTN outperforms GPTQ as well, but yeah the AWQ regression is very strange. Can you try autoround and see if that performs any better? If none of the calibrated flows outperforms RTN, the calibrated dataset is not helpful in steering the quantized version to improve on the eval dataset.

You can ignore the JIRA ticket&link. That is something new we've added for internal processes.

### Yatimai · 2026-03-27

Hi @brian-dellabetta,

I looked into this as a contributor to #2500. I believe the root cause is a missing `module2inspect` equivalent in llm-compressor's AWQ implementation.

In the reference MIT implementation (`llm-awq/awq/quantize/auto_scale.py`), each mapping can specify a `module2inspect`, the module on which the grid search loss is computed. For the `post_attention_layernorm → gate,up` mapping, MIT sets `module2inspect=module` (the full DecoderLayer), not just `mlp`. This ensures the loss sees everything downstream of the balance layers, including any post-norms.

llm-compressor computes the loss at the LCA of the balance layers (`self_attn` or `mlp`), with no way to override it. On Gemma3, `post_attention_layernorm` and `post_feedforward_layernorm` sit outside that scope, so the grid search optimizes scales without seeing how the post-norms transform the quantization error.

### brian-dellabetta · 2026-03-27

Thanks @Yatimai for the details! Rather than requiring user to declare the `module2inspect` (we call this the parent), we infer it to just be the lowest common ancestor of the balance layers. This is wrong though, it should be the lowest common ancestor of the balance layers AND the smooth layer. I have updated this in 
* #2531

@Jeevi10 , can you try re-running your AWQ script on that branch and report back how it performs?

### Jeevi10 · 2026-03-27

<img width="530" height="69" alt="Image" src="https://github.com/user-attachments/assets/d5fe2f51-9305-4304-a2ca-6f5e002cc80d" />

@brian-dellabetta  I ran the script and did not get any improvement  @https://github.com/vllm-project/llm-compressor/pull/2531 

### brian-dellabetta · 2026-03-27

Hmm, even worse. I looked at AutoAWQ, which is what our implementation is based on, and [they define](https://github.com/casper-hansen/AutoAWQ/blob/main/awq/models/gemma2.py#L68-L73) the module2inspect (a.k.a. parent) should be the mlp layer for this mapping, not the decoder layer. So maybe this isn't a bug. 

@Yatimai can you point to where you're looking in https://github.com/mit-han-lab/llm-awq/blob/main/awq/quantize/auto_scale.py ? I don't see anything related to gemma 3

### brian-dellabetta · 2026-03-27

I'm starting to think there's a bug dating back to the original AutoAWQ implementation.
In [compute_best_scales](https://github.com/casper-hansen/AutoAWQ/blob/main/awq/quantize/quantizer.py#L368), the loss calculation is listed as
```
L(s) = || Q(W * s) (s^-1 * X) - W * X ||
```
In the grid search, the scales `s` are calculated and the weights of the balance layers are scaled and quantized, so we have `Q(W * s)`, but the inputs are never inversely scaled anywhere, i.e. we have `X` and not `(s^-1 * X)`. There is a comment [here](https://github.com/casper-hansen/AutoAWQ/blob/main/awq/quantize/quantizer.py#L403) saying that they're already fused but i don't see where that's the case. The same `X` is always passed into `_module_forward` without any scaling.

Will discuss internally and do some more troubleshooting next week. Have a good weekend!

EDIT: after internal discussions, this is not a bug. The activations are scaled [in a weird place](https://github.com/casper-hansen/AutoAWQ/blob/main/awq/quantize/quantizer.py#L419), but they are scaled nonetheless

### Yatimai · 2026-03-27

@brian-dellabetta You're right, there's no Gemma 3 specific code in MIT auto_scale.py, I was reasoning by analogy from the generic Bloom/Falcon path, not from anything Gemma-specific. That was misleading on my part, sorry for the confusion.

### brian-dellabetta · 2026-03-27

@Yatimai all good, thanks for clarifying. We are exploring this very thing, including the smooth layer when finding the parent and calculating best scales, in other places as well (#2323)

### brian-dellabetta · 2026-03-30

Following up from last week -- no bugs in mappings or in our AWQ implementation. I don't see why it wouldn't work. Other options:
- run with only one of the mappings turned on, and see if it improves. Perhaps one mapping in particular is causing the degradation.
- Validate non-medical gemma3 models perform as expected (with non-medical calibration dataset and eval)
- Try autoround out on your use case.

Will tag this to be left open for now, in case other users hit similar issues

### HDCharles · 2026-04-02

what is teh calibration set that you're using? is it related to your evaluation set or somethign different?

### Yatimai · 2026-04-03

Hi @brian-dellabetta, @HDCharles,

Following up on the per-mapping ablation suggestion. I ran a series of experiments on `medgemma-27b-text-it` to isolate the source of the AWQ degradation.

## Per-mapping ablation results

Evaluation: `lm_eval --model hf --tasks careqa_en --num_fewshot 5` (5,621 medical MCQA questions).
Quantization: W4A16_ASYM, `duo_scaling="both"`, 512 calibration samples from `medical-o1-reasoning-SFT`.

| Config | CareQA acc | Delta vs RTN |
|---|---|---|
| RTN (W4A16_ASYM) | 78.14% | — |
| AWQ (all mappings) | 67.44% | **-10.7 pp** |
| AWQ (mapping 1 removed) | 77.80% | -0.3 pp |

**Mapping 1 (`input_layernorm → [q_proj, k_proj, v_proj]`) causes the entire degradation.** Removing it recovers accuracy to within 0.3 pp of RTN. The MLP mappings (`pre_feedforward_layernorm → gate/up` and `up_proj → down`) are benign.

Note: absolute scores are ~6 pp below @Jeevi10's results, likely due to `--model hf` vs `--model vllm` backend. The deltas are consistent (Jeevi10: -12.8 pp for AWQ vs RTN, us: -10.7 pp).

## Root cause: QK-Norm

Gemma 3 applies per-head RMSNorm (`q_norm`, `k_norm`) to query and key states immediately after projection:

```python
# https://github.com/huggingface/transformers/blob/138f757/src/transformers/models/gemma3/modeling_gemma3.py#L357-L362
query_states = self.q_proj(hidden_states).view(hidden_shape).transpose(1, 2)
key_states = self.k_proj(hidden_states).view(hidden_shape).transpose(1, 2)
value_states = self.v_proj(hidden_states).view(hidden_shape).transpose(1, 2)

query_states = self.q_norm(query_states)  # ← per-head RMSNorm (Gemma3RMSNorm)
key_states = self.k_norm(key_states)      # ← per-head RMSNorm (Gemma3RMSNorm)
```

RMSNorm re-normalizes magnitudes, largely negating the per-channel scaling that AWQ applies. AWQ's smoothing scales up salient input channels in q/k/v weights and scales down the corresponding activations via `input_layernorm`. But `q_norm`/`k_norm` immediately re-normalize the projected Q and K, **absorbing the magnitude protection** that AWQ applied. The weights are distorted (scaled up for quantization protection) but the protection is erased, net effect is worse quantization than doing nothing (RTN).

Gemma 2 does **not** have `q_norm`/`k_norm` (it uses soft-capping instead). To confirm this is the cause, I ran the same AWQ configuration on `gemma-2-27b-it`:

| Model | q_norm/k_norm | RTN | AWQ (all mappings) | Delta |
|---|---|---|---|---|
| **medgemma-27b** (Gemma 3) | Yes | 78.14% | 67.44% | **-10.7 pp** |
| **gemma-2-27b-it** (Gemma 2) | No | 50.08% | 51.56% | **+1.5 pp** |

Same mappings, same algorithm, same eval. On Gemma 2 (no QK-norm), mapping 1 **improves** accuracy. On Gemma 3 (has QK-norm), it **destroys** it.

## Precedent

Exaone4 and Olmo3 also have `q_norm`/`k_norm`. Their AWQ mappings in the registry already skip the `input_layernorm → q/k/v` mapping:

```python
# src/llmcompressor/modifiers/awq/mappings.py:161-167
_exaone4_mappings = [
    AWQMapping("re:.*v_proj$", ["re:.*o_proj$"]),
    AWQMapping("re:.*up_proj$", ["re:.*down_proj$"]),
]
```

The Gemma 3 mappings (`_gemma_mappings`) were inherited from Gemma 2, which does not have QK-norm. They need to be updated for Gemma 3.

## Proposed fix

Separate `_gemma_mappings` (Gemma 2, no QK-norm) from a new `_gemma3_mappings` (Gemma 3, has QK-norm) that removes the attention smoothing:

```python
_gemma3_mappings = [
    # No input_layernorm → q/k/v (QK-norm makes it counterproductive)
    AWQMapping("re:.*v_proj$", ["re:.*o_proj$"]),
    AWQMapping(
        "re:.*pre_feedforward_layernorm$",
        ["re:.*gate_proj$", "re:.*up_proj$"],
    ),
    AWQMapping("re:.*up_proj$", ["re:.*down_proj$"]),
]
```


### brian-dellabetta · 2026-04-03

Ah, thanks @Yatimai for the great detective work! That makes sense to me. It's strange though, Gemma3 is not the only model with `q_norm`/`k_norm` RMSNorm components. Doing a quick audit of other models, I'm surprised we haven't hit this issue before

Models with q_norm/k_norm RMSNorm components:

- [ ] Gemma3
- [ ] Qwen3 and Qwen3.5
- [ ] Afmoe 
- [ ] Glm 4 (has a `use_qk_norm` option in config)
- [ ] Gemma4 (new, no mappings, not yet supported in llm-compressor)
- [x] exaone (already excludes that mapping)
- [x] Olmo2 (no mappings exist)

I wonder why the regression is so prominent for Gemma3, whereas for Qwen 3 and 3.5 it hasn't seemed to be an issue. Shouldn't the best scales just be computed to be `[1.0, 1.0, ..., 1.0]` for the mapping?

### Yatimai · 2026-04-03

@brian-dellabetta, excellent question ! I guess V (without norm after projection) benefits from non-identity scales The grid search picks scales that help V, but those same scales distort Q/K weights for no benefit (q_norm/k_norm absorb the protection). V pulls the scales away from identity at Q/K's expense. 
On Gemma 3, V is 25% of the total weight, enough to pull scales away from identity. On Qwen3-32B, V is only 10%, maybe not enough to meaningfully shift the scales :  so the regression is smaller or undetectable.






### brian-dellabetta · 2026-04-06

Thanks @Yatimai , that's a good point. I think for now we can remove the mapping with a comment and add gemma 4 mappings. i'll do that in a PR today with some gemma 4 quant examples i'm working on. And we'll just keep an eye out in future for the RMS norms on outputs of q/k/v proj

### brian-dellabetta · 2026-04-06

Hi @Jeevi10 , do you mind retrying on branch `bdellabe/bugfix-gemma3-awq` from #2571 and letting us know if you see the large drop in recovery?

### HDCharles · 2026-04-07

its still surprising that even after this is fixed, it seems like AWQ is underperforming RTN unless i'm reading that wrong?


| Config | CareQA acc | Delta vs RTN |
|---|---|---|
| RTN (W4A16_ASYM) | 78.14% | — |
| AWQ (all mappings) | 67.44% | **-10.7 pp** |
| AWQ (mapping 1 removed) | 77.80% | -0.3 pp |

that seems almost impossible given that each layer is explicitly compared to RTN.

### Jeevi10 · 2026-04-07

@brian-dellabetta I can do that and update as soon as I can. Thank you all.

### Yatimai · 2026-04-07

@HDCharles The -0.3 pp delta (77.80% vs 78.14%) is within noise (~19 questions out of 5,621). Indeed, the grid search minimizes per-layer MSE, not end-to-end accuracy, so a small negative delta is possible. On this model, RTN already achieves ~98% recovery, leaving very little room for the MLP mappings to improve on.

### issacchan26 · 2026-05-01

Hi @brian-dellabetta , when quantizing google/medgemma-27b-text-it with AWQ, do we need to explicitly add the mappings in the recipe?

For example:

```
gemma3_mappings = [
    AWQMapping("re:.*v_proj$", ["re:.*o_proj$"]),
    AWQMapping(
        "re:.*pre_feedforward_layernorm$",
        ["re:.*gate_proj$", "re:.*up_proj$"],
    ),
    AWQMapping(
        "re:.*up_proj$",
        ["re:.*down_proj$"],
    ),
]

recipe = [
    AWQModifier(
        targets=["Linear"],
        scheme="W4A16_ASYM",
        ignore=["lm_head"],
        mappings=gemma3_mappings,
        duo_scaling="both"
    )
]
```

Or is it fine to leave mappings unset and rely on the default behavior for this model?

### brian-dellabetta · 2026-05-04

Hi @issacchan26 , if you leave them unset they will default to the following for `Gemma3ForCausalLM` models:

```
[
    AWQMapping(
        "re:.*input_layernorm$",
        ["re:.*q_proj$", "re:.*k_proj$", "re:.*v_proj$"],
    ),
    AWQMapping("re:.*v_proj$", ["re:.*o_proj$"]),
    AWQMapping(
        "re:.*pre_feedforward_layernorm$",
        ["re:.*gate_proj$", "re:.*up_proj$"],
    ),
    AWQMapping(
        "re:.*up_proj$",
        ["re:.*down_proj$"],
    ),
]
```

There is an open question though if that first mapping is degrading recovery, and may want to be removed. We have also pushed some recent changes for AWQ to make sure unit scales are always benchmarked. Can you try on latest main with the current default mappings and see if you hit the same issue originally posted by @Jeevi10 ? We may want to remove that first mapping entirely, as I do in #2571 

### github-actions[bot] · 2026-08-13

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
