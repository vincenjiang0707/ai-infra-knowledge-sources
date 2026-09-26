source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/dspark/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.cpu.dspark`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.dspark)

CPU DeepSeek-V4 DSpark (speculative decoding) — deferred, not implemented.

`DSparkDeepseekV4ForCausalLM`

is only instantiated when the speculative- decoding registry resolves it by name for a DSpark speculative config; a plain (non-spec) DeepSeek-V4 CPU model never constructs this class. This stub exists solely so `vllm.models.deepseek_v4.cpu`

is import-clean.