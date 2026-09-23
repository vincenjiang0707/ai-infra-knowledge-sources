# 2026-09-13-kimi-k3-performance-optimization

source: https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization

# Kimi K3 Performance Optimizations in vLLM: The Road to 2.8× Throughput

Day-0 support got Kimi K3 running in vLLM. Efficient serving required another pass across the stack. KDA recurrent state, LatentMoE, MXFP4 expert kernels, speculative decoding, and TP/PP each exposed different bottlenecks; scheduler limits and small tensor copies could matter as much as a large GEMM.

This post starts with the end-to-end result, then looks at four representative changes: adaptive speculative-token budgets, internal KDA prefix checkpoints, zero-copy mixed KDA batches, and deferred MXFP4 finalization. Also covered: ReplaySSM, prefill/decode disaggregation and cache offload, and decode context parallelism. The wider effort is tracked in [Kimi K3 Performance Optimization #50587](https://github.com/vllm-project/vllm/issues/50587).

## Performance

Measured with an 8K/1K workload with TP8, eight tokens DSpark speculation. Concurrency 1, 4, and 16. Comparison from v0.27.1 to commit `82a85dc1`

(0913), tested on B300 node (CUDA 13.3).

Start the server:

Note: Prefix caching was disabled in both runs because v0.27.1 had a known Kimi K3 prefix-caching issue fixed later.

Run the benchmark:

| Concurrency | 0.27.1 Avg Latency (s) | 0913 main Avg Latency (s) | 0.27.1 Throughput (tok/s) | 0913 main Throughput (tok/s) | 0.27.1 Avg TTFT (ms) | 0913 main Avg TTFT (ms) |
|---|---|---|---|---|---|---|
| 1 | 12.37 | 5.30 (−57.2%) | 83.3 | 183.3 (+120.0%) | 2262.9 | 376.3 (−83.4%) |
| 4 | 23.67 | 10.50 (−55.6%) | 166.7 | 416.7 (+150.0%) | 2314.9 | 640.5 (−72.3%) |
| 16 | 55.90 | 22.17 (−60.3%) | 258.3 | 725.0 (+180.6%) | 7601.1 | 1121.0 (−85.3%) |

## End-to-end optimization examples

### Adaptive scheduling budget

Low request counts left much of `max_num_batched_tokens`

unused. [PR #51725](https://github.com/vllm-project/vllm/pull/51725): adaptive scheduled-token budget. [PR #51726](https://github.com/vllm-project/vllm/pull/51726): default limit from 8,192 to 16,384 for the high-memory GPU tier. On the reported 8K/1K workload: TTFT down 55%–65%, throughput up to 41.5%.

Let's consider `max_num_seqs=1024`

, `max_num_batched_tokens=8192`

, and `K=8`

:

| Actual Request num | Old logic scheduled tokens | Now |
|---|---|---|
| 1 | 1024 (8192 - 1024 * (8-1)) | 8185 (8192 - 7) |
| 32 | 1024 | 7968 |
| 128 | 1024 | 7296 |
| 1024 | 1024 | 1024 |

The PR makes the scheduled tokens much larger when request count is small by using an adaptive strategy, so one request won't be split to multiple forward calls.

### Internal KDA prefix checkpoints

The Mamba-style prefix cache split prefill at the last cacheable block boundary, sometimes adding a full-model pass for a short suffix. [PR #52789](https://github.com/vllm-project/vllm/pull/52789): checkpoint export inside one prefill pass, TTFT down 9%–25%. [PR #53614](https://github.com/vllm-project/vllm/pull/53614): partial prefix hits and speculative decoding, including EAGLE replay-boundary alignment.

For an 8K input:

This PR helps us avoid a second full-model pass through attention, MoE, routing, and TP collectives.

### Zero-copy mixed KDA batches

Mixed speculative and non-speculative batches used six `index_select`

and two `index_copy_`

operations per layer. [PR #56159](https://github.com/vllm-project/vllm/pull/56159): contiguous zero-copy slices and direct output writes. Throughput up 5.2%–7.7% at concurrency 4 and 16; batch size 1 flat.

### Deferred MXFP4 finalization

[PR #53152](https://github.com/vllm-project/vllm/pull/53152): MXFP4 top-k finalization inside the latent-tail kernel; one launch and one intermediate tensor write/read removed. End-to-end latency down roughly 5%. [PR #53327](https://github.com/vllm-project/vllm/pull/53327): initialization-order fix, enabling the deferred path before weight loading.

This removes one kernel launch and avoids writing and rereading the finalized intermediate tensor.

## ReplaySSM: reconstruct the KDA state instead of storing it

Speculative decoding writes a KDA recurrent state at every draft position so rejected tokens can be rolled back. For T draft positions, that means T extra state writes per step. [ReplaySSM](https://dao-lab.ai/blog/2026/replayssm/) buffers recent SSM inputs instead and reconstructs the accepted state at commit. Rollback only moves a buffer pointer.

[PR #51855](https://github.com/vllm-project/vllm/pull/51855): ReplaySSM for Kimi K3 on Model Runner V2. One Triton kernel commits the accepted state and the next prefix-cache boundary in `align`

mode. At the same 46.48 GiB cache budget, effective capacity rises 10.97% under TP8 without accuracy hurt.

## Prefill/decode disaggregation and hybrid state offload

PD disaggregation and cache offload must transfer both MLA KV and KDA state. MLA KV is replicated across TP ranks; KDA state is sharded by head and dimension. Mamba `align`

block tables can also be sparse and mutable. Pure-attention transfer assumptions do not apply.

[PR #51358](https://github.com/vllm-project/vllm/pull/51358): Mooncake stores the boundary states selected by the scheduler and pins them until asynchronous writes finish on every rank. [PR #50344](https://github.com/vllm-project/vllm/pull/50344): only connectors that can restore KDA state may serve divergent per-group prefix hits.

## Decode context parallelism

TP replicates MLA latent KV on every rank, so adding TP ranks does not increase KV-cache capacity. [Decode context parallelism](https://vllm.ai/blog/2026-08-07-decode-context-parallelism) shards it along the sequence dimension, useful for long shared-prefix [agentic workloads](https://vllm.ai/blog/2026-09-08-vllm-agentx).

[PR #50484](https://github.com/vllm-project/vllm/pull/50484): DCP for Kimi K3's fused MLA path. Symmetric-memory A2A handles output/LSE reduction; NVLS multicast gathers queries; multimem gathers chunked-context KV. Query shards write directly into the consumer's final buffer. Query-exchange latency drops 10.4%–29.9% on 4×GB200.

On a 120k-token workload (114k shared prefix, 6k suffix, 400 output tokens), KV-cache capacity rises from 1.93M to 19.75M tokens. TPOT p50 drops from 13.8 ms to 10.5 ms at concurrency 1, and from 16.2 ms to 11.8 ms at concurrency 2. GSM8K: 96.97% with DCP8 vs. 96.21% with TP8; zero request errors.

## Beyond the examples

The wider effort covered memory layout, sequence and pipeline parallelism, KDA prefill and recurrent state, MLA, MoE, and GEMM. It sharded large projections and shared experts, reduced collectives and data movement, and tightened small-batch GPU paths. The complete PR list is tracked in [issue #50587](https://github.com/vllm-project/vllm/issues/50587).

Selected community PRs broadened the work: [Robert Shaw](https://github.com/robertgshaw2-redhat) and [Summer Yang](https://github.com/GirasoleY) added [DeepEPv2 with DeepGEMM MXFP4](https://github.com/vllm-project/vllm/pull/50478) and the [DCP support](https://vllm.ai#decode-context-parallelism) described above, while [Thien Tran](https://github.com/gau-nernst) developed [sequence-parallel GEMM paths](https://github.com/vllm-project/vllm/pull/52079). [Nick Hill](https://github.com/njhill) and [Xiaolong Xu](https://github.com/BabyDrangoner) tightened KDA prefill in [PR #51540](https://github.com/vllm-project/vllm/pull/51540) and [PR #52458](https://github.com/vllm-project/vllm/pull/52458). The full contributor group is credited below.

## Acknowledgments

[Benjamin Chislett](https://github.com/benchislett), [Bolin Sun](https://github.com/BolinSNLHM), [Dao Le](https://github.com/Dao007forever), [Duncan Moss](https://github.com/djmmoss), [Harris Nover](https://github.com/hnover-nv), [Julian Huang](https://github.com/huangzhilin-hzl), [Ming](https://github.com/mingg26), [Nick Hill](https://github.com/njhill), [Rebecca Lee](https://github.com/rebklee), [Robert Shaw](https://github.com/robertgshaw2-redhat), [Summer Yang](https://github.com/GirasoleY), [Thien Tran](https://github.com/gau-nernst), [Tyler Michael Smith](https://github.com/tlrmchlsmth), [Xiaolong Xu](https://github.com/BabyDrangoner), and [Yifan Qiao](https://github.com/ivanium) for their Kimi K3 PRs. Thanks to the reviewers, CI maintainers, benchmark owners, and hardware teams. We would also like to thank the [Novita AI](https://novita.ai/) team for sponsoring compute for some of the optimization efforts described in this post.
