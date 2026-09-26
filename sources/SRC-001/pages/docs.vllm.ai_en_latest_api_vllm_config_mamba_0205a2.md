source: https://docs.vllm.ai/en/latest/api/vllm/config/mamba/
lastmod: 2026-09-24

#

`vllm.config.mamba`

[¶](https://docs.vllm.ai#vllm.config.mamba)

Classes:

-
–[MambaBackendEnum](https://docs.vllm.ai#vllm.config.mamba.MambaBackendEnum)Enumeration of supported Mamba SSU (selective state update) backends.

-
–[MambaConfig](https://docs.vllm.ai#vllm.config.mamba.MambaConfig)Configuration for Mamba SSM backends.


##

`MambaBackendEnum`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaBackendEnum)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Enumeration of supported Mamba SSU (selective state update) backends.

## Source code in `vllm/config/mamba.py`


##

`MambaConfig`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaConfig)

Configuration for Mamba SSM backends.

Methods:

-
–[validate_backend_before](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.validate_backend_before)Enable parsing of the

`backend`

enum type from string.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.backend)

) –[MambaBackendEnum](https://docs.vllm.ai#vllm.config.mamba.MambaBackendEnum)Mamba SSU backend to use.

-
([enable_stochastic_rounding](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.enable_stochastic_rounding)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable stochastic rounding when writing SSM state to fp16 cache.

-
([ssu_algorithm](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.ssu_algorithm)`MambaSSUAlgorithm | None`

) –Selective state update algorithm to use with the FlashInfer backend.

-
([stochastic_rounding_philox_rounds](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.stochastic_rounding_philox_rounds)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of Philox PRNG rounds for stochastic rounding random number


## Source code in `vllm/config/mamba.py`


###

`backend = MambaBackendEnum.TRITON`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.backend)

Mamba SSU backend to use.

###

`enable_stochastic_rounding = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.enable_stochastic_rounding)

Enable stochastic rounding when writing SSM state to fp16 cache. Uses random bits to unbias the rounding error, which can improve numerical stability for long sequences.

###

`ssu_algorithm = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.ssu_algorithm)

Selective state update algorithm to use with the FlashInfer backend. None defaults to FlashInfer's "auto" algorithm. Forced algorithms must be supported by FlashInfer for the active GPU, state dtype, and decoding mode.

###

`stochastic_rounding_philox_rounds = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.stochastic_rounding_philox_rounds)

Number of Philox PRNG rounds for stochastic rounding random number generation. 0 uses the Triton default. Higher values improve randomness quality at the cost of compute.

###

`validate_backend_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.mamba.MambaConfig.validate_backend_before)

Enable parsing of the `backend`

enum type from string.

## Source code in `vllm/config/mamba.py`


##

`_MambaBackendEnumMeta`

[¶](https://docs.vllm.ai#vllm.config.mamba._MambaBackendEnumMeta)

Bases: `EnumMeta`


Metaclass for MambaBackendEnum to provide better error messages.