# [Issue #1577] generate_context_logits returns truncated logits when KV prefix cache is enabled, causing silently wrong loglikelihood evaluation

source: https://github.com/NVIDIA/Model-Optimizer/issues/1577
state: open | updated: 2026-09-01T09:23:41Z
labels: bug

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
<!-- Description of what the bug is, its impact (blocker, should have, nice to have) and any stack traces or error messages. -->

- modelopt.deploy.llm.LLM.generate_context_logits() is built on top of TensorRT-LLM's return_context_logits=True. When KV cache prefix reuse is active (which is the default), TensorRT-LLM skips the forward pass for cached prefix tokens and returns only the logits for the un-cached tail of the prompt — without any error or warning. This silently breaks every downstream loglikelihood-style evaluation (lm-eval-harness MMLU etc.) that uses generate_context_logits, because parse_logprobs slices into a logits tensor that is much shorter than the prompt and produces meaningless logprobs.

### Steps/Code to reproduce bug
<!-- Please list *minimal* steps or code snippet for us to be able to reproduce the bug. -->
<!-- A helpful guide on on how to craft a minimal bug report http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports. -->

```
python examples/llm_eval/lm_eval_tensorrt_llm.py \
      --model trt-llm \
      --model_args tokenizer=/path/to/Llama-3.2-1B,checkpoint_dir=/path/to/Llama-3.2-1B \
      --tasks mmlu_philosophy \
      --num_fewshot 5 \
      --batch_size 1
```
❯ trt-llm (tokenizer=/root/infra/hf/Llama-3.2-1B,checkpoint_dir=/root/infra/hf/Llama-3.2-1B), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: 1                                                  
  |  Tasks   |Version|Filter|n-shot|Metric|   |Value |   |Stderr|                                                                                                                                             
  |----------|------:|------|-----:|------|---|-----:|---|-----:|                                                                                                                                             
  |philosophy|      1|none  |     5|acc   |↑  |0.1865|±  |0.0221|
```
 lm_eval --model hf \
      --model_args pretrained=/path/to/Llama-3.2-1B,dtype=float16 \
      --tasks mmlu_philosophy \
      --num_fewshot 5 \
      --batch_size 1
```
❯ hf (pretrained=/root/infra/hf/Llama-3.2-1B,dtype=float16), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: 1                                                                                   
  |  Tasks   |Version|Filter|n-shot|Metric|   |Value |   |Stderr|                                                                                                                                             
  |----------|------:|------|-----:|------|---|-----:|---|-----:|                                                                                                                                             
  |philosophy|      1|none  |     5|acc   |↑  |0.3344|±  |0.0268|

 - The TRT-LLM result is below the 25% random baseline because every prompt after the first one returns truncated logits → parse_logprobs ends up summing to ~0.0 for every candidate → lm-eval picks option A by stable-sort tie-breaking, and accuracy collapses to "% of questions where A is the gold answer".

### Root cause
- Adding debug prints to parse_logprobs shows the smoking gun:
 ```
  # request 1 (cold)
  ctxlen=469, logits_len=470, tokens_len=470   ← OK

  # request 2+ (prefix cache hit)
  [TensorRT-LLM][WARNING] [kv cache manager] storeContextBlocks: Can not find sequence for request 2048
  ctxlen=469, logits_len=1, tokens_len=470     ← BROKEN: only 1 logit returned
 ```
- The first request does a full prefill and returns 470 logits as expected. Subsequent requests in the same MMLU subtask share the 5-shot demo prefix → KV cache prefix reuse hits → the forward pass is skipped for the cached portion → TensorRT-LLM returns only the logits for the un-cached tail (often just 1 token, the last differing token of the question).

 - parse_logprobs in examples/llm_eval/lm_eval_tensorrt_llm.py then does:
 ```
  logits_single_batch[(ctxlen_single_batch - 1) : -1]   # slice [468:-1] on a length-1 tensor
 ```
  which yields an empty tensor → logprob_sum=0.0 for every continuation candidate → lm-eval cannot distinguish A/B/C/D.

 ### Confirmed fix

  - Setting enable_block_reuse=False in the KV cache config restores correctness. Verified locally: mmlu_philosophy 5-shot recovers from 0.1865 to 0.3151, matching the HF golden baseline.
 
```
# In modelopt/deploy/llm/generate.py, line ~122:

  trt_kv_cache_config = TRT_KvCacheConfig(
      free_gpu_memory_fraction=0.7,
      enable_block_reuse=False,
  )
```
❯ trt-llm  (tokenizer=/root/infra/hf/Llama-3.2-1B,checkpoint_dir=/root/infra/hf/Llama-3.2-1B), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: 1

|  Tasks   |Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|----------|------:|------|-----:|------|---|-----:|---|-----:|
|philosophy|      1|none  |     5|acc   |↑  |0.3151|±  |0.0264|

 ### Things tried that did NOT fix it
  - Switching to TensorRT-LLM's prompt_logprobs API (SamplingParams(prompt_logprobs=k)): on the tested TRT-LLM version, prompt_logprobs shares the same forward-output path as1 return_context_logits and is also truncated when prefix cache hits. The hope that prompt_logprobs would semantically guarantee full-length output (as it does in vLLM) does not hold for TensorRT-LLM in this version.

### Expected behavior

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): nvcr.io/nvidia/tensorrt-llm/release:1.2.0
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10):  <!-- If Windows, please add the `windows` label to the issue. --> Ubuntu 22.04
- CPU architecture (x86_64, aarch64): x86_64
- GPU name (e.g. H100, A100, L40S): NVIDIA RTX A4000
- GPU memory size: 16GB
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: ?
  - ModelOpt version or commit hash: tag0.37.0 + 824c9457 ([NVBUG: 5617733] Update LLM generate API for modelopt LLM eval)
  - CUDA: ?
  - PyTorch: ?
  - Transformers: ?
  - TensorRT-LLM: v1.2.0
  - ONNXRuntime: ?
  - TensorRT: ?
- Any other details that may help: I'm curious if there is a way that can both fix this bug and use prefix caching.

## 评论 (1)

### harshal-96 · 2026-09-01

This appears to be fully addressed on current main, via changes that did not reference this issue:

1. `modelopt.deploy.llm.LLM` now takes `enable_kv_cache_reuse` (documented for exactly this case), and `generate_context_logits` asserts it is disabled, so the failure is loud instead of silent.
2. #2066 migrated the lm-eval flow to lm-eval 0.4.12's built-in `trtllm` backend, which sets `enable_block_reuse=False` itself; the repo's `_parse_logprobs` override additionally raises on truncated or misaligned `prompt_logprobs`, so a regression cannot corrupt results silently.
3. `examples/hf_ptq/run_tensorrt_llm.py`, the remaining `generate_context_logits` caller, passes `enable_kv_cache_reuse=False`.

On the question of keeping prefix caching together with context logits: full-prompt logits require running the full forward pass, which is precisely the work block reuse skips, so disabling reuse for those requests is inherent to the semantics rather than a workaround. Generative tasks are unaffected and keep reuse.

Looks closable to me.

