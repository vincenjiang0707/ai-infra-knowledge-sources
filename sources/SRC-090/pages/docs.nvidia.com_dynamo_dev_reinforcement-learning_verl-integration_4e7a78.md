source: https://docs.nvidia.com/dynamo/dev/reinforcement-learning/verl-integration
lastmod: 2026-09-24T19:58:16.636Z

# verl Integration

Run the public verl-recipe Dynamo rollout backend

**Experimental.** verl-recipe provides an asynchronous Dynamo rollout backend with a shared frontend, vLLM workers, routing, and colocated policy updates. Use the upstream recipe as the implementation source of truth; this page covers the shortest Dynamo workflow and its support boundary.

## Integration Shape

The native router and ThunderAgent are different scheduling paths. Choose one before building the environment and do not compare their results as if only a router flag changed.

## Prerequisites

- A Linux GPU environment that satisfies the selected verl, Dynamo, vLLM, CUDA, and PyTorch versions
`git`

, Python,`etcd`

, and`nats-server`

`flash-attn`

, installed explicitly as its own step under Prepare the Source. The selected verl core reaches`flash_attn.bert_padding`

through`verl/utils/attention_utils.py`

on the CUDA path with no fallback, but declares the dependency in neither`requirements.txt`

nor`pyproject.toml`

, and the installer does not add it. Without it the training iteration stops at`ModuleNotFoundError: No module named 'flash_attn'`

- Model and dataset paths visible on every participating node
- Enough GPUs for the trainer and rollout layout; the validation smoke is not a full training run

## Prepare the Source

The reviewed recipe snapshot is `461b830c`

, and its `REQUIRED_VERL.txt`

selects the matching core verl commit. The core commit records an older recipe submodule, so use the installer and then set the nested recipe checkout to the same reviewed snapshot:

The recipe does not pin a complete Dynamo/vLLM image for the native-router path. Build one clean environment, record its immutable image and package versions, and keep the Dynamo and nested recipe checkouts clean during validation.

Build that environment on vLLM `0.26.0`

, which is what `ai-dynamo[vllm]==1.4.x`

pins. The verl commit selected by this snapshot imports `FusedMoE`

from `vllm.model_executor.layers.fused_moe.layer`

at import time in `verl/utils/vllm/vllm_fp8_utils.py`

. vLLM exports that name up to and including `0.26.0`

and renamed it to `FusedMoEFactory`

in `0.27.0`

, so the import fails from `0.27.0`

onward. On `ai-dynamo[vllm]==1.5.0`

, which pins `vllm[flashinfer,runai,otel]==0.28.0`

, loading the Dynamo rollout backend raises `ImportError: FP8 quantization not available`

and the Dynamo stack never starts.

### Install flash-attn

`install_verl.sh`

does not install `flash-attn`

, so add it to the same environment before running anything below:

Run this after PyTorch is installed. `--no-build-isolation`

is what lets the build compile against the PyTorch already in the environment; upstream requires PyTorch `2.2`

or newer and CUDA `12.0`

or newer. Confirm `ninja --version`

exits `0`

first — a broken `ninja`

leaves the build single-threaded and it can then take hours instead of minutes. Lower `MAX_JOBS`

if the machine runs out of RAM during the build. See the [FlashAttention project](https://github.com/Dao-AILab/flash-attention) for platform notes and prebuilt wheels.

The selected verl also lists `flash-attn`

in the `gpu`

extra of its `setup.py`

(`GPU_REQUIRES`

), so `pip install -e '.[gpu]'`

from the verl checkout is an equivalent route that additionally installs `liger-kernel`

. Neither installer path the recipe uses requests that extra.

## Run the Validation Smoke

Run the upstream validation-only smoke from the resulting verl checkout:

The three overrides are required because the selected verl leaves `use_dynamic_bsz`

at `false`

and defaults every micro-batch field to `null`

, and neither the smoke script nor the recipe’s trainer configuration sets one, so the trainer rejects the run during config validation. The smoke script forwards any extra arguments to the trainer, so pass them on the command line instead of editing the upstream script. Use the `_per_gpu`

form: upstream marks the global form deprecated.

The smoke starts recipe-managed etcd, NATS, a Dynamo vLLM worker, and the shared frontend. `PASS: Dynamo validation smoke completed`

confirms the validation command completed; it does not prove an optimizer step or policy refresh.

## Run a Training Iteration

After the smoke passes, run at least one optimizer step with the same environment. Use the pinned upstream [Dynamo trainer configuration](https://github.com/verl-project/verl-recipe/blob/461b830cfee4f5a67c21edc300c24373230babc7/dynamo/config/dynamo_trainer.yaml) as the baseline, then make the model, data, resource, and routing overrides required for your environment. This example selects the native Dynamo router explicitly:

The three micro-batch overrides are required here for the same reason they are required in the smoke. `actor_rollout_ref.rollout.tensor_model_parallel_size=2`

states the selected verl’s own default rather than changing it: this example runs one rollout that is tensor-parallel across both requested GPUs. Set it to `1`

for two independent rollout workers instead.

Adjust model, data, and resource values for your environment. A passing run must include rollout generation, reward or advantage computation, an actor update, policy synchronization, and generation after the update.

## Verify the Run

Check three boundaries before scaling:

**Generation correctness:**The completion token IDs and selected log probabilities consumed by verl match in length and order. Record terminal and canceled attempts separately.**Policy update:**Every intended rollout shard receives the same trainer step through the recipe’s CUDA IPC path, stale KV state is handled, and post-update generation succeeds.**Routing:**With ThunderAgent disabled, compare`round-robin`

and`kv`

using the same prompts, concurrency, cache state, and update cadence. Report useful framework output, not only request throughput.

Set `request_completion_token_ids=true`

when the framework must score the exact engine tokens. Use [RL Integration Reference](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#preserve-token-authority) for the shared response checks and [KV-Aware Load Balancing for RL Rollouts](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/kv-aware-load-balancing) for the routing experiment.

## Observe and Recover

The training command above enables worker system metrics and starts the provided sidecar before workers come online. The sidecar rediscovers endpoint files throughout the run and writes per-worker snapshots to `/tmp/verl-dynamo/kv-metrics.jsonl`

; starting it only after training leaves no live workers to scrape.

See [Profile and Simulate RL Rollouts](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-profiling-and-simulation) for request tracing and [Distribute and Update Rollout Weights](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rollout-weight-updates#verl-colocated-update) for the policy-update boundary.

## Current Limitations

- The recipe does not provide one complete native-path Dynamo/vLLM image pin.
- The documented policy update is the recipe’s colocated CUDA IPC path, not public Dynamo worker discovery or ModelExpress.
- Multi-node and large-model layouts require separate topology and failure validation.
- Supported status requires an independent run with token correctness, policy refresh, post-update generation, and request, worker, and update recovery.