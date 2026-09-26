# [Issue #1363] Token Count Calculation in SFT Data Distribution Curation

source: https://github.com/PaddlePaddle/ERNIE/issues/1363
state: closed | updated: 2026-02-18T12:01:58Z
labels: 

## 正文

Regarding the curation of SFT data, including the curation of the data distribution, I would like to understand how you calculate the token count for each data entry when designing the distribution. Is the token count based only on the user tokens, or does it also include the assistant tokens? (The reason I ask is that I understand the SFT loss is calculated only based on the assistant tokens.)

## 评论 (6)

### BossPi · 2025-11-17

Thank you very much for your interest in and inquiry about our data distribution curation process. Regarding your question about how we calculate the token count for each data entry, we would like to clarify that our calculation method includes assistant tokens in addition to user tokens.
If you have any further doubts or require additional clarification, please feel free to let us know.

### tcy6 · 2025-11-17

@BossPi Thank you for the clarification! I do have a follow-up question. Since the SFT loss is computed only on the assistant tokens, I'm wondering whether it might make more sense—both for task balancing and for learning dynamics—to base the token count on assistant tokens only when designing the data distribution. Could you share more details on why the distribution is calculated using both user and assistant tokens?

I'd really appreciate a more in-depth explanation. Thanks again!

### Yelrose · 2025-11-18

> Thank you for the clarification! I do have a follow-up question. Since the SFT loss is computed only on the assistant tokens, I'm wondering whether it might make more sense—both for task balancing and for learning dynamics—to base the token count on assistant tokens only when designing the data distribution. Could you share more details on why the distribution is calculated using both user and assistant tokens?
> 
> I'd really appreciate a more in-depth explanation. Thanks again!

Task re-weighting is essential in multimodal training, as different tasks exhibit varying context lengths during training. For our re-weighting strategy, we refer to the approach proposed in [InternVL 2.5](https://arxiv.org/pdf/2412.05271).

### tcy6 · 2025-11-18

> > Thank you for the clarification! I do have a follow-up question. Since the SFT loss is computed only on the assistant tokens, I'm wondering whether it might make more sense—both for task balancing and for learning dynamics—to base the token count on assistant tokens only when designing the data distribution. Could you share more details on why the distribution is calculated using both user and assistant tokens?
> > I'd really appreciate a more in-depth explanation. Thanks again!
> 
> Task re-weighting is essential in multimodal training, as different tasks exhibit varying context lengths during training. For our re-weighting strategy, we refer to the approach proposed in [InternVL 2.5](https://arxiv.org/pdf/2412.05271).

Thanks for the reply! I have a question: my understanding is that the advantage of this kind of re-weighting strategy is that it makes the training less sensitive to the exact data distribution ratios (because of the square root), so you don’t need to carefully tune the mixture of data. Is my understanding correct?

Because even if I don’t apply this special re-weighting and just use token averaging, I could simply adjust the proportions of different datasets so that the total number of tokens from long answers and short answers are not too different. Then, when I randomly sample a batch, the number of tokens from long and short answers in the batch should also be similar, and the trained model shouldn’t be biased toward longer or shorter responses.

### BossPi · 2025-11-19

We control the proportion of different types of data by adjusting the sampling ratio. Typically, we configure it based on the number of epochs for samples. For example, we sample text data for 1 epoch and image data for 1 epoch in an alternating manner.

### nepeplwu · 2026-02-18

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
