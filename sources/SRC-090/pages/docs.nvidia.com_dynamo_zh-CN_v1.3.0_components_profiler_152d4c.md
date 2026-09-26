source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/components/profiler
lastmod: 2026-09-23T23:30:39.914Z

# Profiler

Automated performance analysis that finds optimal prefill and decode parallelism and generates SLA-driven deployment configurations.

The Dynamo Profiler is an automated performance analysis tool that measures model inference characteristics to optimize deployment configurations. It determines optimal tensor parallelism (TP) settings for prefill and decode phases, generates performance interpolation data, and enables SLA-driven autoscaling through the Planner.

## Feature Matrix

## Quick Start

### Prerequisites

- Dynamo platform installed (see
[Installation Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide)) - Kubernetes cluster with GPU nodes (for DGDR-based profiling)
- kube-prometheus-stack installed (required for SLA planner)

### Using DynamoGraphDeploymentRequest (Recommended)

The recommended way to profile models is through DGDRs, which automate the entire profiling and deployment workflow.

### Using AI Configurator (Fast Offline Profiling)

AI Configurator enables rapid offline profiling (~30 seconds) and supports all backends (vLLM, SGLang, TensorRT-LLM). Since `searchStrategy: rapid`

is the default, AIC is used automatically unless you explicitly set `searchStrategy: thorough`

.

## Configuration

## Profiling Methods

## Output

The profiler generates:

**Optimal Configuration**: Recommended TP sizes for prefill and decode engines**Performance Data**: Interpolation models for the SLA Planner**Generated DGD**: Complete deployment manifest with optimized settings

Example recommendations: