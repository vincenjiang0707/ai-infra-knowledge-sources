source: https://docs.nvidia.com/dynamo/zh-CN/cli/model-deployment/multi-node-deployment
lastmod: 2026-09-24T19:58:16.636Z

Multi-Node Deployment


Multi-Node Deployment

When a model’s tensor-parallel size exceeds the number of GPUs on one node, you split a single worker across **multiple nodes**. This is not limited to Kubernetes — vLLM and SGLang can run this topology directly with the CLI. One node acts as the **head** (running the frontend and rank 0), and additional nodes join the same distributed worker group.

Reach for this only when one model copy genuinely does not fit on a single node. If it fits on one node, stay [single-node](https://docs.nvidia.com/dynamo/cli/model-deployment/introduction#more-on-one-node) — tensor parallelism synchronizes on every layer, and crossing the node boundary trades the fast intra-node NVLink interconnect for slower inter-node networking.

For spanning **multiple machines**, we recommend [Kubernetes](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) instead — it handles the cross-node scheduling, networking, and fault tolerance for you. The CLI path documented here works and is fully real, but you own placement and restarts by hand. Use it if you’re set on the CLI for a fixed set of machines you control.

## How multi-node works without the operator

On Kubernetes, multi-node serving relies on a gang-scheduler (Grove, KAI, or Volcano) to place all the pods across nodes atomically and wire up their networking. That scheduling problem only exists because Kubernetes owns placement — the actual cross-node mechanism underneath is plain `torch.distributed`

.

With the CLI, **you are the scheduler**: you start the process on each node yourself. There is no operator and no gang-scheduler. Each node runs the same backend command with a different `--node-rank`

, and all ranks point at the head node’s distributed initialization address.

Both paths use the same underlying mechanism. The operator adds automatic scheduling, networking setup, and fault tolerance/restart on top — which is why [Kubernetes](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) remains the recommended path for production multi-node clusters. The CLI path is fully real for a fixed set of machines you control, but if a node dies you restart it by hand.

## Prerequisites

**Enough GPUs across nodes**for the model’s tensor-parallel size. The launch preset assumes 8 GPUs per node, so TP=16 spans 2 nodes.between nodes — the head node’s address must be reachable from every worker on the port NCCL uses. Fast inter-node networking (RDMA/InfiniBand) matters here, because tensor parallelism does an all-reduce on every layer.`torch.distributed`

connectivity**NATS and etcd reachable from every node**, so workers and the frontend can discover each other. This is the same discovery requirement as a single-node deployment — it just has to be reachable across the network now.**Start the head node first**, then each worker.

## Serve a model across two nodes

The worker command is nearly identical on every node — only `--node-rank`

changes, and the head additionally runs the frontend. The tensor-parallel size is the **total across all nodes** (16 = 8 GPUs × 2 nodes). vLLM uses `--master-addr`

; SGLang uses `--dist-init-addr`

with an explicit port.

###### vLLM

###### SGLang

### Verify the deployment

The head node’s worker registers with the frontend as usual; the headless workers contribute their GPUs to the tensor-parallel group but do not run their own ingress. Once every node has joined and the model has loaded, send requests to the frontend on the head node exactly as in the [single-node tutorial](https://docs.nvidia.com/dynamo/cli/model-deployment/introduction).

For vLLM, `--headless`

prevents a nonzero rank from registering its own Dynamo endpoint. SGLang handles this from `--node-rank`

: nonzero ranks join the distributed engine without serving a separate endpoint.

## Backend Support

TensorRT-LLM supports multi-node serving, but the current Dynamo examples rely on the Kubernetes operator to create the worker group and MPI launch environment. This page does not provide an unvalidated manual `mpirun`

command.

## vLLM Launch Script

The repository provides [ launch/multi_node_tp.sh](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/vllm/launch/multi_node_tp.sh) as a vLLM head/worker preset that wraps the commands above. Run it with a role flag on each node, pointing both at the head node’s IP:

Override the model, tensor-parallel size, and node count with the `MODEL`

, `TENSOR_PARALLEL_SIZE`

, and `NNODES`

environment variables. The script assumes 8 GPUs per node and starts the head node first. SGLang does not currently have an equivalent checked-in helper script; use the SGLang tab’s commands directly.

## Choosing how to span nodes

The tensor-parallel size is the total number of GPUs in the group, but on multi-node you have a choice in how it maps onto your nodes:

**Tensor parallelism across nodes**(as above, TP=16 over 2 nodes) treats a node*pair*as a single TP domain. This is the simplest to launch and matches the preset, but every layer’s all-reduce now crosses the node boundary — it works well only when the inter-node link is fast (RDMA/InfiniBand).**Tensor parallelism within each node, pipeline parallelism across nodes**(for example TP=8 per node × PP=2) keeps the chatty per-layer all-reduce on NVLink inside each node and only communicates at pipeline-stage boundaries between nodes. This tolerates slower inter-node links at the cost of pipeline bubbles, and is often the safer default for larger clusters.

Both hold exactly one copy of the model — tensor and pipeline parallelism partition the weights without duplicating them. See [Scaling to larger models and more GPUs](https://docs.nvidia.com/dynamo/cli/model-deployment/introduction#scaling-and-larger-deployments) for how to size the GPU pool.

## Next steps

— how a deployment is structured and single-node scaling.[Overview](https://docs.nvidia.com/dynamo/cli/model-deployment/introduction)— native SGLang multi-node flags and the Kubernetes example.[SGLang backend guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/overview#multi-node-tp)— supported operator-managed TensorRT-LLM entrypoints.[TensorRT-LLM multinode examples](https://docs.nvidia.com/dynamo/additional-resources/tensor-rt-llm-details/multinode-examples)— the recommended production path, with scheduling and fault tolerance handled for you.[Kubernetes multi-node deployment](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments)