source: https://docs.vllm.ai/en/latest/api/vllm/config/fault_tolerance/
lastmod: 2026-09-24

#

`vllm.config.fault_tolerance`

[¶](https://docs.vllm.ai#vllm.config.fault_tolerance)

Classes:

-
–[FaultToleranceConfig](https://docs.vllm.ai#vllm.config.fault_tolerance.FaultToleranceConfig)Configuration for fault tolerance.


##

`FaultToleranceConfig`

[¶](https://docs.vllm.ai#vllm.config.fault_tolerance.FaultToleranceConfig)

Configuration for fault tolerance.

Attributes:

-
([engine_recovery_timeout_sec](https://docs.vllm.ai#vllm.config.fault_tolerance.FaultToleranceConfig.engine_recovery_timeout_sec)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Timeout (in seconds) to wait for error handling instructions


## Source code in `vllm/config/fault_tolerance.py`


###

`engine_recovery_timeout_sec = 120`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.fault_tolerance.FaultToleranceConfig.engine_recovery_timeout_sec)

Timeout (in seconds) to wait for error handling instructions before raising an exception. If the EngineCore encounters an error, it waits up to this many seconds for vLLM to receive instructions on how to handle the error and then recover from the fault. If vLLM does not recover during this time, the original error is raised.