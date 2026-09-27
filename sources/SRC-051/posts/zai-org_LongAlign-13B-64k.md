# zai-org/LongAlign-13B-64k

source: https://huggingface.co/zai-org/LongAlign-13B-64k

---
language:
- en
- zh
library_name: transformers
tags:
- Long Context
- llama
datasets:
- THUDM/LongAlign-10k
pipeline_tag: text-generation
license: apache-2.0
---
# LongAlign-13B-64k

<p align="center">
  🤗 <a href="https://huggingface.co/datasets/THUDM/LongAlign-10k" target="_blank">[LongAlign Dataset] </a> • 💻 <a href="https://github.com/THUDM/LongAlign" target="_blank">[Github Repo]</a> • 📃 <a href="https://arxiv.org/abs/2401.18058" target="_blank">[LongAlign Paper]</a> 
</p>

**LongAlign** is the first full recipe for LLM alignment on long context. We propose the **LongAlign-10k** dataset, containing 10,000 long instruction data of 8k-64k in length. We investigate on trianing strategies, namely **packing (with loss weighting) and sorted batching**, which are all implemented in our code. For real-world long context evaluation, we introduce **LongBench-Chat** that evaluate the instruction-following capability on queries of 10k-100k length.

## All Models

We open-sourced the following list of models:

|Model|Huggingface Repo|Description|
|---|---|---|
|**LongAlign-6B-64k-base**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/LongAlign-6B-64k-base) | **ChatGLM3-6B** with an extended 64k context window |
|**LongAlign-6B-64k**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/LongAlign-6B-64k) | Chat model by LongAlign training on LongAlign-6B-64k-base|
|**LongAlign-7B-64k-base**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/LongAlign-7B-64k-base) | **Llama-2-7B** with an extended 64k context window |
|**LongAlign-7B-64k**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/LongAlign-7B-64k) | Chat model by LongAlign training on LongAlign-7B-64k-base|
|**LongAlign-13B-64k-base**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/LongAlign-13B-64k-base) | **Llama-2-13B** with an extended 64k context window |
|**LongAlign-13B-64k**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/LongAlign-13B-64k) | Chat model by LongAlign training on LongAlign-13B-64k-base|
|**ChatGLM3-6B-128k**| [🤗 Huggingface Repo](https://huggingface.co/THUDM/chatglm3-6b-128k) | **ChatGLM3-6B** with a 128k context window|

![](assets/leaderboard.png)

## Model usage
Chat prompt template for LongAlign-6B-64k:
```text
[Round 1]

问：Hi!

答：Hello! What can I assist you today?

[Round 2]

问：What should I do if I can't sleep at night?

答：
```
Chat prompt template for LongAlign-7B-64k and LongAlign-13B-64k:
```text
[INST]Hi![/INST]Hello! What can I assist you today?

[INST]What should I do if I can't sleep at night?[/INST]
```
ChatGLM3-6B-128k uses the same prompt template as [ChatGLM3-6B](https://huggingface.co/THUDM/chatglm3-6b).

A simple demo for deployment of the model:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
tokenizer = AutoTokenizer.from_pretrained("THUDM/LongAlign-6B-64k", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("THUDM/LongAlign-6B-64k", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
model = model.eval()
query = open("assets/paper.txt").read() + "\n\nPlease summarize the paper."
response, history = model.chat(tokenizer, query, history=[], max_new_tokens=512, temperature=1)
print(response)
```

## Citation

If you find our work useful, please consider citing LongAlign:

```

```
