# [Issue #599] [RFC]: Multi-node support

source: https://github.com/vllm-project/speculators/issues/599
state: open | updated: 2026-08-23T08:52:20Z
labels: RFC

## 正文

### Motivation.

Scaling up speculators training can quickly hit limits of individual compute nodes. This is particularly an issue for online training workflows where some of the gpus have to be allocated to vllm hidden states generation, which can require multiple gpus for larger models.

For this reason, we'd like to be able to scale speculators training beyond a single compute node. This RFC explores the current blockers for this and implementation plan.

### Proposed Change.

## Stage 1: Offline multi-node datagen
Status: Complete
Implemented in #526. Simply shards the hidden states to generate between nodes, allowing them to be generated independently. Maintains data indices, so that hidden states can be combined.

## Stage 2: Offline multi-node training
Status: In-progress
Utilize `torchrun` / `FSDP`'s multi-node capability. To run training across multiple nodes. Currently requires all nodes to have the full preprocessed locally + access to all pre-generated hidden states. This is probably easiest enabled using some kind of shared network drive to store the generated hidden states.

Blockers:
- Some parts of the speculators library currently use `local_rank` instead of `rank`, which will need to be updated to handle the multi-node case.
- Needs testing

## Stage 3: Online multi-node training with co-located hidden states generation
e.g. Node 0 and 1, both w/ gpus 0-3 running vLLM, gpus 4-7 running training (training processes are synced across nodes, vllm processes are not)
Status: In-progress (should be possible whenever stage 2 is complete)

Blockers:
- Same as stage 2

## Stage 4: Online multi-node training with separate nodes for hidden states generation and training
This will be the biggest lift in training ability as it will allow a full node to be dedicated to hidden states extraction, will another node (or multiple) run the training loop.

The main challenge here is in getting the hidden states from the vLLM node to the training node. The current hidden states extraction system simply writes hidden states to disk where they can then be loaded by the training process. Technically this could be sufficient for stage 4 if using a shared network drive, but we'd like to have a better system.

That means we will need to implement a different HiddenStatesConnector based on either the Nccl, Nixl, or Mooncake KVConnectors. This will allow for direct transfer of the hidden states to the accelerator memory for the training process. This should help with performance for single node training as well.

Blockers:
- Better HiddenStatesConnector compatible with RDMA in vLLM

### Any Other Things.

_No response_

## 评论 (3)

### guan404ming · 2026-06-19

Hi could I help with this one?

### clumsylad21 · 2026-06-22

Hi @fynnsu , I’d be happy to help with Stage 2 multi-node training. Since #619 covers the global-rank changes, I was thinking of adding a small multi-node smoke test to verify data sharding and rank-0-only behavior, along with documentation for the two-node torchrun setup and shared-storage requirements. Would this be helpful?

### zihanlin-ai · 2026-08-22

Data points from a downstream trainer built on speculators, relevant to Stage 2:

- FSDP2 training across 8 nodes / 128 ranks using a 2D replicate × shard mesh (HSDP), and a 32-rank, ~6.4B-trainable-parameter full-expert configuration through training, validation, sharded checkpointing and crash recovery; each node keeps a complete replica, so resume needs no cross-node consolidation. This shows scale and operability only — no performance comparison against full-world FSDP.
- Two things that cost the most time and that a Stage 2 smoke test could assert cheaply: per-rank step counts must be strictly equal (skipping samples per rank inside the epoch loop desynchronised the collectives until a timeout that surfaced as an unrelated device error); and rank-0 gathering of the full checkpoint becomes the bottleneck once the drafter grows (e.g. an MoE drafter), at which point "sharded checkpoint for training resume" and "HF checkpoint for deployment export" need to be separate artifacts.

The blockers list says "needs testing"; a 2-node FSDP smoke can be run on our environment and reported back. Direction question: are the HSDP DeviceMesh and, later, multi-replica fault tolerance in scope for Stage 2, or follow-ups?

