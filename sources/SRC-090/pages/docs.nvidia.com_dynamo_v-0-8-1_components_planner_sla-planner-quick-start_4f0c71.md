source: https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-planner-quick-start
lastmod: 2026-09-24T19:58:16.636Z

SLA-Driven Profiling and Planner Deployment Quick Start Guide


SLA-Driven Profiling and Planner Deployment Quick Start Guide

Complete workflow to deploy SLA-optimized Dynamo models using DynamoGraphDeploymentRequests (DGDR). This guide shows how to automatically profile models and deploy them with optimal configurations that meet your Service Level Agreements (SLAs).

**Prerequisites**: This guide assumes you have a Kubernetes cluster with GPU nodes and have completed the [Dynamo Platform installation](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/detailed-installation-guide).

## Overview

The DGDR workflow automates the entire process from SLA specification to deployment:

**Define SLAs**: Specify performance requirements (TTFT, ITL) and model information in a DGDR Custom Resource**Automatic Profiling**: The Dynamo Operator automatically profiles your model to find optimal configurations**Auto-Deploy**: The system automatically deploys the optimal configuration that meets your SLAs

## What is a DynamoGraphDeploymentRequest (DGDR)?

A **DynamoGraphDeploymentRequest (DGDR)** is a Kubernetes Custom Resource that serves as the primary interface for users to request model deployments with specific performance and resource constraints. Think of it as a “deployment order” where you specify:

**What**model you want to deploy (`model`

)**How**it should perform (SLA targets:`ttft`

,`itl`

)**Where**it should run (optional GPU preferences)**Which**backend to use (`backend`

: vllm, sglang, or trtllm)**Which**images to use (`profilingConfig.profilerImage`

,`deploymentOverrides.workersImage`

)

The Dynamo Operator watches for DGDRs and automatically:

- Discovers available GPU resources in your cluster
- Runs profiling (online or offline) to find optimal configurations
- Generates an optimized DynamoGraphDeployment (DGD) configuration
- Deploys the DGD to your cluster

**Key Benefits:**

**Declarative**: Specify what you want, not how to achieve it**Automated**: No manual profiling job setup or result processing**SLA-Driven**: Ensures deployments meet your performance requirements**Integrated**: Works seamlessly with the Dynamo Operator

## Prerequisites

Before creating a DGDR, ensure:

**Dynamo platform installed**with the operator running (see[Installation Guide](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/detailed-installation-guide))(required for SLA planner)[kube-prometheus-stack](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/observability-k-8-s/metrics)installed and running**Image pull secrets configured**if using private registries (typically`nvcr-imagepullsecret`

for NVIDIA images)**Sufficient GPU resources**available in your cluster for profiling**Runtime images available**that contain both profiler and runtime components

### Container Images

Each DGDR requires you to specify container images for the profiling and deployment process:

**profilingConfig.profilerImage** (Required):
Specifies the container image used for the profiling job itself. This image must contain the profiler code and dependencies needed for SLA-based profiling.

**deploymentOverrides.workersImage** (Optional):
Specifies the container image used for DynamoGraphDeployment worker components (frontend, workers, planner). This image is used for:

- Temporary DGDs created during online profiling (for performance measurements)
- The final DGD deployed after profiling completes

If `workersImage`

is omitted, the image from the base config file (e.g., `disagg.yaml`

) is used. You may use our public images (0.6.1 and later) or build and push your own.

## Quick Start: Deploy with DGDR

### Step 1: Create Your DGDR

Dynamo provides sample DGDR configurations in `benchmarks/profiler/deploy/`

. You can use these as starting points:

**Available Sample DGDRs:**

: Standard online profiling for dense models`profile_sla_dgdr.yaml`

: Fast offline profiling using AI Configurator`profile_sla_aic_dgdr.yaml`

: Online profiling for MoE models (SGLang)`profile_sla_moe_dgdr.yaml`


Or, you can create your own DGDR for your own needs.


Important - Profiling Config Cases: Prior to 0.8.1, any fields under`profilingConfig.config`

are represented in snake_case. Starting 0.8.1, fields under`profilingConfig.config`

are represented in camelCase for uniformity. There is backwards compatibility to snake_case, but as all example DGDRs are using camelCase, anyone using a release prior to 0.8.1 must manually update the configs under the examples to have snake_case config fields.

For detailed explanations of all configuration options (SLA, hardware, sweep, AIC, planner), see the [DGDR Configuration Reference](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#dgdr-configuration-reference).

### Step 2: Apply the DGDR

The rest of this quickstart will use the DGDR sample that uses AIC profiling. If you use a different DGDR file and/or name, be sure to adjust the commands accordingly.

The Dynamo Operator will immediately begin processing your request.

### Step 3: Monitor Progress

Watch the DGDR status:

**DGDR Status States:**

`Pending`

: Initial state, preparing to profile`Profiling`

: Running profiling job (20-30 seconds for AIC, 2-4 hours for online)`Deploying`

: Generating and applying DGD configuration`Ready`

: DGD successfully deployed and running`Failed`

: Error occurred (check events for details)

With AI Configurator, profiling completes in **20-30 seconds**! This is much faster than online profiling which takes 2-4 hours.

### Step 4: Access Your Deployment

Once the DGDR reaches `Ready`

state, your model is deployed and ready to serve:

### Step 5 (Optional): Access the Planner Grafana Dashboard

If you want to monitor the SLA Planner’s decision-making in real-time, you can deploy the Planner Grafana dashboard.

Follow the instructions in [Dynamo Metrics Collection on Kubernetes](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/observability-k-8-s/metrics) to access the Grafana UI and select the **Dynamo Planner Dashboard**.

The dashboard displays:

**Worker Counts & GPU Usage**: Current prefill/decode worker counts and cumulative GPU hours**Observed Metrics**: Real-time TTFT, ITL, request rate, and sequence lengths from Prometheus**Predicted Metrics**: Planner’s load predictions and recommended replica counts**Correction Factors**: How the planner adjusts predictions based on observed vs expected performance

Use the **Namespace** dropdown at the top of the dashboard to filter metrics for your specific deployment namespace.

## DGDR Configuration Details

### Required Fields

### Optional Fields

### SLA Configuration

The `sla`

section defines performance requirements and workload characteristics:

**Choosing SLA Values:**

**ISL/OSL**: Based on your expected traffic patterns**TTFT**: First token latency target (lower = more GPUs needed)**ITL**: Token generation latency target (lower = more GPUs needed)**Trade-offs**: Tighter SLAs require more GPU resources

### Profiling Methods

Choose between **online profiling** (real measurements, 2-4 hours) or **offline profiling** with AI Configurator (estimated, 20-30 seconds):

For detailed comparison, supported configurations, and limitations, see [SLA-Driven Profiling Documentation](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#profiling-methods).

### Hardware Configuration

For details on hardware configuration and GPU discovery options, see [Hardware Configuration in SLA-Driven Profiling](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#hardware-configuration).

### Advanced Configuration

#### Using Existing DGD Configs (Recommended for Custom Setups)

If you have an existing DynamoGraphDeployment config (e.g., from `examples/backends/*/deploy/disagg.yaml`

or custom recipes), you can reference it via ConfigMap:

**Step 1: Create ConfigMap from your DGD config file:**

**Step 2: Reference the ConfigMap in your DGDR:**


What’s happening: The profiler uses the DGD config from the ConfigMap as abase template, then optimizes it based on your SLA targets. The controller automatically injects`spec.model`

into`deployment.model`

and`spec.backend`

into`engine.backend`

in the final configuration.

#### Inline Configuration (Simple Use Cases)

For simple use cases without a custom DGD config, provide profiler configuration directly. The profiler will auto-generate a basic DGD configuration from your `model`

and `backend`

:


Note:`engine.config`

is afile pathto a DGD YAML file, not inline configuration. Use ConfigMapRef (recommended) or leave it unset to auto-generate.

#### Planner Configuration Passthrough

Add planner-specific settings:

## Understanding Profiling Results

For details about the profiling process, performance plots, and interpolation data, see [SLA-Driven Profiling Documentation](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#profiling-process-details).

## Advanced Topics

### Mocker Deployment

Instead of a real DGD that uses GPU resources, you can deploy a mocker deployment that uses simulated engines rather than GPUs. Mocker is available in all backend images and uses profiling data to simulate realistic GPU timing behavior. It is useful for:

- Large-scale experiments without GPU resources
- Testing Planner behavior and infrastructure
- Validating deployment configurations

To deploy mocker instead of the real backend, set `useMocker: true`

:

Profiling still runs against the real backend (via GPUs or AIC) to collect performance data. The mocker deployment then uses this data to simulate realistic timing behavior.

### Using a Model Cache PVC (0.8.1 or later)

Starting in Dynamo 0.8.1, for large models, you can use a pre-populated PVC containing model weights instead of downloading from HuggingFace. See [Model Cache PVC](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#model-cache-pvc-advanced) for configuration details.

### DGDR Immutability

DGDRs are **immutable** - if you need to update SLAs or configuration:

- Delete the existing DGDR:
`kubectl delete dgdr sla-aic`

- Create a new DGDR with updated specifications

### Manual Deployment Control

There are two ways to manually control deployment after profiling:

#### Option 1: Use DGDR-Generated Configuration (Recommended)

Disable auto-deployment to review the generated DGD before applying:

Then manually extract and apply the generated DGD:

The generated DGD includes optimized configurations and the SLA planner component. The required `planner-profile-data`

ConfigMap is automatically created when profiling completes, so the DGD will deploy successfully.

#### Option 2: Use Standalone Planner Templates (Advanced)

For advanced use cases, you can manually deploy using the standalone planner templates in `examples/backends/*/deploy/disagg_planner.yaml`

:


Note: The standalone templates are provided as examples and may need customization for your model and requirements. The DGDR-generated configuration (Option 1) is recommended as it’s automatically tuned to your profiling results and SLA targets.

Important - Prometheus Configuration: The planner queries Prometheus to get frontend request metrics for scaling decisions. If you see errors like “Failed to resolve prometheus service”, ensure the`PROMETHEUS_ENDPOINT`

environment variable in your planner configuration correctly points to your Prometheus service. See the comments in the example templates for details.

### Relationship to DynamoGraphDeployment (DGD)

**DGDR**: High-level “intent” - what you want deployed**DGD**: Low-level “implementation” - how it’s deployed

The DGDR controller generates a DGD that:

- Uses optimal TP configurations from profiling
- Includes SLA planner for autoscaling
- Has deployment and engine settings tuned for your SLAs

The generated DGD is tracked via labels:

### Accessing Detailed Profiling Artifacts

By default, profiling jobs save essential data to ConfigMaps for planner integration. For advanced users who need access to detailed artifacts (logs, performance plots, AIPerf results, etc), configure the DGDR to use `dynamo-pvc`

. This is optional and will not affect the functionality of profiler or Planner.

**What’s available in ConfigMaps (always created):**

- Generated DGD configuration
- Profiling data for Planner (
`.json`

files)

**What’s available in PVC if attached to DGDR (optional):**

- Performance plots (PNGs)
- DGD configuration and logs of all services for each profiled deployment
- AIPerf profiling artifacts for each AIPerf run
- Raw profiling data (
`.npz`

files) - Profiler log

**Setup:**

- Set up the benchmarking PVC:

- Add
`outputPVC`

to your DGDR’s`profilingConfig`

:

- After profiling completes, access results:

## Troubleshooting

### Quick Diagnostics

### Common Issues

For comprehensive troubleshooting including AI Configurator constraints, performance debugging, and backend-specific issues, see [SLA-Driven Profiling Troubleshooting](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#troubleshooting).

## Configuration Reference

For comprehensive documentation of all DGDR configuration options, see the [DGDR Configuration Reference](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-driven-profiling#dgdr-configuration-reference).

This includes detailed explanations of:

**SLA Configuration**: ISL, OSL, TTFT, ITL with use cases and trade-offs**Hardware Configuration**: GPU constraints and search space control**Sweep Configuration**: Profiling behavior and interpolation settings**AI Configurator Configuration**: System types, model mappings, backend versions**Planner Configuration**: Autoscaling and adjustment parameters**Complete Examples**: Full DGDRs for online, offline (AIC), and MoE profiling