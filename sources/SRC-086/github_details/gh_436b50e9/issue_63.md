# [Issue #63] Some questions about sampling strategy

source: https://github.com/FasterDecoding/Medusa/issues/63
state: closed | updated: 2024-06-20T10:03:49Z
labels: 

## 正文

1. How do the "medusa_choices " generated. More specificly， what's the "mc_sim_7b_63" stands for? And can it fit  all the medusa heads number config?
2. I found that after i trained a 3 head medusa model.  Using the original "mc_sim_7b_63" value , there will be index overflow in the generate_candidates() function and tree_decoding() function when inference.
value as follows:
tree_indices, max value 32:
![image](https://github.com/FasterDecoding/Medusa/assets/42954889/1687ced2-a988-4217-8636-2629e08f4860)
however, the candidates shape:
![image](https://github.com/FasterDecoding/Medusa/assets/42954889/a195b293-ade1-4ba2-8373-d8c8860d2296)



## 评论 (3)

### Oscilloscope98 · 2023-11-15

@qianxiao1111 I have the same concern regarding `mc_sim_7b_6`. Do you have an answer? Thank you :)

### yuyangxie96 · 2024-05-19

@qianxiao1111 @Oscilloscope98  the same problem. Any idea now?

### xlim1997 · 2024-06-20

I discovered that they explain how to generate the Medusa choices in Appendix C of the paper. But I'm not sure whether they provided the code for medusa_choices generation or not.
 `The tree is initially formed through a
Cartesian product approach and subsequently refined by pruning based on the statistical expectations of the top-k predictions
from each MEDUSA head measured on the Alpaca-eval dataset (Dubois et al., 2023). The tree’s lean towards the left visually
represents the algorithm’s preference for nodes with higher probabilities on each head.`
