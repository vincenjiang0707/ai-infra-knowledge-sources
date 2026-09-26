source: https://docs.nvidia.com/dynamo/dev/reinforcement-learning/external-trainer-integration
lastmod: 2026-09-24T19:58:16.636Z

# External Trainer Integration

**Experimental.** Use this guide when your RL framework does not have a maintained Dynamo integration. The shared contract is intentionally small: send rollout generation through the Dynamo frontend, use discovery when the selected backend advertises it, send administrative operations directly to workers, and keep training decisions in the framework.

An external trainer does not need to be written in Python to call Dynamo’s HTTP APIs. A framework-specific adapter may still need Python or backend libraries for checkpoint conversion, collective communication, ModelExpress, or colocated execution.

## Connect to Dynamo

Start with the canonical [request, discovery, and administration contract](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#separate-the-three-planes). The trainer sends generation through the shared frontend, reads worker capabilities from the RL listener when the backend supports it, and sends mutating operations directly to trusted worker URLs.

These surfaces do not form a fleet transaction. The trainer or rollout orchestrator owns barriers, retry policy, sample acceptance, policy freshness, and recovery from partial updates. The integration reference also defines the trusted-network boundary for discovery and administration.

## Generate Rollouts

Use the native SGLang interface when the adapter already consumes SGLang request and streaming response objects:

Set `DYN_SGLANG_ENABLE_GENERATE=1`

on the frontend. The worker must accept token input; do not start it with `--use-sglang-tokenizer`

, which selects text input and prevents the worker from advertising `/generate`

.

Use an OpenAI-compatible route when the adapter needs one envelope across backends or named NVIDIA request extensions. This example bypasses frontend tokenization and asks Dynamo to return the effective prompt token sequence, generated token IDs, and prompt log probabilities:

`nvext.token_data`

supplies pre-tokenized request input. `nvext.extra_fields`

selects response metadata; `prompt_token_ids`

returns the effective single-prompt token sequence used after preprocessing, including pre-tokenized input.

Treat the engine’s token sequence as authoritative. Do not reconstruct training tokens from generated text. Before accepting a sample, check token and log-probability alignment, the terminal state, the selected model and tokenizer, and the framework’s mask and retry rules. See [RL Integration Reference](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#know-what-returns-to-the-trainer) for the data Dynamo can return and what remains framework-owned.

## Discover and Administer Workers

For RL-enabled vLLM workers, enable the dedicated listener and query it before each control phase:

Require protocol version `1`

, use the returned `system_url`

, and treat `routes`

as the capability list for that specific process. Do not derive a worker administration URL from its request-plane URL or interpret the order of the worker list as a rank map. SGLang workers do not currently register with this listener, so their trusted administration URLs must come from the deployment or framework.

The [discovery response](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#discover-workers-safely) and [vLLM/SGLang administration matrix](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#compare-vllm-and-sglang-administration) show the exact differences an adapter must handle.

## Choose a Policy Update Path

ModelExpress supports trainer-to-inference, artifact-to-inference, and inference-to-inference paths, but they are not one interchangeable API or a universal RL update contract. The current refit surface is Experimental and path-specific. See [Distribute and Update Rollout Weights](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rollout-weight-updates) for current boundaries, including fleet atomicity, deltas, quantization, version state, and replacement workers.

## Validate the Adapter

Before publishing an integration:

- Complete a rollout with authoritative token IDs, aligned log probabilities, a recognized terminal state, and the framework’s acceptance checks.
- Exercise streaming cancellation and retry without accepting the same sample twice.
- Negotiate the required worker capabilities and keep mutating calls on the trusted administration network.
- Complete one policy update across the intended worker set, clear incompatible cache state, verify every target, and generate again.
- Inject a missing-worker, transfer, and post-update failure and confirm the fleet remains gated or excludes the failed worker.
- Correlate the framework’s request identity with Dynamo traces without placing unbounded identifiers in metric labels.

Start with [KV-Aware Load Balancing](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/kv-aware-load-balancing) when routing is the bottleneck, or [RL Profiling and Simulation](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-profiling-and-simulation) when you need to capture and replay the serving workload.