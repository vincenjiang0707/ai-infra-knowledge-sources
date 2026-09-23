source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fusers/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.fusers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers)

Concrete fusers for the Transformers modeling backend.

Modules:

-
–[attention](https://docs.vllm.ai/attention/#vllm.model_executor.models.transformers.fusers.attention)Attention fuser: the module that dispatches to the attention interface.

-
–[base](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base)Base classes for the Transformers backend fusers.

-
–[glu](https://docs.vllm.ai/glu/#vllm.model_executor.models.transformers.fusers.glu)GLU projection fuser:

`act(gate(x)) * up(x)`

-> a fused gate/up linear. -
–[merged_column](https://docs.vllm.ai/merged_column/#vllm.model_executor.models.transformers.fusers.merged_column)Fuser for parallel linear projections.

-
–[mla](https://docs.vllm.ai/mla/#vllm.model_executor.models.transformers.fusers.mla)MLA fuser: adapt a Transformers MLA attention module for vLLM's MLA layer.

-
–[moe](https://docs.vllm.ai/moe/#vllm.model_executor.models.transformers.fusers.moe)MoE fuser: route an HF MoE block through

`FusedMoE`

with vLLM's own routing. -
–[packed_qkv](https://docs.vllm.ai/packed_qkv/#vllm.model_executor.models.transformers.fusers.packed_qkv)Packed-QKV fuser:

`c_attn(x).split((q, kv, kv))`

-> a`QKVParallelLinear`

. -
–[qkv](https://docs.vllm.ai/qkv/#vllm.model_executor.models.transformers.fusers.qkv)QKV projection fuser:

`q(x), k(x), v(x)`

-> a fused qkv linear + split. -
–[rms_norm](https://docs.vllm.ai/rms_norm/#vllm.model_executor.models.transformers.fusers.rms_norm)RMSNorm fuser: detect the norm structurally and swap in vLLM's fused RMSNorm.


Classes:

-
–[AttentionFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser)A module that dispatches through the Transformers attention interface.

-
–[BaseFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser)A detected fusion and how to apply it.

-
–[GLUFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser)Fuser for the GLU pattern

`act(gate(x)) * up(x)`

. -
–[MLAFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MLAFuser)Fuser for the MLA attention pattern.

-
–[MergedColumnParallelFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser)Fuser for merging column-parallel linear projections.

-
–[MoEBlockFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser)Fuser for MoE block

`experts`

,`gate`

and`shared_experts`

(optional). -
–[PackedQKVFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser)Fuser for attention with q, k and v packed into one projection.

-
–[QKVFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser)Fuser for the attention QKV pattern

`q(x), k(x), v(x)`

. -
–[RMSNormFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser)Fuser for RMSNorm patterns, including Gemma-style zero-centered weights.

-
–[RewriteFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser)A fuser that rewrites the module's forward and rebinds it.

-
–[StackedFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser)A fuser that merges sibling projections into one stacked linear and


##

`AttentionFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser)

Bases: [BaseFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

A module that dispatches through the Transformers attention interface.

Methods:

-
–[layer_index](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.layer_index)The layer

`module`

computes attention for, if it declares one. -
–[scale](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.scale)The softmax scale

`module`

passes to the interface, or`None`

. -
–[sinks](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.sinks)The per-head sink tensor

`module`

passes to the interface, or`None`

. -
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.validate)Whether

`module`

will actually dispatch to vLLM.

Attributes:

-
([s_aux_expr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.s_aux_expr)`expr | None`

) –Source of the

`s_aux=`

the module hands the interface, if it hands one. -
([scale_expr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.scale_expr)`expr | None`

) –Source of the

`scaling=`

the module hands the interface, if it hands one. -
([source_cls](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.source_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Class of the HF module that dispatches (for logging).


## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


|
|

###

`s_aux_expr = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.s_aux_expr)

Source of the `s_aux=`

the module hands the interface, if it hands one.

###

`scale_expr = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.scale_expr)

Source of the `scaling=`

the module hands the interface, if it hands one.

###

`source_cls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.source_cls)

Class of the HF module that dispatches (for logging).

###

`layer_index(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.layer_index)

The layer `module`

computes attention for, if it declares one.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


###

`scale(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.scale)

The softmax scale `module`

passes to the interface, or `None`

.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


###

`sinks(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.sinks)

The per-head sink tensor `module`

passes to the interface, or `None`

.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


###

`validate(module, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.AttentionFuser.validate)

Whether `module`

will actually dispatch to vLLM.

## Source code in `vllm/model_executor/models/transformers/fusers/attention.py`


##

`BaseFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

A detected fusion and how to apply it.

`match`

analyses the module *class* once (cached, see `get_fusers`

); `fuse`

then applies the fusion to an instance in `recursive_replace`

, returning the module to install in its place.

Methods:

-
–[fuse](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.fuse)Apply the fusion to an already-validated

`module`

, returning the -
–[info](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.info)A human-readable description of the fusion at

`name`

, for logging. -
–[match](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.match)Match the pattern in

`graph`

, returning a fuser if found. -
–[orig_to_new_stacked](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.orig_to_new_stacked)`WeightsMapper.orig_to_new_stacked`

entries this fuser contributes -
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.validate)Whether this fuser can be applied to this

`module`

instance.

Attributes:

-
([packed_modules_mapping](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.packed_modules_mapping)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]`packed_modules_mapping`

entries this fuser contributes (none unless -
([redefines_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.redefines_forward)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`fuse`

gives the module a different forward,

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`packed_modules_mapping`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.packed_modules_mapping)

`packed_modules_mapping`

entries this fuser contributes (none unless it stacks weights).

###

`redefines_forward = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.redefines_forward)

Whether `fuse`

gives the module a different forward, by rewriting its source or by returning a different module in its place.

###

`fuse(module, prefix, vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.fuse)

Apply the fusion to an already-validated `module`

, returning the module to install in its place (mutated in place, or freshly built).

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`info(name)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.info)

###

`match(graph, module)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.match)

Match the pattern in `graph`

, returning a fuser if found.

###

`orig_to_new_stacked(prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.orig_to_new_stacked)

`WeightsMapper.orig_to_new_stacked`

entries this fuser contributes (none unless it stacks weights).

###

`validate(module, vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.BaseFuser.validate)

##

`GLUFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser)

Bases: [MergedColumnParallelFuser](https://docs.vllm.ai/merged_column/#vllm.model_executor.models.transformers.fusers.merged_column.MergedColumnParallelFuser)

Fuser for the GLU pattern `act(gate(x)) * up(x)`

.

Methods:

-
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser.update_forward)Replace

`act(gate(x)) * up(x)`

with`act(gate_up(x))`

in source.

## Source code in `vllm/model_executor/models/transformers/fusers/glu.py`


|
|

###

`_get_act_and_mul(act)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser._get_act_and_mul)

Get the `...AndMul`

equivalent of a Transformers activation module.

## Source code in `vllm/model_executor/models/transformers/fusers/glu.py`


###

`_get_act_and_mul_name(act)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser._get_act_and_mul_name)

Get the name of `act`

if it has an `...AndMul`

equivalent.

## Source code in `vllm/model_executor/models/transformers/fusers/glu.py`


###

`_get_glu_nodes(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser._get_glu_nodes)

Search graph for the GLU pattern `act(gate(x)) * up(x)`

.

## Source code in `vllm/model_executor/models/transformers/fusers/glu.py`


###

`_is_act_of_gate(node, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser._is_act_of_gate)

Is node `act(gate(x))`

where `gate`

is linear and `act`

is not linear.

## Source code in `vllm/model_executor/models/transformers/fusers/glu.py`


###

`update_forward(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.GLUFuser.update_forward)

Replace `act(gate(x)) * up(x)`

with `act(gate_up(x))`

in source.

## Source code in `vllm/model_executor/models/transformers/fusers/glu.py`


##

`MLAFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MLAFuser)

Bases: [StackedFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.StackedFuser)

Fuser for the MLA attention pattern.

Methods:

-
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MLAFuser.update_forward)Merge

`q_a_proj`

and`kv_a_proj`

into one fused down proj then split.

Attributes:

-
([shards](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MLAFuser.shards)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[ShardId](https://docs.vllm.ai/utils/#vllm.model_executor.models.utils.ShardId)]]`q_a_proj`

and`kv_a_proj_with_mqa`

stack into one down-projection.

## Source code in `vllm/model_executor/models/transformers/fusers/mla.py`


|
|

###

`shards`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MLAFuser.shards)

`q_a_proj`

and `kv_a_proj_with_mqa`

stack into one down-projection.

###

`update_forward(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MLAFuser.update_forward)

Merge `q_a_proj`

and `kv_a_proj`

into one fused down proj then split. Bypass the KV expansion method so the compressed latent reaches the `vllm_mla`

attention interface unexpanded.

## Source code in `vllm/model_executor/models/transformers/fusers/mla.py`


##

`MergedColumnParallelFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser)

Bases: [StackedFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.StackedFuser)

Fuser for merging column-parallel linear projections.

Methods:

-
–[match](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.match)Fuse the module's sibling linears when there is only one such group.

-
–[update_attrs](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.update_attrs)Replace the module's parallel linears with one merged projection.

-
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.update_forward)Replace the parallel calls with one merged call and split.

-
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.validate)Check that the parallel linears are compatible for merging.


Attributes:

-
([merged_name](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.merged_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Programmatic name for the merged projection, based on the original names.


## Source code in `vllm/model_executor/models/transformers/fusers/merged_column.py`


|
|

###

`merged_name`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.merged_name)

Programmatic name for the merged projection, based on the original names.

###

`match(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.match)

Fuse the module's sibling linears when there is only one such group.

## Source code in `vllm/model_executor/models/transformers/fusers/merged_column.py`


###

`update_attrs(module, prefix, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.update_attrs)

Replace the module's parallel linears with one merged projection.

## Source code in `vllm/model_executor/models/transformers/fusers/merged_column.py`


###

`update_forward(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.update_forward)

Replace the parallel calls with one merged call and split.

## Source code in `vllm/model_executor/models/transformers/fusers/merged_column.py`


###

`validate(module, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MergedColumnParallelFuser.validate)

Check that the parallel linears are compatible for merging.

## Source code in `vllm/model_executor/models/transformers/fusers/merged_column.py`


##

`MoEBlockFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser)

Fuser for MoE block `experts`

, `gate`

and `shared_experts`

(optional).

Methods:

-
–[gate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser.gate)Rebuild the HF gate as a

`GateLinear`

for vLLM's fused MoE. -
–[rewrite_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser.rewrite_forward)Rewrite

`moe_block.forward`

to route through vLLM's fused MoE. -
–[shared_experts](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser.shared_experts)Build the HF shared expert (and its optional gate)


## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


|
|

###

`_match_router(gate)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser._match_router)

Matches `topk(score(linear(x)))`

, `score`

being `softmax`

/`sigmoid`

.

Returns the scoring function and the dtype the router computes in.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


###

`_match_shared_experts(graph, experts)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser._match_shared_experts)

Detects the shared expert and its optional gate by dataflow.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


###

`gate(moe_block, prefix, out_dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser.gate)

Rebuild the HF gate as a `GateLinear`

for vLLM's fused MoE.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


###

`rewrite_forward(moe_block)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser.rewrite_forward)

Rewrite `moe_block.forward`

to route through vLLM's fused MoE.

###

`shared_experts(moe_block, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.MoEBlockFuser.shared_experts)

Build the HF shared expert (and its optional gate) as a `SharedExpertMLP`

for vLLM's fused MoE.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`PackedQKVFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser)

Bases: [RewriteFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.RewriteFuser)

Fuser for attention with q, k and v packed into one projection.

Methods:

-
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser.update_forward)Rewrite the split sizes to the sharded projection's per-rank widths.

-
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser.validate)Shapes must be compatible with a head-sharded packed GEMM.


## Source code in `vllm/model_executor/models/transformers/fusers/packed_qkv.py`


|
|

###

`_packed_sizes(node)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser._packed_sizes)

`(q, kv)`

from a `split((q, kv, kv), ...)`

call, if it is one.

## Source code in `vllm/model_executor/models/transformers/fusers/packed_qkv.py`


###

`_split_call(funcdef)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser._split_call)

The unique `self.<qkv_name>(...)....split((a, b, c), ...)`

call.

## Source code in `vllm/model_executor/models/transformers/fusers/packed_qkv.py`


###

`update_forward(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser.update_forward)

Rewrite the split sizes to the sharded projection's per-rank widths.

## Source code in `vllm/model_executor/models/transformers/fusers/packed_qkv.py`


###

`validate(module, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.PackedQKVFuser.validate)

Shapes must be compatible with a head-sharded packed GEMM.

## Source code in `vllm/model_executor/models/transformers/fusers/packed_qkv.py`


##

`QKVFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser)

Bases: [StackedFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.StackedFuser)

Fuser for the attention QKV pattern `q(x), k(x), v(x)`

.

Methods:

-
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser.update_forward)Replace

`q(x), k(x), v(x)`

with`qkv(x).split(sizes, -1)`

in source. -
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser.validate)Shapes must be compatible for a single merged, head-sharded GEMM.


## Source code in `vllm/model_executor/models/transformers/fusers/qkv.py`


|
|

###

`_get_qkv_nodes(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser._get_qkv_nodes)

Search `graph`

for the QKV pattern `q(x), k(x), v(x)`

.

## Source code in `vllm/model_executor/models/transformers/fusers/qkv.py`


###

`update_forward(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser.update_forward)

Replace `q(x), k(x), v(x)`

with `qkv(x).split(sizes, -1)`

in source.

A projection may be guarded by an existence check -- a `self.<proj> is (not) None`

comparison (e.g. Gemma 4's `v_proj`

) or a bare truthiness test -- which is folded to its constant value (see `bypass_existence_guard`

). The calls may sit in different branches, so the fused GEMM is inserted before the earliest of them, in the innermost block that dominates all three.

## Source code in `vllm/model_executor/models/transformers/fusers/qkv.py`


###

`validate(module, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.QKVFuser.validate)

Shapes must be compatible for a single merged, head-sharded GEMM.

## Source code in `vllm/model_executor/models/transformers/fusers/qkv.py`


##

`RMSNormFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser)

Bases: [BaseFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

Fuser for RMSNorm patterns, including Gemma-style zero-centered weights.

Methods:

-
–[fuse](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.fuse)Fuse the matched RMSNorm pattern into a vLLM fused RMSNorm CustomOp.

-
–[match](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.match)Match a graph to the RMSNorm pattern, returning a fuser if found.


Attributes:

-
([eps](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.eps)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| None`eps`

itself, when it is not held in an attribute (see`_eps_source`

). -
([eps_attr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.eps_attr)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneAttribute holding

`eps`

, read per instance in`fuse`

. -
([source_cls](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.source_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Class name of the norm this was matched from (for logging).

-
([zero_centered](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.zero_centered)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Gemma-style

`(1 + weight)`

scaling (weight initialised at zero).

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


|
|

###

`eps = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.eps)

`eps`

itself, when it is not held in an attribute (see `_eps_source`

).

###

`eps_attr = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.eps_attr)

Attribute holding `eps`

, read per instance in `fuse`

.

###

`source_cls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.source_cls)

Class name of the norm this was matched from (for logging).

###

`zero_centered`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.zero_centered)

Gemma-style `(1 + weight)`

scaling (weight initialised at zero).

###

`_eps_from_graph(graph)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser._eps_from_graph)

Extract the `eps`

constant from the graph, if present.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


###

`_eps_source(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser._eps_source)

Where `fuse`

should read `eps`

from, resolved once per class.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


###

`fuse(module, prefix, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.fuse)

Fuse the matched RMSNorm pattern into a vLLM fused RMSNorm CustomOp.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


###

`match(graph, module)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RMSNormFuser.match)

Match a graph to the RMSNorm pattern, returning a fuser if found.

## Source code in `vllm/model_executor/models/transformers/fusers/rms_norm.py`


##

`RewriteFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser)

Bases: [BaseFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

A fuser that rewrites the module's forward and rebinds it.

`match`

and `update_forward`

analyse the class once; `fuse`

swaps the submodules and binds the compiled forward on an instance in place, so it keeps its class and any attribute the fusion does not consume.

Methods:

-
–[fuse](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.fuse)Fuse an already-validated

`module`

in place (see`Fusers.__getitem__`

). -
–[update_attrs](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.update_attrs)Replace

`module`

's submodules with their vLLM equivalents. -
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.update_forward)Rewrite and compile

`type(module)`

's forward source.

Attributes:

-
([fused_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.fused_forward)

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)The compiled rewritten forward, set by

`update_forward`

. -
([source_cls](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.source_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Class of the HF module the fused projections belonged to (for logging).


## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`fused_forward = field(init=False, repr=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.fused_forward)

The compiled rewritten forward, set by `update_forward`

.

###

`source_cls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.source_cls)

Class of the HF module the fused projections belonged to (for logging).

###

`fuse(module, prefix, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.fuse)

Fuse an already-validated `module`

in place (see `Fusers.__getitem__`

).

Builds the merged submodule and binds the compiled forward.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`update_attrs(module, prefix, vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.update_attrs)

Replace `module`

's submodules with their vLLM equivalents.

###

`update_forward(module)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.RewriteFuser.update_forward)

Rewrite and compile `type(module)`

's forward source.

Raises if the source does not admit the rewrite (fusion is then skipped).

##

`StackedFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser)

Bases: [RewriteFuser](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.fusers.base.RewriteFuser)

A fuser that merges sibling projections into one stacked linear and rewrites the forward to call it.

Methods:

-
–[orig_to_new_stacked](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.orig_to_new_stacked)`WeightsMapper.orig_to_new_stacked`

entries for one fused instance.

Attributes:

-
([merged_cls_name](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.merged_cls_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the vLLM class the merged projection becomes (for logging).

-
([merged_name](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.merged_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Attribute name of the merged module created by

`update_attrs`

. -
([packed_modules_mapping](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.packed_modules_mapping)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]`{merged_name: [projection names]}`

so quantization can unpack the -
([shards](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.shards)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[ShardId](https://docs.vllm.ai/utils/#vllm.model_executor.models.utils.ShardId)]]Each projection's original name and its shard id in the merged module.


## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


|
|

###

`merged_cls_name`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.merged_cls_name)

Name of the vLLM class the merged projection becomes (for logging).

###

`merged_name`

`abstractmethod`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.merged_name)

Attribute name of the merged module created by `update_attrs`

.

###

`packed_modules_mapping`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.packed_modules_mapping)

`{merged_name: [projection names]}`

so quantization can unpack the fused layer into its per-shard configs.

###

`shards`

`abstractmethod`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.shards)

Each projection's original name and its shard id in the merged module.

Source for both `orig_to_new_stacked`

and `packed_modules_mapping`

.

###

`_check_input_stable(funcdef, module, calls, block, indices)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser._check_input_stable)

Raise unless hoisting the merged GEMM preserves what it reads.

Fusing moves every projection to one call at `min(indices)`

, so the merged GEMM reads the input once, up front, where the last of `calls`

would have read it later. That holds only if nothing in between changes the input, and a change need not name it: writing any view that shares its storage changes it too. Both halves of the check over-approximate, since a false hit costs a fusion while a miss returns wrong numbers.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`_splice_merged_split(funcdef, calls, block, index)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser._splice_merged_split)

Insert `temps = self.<merged_name>(arg).split(sizes, -1)`

at `block[index]`

and replace each of `calls`

with its temp name.

`calls`

must share one input argument; `block[index]`

must be where they are (or would be) evaluated. Raises if a generated temporary would shadow an existing name in `funcdef`

.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`_unguarded_calls(funcdef, names)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser._unguarded_calls)

One `self.<name>(arg)`

call per projection, existence guards folded.

`update_attrs`

deletes the projections it merges, so any reference to one beyond its call site must be a guard on its existence; folding those to their constant value keeps the rewritten forward off a name that no longer exists. A reference that is not such a guard raises, so fusion is skipped.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`orig_to_new_stacked(prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.StackedFuser.orig_to_new_stacked)

`WeightsMapper.orig_to_new_stacked`

entries for one fused instance.

Maps each checkpoint name to `(merged_name, shard_id)`

, keyed by qualname so only this exact layer is remapped, never a same-named projection elsewhere (e.g. an unfused MoE expert's `gate_proj`

).