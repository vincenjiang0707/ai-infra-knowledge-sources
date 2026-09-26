# [Issue #2680] AWQ calibration for Qwen3.5 thinking models: non-thinking leakage of <think> and failure to emit </think> after quantization

source: https://github.com/vllm-project/llm-compressor/issues/2680
state: closed | updated: 2026-07-13T17:29:59Z
labels: 

## 正文

Hi,
I am quantizing Qwen/Qwen3.5-122B-A10B with AWQ using llmcompressor, and I am seeing a behavior regression that seems specific to thinking-mode calibration.

**Observed issue:**

After AWQ quantization:

1. In non-thinking inference with `enable_thinking=False`, the quantized model sometimes generates `<think>` tokens in the output.
2. In thinking inference with `enable_thinking=True`, the quantized model often produces very long reasoning traces, sometimes does not emit `</think>`, and may fail to transition to the final answer tokens.
3. The original base model does not show this behavior.
4. An open-source quantized variant I tested also does not show this behavior.

So the failure seems to be around preserving:
- suppression of thinking in non-thinking mode
- proper exit from thinking mode via `</think>`

**Model / setup:**
* Model: Qwen/Qwen3.5-122B-A10B
* Quantization: [AWQModifier(scheme="W4A16", targets=["Linear"])]
* Calibration dataset: Dataset name: HuggingFaceH4/ultrachat_200k


**Question:**
Do you have any guidance on the calibration datasets for Qwen3.5-122B model?

In particular, I would like to understand whether `ultrachat_200k` alone is insufficient for preserving the intended `<think>` / `</think>` behavior after quantization, which was not the case with Qwen3-4B or Qwen3-30B model.

Any suggestions would be very helpful. Thanks.

## 评论 (11)

### brian-dellabetta · 2026-05-01

Hi @Priya95715 , thanks for the details, very interesting. Calibrated quantization flows like AWQ work to reduce quantization loss against the calibration set, so while I'm not aware of any ablations or thorough benchmarking, it is probably safe to say the quantized model is tuned towards ultrachat, and so it is less likely to generate reasoning tokens. [This recent blog from Cohere](https://cohere.com/blog/vllm-integration-and-quality-recovery-techniques-explained) showed the importance of long-context evals and token masking for their AWQ runs, this might be an extension of that.

A few things to test the hypothesis:
- **data-free**: Does pure round-to-nearest (no calibration dataset) work better?
- **self calibration**: Can you pull a calibration dataset out after using the full-precision model specific to how you'd like to use the quantized model, and see if it performs better with that dataset relative to ultrachat?
- **reasoning dataset**: Did a quick gemini search -- Magpie-reasoning and open-thinker datasets would be easy to try and compare against ultrachat

I will ask our research team if they have further thoughts. Not sure why this would be new behavior in `Qwen/Qwen3.5-122B-A10B`

### jayakumarpujar · 2026-05-01

Hi @brian-dellabetta, I'd like to be assigned to this issue. I've looked into the root cause and have a fix ready to implement.

**Root Cause**

In the AWQ calibration examples for Qwen3.5/Qwen3-Next thinking models, `apply_chat_template` is called without `enable_thinking=False`. Qwen3.5 thinking tokenizers default to `enable_thinking=True`, so calibration samples get formatted with a thinking-mode prompt - but the calibration dataset (`ultrachat_200k`) has no actual `<think>...</think>` completions. AWQ then fits weight scales to this mismatched activation distribution, which corrupts the think-token generation pathway and causes the symptoms described above.

**Plan**

1. Pass `enable_thinking=False` in `apply_chat_template` for non-thinking AWQ calibration examples.
2. Add a thinking-mode calibration example using a dataset with real reasoning chains (e.g. s1K or OpenThoughts), leveraging the existing `loss_mask` support in `AWQModifier` to focus calibration on reasoning tokens.
3. Add a short note in the relevant docs explaining when to use each approach.

No core modifier changes needed. Happy to open a PR once assigned.

### brian-dellabetta · 2026-05-01

@jayakumarpujar thanks! I can definitely assign this to you. The plan looks good to me, an example for reasoning models similar to our [coder example](https://github.com/vllm-project/llm-compressor/blob/main/examples/awq/qwen3_coder_moe_example.py) would be good, using a reasoning dataset and reasoning evals, with some basic ablations in the PR summary to show how important `enable_thinking` and calibration dataset choice is. Excited to hear how it goes!

### jayakumarpujar · 2026-05-02

@brian-dellabetta Opened PR #2681 with the fix - https://github.com/vllm-project/llm-compressor/pull/2681 

### jayakumarpujar · 2026-05-02

@Priya95715 update - extended PR #2681 to also fix your exact model.

The original PR fixed 'examples/awq/qwen3_next_example.py' (Qwen3-Next family), but you're on 'Qwen/Qwen3.5-122B-A10B', which is exercised by 'examples/quantization_w4a4_fp4/qwen3_5_example.py'. That file had the same 'apply_chat_template' bug - calling it without 'enable_thinking=False' on a thinking-capable tokenizer while calibrating on 'ultrachat_200k'. Same one-line fix is now applied there (and to the sibling 'qwen3_6_example.py').

The 'mxfp4' / 'nvfp4' Qwen3.5 examples are unaffected - they use data-free quantization, so there's no calibration distribution mismatch to fix.

When the PR merges, the recommended workflow for your case will be either:
1. **Non-thinking deployment** - re-run with the fixed 'qwen3_5_example.py' (now with 'enable_thinking=False').
2. **Thinking deployment** - follow the new 'qwen3_next_thinking_example.py' pattern: a reasoning dataset (e.g. Magpie-Reasoning-V2) + 'use_loss_mask=True' to focus AWQ on assistant reasoning + answer tokens.

### Priya95715 · 2026-05-02

Hi @jayakumarpujar, Thanks for the update!

One follow-up question: is there any recommended way to produce a single AWQ-quantized Qwen3.5 checkpoint that supports both `enable_thinking=False` and `enable_thinking=True` well, or is the recommended approach to build separate quantized models for non-thinking and thinking deployment?

### jayakumarpujar · 2026-05-03

Hi @Priya95715!

The PR ships two calibration patterns, both validated:

- **Non-thinking deployment** - `qwen3_5_example.py` with `enable_thinking=False` + `ultrachat_200k`.
- **Thinking deployment** - `qwen3_next_thinking_example.py` pattern: reasoning dataset (Magpie-Reasoning-V2) + `use_loss_mask=True` + `enable_thinking=True`.

Each fits AWQ scales to one activation distribution, so they produce two separate checkpoints - one optimized per mode.

For a single dual-mode checkpoint, the PR doesn't cover that path and I haven't ablated it. cc @brian-dellabetta in case the research team has guidance on whether a mixed calibration set can preserve both modes acceptably from one checkpoint.

### brian-dellabetta · 2026-05-04

Hi @Priya95715 , hi @jayakumarpujar , thanks for the interesting conversation. #2681 has reasonable changes to it, but we'll want to run some basic ablations before merging and I likely won't have bandwidth to test it out myself this week or next. 

@Priya95715 do you mind trying out the changes @jayakumarpujar introduces in #2681 and let us know if you see a marked change in behavior of the quantized model? 

> is there any recommended way to produce a single AWQ-quantized Qwen3.5 checkpoint that supports both enable_thinking=False and enable_thinking=True well, or is the recommended approach to build separate quantized models for non-thinking and thinking deployment

Regarding this, we would need to run some benchmarks to confirm, as it is likely model and usage-dependent. One thing you can try is to use a dataset with half of all samples from ultrachat (tokenized with enable_thinking=False) and the other half comes from magpie (tokenized with enabled_thinking=True), to see how much it matters at longer contexts. Just make sure you're using the loss mask consistently (the example in #2681 shows how to set it up). We plan to do more of this research in the future, once our platform is stood up.

----

update: I spoke with our research team, they also suggested swapping GPTQ in for AWQ for W4A16 schemes. They also reported that one of our [Qwen W4A16](https://huggingface.co/RedHatAI/Qwen3.5-4B-quantized.w4a16) models is seeing a drop in reasoning capabilities, and are looking into choice of calibration dataset as a way to improve. It is all very much an active area of research

### brian-dellabetta · 2026-05-20

HI @Priya95715 , just wanted to follow up on this. Have you had a chance to try out @jayakumarpujar 's PR and see if it helps to resolve your issue?

### jayakumarpujar · 2026-06-26

Hi @brian-dellabetta, any update on this PR?

### brian-dellabetta · 2026-06-26

Hi @jayakumarpujar , sorry for the delay here. for now, can you just update your PR to only add a new example and not change any of the previous examples' behavior? We can then merge and direct people to it on this issue, and close it as completed
