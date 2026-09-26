# [Issue #1] Missing LICENSE file

source: https://github.com/NVlabs/kda/issues/1
state: closed | updated: 2026-09-10T09:57:55Z
labels: 

## 正文

This repository does not include a LICENSE file. Without one, the code defaults to "all rights reserved," which prevents external users from legally forking, modifying, or redistributing the prompts and verification script.

Other MIT HAN Lab repositories use MIT (`streaming-llm`, `llm-awq`, `temporal-shift-module`) or Apache-2.0 (`efficientvit`, `bevfusion`).

Would you be open to adding a license? Happy to open a PR if you let me know which one you prefer.

## 评论 (1)

### Lyken17 · 2026-09-10

KDA has been transferred to NVLabs as part of NVIDIA's agentic CUDA & RSI efforts.

We will use
> Except for the third-party submodules identified above, first-party documentation, prompts, skills-style content, and assets are licensed under the [Creative Commons Attribution 4.0 International License](https://github.com/NVlabs/kda/blob/main/LICENSE), and first-party source code is licensed under the [Apache License 2.0](https://github.com/NVlabs/kda/blob/main/LICENSE).

for the project license.
