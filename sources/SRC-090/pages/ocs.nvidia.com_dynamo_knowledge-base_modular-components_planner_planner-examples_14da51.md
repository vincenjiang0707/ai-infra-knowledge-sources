source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-examples
lastmod: 2026-09-24T19:58:16.636Z

# Planner Examples

Examples for custom load predictors and the VirtualConnector for non-Kubernetes scaling environments.

Planner-specific examples for advanced configuration and non-Kubernetes
integrations. For DGDR manifests, see
[DGDR Templates](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgdr). For the full configuration
reference, see the [Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide).

## Custom Load Predictors

Each YAML block in this section is a standalone `PlannerConfig`

. Save the block
as `planner.yaml`

and pass it to
`python -m dynamo.planner --config planner.yaml`

. To use the same fields in a
DGDR, nest them under `spec.features.planner`

.

### Warm-starting with Trace Data

Pre-load predictors with historical request patterns before live traffic:

The trace file should be in mooncake-style JSONL format with request-count, ISL, and OSL samples.

### Kalman Filter Tuning

For workloads with rapid changes, tune the Kalman filter:

### Prophet for Seasonal Workloads

For workloads with daily/weekly patterns:

## Virtual Connector

For non-Kubernetes environments, use the VirtualConnector to communicate scaling decisions:

See `components/planner/test/test_virtual_connector.py`

for a full working
example.

## Related Documentation

[Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide)— Planner configuration reference[DGDR Templates](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgdr)— DGDR YAML examples[Profiler Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/profiler/profiler-guide)— Profiling workflow