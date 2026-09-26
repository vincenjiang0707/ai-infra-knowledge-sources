source: https://docs.vllm.ai/en/latest/api/vllm/config/utils/
lastmod: 2026-09-24

#

`vllm.config.utils`

[¶](https://docs.vllm.ai#vllm.config.utils)

Utility functions for vLLM config dataclasses.

Classes:

-
–[Range](https://docs.vllm.ai#vllm.config.utils.Range)A range of numbers.


Functions:

-
–[compute_hash_cached](https://docs.vllm.ai#vllm.config.utils.compute_hash_cached)Cache config.compute_hash() by object identity.

-
–[config](https://docs.vllm.ai#vllm.config.utils.config)Decorator to create a pydantic dataclass with default config. The default config

-
–[get_attr_docs](https://docs.vllm.ai#vllm.config.utils.get_attr_docs)Get any docstrings placed after attribute assignments in a class body.

-
–[get_field](https://docs.vllm.ai#vllm.config.utils.get_field)Get the default factory field of a dataclass by name. Used for getting

-
–[get_from_deprecated_env_if_set](https://docs.vllm.ai#vllm.config.utils.get_from_deprecated_env_if_set)Get value from deprecated environment variable with warning.

-
–[get_hash_factors](https://docs.vllm.ai#vllm.config.utils.get_hash_factors)Gets the factors used for hashing a config class.

-
–[getattr_iter](https://docs.vllm.ai#vllm.config.utils.getattr_iter)A helper function that retrieves an attribute from an object which may

-
–[hash_factors](https://docs.vllm.ai#vllm.config.utils.hash_factors)Return a SHA-256 hex digest of the canonical items structure.

-
–[normalize_value](https://docs.vllm.ai#vllm.config.utils.normalize_value)Return a stable, JSON-serializable canonical form for hashing.

-
–[replace](https://docs.vllm.ai#vllm.config.utils.replace)Like

,`dataclasses.replace`

-
–[set_from_deprecated_env_if_set](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set)Set object field from deprecated environment variable with warning.


##

`Range`

[¶](https://docs.vllm.ai#vllm.config.utils.Range)

A range of numbers. Inclusive of start, inclusive of end.

## Source code in `vllm/config/utils.py`


##

`compute_hash_cached(config)`

[¶](https://docs.vllm.ai#vllm.config.utils.compute_hash_cached)

Cache config.compute_hash() by object identity.

Config objects (ModelConfig, etc.) are long-lived singletons that never mutate after construction, but compute_hash() is expensive (JSON serialization + SHA-256). This utility avoids recomputing the hash on every forward pass while keeping a single consistent key type for all lookup paths.

## Source code in `vllm/config/utils.py`


##

`config(cls=None, *, config=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.config.utils.config)

Decorator to create a pydantic dataclass with default config. The default config for the dataclass forbids extra fields.

All config classes in vLLM should use this decorator.

Parameters:

-

(`cls`

[¶](https://docs.vllm.ai#vllm.config.utils.config(cls))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[ConfigT] | None`None`

) –The class to decorate

-

(`config`

[¶](https://docs.vllm.ai#vllm.config.utils.config(config))`ConfigDict | None`

, default:`None`

) –The pydantic ConfigDict to use. If provided, it will be merged with the default config.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.config.utils.config(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Additional arguments to pass to pydantic.dataclass.


## Source code in `vllm/config/utils.py`


##

`get_attr_docs(cls)`

[¶](https://docs.vllm.ai#vllm.config.utils.get_attr_docs)

Get any docstrings placed after attribute assignments in a class body.

https://davidism.com/mit-license/

## Source code in `vllm/config/utils.py`


##

`get_field(cls, name)`

[¶](https://docs.vllm.ai#vllm.config.utils.get_field)

Get the default factory field of a dataclass by name. Used for getting default factory fields in `EngineArgs`

.

## Source code in `vllm/config/utils.py`


##

`get_from_deprecated_env_if_set(env_name, removal_version, field_name=None)`

[¶](https://docs.vllm.ai#vllm.config.utils.get_from_deprecated_env_if_set)

Get value from deprecated environment variable with warning.

Parameters:

-

(`env_name`

[¶](https://docs.vllm.ai#vllm.config.utils.get_from_deprecated_env_if_set(env_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the deprecated environment variable

-

(`removal_version`

[¶](https://docs.vllm.ai#vllm.config.utils.get_from_deprecated_env_if_set(removal_version))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Version when it will be removed

-

(`field_name`

[¶](https://docs.vllm.ai#vllm.config.utils.get_from_deprecated_env_if_set(field_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Name of the field to suggest as alternative


Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe environment variable value if set, None otherwise


## Source code in `vllm/config/utils.py`


##

`get_hash_factors(config, ignored_factors)`

[¶](https://docs.vllm.ai#vllm.config.utils.get_hash_factors)

Gets the factors used for hashing a config class. - Includes all dataclass fields not in `ignored_factors`

. - Errors on non-normalizable values.

## Source code in `vllm/config/utils.py`


##

`getattr_iter(object, names, default=None, default_factory=None, warn=False)`

[¶](https://docs.vllm.ai#vllm.config.utils.getattr_iter)

A helper function that retrieves an attribute from an object which may have multiple possible names. This is useful when fetching attributes from arbitrary `transformers.PreTrainedConfig`

instances.

In the case where the first name in `names`

is the preferred name, and any other names are deprecated aliases, setting `warn=True`

will log a warning when a deprecated name is used.

## Source code in `vllm/config/utils.py`


##

`hash_factors(items)`

[¶](https://docs.vllm.ai#vllm.config.utils.hash_factors)

Return a SHA-256 hex digest of the canonical items structure.

##

`normalize_value(x)`

[¶](https://docs.vllm.ai#vllm.config.utils.normalize_value)

Return a stable, JSON-serializable canonical form for hashing. Order: primitives, special types (Enum, callable, torch.dtype, Path), then generic containers (Mapping/Set/Sequence) with recursion.

## Source code in `vllm/config/utils.py`


|
|

##

`replace(dataclass_instance, /, **kwargs)`

[¶](https://docs.vllm.ai#vllm.config.utils.replace)

Like [ dataclasses.replace](https://docs.python.org/3/library/dataclasses.html#dataclasses.replace), but compatible with Pydantic dataclasses which use

`pydantic.fields.Field`

instead of `dataclasses.field`

## Source code in `vllm/config/utils.py`


##

`set_from_deprecated_env_if_set(config, env_name, removal_version, field_name, to_bool=False, to_int=False)`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set)

Set object field from deprecated environment variable with warning.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set(config))`ConfigT`

) –Config object to set the field on

-

(`env_name`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set(env_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the deprecated environment variable

-

(`removal_version`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set(removal_version))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Version when the env var will be removed

-

(`field_name`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set(field_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the field to set

-

(`to_bool`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set(to_bool))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to convert the environment variable value to boolean

-

(`to_int`

[¶](https://docs.vllm.ai#vllm.config.utils.set_from_deprecated_env_if_set(to_int))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to convert the environment variable value to integer


Returns: None