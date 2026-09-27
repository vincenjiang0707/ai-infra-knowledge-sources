source: https://docs.vllm.ai/en/latest/api/vllm/logger/
lastmod: 2026-09-27

#

`vllm.logger`

[¶](https://docs.vllm.ai#vllm.logger)

Logging configuration for vLLM.

Functions:

-
–[configure_logging](https://docs.vllm.ai#vllm.logger.configure_logging)Apply a logging configuration in the current process.

-
–[configure_logging_from_args](https://docs.vllm.ai#vllm.logger.configure_logging_from_args)Apply parsed logging arguments and retain them for child processes.

-
–[configure_logging_if_needed](https://docs.vllm.ai#vllm.logger.configure_logging_if_needed)Apply a logging configuration unless it is already active in this process.

-
–[enable_trace_function_call](https://docs.vllm.ai#vllm.logger.enable_trace_function_call)Enable tracing of every function call in code under

`root_dir`

. -
–[init_logger](https://docs.vllm.ai#vllm.logger.init_logger)Retrieve a logger and add vLLM's convenience logging methods.

-
–[set_vllm_process_name](https://docs.vllm.ai#vllm.logger.set_vllm_process_name)Set the vLLM process name added to subsequent log records.


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

`_configure_vllm_root_logger(config=None)`

[¶](https://docs.vllm.ai#vllm.logger._configure_vllm_root_logger)

Configure logging from explicit config or bootstrap environment values.

## Source code in `vllm/logger.py`


##

`_log_platform_warnings(config)`

[¶](https://docs.vllm.ai#vllm.logger._log_platform_warnings)

Emit platform diagnostics only after an enabled config is active.

## Source code in `vllm/logger.py`


##

`_should_log_with_scope(scope)`

[¶](https://docs.vllm.ai#vllm.logger._should_log_with_scope)

Decide whether to log based on scope.

## Source code in `vllm/logger.py`


##

`_vllm_log_record_factory(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.logger._vllm_log_record_factory)

Add vLLM process metadata to each log record.

## Source code in `vllm/logger.py`


##

`configure_logging(config)`

[¶](https://docs.vllm.ai#vllm.logger.configure_logging)

Apply a logging configuration in the current process.

## Source code in `vllm/logger.py`


##

`configure_logging_from_args(args)`

[¶](https://docs.vllm.ai#vllm.logger.configure_logging_from_args)

Apply parsed logging arguments and retain them for child processes.

## Source code in `vllm/logger.py`


##

`configure_logging_if_needed(config)`

[¶](https://docs.vllm.ai#vllm.logger.configure_logging_if_needed)

Apply a logging configuration unless it is already active in this process.

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

Retrieve a logger and add vLLM's convenience logging methods.

## Source code in `vllm/logger.py`


##

`set_vllm_process_name(process_name, *, skip_if_set=False)`

[¶](https://docs.vllm.ai#vllm.logger.set_vllm_process_name)

Set the vLLM process name added to subsequent log records.