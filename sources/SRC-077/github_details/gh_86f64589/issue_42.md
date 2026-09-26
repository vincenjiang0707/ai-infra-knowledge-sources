# [Issue #42] httpx - INFO - HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 400 Bad Request"

source: https://github.com/meta-pytorch/KernelAgent/issues/42
state: closed | updated: 2025-11-08T05:16:29Z
labels: 

## 正文

### 🐛 Describe the bug

Seeing the above error on running the following. 

`ython -m Fuser.auto_agent   --problem  /home/sgoswami/ai/KernelBench/KernelBench/level1/19_ReLU.py   --verify`


### Platform and Version

_No response_

## 评论 (2)

### kaiming-cheng · 2025-11-07

@whatdhack Make sure your `.env` file is in the same directory where you're running the command. 

### whatdhack · 2025-11-08

Thanks.  The following works too.   

`OPENAI_MODEL=gpt-5 NUM_KERNEL_SEEDS=4 MAX_REFINEMENT_ROUNDS=10 LOG_LEVEL=INFO OPENAI_API_KEY=<key> python -m Fuser.auto_agent   --problem $HOME/ai/KernelBench/KernelBench/level1/19_ReLU.py   --verify`
