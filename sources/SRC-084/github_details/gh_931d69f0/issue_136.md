# [Issue #136] eval_mmlu ?

source: https://github.com/dropbox/hqq/issues/136
state: closed | updated: 2025-02-11T15:03:38Z
labels: 

## 正文

(empty)

## 评论 (11)

### mistletoe1024 · 2024-12-18

bug fixed.

### mobicham · 2024-12-18

Hi, sorry for the delay. What was the problem again ? 

### mistletoe1024 · 2024-12-18

Hi, I'd like to evaluate the performance of hqq+ on mmlu, 
so I writed a eval_mmlu() behind eval_wikitext2() in hqq_plus.py 
referred to  https://github.com/FranxYao/chain-of-thought-hub/blob/main/MMLU/run_mmlu_llama.py, 
but I got a bad avg score (only 0.0438:(, but FP16 is  0.4583),
my quantization setting is "nbits=2, group_size=8, quant_scale=False, quant_zero=False, axis=0",
lora_params and training_args were not change. 
Could you offer a better solution or any advice? thank you!

-----------------------------------------------------
Today, I printed the pred_answer of  eval_mmlu() after eval_wikitext2() ,  and found lots of '\n' in the list of pred_answer, I thought i had solved the problem, but still got bad score of mmlu (0.0342, and ppl is  5.601, seems normal). So could you offer your solution?

### mobicham · 2024-12-18

Oh I see, which model exactly? Is this an issue with MMLU only or also the other metrics?

### mistletoe1024 · 2024-12-18

> Oh I see, which model exactly? Is this an issue with MMLU only or also the other metrics?

Llama-2-7b-hf， only MMLU at present, the ppl is normal.

### mobicham · 2024-12-18

Did you train the model yourself? How did you train it (what dataset) etc. 

### mistletoe1024 · 2024-12-18

> Did you train the model yourself? How did you train it (what dataset) etc.

yes, but i just ran the hqq_puls.py and did not change any params. So the dataset is dataset = load_dataset('wikitext', 'wikitext-2-raw-v1', split='train')

### mistletoe1024 · 2024-12-18

the key to the question is the eval_mmlu() function, I printed the element of answers and saw "[", it should have been "A" or "B" or "C" or "D".  ( https://github.com/FranxYao/chain-of-thought-hub/blob/main/MMLU/run_mmlu_llama.py, line 172)

### mobicham · 2024-12-18

Sounds like it's overfiting to wikitext, that might explain why the ppl is good but mmlu is bad. You need proper instruct data (and the instruct model not base model) to get good mmlu performance, which is outside the scope of the hqq+ script

### mistletoe1024 · 2024-12-18

> Sounds like it's overfiting to wikitext, that might explain why the ppl is good but mmlu is bad. You need proper instruct data (and the instruct model not base model) to get good mmlu performance, which is outside the scope of the hqq+ script

Ok, I am going to try other dataset or instruct model, thank you :)

### mobicham · 2024-12-18

It's normally a mix of datasets not just 1. It's an art to figure out the right datasets :D 
Let me know how that works out!
