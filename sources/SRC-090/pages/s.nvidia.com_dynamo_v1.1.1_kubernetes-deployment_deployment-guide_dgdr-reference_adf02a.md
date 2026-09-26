source: https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/dgdr-reference
lastmod: 2026-09-24T19:58:16.636Z

# DGDR Reference

A `DynamoGraphDeploymentRequest`

(DGDR) is Dynamo’s **deploy-by-intent** API.
You describe what you want to run and your performance targets; the profiler
determines the optimal configuration and creates the live deployment.

For a step-by-step walkthrough of deploying your model — including strategy
selection, model caching, planner setup, and common pitfalls — see the
[Model Deployment Guide](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-deployment-guide).

## DGDR vs DGD

Dynamo provides two Custom Resources for deploying inference graphs:

**When to use DGD instead**: Use DGD when you have a hand-crafted configuration
for a specific model/hardware combination (e.g., from `recipes/`

). These configs
may be more optimal for known setups but require understanding of what
parallelism parameters (TP, PP, EP) are appropriate and don’t generalize across
different hardware.

For DGD deployment details, see [Creating Deployments](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/creating-deployments).

## Spec Reference

### Minimal Example

### Field Reference

For the complete CRD spec, see the [API Reference](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/api-reference-k-8-s).

### SKU Format

When providing hardware configuration manually, use lowercase underscore format:

All supported values: `gb200_sxm`

, `b200_sxm`

, `h200_sxm`

, `h100_sxm`

,
`h100_pcie`

, `a100_sxm`

, `a100_pcie`

, `l40s`

, `l40`

, `l4`

, `v100_sxm`

,
`v100_pcie`

, `t4`

, `mi200`

, `mi300`

.

Not all SKUs are supported by the AIC profiler for `rapid`

mode. See
[AIC Support Matrix](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-deployment-guide#aic-support-matrix) for details.

## Lifecycle

When you create a DGDR, it progresses through these phases:

### Conditions

The operator maintains these conditions on the DGDR status:

### Monitoring

### Resource Ownership

- The DGDR does
**not**set an owner reference on the DGD it creates. Deleting a DGDR does not delete the DGD — it persists independently so it can continue serving traffic. - The relationship is tracked via labels:
`dgdr.nvidia.com/name`

and`dgdr.nvidia.com/namespace`

. - Additional resources (planner ConfigMaps) are created in the same namespace
and labeled with
`dgdr.nvidia.com/name`

.

## Further Reading

[Model Deployment Guide](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-deployment-guide)— How to deploy your model, strategy selection, pitfalls, examples[Profiler Guide](https://docs.nvidia.com/dynamo/v1.1.1/components/profiler/profiler-guide)— Profiling algorithms, picking modes, gate checks[Profiler Examples](https://docs.nvidia.com/dynamo/v1.1.1/components/profiler/profiler-examples)— Ready-to-use YAML for SLA targets, private models, MoE, overrides[Planner Guide](https://docs.nvidia.com/dynamo/v1.1.1/components/planner/planner-guide)— Scaling modes, PlannerConfig reference[API Reference](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/api-reference-k-8-s)— Complete CRD field specifications[Creating Deployments](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/creating-deployments)— DGD spec for full manual control