source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/vllm_inductor_pass/
lastmod: 2026-09-23

#

`vllm.compilation.passes.vllm_inductor_pass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass)

Classes:

-
–[VllmFusionPatternMatcherPass](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)A VllmPatternMatcherPass for passes that use VllmPatternReplacement objects.

-
–[VllmInductorPass](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)An inductor pass with access to vLLM PassConfig.

-
–[VllmPatternMatcherPass](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)A VllmInductorPass that uses the Inductor pattern matcher.

-
–[VllmPatternReplacement](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)A pattern/replacement pair for FX graph fusion.


Functions:

-
–[fold_consecutive_reshapes](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.fold_consecutive_reshapes)Fold consecutive reshape ops into a single reshape.

-
–[get_match_table](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.get_match_table)Return a snapshot of the match table.

-
–[remove_noop_reshapes](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.remove_noop_reshapes)Drop reshape ops whose output shape equals their input shape.


##

`VllmFusionPatternMatcherPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

Bases: [VllmPatternMatcherPass](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)

A VllmPatternMatcherPass for passes that use VllmPatternReplacement objects. Subclasses register patterns via self.register() in their own **init**.

## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


##

`VllmInductorPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)

Bases: [InductorPass](https://docs.vllm.ai/inductor_pass/#vllm.compilation.passes.inductor_pass.InductorPass)

An inductor pass with access to vLLM PassConfig. It provides timing, logging, and dumping utilities.

Attributes:

-
([dump_prefix](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass.dump_prefix)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneKeep track of pass index for debug dump ordering.


## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


###

`dump_prefix = None`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass.dump_prefix)

Keep track of pass index for debug dump ordering.

##

`VllmPatternMatcherPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)

Bases: [VllmInductorPass](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)

A VllmInductorPass that uses the Inductor pattern matcher. Provides pattern registration with match counting, debug dumping, and logging.

Methods:

-
–[dump_patterns](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.dump_patterns)If debug dumping is enabled, dump the Inductor pattern-matcher patterns


Attributes:

-
([match_table](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.match_table)

) –[defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int)]Global table mapping pass name to its total match count.

-
([matched_count](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.matched_count)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of matched patterns in the pass.


## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


|
|

###

`match_table = defaultdict(int)`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.match_table)

Global table mapping pass name to its total match count.

###

`matched_count = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.matched_count)

The number of matched patterns in the pass.

###

`_replace_op_overloads(string)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass._replace_op_overloads)

Replace

## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


###

`dump_patterns(config, pm_pass)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass.dump_patterns)

If debug dumping is enabled, dump the Inductor pattern-matcher patterns into the debug_dump_path folder next to the dumped fx graphs.

This method does its best to print something that looks like Python code for easier debugging and potentially navigation. If any errors appear in the output, please add to this method.

TODO(luka): use pattern object to manually produce pattern graph

## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


##

`VllmPatternReplacement`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

A pattern/replacement pair for FX graph fusion.

Implement the three abstract members below, then pass instances to VllmFusionPatternMatcherPass.register(). The pass will find every occurrence of `pattern`

in the graph and substitute it with `replacement`

.

Methods:

-
–[get_inputs](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement.get_inputs)Example tensors used to trace pattern and replacement.


Attributes:

-
([pattern](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement.pattern)

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[P, R]Returns a closure defining the FX subgraph to search for.

-
([replacement](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement.replacement)

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[P, R]Returns a closure defining the FX subgraph to


## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


##

`fold_consecutive_reshapes(gm)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.fold_consecutive_reshapes)

Fold consecutive reshape ops into a single reshape.

`make_fx`

faithfully records every view/reshape the Python code performs, so patterns like `x.reshape(a, b).reshape(c, d)`

produce two reshape nodes. Inductor's own optimisation would fold these, but `pm.register_replacement`

's `trace_fn`

runs before Inductor, so we must fold them ourselves for the pattern to match the compiled graph.

When reshape(A, shape1) feeds only into reshape(result, shape2), the first reshape is redundant -- replace with reshape(A, shape2).

## Source code in `vllm/compilation/passes/vllm_inductor_pass.py`


##

`get_match_table()`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.get_match_table)

##

`remove_noop_reshapes(gm)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.vllm_inductor_pass.remove_noop_reshapes)

Drop reshape ops whose output shape equals their input shape.

Companion to :func:`fold_consecutive_reshapes`

. `make_fx`

records a reshape to the shape the input already has; the compiled graph has already dropped it, so the pattern only matches once we drop it too.