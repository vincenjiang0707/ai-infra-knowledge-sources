source: https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-examples
lastmod: 2026-09-24T19:58:16.636Z

# Profiler Examples

Complete examples for profiling with DGDRs.

## DGDR Examples

### Dense Model: Rapid

Fast profiling (~30 seconds):

### Dense Model: Thorough

Profiling with real GPU measurements:

### MoE Model

Multi-node MoE profiling with SGLang:

The PVC referenced by `modelCache.pvcName`

must already exist in the same namespace and contain
the model weights at the specified `pvcModelPath`

. The DGDR controller does not create or
populate the PVC — it only mounts it into the profiling job and deployed workers.

### Private Model

For gated or private HuggingFace models, pass your token via an environment variable injected into the profiling job. Create the secret first:

Then reference it in your DGDR:

### Custom SLA Targets

Control how the profiler optimizes your deployment by specifying latency targets and workload characteristics.

**Explicit TTFT + ITL targets** (default mode):

**End-to-end latency target** (alternative to ttft+itl):

### Overrides

Use `overrides`

to customize the profiling job pod spec — for example to add tolerations for
GPU node taints or inject environment variables.

**GPU node toleration** (common on GKE and shared clusters):

**Override the generated DynamoGraphDeployment** (e.g., to inject worker environment variables):

## SGLang Runtime Profiling

Profile SGLang workers at runtime via HTTP endpoints:

A test script is provided at `examples/backends/sglang/test_sglang_profile.py`

:

View traces using Chrome’s `chrome://tracing`

, [Perfetto UI](https://ui.perfetto.dev/), or TensorBoard.