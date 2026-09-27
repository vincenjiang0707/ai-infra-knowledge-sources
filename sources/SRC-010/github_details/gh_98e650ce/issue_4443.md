# [Issue #4443] [Feature] Integrate Mooncake Transfer Engine with TurboMind for PD disaggregation and remote KV

source: https://github.com/InternLM/lmdeploy/issues/4443
state: open | updated: 2026-03-26T04:50:53Z
labels: 

## 正文

### Motivation

Motivation

LMDeploy already provides PD disaggregation (DistServe) on the PyTorch engine via lmdeploy/pytorch/disagg/, with Mooncake as an optional KV migration backend (MooncakeBackend, using the Python mooncake.engine.TransferEngine).

TurboMind (C++) remains a high-performance path, but it is not integrated with Mooncake today, so Prefill/Decode split deployments cannot reuse TurboMind's paged KV and kernel stack for cross-node KV.

We would like to integrate Mooncake's Transfer Engine (or an equivalent C++ SDK) into TurboMind's C++ layer to:

- Align block lifecycle with SequenceManager / BlockManager (including optional prefix caching and consistent KV quantization layout);
- Asynchronously export KV after prefill on the prefill side, asynchronously pull on the decode side, and overlap transfer with compute;
- Align or stay compatible with Conductor / metadata protocols used on the PyTorch side to avoid diverging semantics.

Goal: enable end-to-end Mooncake-based PD disaggregation on TurboMind with minimal impact on throughput.

Related resources

- In-repo: lmdeploy/pytorch/disagg/backend/mooncake.py, lmdeploy/pytorch/disagg/config.py (MooncakeEngineConfig, MigrationBackend)
- Mooncake: https://github.com/kvcache-ai/Mooncake
- TurboMind pointers: src/turbomind/models/llama/SequenceManager.*, BlockManager.*, src/turbomind/engine/engine.cc and request/scheduling code

Additional context

- Current state: Mooncake PD disaggregation is implemented for PyTorch; TurboMind has no Mooncake / disagg integration.
- Challenges: block/chunk mapping between TurboMind and Mooncake, KV sharding under attn_tp / attn_cp, and scheduling/state machine when waiting for remote KV.
- Suggested phases: optional CMake dependency -> metadata/RPC -> memory transfer hooks -> two-machine e2e validation.

One-liner 

PyTorch engine supports PD disaggregation and KV migration via Mooncake (and DLSlime); TurboMind does not yet support Mooncake-based PD disaggregation.

### Related resources

_No response_

### Additional context

_No response_

## 评论 (5)

### Dayuxiaoshui · 2026-03-21

@lvhan028 

### windreamer · 2026-03-21

Hi @Dayuxiaoshui ,

Thanks for your insights of P/D  disaggregation for TurboMind. May I know if you are interested in contributing this feature or asking the contributors to implement this feature?

As far as I know, P/D disaggregation for TurboMind is not just a simple adoption of Mooncake or some other framework. The key challenges lay in the management of distributed caches. I believe it requires significant and well-thought work to make the goal realized. It is definitely welcome if you have a solid solution and are planning to contribute since we are not investing on this in the next future.

### Dayuxiaoshui · 2026-03-21

@windreamer Thanks for the encouragement! I'm planning to tackle this by decomposing the task into three incremental phases—1. CMake & TENT C++ SDK integration, 2. Block-level metadata and state machine synchronization in SequenceManager, and 3. Asynchronous KV transfer overlapping with compute—and I will submit PRs for each stage to ensure a solid and reviewable implementation.

### lvhan028 · 2026-03-22

Hi, @Dayuxiaoshui Thank you very much for your proposal to integrate Mooncake's PD disaggregation functionality into TurboMind. This is definitely an interesting direction, and we truly appreciate you taking the time to bring it to the community.

We need some time to discuss this internally with the team to better understand the potential impact on the architecture, especially given the upcoming roadmap.

We'll get back to you with a more detailed response soon.

### lvhan028 · 2026-03-26

Hi, @Dayuxiaoshui Sorry for the late reply.

The TurboMind roadmap for the first half of 2026 focuses on the following priorities:
- Support for single-node and multi-node expert parallelism (EP);
- Native multi-modal model support in TurboMind;
- Speculative decoding.

Currently, PD disaggregation is not a priority for the TurboMind engine, and we do not have detailed design plans for this module in the near term.

We greatly welcome your contributions to implement this feature. However, since our team's efforts are fully dedicated to the roadmap items mentioned above, we may not be able to provide substantial support or timely feedback to you.

Thank you again for your understanding and interest in improving TurboMind.

cc @lzhangzz @irexyc 
