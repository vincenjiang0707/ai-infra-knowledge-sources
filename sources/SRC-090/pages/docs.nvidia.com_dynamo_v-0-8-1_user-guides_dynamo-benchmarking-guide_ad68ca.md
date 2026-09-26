source: https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/dynamo-benchmarking-guide
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Benchmarking Guide

This benchmarking framework lets you compare performance across any combination of:

**DynamoGraphDeployments****External HTTP endpoints**(existing services deployed following standard documentation from vLLM, llm-d, AIBrix, etc.)

## Choosing Your Benchmarking Approach

Dynamo provides two benchmarking approaches to suit different use cases: **client-side** and **server-side**. Client-side refers to running benchmarks on your local machine and connecting to Kubernetes deployments via port-forwarding, while server-side refers to running benchmarks directly within the Kubernetes cluster using internal service URLs. Which method to use depends on your use case.

**TLDR:**
Need high performance/load testing? Server-side.
Just quick testing/comparison? Client-side.

### Use Client-Side Benchmarking When:

- You want to quickly test deployments
- You want immediate access to results on your local machine
- You’re comparing external services or deployments (not necessarily just Dynamo deployments)
- You need to run benchmarks from your laptop/workstation

→ [Go to Client-Side Benchmarking (Local)](https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/dynamo-benchmarking-guide#client-side-benchmarking-local)

### Use Server-Side Benchmarking When:

- You have a development environment with kubectl access
- You’re doing performance validation with high load/speed requirements
- You’re experiencing timeouts or performance issues with client-side benchmarking
- You want optimal network performance (no port-forwarding overhead)
- You’re running automated CI/CD pipelines
- You need isolated execution environments
- You’re doing resource-intensive benchmarking
- You want persistent result storage in the cluster

→ [Go to Server-Side Benchmarking (In-Cluster)](https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/dynamo-benchmarking-guide#server-side-benchmarking-in-cluster)

### Quick Comparison

## What This Tool Does

The framework is a Python-based wrapper around `aiperf`

that:

- Benchmarks any HTTP endpoints
- Runs concurrency sweeps across configurable load levels
- Generates comparison plots with your custom labels
- Works with any HuggingFace-compatible model on NVIDIA GPUs (H200, H100, A100, etc.)
- Provides direct Python script execution for maximum flexibility

**Default sequence lengths**: Input: 2000 tokens, Output: 256 tokens (configurable with `--isl`

and `--osl`

)

**Important**: The `--model`

parameter configures AIPerf for benchmarking and provides logging context. The default `--model`

value in the benchmarking script is `Qwen/Qwen3-0.6B`

, but it must match the model deployed at the endpoint(s).

## Client-Side Benchmarking (Local)

Client-side benchmarking runs on your local machine and connects to Kubernetes deployments via port-forwarding.

## Prerequisites

-
**Dynamo container environment**- You must be running inside a Dynamo container with the benchmarking tools pre-installed. -
**HTTP endpoints**- Ensure you have HTTP endpoints available for benchmarking. These can be:- DynamoGraphDeployments exposed via HTTP endpoints
- External services (vLLM, llm-d, AIBrix, etc.)
- Any HTTP endpoint serving HuggingFace-compatible models

-
**Benchmark dependencies**- Since benchmarks run locally, you need to install the required Python dependencies. Install them using:

## User Workflow

Follow these steps to benchmark Dynamo deployments using client-side benchmarking:

### Step 1: Establish Kubernetes Cluster and Install Dynamo

Set up your Kubernetes cluster with NVIDIA GPUs and install the Dynamo Cloud platform. First follow the [installation guide](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/detailed-installation-guide) to install Dynamo Cloud, then use [deploy/utils/README](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/utils/README.md) to set up benchmarking resources.

### Step 2: Deploy DynamoGraphDeployments

Deploy your DynamoGraphDeployments separately using the [deployment documentation](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/examples/backends/). Each deployment should have a frontend service exposed.

### Step 3: Port-Forward and Benchmark Deployment A

### Step 4: [If Comparative] Teardown Deployment A and Establish Deployment B

If comparing multiple deployments, teardown deployment A and deploy deployment B with a different configuration.

### Step 5: [If Comparative] Port-Forward and Benchmark Deployment B

### Step 6: Generate Summary and Visualization

## Use Cases

The benchmarking framework supports various comparative analysis scenarios:

**Compare multiple DynamoGraphDeployments of a single backend**(e.g., aggregated vs disaggregated configurations)**Compare different backends**(e.g., vLLM vs TensorRT-LLM vs SGLang)**Compare Dynamo vs other platforms**(e.g., Dynamo vs llm-d vs AIBrix)**Compare different models**(e.g., Llama-3-8B vs Llama-3-70B vs Qwen-3-0.6B)**Compare different hardware configurations**(e.g., H100 vs A100 vs H200)**Compare different parallelization strategies**(e.g., different GPU counts or memory configurations)

## Configuration and Usage

### Command Line Options

### Important Notes

**Benchmark Name**: The benchmark name becomes the label in plots and results**Name Restrictions**: Names can only contain letters, numbers, hyphens, and underscores. The name`plots`

is reserved.**Port-Forwarding**: You must have an exposed endpoint before benchmarking**Model Parameter**: The`--model`

parameter configures AIPerf for testing and logging, and must match the model deployed at the endpoint**Sequential Benchmarking**: For comparative benchmarks, deploy and benchmark each configuration separately

### What Happens During Benchmarking

The Python benchmarking module:

**Connects**to your port-forwarded endpoint**Benchmarks**using AIPerf at various concurrency levels (default: 1, 2, 5, 10, 50, 100, 250)**Measures**key metrics: latency, throughput, time-to-first-token**Saves**results to an output directory organized by benchmark name

The Python plotting module:

**Generates**comparison plots using your benchmark name in`<OUTPUT_DIR>/plots/`

**Creates**summary statistics and visualizations

### Plotting Options

The plotting script supports several options for customizing which experiments to visualize:

**Available Options:**

`--data-dir`

: Directory containing benchmark results (required)`--benchmark-name`

: Specific benchmark experiment name to plot (can be specified multiple times). Names must match subdirectory names under the data dir.`--output-dir`

: Custom output directory for plots (defaults to data-dir/plots)

**Note**: If `--benchmark-name`

is not specified, the script will plot all subdirectories found in the data directory.

### Using Your Own Models and Configuration

The benchmarking framework supports any HuggingFace-compatible LLM model. Specify your model in the benchmark script’s `--model`

parameter. It must match the model name of the deployment. You can override the default sequence lengths (2000/256 tokens) with `--isl`

and `--osl`

flags if needed for your specific workload.

The benchmarking framework is built around Python modules that provide direct control over the benchmark workflow. The Python benchmarking module connects to your existing endpoints, runs the benchmarks, and can generate plots. Deployment is user-managed and out of scope for this tool.

### Comparison Limitations

The plotting system supports up to 12 different benchmarks in a single comparison.

### Concurrency Configuration

You can customize the concurrency levels using the CONCURRENCIES environment variable:

## Understanding Your Results

After benchmarking completes, check `./benchmarks/results/`

(or your custom output directory):

### Plot Labels and Organization

The plotting script uses the `--benchmark-name`

as the experiment name in all generated plots. For example:

`--benchmark-name aggregated`

→ plots will show “aggregated” as the label`--benchmark-name vllm-disagg`

→ plots will show “vllm-disagg” as the label

This allows you to easily identify and compare different configurations in the visualization plots.

### Summary and Plots

### Data Files

Raw data is organized by deployment/benchmark type and concurrency level:

**For Any Benchmarking (uses your custom benchmark name):**

**Example with actual benchmark names:**

Each concurrency directory contains:

- Structured metrics from AIPerf`profile_export_aiperf.json`

- CSV format metrics from AIPerf`profile_export_aiperf.csv`

- Raw AIPerf results`profile_export.json`

- Generated test inputs`inputs.json`


# Server-Side Benchmarking (In-Cluster)

Server-side benchmarking runs directly within the Kubernetes cluster, eliminating the need for port forwarding and providing better resource utilization.

## What Server-Side Benchmarking Does

The server-side benchmarking solution:

- Runs benchmarks directly within the Kubernetes cluster using internal service URLs
- Uses Kubernetes service DNS for direct communication (no port forwarding required)
- Leverages the existing benchmarking infrastructure (
`benchmarks.utils.benchmark`

) - Stores results persistently using
`dynamo-pvc`

- Provides isolated execution environment with configurable resources
- Handles high load/speed requirements without timeout issues
**Note**: Each benchmark job runs within a single Kubernetes namespace, but can benchmark services across multiple namespaces using the full DNS format`svc_name.namespace.svc.cluster.local`


## Prerequisites

**Kubernetes cluster**with NVIDIA GPUs and Dynamo namespace setup (see[Dynamo Cloud/Platform docs](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/kubernetes-quickstart))**Storage**PersistentVolumeClaim configured with appropriate permissions (see[deploy/utils README](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/utils/README.md))**Docker image**containing the Dynamo benchmarking tools

## Quick Start

### Step 1: Deploy Your DynamoGraphDeployment

Deploy your DynamoGraphDeployment using the [deployment documentation](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/examples/backends/). Ensure it has a frontend service exposed.

### Step 2: Deploy and Run Benchmark Job

**Note**: The server-side benchmarking job requires a Docker image containing the Dynamo benchmarking tools. Before the 0.5.1 release, you must build your own Docker image using the [container build instructions](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/container/README.md), push it to your container registry, then update the `image`

field in `benchmarks/incluster/benchmark_job.yaml`

to use your built image tag.

#### Customize the job configuration

To customize the benchmark parameters, edit the `benchmarks/incluster/benchmark_job.yaml`

file and modify:

**Model name**: Change`"Qwen/Qwen3-0.6B"`

in the args section**Benchmark name**: Change`"qwen3-0p6b-vllm-agg"`

to your desired benchmark name**Service URL**: Change`"vllm-agg-frontend:8000"`

so the service URL matches your deployed service**Docker image**: Change the image field if needed

Then deploy:

### Step 3: Retrieve Results

### Step 4: Generate Plots

This will create visualization plots. For more details on interpreting these plots, see the [Summary and Plots](https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/dynamo-benchmarking-guide#summary-and-plots) section above.

## Cross-Namespace Service Access

Server-side benchmarking can benchmark services across multiple namespaces from a single job using Kubernetes DNS. When referencing services in other namespaces, use the full DNS format:

**DNS Format**: `<service-name>.<namespace>.svc.cluster.local:port`


This allows you to:

- Benchmark multiple services across different namespaces in a single job
- Compare services running in different environments (dev, staging, production)
- Test cross-namespace integrations without port-forwarding
- Run comprehensive cross-namespace performance comparisons

## Configuration

The benchmark job is configured directly in the YAML file.

### Default Configuration

**Model**:`Qwen/Qwen3-0.6B`

**Benchmark Name**:`qwen3-0p6b-vllm-agg`

**Service**:`vllm-agg-frontend:8000`

**Docker Image**:`nvcr.io/nvidia/ai-dynamo/vllm-runtime:0.8.1`


### Customizing the Job

To customize the benchmark, edit `benchmarks/incluster/benchmark_job.yaml`

:

**Change the model**: Update the`--model`

argument**Change the benchmark name**: Update the`--benchmark-name`

argument**Change the service URL**: Update the`--endpoint-url`

argument (use`<svc_name>.<namespace>.svc.cluster.local:port`

for cross-namespace access)**Change Docker image**: Update the image field if needed

### Example: Multi-Namespace Benchmarking

To benchmark services across multiple namespaces, you would need to run separate benchmark jobs for each service since the format supports one benchmark per job. However, the results are stored in the same PVC and may be accessed together.

## Understanding Your Results

Results are stored in `/data/results`

and follow the same structure as client-side benchmarking:

## Monitoring and Debugging

### Check Job Status

### View Logs

### Debug Failed Jobs

## Troubleshooting

### Common Issues

**Service not found**: Ensure your DynamoGraphDeployment frontend service is running**PVC access**: Check that`dynamo-pvc`

is properly configured and accessible**Image pull issues**: Ensure the Docker image is accessible from the cluster**Resource constraints**: Adjust resource limits if the job is being evicted

### Debug Commands

## Customize Benchmarking Behavior

The built-in Python workflow connects to endpoints, benchmarks with aiperf, and generates plots. If you want to modify the behavior:

-
**Extend the workflow**: Modify`benchmarks/utils/workflow.py`

to add custom deployment types or metrics collection -
**Generate different plots**: Modify`benchmarks/utils/plot.py`

to generate a different set of plots for whatever you wish to visualize. -
**Direct module usage**: Use individual Python modules (`benchmarks.utils.benchmark`

,`benchmarks.utils.plot`

) for granular control over each step of the benchmarking process.

The Python benchmarking module provides a complete end-to-end benchmarking experience with full control over the workflow.

## Testing with Mocker Backend

For development and testing purposes, Dynamo provides a [mocker backend](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/components/src/dynamo/mocker/) that simulates LLM inference without requiring actual GPU resources. This is useful for:

**Testing deployments**without expensive GPU infrastructure**Developing and debugging**router, planner, or frontend logic**CI/CD pipelines**that need to validate infrastructure without model execution**Benchmarking framework validation**to ensure your setup works before using real backends

The mocker backend mimics the API and behavior of real backends (vLLM, SGLang, TensorRT-LLM) but generates mock responses instead of running actual inference.

See the [mocker directory](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/components/src/dynamo/mocker/) for usage examples and configuration options.