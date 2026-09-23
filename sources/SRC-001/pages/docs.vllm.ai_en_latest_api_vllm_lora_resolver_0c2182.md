source: https://docs.vllm.ai/en/latest/api/vllm/lora/resolver/
lastmod: 2026-09-23

#

`vllm.lora.resolver`

[¶](https://docs.vllm.ai#vllm.lora.resolver)

Classes:

-
–[LoRAResolver](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver)Base class for LoRA adapter resolvers.


##

`LoRAResolver`

[¶](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for LoRA adapter resolvers.

This class defines the interface for resolving and fetching LoRA adapters. Implementations of this class should handle the logic for locating and downloading LoRA adapters from various sources (e.g. S3, cloud storage, etc.).

Methods:

-
–[resolve_lora](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver.resolve_lora)Abstract method to resolve and fetch a LoRA model adapter.


## Source code in `vllm/lora/resolver.py`


###

`resolve_lora(base_model_name, lora_name)`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver.resolve_lora)

Abstract method to resolve and fetch a LoRA model adapter.

Implements logic to locate and download LoRA adapter based on the name. Implementations might fetch from a blob storage or other sources.

Parameters:

-

(`base_model_name`

[¶](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver.resolve_lora(base_model_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name/identifier of the base model to resolve.

-

(`lora_name`

[¶](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver.resolve_lora(lora_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name/identifier of the LoRA model to resolve.


Returns:

-

–[LoRARequest](https://docs.vllm.ai/request/#vllm.lora.request.LoRARequest)| NoneOptional[LoRARequest]: The resolved LoRA model information, or None

-

–[LoRARequest](https://docs.vllm.ai/request/#vllm.lora.request.LoRARequest)| Noneif the LoRA model cannot be found.


## Source code in `vllm/lora/resolver.py`


##

`_LoRAResolverRegistry`

`dataclass`

[¶](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry)

Methods:

-
–[get_resolver](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.get_resolver)Get a registered resolver instance by name.

-
–[get_supported_resolvers](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.get_supported_resolvers)Get all registered resolver names.

-
–[register_resolver](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.register_resolver)Register a LoRA resolver.


## Source code in `vllm/lora/resolver.py`


###

`get_resolver(resolver_name)`

[¶](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.get_resolver)

Get a registered resolver instance by name.

Parameters:

Returns:

-

–[LoRAResolver](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver)The resolver instance.


Raises:

-

–[KeyError](https://docs.python.org/3/builtins/exceptions.html#KeyError)If the resolver is not found in the registry.


## Source code in `vllm/lora/resolver.py`


###

`get_supported_resolvers()`

[¶](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.get_supported_resolvers)

###

`register_resolver(resolver_name, resolver)`

[¶](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.register_resolver)

Register a LoRA resolver.

Parameters:

-

(`resolver_name`

[¶](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.register_resolver(resolver_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name to register the resolver under.

-

(`resolver`

[¶](https://docs.vllm.ai#vllm.lora.resolver._LoRAResolverRegistry.register_resolver(resolver))

) –[LoRAResolver](https://docs.vllm.ai#vllm.lora.resolver.LoRAResolver)The LoRA resolver instance to register.