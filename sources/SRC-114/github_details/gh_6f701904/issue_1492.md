# [Issue #1492] Is it possible to calculate the LLM performance, Token per Second ?

source: https://github.com/mlcommons/inference/issues/1492
state: closed | updated: 2026-05-11T00:43:19Z
labels: Stale

## 正文

Hello, I get the inference result v3.1 and analysis the performance, throughput (token per second).
In the large language model task, the test results are measured by Queries/s and Samples/s.

I understand that query is a similar concept to batch and includes multiple samples.
Then i can estimate the number of sentences, but i don't know the specific number of input/output token length.
In the source code, there is only maximum number of input/output token length. 
Is there any way to estimate the throughput performance in terms of token per second metric ?

Thank you.

## 评论 (2)

### ishaan-jaff · 2023-11-29

@ConstantPark 

I'm the maintainer of LiteLLM we provide an Open source proxy for load balancing Azure + OpenAI + Any LiteLLM supported LLM
**It can process (500+ requests/second)**

From this thread it looks like you're trying to maximize throughput - I hope our solution makes it easier for you. **(i'd love feedback if you're trying to do this)**

## Here's the quick start:
Doc: https://docs.litellm.ai/docs/simple_proxy#load-balancing---multiple-instances-of-1-model

## Step 1 Create a Config.yaml
```python
model_list:
  - model_name: gpt-4
    litellm_params:
      model: azure/chatgpt-v-2
      api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
      api_version: "2023-05-15"
      api_key: 
  - model_name: gpt-4
    litellm_params:
      model: azure/gpt-4
      api_key: 
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
  - model_name: gpt-4
    litellm_params:
      model: azure/gpt-4
      api_key: 
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
```

## Step 2: Start the litellm proxy:
```
litellm --config /path/to/config.yaml
```

## Step3 Make Request to LiteLLM proxy:
```
curl --location 'http://0.0.0.0:8000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-4",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ],
    }
'
```

### github-actions[bot] · 2026-05-11

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
