source: https://docs.nvidia.com/dynamo/kubernetes/installation/model-storage/overview
lastmod: 2026-09-25T12:26:00.485Z

# Model Storage Overview

Choose Kubernetes storage for model weights, compilation artifacts, and shared caches

Dynamo deployments often need shared storage before the first model pod starts. Use this page to choose the right storage path for model weights, backend compilation artifacts, and cache data, then follow the provider-specific setup guide for your cluster.

## What Needs Storage

Storage is especially important for large models and multi-node deployments. A slow or single-node model store can dominate cold-start time even when the serving stack is configured correctly.

## Choose a Storage Option

## Selection Guidelines

- Use high-throughput shared storage for large models that start on multiple nodes or replicas.
- Use persistent storage for model weights when repeated downloads would slow cold starts or stress object storage.
- Use fast ephemeral or node-local storage for scratch data that does not need to survive pod replacement.
- Confirm the storage class supports the access mode your deployment needs, such as
`ReadWriteMany`

for shared model caches. - Validate throughput during a scale-out test, not only with a single pod.

## Next Steps

- Pick the storage guide that matches your cloud provider.
- Create or verify the storage class and persistent volume claims.
- Follow
[Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching)to connect the storage to a Dynamo deployment.