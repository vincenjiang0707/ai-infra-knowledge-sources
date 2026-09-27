source: https://docs.vllm.ai/en/latest/api/vllm/config/logging/
lastmod: 2026-09-27

#

`vllm.config.logging`

[¶](https://docs.vllm.ai#vllm.config.logging)

Classes:

-
–[LoggingConfig](https://docs.vllm.ai#vllm.config.logging.LoggingConfig)vLLM logging. Default

`dictConfig`

adds a formatted stream handler.

##

`LoggingConfig`

[¶](https://docs.vllm.ai#vllm.config.logging.LoggingConfig)

vLLM logging. Default `dictConfig`

adds a formatted stream handler.

Supply a JSON object with `--logging-config`

or individual fields with dotted arguments such as `--logging-config.log_level DEBUG`

and `--logging-config.pylogging_config_file logging.json`

. `--log-level`

and legacy `--log-config-file`

override their matching fields. Set `configure_logging`

to false to skip applying a `dictConfig`

.

Attributes:

-
([configure_logging](https://docs.vllm.ai#vllm.config.logging.LoggingConfig.configure_logging)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to apply a Python logging configuration.

-
([log_level](https://docs.vllm.ai#vllm.config.logging.LoggingConfig.log_level)`LogLevel`

) –Log level used when no custom logging configuration is provided.

-
([pylogging_config_file](https://docs.vllm.ai#vllm.config.logging.LoggingConfig.pylogging_config_file)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NonePath to a Python logging JSON file using


## Source code in `vllm/config/logging.py`


###

`configure_logging = Field(default_factory=(lambda: envs.VLLM_CONFIGURE_LOGGING))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.logging.LoggingConfig.configure_logging)

Whether to apply a Python logging configuration.

With no `pylogging_config_file`

, the default config adds a formatted stream handler to the `vllm`

logger. A custom Python logging configuration file also requires this to be enabled.

###

`log_level = Field(default_factory=(lambda: cast(LogLevel, envs.VLLM_LOGGING_LEVEL)))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.logging.LoggingConfig.log_level)

Log level used when no custom logging configuration is provided.

###

`pylogging_config_file = Field(default_factory=(lambda: envs.VLLM_LOGGING_CONFIG_PATH))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.logging.LoggingConfig.pylogging_config_file)

Path to a Python logging JSON file using [ dictConfig schema](https://docs.python.org/3/library/logging.config.html#configuration-file-format).

A custom `dictConfig`

is authoritative over `log_level`

for logger, handler, and formatter settings.