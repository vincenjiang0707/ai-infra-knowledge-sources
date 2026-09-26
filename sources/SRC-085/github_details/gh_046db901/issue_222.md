# [Issue #222] Clarification on d2t and t2d Mapping Logic in EAGLE-3 Draft Model

source: https://github.com/SafeAILab/EAGLE/issues/222
state: closed | updated: 2025-06-05T17:49:16Z
labels: 

## 正文

Hi, thank you for the great work on this project.

I was reviewing the Model class in model/cnets.py and noticed that d2t and t2d are declared within the class. Since EAGLE-3 appears to use its own lm_head for the draft model—rather than sharing the target model's lm_head—I assume there's an intended mapping process from the draft vocab indices to the target vocab indices.

`self.lm_head=nn.Linear(config.hidden_size,config.draft_vocab_size,bias=False)`
`d2t=torch.zeros((config.draft_vocab_size),dtype=torch.long) `
`t2d=torch.zeros((config.vocab_size),dtype=torch.bool)`

However, when I debugged using the official checkpoint, I found that all values in the d2t tensor are initialized to 0. This makes it unclear how the draft tokens are correctly mapped to the target model's vocabulary space during inference.

`ss_token.append(topk_index + self.d2t[topk_index])`
`input_ids = topk_index + self.d2t[topk_index]`


Could you clarify how the d2t and t2d mappings are supposed to be constructed or loaded? Any explanation or pointer would be greatly appreciated.

Thanks again for your work and support!

## 评论 (5)

### hongdaxia · 2025-05-07

The Vicuna-13B-v1.3 model has a smaller vocabulary, and its head overhead is relatively small. Models like LLaMA3.1-Instruct 8B, LLaMA3.3-Instruct 70B, and DeepSeek-R1-Distill-LLaMA 8B have larger vocabularies, resulting in greater head overhead. Therefore, for models with significant head overhead, smaller replacement heads are used. Furthermore, the source code first initializes these two tensors (referring to the head tensors/weights) before loading the actual weights. It's also common for the weights within the head to have many elements close to zero. Thus, your observation could be due to one of three situations:

1.You encountered a model that doesn't require a smaller replacement head, such as Vicuna-13B-v1.3.

2.You printed the weights before they were actually loaded, meaning you were seeing the initial zero values from initialization.

3.You only printed a subset of the values and coincidentally encountered zeros.

### junghye01 · 2025-05-09

@hongdaxia 

Thanks for the clarification — I was able to resolve the issue by adding the weight loading logic from the checkpoint.

That said, I have a follow-up question about d2t. Since it's stored as a register_buffer with requires_grad=False, I assume it's a non-learnable mapping. But if the draft_vocab_size is 32,000, then even after applying d2t to map to target vocab indices, only 32,000 target tokens can be represented.

I'm curious: how is this d2t mapping defined? Specifically, what criteria are used to select which target vocab tokens are included in the draft vocab? Understanding this selection process would really help clarify the mapping logic.

### hongyanz · 2025-05-10

It is based on the frequency analysis of tokens. You can refer to:

https://arxiv.org/abs/2502.14856
https://en.wikipedia.org/wiki/Zipf%27s_law

### NickL77 · 2025-05-16

I am also curious what the effects of the limited vocabulary has on model performance. Eagle 3 paper mentions the 2 main contributions are training time test and feature fusion.  Are all models (including Eagle 1 and 2 models) in the Eagle 3 paper running with or without the limited draft vocabulary?

If Eagle 1 and 2 models are run with full draft vocabulary and Eagle 3 models are run with limited draft vocabulary, then the comparisons are not fair and additional ablations should be included.

### hongyanz · 2025-05-19

The first paper that I listed above compared EAGLE2 vs. EAGLE2 + dictionary pruning. The speedup in the latter method is still far below EAGLE3 (2.20x vs. 3.45x, yes, this is a rough comparison).

![Image](https://github.com/user-attachments/assets/5d372425-1485-4827-8544-4c155eec0bbd)

![Image](https://github.com/user-attachments/assets/5f40de54-a0fb-4f65-a9c0-ce161318dfb4)
