source: https://github.com/vllm-project/guidellm/issues/566

**Is your feature request related to a problem? Please describe.**

External tools which call GuideLLM must wait for the benchmark to complete before doing any analysis. For use in larger pipelines it would be ideal for GuideLLM to stream raw request data back to the caller.

**Describe the solution you'd like**

Implement a mechanism where external callers of GuideLLM ABI can monitor individual LLM responses, either though `benchmark_generative_text`

or as a new entrypoint for streaming.

Is your feature request related to a problem? Please describe.External tools which call GuideLLM must wait for the benchmark to complete before doing any analysis. For use in larger pipelines it would be ideal for GuideLLM to stream raw request data back to the caller.

Describe the solution you'd likeImplement a mechanism where external callers of GuideLLM ABI can monitor individual LLM responses, either though

`benchmark_generative_text`

or as a new entrypoint for streaming.