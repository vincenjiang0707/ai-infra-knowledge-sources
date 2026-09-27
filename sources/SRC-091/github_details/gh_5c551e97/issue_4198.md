# [Issue #4198] [Feature][MP][EC] Add MP-mode encoder cache support for vLLM-Omni

source: https://github.com/LMCache/LMCache/issues/4198
state: open | updated: 2026-09-21T01:52:36Z
labels: stale

## 正文

**Is your feature request related to a problem? Please describe.**

LMCache currently provides encoder-cache support for vLLM through `LMCacheECConnector` and `ECCacheEngine`. This implementation can persist a single encoder-output tensor through LMCache storage backends, but it uses the in-process LMCache architecture.

LMCache MP mode is now the recommended deployment architecture, while MP-mode support for encoder cache is still missing. As a result, users cannot use the preferred LMCache architecture to share encoder outputs across serving processes or disaggregated workers.

This is relevant to [vLLM-Omni #3427](https://github.com/vllm-project/vllm-omni/issues/3427), which proposes sharing encoder embeddings in disaggregated omni-modality inference to avoid repeated multimodal encoder computation and transfer.

The existing multimodal MP work in [LMCache #4183](https://github.com/LMCache/LMCache/pull/4183) focuses on multimodal KV-cache key correctness and explicitly leaves MP encoder-cache support as a separate effort.

**Describe the solution you'd like**

Add an MP-native encoder-cache path to LMCache, initially targeting the single dense encoder-output tensor already supported by `ECCacheEngine`.

A proposed first phase would include:

- MP client/server operations for encoder-cache lookup, load, and store;
- transfer of variable-shaped encoder tensors through the existing MP transport and storage architecture;
- reuse of LMCache storage backends and EC-specific resource configuration;
- cache-key isolation across incompatible model, encoder, preprocessing, schema, and dtype configurations;
- well-defined hit, miss, duplicate-store, error, and lifecycle behavior;
- unit and integration tests covering store, lookup, and load across separate processes.

The LMCache MP encoder-cache service should remain independent of vLLM-Omni model semantics. The engine-specific adapter should be responsible for translating vLLM-Omni metadata and encoder outputs into the LMCache contract.

The intended ownership boundary is:

- vLLM-Omni owns model hooks, scheduler integration, and the decision of which encoder artifacts to cache;
- LMCache owns the MP cache protocol, tensor transport, storage, key compatibility, and cache lifecycle.

For the first phase, I suggest keeping the existing single-tensor EC contract. Support for tensor trees, voice-reference artifacts, or other model-specific structures can be evaluated separately once the basic MP path is validated.

This proposal does not include SGLang-Omni integration or changes to multimodal KV-cache key computation.

**Describe alternatives you've considered**

1. Continue using the existing in-process `ECCacheEngine`.

This supports persistent encoder caching, but it does not align with LMCache's recommended MP deployment model and does not provide a shared MP service boundary.

2. Implement a storage backend directly inside vLLM-Omni.

This may work for a single backend, but it would duplicate functionality already provided by LMCache, including storage configuration, eviction, observability, and remote backend support.

3. Extend the existing MP KV-cache protocol without defining an EC contract.

Encoder outputs have different shapes, keys, access patterns, and lifecycle requirements from paged KV cache. Treating them as KV-cache chunks would make the interface and resource accounting difficult to reason about.

**Additional context**

Relevant references:

- [LMCache Q3 roadmap #4025](https://github.com/LMCache/LMCache/issues/4025)
- [LMCache encoder-cache design](https://github.com/LMCache/LMCache/blob/dev/docs/design/v1/encoder-cache.md)
- [vLLM-Omni encoder embedding sharing RFC #3427](https://github.com/vllm-project/vllm-omni/issues/3427)
- [LMCache multimodal MP cache-key PR #4183](https://github.com/LMCache/LMCache/pull/4183)

This issue is intended to complement vLLM-Omni #3427 rather than duplicate its model-side work.

If this direction and initial scope make sense, I would be interested in implementing the LMCache-side MP foundation and coordinating with the vLLM-Omni RFC on the integration contract.

## 评论 (5)

### DongDongJu · 2026-07-22

Let me work on this today

### Ternura143 · 2026-07-22

Hi @DongDongJu, thanks! Is there any part of this work I can help with?

I also realized that SGLang-Omni is in a different situation from vLLM-Omni: it has local encoder-output caches in some model pipelines, but I have not found an explicit upstream requirement or interface for sharing them through an external cache such as LMCache. In contrast, vLLM-Omni already has #3427 proposing shared encoder embeddings for disaggregated serving. Do you have any advice on how we should approach the SGLang-Omni side? Should we first discuss the need with its maintainers, or keep this work focused on vLLM-Omni for now?

### DongDongJu · 2026-07-22

> Hi [@DongDongJu](https://github.com/DongDongJu), thanks! Is there any part of this work I can help with?
> 
> I also realized that SGLang-Omni is in a different situation from vLLM-Omni: it has local encoder-output caches in some model pipelines, but I have not found an explicit upstream requirement or interface for sharing them through an external cache such as LMCache. In contrast, vLLM-Omni already has [#3427](https://github.com/LMCache/LMCache/pull/3427) proposing shared encoder embeddings for disaggregated serving. Do you have any advice on how we should approach the SGLang-Omni side? Should we first discuss the need with its maintainers, or keep this work focused on vLLM-Omni for now?

Hello @Ternura143, we can do one by one. lets focus on vllm-omni first and move on to the next one. 
I think we need to discuss with sglang side's maintainer first.

### Ternura143 · 2026-07-22

Hi @DongDongJu , sounds good, thanks! Please let me know if there’s anything I can help with :)

### github-actions[bot] · 2026-09-21

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
