# [Issue #256] Discrepancy in the computation of Eagle 3 bw paper and code

source: https://github.com/SafeAILab/EAGLE/issues/256
state: closed | updated: 2025-07-10T21:18:00Z
labels: 

## 正文

Hi!

We are excited to try EAGLE 3 in vLLM and were hoping to see good improvement as shown in the paper. vLLM supports only chain drafts but we still expect similar gains when comparing E1 and E3 for chain drafts. However, we see that even though E3 has 20-30% better AL than E1 for K=3/4, the e2e gains is only ~5% for the best choices of K. E1's optimal K is 3 and E3's optimal K is 4. https://github.com/vllm-project/vllm/issues/20780

Another thing that we observe is that the E3 paper has 2 fc layers as per [Fig 5](https://arxiv.org/pdf/2503.01840). The 2nd fc layer is supposed to bring down the dim of attn input from `2*hidden_dim` to `hidden_dim`. However, code in this repo just passes the `2*hidden_dim` w/o the 2nd fc layer which increases the attn computation by 2x. 

1. Can you please share the reasoning behind the disconnect bw the code and the paper regarding 2nd fc layer and 2x attn computation?
2. what are your thoughts on the AL gain in E3 coming majorly from the increased attention computation?
3. How likely is it to observe good increase in AL from E3 over E1 if the arch proposed in the paper is used?
4. Do you have a E3 checkpoint for `meta-llama/Llama-3.1-8B-Instruct` with the arch which the paper proposed so we can quickly verify the above?

Looking forward to your response!

## 评论 (2)

### ekagra-ranjan · 2025-07-10

Update: the 2nd fc layer is sort of fused into the QKVProjection which is the 1st fc layer in Attention so its not 2x attn increase. The QKVProjection does the job of the 2nd fc layer 

### hongyanz · 2025-07-10

> Update: the 2nd fc layer is sort of fused into the QKVProjection which is the 1st fc layer in Attention so its not 2x attn increase. The QKVProjection does the job of the 2nd fc layer

Exactly! Two linear operations can be merged into one linear operation.
