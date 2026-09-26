source: https://docs.vllm.ai/en/latest/cli/complete/
lastmod: 2026-09-24

# vllm complete[¶](https://docs.vllm.ai#vllm-complete)

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

`--max-tokens`

[¶](https://docs.vllm.ai#-max-tokens)

- Maximum number of tokens to generate per output sequence.

`-q`

, `--quick`

[¶](https://docs.vllm.ai#-q-quick)

- Send a single prompt and print the completion output, then exit.

`--stats`

[¶](https://docs.vllm.ai#-stats)

- Print TTFT and TPS statistics after each response.
- Default:
`False`