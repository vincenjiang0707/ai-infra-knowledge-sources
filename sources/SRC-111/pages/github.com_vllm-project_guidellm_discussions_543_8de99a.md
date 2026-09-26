source: https://github.com/vllm-project/guidellm/discussions/543

# [Bug] 'samples' parameter probably ignored in synthetic data generation (v0.5.0) #543

[Answered](https://github.com#discussioncomment-15573225)by

[sjmonson](https://github.com/sjmonson)

[valebes](https://github.com/valebes)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

|
## Click to view logs``` ✔ Request loader initialized with inf unique requests <-- Why inf { 'data': '[\'{"prompt_tokens": 600, "prompt_tokens_min": 200, "prompt_tokens_max": 1000, "prompt_tokens_stdev": 100, "output_tokens": 300, "output_tokens_stdev": 100, "output_tokens_min": 50, "output_tokens_max": 500, "samples": 10000}\']', 'data_args': '[]', 'data_samples': -1, 'preprocessors': ['GenerativeColumnMapper', 'GenerativeTextCompletionsRequestFormatter'], 'collator': 'GenerativeRequestCollator', 'sampler': 'None', 'num_workers': 1, 'random_seed': 42 } ``` |

Answered by

[sjmonson](https://github.com/sjmonson)Jan 22, 2026
## Replies: 1 comment 2 replies

|
Since GuideLLM v0.4.0 the synthetic dataset uses on-demand sample generation. If you want to pre-generate a specific number of samples use |

2 replies

Answer selected by

Since GuideLLM v0.4.0 the synthetic dataset uses on-demand sample generation. If you want to pre-generate a specific number of samples use

`--data-samples 10000`

.