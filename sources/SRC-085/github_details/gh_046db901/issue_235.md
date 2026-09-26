# [Issue #235] Calculating Average Acceptance Length on EAGLE-3

source: https://github.com/SafeAILab/EAGLE/issues/235
state: open | updated: 2025-07-27T22:10:33Z
labels: 

## 正文

Is this correct to calculate average acceptance length and the number of new tokens generated?

output_ids = model.eagenerate(input_ids, temperature=0.0, max_new_tokens=256, log=True)
new_tokens = int(output_ids[1])
steps = int(output_ids[2])
avg_accept_length = new_tokens / steps

## 评论 (2)

### hongyanz · 2025-07-20

There are multiple ways to define "average acceptance length". It depends on how you define the "average". One way is as what you did here (average within one round). Another way is to calculate the number of accepted tokens in each speculative decoding round, add it by 1 (because the very last token in each round will always be accepted as it is from the target model), and **average the numbers across all rounds**.

### ebubekir-pulat · 2025-07-27

@hongyanz Thank you for your answer. I was wanting to follow the method of calculating average acceptance length used in the EAGLE-3 paper: "The average number of tokens generated per drafting-verification cycle, which corresponds to the number of tokens accepted from the draft." 

Was the method you mentioned the technique used in the paper?
