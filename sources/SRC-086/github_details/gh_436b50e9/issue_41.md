# [Issue #41] vLLM support

source: https://github.com/FasterDecoding/Medusa/issues/41
state: open | updated: 2024-09-29T08:28:07Z
labels: 

## 正文

(empty)

## 评论 (12)

### Data-drone · 2023-10-11

Are there any updates on this one?

### louisoutin · 2023-10-16

+1

### ruidongtd · 2023-10-23

+1

### insist93 · 2023-11-03

+1

### leonardxie · 2023-11-30

+1

### TexasRangers86 · 2023-12-18

+1

### Lvjinhong · 2023-12-20

So, could you provide advice so that I can make custom modifications on vLLM myself (llama2 70b)?

### RonanKMcGovern · 2023-12-21

fwiw, i know this is about vLLM, but you can run medusa on tgi using --speculate 3

### TexasRangers86 · 2023-12-26

> fwiw, i know this is about vLLM, but you can run medusa on tgi using --speculate 3

hello，how can I pass medusa model and base model args when I use medusa on tgi. 

### RonanKMcGovern · 2023-12-26

> > fwiw, i know this is about vLLM, but you can run medusa on tgi using --speculate 3
> 
> hello，how can I pass medusa model and base model args when I use medusa on tgi.

Just pass the medusa model repo (as you would with any other model) and then add on `--speculate 2`

You can try this template: https://runpod.io/gsc?template=2xpg09eenv&ref=jmfkcdio


### TexasRangers86 · 2023-12-26

Thanks a lot !!!!

### chuangzhidan · 2024-09-29

how to use medusa based on vllm or sglang?
