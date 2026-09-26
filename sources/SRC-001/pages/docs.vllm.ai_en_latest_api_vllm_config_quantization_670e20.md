source: https://docs.vllm.ai/en/latest/api/vllm/config/quantization/
lastmod: 2026-09-24

#

`vllm.config.quantization`

[¶](https://docs.vllm.ai#vllm.config.quantization)

Classes:

-
–[QuantSpec](https://docs.vllm.ai#vllm.config.quantization.QuantSpec)Quantization spec for one layer kind (linear or MoE).

-
–[QuantizationConfigArgs](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs)User-facing quantization configuration.


Functions:

-
–[resolve_quantization_config](https://docs.vllm.ai#vllm.config.quantization.resolve_quantization_config)Resolve

`--quantization`

shorthand and`--quantization-config`

into a

##

`QuantSpec`

[¶](https://docs.vllm.ai#vllm.config.quantization.QuantSpec)

Quantization spec for one layer kind (linear or MoE).

`None`

on either side means the method class falls back to its own default (typically inherited from the checkpoint, or unquantized for online).

Attributes:

-
([activation](https://docs.vllm.ai#vllm.config.quantization.QuantSpec.activation)`QuantKeyField`

) –Activation quantization key, or a name from QUANT_KEY_NAMES.

-
([weight](https://docs.vllm.ai#vllm.config.quantization.QuantSpec.weight)`QuantKeyField`

) –Weight quantization key, or a name from QUANT_KEY_NAMES.


## Source code in `vllm/config/quantization.py`


##

`QuantizationConfigArgs`

[¶](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs)

User-facing quantization configuration.

See `docs/features/quantization/online.md`

for the schema and shorthand string forms accepted on `linear`

and `moe`

.

Attributes:

-
([ignore](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.ignore)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Layers to skip quantization for. Online quantization also supports

-
([linear](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.linear)

) –[QuantSpec](https://docs.vllm.ai#vllm.config.quantization.QuantSpec)| NoneSpec applied to

`LinearBase`

layers. -
([moe](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.moe)

) –[QuantSpec](https://docs.vllm.ai#vllm.config.quantization.QuantSpec)| NoneSpec applied to

`FusedMoEFactory`

layers. -
([targets](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.targets)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NonePer-layer online quantization overrides, keyed by exact layer name or


## Source code in `vllm/config/quantization.py`


|
|

###

`ignore = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.ignore)

Layers to skip quantization for. Online quantization also supports fnmatch-style patterns.

###

`linear = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.linear)

Spec applied to `LinearBase`

layers.

###

`moe = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.moe)

Spec applied to `FusedMoEFactory`

layers.

###

`targets = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.quantization.QuantizationConfigArgs.targets)

Per-layer online quantization overrides, keyed by exact layer name or regex patterns with a `re:`

, or fnmatch-style patterns for online quantization, mapping to an online shorthand name (see `_ONLINE_SHORTHANDS`

). A layer that matches no pattern is left unquantized. Mutually exclusive with `linear`

and `moe`

.

##

`resolve_quantization_config(quantization, quantization_config)`

[¶](https://docs.vllm.ai#vllm.config.quantization.resolve_quantization_config)

Resolve `--quantization`

shorthand and `--quantization-config`

into a QuantizationConfigArgs.

`quantization`

is a CLI shorthand that desugars into a base config via `_ONLINE_SHORTHANDS`

. `quantization_config`

is a dict or pre-built args object. When both are given, fields explicitly set in `quantization_config`

take precedence over the shorthand.