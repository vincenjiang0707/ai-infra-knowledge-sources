source: https://docs.vllm.ai/en/latest/serving/offline_inference/
lastmod: 2026-09-24

# Offline Inference[¶](https://docs.vllm.ai#offline-inference)

Offline inference is possible in your own code using vLLM's [ LLM](https://docs.vllm.ai/api/vllm/#vllm.LLM) class.

## Model Types[¶](https://docs.vllm.ai#model-types)

vLLM models can be categorized into two types:

-
- Models that produce text completions or chat responses (e.g., LLaMA, Qwen, DeepSeek). Use[Generative Models](https://docs.vllm.ai/models/supported_models/)`LLM.generate()`

and`LLM.chat()`

for these models. -
- These models do not generate content. They are primarily used for classification and retrieval tasks, such as bge-m3 and Qwen3 Reranker.[Pooling Models](https://docs.vllm.ai/models/pooling_models/)

## Generative APIs[¶](https://docs.vllm.ai#generative-apis)

For further details on generative models, please refer to [this page](https://docs.vllm.ai/models/supported_models/).

`LLM.generate`

- Generates completions for the given input prompts.`LLM.chat`

- Generates responses for a chat conversation.

## Asynchronous Queue APIs[¶](https://docs.vllm.ai#asynchronous-queue-apis)

`LLM.enqueue`

- Enqueues prompts for generation without waiting for completion.`LLM.enqueue_chat`

- Enqueues chat conversations for generation without waiting.`LLM.wait_for_completion`

- Waits for all enqueued requests to complete and returns results.

## Pooling APIs[¶](https://docs.vllm.ai#pooling-apis)

For further details on pooling models, please refer to [this page](https://docs.vllm.ai/models/pooling_models/).

`LLM.classify`

- Only applicable to[classification models](https://docs.vllm.ai/models/pooling_models/classify/).`LLM.embed`

- Only applicable to[embedding models](https://docs.vllm.ai/models/pooling_models/embed/).`LLM.score`

- Applicable to[score models](https://docs.vllm.ai/models/pooling_models/scoring/)(cross-encoder, bi-encoder, late-interaction).`LLM.encode`

- Applicable to all[pooling models](https://docs.vllm.ai/models/pooling_models/).

## Profiling APIs[¶](https://docs.vllm.ai#profiling-apis)

For further details on profiling, please refer to [this page](https://docs.vllm.ai/contributing/profiling/).

`LLM.start_profile`

- Starts profiling with an optional custom trace prefix.`LLM.stop_profile`

- Stops the ongoing profiling session.

## Sleep Mode APIs[¶](https://docs.vllm.ai#sleep-mode-apis)

For further details on sleep mode, please refer to [this page](https://docs.vllm.ai/features/sleep_mode/).

`LLM.sleep`

- Puts the engine into sleep mode.`LLM.wake_up`

- Wakes up the engine from sleep mode.

## Cache Management APIs[¶](https://docs.vllm.ai#cache-management-apis)

`LLM.reset_mm_cache`

- Resets the multi-modal cache.`LLM.reset_prefix_cache`

- Resets the prefix cache.

## Metrics APIs[¶](https://docs.vllm.ai#metrics-apis)

For further details on metrics, please refer to [this page](https://docs.vllm.ai/design/metrics/).

`LLM.get_metrics`

- Returns a snapshot of aggregated metrics from Prometheus.

## Weight Transfer APIs (RL Training)[¶](https://docs.vllm.ai#weight-transfer-apis-rl-training)

For further details on Weight Transfer, please refer to [this page](https://docs.vllm.ai/training/weight_transfer/).

`LLM.init_weight_transfer_engine`

- Initializes the weight transfer engine for RL training.`LLM.start_weight_update`

- Starts a new weight update cycle.`LLM.update_weights`

- Updates the model weights.`LLM.finish_weight_update`

- Finishes the current weight update cycle.`LLM.update_weight_version`

- Sets the weight version without updating model weights.`LLM.get_weight_version`

- Returns the latest committed weight version.

## Additional APIs[¶](https://docs.vllm.ai#additional-apis)

`LLM.collective_rpc`

- Executes a method or callable collectively across all workers.`LLM.apply_model`

- Applies a function directly to the model inside each worker.

## API Reference[¶](https://docs.vllm.ai#api-reference)

## Ray Data LLM API[¶](https://docs.vllm.ai#ray-data-llm-api)

Ray Data LLM is an alternative offline inference API that uses vLLM as the underlying engine. This API adds several batteries-included capabilities that simplify large-scale, GPU-efficient inference:

- Streaming execution processes datasets that exceed aggregate cluster memory.
- Automatic sharding, load balancing, and autoscaling distribute work across a Ray cluster with built-in fault tolerance.
- Continuous batching keeps vLLM replicas saturated and maximizes GPU utilization.
- Transparent support for tensor and pipeline parallelism enables efficient multi-GPU inference.
- Reading and writing to most popular file formats and cloud object storage.
- Scaling up the workload without code changes.

## Code

import ray # Requires ray>=2.44.1
from ray.data.llm import vLLMEngineProcessorConfig, build_llm_processor
config = vLLMEngineProcessorConfig(model_source="unsloth/Llama-3.2-1B-Instruct")
processor = build_llm_processor(
config,
preprocess=lambda row: {
"messages": [
{"role": "system", "content": "You are a bot that completes unfinished haikus."},
{"role": "user", "content": row["item"]},
],
"sampling_params": {"temperature": 0.3, "max_tokens": 250},
},
postprocess=lambda row: {"answer": row["generated_text"]},
)
ds = ray.data.from_items(["An old silent pond..."])
ds = processor(ds)
ds.write_parquet("local:///tmp/data/")


For more information about the Ray Data LLM API, see the [Ray Data LLM documentation](https://docs.ray.io/en/latest/data/working-with-llms.html).