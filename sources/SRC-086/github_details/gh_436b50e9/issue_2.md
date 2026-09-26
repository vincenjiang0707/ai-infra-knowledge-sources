# [Issue #2] Fine-tune?

source: https://github.com/FasterDecoding/Medusa/issues/2
state: closed | updated: 2023-09-12T01:46:29Z
labels: 

## 正文

Can you clarify this passage:

> Training these heads is remarkably straightforward. You can either use the same corpus that trained the original model or generate a new corpus using the model itself. 

Which is the advantage of using a new dataset instead of the one that has been used to pre-train the original model to train the Medusa head? Put in other terms, while keeping in mind that original model would be frozen, could this training step be considered - as a whole - as a fine-tune?

Thank you.

## 评论 (1)

### ctlllll · 2023-09-12

Hey Loreto,

Thanks for your question! 
- You can view the new dataset here as distilling from the model. The advantage is it's more aligned to the output distribution of the model.
- Yes, the training step is some sort of parameter-efficient fine-tuning.

I'll close this issue, feel free to reopen it if you have further questions :)
