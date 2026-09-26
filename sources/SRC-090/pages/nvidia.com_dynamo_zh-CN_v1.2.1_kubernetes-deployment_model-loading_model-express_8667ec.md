source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/model-loading/model-express
lastmod: 2026-09-23T23:30:39.914Z

# ModelExpress

ModelExpress is a model weight distribution service for faster worker startup in larger Dynamo clusters. Instead of every worker downloading the full model from storage, one worker can publish model weight availability and later workers can pull compatible tensors from that source over NIXL/RDMA. ModelExpress can also pair with ModelStreamer to stream safetensors directly from object storage into GPU memory.

Use ModelExpress when model rollout time, autoscale cold start, or fleet-wide model updates matter more than the simplicity of a shared PVC. For smaller clusters, start with [Model Caching](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/model-loading/model-caching).

## When to Use It

## How It Works

- A ModelExpress server runs in the cluster and stores metadata for available model sources.
- vLLM workers use the ModelExpress loader (
`--load-format mx`

on newer images, or`mx-source`

/`mx-target`

on older split-loader images). - If a compatible source worker is already serving the model, a new worker pulls model tensors from that source over NIXL/RDMA.
- If no source is available, the worker falls back to storage. With ModelStreamer, the first worker can stream safetensors from
`s3://`

,`gs://`

,`az://`

, or a local path. - The Kubernetes operator can inject
`MODEL_EXPRESS_URL`

into all Dynamo pods from the platform`modelExpressURL`

setting.

## Configure the Platform

Set the ModelExpress server URL when installing the Dynamo platform:

If the ModelExpress server is installed separately, point `dynamo-operator.modelExpressURL`

at that service. The operator injects the value into worker pods as `MODEL_EXPRESS_URL`

.

## Configure vLLM Workers

Use a runtime image that includes the `modelexpress`

Python package. For ModelStreamer, the image also needs `runai-model-streamer`

and the relevant object-storage SDK dependencies.

Use the load format supported by your runtime image. ModelExpress v0.3 and newer document the unified `mx`

loader. Some older Dynamo images expose `mx-source`

and `mx-target`

loader names instead.

## Stream Without Shared Storage

If the ModelExpress server cache is on a non-shared volume, workers cannot read the server’s local cache path. Set `MODEL_EXPRESS_NO_SHARED_STORAGE=1`

on worker pods so the client streams model files from the server over gRPC:

Use this path when the server has an RWO PVC, runs in a different namespace, or the cluster has no RDMA fabric available. Shared-filesystem mode is still faster when available.

## Stream From Object Storage

Set `MX_MODEL_URI`

when the first worker should stream safetensors directly from object storage or a local mounted path:

Credentials are consumed by the storage SDKs in the worker pod. They do not flow through the ModelExpress server.

## See Also

[Model Caching](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/model-loading/model-caching)- simple PVC-based model caching and the longer ModelExpress background.[ModelExpress deployment guide](https://github.com/ai-dynamo/modelexpress/blob/main/docs/DEPLOYMENT.md)- server, P2P, and ModelStreamer configuration.[Installation Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/installation-guide)- Dynamo platform install options, including`modelExpressURL`

.