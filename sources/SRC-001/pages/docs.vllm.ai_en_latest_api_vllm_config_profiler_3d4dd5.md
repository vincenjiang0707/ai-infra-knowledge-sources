source: https://docs.vllm.ai/en/latest/api/vllm/config/profiler/
lastmod: 2026-09-24

#

`vllm.config.profiler`

[¶](https://docs.vllm.ai#vllm.config.profiler)

Classes:

-
–[ProfilerConfig](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig)Dataclass which contains profiler config for the engine.


##

`ProfilerConfig`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig)

Dataclass which contains profiler config for the engine.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([active_iterations](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.active_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of active iterations for PyTorch profiler schedule.

-
([capture_torch_profiler](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.capture_torch_profiler)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables a torch profiler during CUDA graph capture on rank 0. -
([delay_iterations](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.delay_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of engine iterations to skip before starting profiling.

-
([detailed_trace_annotation](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.detailed_trace_annotation)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, uses detailed annotations with roofline metrics (sk, sqsq, -
([ignore_frontend](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.ignore_frontend)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, disables the front-end profiling of AsyncLLM when using the -
([max_iterations](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.max_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of engine iterations to profile after starting profiling.

-
([profiler](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.profiler)`ProfilerKind | None`

) –Which profiler to use. Defaults to None. Options are:

-
([proton_backend](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_backend)`ProtonBackend | None`

) –Proton GPU backend.

`None`

lets Proton select CUPTI automatically. -
([proton_context](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_context)`ProtonContext`

) –Proton context source.

`shadow`

records explicit scopes with low -
([proton_data](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_data)`ProtonData`

) –Proton output type.

`tree`

produces Hatchet data and`trace`

-
([proton_graph_attribution](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_graph_attribution)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Observe CUDA graph capture so replayed kernels can be attributed.

-
([proton_hook](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_hook)`ProtonHook | None`

) –Optional Proton hook. Use

`triton`

to add Triton launch metadata. -
([proton_mode](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_mode)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneOptional backend-specific Proton mode string, such as

`pcsampling`

. -
([proton_output_format](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_output_format)`ProtonOutputFormat | None`

) –Optional format passed to Proton when finalizing a profile.

`None`

-
([proton_profiler_dir](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_profiler_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Directory to save Triton Proton profiles. Each worker writes a

-
([torch_profiler_activities](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_activities)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[TorchProfilerActivity] | NoneActivities recorded by workers using the torch profiler. When unset,

-
([torch_profiler_dir](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Directory to save torch profiler traces. Both AsyncLLM's CPU traces and

-
([torch_profiler_dump_cuda_time_total](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_dump_cuda_time_total)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, dumps total CUDA time in torch profiler traces. Enabled by default. -
([torch_profiler_record_shapes](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_record_shapes)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, records tensor shapes in the torch profiler. Disabled by default. -
([torch_profiler_use_gzip](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_use_gzip)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, saves torch profiler traces in gzip format. Enabled by default -
([torch_profiler_with_flops](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_with_flops)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables FLOPS counting in the torch profiler. Disabled by default. -
([torch_profiler_with_memory](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_with_memory)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables memory profiling in the torch profiler. -
([torch_profiler_with_stack](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_with_stack)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables stack tracing in the torch profiler. Enabled by default -
([wait_iterations](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.wait_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of wait iterations for PyTorch profiler schedule.

-
([warmup_iterations](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.warmup_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of warmup iterations for PyTorch profiler schedule.


## Source code in `vllm/config/profiler.py`


|
|

###

`active_iterations = Field(default=5, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.active_iterations)

Number of active iterations for PyTorch profiler schedule. This is the number of iterations where profiling data is actually collected. Defaults to 5 active iterations.

###

`capture_torch_profiler = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.capture_torch_profiler)

If `True`

, enables a torch profiler during CUDA graph capture on rank 0. Traces are saved to a `capture_traces`

subdirectory under `torch_profiler_dir`

. Requires `profiler`

to be set to 'torch'.

###

`delay_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.delay_iterations)

Number of engine iterations to skip before starting profiling. Defaults to 0, meaning profiling starts immediately after receiving /start_profile.

###

`detailed_trace_annotation = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.detailed_trace_annotation)

If `True`

, uses detailed annotations with roofline metrics (sk, sqsq, sqsk) in profiler trace events. If `False`

, uses simple annotations with only context/generation request counts and token counts. Disabled by default.

###

`ignore_frontend = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.ignore_frontend)

If `True`

, disables the front-end profiling of AsyncLLM when using the 'torch' profiler. This is needed to reduce overhead when using delay/limit options, since the front-end profiling does not track iterations and will capture the entire range.

###

`max_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.max_iterations)

Maximum number of engine iterations to profile after starting profiling. Defaults to 0, meaning no limit.

###

`profiler = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.profiler)

Which profiler to use. Defaults to None. Options are:

- 'torch': Use PyTorch profiler.
- 'cuda': Use CUDA profiler.
- 'proton': Use Triton Proton profiler.

###

`proton_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_backend)

Proton GPU backend. `None`

lets Proton select CUPTI automatically.

###

`proton_context = 'shadow'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_context)

Proton context source. `shadow`

records explicit scopes with low overhead; `python`

records Python call stacks.

###

`proton_data = 'tree'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_data)

Proton output type. `tree`

produces Hatchet data and `trace`

produces a Chrome trace.

###

`proton_graph_attribution = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_graph_attribution)

Observe CUDA graph capture so replayed kernels can be attributed. Requires Triton >= 3.7 and `proton_data='tree'`

.

###

`proton_hook = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_hook)

Optional Proton hook. Use `triton`

to add Triton launch metadata.

###

`proton_mode = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_mode)

Optional backend-specific Proton mode string, such as `pcsampling`

.

###

`proton_output_format = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_output_format)

Optional format passed to Proton when finalizing a profile. `None`

uses the default format for `proton_data`

.

###

`proton_profiler_dir = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.proton_profiler_dir)

Directory to save Triton Proton profiles. Each worker writes a separate rank-qualified file.

###

`torch_profiler_activities = Field(default=None, min_length=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_activities)

Activities recorded by workers using the torch profiler. When unset, each worker uses its platform default: CPU; CPU and CUDA; or CPU and XPU.

###

`torch_profiler_dir = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_dir)

Directory to save torch profiler traces. Both AsyncLLM's CPU traces and worker's traces (CPU & GPU) will be saved under this directory. Note that it must be an absolute path.

###

`torch_profiler_dump_cuda_time_total = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_dump_cuda_time_total)

If `True`

, dumps total CUDA time in torch profiler traces. Enabled by default.

###

`torch_profiler_record_shapes = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_record_shapes)

If `True`

, records tensor shapes in the torch profiler. Disabled by default.

###

`torch_profiler_use_gzip = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_use_gzip)

If `True`

, saves torch profiler traces in gzip format. Enabled by default

###

`torch_profiler_with_flops = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_with_flops)

If `True`

, enables FLOPS counting in the torch profiler. Disabled by default.

###

`torch_profiler_with_memory = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_with_memory)

If `True`

, enables memory profiling in the torch profiler. Disabled by default.

###

`torch_profiler_with_stack = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.torch_profiler_with_stack)

If `True`

, enables stack tracing in the torch profiler. Enabled by default as it is useful for debugging. Can be disabled via --profiler-config.torch_profiler_with_stack=false CLI flag.

###

`wait_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.wait_iterations)

Number of wait iterations for PyTorch profiler schedule. During wait, the profiler is completely off with zero overhead. This allows skipping initial iterations before warmup begins. Defaults to 0 (no wait period).

###

`warmup_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.warmup_iterations)

Number of warmup iterations for PyTorch profiler schedule. During warmup, the profiler runs but data is discarded. This helps reduce noise from JIT compilation and other one-time costs in the profiled trace. Defaults to 0 (schedule-based profiling disabled, recording all iterations). Set to a positive value (e.g., 2) to enable schedule-based profiling.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.profiler.ProfilerConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/profiler.py`


##

`_is_uri_path(path)`

[¶](https://docs.vllm.ai#vllm.config.profiler._is_uri_path)

Check if path is a URI (scheme://...), excluding Windows drive letters.

Supports custom URI schemes like gs://, s3://, hdfs://, etc. These paths should not be converted to absolute paths.