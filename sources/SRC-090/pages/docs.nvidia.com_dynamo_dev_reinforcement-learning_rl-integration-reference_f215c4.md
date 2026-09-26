source: https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rl-integration-reference
lastmod: 2026-09-24T19:58:16.636Z

# RL Integration Reference

Use this reference when implementing or reviewing a Dynamo rollout adapter. It defines the shared serving contract once; framework guides describe only what differs for that integration.

This reference tracks the current `dev`

documentation and Dynamo `main`

. For a released version, use the matching versioned documentation and confirm that the selected backend advertises the required routes.

## Separate the Three Planes

Send rollout inference through the shared frontend. Send mutating operations only to selected workers. The discovery endpoint is read-only and does not create a fleet-wide transaction.

Discovery and worker administration do not add a separate authentication layer. Keep them on a trusted orchestrator network and expose only the backend methods the integration requires.

## Choose a Request Interface

Use the native SGLang route when the framework already speaks that schema. Use an OpenAI-compatible route when the adapter needs one request envelope across backends or named `nvext`

response fields.

## Preserve Token Authority

The engine token sequence used for training is authoritative. Do not reconstruct it by tokenizing generated text; chat templates, normalization, special tokens, and tokenizer versions can change the result.

For OpenAI-compatible completions, send token IDs and request generated token IDs explicitly:

Before admitting a sample to training, verify:

- Generated token IDs are present and contain the expected number of choices.
- Selected log probabilities match those token IDs in length and order.
- Prompt log probabilities preserve undefined positions instead of shifting alignment.
- The response has a terminal state recognized by the framework.
- The tokenizer and model identity match the selected rollout worker.

`POST /v1/responses/input_tokens`

estimates input size for preflight decisions. It does not return authoritative token IDs, verify the model or tokenizer, or prove that a worker is ready.

## Know What Returns to the Trainer

See [NVIDIA Request Extensions](https://docs.nvidia.com/dynamo/dev/additional-resources/nvidia-request-extensions-nvext) for the complete `nvext`

request and response shapes.

## Handle Streaming and Retries

Treat a streaming request as a state machine: accepted, streaming, terminal success, canceled, or failed. Admit only a verified terminal result. Preserve attempt identity when retrying, because a timed-out request may have completed after the client stopped waiting and generation is not idempotent.

The framework owns retry policy, duplicate suppression, partial-rollout handling, and sample acceptance. Dynamo propagates supported cancellations and serving failures but does not decide whether a partial attempt is scoreable.

## Discover Workers Safely

Start the RL listener and an RL-enabled vLLM worker on the trusted control network:

A protocol version `1`

response has this shape. Optional fields such as `model`

, `system_url`

, `admin_base_url`

, and `world_size`

appear only when the worker provides them:

Check `protocol_version`

before reading the worker list. In protocol version `1`

:

Refresh discovery before each control phase and require the complete capability set for the selected update path. Do not cache membership indefinitely or interpret list position as worker identity.

### Scope Discovery by Namespace

The RL listener reads the set of Dynamo namespaces it searches from its own process environment, and from nothing else. The `--namespace`

and `--namespace-prefix`

frontend flags scope model discovery only; neither writes its value back into the environment. A frontend started with `--namespace-prefix ns`

and no `DYN_NAMESPACE_PREFIX`

set therefore gets prefix-scoped model discovery and exact-scoped RL discovery. Set the environment variable, not the flag, to scope RL discovery.

Three variables decide that scope, and the first one that applies wins:

The `dynamo`

value is the one case where a prefix deliberately reaches past its own deployment: every other deployment’s pause, resume, and weight-update endpoints then appear in this listener’s `/v1/rl/workers`

. On Kubernetes it is opt-in through `globalDynamoNamespace: true`

, which makes the operator set `DYN_NAMESPACE_PREFIX=dynamo`

. Use it only when one trainer is meant to control every deployment in the cluster.

An empty `DYN_NAMESPACE_PREFIX`

or `DYN_NAMESPACE_WORKER_SUFFIX`

counts as absent, exactly as an unset one does. An empty `DYN_NAMESPACE`

does not: it is the namespace to search. Model discovery agrees with RL discovery on the `dynamo`

value but not on the empty one, where it reads an empty `DYN_NAMESPACE_PREFIX`

as every namespace rather than as absent.

This ordering matters because a worker that is given `DYN_NAMESPACE_WORKER_SUFFIX`

registers under `{DYN_NAMESPACE}-{suffix}`

, not under `{DYN_NAMESPACE}`

. A listener configured for the bare namespace would find none of those workers.

When the Dynamo Kubernetes Operator manages the deployment, it sets `DYN_NAMESPACE_PREFIX`

on the frontend container, so the listener matches every worker generation at once, including the two generations that coexist during a rolling update. For a listener that the operator does not manage, including an unmanaged Kubernetes deployment or a deployment outside Kubernetes, configure the listener’s namespace scope explicitly. To reach the workers of one suffixed pool:

`DYN_NAMESPACE_PREFIX`

is also documented in the [frontend configuration reference](https://docs.nvidia.com/dynamo/dev/reference/components/frontend-configuration), and `DYN_NAMESPACE_WORKER_SUFFIX`

in the [runtime configuration reference](https://docs.nvidia.com/dynamo/dev/reference/components/runtime-configuration). Those pages describe how the variables scope model discovery; this section describes the RL listener only.

## Coordinate Policy Refresh

The framework owns the fleet-level lifecycle:

- Gate new rollout work for the target workers.
- Resolve the current worker set and required capabilities.
- Pause or drain workers when the backend requires it.
- Transfer and apply one target policy.
- Invalidate stale KV state.
- Verify every worker and run post-update generation before reopening the fleet.

Per-worker success is not fleet-wide atomicity. Keep generation gated when membership changes, an update fails, cache reset fails, or post-update generation does not pass. See [Distribute and Update Rollout Weights](https://docs.nvidia.com/dynamo/dev/reinforcement-learning/rollout-weight-updates) for the supported paths and recovery rules.

## Compare vLLM and SGLang Administration

The backends do not share one administration schema. Use the exact route returned by discovery or configured by the deployment, and validate request bodies against the installed backend version.

Even two vLLM deployments can expose different route families because the Python worker and native sidecar adapt different backend control APIs. Never prepend, remove, or rename route segments returned in `routes`

.

### Read and Declare the Weight Version

A Python vLLM worker reports the last weight version declared to it through `get_weight_version`

:

A worker tracks only the versions declared to it. `version_declared`

is `false`

, with `version`

set to `null`

, until something declares one, either through a `/engine/`

weight-update route that carries `weight_version`

or through `set_weight_version`

. Branch on `version_declared`

rather than comparing `version`

against a placeholder string: any string, including `"initial"`

, is a legal version tag that a caller can declare.

For each Python vLLM worker, check that `routes`

from `GET /v1/rl/workers`

includes `set_weight_version`

before relying on `version_declared`

. Older workers omit both that route and the response field; treat a missing `version_declared`

as unsupported declaration tracking, not as `false`

, because their `"initial"`

version cannot distinguish an undeclared worker from an explicit declaration.

Version declarations accept any JSON value, including `null`

. An explicit `{"weight_version": null}`

is a declaration: `get_weight_version`

then returns `"version": null`

with `"version_declared": true`

.

A successful weight-update reply includes `version_declared`

to indicate whether that update declared a version. If the request omits `weight_version`

, the reply contains `"version": "unknown"`

and `"version_declared": false`

, and the previous declaration remains unchanged. An explicit `{"weight_version": "unknown"}`

returns the same version with `"version_declared": true`

. In an update reply, this flag describes the update; in `get_weight_version`

, it describes the stored declaration. A worker with no previous declaration remains undeclared after an update that omits the version. Pass `weight_version`

on every update whose version you want the worker to report.

A worker reports the last version declared to it, not the weights loaded in its GPU memory. Dynamo observes only the weight updates that traverse its own `/engine/`

routes. Loading weights by another path, such as calling `collective_rpc`

on the engine object directly, leaves the reported version stale unless the loader declares the new version.

When an RL framework loads weights outside Dynamo, declare the resulting version so the worker reports it. `set_weight_version`

records the version without loading weights:

The route requires `weight_version`

in the body and returns `{"status": "error"}`

when it is missing. It neither pauses generation nor invalidates the prefix cache, so a caller that changed the weights must handle both itself.

## Framework Compatibility

A status reflects the documented integration, not whether the framework can call a generic HTTP endpoint.

## Backend Compatibility

Backend support does not imply every topology or framework combination is validated. Record aggregated or prefill/decode serving, placement, model parallelism, model class, cancellation, discovery, weight layout, and cache behavior for the path you test.

## Integration Checklist

Before publishing a runnable integration, verify:

- Generation reaches the intended Dynamo frontend and backend.
- Token IDs, log probabilities, masks, and terminal states match the framework contract.
- Retries and cancellations cannot admit the same sample twice.
- Discovery is refreshed and every administration route is negotiated.
- Mutating calls use direct worker URLs on a trusted network.
- One complete training iteration includes policy refresh and post-update generation.
- Request, worker, and update failures have a tested recovery path.
- Framework identity can be correlated with Dynamo telemetry without high-cardinality metric labels.
- The tested versions, environment, and topology are recorded with the integration.