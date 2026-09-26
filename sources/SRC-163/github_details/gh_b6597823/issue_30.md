# [Issue #30] Generating max_num_tokens.csv for Different Hardware Environments

source: https://github.com/LLMServe/DistServe/issues/30
state: open | updated: 2024-10-17T01:18:12Z
labels: 

## 正文

In the part of the experimental model for finding the optimal placement strategy, there are three files in the `simdistserve/estimators/profile_data` directory, one of which is named `max_num_tokens.csv`. I am very curious about how this file is generated in different environments, because the other two JSON files can be generated based on the code in `evaluation/0-test-single-forward-performance`. However, I have not found a method for generating this CSV file. Based on my understanding, this file should be associated with different hardware or GPU environments, and the profiles in different environments should be different. I am eagerly awaiting your response. Thank you very much!

<img width="1260" alt="image" src="https://github.com/user-attachments/assets/1d2a203a-9760-42d8-bb5e-6070b3c4bf1b">


## 评论 (1)

### lzc-code · 2024-10-17

I met the same problem.
