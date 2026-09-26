source: https://docs.nvidia.com/dynamo/v1.3.0/getting-started/kubernetes-deployment
lastmod: 2026-09-24T19:58:16.636Z

# Kubernetes Deployment

Use Dynamo’s Kubernetes-native path when you are ready to deploy on a GPU cluster.

Use the Kubernetes guides when you are ready to move beyond a local Dynamo process and deploy on a GPU cluster. Dynamo’s Kubernetes path is native to the platform: inference graphs are expressed as Dynamo CRDs, reconciled by the Dynamo operator, installed with Helm, and integrated with Kubernetes service discovery, Gateway API Inference Extension, scheduling, observability, and model-loading workflows.

This does not make Kubernetes the only way to use Dynamo. Local containers, PyPI installs, and standalone components remain the right path for evaluation, development, and incremental adoption.

Start with the [Kubernetes Quickstart](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart) to run one model end to end. Then use the rest of the Kubernetes Deployment section based on what you need next:

If you are still evaluating Dynamo locally, start with the [Quickstart](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/quickstart) and [Local Installation](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/local-installation) first.