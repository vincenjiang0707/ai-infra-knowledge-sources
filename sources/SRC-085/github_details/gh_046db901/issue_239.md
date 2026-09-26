# [Issue #239] question about layer for eagle3 train code

source: https://github.com/SafeAILab/EAGLE/issues/239
state: closed | updated: 2025-06-11T14:55:52Z
labels: 

## 正文

I notice train code for eagle3:

hidden_states0 = outs.hidden_states[0]
hidden_states1 = outs.hidden_states[1]
hidden_states2 = outs.hidden_states[2]

why use 0,1,2 ? I understand that this is the 0th layer, the 1st layer, and the 2th layer，not the low layer，medium layer and high layer  mentioned in the paper ？

## 评论 (2)

### MeganEFlynn · 2025-06-10

In line 1138 of modeling_llama_kv.py, they only keep the hidden states if it is one of the correct layers.  


### xinlong-yang · 2025-06-11

The training data is generated online, so you should check the modeling_llama_kv.py file to verify the real layers chosen.
