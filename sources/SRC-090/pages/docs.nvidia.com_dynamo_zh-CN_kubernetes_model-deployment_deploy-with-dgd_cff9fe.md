source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/model-deployment/deploy-with-dgd
lastmod: 2026-09-24T19:58:16.636Z

# Deploy with DGD

Author a DynamoGraphDeployment spec step by step — choose a model and backend, size parallelism for your hardware, then apply it and send requests.

A **DynamoGraphDeployment (DGD)** is the Kubernetes Custom Resource (CRD) that describes how to deploy a model with Dynamo. You write the spec, `kubectl apply`

it, and the Dynamo operator reconciles it into the running pods, services, and scheduling resources that serve your model. One DGD describes one inference graph: a Frontend plus one or more workers.

This guide walks through authoring that spec end to end: choose a model, pick a backend, choose aggregated or disaggregated serving, size the topology and parallelism for your hardware, then apply the deployment and send it a request. Each step fills in more of a single DGD spec. Environment-specific values — namespace, runtime image, HuggingFace token — stay in shell variables and are filled into the spec at apply time with `envsubst`

, so the same YAML file moves between clusters unchanged.

The examples use the `nvidia.com/v1beta1`

API: `spec.components`

is a list, and each component carries a standard Kubernetes `podTemplate`

. (The older `nvidia.com/v1alpha1`

API used a `spec.services`

map with `extraPodSpec`

; the operator still serves it and converts between the two.)

## Prerequisites

Before authoring a DGD, make sure you have:

- A Kubernetes cluster with the
**Dynamo Platform installed**. See the[Installation Guide](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo). `kubectl`

access to that cluster and a target namespace.- A
**HuggingFace token**for gated or rate-limited models (you create the Secret in step 1). - New to Dynamo on Kubernetes? Run one model end to end with the
[Kubernetes Quickstart](https://docs.nvidia.com/dynamo/kubernetes/getting-started/quickstart)first, then come back here to author your own spec.

For the concepts behind the CRDs and the operator, see the [Model Deployment](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/introduction) and the [API Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/full-api-reference).

## How a DGD is structured

Every DGD has the same top-level shape. `spec.components`

is a list, where each entry is one Dynamo component with a stable `name`

and a `type`

:

`type: frontend`

is the HTTP entry point — see[Frontend](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/frontend/overview).`type: worker`

runs the inference engine (vLLM, SGLang, or TensorRT-LLM).- Per-component fields you will use most:
`replicas`

,`multinode`

,`sharedMemorySize`

, and`podTemplate`

— a standard Kubernetes[PodTemplateSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podtemplatespec-v1-core). The operator injects its defaults into the container named`main`

inside`podTemplate.spec.containers`

, where you set the`image`

, the`command`

/`args`

that launch the engine,`resources`

(CPU/memory/GPU),`envFrom`

,`env`

, and`volumeMounts`

.

The steps below fill in these fields, building one spec from a model to a running deployment.

### Choose your model

Pick the model you want to serve from HuggingFace. This guide uses **Qwen3-32B** as the running example; substitute your own anywhere you see it.

A few values change per environment — the target namespace, the runtime image, and your HuggingFace token. Rather than hard-code them, keep them in shell variables and fill them into the spec at apply time with `envsubst`

(from the `gettext`

package). Export the two you know now — you pick the image in the next step:

Gated or rate-limited models need the token as a Secret in your namespace. Create it once from `$HF_TOKEN`

:

Start the spec with a Frontend and one worker. The `${NAMESPACE}`

and `${RUNTIME_IMAGE}`

placeholders are expanded by `envsubst`

when you apply (see the *Apply* step); the worker pulls the token from the Secret via `envFrom`

, and the model name is passed to the engine as an argument. The worker’s launch command is backend-specific — this guide defaults to **vLLM**; select your backend and the choice syncs across every code block on this page (you set the matching image in the next step):

###### vLLM

###### SGLang

###### TensorRT-LLM

Substitute `Qwen/Qwen3-32B`

with your model, `hf-token-secret`

with your Secret name if you changed it. Keeping the namespace, image, and token in the environment means the same YAML file works across clusters — you change the exports, not the spec.

**Large model?** By default every worker pod downloads the weights from HuggingFace on startup — slow for big models and prone to rate limits across many replicas. Cache the weights once on a shared volume and mount them into each worker. See [Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching) (and [ModelExpress](https://docs.nvidia.com/dynamo/kubernetes/operations/cold-start-optimizations/model-express) for fleet-scale distribution).

### Choose your backend

The worker in the previous step runs **vLLM**. Dynamo also supports **SGLang** and **TensorRT-LLM**, and the backend you picked there already synced every code block on this page. The backend sets three things: the runtime image, the launch module (`dynamo.vllm`

/ `dynamo.sglang`

/ `dynamo.trtllm`

), and how you pass the model and parallelism. Export the matching image so `envsubst`

fills the `${RUNTIME_IMAGE}`

placeholder on both the Frontend and the worker:

###### vLLM

###### SGLang

###### TensorRT-LLM

The launch module and the way each engine takes the model differ, which is why the worker block changed when you switched tabs above:

vLLM and SGLang take tensor/pipeline/data parallelism as CLI flags (covered in the topology step). TensorRT-LLM is the exception: it reads **all** parallelism from the engine-config YAML referenced by `--extra-engine-args`

, not from worker flags.

**Check the model works on your hardware and backend before you deploy.** Not every model, GPU, and backend combination is valid — a quantization can be unsupported on your GPU architecture (for example, FP8 needs Hopper/Ada or newer; some FP4/NVFP4 paths need Blackwell), or an engine may not yet implement a model’s architecture. Confirm against the backend’s supported-models list ([vLLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/overview), [SGLang](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/overview), [TensorRT-LLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/overview)) and, for sizing, the [AIConfigurator support matrix](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference).

You normally do not need to set the top-level `spec.backendFramework`

field — the operator infers the backend from the worker command. Set it explicitly (`vllm`

, `sglang`

, or `trtllm`

) only when a feature needs the framework known up front, such as GMS failover or multinode TensorRT-LLM.

For per-backend setup and tuning, see [vLLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/overview), [SGLang](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/overview), and [TensorRT-LLM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/overview).

**Private registry?** The operator **auto-discovers and injects** image pull secrets by matching Docker config Secrets in the namespace against your image’s registry host, so private registries usually work with no extra config. To take manual control for a component, set the `nvidia.com/disable-image-pull-secret-discovery: "true"`

annotation on it and list your own `imagePullSecrets`

under `podTemplate.spec`

.

### Choose aggregated or disaggregated serving

Before sizing hardware, decide how prefill (prompt processing) and decode (token generation) are placed. Both patterns work with the same DGD spec — you are choosing how many worker roles it has.

**Aggregated**— the single worker you have been building does both phases. Simplest to deploy and debug; a good default for smaller models and uniform traffic.**Disaggregated**— separate prefill and decode worker pools, each sized, scaled, and parallelized independently, with the KV cache transferred between them over the network. Reach for it when prefill and decode have different bottlenecks — long prompts saturating prefill while decode sits idle, or high concurrency saturating decode.

If you are staying aggregated, keep the single worker and continue to the next step. To go disaggregated, replace the one worker with two, tagged by role. The tabs below use **vLLM** as a concrete example to highlight the structural difference — one worker versus a prefill/decode pair; SGLang and TensorRT-LLM follow the same pattern with their own flags:

###### Aggregated (1 worker)

###### Disaggregated (prefill + decode)

In the disaggregated spec, `type: prefill`

and `type: decode`

tag the roles, the KV cache moves over NIXL (`--kv-transfer-config`

), and `sharedMemorySize`

is raised for the transfer. When you disaggregate, the next step’s sizing applies to prefill and decode **separately** — you pick TP/PP for each role.

The fastest way to start is to copy a ready-to-apply Kubernetes template rather than type the spec from scratch. Choose the [vLLM](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgd/v-llm), [SGLang](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgd/sg-lang), or [TensorRT-LLM](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgd/tensor-rt-llm) templates in the Recipes tab, then adapt the model, image, and parallelism to your case.

For disaggregation-specific configuration — RDMA resources, UCX environment variables, and prefill/decode scaling — see [Disaggregated Serving](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview).

Disaggregated serving moves KV cache between workers over the network. For acceptable performance the cluster needs RDMA — see the [Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication). Without it, transfers fall back to TCP with severe latency penalties.

### Determine topology and parallelism

Now decide how many GPUs each worker needs and how to split the model across them. (If you disaggregated in the previous step, answer this once for the prefill worker and once for the decode worker — they size independently.)

**Will it fit?** A rough lower bound for the weights is `parameters × bytes-per-parameter`

: 2 bytes for BF16/FP16, 1 for FP8. Qwen3-32B in BF16 is ~64 GB of weights, so it needs at least two 40 GB GPUs or one 80 GB GPU — and that is before the KV cache, which grows with context length and concurrency. Leave headroom.

**The parallelism knobs.** A worker’s total GPUs equals the product of its parallel sizes; when it spans machines, that product also equals `multinode.nodeCount × per-node GPUs`

. Five knobs do different jobs:

**Tensor parallelism (TP)**splits every layer’s weight matrices across GPUs so one model copy spans them, cutting memory per GPU. The split is communication-heavy (an all-reduce every layer), so TP wants fast intra-node interconnect (NVLink) — keep it**within a node**.**Pipeline parallelism (PP)**splits the model into sequential stages — contiguous blocks of layers, one block per GPU or node. It also cuts memory per GPU, but only passes activations at stage boundaries, so it tolerates slower links and is how you span**across nodes**.**Data parallelism (DP) / replicas**runs multiple independent model copies for throughput. It does**not**help a model fit — each copy still needs enough GPUs to hold the model. Scale whole pods with`replicas`

, or use the engine’s own`--data-parallel-size`

(common with MoE attention).**Expert parallelism (EP)**applies to Mixture-of-Experts models only: it spreads a layer’s experts across GPUs so no single GPU holds them all.is infrastructure, not a model split: it tells the operator how many physical nodes one worker spans. You set it when TP×PP exceeds the GPUs on a single node.`multinode.nodeCount`


The exact flag differs per backend. vLLM and SGLang take them as CLI args on the worker; TensorRT-LLM reads them from the engine-config YAML instead:

**How to choose.** Work from where the model fits:

**Fits on one GPU**— no parallelism needed. Leave TP/PP/DP at 1, request one GPU, and skip to the*Apply*step. Add replicas later only for throughput.**Doesn’t fit on one GPU, fits on one node**— raise**TP**to the number of GPUs the weights (plus KV cache headroom) require, and set the worker’s`nvidia.com/gpu`

limit to match. TP keeps one model copy on the fast intra-node fabric.**Doesn’t fit on one node**— combine**PP**with`multinode.nodeCount`

so contiguous layer blocks land on separate nodes, typically with TP within each node. Total GPUs = TP × PP =`nodeCount × per-node GPUs`

.**Need more throughput**— the model already fits; add**replicas**(or`--data-parallel-size`

) to run more copies. This scales requests-per-second, not model size.**Mixture-of-Experts**— add**EP**on top of the above (see the MoE note below).

To pick actual numbers, start from a ** recipe**: if one matches your model, backend, and hardware, copy its TP/PP/DP and adapt. If none fits, use

**AIConfigurator**, which sweeps and ranks TP/PP/DP + replica configs for your model, GPU SKU, and latency target — see

[Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference).

**Worked example.** Qwen3-32B in BF16 doesn’t fit on one 80 GB GPU with room for KV cache, but TP-2 does. Set the parallel size on the worker and match the GPU limit — for TensorRT-LLM the size lives in the engine-config YAML instead, so only the GPU limit changes on the worker:

###### vLLM

###### SGLang

###### TensorRT-LLM

**TensorRT-LLM sets parallelism in the engine config, not on the CLI.** TP, PP, and MoE parallelism are keys in the engine-config YAML referenced by `--extra-engine-args`

— `tensor_parallel_size`

, `pipeline_parallel_size`

, `moe_tensor_parallel_size`

, and `moe_expert_parallel_size`

— not worker flags. Edit them there. Start from a per-model config under [ examples/backends/trtllm/engine_configs/](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/backends/trtllm/engine_configs/README.md) (it ships

`agg.yaml`

, `prefill.yaml`

, and `decode.yaml`

variants), and keep the worker’s `nvidia.com/gpu`

limit equal to the product of those sizes.**Context length.** There is no uniform DGD field for maximum context length — it is an engine flag: `--max-model-len`

(vLLM), `--context-length`

(SGLang), or `max_seq_len`

in the engine config (TensorRT-LLM). Longer context needs more free GPU memory for the KV cache, so it trades off against parallel size and concurrency. Set it when the default does not match your workload, for example `--max-model-len 32000`

.

**Mixture-of-Experts.** MoE models — DeepSeek-R1, Qwen3-235B, Kimi-K2 — add **expert parallelism (EP)** on top of the knobs above, and expose it as **two** sizes: how experts are split (EP) and how the non-expert (attention) weights are split (a tensor-parallel size for the MoE layers). In vLLM, enable EP with `--enable-expert-parallel`

, typically alongside `--data-parallel-size`

for the attention layers. In SGLang, use `--ep-size`

with `--enable-dp-attention`

. In TensorRT-LLM, set both `moe_expert_parallel_size`

and `moe_tensor_parallel_size`

in the engine config. Wide-EP deployments usually pair this with multinode and a fast all-to-all backend (for example `VLLM_ALL2ALL_BACKEND=deepep_low_latency`

). For a worked multinode wide-EP example, see the [DeepSeek-R1 recipe](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/recipes/deepseek-r1/vllm/disagg/deploy_hopper_16gpu.yaml).

**Multinode.** When TP × PP exceeds the GPUs on one node, set `multinode.nodeCount`

on the worker so it spans machines; the operator schedules the pods and wires the engine’s cross-node communication (Ray for vLLM, `--dist-init-addr`

/`--nnodes`

for SGLang, MPI for TensorRT-LLM). This needs Grove or LWS installed. See [Multinode Deployments](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) and the `disagg-multinode.yaml`

templates under each backend’s `deploy/`

folder.

**Leave room for the KV cache.** The weights are only part of GPU memory — the KV cache grows with context length and concurrency, and if it has no room the worker OOMs at load or under traffic. Each engine caps the fraction of GPU memory it will use: `--gpu-memory-utilization`

(vLLM, default 0.90), `--mem-fraction-static`

(SGLang), or `free_gpu_memory_fraction`

in the engine config (TensorRT-LLM). If you hit OOM, lower the fraction, add a GPU (raise TP), or reduce max context length.

### Apply the deployment and check status

You have exported `NAMESPACE`

and `RUNTIME_IMAGE`

(and created the token Secret). Expand the placeholders and validate the spec with a server-side dry run, then apply it — pipe the file through `envsubst`

both times:

`envsubst`

only substitutes `${VAR}`

tokens. Confirm the exports are set (`echo ${NAMESPACE} ${RUNTIME_IMAGE}`

) before applying, or the placeholders expand to empty strings. To see the fully rendered spec first, run `envsubst < qwen3-32b-agg.yaml | less`

.

The DGD is the live serving resource. It becomes ready once the Frontend and workers are up — the `Ready`

condition reports `True`

. Watch it reconcile:

Or block until it is ready:

If it stalls, `kubectl describe dynamographdeployment <name> -n ${NAMESPACE}`

and the operator events surface the cause. Common rejections: a multinode component with neither Grove nor LWS installed, an `nvidia.com/gpu`

limit that does not equal tensor-parallel × pipeline-parallel size, or a missing `envFrom`

Secret.

### Send a request

The operator creates a `ClusterIP`

Service named `<name>-frontend`

on port 8000. Port-forward it and send requests to the OpenAI-compatible API:

List the served models:

Send a chat completion — the `model`

field must match the model you deployed:

For a stable external address instead of `port-forward`

, see [Expose the Frontend](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/expose-the-frontend).

## Put it all together: Qwen3-32B

The following spec assembles the steps above into one aggregated Qwen3-32B deployment, adapted from the [agg-round-robin recipe](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/recipes/qwen3-32b/vllm/agg-round-robin/deploy.yaml). It reflects the backend you selected earlier. Comments mark the values you substitute for your model, hardware, and scale:

###### vLLM

###### SGLang

###### TensorRT-LLM

This runs eight TP-2 workers (16 GPUs). To turn it into one of the variations above — disaggregated, multinode, MoE expert-parallel, cached, KV-routed, or offloaded — apply the change from that step or the matching page below.

## Optional next steps

These are independent capabilities you opt into per workload. None are required for a working deployment.

**The Planner is not part of the DGD spec.** SLA-driven autoscaling with the [Planner](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/overview) is configured through a **DynamoGraphDeploymentRequest (DGDR)** — see [Auto Deploy with DGDR](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough). For HPA/KEDA scaling of a DGD service, see [Autoscaling](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/autoscaling). For the full field reference, see the [API Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/full-api-reference).