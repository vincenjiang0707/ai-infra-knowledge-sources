source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.oracle`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle)

Modules:

-
–[base](https://docs.vllm.ai/base/#vllm.model_executor.layers.fused_moe.oracle.base)Abstract base class for MoE kernel oracles.

-
–[fp8](https://docs.vllm.ai/fp8/#vllm.model_executor.layers.fused_moe.oracle.fp8) -
–[int8](https://docs.vllm.ai/int8/#vllm.model_executor.layers.fused_moe.oracle.int8) -
–[int_wna16](https://docs.vllm.ai/int_wna16/#vllm.model_executor.layers.fused_moe.oracle.int_wna16) -
–[mxfp4](https://docs.vllm.ai/mxfp4/#vllm.model_executor.layers.fused_moe.oracle.mxfp4) -
–[mxfp8](https://docs.vllm.ai/mxfp8/#vllm.model_executor.layers.fused_moe.oracle.mxfp8) -
–[nvfp4](https://docs.vllm.ai/nvfp4/#vllm.model_executor.layers.fused_moe.oracle.nvfp4) -
–[unquantized](https://docs.vllm.ai/unquantized/#vllm.model_executor.layers.fused_moe.oracle.unquantized) -
–[w4a8_int8](https://docs.vllm.ai/w4a8_int8/#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8)

Classes:

-
–[MoEKernelOracle](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle)Abstract base for MoE kernel-selection oracles.

-
–[UnquantizedMoEKernelOracle](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.UnquantizedMoEKernelOracle)Class-based view of the unquantized MoE kernel oracle.


##

`MoEKernelOracle`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle)

Abstract base for MoE kernel-selection oracles.

Concrete oracles MUST implement: `backend_enum_cls`

, `get_priority_backends`

, `backend_to_kernel_cls`

, `map_backend`

, `select_backend`

, `make_kernel`

.

Concrete oracles MAY override: `convert_to_kernel_format`

, `make_quant_config`

. The base class provides default implementations that are appropriate for oracles which do not need them (e.g. `make_quant_config`

raises on the unquantized oracle).

Methods:

-
–[backend_enum_cls](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.backend_enum_cls)Return the concrete

`Enum`

class enumerating this oracle's -
–[backend_to_kernel_cls](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.backend_to_kernel_cls)Map a backend enum value to its concrete

`FusedMoEExperts`

-
–[convert_to_kernel_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.convert_to_kernel_format)Shuffle weights into the layout expected by

`backend`

. -
–[get_priority_backends](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.get_priority_backends)Return platform-appropriate backends in priority order for

-
–[make_kernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.make_kernel)Construct the

`FusedMoEKernel`

(Prepare/Finalize + Experts -
–[make_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.make_quant_config)Build a

`FusedMoEQuantConfig`

for this oracle. -
–[map_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.map_backend)Map a user-facing

`MoEBackend`

(from the runner config) to -
–[select_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.select_backend)Primary entry point: choose the best supported backend for


## Source code in `vllm/model_executor/layers/fused_moe/oracle/base.py`


|
|

###

`backend_enum_cls()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.backend_enum_cls)

Return the concrete `Enum`

class enumerating this oracle's backends (e.g. `UnquantizedMoeBackend`

, `Fp8MoeBackend`

).

###

`backend_to_kernel_cls(backend)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.backend_to_kernel_cls)

Map a backend enum value to its concrete `FusedMoEExperts`

subclasses, in selection priority order.

###

`convert_to_kernel_format(backend, moe_config, w13_weight, w2_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.convert_to_kernel_format)

Shuffle weights into the layout expected by `backend`

.

Default implementation returns the inputs unchanged. Oracles whose backends need weight permutation should override this (e.g. `UnquantizedMoEKernelOracle`

handles AITER and FlashInfer layouts).

`moe_config`

carries MoE-layer state (e.g. `is_act_and_mul`

) that the conversion needs without coupling the oracle to a `Module`

reference. Quantized oracles whose conversion additionally needs scales / zero-points / block shapes will override with a wider signature (and ultimately a per-oracle config object — tracked in the #37753 follow-up PRs).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/base.py`


###

`get_priority_backends(moe_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.get_priority_backends)

Return platform-appropriate backends in priority order for this `moe_config`

.

###

`make_kernel(quant_config, moe_config, backend, experts_cls, routing_tables=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.make_kernel)

Construct the `FusedMoEKernel`

(Prepare/Finalize + Experts combinator) for the chosen backend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/base.py`


###

`make_quant_config(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.make_quant_config)

Build a `FusedMoEQuantConfig`

for this oracle.

Quantized oracles (fp8, nvfp4, mxfp4, ...) override this with the appropriate signature for their quantization scheme. Unquantized oracles inherit the default, which raises because there is no quantization-specific config to build.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/base.py`


###

`map_backend(runner_backend)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.map_backend)

Map a user-facing `MoEBackend`

(from the runner config) to this oracle's enum.

###

`select_backend(moe_config, weight_key=None, activation_key=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.MoEKernelOracle.select_backend)

Primary entry point: choose the best supported backend for the given `moe_config`

.

`weight_key`

/ `activation_key`

carry the quantization scheme of the weights and activations and are consumed by quantized oracles (fp8, nvfp4, int8, ...) to disambiguate backends. The unquantized oracle ignores them. Subclasses with additional selection inputs (e.g. int_wna16 needs `weight_bits`

, fp8 needs `allow_vllm_cutlass`

) widen the signature in their override; a per-oracle config object is the longer-term target tracked in the #37753 follow-up PRs.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/base.py`


##

`UnquantizedMoEKernelOracle`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.UnquantizedMoEKernelOracle)

Bases: [MoEKernelOracle](https://docs.vllm.ai/base/#vllm.model_executor.layers.fused_moe.oracle.base.MoEKernelOracle)[UnquantizedMoeBackend]

Class-based view of the unquantized MoE kernel oracle.

Each method delegates to its module-level counterpart so that instantiating and calling this class is bit-identical to calling the standalone functions. Follow-up PRs may move logic from the module-level functions into these methods.