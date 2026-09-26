source: https://docs.vllm.ai/en/latest/api/vllm/envs/
lastmod: 2026-09-24

#

`vllm.envs`

[¶](https://docs.vllm.ai#vllm.envs)

Functions:

-
–[__getattr__](https://docs.vllm.ai#vllm.envs.__getattr__)Gets environment variables lazily.

-
–[compile_factors](https://docs.vllm.ai#vllm.envs.compile_factors)Return env vars used for torch.compile cache keys.

-
–[disable_envs_cache](https://docs.vllm.ai#vllm.envs.disable_envs_cache)Resets the environment variables cache. It could be used to isolate environments

-
–[enable_envs_cache](https://docs.vllm.ai#vllm.envs.enable_envs_cache)Enables caching of environment variables. This is useful for performance

-
–[env_list_with_choices](https://docs.vllm.ai#vllm.envs.env_list_with_choices)Create a lambda that validates environment variable

-
–[env_set_with_choices](https://docs.vllm.ai#vllm.envs.env_set_with_choices)Creates a lambda which that validates environment variable

-
–[env_with_choices](https://docs.vllm.ai#vllm.envs.env_with_choices)Create a lambda that validates environment variable against allowed choices.

-
–[get_env_or_set_default](https://docs.vllm.ai#vllm.envs.get_env_or_set_default)Create a lambda that returns an environment variable value if set,

-
–[get_vllm_port](https://docs.vllm.ai#vllm.envs.get_vllm_port)Get the port from VLLM_PORT environment variable.

-
–[is_set](https://docs.vllm.ai#vllm.envs.is_set)Check if an environment variable is explicitly set.


Attributes:

-
([VLLM_SKIP_MODEL_NAME_VALIDATION](https://docs.vllm.ai#vllm.envs.VLLM_SKIP_MODEL_NAME_VALIDATION)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set, vLLM will skip model name validation in API requests.


##

`VLLM_SKIP_MODEL_NAME_VALIDATION = False`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.envs.VLLM_SKIP_MODEL_NAME_VALIDATION)

If set, vLLM will skip model name validation in API requests. This allows any model name to be accepted in the 'model' field of requests, making the server model-name agnostic. Useful for proxy/gateway scenarios.

##

`__getattr__(name)`

[¶](https://docs.vllm.ai#vllm.envs.__getattr__)

Gets environment variables lazily.

NOTE: After enable_envs_cache() invocation (which triggered after service initialization), all environment variables will be cached.

## Source code in `vllm/envs.py`


##

`_is_envs_cache_enabled()`

[¶](https://docs.vllm.ai#vllm.envs._is_envs_cache_enabled)

##

`_resolve_rust_cli_path()`

[¶](https://docs.vllm.ai#vllm.envs._resolve_rust_cli_path)

Resolve the vllm-rs binary path.

Returns None unless VLLM_USE_RUST_FRONTEND or VLLM_USE_RUST_BENCH is enabled. When enabled, resolves VLLM_RUST_FRONTEND_PATH ("auto" by default) to the actual binary path.

## Source code in `vllm/envs.py`


##

`compile_factors()`

[¶](https://docs.vllm.ai#vllm.envs.compile_factors)

Return env vars used for torch.compile cache keys.

Start with every known vLLM env var; drop entries in `ignored_factors`

; hash everything else. This keeps the cache key aligned across workers.

## Source code in `vllm/envs.py`


|
|

##

`disable_envs_cache()`

[¶](https://docs.vllm.ai#vllm.envs.disable_envs_cache)

Resets the environment variables cache. It could be used to isolate environments between unit tests.

## Source code in `vllm/envs.py`


##

`enable_envs_cache()`

[¶](https://docs.vllm.ai#vllm.envs.enable_envs_cache)

Enables caching of environment variables. This is useful for performance reasons, as it avoids the need to re-evaluate environment variables on every call.

NOTE: Currently, it's invoked after service initialization to reduce runtime overhead. This also means that environment variables should NOT be updated after the service is initialized.

## Source code in `vllm/envs.py`


##

`env_list_with_choices(env_name, default, choices, case_sensitive=True)`

[¶](https://docs.vllm.ai#vllm.envs.env_list_with_choices)

Create a lambda that validates environment variable containing comma-separated values against allowed choices

Parameters:

-

(`env_name`

[¶](https://docs.vllm.ai#vllm.envs.env_list_with_choices(env_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the environment variable

-

(`default`

[¶](https://docs.vllm.ai#vllm.envs.env_list_with_choices(default))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Default list of values if not set

-

(`choices`

[¶](https://docs.vllm.ai#vllm.envs.env_list_with_choices(choices))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] |[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]List of valid string options or callable that returns list

-

(`case_sensitive`

[¶](https://docs.vllm.ai#vllm.envs.env_list_with_choices(case_sensitive))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether validation should be case sensitive


Returns:

-

–[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]Lambda function for environment_variables

-

–[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]dict that returns list of strings


## Source code in `vllm/envs.py`


##

`env_set_with_choices(env_name, default, choices, case_sensitive=True)`

[¶](https://docs.vllm.ai#vllm.envs.env_set_with_choices)

Creates a lambda which that validates environment variable containing comma-separated values against allowed choices which returns choices as a set.

## Source code in `vllm/envs.py`


##

`env_with_choices(env_name, default, choices, case_sensitive=True)`

[¶](https://docs.vllm.ai#vllm.envs.env_with_choices)

Create a lambda that validates environment variable against allowed choices.

Parameters:

-

(`env_name`

[¶](https://docs.vllm.ai#vllm.envs.env_with_choices(env_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the environment variable

-

(`default`

[¶](https://docs.vllm.ai#vllm.envs.env_with_choices(default))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneDefault value if not set (can be None)

-

(`choices`

[¶](https://docs.vllm.ai#vllm.envs.env_with_choices(choices))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] |[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]List of valid string options or callable that returns list

-

(`case_sensitive`

[¶](https://docs.vllm.ai#vllm.envs.env_with_choices(case_sensitive))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether validation should be case sensitive


Returns:

## Source code in `vllm/envs.py`


##

`get_env_or_set_default(env_name, default_factory)`

[¶](https://docs.vllm.ai#vllm.envs.get_env_or_set_default)

Create a lambda that returns an environment variable value if set, or generates and sets a default value using the provided factory function.

## Source code in `vllm/envs.py`


##

`get_vllm_port()`

[¶](https://docs.vllm.ai#vllm.envs.get_vllm_port)

Get the port from VLLM_PORT environment variable.

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe port number as an integer if VLLM_PORT is set, None otherwise.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If VLLM_PORT is a URI, suggest k8s service discovery issue.


## Source code in `vllm/envs.py`


##

`is_set(name)`

[¶](https://docs.vllm.ai#vllm.envs.is_set)

Check if an environment variable is explicitly set.