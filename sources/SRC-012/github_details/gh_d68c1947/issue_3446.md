# [Issue #3446] [Tracking] Multi-LoRA Serving

source: https://github.com/mlc-ai/mlc-llm/issues/3446
state: open | updated: 2026-05-23T08:56:52Z
labels: status: tracking

## 正文

<!--

A tracking issue contains a list of action items
that can be executed to complete a feature or fix.

We use tracking issues when we have a clear list of action items
related to feature items as they provide fine-grained
view of action items and provide clarity on what it takes to implement a feature.

When to open a tracking issue: Open a new tracking issue when you have
clear, actionable items (as a rule of thumb, make sure action items
items can be carried through if you are assigned to work on it and
you can provide enough guides to others who plan to work on these actions).
-->


## Overview
<!-- A brief overview of the task  -->
Adding proper Multi-LoRA serving.

*from old discussion thread*

These are the two important works that established Multi-LoRA serving:

S-LoRA: [blog](https://lmsys.org/blog/2023-11-15-slora/), [paper](https://arxiv.org/abs/2311.03285)
Punica: [paper](https://arxiv.org/pdf/2310.18547).
S-LoRA leverages memory paging / memory pool to manage the memory pressure of adapters, and extends the idea of Paged KV Caching. We already use a Paged KV Cache from TVM upstream, so this is a good place to start.

Punica introduces the SGMV kernel. It takes a single large input tensor (the hidden states for the whole batch, then, it uses a "segment" vector to define which rows belong to which request. In a single GPU kernel launch, it "gathers" the specific weights for each segment and performs the correct low-rank multiplication across the whole batch. I'm not an expert here, so I'd refer to the paper for details.

I would first start by reading these two resources, understanding them deeply, and then circling back. In my opinion, it would be smart to first figure out how S-LoRA can work by itself - we do not need Punica kernels for correctness, they are more for compute efficiency (ie. it's ok to launch N small kernels rather than fuse using SGMV operation, it just underutilizes the chip). As such, let's see if we can get just S-LoRA working, and then if that passes, then we move to Punica style integration.

The implementation of S-LoRA (IMO) will almost certainly require an upstream patch to TVM, to implement interfacing with the page pool to handle the adaptor weights. You'll also have to think about how to structure the forward linear pass to integrate aggregating the correct adaptor weight for each request in the batch.

In case you haven't explored the TVM codebase as much, these are the four files that are mostly relevant to the KV Cache.
[kv_cache.py](https://github.com/apache/tvm/blob/main/python/tvm/relax/frontend/nn/llm/kv_cache.py)
[kv_cache.cc](https://github.com/apache/tvm/blob/main/src/runtime/vm/paged_kv_cache.cc)
[kv_state.cc](https://github.com/apache/tvm/blob/main/src/runtime/vm/kv_state.cc)
[kv_state.h](https://github.com/apache/tvm/blob/main/src/runtime/vm/kv_state.h)

I imagine you might need to add a dedicated LoraPagePool or something within the KV Cache construct that allows fetching the LoRA weights given some adapter ID. This will definitely be upstream.

In our repository, you'll have to add indirection in our relax graph to where the linear layers trigger an adapter fetch if they are associated with the LoRA, and request the adapter with the aforementioned adapter ID.

I'm not perfectly sure that the PagedKVCache is the right construct for this, but the S-LoRA paper does use a unified pool for both adaptors and KV Cache.


## Action Items
<!-- Please list set of action items to complete -->

PR 1: Upstream patch to TVM to adjust the runtime KV_Cache (Cpp layer) as well as python bindings to extend the PagedKVCache to support LoraPool in the same way S-LoRA does. This is a good scope for a single PR.

PR 2: Leverage patch from PR 1 to update MLC-side plumbing, and make sure linear ops fetch the right adaptor at runtime. Don't worry about getting mixed-adapter batching working immediately at this stage - assume they are still serving one LoRA, just without the easy PEFT path. The goal here is to verify that the S-LoRA implementation works in the easy case when num_adaptors=1. You can add defensive checks against trying multi-adapter at this stage.

PR 3: Simple multi-adaptor support. Basically get num_adaptors to go beyond 1. No need for Punica Kernels yet - we can tolerate the gather inefficiency.

PR 4: Add Punica kernels if you can to maximize our efficiency. This isn't like strictly needed for multi-lora serving, but I think it would be good to have to make us truly efficient.

## Links to Related Issues and PRs

<!-- Cross link feature requests bug report issues related to the tracking item -->
<!-- When there are new PRs, open up new PRs -->

Old Discussion thread / PR
https://github.com/mlc-ai/mlc-llm/pull/3281

## 评论 (4)

### babusid · 2026-03-06

Our Community Contributor @MagellaX has been working on this effort

### babusid · 2026-03-06

@MagellaX Whenever you open any PR related to this effort, please link it here / link this issue there. That will make it easier for me to keep an eye on things.

### babusid · 2026-03-10

Did a bit more of a scan into S-LoRA, looks like S-LoRA itself introduced additional kernels necessary to support the effort. Just something to keep an eye on @MagellaX. 

### MagellaX · 2026-05-23

Hey @MasterJH5574, I wanted to talk to you, can we talk? do you have a Calendly?
