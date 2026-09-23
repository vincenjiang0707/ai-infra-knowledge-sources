source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/jit_warmup_cutedsl_helper/
lastmod: 2026-09-23

Bases: [VllmJitKernel](../jit_warmup/#vllm.model_executor.warmup.jit_warmup.VllmJitKernel)[CompileKeyT]

, [Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[CompileKeyT]


CuTeDSL owner whose compiled executor is shared by warmup and runtime.

Methods:

-
[warmup_inputs](#vllm.model_executor.warmup.jit_warmup_cutedsl_helper.VllmCuTeDSLJitKernel.warmup_inputs)

– Return fake arguments that compile one executor specialization.


## Source code in `vllm/model_executor/warmup/jit_warmup_cutedsl_helper.py`


| class VllmCuTeDSLJitKernel(VllmJitKernel[CompileKeyT], Generic[CompileKeyT]):
"""CuTeDSL owner whose compiled executor is shared by warmup and runtime."""
kernel: ClassVar[Any]
bind_launch_inputs = False
@abstractmethod
def warmup_inputs(self, compile_key: CompileKeyT) -> tuple[Any, ...]:
"""Return fake arguments that compile one executor specialization."""
raise NotImplementedError
def compile(self, compile_key: CompileKeyT) -> None:
if compile_key in self._compiled_cache:
return
self._compiled_cache[compile_key] = compile_cutedsl(
self.kernel(compile_key),
*self.warmup_inputs(compile_key),
)
def launch(
self,
launch_spec: CuTeDSLLaunchSpec[CompileKeyT],
_inputs: Mapping[str, Any],
) -> Any:
# (compile_key, args), optionally followed by output and epilogue.
compile_key, launch_args = launch_spec[:2]
executor = self._get_or_compile(compile_key)
result = executor(*launch_args)
if len(launch_spec) == 4:
return launch_spec[3]()
return launch_spec[2] if len(launch_spec) == 3 else result
|

Return fake arguments that compile one executor specialization.

## Source code in `vllm/model_executor/warmup/jit_warmup_cutedsl_helper.py`


| @abstractmethod
def warmup_inputs(self, compile_key: CompileKeyT) -> tuple[Any, ...]:
"""Return fake arguments that compile one executor specialization."""
raise NotImplementedError
|