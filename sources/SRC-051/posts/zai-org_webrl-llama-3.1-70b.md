# zai-org/webrl-llama-3.1-70b

source: https://huggingface.co/zai-org/webrl-llama-3.1-70b

---
license: other
language:
- en
base_model:
- meta/Llama-3.1-70B
tags:
- webrl
- llama3.1
- webarena-lite
- llm
- agent
---


# WebRL-Llama-3.1-70B


## Model Introduction
WebRL-Llama-3.1-70B is the open-source version of WebRL in Llama-3.1-70B released by Zhipu AI.
It has the ability to complete web operations on five websites in WebArena: OpenStreetMap (Map), Reddit, GitLab, online store content management system (CMS) and OneStopShop (OSS).


## Evaluation Results


We evaluated the WebRL-Llama-3.1-70B model on WebArena-Lite and obtained the following results:


| Model               | Reddit | Gitlab | CMS | Map | OSS | Avg.SR  |
|:--------------------|:------:|:------:|:------:|:------:|:------:|:--------:|
| Llama-3.1-8B-Instruct |     0.0      |   3.3   | 2.9  | 3.3 | 11.1 |  4.8  |
| Llama-3.1-70B-Instruct |     10.5      |   16.7   | 17.1  | 20.0 | 4.4 |  12.7  |
| WebRL-Llama-3.1-70B      |     78.9     |   50.0  |  54.3 | 40.0 | 44.4  |  49.1 |


**For more inference code and requirements, please visit our [github page](GitHub - THUDM/WebRL).**


## Citations


If you find our work useful, please consider citing the following paper.


```
@artical{qi2024webrl,
      title={WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning}, 
      author={Zehan Qi and Xiao Liu and Iat Long Iong and Hanyu Lai and Xueqiao Sun and Xinyue Yang and Jiadai Sun and Yu Yang and Shuntian Yao and Tianjie Zhang and Wei Xu and Jie Tang and Yuxiao Dong},
      journal={arXiv preprint arXiv:2411.02337},
      year={2024},
}
```
