source: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/
lastmod: 2026-09-24

#

`vllm.logging_utils`

[¶](https://docs.vllm.ai#vllm.logging_utils)

Modules:

-
–[access_log_filter](https://docs.vllm.ai/access_log_filter/#vllm.logging_utils.access_log_filter)Access log filter for uvicorn to exclude specific endpoints from logging.

-
–[formatter](https://docs.vllm.ai/formatter/#vllm.logging_utils.formatter) -
–[lazy](https://docs.vllm.ai/lazy/#vllm.logging_utils.lazy) -
–[log_time](https://docs.vllm.ai/log_time/#vllm.logging_utils.log_time)Provides a timeslice logging decorator.


Classes:

-
–[ColoredFormatter](https://docs.vllm.ai#vllm.logging_utils.ColoredFormatter)Adds ANSI color codes to log levels for terminal output.

-
–[NewLineFormatter](https://docs.vllm.ai#vllm.logging_utils.NewLineFormatter)Adds logging prefix to newlines to align multi-line messages.

-
–[UvicornAccessLogFilter](https://docs.vllm.ai#vllm.logging_utils.UvicornAccessLogFilter)A logging filter that excludes access logs for specified endpoint paths.


Functions:

-
–[create_uvicorn_log_config](https://docs.vllm.ai#vllm.logging_utils.create_uvicorn_log_config)Create a uvicorn logging configuration with access log filtering.

-
–[logtime](https://docs.vllm.ai#vllm.logging_utils.logtime)Logs the execution time of the decorated function.


##

`ColoredFormatter`

[¶](https://docs.vllm.ai#vllm.logging_utils.ColoredFormatter)

Bases: [NewLineFormatter](https://docs.vllm.ai/formatter/#vllm.logging_utils.formatter.NewLineFormatter)

Adds ANSI color codes to log levels for terminal output.

This formatter adds colors by injecting them into the format string for static elements (timestamp, filename, line number) and modifying the levelname attribute for dynamic color selection.

## Source code in `vllm/logging_utils/formatter.py`


##

`NewLineFormatter`

[¶](https://docs.vllm.ai#vllm.logging_utils.NewLineFormatter)

Bases: [Formatter](https://docs.python.org/3/library/logging.html#logging.Formatter)

Adds logging prefix to newlines to align multi-line messages.

## Source code in `vllm/logging_utils/formatter.py`


##

`UvicornAccessLogFilter`

[¶](https://docs.vllm.ai#vllm.logging_utils.UvicornAccessLogFilter)

Bases: [Filter](https://docs.python.org/3/library/logging.html#logging.Filter)

A logging filter that excludes access logs for specified endpoint paths.

This filter is designed to work with uvicorn's access logger. It checks the log record's arguments for the request path and filters out records matching the excluded paths.

## Uvicorn access log format

'%s - "%s %s HTTP/%s" %d' (client_addr, method, path, http_version, status_code)

## Example

127.0.0.1:12345 - "GET /health HTTP/1.1" 200

Parameters:

-

(`excluded_paths`

[¶](https://docs.vllm.ai#vllm.logging_utils.UvicornAccessLogFilter(excluded_paths))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –A list of URL paths to exclude from logging. Paths are matched exactly. Example: ["/health", "/metrics"]


Methods:

-
–[filter](https://docs.vllm.ai#vllm.logging_utils.UvicornAccessLogFilter.filter)Determine if the log record should be logged.


## Source code in `vllm/logging_utils/access_log_filter.py`


###

`filter(record)`

[¶](https://docs.vllm.ai#vllm.logging_utils.UvicornAccessLogFilter.filter)

Determine if the log record should be logged.

Parameters:

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the record should be logged, False otherwise.


## Source code in `vllm/logging_utils/access_log_filter.py`


##

`create_uvicorn_log_config(excluded_paths=None, log_level='info')`

[¶](https://docs.vllm.ai#vllm.logging_utils.create_uvicorn_log_config)

Create a uvicorn logging configuration with access log filtering.

This function generates a logging configuration dictionary that can be passed to uvicorn's `log_config`

parameter. It sets up the access log filter to exclude specified paths.

Parameters:

-

(`excluded_paths`

[¶](https://docs.vllm.ai#vllm.logging_utils.create_uvicorn_log_config(excluded_paths))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –List of URL paths to exclude from access logs.

-

(`log_level`

[¶](https://docs.vllm.ai#vllm.logging_utils.create_uvicorn_log_config(log_level))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'info'`

) –The log level for uvicorn loggers.


Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)A dictionary containing the logging configuration.


## Example

config = create_uvicorn_log_config(["/health", "/metrics"]) uvicorn.run(app, log_config=config)


## Source code in `vllm/logging_utils/access_log_filter.py`


##

`logtime(logger, msg=None)`

[¶](https://docs.vllm.ai#vllm.logging_utils.logtime)

Logs the execution time of the decorated function. Always place it beneath other decorators.