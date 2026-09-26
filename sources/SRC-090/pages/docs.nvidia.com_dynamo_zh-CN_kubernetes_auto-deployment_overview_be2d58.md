source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/auto-deployment/overview
lastmod: 2026-09-24T19:58:16.636Z

# Auto Deployment

Dynamo auto deployment starts with a `DynamoGraphDeploymentRequest`

(DGDR). Instead of specifying
every worker, parallelism setting, and replica count, you describe the model and deployment intent.
Dynamo profiles the available options and generates the `DynamoGraphDeployment`

(DGD) that serves
traffic.

Auto deployment does not replace the DGD. It provides a way to generate one when you do not already have a known-good deployment configuration.

## When to Use Auto Deployment

Use a DGDR when:

- You are deploying a new model and hardware combination and do not know the best configuration.
- You want Dynamo to choose parallelism, topology, and replica counts.
- You want to size a deployment for an expected workload or latency target.
- You want to inspect and customize a generated DGD before deploying it.
- You want profiling data to initialize optional Planner autoscaling.

Use a DGD directly when:

- A
[recipe or backend template](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/introduction#create-a-dgd)already matches your deployment. - You already know the topology, parallelism, and replica counts.
- You need complete control over the workers and Kubernetes configuration.
- Your model, backend, or hardware combination is not adequately supported by the profiler.

## How DGDR Creates a Deployment

### Describe the deployment intent

Create a DGDR with the model and optional backend, workload, latency targets, hardware limits, model cache, and Planner configuration.

### Discover the available hardware

The operator discovers the cluster’s GPU type, memory, GPU count, and node capacity. You can override the discovered values when you want to constrain the search or when the operator runs without cluster-wide node permissions.

### Profile candidate configurations

The Profiler uses AIConfigurator to enumerate and evaluate deployment configurations. The
`rapid`

strategy uses performance estimates, while `thorough`

deploys candidates and measures
them on real GPUs.

### Generate the DGD

The Profiler selects a configuration and produces a complete DGD containing the worker topology, parallelism, replica counts, resources, model settings, and enabled platform features.

## Auto Deployment Components

The Profiler and Planner serve different phases. The Profiler runs before deployment to choose a configuration. The Planner runs with the deployed DGD and changes capacity over time. You can use a DGDR without enabling the Planner.

## Profiling Strategies

See the [Profiler Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/profiler/profiler-guide) for support, gate checks, picking
behavior, and profiling artifacts.