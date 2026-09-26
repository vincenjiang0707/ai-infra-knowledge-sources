source: https://docs.vllm.ai/en/latest/api/vllm/logger/
lastmod: 2026-09-24

#

`vllm.logger`

[¶](https://docs.vllm.ai#vllm.logger)

Logging configuration for vLLM.

Functions:

-
–[enable_trace_function_call](https://docs.vllm.ai#vllm.logger.enable_trace_function_call)Enable tracing of every function call in code under

`root_dir`

. -
–[init_logger](https://docs.vllm.ai#vllm.logger.init_logger)The main purpose of this function is to ensure that loggers are


##

`_VllmLogger`

[¶](https://docs.vllm.ai#vllm.logger._VllmLogger)

Bases: [Logger](https://docs.python.org/3/library/logging.html#logging.Logger)

Note: This class is just to provide type information. We actually patch the methods directly on the [ logging.Logger](https://docs.python.org/3/library/logging.html#logging.Logger) instance to avoid conflicting with other libraries such as

`intel_extension_for_pytorch.utils._logger`

.Methods:

-
–[debug_once](https://docs.vllm.ai#vllm.logger._VllmLogger.debug_once)As

, but subsequent calls with`debug`

-
–[error_once](https://docs.vllm.ai#vllm.logger._VllmLogger.error_once)As

, but subsequent calls with`error`

-
–[info_once](https://docs.vllm.ai#vllm.logger._VllmLogger.info_once)As

, but subsequent calls with`info`

-
–[warning_once](https://docs.vllm.ai#vllm.logger._VllmLogger.warning_once)As

, but subsequent calls with`warning`


## Source code in `vllm/logger.py`


###

`debug_once(msg, *args, scope='local')`

[¶](https://docs.vllm.ai#vllm.logger._VllmLogger.debug_once)

As [ debug](https://docs.python.org/3/library/logging.html#logging.Logger.debug), but subsequent calls with the same message are silently dropped.

## Source code in `vllm/logger.py`


###

`error_once(msg, *args, scope='local')`

[¶](https://docs.vllm.ai#vllm.logger._VllmLogger.error_once)

As [ error](https://docs.python.org/3/library/logging.html#logging.Logger.error), but subsequent calls with the same message are silently dropped.

## Source code in `vllm/logger.py`


###

`info_once(msg, *args, scope='local')`

[¶](https://docs.vllm.ai#vllm.logger._VllmLogger.info_once)

As [ info](https://docs.python.org/3/library/logging.html#logging.Logger.info), but subsequent calls with the same message are silently dropped.

## Source code in `vllm/logger.py`


##

`_should_log_with_scope(scope)`

[¶](https://docs.vllm.ai#vllm.logger._should_log_with_scope)

Decide whether to log based on scope.

## Source code in `vllm/logger.py`


##

`enable_trace_function_call(log_file_path, root_dir=None)`

[¶](https://docs.vllm.ai#vllm.logger.enable_trace_function_call)

Enable tracing of every function call in code under `root_dir`

. This is useful for debugging hangs or crashes. `log_file_path`

is the path to the log file. `root_dir`

is the root directory of the code to trace. If None, it is the vllm root directory.

Note that this call is thread-level, any threads calling this function will have the trace enabled. Other threads will not be affected.

## Source code in `vllm/logger.py`


##

`init_logger(name)`

[¶](https://docs.vllm.ai#vllm.logger.init_logger)

The main purpose of this function is to ensure that loggers are retrieved in such a way that we can be sure the root vllm logger has already been configured.