# [Issue #286] Why doesn't --output-tokens-mean-deterministic guarantee exact token count?

source: https://github.com/triton-inference-server/perf_analyzer/issues/286
state: closed | updated: 2025-02-24T17:35:03Z
labels: question

## 正文

I noticed the documentation for --output-tokens-mean-deterministic states:

> When using --output-tokens-mean, this flag can be set to improve precision by setting the minimum number of tokens equal to the requested number of tokens. This is currently supported with the Triton service-kind. Note that there is still some variability in the requested number of output tokens, but GenAi-Perf attempts its best effort with your model to get the right number of output tokens.

However, there's another approach using extra inputs that seems to enforce fixed length:

```

--extra-inputs "min_tokens:${output_size}" \

--extra-inputs "ignore_eos:True"

```

Questions:

Why does --output-tokens-mean-deterministic still have variability while the extra inputs approach seems to enforce fixed length?


## 评论 (1)

### the-david-oy · 2025-02-18

It's dependent on the endpoints. Some endpoinst have ways to enforce fixed lengths, some don't. And some of the APIs are shared amongst backends in different servers, so we try to keep GenAI-Perf flexible enough among servers.

I think for the endpoints where it is generally possible, --output-tokens-mean-deterministic does result in a fixed length. For example, the Triton + vLLM converter does exactly what you're describing (except ignore_eos, which I think is redundant for it): https://github.com/triton-inference-server/perf_analyzer/blob/ef05026b25130642cca98f9bc1ef2e8bd2078d76/genai-perf/genai_perf/inputs/converters/vllm_converter.py#L83-L84
