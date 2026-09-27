# zai-org/BPO

source: https://huggingface.co/zai-org/BPO

---
language:
- en
tags:
- bpo
- llama
- thudm
inference: false
---

<h1>Black-Box Prompt Optimization: Aligning Large Language Models without Model Training</h1>

- **Repository:** https://github.com/thu-coai/BPO
- **Paper:** https://arxiv.org/abs/2311.04155
- **Data:** https://huggingface.co/datasets/THUDM/BPO

# Black-box Prompt Optimization (BPO)
BPO is a black-box alignment technique that differs from training-based methods (like PPO or DPO). BPO only requires training of a plug-and-play model and optimizes LLMs through optimizing user inputs. Therefore, it can be used on a variety of open-source or API-based LLMs.

## Model Details

### Data
Prompt优化模型由隐含人类偏好特征的prompt优化对训练得到，数据集的详细信息在这里。
The Prompt Optimization Model is trained on prompt optimization pairs which contain human preference features. Detailed information on the dataset can be found [here](https://huggingface.co/datasets/CCCCCC/BPO).

### Backbone Model
The prompt preference optimizer is built on `Llama-2-7b-chat-hf`.

### Language
English

### Performance


| Model A| Model B | A win | tie | B win |
|-------------|-------------|----|----|----|
| gpt-3.5-turbo + BPO | gpt-3.5-turbo | **60.0** | 8.7 | 31.3 |
| claude-2 + BPO | claude-2 | **57.5** | 5.0 | 37.5 |
| llama-2-13b-chat + BPO | llama-2-70b-chat | **61.3** | 0.0 | 38.7 |
| vicuna-13b + BPO | vicuna-13b + PPO | **52.5** | 3.7 | 43.7  |
| vicuna-13b + BPO | vicuna-13b + DPO | **53.8** | 2.5 | 43.7 |
| vicuna-13b + DPO + BPO | vicuna-13b + DPO | **60.0** | 2.5 | 37.5 |

## Intended Use

### Prompt Template 
We adopt a prompt template as 
```
[INST] You are an expert prompt engineer. Please help me improve this prompt to get a more helpful and harmless response:\n{user prompt} [/INST]
```

### Inference code
Here is an example code for inference: 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = 'Your-Model-Path'

prompt_template = "[INST] You are an expert prompt engineer. Please help me improve this prompt to get a more helpful and harmless response:\n{} [/INST]"

model = AutoModelForCausalLM.from_pretrained(model_path).cuda()
tokenizer = AutoTokenizer.from_pretrained(model_path)

text = 'Tell me about Harry Potter'

prompt = prompt_template.format(text)
model_inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")
output = model.generate(**model_inputs, max_new_tokens=1024, do_sample=True, top_p=0.9, temperature=0.6, num_beams=1)
resp = tokenizer.decode(output[0], skip_special_tokens=True).split('[/INST]')[1].strip()

print(resp)
```
See our [Github Repo](https://github.com/thu-coai/BPO/blob/main/src/infer_example.py) for more detailed usage (e.g. more aggressive optimization).


### Other Known Limitations
- Task coverage is not sufficient, as we only used open-source data to get about 14k optimized prompts. Clearly, it is impossible to cover a wide range of user queries, so the current model may not perform well on every prompt.
- Due to the small ratio of long-context-based tasks and mathematical problems, the prompt optimizer underperforms when dealing with these tasks.

## Citation
If you find our model is useful in your work, please cite it with:
```
@article{cheng2023black,
  title={Black-Box Prompt Optimization: Aligning Large Language Models without Model Training},
  author={Cheng, Jiale and Liu, Xiao and Zheng, Kehan and Ke, Pei and Wang, Hongning and Dong, Yuxiao and Tang, Jie and Huang, Minlie},
  journal={arXiv preprint arXiv:2311.04155},
  year={2023}
}
```
