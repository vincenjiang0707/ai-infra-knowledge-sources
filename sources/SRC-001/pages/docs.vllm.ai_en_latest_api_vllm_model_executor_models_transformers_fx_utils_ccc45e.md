source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fx_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.models.transformers.fx_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils)

fx tracing and forward-source rewriting for the Transformers backend fusers.

A small engine, independent of any particular pattern: trace a module's forward with `torch.fx`

(tolerating a partial graph), inspect the resulting nodes, and rewrite the forward's *source* (AST) so only matched calls change while the rest stays live Python. `fusion.py`

builds the concrete fusion patterns on top.

Functions:

-
–[aliasing_names](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.aliasing_names)`seed`

plus every name that may alias one of them. -
–[block_chain](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.block_chain)Path of (statement list, index) pairs from

`block`

down to`node`

. -
–[bypass_existence_guard](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.bypass_existence_guard)Fold a guard on

`self.<name>`

's existence to its constant value. -
–[compile_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.compile_forward)Compile

`funcdef`

in`fn`

's module so tracebacks point at the source. -
–[downstream_linear](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.downstream_linear)Nearest linear consuming

`node`

's output, walking through casts/scalings. -
–[find_node](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.find_node)The first node in

`graph`

matching`predicate`

, or`None`

. -
–[forward_input_count](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.forward_input_count)The number of tensor inputs

`cls.forward`

declares, excluding`self`

and -
–[forward_parameters](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.forward_parameters)`cls.forward`

's signature parameters, or empty if uninspectable. -
–[is_fn](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_fn)Is node

`<target>()`

. -
–[is_leaf_call](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_leaf_call)Is node a call recorded by

`_as_leaf_call`

(e.g. an attention interface). -
–[is_linear](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_linear)Is node

`nn.Linear.__call__()`

. -
–[is_method](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_method)Is node

`.<name>()`

. -
–[is_op](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_op)Is node

`<mod>.<name>()`

for torch, F, operator, or Tensor. -
–[output_value](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.output_value)The value the graph's

`output`

node returns, if the trace reached one. -
–[peel](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.peel)Strip dtype-cast wrappers (

`.to(...)`

,`.float()`

,`.type_as(...)`

). -
–[recover_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.recover_forward)Parse the source of

`cls.forward`

, ready for rewriting. -
–[replace_expr](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.replace_expr)Replace the expression

`old`

(by identity) with`new`

within`module`

. -
–[returned_linear](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.returned_linear)Name of the Linear producing the graph's (first) output value.

-
–[self_call_and_refs](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.self_call_and_refs)The unique

`self.<name>(arg)`

call, plus every other`self.<name>`

reference. -
–[single_self_call](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.single_self_call)The unique

`self.<name>(arg)`

call in`funcdef`

. -
–[trace](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.trace)Trace

`module.forward`

, returning the partial graph on failure. -
–[upstream_linear](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.upstream_linear)Nearest linear producing

`node`

, walking back through splits/reshapes. -
–[written_names](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.written_names)Names

`region`

may rebind or write through.

##

`_MODULE_CALL = nn.Module.__call__`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._MODULE_CALL)

The unpatched `nn.Module.__call__`

. During tracing fx patches it to record `call_module`

nodes; meta execution must call modules for real.

##

`_UNKNOWN = object()`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._UNKNOWN)

Sentinel meta value for proxies whose concrete value could not be inferred. Distinct from `None`

, which is a valid concrete value (e.g. `attn_weights`

).

##

`_AllLeafTracer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._AllLeafTracer)

Bases: [Tracer](https://pytorch.org/docs/stable/fx.html#torch.fx.Tracer)

Tracer that treats every submodule as a leaf.

Each child stays one `call_module`

node, so matching sees the module's own forward structure (activations aren't decomposed into e.g. `sigmoid * x`

). Every traced op is also executed on meta tensors (see `_MetaProxy`

) so shape unpacks and `*`

-splats trace through; anything else untraceable ends the trace early and the partial graph is matched.

Attributes:

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


|
|

###

`varkw = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._AllLeafTracer.varkw)

Name of the traced forward's `**kwargs`

parameter, if any.

###

`_infer_meta(kind, target, args, kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._AllLeafTracer._infer_meta)

Execute the op on meta tensors; PyTorch infers the output value.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_MetaAttribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._MetaAttribute)

Bases:

, [_MetaProxy](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._MetaProxy)`Attribute`


Attribute proxy (e.g. `x.shape`

) carrying its meta value.

`Proxy.__getattr__`

constructs `Attribute`

directly, bypassing `Tracer.proxy`

, so the meta value must be grafted on here too.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_MetaProxy`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._MetaProxy)

Bases: [Proxy](https://pytorch.org/docs/stable/fx.html#torch.fx.Proxy)

Proxy carrying the meta-tensor value of the traced expression.

Shape questions (`len`

, iteration, `.shape`

unpacks) are answered by executing each op on the meta values, so PyTorch's meta kernels are the single source of shape inference — no per-op rules.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_aliasing_reads(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._aliasing_reads)

Names `node`

reads in a way that could yield a view of them.

Metadata (`x.shape`

, `x.size(0)`

, `x.dtype`

) is ints and tuples sharing no storage with `x`

, so reaching a name only through metadata cannot alias it. Shape arithmetic is pervasive between projections, so propagating through it would taint nearly every later name.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_arg_names(call)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._arg_names)

Every name `call`

reads through its arguments.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_as_leaf_call(fn, length=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._as_leaf_call)

Wrap any callable so tracing records it as one opaque `call_function`

node.

Lets the trace continue past untraceable bodies. Only the proxy arguments carry into the node's dataflow; the rest are dropped rather than lifted into the graph. `length`

declares how many values the callable returns, so unpacking its result also traces. Called without proxies (i.e. outside tracing), the wrapper is a passthrough.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_base_name(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._base_name)

The root `Name`

of an attribute/subscript chain (`a.b[c]`

-> `a`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_call_name(call)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._call_name)

The called function's own name, without its qualifier.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_in_boolean_context(funcdef, ref)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._in_boolean_context)

Is `ref`

used only for its truth value (a test, or a `not`

operand)?

In these positions the object's identity never escapes, so a reference that is always truthy can be replaced by `True`

. `and`

/`or`

are excluded: they yield an operand, so the module could escape (`x and self.<name>`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_inplace_target(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._inplace_target)

Base name `node`

mutates in place, if any.

A write through the name (`x[i] = ...`

, `x.attr = ...`

) or an in-place method call (`x.mul_(...)`

) leaves the base name in a `Load`

context, so it is not a plain `Name`

store (see `_rebound_names`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_leaf_attention_interfaces()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._leaf_attention_interfaces)

Patch `AttentionInterface.get_interface`

so traced forwards see a leaf node.

`vllm_attention_function`

needs runtime context so it is untraceable. Every interface returns `(attn_output, attn_weights)`

.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_mutated_names(region)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._mutated_names)

Names mutated in place within `region`

(see `_inplace_target`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_rebound_names(region)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._rebound_names)

Names rebound outright within `region`

(`x = ...`

, `del x`

).

These are `Name`

nodes in a `Store`

/`Del`

context.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_reference_weight(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._reference_weight)

A weight whose trailing dim is the module's hidden size.

Linears and 2-D gate weights are `[out, hidden]`

; norm weights are `[hidden]`

. Used to fabricate a placeholder input of matching size/dtype.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_returns_fresh(node, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._returns_fresh)

Does evaluating `node`

allocate, rather than return a view of its input?

A `nn.Linear`

writes its output into new storage, so its result aliases nothing that went in, and a chain of view ops on top of it aliases only that fresh tensor. Walking the receiver chain down to a `self.<linear>(...)`

call therefore proves the value cannot alias the projection input. A literal aliases nothing either, and a branch or sequence is fresh when every part is -- which is how a guarded projection (`p(x) if p is not None else None`

) stays untracked. A call on an attribute that is missing or `None`

cannot run at all, so a branch selecting a different configuration is fresh too.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`_writes_through_args(call)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils._writes_through_args)

Does `call`

write through an argument rather than return a new value?

Torch spells this three ways: an `out=`

destination, `inplace=True`

, and the trailing-underscore convention (`torch.relu_(x)`

). The underscore is checked on the function's own name, so it catches the free-function form that `_inplace_target`

cannot (there the base name is the module, `torch`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`aliasing_names(funcdef, seed, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.aliasing_names)

`seed`

plus every name that may alias one of them.

A view shares storage with its base (`h = x.view(-1)`

), so mutating `h`

mutates `x`

; tracking only `seed`

would miss that. Any assignment reading a tracked name therefore taints its targets, transitively, unless its value is freshly allocated (`_returns_fresh`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`block_chain(block, node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.block_chain)

Path of (statement list, index) pairs from `block`

down to `node`

.

Each pair names a nested block and the index in it of the statement containing `node`

; the last pair is `node`

's innermost block. Empty if `node`

is not in `block`

. The longest common prefix of several nodes' chains is the innermost block that dominates them all.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`bypass_existence_guard(funcdef, ref, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.bypass_existence_guard)

Fold a guard on `self.<name>`

's existence to its constant value.

The fuser deletes `self.<name>`

and binds only instances where it exists as a truthy `nn.Linear`

(guaranteed by the match, the cache key, and `validate`

), so a guard testing its presence is a fusion invariant. Two forms are folded:

- an identity
`None`

check`self.<name> is None`

->`False`

,`self.<name> is not None`

->`True`

(either operand order).`==`

/`!=`

are*not*folded:`is_linear`

accepts`nn.Linear`

subclasses, which may override`__eq__`

/`__ne__`

, so equality is not guaranteed to track identity. - a bare truthiness test (
`if self.<name>:`

,`... if self.<name> else ...`

,`not self.<name>`

): the reference itself to`True`

.

Any other surviving reference escapes the projection's value, which no longer exists after fusion, so refuse rather than change semantics.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`compile_forward(funcdef, fn)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.compile_forward)

Compile `funcdef`

in `fn`

's module so tracebacks point at the source.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`downstream_linear(node, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.downstream_linear)

Nearest linear consuming `node`

's output, walking through casts/scalings.

Never walks through a leaf call (e.g. an attention interface): what crosses it is consumed by the attention computation, not projected.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`find_node(graph, predicate)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.find_node)

The first node in `graph`

matching `predicate`

, or `None`

.

##

`forward_input_count(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.forward_input_count)

The number of tensor inputs `cls.forward`

declares, excluding `self`

and any `*args`

/`**kwargs`

. Read from the signature, so it is independent of whether the trace completes (unlike counting placeholders).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`forward_parameters(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.forward_parameters)

`cls.forward`

's signature parameters, or empty if uninspectable.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`is_fn(node, target)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_fn)

##

`is_leaf_call(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_leaf_call)

Is node a call recorded by `_as_leaf_call`

(e.g. an attention interface).

##

`is_linear(node, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_linear)

Is node `nn.Linear.__call__()`

.

##

`is_method(node, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_method)

##

`is_op(node, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.is_op)

Is node `<mod>.<name>()`

for torch, F, operator, or Tensor.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`output_value(graph)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.output_value)

The value the graph's `output`

node returns, if the trace reached one.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`peel(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.peel)

Strip dtype-cast wrappers (`.to(...)`

, `.float()`

, `.type_as(...)`

).

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`recover_forward(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.recover_forward)

Parse the source of `cls.forward`

, ready for rewriting.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`replace_expr(module, old, new)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.replace_expr)

Replace the expression `old`

(by identity) with `new`

within `module`

.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`returned_linear(graph, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.returned_linear)

Name of the Linear producing the graph's (first) output value.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`self_call_and_refs(funcdef, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.self_call_and_refs)

The unique `self.<name>(arg)`

call, plus every other `self.<name>`

reference.

Raises unless exactly one single-argument `self.<name>(arg)`

call exists, so one fx `call_module`

node maps to one syntactic call site. The remaining references (e.g. `is not None`

guards) are returned for the caller to resolve.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`single_self_call(funcdef, name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.single_self_call)

The unique `self.<name>(arg)`

call in `funcdef`

.

Raises unless `name`

appears exactly once, as such a call, so the source rewrite agrees with the fx match.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`trace(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.trace)

Trace `module.forward`

, returning the partial graph on failure.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`upstream_linear(node, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.upstream_linear)

Nearest linear producing `node`

, walking back through splits/reshapes.

Non-linear submodules are transparent too (e.g. the dropout GPT-style attentions apply after their output projection). Never walks through a leaf call (e.g. an attention interface): its inputs are what attention consumes, not what produced the value.

## Source code in `vllm/model_executor/models/transformers/fx_utils.py`


##

`written_names(region)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fx_utils.written_names)

Names `region`

may rebind or write through.

Beyond plain rebinding and writes through the name itself (`_rebound_names`

, `_mutated_names`

), a call can write through an argument without naming it as a target: `F.relu(x, inplace=True)`

, `torch.add(x, y, out=x)`

, `torch.relu_(x)`

. A statement-level call whose result is discarded is treated the same way, since it can only be there for a side effect.