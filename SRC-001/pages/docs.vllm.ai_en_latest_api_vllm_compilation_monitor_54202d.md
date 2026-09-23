source: https://docs.vllm.ai/en/latest/api/vllm/compilation/monitor/
lastmod: 2026-09-23

#

`vllm.compilation.monitor`

[¶](https://docs.vllm.ai#vllm.compilation.monitor)

Functions:

-
–[monitor_profiling_run](https://docs.vllm.ai#vllm.compilation.monitor.monitor_profiling_run)Context manager that times the initial profiling run.

-
–[monitor_torch_compile](https://docs.vllm.ai#vllm.compilation.monitor.monitor_torch_compile)Context manager that times torch.compile and manages depyf debugging.


##

`monitor_profiling_run()`

[¶](https://docs.vllm.ai#vllm.compilation.monitor.monitor_profiling_run)

Context manager that times the initial profiling run.

Asserts that no backend compilation occurs during the profiling run (all compilation should have completed before this point).

## Source code in `vllm/compilation/monitor.py`


##

`monitor_torch_compile(vllm_config, message='torch.compile took %.2f s in total', is_encoder=False)`

[¶](https://docs.vllm.ai#vllm.compilation.monitor.monitor_torch_compile)

Context manager that times torch.compile and manages depyf debugging.

On normal exit: logs the compile time and exits depyf. On exception: cleans up depyf without logging (compilation failed).