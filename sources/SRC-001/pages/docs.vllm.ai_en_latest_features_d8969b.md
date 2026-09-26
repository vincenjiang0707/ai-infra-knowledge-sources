source: https://docs.vllm.ai/en/latest/features/
lastmod: 2026-09-24

# Features[¶](https://docs.vllm.ai#features)

## Compatibility Matrix[¶](https://docs.vllm.ai#compatibility-matrix)

The tables below show mutually exclusive features and the support on some hardware.

The symbols used have the following meanings:

- ✅ = Full compatibility
- 🟠 = Partial compatibility
- ❌ = No compatibility
- ❔ = Unknown or TBD

Note

Check the ❌ or 🟠 with links to see tracking issue for unsupported feature/hardware combination.

### Feature x Feature[¶](https://docs.vllm.ai#feature-x-feature)

| Feature |
|
|---|

[APC](https://docs.vllm.ai/automatic_prefix_caching/)

[LoRA](https://docs.vllm.ai/lora/)

[SD](https://docs.vllm.ai/speculative_decoding/)

[pooling](https://docs.vllm.ai/models/pooling_models/)

[prompt-embeds](https://docs.vllm.ai/prompt_embeds/)

[CP](https://docs.vllm.ai/configuration/optimization/#chunked-prefill)[APC](https://docs.vllm.ai/automatic_prefix_caching/)[LoRA](https://docs.vllm.ai/lora/)[SD](https://docs.vllm.ai/speculative_decoding/)[pooling](https://docs.vllm.ai/models/pooling_models/)[❌](https://github.com/vllm-project/vllm/issues/7366)[❌](https://github.com/vllm-project/vllm/issues/7366)[mm](https://docs.vllm.ai/multimodal_inputs/)[🟠](https://github.com/vllm-project/vllm/pull/4194)^[❌](https://github.com/vllm-project/vllm/issues/6137)[❌](https://github.com/vllm-project/vllm/issues/7968)[❌](https://github.com/vllm-project/vllm/issues/6137)[❌](https://github.com/vllm-project/vllm/issues/7968)[prompt-embeds](https://docs.vllm.ai/prompt_embeds/)* Chunked prefill and prefix caching are only applicable to last-token or all pooling with causal attention.

^ LoRA is only applicable to the language backbone of multimodal models.

### Feature x Hardware[¶](https://docs.vllm.ai#feature-x-hardware)

| Feature | Volta | Turing | Ampere | Ada | Hopper | CPU | AMD | Intel GPU |
|---|---|---|---|---|---|---|---|---|
|

[❌](https://github.com/vllm-project/vllm/issues/2729)[APC](https://docs.vllm.ai/automatic_prefix_caching/)[❌](https://github.com/vllm-project/vllm/issues/3687)[LoRA](https://docs.vllm.ai/lora/)[SD](https://docs.vllm.ai/speculative_decoding/)[❌](https://github.com/vllm-project/vllm/issues/26970)[pooling](https://docs.vllm.ai/models/pooling_models/)[mm](https://docs.vllm.ai/multimodal_inputs/)[prompt-embeds](https://docs.vllm.ai/prompt_embeds/)[❌](https://github.com/vllm-project/vllm/issues/8477)Note

For information on feature support on Google TPU, please refer to the [TPU-Inference Recommended Models and Features](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models_features/) documentation.