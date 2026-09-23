source: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/log_time/
lastmod: 2026-09-23

#

`vllm.logging_utils.log_time`

[¶](https://docs.vllm.ai#vllm.logging_utils.log_time)

Provides a timeslice logging decorator.

Functions:

-
–[logtime](https://docs.vllm.ai#vllm.logging_utils.log_time.logtime)Logs the execution time of the decorated function.


##

`logtime(logger, msg=None)`

[¶](https://docs.vllm.ai#vllm.logging_utils.log_time.logtime)

Logs the execution time of the decorated function. Always place it beneath other decorators.