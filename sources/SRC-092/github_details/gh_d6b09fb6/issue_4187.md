# [Issue #4187] [Feature Request]: Is there any plan to release official pre-built Docker images for Ascend NPU (910b/950)?

source: https://github.com/kvcache-ai/Mooncake/issues/4187
state: open | updated: 2026-09-22T01:46:33Z
labels: 

## 正文

### Describe your feature request

## Question
I would like to ask whether the Mooncake team has a plan to release official pre-built Docker images for Ascend NPU (910b / 950).

### Background
Mooncake already supports compiling with `-DUSE_ASCEND_DIRECT=ON` to enable AscendDirectTransport.
Currently, the repository only provides Dockerfile for CUDA.
For Ascend users, we need to manually build the image from source every time. It is challenging to keep CANN version, driver and all dependencies aligned.

thanks a lot

### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (2)

### github-actions[bot] · 2026-09-17

Thanks for opening this issue, @gitgaoqian!

| Field | Value |
|-------|-------|
| **Issue** | #4187 |
| **GitHub user ID** | `33947447` |
| **Reporter** | @gitgaoqian |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ascend-direct-dev · 2026-09-22

Thanks for the question.

Mooncake itself does not currently plan to publish a separate official Ascend NPU image. For Ascend deployments we recommend using the **Ascend official images maintained by the inference frameworks**, which already bundle the needed CANN / driver alignment (and Mooncake where applicable):

### vLLM Ascend
Use the prebuilt images from [`quay.io/ascend/vllm-ascend`](https://quay.io/repository/ascend/vllm-ascend) — they ship vLLM + CANN + Mooncake. Docs: [vLLM Ascend Quick Start](https://docs.vllm.ai/projects/ascend/en/latest/getting_started/quick_start.html).

```bash
# pick a tag that matches your device / release
docker pull quay.io/ascend/vllm-ascend:<TAG>
```

### SGLang Ascend
Use the Ascend NPU images from [`quay.io/ascend/sglang`](https://quay.io/repository/ascend/sglang). Docs: [SGLang Ascend installation](https://docs.sglang.io/docs/hardware-platforms/ascend-npus/getting-started/installation).

```bash
# examples (stable tags; choose A2/A3 as needed)
docker pull quay.io/ascend/sglang:cann9.0.0-910b-v0.5.16   # Atlas 800I A2
docker pull quay.io/ascend/sglang:cann9.0.0-a3-v0.5.16     # Atlas 800I A3
```

If you specifically need a standalone Mooncake build for development, building from source with `-DUSE_ASCEND_DIRECT=ON` remains the supported path; for production inference stacks, prefer the framework Ascend images above.
