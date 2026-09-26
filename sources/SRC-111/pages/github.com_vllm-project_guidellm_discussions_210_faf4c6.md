source: https://github.com/vllm-project/guidellm/discussions/210

#
Possible invalid request formatting for `max_completion_tokens`

#210

[Answered](https://github.com#discussioncomment-13600689)by

[sjmonson](https://github.com/sjmonson)

[stmcginnis](https://github.com/stmcginnis)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

|
```json
Just looking in to this, but wanted to report it in case it was a known issue or someone has more information. While running guidellm against a locally running `WARNING 06-27 14:57:36 [protocol.py:58] The following fields were present in the request but ignored: {'max_completion_tokens'}` Running a request manually against the endpoint is happy, with no errors in the vllm logs: `curl -k -s -H "Content-Type: application/json" http://localhost:8000/v1/chat/completions -d '{"model":"llama3.1-8b-instruct","messages":[{"role":"user","content":"What is an AI tensorized weight?"}],"max_completion_tokens":35}' | jq .` ```
{
"id": "chatcmpl-e00ce83f-121f-482a-b43c-5c4494ad29ae",
"object": "chat.completion",
"created": 1751037186,
"model": "llama3.1-8b-instruct",
"choices": [
{
"index": 0,
"message": {
"role": "assistant",
"reasoning_content": null,
"content": "A tensorized weight, also known as a tensor weight or a weight tensor, is a type of weight used in artificial neural networks (ANNs) and deep learning models.",
"tool_calls": []
},
"logprobs": null,
"finish_reason": "length",
"stop_reason": null
}
],
"usage": {
"prompt_tokens": 43,
"total_tokens": 78,
"completion_tokens": 35,
"prompt_tokens_details": null
},
"prompt_logprobs": null
}
``` Which leads me to believe the prompt being formed by guidellm must be placing |
```

[sjmonson](https://github.com/sjmonson)

Jun 27, 2025

## Replies: 1 comment 1 reply

|
Tldr: you can ignore that error. We set both The standard for setting a max tokens is kinda of messy. Some model servers support vLLM started with |

[sjmonson](https://github.com/sjmonson)

Tldr: you can ignore that error. We set both

`max_completion_tokens`

and`max_tokens`

to the same value.The standard for setting a max tokens is kinda of messy. Some model servers support

`max_tokens`

as the flag and some support`max_completion_tokens`

. In the official OpenAI documentation the legacy endpoint only supports`max_tokens`

while the chat endpoint supports`max_tokens`

for older models and`max_completion_tokens`

for everything. Ollama supports only`max_completion_tokens`

vLLM started with

`max_completion_tokens`

but at some point switched to`max_tokens`

and throws a harmless warning for the former. We kept both in GuideLLM for compatibility, but some model serverscough cough Ollamadon't li…