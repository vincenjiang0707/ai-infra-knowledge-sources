source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/design-docs/planner-design
lastmod: 2026-09-23T23:30:39.914Z

# Planner Design


Tier 3 design documentationfor contributors and architects. For user-facing docs, see[docs/components/planner/].

## Overview

The Planner is Dynamo’s autoscaling controller. It observes system metrics, predicts future load, and adjusts prefill/decode worker replica counts to proactively meet SLA targets. This document covers the internal architecture, algorithms, and design trade-offs.

## Architecture


## Scaling Algorithm

### Step 1: Metric Collection

Every `adjustment_interval`

seconds, the planner queries Prometheus for:

- Average TTFT and ITL over the interval
- Total request count
- Average input sequence length (ISL) and output sequence length (OSL)

The Prometheus query targets the Frontend’s `/metrics`

endpoint, which exposes histograms and counters.

### Step 2: Correction Factor Calculation

The planner maintains correction factors that adapt profiling-based predictions to real-world behavior:

These factors account for hard to model factors such as:

**Request queueing**: Bursty traffic causes higher TTFT than profiled steady-state**Prefix cache hits**: KV reuse reduces effective prefill tokens, lowering actual TTFT**Chunked prefill in decode**: Small prefills processed in decode engine affect ITL**Metric variance**: Average ISL/OSL may not represent the actual distribution

The correction factors are applied as multipliers to the next scaling decision. Setting `--no-correction`

disables this for debugging or when cold-start artifacts dominate.

### Step 3: Load Prediction

The planner forecasts three values for the next interval:

`next_num_req`

: Number of requests`next_isl`

: Average input sequence length`next_osl`

: Average output sequence length

Four predictor implementations are available:

All predictors support warm-starting from trace files (`--load-predictor-warmup-trace`

).

### Step 4: Replica Calculation

**Prefill replicas:**

The prefill correction factor has a linear effect on throughput because prefill is single-batched.

**Decode replicas:**

### Step 5: Scaling Execution

The planner calls `connector.set_component_replicas()`

with the calculated targets. Scaling is non-blocking by default: the planner continues monitoring while replicas are adjusting.

## Connector Design

### Interface

### KubernetesConnector

Directly PATCHes the DGD resource to update replica counts. The operator watches for DGD changes and reconciles component deployments.

**Design decisions:**

- Uses
`DYN_PARENT_DGD_K8S_NAME`

to find its parent DGD (injected by operator) - Resolves services by
`subComponentType`

field (prefill/decode), with fallback to legacy component names - Validates deployment structure on startup: checks that prefill and decode services exist and model names match

### VirtualConnector

For non-native environments (e.g., custom orchestrators). Writes scaling decisions to the distributed runtime via `VirtualConnectorCoordinator`

(Rust binding). External systems use `VirtualConnectorClient`

to poll decisions and report completion.

**Scaling decision flow:**

- Planner writes
`(num_prefill, num_decode, decision_id)`

to runtime - External system reads decision via
`client.wait()`

- External system executes scaling
- External system reports completion via
`client.complete(decision)`

- Planner sees
`scaled_decision_id >= decision_id`

and proceeds

**Timeout**: If scaling isn’t acknowledged within 1800s (configurable), the planner proceeds with new decisions anyway.

## Performance Interpolation

The planner uses pre-deployment profiling data (NPZ files) to map (throughput, ISL/OSL, context_length) -> (TTFT, ITL). This data comes from the SLA-driven profiling process (either online GPU profiling or AI Configurator estimation).

Two interpolators are maintained:

**Prefill interpolator**: Maps (throughput_per_gpu, ISL) -> TTFT**Decode interpolator**: Maps (throughput_per_gpu, context_length) -> ITL

The interpolators use the profiling sweep granularity to determine precision. Finer granularity means more profiling samples but more accurate interpolation.

## Initialization

The planner starts with a 30-second delay (`INIT_PLANNER_START_DELAY`

) to allow other components (frontend, workers) to register and stabilize. This is a known workaround (marked TODO in code) that should be replaced with a proper readiness check.

After the delay:

- Initialize the connector (K8s or Virtual based on
`--environment`

) - Validate deployment structure
- Load profiling results
- Build interpolators
- Initialize load predictor
- Enter main scaling loop

## Performance Considerations

**Adjustment interval sizing**: The interval must be long enough for scaling operations to complete. If`adjustment_interval`

is shorter than the time to add/remove a worker (which includes pod scheduling, model loading, and registration), scaling decisions will overlap. Default of 180s is conservative; workloads with fast model loading can use shorter intervals.**Correction factor stability**: Correction factors are recalculated each interval. During traffic transitions (e.g., ramp-up), they can oscillate. The`--no-correction`

flag disables correction for scenarios where cold-start artifacts dominate and distort the factor.**Interpolation accuracy vs profiling cost**: Higher`prefillInterpolationGranularity`

and`decodeInterpolationGranularity`

in the profiling sweep produce more accurate interpolation but increase profiling time linearly. Default granularity (16 prefill, 6 decode) balances accuracy with profiling duration.**Predictor warm-up period**: All predictors need observation history before making reliable forecasts. ARIMA and Prophet need multiple adjustment intervals of data. Kalman starts forecasting after`--kalman-min-points`

observations. During warm-up, the planner uses the constant predictor as fallback.

## Known Limitations

**30-second startup delay**: Hardcoded wait for component registration. It should be replaced with runtime readiness probing.**Adjustment interval vs scaling latency**: If`adjustment_interval`

< time to scale, scaling decisions can pile up. The planner logs warnings but doesn’t queue.**Average-based interpolation**: The planner uses average ISL/OSL, which may not represent bimodal or heavy-tailed distributions well.**Single DGD scope**: Each planner instance manages exactly one DGD. Multi-model/multi-DGD coordination is not supported.**Load-based planner deprecated**: The load-based code path exists but is non-functional with current backends (no prefill queue metrics).

## Future Work

- Support aggregated (non-disaggregated) scaling mode for single-worker deployments
- Multi-DGD coordination for shared-cluster scenarios
- Distribution-aware interpolation (beyond mean ISL/OSL)
- Adaptive adjustment interval based on observed scaling latency