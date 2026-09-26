# [Issue #99] Token-wise the same generalization?

source: https://github.com/FasterDecoding/Medusa/issues/99
state: closed | updated: 2024-05-21T09:25:24Z
labels: 

## 正文

Is Medusa1 model generalize token-wise the same as the base model w.o. medusa head?

I found change medusa choices will change the output.

## 评论 (2)

### Ageliss · 2024-05-21

We've figured out this problem by shrinking the medusa choices to only top-1 predictions, i.e., [(0), (0,0), (0,0,0), (0,0,0,0), (0,0,0,0,0)]. 

In such way, MHCA computation will get a bit-wise the same logits as the baseline wo medusa decoding. 

Hope it helps for other people interested in bitwise the same decoding.

### Ageliss · 2024-05-21

> We've figured out this problem by shrinking the medusa choices to only top-1 predictions, i.e., [(0), (0,0), (0,0,0), (0,0,0,0), (0,0,0,0,0)].
> 
> In such way, MHCA computation will get a bit-wise the same logits as the baseline wo medusa decoding.
> 
> Hope it helps for other people interested in bitwise the same decoding.


