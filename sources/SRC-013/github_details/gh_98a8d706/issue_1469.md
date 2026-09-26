# [Issue #1469] [P/D][AMD]: Support AMD MoRI-IO

source: https://github.com/llm-d/llm-d/issues/1469
state: open | updated: 2026-08-23T18:59:29Z
labels: enhancement, release/v0.8, amd

## 正文

### Feature Area

Prefill/Decode Disaggregation

### Problem Statement

Hi @powderluv @chunfangamd @andyluo7 @kenroche @vcave,

Right now the only AMD P/D disaggregation "well-lit" path in llm-d (#776 , https://github.com/andyluo7/llm-d/blob/main/guides/pd-disaggregation/README.amd.md) **ONLY** ships RIXL as the KV transfer engine. RIXL is second-class fork of NIXL. The "well-lit" RIXL AMD path does not have CI/CD either as tracked in https://github.com/llm-d/llm-d/issues/1468 

AMD's first class KVCache Transfer library is [**MoRI-IO**](https://github.com/ROCm/mori) yet it does not have an well lit path in AMD's `llm-d`

@simondanielsson is already trying to get MoRI-IO running in upstream vLLM native engine with vllm router tho there is additional work to get MoRI-IO to be well lit in `llm-d`

the `llm-d` ROCm do not work with MoRI-IO either on Pollara or Thor-2 NICs https://github.com/llm-d/llm-d/blob/main/docker/Dockerfile.rocm


### Proposed Solution

have well-lit path for MoRI-IO KVCache Transfer for AMD `llm-d`

### Alternatives Considered

_No response_

### Willingness to Contribute

No, but I can help test

### Additional Context

_No response_

## 评论 (11)

### vcave · 2026-05-11

The new kustomize-based structure makes it very easy to add configuration variants. Please ping @kenroche and @vcave to coordinate development and upstream.

### functionstackx · 2026-05-11

> The new kustomize-based structure makes it very easy to add configuration variants. Please ping [@kenroche](https://github.com/kenroche) and [@vcave](https://github.com/vcave) to coordinate development and upstream.

thanks for the reply @vcave it isnt part of the base image as ainic dependencies arent part of the build pipeline yet https://github.com/llm-d/llm-d/blob/46a675ddd2ffec46e60ecb014db0ef3cc8415cb8/docker/Dockerfile.rocm#L1

as https://github.com/vllm-project/vllm/pull/38371/changes only adds it as an optional dependency with ARG NIC_BACKEND set to none by default and vllm release pipeline doesnt set ARG NIC_BACKEND to any nic https://github.com/tjtanaa/vllm/blob/main/.buildkite/release-pipeline.yaml

it would be great if AMD had well lit path for end users for MoRI-IO +viz @andyluo7

### robertgshaw2-redhat · 2026-05-11

makes sense - welcome contribution of MORI-IO

@functionstackx - is MORI-IO built into the vllm/vllm-openai-rocm:v0.20.1 docker image?

Also, do you have any reference for the KV transfer protocol? We need to support it in the llm-d sidecar image

It would be good to have some understanding of how the MORI-IO connector works

https://github.com/llm-d/llm-d/tree/main/docs/architecture/advanced/disaggregation

What is your name on slack?

### functionstackx · 2026-05-11

> makes sense - welcome contribution of MORI-IO

hi @robertgshaw2-redhat thanks for the quick reply! i am discussing with AMD rn about this

> [@functionstackx](https://github.com/functionstackx) - is MORI-IO built into the vllm/vllm-openai-rocm:v0.20.1 docker image?

MoRI-IO (with the needed NIC userspace lib roce dependencies isnt in vllm/vllm-openai-rocm:v0.20.1  yet, still waiting for AMD @simondanielsson  to update the build pipeline)

> Also, do you have any reference for the KV transfer protocol? We need to support it in the llm-d sidecar image

the corresponding vllm connector PRs & vllm router PRs  in this vllm thread should be https://github.com/vllm-project/vllm/issues/38692#issuecomment-4280534784 would be an good start to understand the protocol


### functionstackx · 2026-05-11

> Also, do you have any reference for the KV transfer protocol? We need to support it in the llm-d sidecar image

looking at https://github.com/llm-d/llm-d/tree/main/docs/architecture/advanced/disaggregation it seems like it is not as easy as updating kustomize yaml but requires modifications to llm-d sidecar too since MoRI-IO connector is not exactly an 1 to 1 mapping to NIXL connector (as seem in the changes requires to vllm-router)

### simondanielsson · 2026-05-12

> Also, do you have any reference for the KV transfer protocol? We need to support it in the llm-d sidecar image

The best reference is probably https://github.com/vllm-project/router/pull/138 and https://github.com/vllm-project/router/pull/157, and MoRI's protocol (in READ mode) is very similar to the P2pNcclConnector. In WRITE mode it requires concurrent dispatch which resembles the sglang sidecar: https://github.com/llm-d/llm-d-inference-scheduler/blob/e4b2f70031a4088d804cab4b4acea04ccaa214f2/pkg/sidecar/proxy/connector_sglang.go#L85. 

> looking at https://github.com/llm-d/llm-d/tree/main/docs/architecture/advanced/disaggregation it seems like it is not as easy as updating kustomize yaml but requires modifications to llm-d sidecar too since MoRI-IO connector is not exactly an 1 to 1 mapping to NIXL connector (as seem in the changes requires to vllm-router)

My understanding is aligned with @functionstackx. We likely need another sidecar connector implementation which will be a mix of the sglang and nixlv2 connectors.

This is on my priority list to assist with once MoRI support in vllm-router is stabilized.

cc: @mpashkovskii

### robertgshaw2-redhat · 2026-05-16

assigning to @shikamd123 and @vcave 

### shikamd123 · 2026-05-18

Working on this

### github-actions[bot] · 2026-08-22

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.

### functionstackx · 2026-08-23

.

### shikamd123 · 2026-08-23

Please do not close this issue, due to internal logistics, it is being tested in internal CI system first.
