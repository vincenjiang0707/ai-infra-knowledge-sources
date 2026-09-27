# [Issue #3458] [Model Request] Nemotron-3-nano-4b

source: https://github.com/mlc-ai/mlc-llm/issues/3458
state: open | updated: 2026-03-27T11:03:48Z
labels: new-models

## 正文

## ⚙️  Request New Models

- Link to an existing implementation (e.g. Hugging Face/Github): https://huggingface.co/blog/nvidia/nemotron-3-nano-4b
- Is this model architecture supported by MLC-LLM? (the list of [supported models](https://llm.mlc.ai/docs/prebuilt_models.html)) Yes

## Additional context

> Nemotron 3 Nano 4B: A Compact Hybrid Model for Efficient Local AI

<img width="1622" height="589" alt="Image" src="https://github.com/user-attachments/assets/cef9f05d-cadb-46c2-8fde-824cb08100dd" />

It hallucinates far less than Qwen3/3.5 in thinking mode.
Thank you for maintaining this amazing project!

## 评论 (4)

### OmarAzizi · 2026-03-26

Hi @XomaDev, thanks for sharing the reference! I've started working on this, and I’ll be opening a PR soon.

### XomaDev · 2026-03-26

Thanks!! @OmarAzizi All the best! 👍🏻 

### OmarAzizi · 2026-03-27

Hi @XomaDev, the PR is open at #3464. full pipeline tested (convert -> compile -> chat). I would love to hear how it runs on your end, since I only had a CPU to test with.

### XomaDev · 2026-03-27

Hello @OmarAzizi, I apologise, but I am unable to test it with a GPU. I will try again compiling using those commands on a CPU and will let you know if I succeed. Thank you.
