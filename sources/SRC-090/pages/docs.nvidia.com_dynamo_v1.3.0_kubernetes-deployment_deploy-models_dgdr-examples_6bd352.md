source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-examples
lastmod: 2026-09-24T19:58:16.636Z

# DGDR Examples

Practical DynamoGraphDeploymentRequest examples covering AIC estimates, online profiling, and SLA-driven generation.

Practical examples for deploying with `DynamoGraphDeploymentRequest`

(DGDR).
The DGDR workflow can use native AIC estimates, optional bootstrap profiling
data, or live FPM warmup depending on the model/backend combination. For DGDR
concepts, see the [DGDR Reference](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference). For profiling concepts, see the
[Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide).

## DGDR Examples

### Minimal DGDR with AIC (Fastest)

The simplest way to generate a deployment from native AIC estimates. Uses AI Configurator for offline profiling (20-30 seconds instead of hours):

Deploy:

### Online Profiling (Real Measurements)

Standard online profiling runs real GPU measurements for more accurate results. Takes 2-4 hours:

Deploy:


Note: Starting with Dynamo 1.0.0 (DGDR API version v1beta1), DGDR fields use structured spec fields (e.g.,`spec.workload`

,`spec.sla`

,`spec.hardware`

) instead of the nested`profilingConfig.config`

blob used in v1alpha1.

### Planner-Enabled DGDR

Set `spec.features.planner`

to enable Planner generation in the final DGD. DGDR
passes this object as PlannerConfig to the Planner service; see the
[Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide#plannerconfig-reference)
for available fields.

`spec.overrides.dgd`

is not required to enable Planner; use it only when the
generated DGD needs additional customization.

## Additional DGDR Patterns

### MoE Models (SGLang)

For Mixture-of-Experts models like DeepSeek-R1, use SGLang backend:

Deploy:

### Customizing the Generated DGD

Use `spec.overrides.dgd`

to provide a partial `DynamoGraphDeployment`

that is
merged into the profiler-generated deployment. Use a `v1beta1`

override for
new DGDRs:

DGDR merges the override into the generated DGD after profiling selects a
configuration. Both `.status.profilingResults.selectedConfig`

and the DGD
created when `autoApply: true`

use `nvidia.com/v1beta1`

.

Existing `v1alpha1`

overrides remain supported. Their field shape follows the
`v1alpha1`

DGD schema:

The override’s API version controls its merge semantics. In particular, the
`v1beta1`

graph-level `spec.env`

list and container `args`

replace their
generated lists, while nested container environment variables merge by name.
`v1alpha1`

worker arguments append for compatibility. See
[Generated DGD Overrides](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference#generated-dgd-overrides) for the complete
behavior and direct-profiler requirements.

### Inline Configuration (Simple Use Cases)

For simple use cases without a custom DGD config, provide the configuration directly in the v1beta1 DGDR spec fields. The profiler auto-generates a basic DGD configuration:

### Simulation with Mocker

Deploy a mocker backend that simulates GPU timing behavior without real GPUs. Useful for:

- Large-scale experiments without GPU resources
- Testing profiling behavior and infrastructure
- Validating deployment configurations

Profiling runs against the real backend (via GPUs or AIC). The mocker deployment then uses profiling data to simulate realistic timing.

### Model Cache PVC (0.8.1+)

For large models, use a pre-populated PVC instead of downloading from HuggingFace:

See [SLA-Driven Profiling](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide) for configuration details.

## Advanced DGDR Patterns

### Review Before Deploy (autoApply: false)

Disable auto-deployment to inspect the generated DGD:

After profiling completes:

### Profiling Artifacts with PVC

Save detailed profiling artifacts (plots, logs, raw data) to a PVC:

Setup:

Access results:

## Related Documentation

[DGDR Reference](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference)— DGDR field reference and lifecycle[Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide)— Profiling workflow