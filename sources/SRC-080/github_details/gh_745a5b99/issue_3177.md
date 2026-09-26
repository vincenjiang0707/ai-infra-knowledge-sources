# [Issue #3177] Centralize SSOT for module fusion

source: https://github.com/vllm-project/llm-compressor/issues/3177
state: open | updated: 2026-09-23T13:12:07Z
labels: enhancement, good first issue, good follow-up issue

## 正文

## Background ##
LLM Compressor requires information as to which transformers modules are fused by vLLM. These "fused mappings" are used to
* Ensure that nvfp4 global scales are shared between fused modules
* Ensure that fused modules have the same quantization
  * This check is implemented in [HIGGS](#3028) and [model_free_ptq](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/entrypoints/model_free/microscale.py#L27-L61)
  * This check needs to be implemented in `oneshot` (followup)

However, there are currently multiple sources of truth, and these sources of truth are out-of-date with respect to recent model architectures and attention implementations.

## Requested Changes ##
* Consolidate the fusion mappings below into a single mapping in a single file
  * https://github.com/vllm-project/llm-compressor/blob/3ae3cb11fbf6e2958ff64133a833148d5f18eaed/src/llmcompressor/observers/helpers.py#L162-L215
  * https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/entrypoints/model_free/microscale.py#L27-L61
* Ensure that the mappings structure can support matching against both checkpoint weight names as well as hf module names
* Add missing fusion mappings for more complex attention (DSA, HCA, kimi_linear, etc.)

## 评论 (3)

### kylesayrs · 2026-09-14

@amacharla15 You might have some interest in this realm?

### amacharla15 · 2026-09-14

Hi @kylesayrs , thank you for asking. Very interested, please assign.

### amacharla15 · 2026-09-23

@kylesayrs I’ve opened #3224 for #3177.

I consolidated the fusion definitions into a single FUSED_MODULE_MAPPINGS source of truth shared by oneshot and model_free_ptq, and added the newer Kimi KDA/MLA, DeepSeek V4/HCA, and DSA mappings.

The main wrinkle was Kimi g_proj, since it belongs to different packed groups depending on the layer. I resolved that from the sibling layers present on the same parent; for model-free PTQ, _build_jobs now passes the checkpoint weight names so the correct group can be determined without changing the compressed-tensors Converter protocol.

I also validated the change locally and on an H100. On the reduced Kimi-K3 checkpoint, the targeted packed attention groups went from 8/8 mismatched to 0/8 with model-free PTQ, and 7/8 to 0/8 with oneshot. I included the full validation details and the overlap with #3206, #3162, and #3217/#3118 in the PR.

The PR is ready for review, but it looks like I don’t have permission to add the ready label myself. Could you add it when you get a chance so the full CI suite can run?
