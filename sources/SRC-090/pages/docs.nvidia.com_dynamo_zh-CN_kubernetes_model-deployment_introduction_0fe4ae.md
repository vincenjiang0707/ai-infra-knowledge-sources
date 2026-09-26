source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/model-deployment/introduction
lastmod: 2026-09-24T19:58:16.636Z

# Model Deployment

A **DynamoGraphDeployment (DGD)** is the Kubernetes entry point for serving a model
with Dynamo. It defines the frontend and model workers, their images and resources,
and how requests flow through the inference graph. When you apply a DGD, the Dynamo
operator creates and manages the underlying Kubernetes workloads and services.

The DGD is the deployment artifact that ultimately serves traffic, regardless of whether you start from a tuned manifest, copy a template, generate one, or write the resource directly.

## Create a DGD

Choose the starting point that best matches your model, hardware, and desired level of control.

## Choose a Deployment Topology

Start with aggregated serving when one worker can handle both prompt processing and token generation. For more demanding models and workloads, use these guides to split, size, or distribute the deployment.