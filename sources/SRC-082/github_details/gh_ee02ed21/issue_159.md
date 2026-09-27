# [Issue #159] KeyError: 'llava_llama'

source: https://github.com/mit-han-lab/llm-awq/issues/159
state: open | updated: 2026-02-08T12:28:48Z
labels: 

## 正文

When I ran vila's demo, I ran into the bug below：
![image](https://github.com/mit-han-lab/llm-awq/assets/101184592/6ceea783-2b53-4af0-a77c-a71339bb4ad2)


## 评论 (3)

### ocg2347 · 2024-03-15

I imagine you missed a step during VILA installation:
`cp -rv ./llava/train/transformers_replace/* ~/anaconda3/envs/vila/lib/python3.10/site-packages/transformers/models/`
Source: README/Installation @ https://github.com/Efficient-Large-Model/VILA


### surfingnirvana · 2025-05-16

It is not there anymore.

### ZhangJinghe-AI · 2026-02-08

@huzicong Have you solved this problem？
