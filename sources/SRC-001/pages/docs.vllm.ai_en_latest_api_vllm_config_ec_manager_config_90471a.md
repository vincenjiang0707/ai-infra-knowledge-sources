source: https://docs.vllm.ai/en/latest/api/vllm/config/ec_manager_config/
lastmod: 2026-09-24

#

`vllm.config.ec_manager_config`

[¶](https://docs.vllm.ai#vllm.config.ec_manager_config)

Classes:

-
–[EncoderCacheManagerConfig](https://docs.vllm.ai#vllm.config.ec_manager_config.EncoderCacheManagerConfig) -
–[EncoderCacheManagerMetadata](https://docs.vllm.ai#vllm.config.ec_manager_config.EncoderCacheManagerMetadata)Abstract Metadata used to communicate between the


##

`EncoderCacheManagerConfig`

[¶](https://docs.vllm.ai#vllm.config.ec_manager_config.EncoderCacheManagerConfig)

Attributes:

-
([encoder_cache_manager_cls](https://docs.vllm.ai#vllm.config.ec_manager_config.EncoderCacheManagerConfig.encoder_cache_manager_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneFully qualified class name of the custom encoder cache manager.

-
([manager_config](https://docs.vllm.ai#vllm.config.ec_manager_config.EncoderCacheManagerConfig.manager_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]Opaque configuration interpreted by the custom cache manager.