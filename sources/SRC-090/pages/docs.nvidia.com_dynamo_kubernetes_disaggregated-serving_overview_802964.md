source: https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview
lastmod: 2026-09-25T12:26:00.485Z

# Disaggregated Serving

Disaggregated serving separates the two phases of LLM inference into their own worker pools so you can scale, size, and place them independently:

In an **aggregated** deployment, one worker does both phases. In a
**disaggregated** deployment, prefill and decode are separate pools on separate
GPUs: Dynamo routes each request through prefill first, transfers the KV cache to
the decode worker, then streams the response from decode.

Structurally, that difference is one worker versus two. The rest of the
`DynamoGraphDeployment`

(DGD) is the same:

###### Aggregated (1 worker)

###### Disaggregated (prefill + decode)

This guide walks through writing the disaggregated spec end to end. If you have
not authored a DGD before, read the [Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd)
guide first — this page assumes you know the overall shape and focuses on what
disaggregation adds.

## Should you disaggregate?

Disaggregation helps most when prefill and decode need different resource shapes:

- long prompts or retrieval-heavy traffic make prefill expensive
- long generations or high concurrency make decode the bottleneck
- you want to scale prefill and decode replicas independently
- large models need different parallelism for prompt processing and generation

It is not automatically better. For small models, short prompts, low concurrency,
or clusters without a fast KV-transfer fabric, an aggregated deployment is
simpler and often faster. Use [Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference) to
compare aggregated vs. disaggregated layouts before committing.

This guide uses a **single-node, multi-GPU** example — prefill and decode run on
separate GPUs in the same node (for instance, a node with 8×H100 serving
Qwen3-32B, one GPU per worker). On a single node the KV cache moves GPU-to-GPU
over NVLink, so there is nothing extra to configure for the transport. Scaling
prefill and decode across **multiple nodes** adds RDMA networking — see
[Enable multi-node transfer](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview#enable-multi-node-transfer) at the end.

## Write the deployment

### Check prerequisites

For the single-node example in this guide you need:

**A node with multiple GPUs**— one per prefill and decode worker (this example uses 8×H100 with`gpu: "1"`

per worker).**ETCD and NATS**deployed for Dynamo coordination.**A HuggingFace token secret**(`hf-token-secret`

) if the model is gated.

Model caching (the PVC and `HF_HOME`

wiring the workers mount) is configured
separately — see [Model caching](https://docs.nvidia.com/dynamo/kubernetes/kv-cache-offloading/overview). This
guide omits those fields for clarity; without them the model downloads to the
container’s default cache.

Scaling across multiple nodes additionally requires an RDMA-capable network and
device plugin — covered in [Enable multi-node transfer](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview#enable-multi-node-transfer).

### Start the spec: the frontend

Begin with the DGD skeleton — just a frontend. This is identical to an aggregated deployment; nothing about disaggregation changes it.

### Add the prefill worker

The prefill worker runs the prompt phase. Two things make it a prefill worker rather than a plain worker:

`subComponentType: prefill`

tags the role for the operator and router.`--disaggregation-mode prefill`

tells the engine to stop after producing the KV cache instead of generating tokens.

Qwen3-32B fits on a single H100, so each worker takes `gpu: "1"`

with no tensor
parallelism. `replicas: 3`

gives three prefill workers; size the count for your
prompt load independently of decode. (`sharedMemory`

is explained in the KV
transfer step.)

### Add the decode worker

The decode worker continues generation after prefill hands off the KV cache. It
mirrors the prefill worker with `subComponentType: decode`

and
`--disaggregation-mode decode`

, and its replica count is sized for concurrency
rather than prompt load.

Prefill and decode workers must pass the **same --model** (and, if you set
them, the same dtype, block size, and KV layout). A mismatch means the KV cache
prefill produces cannot be consumed by decode — you get transfer errors or
silently corrupt output.

### Enable KV transfer

Because prefill and decode run on **different GPUs**, the KV cache prefill
produces has to be copied into the decode worker’s GPU memory before decode can
generate. Dynamo’s transfer layer, **NIXL**, does this automatically. On a
single node it selects **CUDA IPC** and moves the cache GPU-to-GPU over NVLink —
no network, no RDMA, nothing to configure for the transport itself.

The one field you do set is shared memory, already in the worker specs above:

That is the entire KV-transfer configuration for a single node: two workers
tagged prefill/decode, matching `--model`

, and enough shared memory for NIXL.

### Apply and verify the transfer path

Apply the assembled spec:

Then confirm NIXL initialized its transfer backend — the key check for a disaggregated deployment. Grep a prefill worker’s logs:

You want to see NIXL bring up a backend, for example:

If NIXL fails to initialize, the usual cause is `sharedMemory.size`

left at the
default. Symptoms of a broken transfer path include high TTFT despite free
prefill capacity, decode workers sitting idle while prefill is busy, or
disaggregated throughput falling below your aggregated baseline.

### Enable multi-node transfer

Everything above keeps prefill and decode on **one node**, where the KV cache
moves over NVLink. When a worker’s parallelism exceeds the GPUs on a node, or you
want prefill and decode pools on separate machines, the KV cache travels over the
**network** instead — and that path needs **RDMA** (InfiniBand or RoCE). Without
it, transfers fall back to TCP and KV movement can dominate TTFT and throughput.

Multi-node adds RDMA fields to each worker (`rdma/ib`

resource requests, the
`IPC_LOCK`

capability, and `UCX_*`

transport env vars) plus an RDMA device plugin
on the cluster. That setup is out of scope here — see the
[Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication)
for the transport configuration and [Multinode Deployments](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments)
for spanning workers across machines.

## Faster starting points

Typing the full spec from scratch is rarely the fastest path. Copy a validated template and adapt it:

Good recipe starting points:

[Qwen3-32B vLLM disagg + KV router](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/recipes/qwen3-32b)[DeepSeek V3.2 TensorRT-LLM disagg + KV router](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/recipes/deepseek-v32-fp4)[Llama 3 70B vLLM disaggregated recipes](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/recipes/llama-3-70b)

Backend deployment examples with concrete worker flags:

## How disaggregation relates to KV-aware routing

These are separate features that pair well. Disaggregation splits prefill and decode. KV-aware routing chooses workers based on cache locality. Many production deployments use both, but you can reason about them independently.

For router behavior, see [Router: Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving)
and [KV Cache Aware Routing](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide).

## Before production

- Confirm NIXL initialized on each worker (the log check above).
- Confirm prefill and decode workers agree on model, dtype, block size, and KV layout.
- Confirm pods have the required GPU and shared memory.
- Confirm frontend/router flags match your routing strategy.
- Run benchmarks inside the cluster, not through local port-forwarding.
- If you scale across nodes, validate the RDMA transfer path — see
[Enable multi-node transfer](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview#enable-multi-node-transfer).

Use [Dynamo Benchmarking](https://docs.nvidia.com/dynamo/recipes/benchmarks/benchmarking) to compare
aggregated and disaggregated configurations under the same workload.

## Next steps

- Start from a matching
[Dynamo Recipe](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/recipes)when one exists. - Read the backend-specific
`disagg.yaml`

for your engine. - Use
[Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference)or DGDR to choose prefill/decode sizing. - Validate with
[Dynamo Benchmarking](https://docs.nvidia.com/dynamo/recipes/benchmarks/benchmarking).