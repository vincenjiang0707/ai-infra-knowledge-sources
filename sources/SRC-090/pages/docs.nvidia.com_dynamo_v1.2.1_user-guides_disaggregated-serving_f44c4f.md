source: https://docs.nvidia.com/dynamo/v1.2.1/user-guides/disaggregated-serving
lastmod: 2026-09-24T19:58:16.636Z

# Disaggregated Serving

Disaggregated serving separates the two main phases of LLM inference:

In an aggregated deployment, each worker does both phases. In a disaggregated deployment, prefill workers and decode workers are separate pools. Dynamo routes each request through prefill first, transfers or exposes the KV cache state to decode, and streams the response from the decode worker.

## When It Helps

Disaggregated serving is most useful when prefill and decode need different resource shapes:

- long prompts or retrieval-heavy traffic make prefill expensive
- long generations or high concurrency make decode the bottleneck
- you want to scale prefill and decode replicas independently
- you want to pair prefill/decode separation with KV-aware routing
- large models need different parallelism for prompt processing and generation

It is not automatically better for every workload. For small models, short prompts, low concurrency, or clusters without fast KV transfer, an aggregated deployment may be simpler and faster.

## Mental Model

Disaggregated serving usually combines four pieces:

KV-aware routing is related but separate. Disaggregated serving splits prefill and decode. KV-aware routing chooses workers based on cache locality. Many production deployments use both, but you can reason about them independently.

For router-specific behavior, see [Router: Disaggregated Serving](https://docs.nvidia.com/dynamo/v1.2.1/components/router/disaggregated-serving)
and [KV Cache Aware Routing](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/kv-cache-aware-routing).

## KV Transfer Is the Critical Path

Disaggregation only helps when decode workers can access the KV cache produced by prefill quickly. In cross-node or high-throughput deployments, the KV transfer path commonly depends on RDMA-capable networking through the backend’s transfer layer, such as NIXL/UCX. If RDMA is missing or silently falls back to TCP, TTFT and throughput can be dominated by KV movement rather than model compute.

Treat KV transfer as an early validation step, not a final tuning detail. Common
failure modes include missing RDMA device-plugin resources, pods without the
needed `rdma/ib`

requests or `IPC_LOCK`

capability, UCX/NIXL transport errors,
mismatched model or KV cache settings between prefill and decode workers, and
benchmarks that run through local port-forwarding instead of inside the cluster.

Symptoms usually look like high TTFT despite available prefill capacity, decode workers sitting idle while prefill workers are busy, or disaggregated throughput falling below an aggregated baseline after splitting workers across nodes.

Production cross-node disaggregated deployments usually require RDMA or an equivalent fast fabric for KV cache transfer. Without it, the backend may fall back to TCP and KV transfer can dominate TTFT and throughput. Validate the transfer path before spending time tuning replica counts.

### Deploying Disaggregated with RDMA

Disaggregated deployments transfer KV cache between prefill and decode workers. Without RDMA or another fast transfer path, this movement can become the main performance bottleneck.

Prerequisites for a production cross-node deployment:

**RDMA-capable network**such as InfiniBand, RoCE, or an equivalent fast fabric.**RDMA device plugin**installed on the cluster so worker pods can request`rdma/ib`

resources.**ETCD and NATS**deployed for Dynamo coordination.

The following example shows the RDMA-relevant fields in a disaggregated vLLM
`DynamoGraphDeployment`

. Start from a validated recipe when one exists, then
adapt the resource requests, model, image, and parallelism for your cluster.

Critical RDMA settings:

After deployment, check the worker logs for UCX/NIXL initialization:

Expected output includes:

If logs only show TCP transports, RDMA is not active. Check the RDMA device
plugin, worker `rdma/ib`

resource requests, security context, and UCX settings.
For full transport setup and troubleshooting, see the
[Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/disagg-communication).

## Deployment Paths

Choose the path that matches how much control you need:

Good recipe starting points include:

[Qwen3-32B vLLM disagg + KV router](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/recipes/qwen3-32b)[DeepSeek V3.2 TensorRT-LLM disagg + KV router](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/recipes/deepseek-v32-fp4)[Llama 3 70B vLLM disaggregated recipes](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/recipes/llama-3-70b)

For the Kubernetes resource model, see the [Deployment Overview](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/model-deployment-guide).

## Backend Examples

Each built-in backend has examples that show the concrete worker flags and transfer settings:

## Operational Notes

Disaggregated deployments add a data-movement path between workers. Before moving to production, verify:

- KV transfer backend and network fabric are configured for your backend
- RDMA resources, UCX/NIXL settings, and security context are active when your deployment depends on RDMA
- prefill and decode workers agree on model, dtype, block size, and KV layout
- pods have the required GPU, shared memory, and network resources
- frontend/router flags match your routing strategy
- benchmarks run inside the cluster, not through local port-forwarding, when validating high-load performance

Use [Dynamo Benchmarking](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/benchmarking) to compare
aggregated and disaggregated configurations with the same workload.

## Next Steps

- Start from a matching
[Dynamo Recipe](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/recipes)when available. - Read the backend-specific deployment example for your engine.
- Use
[Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/disaggregated-serving/sizing-with-ai-configurator)or DGDR when you need help choosing prefill/decode sizing. - Validate the result with
[Dynamo Benchmarking](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/benchmarking).