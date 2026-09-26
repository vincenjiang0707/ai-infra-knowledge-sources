source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/mtp/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.cpu.mtp`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.mtp)

CPU DeepSeek-V4 MTP (speculative decoding) — deferred, not implemented.

`DeepSeekV4MTP`

is only instantiated when `vllm/model_executor/models/registry.py`

's speculative-decoding registry resolves it by name for a speculative-decoding config; a plain (non-spec) DeepSeek-V4 CPU model never constructs this class. This stub exists solely so `vllm.models.deepseek_v4.cpu`

is import-clean.