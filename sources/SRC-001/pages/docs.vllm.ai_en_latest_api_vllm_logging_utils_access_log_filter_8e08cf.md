source: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/access_log_filter/
lastmod: 2026-09-24

#

`vllm.logging_utils.access_log_filter`

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter)

Access log filter for uvicorn to exclude specific endpoints from logging.

This module provides a logging filter that can be used to suppress access logs for specific endpoints (e.g., /health, /metrics) to reduce log noise in production environments.

Classes:

-
–[UvicornAccessLogFilter](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.UvicornAccessLogFilter)A logging filter that excludes access logs for specified endpoint paths.


Functions:

-
–[create_uvicorn_log_config](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.create_uvicorn_log_config)Create a uvicorn logging configuration with access log filtering.


##

`UvicornAccessLogFilter`

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.UvicornAccessLogFilter)

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

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.UvicornAccessLogFilter(excluded_paths))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –A list of URL paths to exclude from logging. Paths are matched exactly. Example: ["/health", "/metrics"]


Methods:

-
–[filter](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.UvicornAccessLogFilter.filter)Determine if the log record should be logged.


## Source code in `vllm/logging_utils/access_log_filter.py`


###

`filter(record)`

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.UvicornAccessLogFilter.filter)

Determine if the log record should be logged.

Parameters:

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the record should be logged, False otherwise.


## Source code in `vllm/logging_utils/access_log_filter.py`


##

`create_uvicorn_log_config(excluded_paths=None, log_level='info')`

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.create_uvicorn_log_config)

Create a uvicorn logging configuration with access log filtering.

This function generates a logging configuration dictionary that can be passed to uvicorn's `log_config`

parameter. It sets up the access log filter to exclude specified paths.

Parameters:

-

(`excluded_paths`

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.create_uvicorn_log_config(excluded_paths))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –List of URL paths to exclude from access logs.

-

(`log_level`

[¶](https://docs.vllm.ai#vllm.logging_utils.access_log_filter.create_uvicorn_log_config(log_level))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'info'`

) –The log level for uvicorn loggers.


Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)A dictionary containing the logging configuration.


## Example

config = create_uvicorn_log_config(["/health", "/metrics"]) uvicorn.run(app, log_config=config)