source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/kubernetes-deployment/model-loading/model-caching
lastmod: 2026-09-23T23:30:39.914Z

# Model Caching

Large language models can take minutes to download. Without caching, every pod downloads the full model independently, wasting bandwidth and delaying startup. Dynamo supports a simple shared-storage path and a ModelExpress path for faster weight distribution across larger clusters.

## Option 1: PVC + Download Job (Recommended)

The simplest approach: create a shared PVC, run a one-time Job to download the model, then mount the PVC in your DynamoGraphDeployment.

This is the pattern used by all Dynamo recipes today.

### Step 1: Create a Shared PVC

`ReadWriteMany`

access mode is required so multiple pods can mount the PVC simultaneously. Ensure your storage class supports RWX (e.g., NFS, CephFS, or cloud-provider shared file systems).

### Step 2: Download the model

### Find the Snapshot Path

After the Job completes, the model is stored in HuggingFace’s cache layout:

For example, `meta-llama/Llama-3.1-70B-Instruct`

becomes:

To find the exact commit hash after the download Job completes:

Alternatively, look up the commit hash on the HuggingFace Hub model page under **Files and versions**.

You need this path for the `pvcModelPath`

field in a DGDR spec (see [Deployment Overview — Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/model-deployment-guide#production-detail-model-caching)).

### Step 3: Mount in DynamoGraphDeployment

All `VllmWorker`

pods that mount `model-cache`

now read from the shared cache, avoiding per-pod worker downloads. If you also want the frontend to reuse tokenizer and config files, mount the same PVC there too.

### Compilation Cache

For vLLM, you can also cache compiled artifacts (CUDA graphs, etc.) with a second PVC:

## Option 2: ModelExpress (P2P Distribution)

[ModelExpress](https://github.com/ai-dynamo/modelexpress) is a model weight distribution service that integrates with engine weight loading pipelines. It can publish model weights from one worker and let later workers pull those tensors from GPU memory over NIXL/RDMA instead of repeating a full storage download.

ModelExpress can also use **ModelStreamer** as a loading strategy. ModelStreamer streams safetensors directly from object storage or a local filesystem path into GPU memory through the `runai-model-streamer`

package. In that setup, the first worker can stream from storage and then publish ModelExpress metadata so later workers can use the P2P path.

Use this path when startup time or fleet-wide model rollout time matters more than the simplicity of a shared PVC.

### How It Works

- A ModelExpress server runs in the cluster and stores metadata for available sources.
- Engine workers use the ModelExpress loader from an MX-enabled runtime image. For vLLM, set
`--load-format modelexpress`

. For SGLang, use a runtime image whose SGLang version includes the native`backend=modelexpress`

loader. - If a compatible source is already serving the model, a new worker pulls model tensors from that source over NIXL/RDMA.
- If no source is available, the worker falls back to storage. With a shared filesystem (RWX PVC, NFS, hostPath), the worker reads directly from the server’s cache. Without a shared filesystem, set
`MODEL_EXPRESS_NO_SHARED_STORAGE=1`

so the client streams files from the server over gRPC; see[Streaming Without Shared Storage](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching#streaming-without-shared-storage)below. When`MX_MODEL_URI`

is set, ModelStreamer can stream safetensors from S3, GCS, Azure Blob Storage, or a local path. - Workers that use a ModelExpress server set
`MODEL_EXPRESS_URL`

in the worker pod environment.

### What To Configure

### Setup

**Install with Dynamo Platform:**

You can also deploy the ModelExpress server separately with the [ModelExpress deployment guide](https://github.com/ai-dynamo/modelexpress/blob/main/docs/DEPLOYMENT.md) and set `MODEL_EXPRESS_URL`

directly in the worker manifest. The examples below assume the server is reachable at `http://model-express-server.model-express.svc.cluster.local:8080`

.

**Configure workers to use ModelExpress:**

When `dynamo-operator.modelExpressURL`

is configured, the operator injects `MODEL_EXPRESS_URL`

into component pods, so you do not need to repeat it in every worker manifest. If different workers should use different ModelExpress servers, or if you are using a ModelStreamer-only flow that does not need a server, set the relevant env vars explicitly in the DGD manifest instead.

`VLLM_PLUGINS=modelexpress`

is required while vLLM discovers this loader through the plugin path. Set it in the DGD manifest when using `--load-format=modelexpress`

. If a manifest enables additional vLLM plugins, include `modelexpress`

in the same comma-separated value.

### Streaming Without Shared Storage

If the ModelExpress server’s cache is on a non-shared volume (e.g. a `ReadWriteOnce`

PVC, a cross-namespace deployment, or any topology where worker pods cannot mount the same filesystem as the server), the default shared-storage mode fails: the server reports the model as downloaded and returns its own local path, the worker cannot read that path from inside its own pod, and the load silently falls back to a direct HuggingFace download — defeating the point of running ModelExpress.

Set `MODEL_EXPRESS_NO_SHARED_STORAGE=1`

on every worker pod to switch the ModelExpress client into gRPC streaming mode. The server then sends model files to the client over the existing gRPC channel and the worker writes them to its own local cache.

No volume mount for the ModelExpress cache is required on worker pods in this mode.

Use this path when:

- The server runs with an RWO PVC, or in a different namespace from the workers.
- The cluster has no RDMA / InfiniBand fabric available, so P2P over NIXL is not an option.
- You want ModelExpress to act as a centralized download-and-cache server (one HuggingFace pull, fan out over gRPC to many workers) without standing up object storage and
`MX_MODEL_URI`

.

Shared-filesystem mode is still faster when available, so prefer an RWX PVC mounted on both the server and the workers when the storage class supports it. See the [ModelExpress storage access modes documentation](https://github.com/ai-dynamo/modelexpress/blob/main/docs/DEPLOYMENT.md#storage-access-modes) for the full trade-off and tuning knobs (chunk size, etc.).

### ModelStreamer From Object Storage

Set `MX_MODEL_URI`

when the first worker should stream safetensors directly from storage instead of reading a PVC or relying on a prior source worker.

ModelStreamer relies on the underlying cloud SDK credentials:

Credentials are consumed by the storage SDKs in the worker pod. They do not flow through the ModelExpress server.

### Relationship To Shadow Engine Failover

ModelExpress and ModelStreamer are model loading and distribution paths. They are not required for [Shadow Engine Failover](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/shadow-engine-failover), and enabling them does not create standby engines.

Use Shadow Engine Failover only when you specifically need an active/shadow recovery topology backed by GPU Memory Service (GMS), DRA, and a backend load format such as `--load-format gms`

. Keep the ModelExpress / ModelStreamer configuration separate unless you have validated a combined workflow for your runtime image and cluster.

### When to Use ModelExpress

## See Also

[Managing Models with DynamoModel](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/managing-models-with-dynamo-model)— declarative model management CRD[Detailed Installation Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide)— Helm chart configuration including ModelExpress[Shadow Engine Failover](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/shadow-engine-failover)— GMS-backed active/shadow engine recovery, separate from model distribution[ModelExpress deployment guide](https://github.com/ai-dynamo/modelexpress/blob/main/docs/DEPLOYMENT.md)— server, P2P, and ModelStreamer configuration[LoRA Adapters](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/lo-ra-adapters)— dynamic adapter loading (separate from base model caching)