# [Issue #1817] Implement BucketServe-style bucket-based dynamic batching in AIBrix

source: https://github.com/vllm-project/aibrix/issues/1817
state: open | updated: 2026-09-24T01:44:37Z
labels: area/gateway

## 正文

### 🚀 Feature Description and Motivation

The recent paper “BucketServe: Bucket-Based Dynamic Batching for Smart and Efficient LLM Inference Serving” proposes a bucket-based dynamic batching framework built on vLLM, designed to handle heterogeneous sequence lengths and mixed workloads. It groups requests into sequence-length–homogeneous buckets, dynamically splits/merges buckets, and chooses batch sizes based on GPU memory constraints to avoid OOM while improving throughput and SLO attainment


Implementing a BucketServe-style bucketizer in the AIBrix gateway would:
- Reduce padding overhead for mixed short/long prompts.
- Improve GPU utilization under heterogeneous workloads and high concurrency.
- Provide a clean interface to plug in SLO-aware scheduling (e.g., “RPS mode” vs “throughput mode”).

But this is not just gateway works, we need to make sure underneath deployment have different configuration as well, aligned with autoscaling settings.


Reference

BucketServe: Bucket-Based Dynamic Batching for Smart and Efficient LLM Inference Serving https://arxiv.org/abs/2507.17120

### Use Case

reduce cost and improve throughput

### Proposed Solution

_No response_

## 评论 (2)

### zhixian82 · 2026-05-27

Hi，Could you share the current plan or expected timeline for this issue?

### bolubo · 2026-09-24

Hi @Jeffwan, I'd like to take the gateway-side part of this.

The issue spans the gateway, deployment config and autoscaling, so I would keep the first pass to the gateway and build on what is already in the tree: the static prompt-length bucketing (bucket ranges declared in the model config profile, plus the `PromptLengthBucketing` profile knob from #2786). On top of that, the v1 would add the dynamic pieces from the paper at the routing layer: bucket ranges that adapt as traffic shifts (split/merge), the RPS vs throughput mode switch for SLO-aware routing, and metrics that make the behavior observable.

Out of scope for the first pass: autoscaling and any engine or deployment configuration changes. I will not assume them in the gateway design, and the engine-side batching work stays open for follow-ups.

If you had a different split in mind for the gateway side, happy to adjust before I open the PR.
