# [Issue #225] How to train eagle3 and support qwen2

source: https://github.com/SafeAILab/EAGLE/issues/225
state: closed | updated: 2025-06-23T04:20:02Z
labels: 

## 正文

How can we train eagle3 and support qwen2? We want to implement it in our business, but we didn't find any code for training eagle3 in the project.

## 评论 (13)

### ravi03071991 · 2025-05-13

The `cnets.py` file [here](https://github.com/SafeAILab/EAGLE/tree/main/eagle/model) caters to `eagle3` model training and `cnets1.py` for `eagle1/2` model training. We can adjust our scripts accordingly.

### skylee-01 · 2025-05-13

> The `cnets.py` file [here](https://github.com/SafeAILab/EAGLE/tree/main/eagle/model) caters to `eagle3` model training and `cnets1.py` for `eagle1/2` model training. We can adjust our scripts accordingly.

How to adapt the Qwen2 model? I didn't find the script for training Qwen2.

### ravi03071991 · 2025-05-13

> > The `cnets.py` file [here](https://github.com/SafeAILab/EAGLE/tree/main/eagle/model) caters to `eagle3` model training and `cnets1.py` for `eagle1/2` model training. We can adjust our scripts accordingly.
> 
> How to adapt the Qwen2 model? I didn't find the script for training Qwen2.

Yeah, so I think you need to change some parts of the `cnets.py` / `cnets1.py` file to adapt to Qwen2 by taking a closer look at the [qwen2 modeling file](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen2/modeling_qwen2.py).

### skylee-01 · 2025-05-14

> > > The `cnets.py` file [here](https://github.com/SafeAILab/EAGLE/tree/main/eagle/model) caters to `eagle3` model training and `cnets1.py` for `eagle1/2` model training. We can adjust our scripts accordingly.
> > 
> > 
> > How to adapt the Qwen2 model? I didn't find the script for training Qwen2.
> 
> Yeah, so I think you need to change some parts of the `cnets.py` / `cnets1.py` file to adapt to Qwen2 by taking a closer look at the [qwen2 modeling file](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen2/modeling_qwen2.py).

Thank you for your reply      

### cailinhang · 2025-05-16

> The `cnets.py` file [here](https://github.com/SafeAILab/EAGLE/tree/main/eagle/model) caters to `eagle3` model training and `cnets1.py` for `eagle1/2` model training. We can adjust our scripts accordingly.

If I want to  train egale2 model for qwen2.5-7b-instruct, should I  modify the `cnets1.py`  or not ?  I think that  `cnets1.py`   already supports qwen2 models beacause we can inference  with the author provided eagle2 of qwen2-7b-instruct. 

### skylee-01 · 2025-05-17





> > The `cnets.py` file [here](https://github.com/SafeAILab/EAGLE/tree/main/eagle/model) caters to `eagle3` model training and `cnets1.py` for `eagle1/2` model training. We can adjust our scripts accordingly.
> 
> If I want to train egale2 model for qwen2.5-7b-instruct, should I modify the `cnets1.py` or not ? I think that `cnets1.py` already supports qwen2 models beacause we can inference with the author provided eagle2 of qwen2-7b-instruct.

I guess the author only open-sourced the inference part, not the training part.

### ravi03071991 · 2025-05-20

I think the [training file](https://github.com/SafeAILab/EAGLE/blob/main/eagle/train/main.py) is the same for both Eagle2 and Eagle3. The model file differs with`cnets1.py` for Eagle2 and `cnets.py` for Eagle3.

### lahmuller · 2025-05-28

hey @skylee-01 , I wonder have you successfully trained the qwen2 model with EAGLE3, cause I'm also planning doing the same thing.

### skylee-01 · 2025-05-28

> hey [@skylee-01](https://github.com/skylee-01) , I wonder have you successfully trained the qwen2 model with EAGLE3, cause I'm also planning doing the same thing.

Good luck to you

### lahmuller · 2025-05-29

> > hey [@skylee-01](https://github.com/skylee-01) , I wonder have you successfully trained the qwen2 model with EAGLE3, cause I'm also planning doing the same thing.
> 
> Good luck to you
OK, I'll try


### garycaokai · 2025-06-03

![Image](https://github.com/user-attachments/assets/5a5460d6-6660-4333-b3a4-f34db7ce6e17)

### hongyanz · 2025-06-13

The training code has been released.

### liuqianchao · 2025-06-23

> The training code has been released.

@hongyanz Can you help update the `cnets.py` code to make it compatible with the Qwen model?


