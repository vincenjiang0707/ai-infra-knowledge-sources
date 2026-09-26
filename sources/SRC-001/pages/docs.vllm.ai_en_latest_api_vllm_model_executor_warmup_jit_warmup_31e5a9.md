source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/jit_warmup/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup.jit_warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup)

Shared interfaces and tracing helpers for explicit JIT warmup keys.

Classes:

-
–[JitWarmupRegistry](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry)Collect and compile JIT kernels selected during runner setup.

-
–[VllmJitKernel](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel)Kernel wrapper that owns dispatch, warmup keys, and compilation.

-
–[WarmupChoices](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.WarmupChoices)Expand an explicit finite set of values in a traced warmup method.

-
–[WarmupIntRange](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.WarmupIntRange)Expand integers with range semantics or a custom monotonic progression.


Functions:

-
–[kernel_launcher](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.kernel_launcher)Delegate a declarative launch specification to its backend owner.

-
–[zip_inputs](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.zip_inputs)Group row-wise dispatch inputs that should be expanded in lockstep.


##

`JitWarmupRegistry`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry)

Collect and compile JIT kernels selected during runner setup.

Methods:

-
–[activate](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.activate)Collect registrations made in this context.

-
–[capture](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.capture)Collect warmup registrations made while the decorated callable runs.

-
–[register](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.register)Register a kernel with the active registry, if one exists.

-
–[warmup](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.warmup)Expand registrations and compile each wrapper/key pair once.


## Source code in `vllm/model_executor/warmup/jit_warmup.py`


|
|

###

`activate()`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.activate)

Collect registrations made in this context.

###

`capture(init_fn)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.capture)

Collect warmup registrations made while the decorated callable runs.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


###

`register(kernel, *args, **kwargs)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.register)

Register a kernel with the active registry, if one exists.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


###

`warmup()`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.JitWarmupRegistry.warmup)

Expand registrations and compile each wrapper/key pair once.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`VllmJitKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel)

Bases:

, [Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[CompileKeyT][ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Kernel wrapper that owns dispatch, warmup keys, and compilation.

Methods:

-
–[compile](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.compile)Compile one warmup key.

-
–[compile_many](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.compile_many)Compile a batch of warmup keys, allowing backend-specific scheduling.

-
–[dispatch](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.dispatch)Build one compile key from one concrete dispatch point.

-
–[get_warmup_keys](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.get_warmup_keys)Return compile keys that should be warmed for this kernel.

-
–[register_warmup](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.register_warmup)Register this kernel with the active runner's warmup registry.

-
–[warmup](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.warmup)Compile this kernel's warmup keys.


## Source code in `vllm/model_executor/warmup/jit_warmup.py`


|
|

###

`_expand_warmup_cases(cases_fn, *args, _value_expander=_expand_warmup_values, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel._expand_warmup_cases)

Expand symbolic domains declared inside a warmup-cases method.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


|
|

###

`_get_or_compile(compile_key, *, runtime_context=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel._get_or_compile)

Return a cached executor, compiling it on a monitored cache miss.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


###

`compile(compile_key)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.compile)

###

`compile_many(compile_keys)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.compile_many)

Compile a batch of warmup keys, allowing backend-specific scheduling.

###

`dispatch(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.dispatch)

###

`get_warmup_keys(*args, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.get_warmup_keys)

Return compile keys that should be warmed for this kernel.

###

`register_warmup(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.VllmJitKernel.register_warmup)

Register this kernel with the active runner's warmup registry.

##

`WarmupChoices`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.WarmupChoices)

Expand an explicit finite set of values in a traced warmup method.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`WarmupIntRange`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.WarmupIntRange)

Expand integers with range semantics or a custom monotonic progression.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`_WarmupInputRows`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup._WarmupInputRows)

##

`_same_registration(left, right)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup._same_registration)

True if two `(args, kwargs)`

registrations are equivalent.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`_same_value(left, right)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup._same_value)

True if two registration values are the same object or compare equal.

Identity is checked first so shared singletons (e.g. `vllm_config`

, torch dtypes) short-circuit before any potentially deep or non-boolean `__eq__`

.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`_validate_dispatch_expr(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup._validate_dispatch_expr)

Enforce the dispatch AST subset before compiling traced code.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`_when(condition)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup._when)

Filter symbolic cases in an AST-traced warmup-cases method.

##

`kernel_launcher(call_fn)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.kernel_launcher)

Delegate a declarative launch specification to its backend owner.

## Source code in `vllm/model_executor/warmup/jit_warmup.py`


##

`zip_inputs(*rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup.zip_inputs)

Group row-wise dispatch inputs that should be expanded in lockstep.