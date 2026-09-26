source: https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-examples
lastmod: 2026-09-24T19:58:16.636Z

# Planner Examples

Examples for custom load predictors and the VirtualConnector for non-Kubernetes scaling environments.

Planner-specific examples for advanced configuration and non-Kubernetes
integrations. For DGDR manifests, see
[DGDR Examples](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-examples). For the full configuration
reference, see the [Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide).

## Custom Load Predictors

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

[Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide)— Planner configuration reference[DGDR Examples](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-examples)— DGDR YAML examples[Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide)— Profiling workflow