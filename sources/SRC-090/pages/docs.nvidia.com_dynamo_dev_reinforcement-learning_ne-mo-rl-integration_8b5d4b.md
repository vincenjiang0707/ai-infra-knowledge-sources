source: https://docs.nvidia.com/dynamo/dev/reinforcement-learning/ne-mo-rl-integration
lastmod: 2026-09-24T19:58:16.636Z

# NeMo RL Integration

**Experimental.** NeMo RL includes a managed Dynamo generation backend with a pinned runtime and dedicated GPU functional test. NeMo RL launches and owns a fixed Dynamo vLLM fleet inside its Slurm/Ray allocation; it does not connect to an existing Dynamo deployment or require Kubernetes.

## Integration Shape

The reviewed NeMo RL integration pins `ai-dynamo[vllm]==1.3.0.post1`

and its compatible vLLM environment. Do not replace that runtime with current Dynamo `main`

or a newer wheel without rerunning the functional and training checks.

## Prerequisites

- A Slurm site supported by NeMo RL’s Ray launcher
- A full-node allocation with at least two GPUs available to the recipe
- A container registry and image-conversion path readable by the Slurm site
- Model, data, results, and container paths shared where required by the allocation

## Build the Runtime

Clone the reviewed NeMo RL source and build its opt-in Dynamo layer:

Replace the registry with one available to your site and record the resolved image digest. Convert the image to the format expected by the Slurm environment using the site’s normal NeMo RL workflow.

## Configure the Backend

Start from the pinned `examples/configs/grpo_math_1B_dynamo.yaml`

. Its essential generation settings are:

NeMo RL validates which vLLM options are translated, managed, unsupported, or ignored by the Dynamo backend. Treat configuration warnings and errors as contract checks rather than assuming every normal vLLM field reaches `dynamo.vllm`

.

## Run the Training Smoke

Set the site-specific allocation values and submit the pinned two-step recipe from the NeMo RL repository root:

Set `GPUS_PER_NODE`

to the physical GPU count expected by the partition. The launcher requests an exclusive full node even though the small recipe uses one training GPU and one generation GPU.

The upstream functional entry point is:

Run it only in the purpose-built Dynamo image on a compatible allocation. A passing result covers the pinned configuration, not other models, topologies, Dynamo versions, or Slurm environments.

## Verify the Run

### Token Correctness

Direct GRPO sends token-ID prompts to `/v1/completions`

and consumes returned completion token IDs and log probabilities. NeMo Gym uses a local chat wrapper with `nvext.token_data`

. Validate both paths separately when your workload uses both; missing token IDs, missing log probabilities, or mismatched lengths must fail the sample.

### Policy Refit

NeMo RL fixes worker membership, creates a trainer-plus-inference NCCL world, drains generation, applies the target checkpoint to each worker, clears stale cache state, and resumes the fleet. Verify that every worker completes the refit and cache barrier before post-update generation begins. A per-worker success is not a fleet transaction, and this path does not replace failed workers in place.

### Routing and Telemetry

Compare the example’s `kv`

router with `round-robin`

while holding prompts, concurrency, engine count, update cadence, and cache-reset behavior fixed. NeMo RL can poll per-worker Dynamo and vLLM metrics, but the current integration does not provide a lossless rollout-to-Dynamo request identity. Keep trainer step, rollout, attempt, target policy, and accepted sample identity in NeMo RL records.

## Troubleshoot

Keep new rollout admission gated after any refit or cache-control failure. See [Distribute and Update Rollout Weights](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rollout-weight-updates#nemo-rl-managed-update) and [Profile and Simulate RL Rollouts](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-profiling-and-simulation) for the shared lifecycle and telemetry boundaries.

## Current Limitations

- Managed Slurm/Ray and vLLM only; no external Dynamo fleet, Kubernetes deployment, SGLang, or TensorRT-LLM path
- Fixed, non-colocated fleet; no elastic worker replacement during the update lifecycle
- No general policy-version transaction or automatic rollback
- No current lossless framework rollout-to-Dynamo request join
- Supported status requires an independent reproduction with token correctness, refit, post-update generation, and failure recovery