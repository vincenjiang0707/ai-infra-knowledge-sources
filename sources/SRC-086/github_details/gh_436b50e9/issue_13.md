# [Issue #13] Is there any document that describes the Medusa inference details and theory?

source: https://github.com/FasterDecoding/Medusa/issues/13
state: closed | updated: 2023-10-29T04:32:04Z
labels: 

## 正文

Hi there,

Thank you for the great work! I've read through the blog in https://sites.google.com/view/medusa-llm, and I found it useful to understand the broader picture of the method. However, I do find the implementation details to be quite challenging to comprehend. I was wondering if there is (or planning) a document that contains the underlying theory, such as these functions:
- generate_candidates
- tree_decoding
- evaluate_posterior
- update_inference_inputs

Many thanks!

## 评论 (4)

### leeyeehoo · 2023-09-14

Yes, I have the same thought! Will write a detailed document to explain this (estimated done by this week).

### leeyeehoo · 2023-09-20

UPDATE: Preview is [here](https://github.com/FasterDecoding/Medusa/blob/sparse_tree/notebooks/medusa_introduction.ipynb)

### MeWannaSleep · 2023-09-29

@leeyeehoo ,hi I've read medusa_configuration_explained.ipynb, but still don't understand why is medusa_attn_mask only used in the inference phase? Could you please elaborate on this ?

### leeyeehoo · 2023-10-29

@MeWannaSleep Sorry, I didn't have a notification on. It is for tree attention. For training, we just train the heads to predict the future. If you want to further understand the training pipeline, see our training code. 
