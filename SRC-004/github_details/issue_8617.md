# [Issue #8617] [Usage]: Number of requests currently in the queue

source: https://github.com/vllm-project/vllm/issues/8617
state: closed | updated: 2026-09-22T18:53:58Z
labels: usage

## 正文

### Your current environment

```text
The output of `python collect_env.py`
```


### How would you like to use vllm

I am running an online inference server via the code: 
`vllm serve "daryl149/llama-2-7b-chat-hf" --max-model-len 2048`  for which I am sending request through a load generator. I want to know if it is possible to find out the number of requests currently in the queue or alternatively number of requests currently being processed in a batch (assume batch size=248 and number of batches=1). 

### Before submitting a new issue...

- [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 评论 (3)

### hmellor · 2024-09-20

You can query the `/metrics` endpoint for this information. 


https://docs.vllm.ai/en/latest/serving/metrics.html

### surak · 2026-09-22

> You can query the `/metrics` endpoint for this information.
> 
> https://docs.vllm.ai/en/latest/serving/metrics.html

this document is no longer there.

### hmellor · 2026-09-22

New location https://docs.vllm.ai/en/latest/usage/metrics/
