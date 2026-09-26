# [Issue #169] Property rate consult

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/169
state: open | updated: 2026-01-30T20:17:09Z
labels: 

## 正文

Hello, may you public your solution generated rate && proper kernel rate? I trailed in 3080ti and deepseek-v3.2, finding the rate so low--40% solution generated, that I suspected my recurrence is right or not.

## 评论 (5)

### OwenVigil · 2026-01-26

```bash
--------------------------------------------------
BuildError: Destination-passing style callable has incorrect number of parameters: 2 != 3

Traceback:
Traceback (most recent call last):
  File "/workspace/OpenEvolve/flashinfer-bench/flashinfer_bench/bench/runner/persistent_runner.py", line 705, in _persistent_worker_main
    runnable_sol = registry.build(definition, solution)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/OpenEvolve/flashinfer-bench/flashinfer_bench/compile/registry.py", line 115, in build
    runnable = builder.build(definition, solution)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/OpenEvolve/flashinfer-bench/flashinfer_bench/compile/builders/triton_builder.py", line 80, in build
    result = super().build(definition, solution)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspace/OpenEvolve/flashinfer-bench/flashinfer_bench/compile/builders/python_builder.py", line 150, in build
    self._try_validate_signature(fn, definition, solution)
  File "/workspace/OpenEvolve/flashinfer-bench/flashinfer_bench/compile/builder.py", line 158, in _try_validate_signature
    raise BuildError(
flashinfer_bench.compile.builder.BuildError: Destination-passing style callable has incorrect number of parameters: 2 != 3
--------------------------------------------------
```
Target backend is triton, errors mostly occurred likes above. I think that's why the code appends error and the low generated rate.  Does this need a commit? I would track the problem.

### xslingcn · 2026-01-27

The default way that solutions pass arguments has changed to destination-passing style (i.e. we pre-allocate the tensor where the kernel writes back the results and provide the empty tensor along with other inputs, this way we save the time of allocating memory in the kernel). This might be a bit implicit to the agents and we can update our example prompts & docs to include this. cc @zanderjiang 
ref:
https://github.com/flashinfer-ai/flashinfer-bench/pull/125
https://github.com/flashinfer-ai/flashinfer-bench/blob/main/flashinfer_bench/data/solution.py#L82

### zanderjiang · 2026-01-27

> The default way that solutions pass arguments has changed to destination-passing style (i.e. we pre-allocate the tensor where the kernel writes back the results and provide the empty tensor along with other inputs, this way we save the time of allocating memory in the kernel). This might be a bit implicit to the agents and we can update our example prompts & docs to include this. cc [@zanderjiang](https://github.com/zanderjiang) ref: [#125](https://github.com/flashinfer-ai/flashinfer-bench/pull/125) https://github.com/flashinfer-ai/flashinfer-bench/blob/main/flashinfer_bench/data/solution.py#L82

The destination passing style requires fixed inputs (no keyword arguments), when we compile a kernel, we check that the number of arguments match the number of inputs + number of outputs in the definition, this is likely the reason why your kernel success rate is low. Without specifying, agents might not write the correct convention, for our supported kernel generator, we've adjusted the prompts in this PR: https://github.com/flashinfer-ai/flashinfer-bench/pull/168

We're also going to publish an agent guideline that should help you develop/debug your agent recurrences. 

For now, updating your prompt to 
1. avoid keyword arguments, 
2. follow destination passing style (write to the output buffer parameter) 

This should improve the success rate.

### OwenVigil · 2026-01-29

> The default way that solutions pass arguments has changed to destination-passing style (i.e. we pre-allocate the tensor where the kernel writes back the results and provide the empty tensor along with other inputs, this way we save the time of allocating memory in the kernel). This might be a bit implicit to the agents and we can update our example prompts & docs to include this. cc [@zanderjiang](https://github.com/zanderjiang) ref: [#125](https://github.com/flashinfer-ai/flashinfer-bench/pull/125) https://github.com/flashinfer-ai/flashinfer-bench/blob/main/flashinfer_bench/data/solution.py#L82

Really thanks for your effort, now the solution passing rate is 100%! But the proper rate, I roughly count it no more than 30%,  which is still very low though we tried a lot ways to recurrence by deepseekv3.2. I sincerely care about if you can give some property rate baseline or matrixes? Really really congratulate to your hard work.


### Ubospica · 2026-01-30

> > The default way that solutions pass arguments has changed to destination-passing style (i.e. we pre-allocate the tensor where the kernel writes back the results and provide the empty tensor along with other inputs, this way we save the time of allocating memory in the kernel). This might be a bit implicit to the agents and we can update our example prompts & docs to include this. cc [@zanderjiang](https://github.com/zanderjiang) ref: [#125](https://github.com/flashinfer-ai/flashinfer-bench/pull/125) https://github.com/flashinfer-ai/flashinfer-bench/blob/main/flashinfer_bench/data/solution.py#L82
> 
> Really thanks for your effort, now the solution passing rate is 100%! But the proper rate, I roughly count it no more than 30%, which is still very low though we tried a lot ways to recurrence by deepseekv3.2. I sincerely care about if you can give some property rate baseline or matrixes? Really really congratulate to your hard work.

Thanks for the followup. The correctness rate highly depends on the model, agent design, and the difficulty of the kernel. In our experiments, we also measured a correctness rate of around 30% for some difficult kernels, even for sota models. Enhancing agents could be helpful to further increase the rate.
