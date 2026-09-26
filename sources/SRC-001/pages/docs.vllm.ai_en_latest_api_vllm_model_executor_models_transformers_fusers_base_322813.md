source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fusers/base/
lastmod: 2026-09-24

#

`vllm.model_executor.models.transformers.fusers.base`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base)

Base classes for the Transformers backend fusers.

Classes:

-
–[BaseFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser)A detected fusion and how to apply it.

-
–[RewriteFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser)A fuser that rewrites the module's forward and rebinds it.

-
–[StackedFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser)A fuser that merges sibling projections into one stacked linear and


Functions:

-
–[fused_head_size](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.fused_head_size)The head size of

`module`

, which head counts are derived from. -
–[local_output_sizes](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.local_output_sizes)Source for the per-rank widths of the merged linear

`self.<merged_name>`

.

##

`BaseFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

A detected fusion and how to apply it.

`match`

analyses the module *class* once (cached, see `get_fusers`

); `fuse`

then applies the fusion to an instance in `recursive_replace`

, returning the module to install in its place.

Methods:

-
–[fuse](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.fuse)Apply the fusion to an already-validated

`module`

, returning the -
–[info](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.info)A human-readable description of the fusion at

`name`

, for logging. -
–[match](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.match)Match the pattern in

`graph`

, returning a fuser if found. -
–[orig_to_new_stacked](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.orig_to_new_stacked)`WeightsMapper.orig_to_new_stacked`

entries this fuser contributes -
–[validate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.validate)Whether this fuser can be applied to this

`module`

instance.

Attributes:

-
([packed_modules_mapping](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.packed_modules_mapping)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]`packed_modules_mapping`

entries this fuser contributes (none unless -
([redefines_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.redefines_forward)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`fuse`

gives the module a different forward,

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`packed_modules_mapping`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.packed_modules_mapping)

`packed_modules_mapping`

entries this fuser contributes (none unless it stacks weights).

###

`redefines_forward = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.redefines_forward)

Whether `fuse`

gives the module a different forward, by rewriting its source or by returning a different module in its place.

###

`fuse(module, prefix, vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.fuse)

Apply the fusion to an already-validated `module`

, returning the module to install in its place (mutated in place, or freshly built).

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`info(name)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.info)

###

`match(graph, module)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.match)

Match the pattern in `graph`

, returning a fuser if found.

###

`orig_to_new_stacked(prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.orig_to_new_stacked)

`WeightsMapper.orig_to_new_stacked`

entries this fuser contributes (none unless it stacks weights).

###

`validate(module, vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser.validate)

##

`RewriteFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser)

Bases: [BaseFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.BaseFuser)

A fuser that rewrites the module's forward and rebinds it.

`match`

and `update_forward`

analyse the class once; `fuse`

swaps the submodules and binds the compiled forward on an instance in place, so it keeps its class and any attribute the fusion does not consume.

Methods:

-
–[fuse](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.fuse)Fuse an already-validated

`module`

in place (see`Fusers.__getitem__`

). -
–[update_attrs](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.update_attrs)Replace

`module`

's submodules with their vLLM equivalents. -
–[update_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.update_forward)Rewrite and compile

`type(module)`

's forward source.

Attributes:

-
([fused_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.fused_forward)

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)The compiled rewritten forward, set by

`update_forward`

. -
([source_cls](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.source_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Class of the HF module the fused projections belonged to (for logging).


## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`fused_forward = field(init=False, repr=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.fused_forward)

The compiled rewritten forward, set by `update_forward`

.

###

`source_cls`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.source_cls)

Class of the HF module the fused projections belonged to (for logging).

###

`fuse(module, prefix, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.fuse)

Fuse an already-validated `module`

in place (see `Fusers.__getitem__`

).

Builds the merged submodule and binds the compiled forward.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`update_attrs(module, prefix, vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.update_attrs)

Replace `module`

's submodules with their vLLM equivalents.

###

`update_forward(module)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser.update_forward)

Rewrite and compile `type(module)`

's forward source.

Raises if the source does not admit the rewrite (fusion is then skipped).

##

`StackedFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser)

Bases: [RewriteFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.RewriteFuser)

A fuser that merges sibling projections into one stacked linear and rewrites the forward to call it.

Methods:

-
–[orig_to_new_stacked](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.orig_to_new_stacked)`WeightsMapper.orig_to_new_stacked`

entries for one fused instance.

Attributes:

-
([merged_cls_name](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.merged_cls_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the vLLM class the merged projection becomes (for logging).

-
([merged_name](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.merged_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Attribute name of the merged module created by

`update_attrs`

. -
([packed_modules_mapping](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.packed_modules_mapping)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]`{merged_name: [projection names]}`

so quantization can unpack the -
([shards](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.shards)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[ShardId](https://docs.vllm.ai/utils/#vllm.model_executor.models.utils.ShardId)]]Each projection's original name and its shard id in the merged module.


## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


|
|

###

`merged_cls_name`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.merged_cls_name)

Name of the vLLM class the merged projection becomes (for logging).

###

`merged_name`

`abstractmethod`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.merged_name)

Attribute name of the merged module created by `update_attrs`

.

###

`packed_modules_mapping`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.packed_modules_mapping)

`{merged_name: [projection names]}`

so quantization can unpack the fused layer into its per-shard configs.

###

`shards`

`abstractmethod`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.shards)

Each projection's original name and its shard id in the merged module.

Source for both `orig_to_new_stacked`

and `packed_modules_mapping`

.

###

`_check_input_stable(funcdef, module, calls, block, indices)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser._check_input_stable)

Raise unless hoisting the merged GEMM preserves what it reads.

Fusing moves every projection to one call at `min(indices)`

, so the merged GEMM reads the input once, up front, where the last of `calls`

would have read it later. That holds only if nothing in between changes the input, and a change need not name it: writing any view that shares its storage changes it too. Both halves of the check over-approximate, since a false hit costs a fusion while a miss returns wrong numbers.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`_splice_merged_split(funcdef, calls, block, index)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser._splice_merged_split)

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

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser._unguarded_calls)

One `self.<name>(arg)`

call per projection, existence guards folded.

`update_attrs`

deletes the projections it merges, so any reference to one beyond its call site must be a guard on its existence; folding those to their constant value keeps the rewritten forward off a name that no longer exists. A reference that is not such a guard raises, so fusion is skipped.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


###

`orig_to_new_stacked(prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.StackedFuser.orig_to_new_stacked)

`WeightsMapper.orig_to_new_stacked`

entries for one fused instance.

Maps each checkpoint name to `(merged_name, shard_id)`

, keyed by qualname so only this exact layer is remapped, never a same-named projection elsewhere (e.g. an unfused MoE expert's `gate_proj`

).

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


##

`fused_head_size(module, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.fused_head_size)

The head size of `module`

, which head counts are derived from.

Prefer the module's own `head_dim`

, which Transformers sets per instance: the model-wide value is the largest head size across layers, so on a heterogeneous checkpoint it would divide out the wrong number of heads, and it is the text head size, so it does not describe a vision tower at all.

## Source code in `vllm/model_executor/models/transformers/fusers/base.py`


##

`local_output_sizes(merged_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.base.local_output_sizes)

Source for the per-rank widths of the merged linear `self.<merged_name>`

.