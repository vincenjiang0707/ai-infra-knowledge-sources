source: https://docs.vllm.ai/en/latest/cli/chat/
lastmod: 2026-09-24

# vllm chat[¶](https://docs.vllm.ai#vllm-chat)

## Arguments[¶](https://docs.vllm.ai#arguments)

`--url`

[¶](https://docs.vllm.ai#-url)

- url of the running OpenAI-Compatible RESTful API server
- Default:
`http://localhost:8000/v1`


`--model-name`

[¶](https://docs.vllm.ai#-model-name)

- The model name used in prompt completion, default to the first model in list models API call.

`--api-key`

[¶](https://docs.vllm.ai#-api-key)

- API key for OpenAI services. If provided, this api key will overwrite the api key obtained through environment variables. It is important to note that this option only applies to the OpenAI-compatible API endpoints and NOT other endpoints that may be present in the server. See the security guide in the vLLM docs for more details.

`--system-prompt`

[¶](https://docs.vllm.ai#-system-prompt)

- The system prompt to be added to the chat template, used for models that support system prompts.

`-q`

, `--quick`

[¶](https://docs.vllm.ai#-q-quick)

- Send a single prompt as MESSAGE and print the response, then exit.

`--stats`

[¶](https://docs.vllm.ai#-stats)

- Print TTFT and TPS statistics after each response.
- Default:
`False`