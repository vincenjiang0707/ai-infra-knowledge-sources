# [Issue #247] Inquiry about attention mask used for EAGLE-3 Training

source: https://github.com/SafeAILab/EAGLE/issues/247
state: open | updated: 2025-09-10T09:33:07Z
labels: 

## 正文

May I ask why does the attention mask also need to be shifted during the training-time test process? From what I've read in the code, it seems the attention mask is only applied to the KV cache stored at step=0. If that's the case, wouldn't it be the same as what is described in Figure 6 of the paper if we don't shift the mask?

https://github.com/SafeAILab/EAGLE/blob/main/eagle/traineagle3/cnets.py#L844

Thanks for your time.

## 评论 (3)

### DeclK · 2025-06-30

This masking is extremely weird, it would gradually make the past unseen for input tokens. I make a demo mask code below
```python
import torch
seq_len = 6
idx = 1
attn_mask = torch.tril(torch.ones((seq_len, seq_len)))
index = torch.arange(seq_len)
attn_mask[index[idx:], index[:seq_len-idx]] = -100
print(attn_mask)
```
output is like this:
```python
tensor([[   1.,    0.,    0.,    0.,    0.,    0.],
        [-100.,    1.,    0.,    0.,    0.,    0.],
        [   1., -100.,    1.,    0.,    0.,    0.],
        [   1.,    1., -100.,    1.,    0.,    0.],
        [   1.,    1.,    1., -100.,    1.,    0.],
        [   1.,    1.,    1.,    1., -100.,    1.]])
```
according to the code, this weights apply to current q and the first k, i.e. k0. So the input token is [1, 2, 3, 4, 5, X], and the past key is [0, 1, 2, 3, 4, 5], this masking means, the token 1 would attend token 0, which is normal; but the token 2 would attend wotken 1, but not attend the token 0, which would being weird. 
I can't run the code right now, maybe there is something missing, it would be great to hear some explaination.🤔 @Liyuhui-12 @hongyanz 

### xinlong-yang · 2025-07-01

That's true, I think this may be a tiny bug. If we comment line841-line844 in cnets.py, the performance would be slightly better in my experiments. But since the seqlen here is 2k, and the shift is only 7 steps, most tokens in the sequence are minimally affected. The performance comparison chart is shown below (fix-test means comment the line841-line844): 

![Image](https://github.com/user-attachments/assets/2de0c46d-3938-4bc4-b1f2-24ebbcaaa6aa)

### SunnyLi2015 · 2025-09-09

same question here. @hongyanz  is this a bug?
Code link https://github.com/SafeAILab/EAGLE/blob/a19206e0edfaa13d835027eb28933631ce89aa5c/eagle/traineagle3/cnets.py#L865-L868
