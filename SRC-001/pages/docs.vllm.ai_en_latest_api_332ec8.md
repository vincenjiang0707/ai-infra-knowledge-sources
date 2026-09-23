source: https://docs.vllm.ai/en/latest/api/
lastmod: 2026-09-23

# Summary[¶](https://docs.vllm.ai#summary)

## Configuration[¶](https://docs.vllm.ai#configuration)

API documentation for vLLM's configuration classes.

[vllm.config.ModelConfig](https://docs.vllm.ai/vllm/config/#vllm.config.ModelConfig)[vllm.config.CacheConfig](https://docs.vllm.ai/vllm/config/#vllm.config.CacheConfig)[vllm.config.LoadConfig](https://docs.vllm.ai/vllm/config/#vllm.config.LoadConfig)[vllm.config.ParallelConfig](https://docs.vllm.ai/vllm/config/#vllm.config.ParallelConfig)[vllm.config.SchedulerConfig](https://docs.vllm.ai/vllm/config/#vllm.config.SchedulerConfig)[vllm.config.DeviceConfig](https://docs.vllm.ai/vllm/config/#vllm.config.DeviceConfig)[vllm.config.SpeculativeConfig](https://docs.vllm.ai/vllm/config/#vllm.config.SpeculativeConfig)[vllm.config.LoRAConfig](https://docs.vllm.ai/vllm/config/#vllm.config.LoRAConfig)[vllm.config.MultiModalConfig](https://docs.vllm.ai/vllm/config/#vllm.config.MultiModalConfig)[vllm.config.PoolerConfig](https://docs.vllm.ai/vllm/config/#vllm.config.PoolerConfig)[vllm.config.StructuredOutputsConfig](https://docs.vllm.ai/vllm/config/#vllm.config.StructuredOutputsConfig)[vllm.config.ProfilerConfig](https://docs.vllm.ai/vllm/config/#vllm.config.ProfilerConfig)[vllm.config.ObservabilityConfig](https://docs.vllm.ai/vllm/config/#vllm.config.ObservabilityConfig)[vllm.config.KVTransferConfig](https://docs.vllm.ai/vllm/config/#vllm.config.KVTransferConfig)[vllm.config.CompilationConfig](https://docs.vllm.ai/vllm/config/#vllm.config.CompilationConfig)[vllm.config.VllmConfig](https://docs.vllm.ai/vllm/config/#vllm.config.VllmConfig)

## Offline Inference[¶](https://docs.vllm.ai#offline-inference)

LLM Class.

Prompt schema for LLM APIs.

## vLLM Engines[¶](https://docs.vllm.ai#vllm-engines)

Engine classes for offline and online inference.

## Inference Parameters[¶](https://docs.vllm.ai#inference-parameters)

Inference parameters for vLLM APIs.

## Multi-Modality[¶](https://docs.vllm.ai#multi-modality)

vLLM provides experimental support for multi-modal models through the [vllm.multimodal](https://docs.vllm.ai/vllm/multimodal/#vllm.multimodal) package.

Multi-modal inputs can be passed alongside text and token prompts to [supported models](https://docs.vllm.ai/models/supported_models/#list-of-multimodal-language-models) via the `multi_modal_data`

field in [vllm.inputs.PromptType](https://docs.vllm.ai/vllm/inputs/#vllm.inputs.PromptType).

Looking to add your own multi-modal model? Please follow the instructions listed [here](https://docs.vllm.ai/contributing/model/multimodal/).

### Internal data structures[¶](https://docs.vllm.ai#internal-data-structures)

[vllm.multimodal.inputs.PlaceholderRange](https://docs.vllm.ai/vllm/multimodal/inputs/#vllm.multimodal.inputs.PlaceholderRange)[vllm.multimodal.inputs.NestedTensors](https://docs.vllm.ai/vllm/multimodal/inputs/#vllm.multimodal.inputs.NestedTensors)[vllm.multimodal.inputs.MultiModalFieldElem](https://docs.vllm.ai/vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalFieldElem)[vllm.multimodal.inputs.MultiModalFieldConfig](https://docs.vllm.ai/vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalFieldConfig)[vllm.multimodal.inputs.MultiModalKwargsItem](https://docs.vllm.ai/vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalKwargsItem)[vllm.multimodal.inputs.MultiModalKwargsItems](https://docs.vllm.ai/vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalKwargsItems)