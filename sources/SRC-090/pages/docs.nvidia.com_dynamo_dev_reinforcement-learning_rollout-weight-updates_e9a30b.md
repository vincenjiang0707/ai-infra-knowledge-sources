source: https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rollout-weight-updates
lastmod: 2026-09-24T19:58:16.636Z

# Distribute and Update Rollout Weights

A live policy refresh is more than tensor transfer. The RL framework must select the target workers, gate generation, apply one policy, clear stale cache state, verify readiness, and decide when new rollouts can begin. Dynamo exposes backend controls but does not provide a fleet-wide atomic update.

## Choose a ModelExpress Source

[ModelExpress](https://github.com/ai-dynamo/modelexpress/tree/main/modelexpress_client/python/modelexpress_rl) can move a policy from a trainer, object storage, or another inference worker. Its RL refit client separates transfer from installation so an inference worker can stage a version, apply it at an orchestrator-selected safe point, and then publish that applied version as a compatible peer source.

ModelExpress can stage a version from three sources:

**Trainer to inference:**trainer ranks publish the GPU shards they already own and each inference rank pulls the ranges required by its own layout over NIXL.**Artifact to inference:**an inference worker prepares a canonical checkpoint from S3, including the current exact-base XOR delta format, before engine installation.**Inference to inference:**after an inference worker applies a version, a rank-compatible worker can pull that version from it instead of returning to the trainer.

All three refit paths are Experimental. The [ModelExpress RL refit package](https://github.com/ai-dynamo/modelexpress/tree/main/modelexpress_client/python/modelexpress_rl) contains the current source strategies. The [Dynamo vLLM reshard refit example](https://github.com/ai-dynamo/modelexpress/tree/main/examples/rl/dynamo_vllm_reshard_refit) validates the full-weight trainer-to-inference path, and the [Dynamo vLLM S3 delta refit example](https://github.com/ai-dynamo/modelexpress/tree/main/examples/rl/dynamo_vllm_s3_delta_refit) exercises the artifact-to-inference path with a full snapshot followed by incremental deltas. Neither qualifies every backend and topology. ModelExpress startup loading remains a separate boot and scale-out workflow.

ModelExpress startup loading and live RL refit have different interfaces. vLLM 0.23 and later use the native `--load-format modelexpress`

; `mx`

remains a backward-compatible alias. Earlier plugin-based images generally use `mx`

, while legacy split-loader images can expose `mx-source`

and `mx-target`

. Match the loader to the installed vLLM, ModelExpress package, and runtime image instead of inferring it from the refit API. See [Dynamo deprecations](https://docs.nvidia.com/dynamo/reference/releases/deprecations) for the Dynamo-owned loader migration.

## Choose the Update Path

The transport name does not determine compatibility. Record checkpoint format, source and destination parallel layouts, rank mapping, dtype, group membership, resharding, network transport, and failure behavior.

## Know the Current Contract Boundaries

## Use the Shared Refresh Lifecycle

Follow the canonical [policy-refresh lifecycle](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#coordinate-policy-refresh) for every transfer path. Persist the target policy identity and every worker result; do not infer fleet success from one worker, one HTTP 200 response, or one trainer send. The sections below describe only the backend- and framework-specific differences.

## Update a vLLM Worker from Disk

Start the RL listener and worker as described in [RL Integration Reference](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference#discover-workers-safely). Discover workers with `GET /v1/rl/workers`

, require protocol version `1`

, and select only workers that advertise `pause_generation`

, `update_weights_from_disk`

, `get_weight_version`

, and `resume_generation`

.

Use each returned `system_url`

. The following shape updates one worker and keeps it paused if validation fails:

Repeat the operation under one framework-owned barrier for the complete target set. The version is caller-supplied metadata, not a tensor digest; pair it with update success, cache handling, and post-update generation.

For distributed vLLM updates, use the advertised group lifecycle and distributed-update routes only with the exact request schema and rank mapping validated by the integration. Treat group-initialization timeout as worker failure because the backend process can remain blocked.

## Update an SGLang Worker from Disk

**Experimental.** SGLang workers do not currently register with `GET /v1/rl/workers`

. Set `DYN_SYSTEM_PORT`

on each worker and obtain its trusted system-server URL from the framework or deployment. Do not derive that URL from the shared frontend address.

SGLang exposes fixed weight-update routes under `/engine/control/*`

. Generation pause and continue methods must be explicitly allowlisted when the integration needs a framework-owned update barrier:

After the framework gates new rollout work, update one worker with the request schema supported by the installed SGLang version:

Repeat this sequence across the framework-selected worker set under one barrier. The fixed update response reports `success`

, `message`

, and paused-request count, but SGLang does not currently expose the vLLM discovery and `get_weight_version`

contract. Keep the target version in the orchestrator, check every response body, and require post-update generation before admitting the worker.

The built-in disk update can flush SGLang’s local cache. Validate any additional host, disk, or shared cache tier separately. Distributed, tensor, and IPC update routes use the request schemas of the installed SGLang version; the [SGLang engine-route reference](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/sg-lang/reference-guide#engine-routes) documents the fixed routes and explicit method allowlist.

## verl Colocated Update

The public verl recipe sends generation through Dynamo but keeps sleep, wake, and weight transfer in recipe-owned Ray actors and a ZMQ/CUDA IPC bridge. Do not replace this path with public worker discovery unless the integration itself changes.

Verify that every data-parallel shard receives the same trainer step, old cache state is handled, and every worker resumes before post-update rollout generation. See [verl Integration](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/verl-integration#verify-the-run).

## NeMo RL Managed Update

NeMo RL records a fixed vLLM fleet, creates one trainer-plus-inference NCCL world, drains generation, applies the checkpoint to every engine, clears cache state in a separate pause phase, and resumes only after the framework collects all results.

This path prevents a dead or replaced worker from silently joining with initial weights, but it is not elastic and has no fleet-wide rollback. Keep the rollout phase gated after any worker, refit, cache, or resume failure. See [NeMo RL Integration](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/ne-mo-rl-integration#policy-refit).

## Keep Cache and Version State Correct

KV entries created under one policy are invalid under another policy even when token IDs are unchanged. Identify every device, host, disk, or shared cache tier and verify how each tier is cleared before generation resumes. Separate required cold-cache warm-up from steady-state measurements.

Use an immutable checkpoint ID or digest as the target policy identity. Record the framework step, intended worker set, previous and target versions, transfer and cache-reset timing, readiness, and post-update request. A readable version string alone does not prove which tensors are resident, and the current router does not select workers by that value.

## Handle Partial Failure

Always check both HTTP status and the backend-specific response body. A practical rollback can require reapplying the previous checkpoint or replacing the worker; test that path before enabling asynchronous updates.

## Validate the Complete Update

Record the target policy, selected worker set, request gate, transfer parameters, per-worker apply and cache results, version and liveness checks, post-update generation, and update duration. Inject at least one missing-worker, transfer, and post-update failure.

Do not call a path supported when only transfer bandwidth or one-worker success was measured. Readiness, cache correctness, failure recovery, and useful post-update rollout generation are part of the contract.