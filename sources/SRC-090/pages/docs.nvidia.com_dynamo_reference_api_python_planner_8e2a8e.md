source: https://docs.nvidia.com/dynamo/reference/api/python/planner
lastmod: 2026-09-24T19:58:16.636Z

# dynamo.planner

`dynamo.planner`

publishes 31 classes and 0 functions. Source: `components/src/dynamo/planner/__init__.py`


###### BackendFrameworkInvalidError (class)


Raised when the backend framework does not exist.

This occurs when the DynamoGraphDeployment contains an unsupported backend framework.

`components/src/dynamo/planner/errors.py#L152`


**Public methods**

**init**

No summary available.

###### BackendFrameworkNotFoundError (class)


Raised when the backend framework is not supported.

This occurs when the DynamoGraphDeployment contains an unsupported backend framework.

`components/src/dynamo/planner/errors.py#L141`


**Public methods**

**init**

No summary available.

###### ComponentError (class)


Base class for component type configuration issues.

This serves as a parent class for all exceptions related to component type configuration problems in DynamoGraphDeployments.

###### DeploymentModelNameMismatchError (class)


Raised when the model name is not the same in the deployment

`components/src/dynamo/planner/errors.py#L114`


**Public methods**

**init**

No summary available.

###### DeploymentValidationError (class)


Raised when deployment validation fails for multiple components.

This is used to aggregate multiple validation errors into a single exception, providing a comprehensive view of all validation issues.

`components/src/dynamo/planner/errors.py#L211`


**Public methods**

**init**

No summary available.

###### DuplicateSubComponentError (class)


Raised when multiple components have the same planner role.

This occurs when the DynamoGraphDeployment contains more than one component with the same role, which violates the expected uniqueness constraint.

`components/src/dynamo/planner/errors.py#L188`


**Public methods**

**init**

No summary available.

###### DynamoGraphDeploymentNotFoundError (class)


Raised when Parent DynamoGraphDeployment cannot be found.

This typically occurs when:

- The DYN_PARENT_DGD_K8S_NAME environment variable is not set
- The referenced DynamoGraphDeployment doesn’t exist in the namespace

`components/src/dynamo/planner/errors.py#L52`


**Public methods**

**init**

No summary available.

###### DynamoGraphDeploymentNotReadyError (class)


Raised when a DynamoGraphDeployment is not ready for scaling.

`components/src/dynamo/planner/errors.py#L72`


**Public methods**

**init**

No summary available.

###### EmptyTargetReplicasError (class)


Raised when target_replicas is empty or invalid.

This occurs when attempting to set component replicas with an empty or invalid target_replicas dictionary.

`components/src/dynamo/planner/errors.py#L224`


**Public methods**

**init**

No summary available.

###### EngineCapabilities (class)


Static capabilities for a single engine stage (prefill or decode).

`components/src/dynamo/planner/core/types.py#L197`


**Public methods**

**init**

No summary available.

###### FpmObservations (class)


Per-engine ForwardPassMetrics keyed by (worker_id, dp_rank).

`components/src/dynamo/planner/core/types.py#L74`


**Public methods**

**init**

No summary available.

###### GlobalPlannerConnector (class)


Connector that delegates scaling decisions to a centralized GlobalPlanner.

This connector wraps RemotePlannerClient and implements the InfraScaler interface, allowing planner_core.py to treat global-planner environment mode consistently with kubernetes and virtual modes.

`components/src/dynamo/planner/connectors/global_planner.py#L37`


**Public methods**

**init**

Initialize GlobalPlannerConnector.

**Parameters**

Distributed runtime for communication

Local dynamo namespace (caller identification)

Namespace where GlobalPlanner is deployed

Component name of GlobalPlanner (default: “GlobalPlanner”)

Optional model name (will be managed remotely if not provided)

#### async_init

Async initialization - creates RemotePlannerClient

#### set_predicted_load

Set predicted load for inclusion in next scale request.

This is called by planner_core.py before calling set_component_replicas.

#### set_component_replicas

Set component replicas by delegating to GlobalPlanner.

Sends a ScaleRequest to the GlobalPlanner with the target replica configurations.

**Parameters**

List of target replica configurations

Whether to wait for scaling completion (passed to GlobalPlanner)

**Raises**

`EmptyTargetReplicasError`

— If target_replicas is empty`RuntimeError`

— If remote_client is not initialized or the response indicates a hard error (e.g., authorization denied, K8s exception). A REJECTED response is NOT raised — it is logged as a warning and treated as a no-op for this tick.

#### add_component

Add a component (not supported for GlobalPlanner).

GlobalPlanner only supports batch operations via set_component_replicas.

#### remove_component

Remove a component (not supported for GlobalPlanner).

GlobalPlanner only supports batch operations via set_component_replicas.

#### validate_deployment

Validate deployment (no-op for GlobalPlanner).

The GlobalPlanner validates the deployment on its side, so local validation is not needed in delegating mode.

#### wait_for_deployment_ready

Wait for the pool’s own workers to be ready.

Even though GlobalPlanner handles cluster-wide orchestration, the
pool Planner still reads its own workers’ DynamoWorkerMetadata CRs
for capability discovery (`get_worker_info`

). Without a local
wait, `_async_init`

runs within milliseconds of pod entry — long
before workers register MDC — so `get_worker_info`

falls back to
defaults with `context_length`

/ `max_kv_tokens`

unset and
load-scaling silently disables itself for the pod’s lifetime.

Mirror the standalone path by delegating to the pool-local KubernetesConnector. If no local connector is available (e.g. running outside a cluster), fall back to the previous no-op so out-of-cluster callers are not blocked.

#### get_actual_worker_counts

Read ready replica counts and rollout stability from the pool’s own DGD.

GlobalPlanner orchestrates scaling, but the pool Planner pod has direct
access to its own DGD status. Mirror KubernetesConnector by delegating
to the pool-local connector so `_scaling_in_progress`

observes real
rollouts instead of always seeing `is_stable=True`

.

Returns `(0, 0, True)`

when no local KubernetesConnector is available
(e.g. running out-of-cluster), matching the existing capability-discovery
fallback path so out-of-cluster callers aren’t blocked.

#### get_worker_runtime_namespace

Resolve the pool-local worker runtime namespace when available.

#### get_gpu_counts

Resolve pool-local GPU shape when available.

#### get_worker_info

Resolve per-worker capabilities from the pool’s own MDC/DGD.

Without this, `resolve_worker_info`

falls through to
`build_worker_info_from_defaults`

which leaves `context_length`

and `max_kv_tokens`

unset, and load_scaling’s easy-mode decisions
bail out every tick — so the pool Planner silently sends no
ScaleRequests.

#### get_model_name

Get model name.

Prefers the value provided at init time, then the pool’s own DGD container args (via the local KubernetesConnector), and finally falls back to a placeholder indicating the model is managed remotely.

###### KubernetesConnector (class)


No summary available.

`components/src/dynamo/planner/connectors/kubernetes.py#L63`


**Public methods**

**init**

No summary available.

#### async_init

No-op asynchronous lifecycle hook.

#### get_worker_runtime_namespace

Return the Dynamo namespace used by the current worker generation.

Newer operators publish the effective runtime namespace on the worker component status. Older operators expose only the active worker hash, so the planner falls back to appending that hash only for Deployment-backed and LeaderWorkerSet-backed workers.

#### add_component

Add a component by increasing its replica count by 1

#### remove_component

Remove a component by decreasing its replica count by 1

#### validate_deployment

Verify that the deployment contains prefill/decode components and the model name exists. Allows explicit component-name overrides when the caller provides them.

**Raises**

`DynamoGraphDeploymentNotFoundError`

— If the deployment is not found`DeploymentValidationError`

— If the deployment does not contain required prefill/decode components

#### get_model_name

Get the model name from the current deployment.

#### get_gpu_counts

Get the GPU counts for prefill and decode components.

#### get_frontend_metrics_url

Auto-discover the frontend component’s metrics URL from the DGD.

Iterates DGD components to find the component with type “frontend”, then constructs the in-cluster URL using the operator’s naming convention: http://{dgd_name}-{component_name_lowercase}:{port}/metrics

**Returns**

`Optional[str]`

— The metrics URL string, or None if no frontend component is found.

#### wait_for_deployment_ready

Wait for the deployment to be ready.

**Parameters**

If False, skip the planner component when checking readiness. This lets the planner read MDC from worker pods without waiting for itself to be marked ready in the DGD.

#### get_worker_info

Get WorkerInfo for a sub-component, trying MDC first, then fallbacks.

**Parameters**

PREFILL or DECODE

Backend framework name (for default fallback)

#### get_actual_worker_counts

Get actual ready worker counts for prefill and decode from DGD status.

**Returns**

`int`

— tuple[int, int, bool]: (prefill_count, decode_count, is_stable)`int`

— - is_stable: False if any component is in a rollout (scaling should be skipped)

#### set_component_replicas

Set the replicas for multiple components at once

###### ModelNameNotFoundError (class)


Raised when the model name is not found in the deployment

`components/src/dynamo/planner/errors.py#L106`


**Public methods**

**init**

No summary available.

###### PlannerConnector (class)


No summary available.

`components/src/dynamo/planner/connectors/base.py#L28`


**Public methods**

#### async_init

No summary available.

#### validate_deployment

No summary available.

#### wait_for_deployment_ready

No summary available.

#### get_model_name

No summary available.

#### get_gpu_counts

No summary available.

#### get_actual_worker_counts

No summary available.

#### set_component_replicas

No summary available.

###### PlannerEffects (class)


What the core returns after processing a tick.

`components/src/dynamo/planner/core/types.py#L188`


**Public methods**

**init**

No summary available.

###### PlannerError (class)


Base exception for all planner-related errors.

This serves as the root exception class for all custom exceptions in the planner module, allowing for broad exception catching when needed.

###### PlannerScalingState (class)


Shared in-memory scaling state for all planner modes.

Owns perf models, throughput lower bounds, worker inventory, last-value runtime metadata, and all scaling decision logic. It deliberately has no runtime dependencies. Load prediction state lives in the builtin PREDICT plugin and is passed in explicitly.

Builtin orchestrator plugins use this class directly as their private shared core while the remaining cross-plugin state is being split into explicit pipeline artifacts.

`components/src/dynamo/planner/core/state_machine.py#L48`


**Public methods**

**init**

No summary available.

#### update_capabilities

Replace the current worker capabilities.

#### load_benchmark_fpms

No summary available.

#### begin_tick

Reset per-tick diagnostics before builtin plugins run.

#### observe_worker_counts

No summary available.

#### observe_fpm

No summary available.

#### observe_runtime_metadata

Update last-value runtime metadata without touching prediction history.

#### install_regressions

No summary available.

#### advance_load

No summary available.

#### advance_throughput_from_prediction

Run the throughput decision using PREDICT-stage output.

The PREDICT plugin owns load prediction history. This method consumes only explicit prediction output so PROPOSE never re-runs prediction or depends on hidden predictor state.

#### diagnostics

No summary available.

###### SLAPlannerDefaults (class)


###### ScalingDecision (class)


Desired replica counts. `None`

means the core has no opinion on that component (e.g. prefill-only planner leaves decode as None).

`components/src/dynamo/planner/core/types.py#L96`


**Public methods**

**init**

No summary available.

###### ScheduledTick (class)


Declares when the core next needs to be called, what data it needs, and what decisions to make.

`at_s`

is an absolute wall-clock time for the native adapter and a
simulated time for replay. `at_monotonic_s`

is the matching scheduler
timestamp used to make observation-prefetch and plugin-dispatch cadence
decisions against the same clock value.

`components/src/dynamo/planner/core/types.py#L21`


**Public methods**

**init**

No summary available.

###### SubComponentNotFoundError (class)


Raised when a required component role is not found in the deployment.

This occurs when the DynamoGraphDeployment doesn’t contain any component with the requested role (e.g., ‘prefill’, ‘decode’).

`components/src/dynamo/planner/errors.py#L165`


**Public methods**

**init**

No summary available.

###### SubComponentType (class)


###### TargetReplica (class)


###### TickInput (class)


What the adapter provides to the core on each tick.

Fields are filled according to the previous `ScheduledTick`

’s
declared requirements.

`components/src/dynamo/planner/core/types.py#L82`


**Public methods**

**init**

No summary available.

###### TrafficObservation (class)


Aggregated traffic metrics over an observation window.

`components/src/dynamo/planner/core/types.py#L50`


**Public methods**

**init**

No summary available.

###### UserProvidedModelNameMismatchError (class)


Raised when the model name is not the same as the user provided model name

`components/src/dynamo/planner/errors.py#L129`


**Public methods**

**init**

No summary available.

###### VirtualConnector (class)


Coordinate planner scaling decisions for non-native environments.

The connector does not scale a deployment directly. It publishes decisions
through the Dynamo runtime’s `VirtualConnectorCoordinator`

; the deployment
environment consumes them with `VirtualConnectorClient`

and reports scaling
status back to the coordinator.

Virtual deployments do not have a Kubernetes API from which to derive worker
component and endpoint metadata. They therefore require a
`worker_info_provider`

that resolves `WorkerInfo`

from runtime MDC. The
planner factory normally supplies its `RuntimeFpmProvider`

, sharing the same
runtime discovery source used for forward-pass metrics.

`components/src/dynamo/planner/connectors/virtual.py#L30`


**Public methods**

**init**

Initialize a virtual deployment connector.

**Parameters**

Distributed runtime used for coordination and discovery.

Namespace containing the virtual deployment.

Required source of runtime WorkerInfo/MDC used
to locate worker endpoints. `construct_environment`

normally
provides a `RuntimeFpmProvider`

.

Model name reported by the deployment.

#### get_worker_info

No summary available.

#### async_init

Async initialization that must be called after **init**

#### add_component

Add a component by increasing its replica count by 1

#### remove_component

Remove a component by decreasing its replica count by 1

#### set_component_replicas

Set the replicas for multiple components at once

#### validate_deployment

Validate the deployment

#### wait_for_deployment_ready

Wait for the deployment to be ready

#### get_worker_runtime_namespace

No summary available.

#### get_actual_worker_counts

Read active workers from discovery and scaling status from the client ack.

Coordinator worker counts are desired targets, not observations. Runtime endpoint discovery is the source of truth for active workers, while the coordinator’s decision acknowledgement indicates whether scaling is still in progress.

#### get_model_name

Get the model name from the deployment

#### get_gpu_counts

Virtual deployments do not expose GPU shape through the coordinator.

###### WorkerCapabilities (class)


Static per-engine capabilities discovered at startup from MDC.

Provided once when constructing the planner core. In native mode
these come from `WorkerInfo`

(resolved via MDC / DGD); in replay
they come from the simulated engine args.

For agg mode, only `decode`

is populated (single engine type).

`components/src/dynamo/planner/core/types.py#L210`


**Public methods**

**init**

No summary available.

###### WorkerCounts (class)


Current worker inventory as reported by the adapter.

`components/src/dynamo/planner/core/types.py#L62`


**Public methods**

**init**

No summary available.

###### WorkerInfo (class)


Consolidated worker metadata for the planner.

Populated from MDC (DynamoWorkerMetadata CRs) in Kubernetes mode, with fallback to DGD container-arg parsing, then hard-coded defaults.

`components/src/dynamo/planner/monitoring/worker_info.py#L26`


**Public methods**

#### summary

No summary available.

**init**

No summary available.