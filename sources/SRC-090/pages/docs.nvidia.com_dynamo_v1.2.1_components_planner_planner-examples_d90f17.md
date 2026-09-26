source: https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-examples
lastmod: 2026-09-24T19:58:16.636Z

# Planner Examples

Practical examples for deploying the Planner with throughput-based scaling. The DGDR workflow can use native AIC estimates, optional bootstrap profiling data, or live FPM warmup depending on the model/backend combination. For deployment concepts, see the [Planner Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-guide). For a quick overview, see the [Planner README](https://docs.nvidia.com/dynamo/v1.2.1/components/planner).

## Basic Examples

### Minimal DGDR with AIC (Fastest)

The simplest way to deploy with the Planner. Uses AI Configurator for offline profiling (20-30 seconds instead of hours):

Deploy:

### Online Profiling (Real Measurements)

Standard online profiling runs real GPU measurements for more accurate results. Takes 2-4 hours:

Deploy:


Note: Starting with Dynamo 1.0.0 (DGDR API version v1beta1), DGDR fields use structured spec fields (e.g.,`spec.workload`

,`spec.sla`

,`spec.hardware`

) instead of the nested`profilingConfig.config`

blob used in v1alpha1.

## Kubernetes Examples

### MoE Models (SGLang)

For Mixture-of-Experts models like DeepSeek-R1, use SGLang backend:

Deploy:

### Using Existing DGD Configs (Custom Setups)

Reference an existing DynamoGraphDeployment config via ConfigMap:

**Step 1: Create ConfigMap from your DGD config:**

**Step 2: Reference it in your DGDR:**

The profiler uses the DGD config from the ConfigMap as a **base template**, then optimizes it based on your SLA targets. The controller automatically injects `spec.model`

and `spec.backend`

into the final configuration.

### Inline Configuration (Simple Use Cases)

For simple use cases without a custom DGD config, provide the configuration directly in the v1beta1 DGDR spec fields. The profiler auto-generates a basic DGD configuration:

### Simulation with Mocker

Deploy a mocker backend that simulates GPU timing behavior without real GPUs. Useful for:

- Large-scale experiments without GPU resources
- Testing planner behavior and infrastructure
- Validating deployment configurations

Profiling runs against the real backend (via GPUs or AIC). The mocker deployment then uses profiling data to simulate realistic timing.

### Model Cache PVC (0.8.1+)

For large models, use a pre-populated PVC instead of downloading from HuggingFace:

See [SLA-Driven Profiling](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-guide) for configuration details.

## Advanced Examples

### Custom Load Predictors

#### Warm-starting with Trace Data

Pre-load predictors with historical request patterns before live traffic:

The trace file should be in mooncake-style JSONL format with request-count, ISL, and OSL samples.

#### Kalman Filter Tuning

For workloads with rapid changes, tune the Kalman filter:

#### Prophet for Seasonal Workloads

For workloads with daily/weekly patterns:

### Virtual Connector

For non-Kubernetes environments, use the VirtualConnector to communicate scaling decisions:

See `components/planner/test/test_virtual_connector.py`

for a full working example.

### Planner Configuration Passthrough

Pass planner-specific settings through the DGDR:

### Review Before Deploy (autoApply: false)

Disable auto-deployment to inspect the generated DGD:

After profiling completes:

### Profiling Artifacts with PVC

Save detailed profiling artifacts (plots, logs, raw data) to a PVC:

Setup:

Access results:

## Related Documentation

[Planner README](https://docs.nvidia.com/dynamo/v1.2.1/components/planner)— Overview and quick start[Planner Guide](https://docs.nvidia.com/dynamo/v1.2.1/components/planner/planner-guide)— Deployment, configuration, integration[Planner Design](https://docs.nvidia.com/dynamo/v1.2.1/design-docs/component-design/planner-design)— Architecture deep-dive[DGDR Configuration Reference](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-guide#dgdr-configuration-structure)[SLA-Driven Profiling](https://docs.nvidia.com/dynamo/v1.2.1/components/profiler/profiler-guide)