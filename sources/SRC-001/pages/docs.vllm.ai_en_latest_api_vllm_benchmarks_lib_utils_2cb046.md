source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/lib/utils/
lastmod: 2026-09-24

#

`vllm.benchmarks.lib.utils`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.utils)

Functions:

-
–[convert_to_pytorch_benchmark_format](https://docs.vllm.ai#vllm.benchmarks.lib.utils.convert_to_pytorch_benchmark_format)Save the benchmark results in the format used by PyTorch OSS benchmark with

-
–[default_vllm_config](https://docs.vllm.ai#vllm.benchmarks.lib.utils.default_vllm_config)Set a default VllmConfig for cases that directly test CustomOps or pathways

-
–[redact_sensitive_namespace](https://docs.vllm.ai#vllm.benchmarks.lib.utils.redact_sensitive_namespace)Return a copy of CLI arguments with selected values redacted.

-
–[use_compile](https://docs.vllm.ai#vllm.benchmarks.lib.utils.use_compile)Check if the benchmark is run with torch.compile.


##

`convert_to_pytorch_benchmark_format(args, metrics, extra_info)`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.utils.convert_to_pytorch_benchmark_format)

Save the benchmark results in the format used by PyTorch OSS benchmark with on metric per record https://github.com/pytorch/pytorch/wiki/How-to-integrate-with-PyTorch-OSS-benchmark-database

## Source code in `vllm/benchmarks/lib/utils.py`


##

`default_vllm_config()`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.utils.default_vllm_config)

Set a default VllmConfig for cases that directly test CustomOps or pathways that use get_current_vllm_config() outside of a full engine context.

## Source code in `vllm/benchmarks/lib/utils.py`


##

`redact_sensitive_namespace(args, fields)`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.utils.redact_sensitive_namespace)

Return a copy of CLI arguments with selected values redacted.

## Source code in `vllm/benchmarks/lib/utils.py`


##

`use_compile(args, extra_info)`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.utils.use_compile)

Check if the benchmark is run with torch.compile.