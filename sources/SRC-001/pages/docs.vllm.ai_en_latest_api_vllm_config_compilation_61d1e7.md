source: https://docs.vllm.ai/en/latest/api/vllm/config/compilation/
lastmod: 2026-09-23

#

`vllm.config.compilation`

[¶](https://docs.vllm.ai#vllm.config.compilation)

Classes:

-
–[CUDAGraphMode](https://docs.vllm.ai#vllm.config.compilation.CUDAGraphMode)Constants for the cudagraph mode in CompilationConfig.

-
–[CompilationConfig](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig)Configuration for compilation.

-
–[CompilationMode](https://docs.vllm.ai#vllm.config.compilation.CompilationMode)The compilation approach used for torch.compile-based compilation of the

-
–[DynamicShapesConfig](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig)Configuration to control/debug torch compile dynamic shapes.

-
–[DynamicShapesType](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType)Types of dynamic shapes handling in torch.compile().

-
–[PassConfig](https://docs.vllm.ai#vllm.config.compilation.PassConfig)Configuration for custom Inductor passes.


##

`CUDAGraphMode`

[¶](https://docs.vllm.ai#vllm.config.compilation.CUDAGraphMode)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Constants for the cudagraph mode in CompilationConfig. Meanwhile, the subset enum `NONE`

, `PIECEWISE`

and `FULL`

are also treated as concrete runtime mode for cudagraph runtime dispatching.

## Source code in `vllm/config/compilation.py`


##

`CompilationConfig`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig)

Configuration for compilation.

You must pass CompilationConfig to VLLMConfig constructor. VLLMConfig's post_init does further initialization. If used outside of the VLLMConfig, some fields will be left in an improper state.

It contains PassConfig, which controls the custom fusion/transformation passes. The rest has three parts:

- Top-level Compilation control:
- CudaGraph capture:
- Inductor compilation:
`compile_sizes`

- [
`compile_ranges_endpoints`

] [vllm.config.CompilationConfig.compile_ranges_endpoints] `inductor_compile_config`

`inductor_passes`

- custom inductor passes


Why we have different sizes for cudagraph and inductor: - cudagraph: a cudagraph captured for a specific size can only be used for the same size. We need to capture all the sizes we want to use. - inductor: a graph compiled by inductor for a general shape can be used for different sizes. Inductor can also compile for specific sizes, where it can have more information to optimize the graph with fully static shapes. However, we find the general shape compilation is sufficient for most cases. It might be beneficial to compile for certain small batchsizes, where inductor is good at optimizing.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compute_hash)Provide a hash that uniquely identifies all the configs

-
–[custom_op_log_check](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.custom_op_log_check)This method logs the enabled/disabled custom ops and checks that the

-
–[get_compile_ranges](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.get_compile_ranges)Get the compile ranges for the compilation config.

-
–[init_backend](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.init_backend)Initialize the backend for the compilation config from a vllm config.

-
–[post_init_cudagraph_sizes](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.post_init_cudagraph_sizes)To complete the initialization after cudagraph related

-
–[validate_cudagraph_mode_before](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.validate_cudagraph_mode_before)Enable parsing of the

`cudagraph_mode`

enum type from string. -
–[validate_mode_before](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.validate_mode_before)Enable parsing the

`mode`

field from string mode names. -
–[validate_pass_config_before](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.validate_pass_config_before)Enable parsing of the

`pass_config`

field from a dictionary.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.backend)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The backend for compilation. It needs to be a string:

-
([cache_dir](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cache_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The directory to store the compiled graph, to accelerate Inductor

-
([compilation_time](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compilation_time)

) –[float](https://docs.python.org/3/builtins/functions.html#float)time taken for compilation

-
([compile_cache_save_format](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_cache_save_format)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['binary', 'unpacked']Format for saving torch compile cache:

-
([compile_mm_encoder](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_mm_encoder)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether or not to compile the multimodal encoder.

-
([compile_ranges_endpoints](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_ranges_endpoints)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneEndpoints for Inductor compile ranges.

-
([compile_sizes](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_sizes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneSizes to compile for inductor. In addition

-
([cudagraph_capture_sizes](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_capture_sizes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Sizes to capture cudagraph.

-
([cudagraph_copy_inputs](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_copy_inputs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to copy input tensors for

-
([cudagraph_mm_encoder](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_mm_encoder)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable CUDA graph capture for multimodal encoder (ViT).

-
([cudagraph_mode](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_mode)

) –[CUDAGraphMode](https://docs.vllm.ai#vllm.config.compilation.CUDAGraphMode)The mode of the cudagraph:

-
([cudagraph_num_of_warmups](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_num_of_warmups)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of warmup runs for cudagraph.

-
([cudagraph_specialize_lora](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_specialize_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to create separate cuda graphs for cases with and without active

-
([custom_ops](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.custom_ops)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Fine-grained control over which custom ops to enable/disable. Use 'all'

-
([debug_dump_path](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.debug_dump_path)

) –[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)| NoneThe path to dump the debug information.

-
([disabled_custom_ops](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.disabled_custom_ops)

) –[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]custom ops that are disabled

-
([dynamic_shapes_config](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.dynamic_shapes_config)

) –[DynamicShapesConfig](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig)Configuration for dynamic shapes options

-
([enabled_custom_ops](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.enabled_custom_ops)

) –[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]custom ops that are enabled

-
([encoder_compilation_time](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_compilation_time)

) –[float](https://docs.python.org/3/builtins/functions.html#float)time taken for multimodal encoder compilation

-
([encoder_cudagraph_max_frames_per_batch](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_cudagraph_max_frames_per_batch)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum total video frames per batch for encoder CUDA graph capture.

-
([encoder_cudagraph_max_vision_items_per_batch](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_cudagraph_max_vision_items_per_batch)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of images/videos per batch for encoder CUDA graph capture.

-
([encoder_cudagraph_token_budgets](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_cudagraph_token_budgets)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Token budget levels for encoder CUDA graph capture.

-
([fast_moe_cold_start](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.fast_moe_cold_start)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneOptimization for fast MOE cold start.

-
([inductor_compile_config](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.inductor_compile_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Additional configurations for inductor.

-
([inductor_passes](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.inductor_passes)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Additional passes for inductor. It is a dictionary

-
([ir_enable_torch_wrap](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.ir_enable_torch_wrap)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, enable vllm_ir torch custom op wrapping during the forward pass.

-
([local_cache_dir](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.local_cache_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)local cache dir for each rank

-
([max_cudagraph_capture_size](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.max_cudagraph_capture_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The maximum cudagraph capture size.

-
([mode](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.mode)

) –[CompilationMode](https://docs.vllm.ai#vllm.config.compilation.CompilationMode)The compilation approach used for torch.compile-based compilation of the

-
([pass_config](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.pass_config)

) –[PassConfig](https://docs.vllm.ai#vllm.config.compilation.PassConfig)Custom inductor passes, see PassConfig for more details

-
([splitting_ops](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.splitting_ops)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneA list of ops to exclude from cudagraphs, used in piecewise compilation.

-
([static_all_moe_layers](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.static_all_moe_layers)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The names of all the MOE layers in the model

-
([static_forward_context](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.static_forward_context)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]Per-model forward context

-
([traced_files](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.traced_files)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]files that are traced for compilation

-
([use_inductor_graph_partition](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.use_inductor_graph_partition)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use inductor graph partition to split the graph at cudagraph_unsafe ops.


## Source code in `vllm/config/compilation.py`


|
|

###

`backend = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.backend)

The backend for compilation. It needs to be a string:

- "" (empty string): use the default backend ("inductor" on CUDA-alike platforms).
- "eager"/"openxla"/...: use the specified backend registered in PyTorch.
- "full.module.name": a qualified name which can be used to import the

backend function. We use string to avoid serialization issues when using compilation in a distributed setting. When the compilation mode is 1 or 2, the backend is used for the compilation directly (it sees the whole graph). When the compilation mode is 3, the backend supports both whole graph and piecewise compilation, available backends include eager, inductor, and custom backends, the latter of which can be defined via `get_compile_backend`

. Furthermore, compilation is only piecewise if splitting ops is set accordingly and use_inductor_graph_partition is off. Note that the default options for splitting ops are sufficient for piecewise compilation.

###

`cache_dir = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cache_dir)

The directory to store the compiled graph, to accelerate Inductor compilation. By default, it will use model-related information to generate a cache directory.

###

`compilation_time = field(default=0.0, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compilation_time)

time taken for compilation

###

`compile_cache_save_format = field(default_factory=(lambda: envs.VLLM_COMPILE_CACHE_SAVE_FORMAT))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_cache_save_format)

Format for saving torch compile cache:

-
"binary": saves as binary file (multiprocess safe)

-
"unpacked": saves as directory structure for inspection/debugging (NOT multiprocess safe)


Defaults to `VLLM_COMPILE_CACHE_SAVE_FORMAT`

if not specified.

###

`compile_mm_encoder = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_mm_encoder)

Whether or not to compile the multimodal encoder. Currently, this only works for `Qwen2_5_vl`

and `mLLaMa4`

models on selected platforms. It may also work for models loaded with the Transformers modeling backend if the encoder is compilable. Disabled by default until more models are supported/tested to work.

###

`compile_ranges_endpoints = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_ranges_endpoints)

Endpoints for Inductor compile ranges. The compile ranges are [1, endpoints[0]], [endpoints[0] + 1, endpoints[1]], ..., [endpoints[-1] + 1, max_num_batched_tokens]. Compile sizes are also used single element ranges, the range is represented as [compile_sizes[i], compile_sizes[i]].

If a range overlaps with the compile size, graph for compile size will be prioritized, i.e. if we have a range [1, 8] and a compile size 4, graph for compile size 4 will be compiled and used instead of the graph for range [1, 8].

###

`compile_sizes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compile_sizes)

Sizes to compile for inductor. In addition to integers, it also supports "cudagraph_capture_sizes" to specify the sizes for cudagraph capture.

###

`cudagraph_capture_sizes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_capture_sizes)

Sizes to capture cudagraph. - None (default): capture sizes are inferred from vllm config. - list[int]: capture sizes are specified as given.

###

`cudagraph_copy_inputs = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_copy_inputs)

Whether to copy input tensors for cudagraph. If the caller can guarantee that the same input buffers are always used, it can set this to False. Otherwise, it should set this to True, and the compiler will copy the input to an internally managed buffer. Default is False. Note that this flag is only effective when cudagraph_mode is PIECEWISE.

###

`cudagraph_mm_encoder = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_mm_encoder)

Enable CUDA graph capture for multimodal encoder (ViT). When enabled, captures full encoder forward as CUDA graph for each token budget level.

###

`cudagraph_mode = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_mode)

The mode of the cudagraph:

- NONE, no cudagraph capture.
- PIECEWISE.
- FULL.
- FULL_DECODE_ONLY.
- FULL_AND_PIECEWISE. (v1 default)

PIECEWISE mode build piecewise cudagraph only, keeping the cudagraph incompatible ops (i.e. some attention ops) outside the cudagraph for general flexibility.

FULL mode: Capture full cudagraph for all batches. Can be good for small models or workloads with small prompts; not supported by many backends. Generally for performance FULL_AND_PIECEWISE is better.

FULL_DECODE_ONLY mode: Capture full cudagraph for decode batches only. Mixed prefill-decode batches are run without cudagraphs. Can be good for decode instances in a P/D setup where prefill is not as important so we can save some memory.

FULL_AND_PIECEWISE mode: Capture full cudagraph for decode batches and piecewise cudagraph for prefill and mixed prefill-decode batches. This is the most performant mode for most models and is the default.

Currently, the cudagraph mode is only used for the v1 engine. Note that the cudagraph logic is generally orthogonal to the compilation logic. While piecewise cudagraphs require piecewise compilation (mode=VLLM_COMPILE and non-empty splitting_ops), full cudagraphs are supported with and without compilation.

Warning: This flag is new and subject to change in addition more modes may be added.

###

`cudagraph_num_of_warmups = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_num_of_warmups)

Number of warmup runs for cudagraph. It means the first several runs will be treated as warmup runs. Only after that, the execution will be recorded, and the recorded cudagraph will be used for subsequent runs.

###

`cudagraph_specialize_lora = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.cudagraph_specialize_lora)

Whether to create separate cuda graphs for cases with and without active LoRA adapters. When set to False, the LoRA-enabled cuda graph will be used for all cases, incurring the overhead of running LoRA ops even when no adapters are active. Setting this to True will remove this overhead at the cost of increased startup time and slightly higher memory usage. When `enable_lora`

is False, this option has no effect.

###

`custom_ops = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.custom_ops)

Fine-grained control over which custom ops to enable/disable. Use 'all' to enable all, 'none' to disable all. Also specify a list of custom op names to enable (prefixed with a '+'), or disable (prefixed with a '-'). Examples:

- 'all,-op1' to enable all except op1
- 'none,+op1,+op2' to enable only op1 and op2

By default, all custom ops are enabled when running without Inductor and disabled when running with Inductor: mode>CompilationMode.NONE and backend="inductor". Inductor generates (fused) Triton kernels for disabled custom ops.

###

`debug_dump_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.debug_dump_path)

The path to dump the debug information.

###

`disabled_custom_ops = field(default_factory=Counter, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.disabled_custom_ops)

custom ops that are disabled

###

`dynamic_shapes_config = field(default_factory=DynamicShapesConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.dynamic_shapes_config)

Configuration for dynamic shapes options

###

`enabled_custom_ops = field(default_factory=Counter, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.enabled_custom_ops)

custom ops that are enabled

###

`encoder_compilation_time = field(default=0.0, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_compilation_time)

time taken for multimodal encoder compilation

###

`encoder_cudagraph_max_frames_per_batch = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_cudagraph_max_frames_per_batch)

Maximum total video frames per batch for encoder CUDA graph capture. Controls the cu_seqlens buffer size (one entry per attention sequence, i.e. one per video frame). If None (default), auto-inferred as encoder_cudagraph_max_vision_items_per_batch * max_frames_per_video (model-specific value according to processing_info). Positive value overrides auto-inference and applies to all budget levels. If we limit the video count per prompt to `0`

, it will also be set to `0`

(i.e., fall back to image-only mode).

###

`encoder_cudagraph_max_vision_items_per_batch = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_cudagraph_max_vision_items_per_batch)

Maximum number of images/videos per batch for encoder CUDA graph capture. Determines the fixed batch size used during graph capture. If 0 (default), auto-inferred as max_budget // min_budget from the model's budget range. User-provided positive value overrides auto-inference.

###

`encoder_cudagraph_token_budgets = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.encoder_cudagraph_token_budgets)

Token budget levels for encoder CUDA graph capture. Each budget defines a fixed token capacity. At runtime, images are greedy-packed into the smallest fitting budget and the corresponding CUDA graph is replayed. If empty (default), auto-inferred from model architecture as power-of-2 levels from the model's estimated min budget to max budget. User-provided values override auto-inference. Example: [2048, 4096, 8192, 13824]

###

`fast_moe_cold_start = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.fast_moe_cold_start)

Optimization for fast MOE cold start.

This is a bit of a hack that assumes that: 1. the only decoder forward pass being run is the current model 2. the decoder forward pass runs all of the MOEs in the order in which they are initialized

When the above two conditions hold, this option greatly decreases cold start time for MOE models.

The options are: - True: optimization is always on - False: optimization is always off - None: optimization is on usually but off for speculative decoding

If conditions 1&2 don't hold then this option will lead to silent incorrectness. The only condition in which this doesn't hold is speculative decoding, where there is a draft model that may have MOEs in them.

NB: We're working on a longer-term solution that doesn't need these assumptions.

###

`inductor_compile_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.inductor_compile_config)

Additional configurations for inductor. - None: use default configurations.

###

`inductor_passes = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.inductor_passes)

Additional passes for inductor. It is a dictionary from pass name to pass function qualified name. We use function name because the config uses JSON format. If we pass the config from Python, functions can also be passed directly via Python object constructor, e.g. `CompilationConfig(inductor_passes={"a": func})`

.

###

`ir_enable_torch_wrap = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.ir_enable_torch_wrap)

If True, enable vllm_ir torch custom op wrapping during the forward pass. When False, torch custom op wrapping is disabled, allowing Dynamo to trace the selected implementation directly or avoiding torch custom op overhead in eager mode. Defaults to True when using Inductor with vllm-compile (backend=="inductor" and mode == VLLM_COMPILE), False otherwise.

###

`local_cache_dir = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.local_cache_dir)

local cache dir for each rank

###

`max_cudagraph_capture_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.max_cudagraph_capture_size)

The maximum cudagraph capture size.

If cudagraph_capture_sizes is specified, this will be set to the largest size in that list (or checked for consistency if specified). If cudagraph_capture_sizes is not specified, the list of sizes is generated automatically following the pattern:

```
[1, 2, 4] + list(range(8, 256, 8)) + list(
range(256, max_cudagraph_capture_size + 1, 16))
```


If not specified, max_cudagraph_capture_size is capped at 512 by default, or 1024 on data center Blackwell GPUs. This avoids OOM in tight memory scenarios with small max_num_seqs, and limits capture of large graphs that increase startup time and memory usage. Uniform decode sizes are appended only within this default ceiling.

###

`mode = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.mode)

The compilation approach used for torch.compile-based compilation of the model.

- None: If None, we will select the default compilation mode. For V1 engine this is 3.
- 0: NONE: No torch.compile compilation is applied, model runs in fully eager pytorch mode. The model runs as-is.
- 1: STOCK_TORCH_COMPILE: The standard
`torch.compile`

compilation pipeline. - 2: DYNAMO_TRACE_ONCE: Single Dynamo trace through the model, avoiding recompilation by removing guards. Requires no dynamic-shape-dependent control-flow.
- 3: VLLM_COMPILE: Custom vLLM Inductor-based backend with caching, piecewise compilation, shape specialization, and custom passes.

###

`pass_config = field(default_factory=PassConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.pass_config)

Custom inductor passes, see PassConfig for more details

###

`splitting_ops = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.splitting_ops)

A list of ops to exclude from cudagraphs, used in piecewise compilation.

The behavior depends on use_inductor_graph_partition:

-
When use_inductor_graph_partition=False (default): These ops are used for Dynamo FX-level graph splitting. The graph is split at these ops before Inductor compilation, creating separate subgraphs for cudagraph capture.

-
When use_inductor_graph_partition=True: These ops are used to register Inductor partition rules. The graph partitioning happens at Inductor codegen time after all passes and fusions are finished, allowing compilation and custom passes to operate on the full graph while still excluding these ops from cudagraphs.


If None, defaults to attention ops for piecewise cudagraphs. If empty list [], no ops are excluded (suitable for full cudagraphs).

###

`static_all_moe_layers = field(default_factory=list, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.static_all_moe_layers)

The names of all the MOE layers in the model

###

`static_forward_context = field(default_factory=dict, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.static_forward_context)

Per-model forward context Map from layer name to layer objects that need to be accessed outside model code, e.g., Attention, FusedMOE when dp_size>1.

###

`traced_files = field(default_factory=set, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.traced_files)

files that are traced for compilation

###

`use_inductor_graph_partition = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.use_inductor_graph_partition)

Use inductor graph partition to split the graph at cudagraph_unsafe ops. This partition happens at inductor codegen time after all passes and fusions are finished. It generates a single `call`

function which wraps cudagraph-safe ops into partition functions and leave cudagraph-unsafe ops outside the partition functions. For a graph with N cudagraph-unsafe ops (e.g., Attention), there would be N+1 partitions. To mark an op as cudagraph unsafe, we can add `tags=(torch._C.Tag.cudagraph_unsafe)`

when register the custom op.

This config supports both full cudagraph and piecewise cudagraph without compiling twice. For piecewise cudagraph, it applies vLLM CUDAGraph wrapper to each partition. For N+1 partitions, there would be N+1 CUDAGraph wrapper instances.

For full CUDAGraph, we always apply a single CUDAGraph wrapper outside the inductor `call`

function in the model runner. The top-level full cudagraph capture ignores all partitioning.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/compilation.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.compute_hash)

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/compilation.py`


###

`custom_op_log_check()`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.custom_op_log_check)

This method logs the enabled/disabled custom ops and checks that the passed custom_ops field only contains relevant ops. It is called at the end of set_current_vllm_config, after the custom ops have been instantiated.

## Source code in `vllm/config/compilation.py`


###

`get_compile_ranges()`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.get_compile_ranges)

Get the compile ranges for the compilation config.

## Source code in `vllm/config/compilation.py`


###

`init_backend(vllm_config, prefix='', is_encoder=False)`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.init_backend)

Initialize the backend for the compilation config from a vllm config.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.init_backend(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/#vllm.config.VllmConfig)The vllm config to initialize the backend from.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.init_backend(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Cache directory prefix for this compiled module.

-

(`is_encoder`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.init_backend(is_encoder))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether this module is used in an encoder (as opposed to a text backbone).


Returns:

## Source code in `vllm/config/compilation.py`


###

`post_init_cudagraph_sizes()`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.post_init_cudagraph_sizes)

To complete the initialization after cudagraph related configs are set. This includes: - initialize compile_sizes

## Source code in `vllm/config/compilation.py`


###

`validate_cudagraph_mode_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.validate_cudagraph_mode_before)

Enable parsing of the `cudagraph_mode`

enum type from string.

## Source code in `vllm/config/compilation.py`


###

`validate_mode_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.validate_mode_before)

Enable parsing the `mode`

field from string mode names. Accepts both integers (0-3) and string names, like NONE, STOCK_TORCH_COMPILE, DYNAMO_TRACE_ONCE, VLLM_COMPILE.

## Source code in `vllm/config/compilation.py`


###

`validate_pass_config_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationConfig.validate_pass_config_before)

Enable parsing of the `pass_config`

field from a dictionary.

## Source code in `vllm/config/compilation.py`


##

`CompilationMode`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationMode)

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

The compilation approach used for torch.compile-based compilation of the model.

Attributes:

-
–[DYNAMO_TRACE_ONCE](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.DYNAMO_TRACE_ONCE)Single Dynamo trace through the model, avoiding recompilation.

-
–[NONE](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.NONE)No torch.compile compilation is applied, model runs in fully eager pytorch mode.

-
–[STOCK_TORCH_COMPILE](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.STOCK_TORCH_COMPILE)The standard

`torch.compile`

compilation pipeline. -
–[VLLM_COMPILE](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.VLLM_COMPILE)Custom vLLM Inductor-based backend with caching, piecewise compilation,


## Source code in `vllm/config/compilation.py`


###

`DYNAMO_TRACE_ONCE = 2`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.DYNAMO_TRACE_ONCE)

Single Dynamo trace through the model, avoiding recompilation.

###

`NONE = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.NONE)

No torch.compile compilation is applied, model runs in fully eager pytorch mode. The model runs as-is.

###

`STOCK_TORCH_COMPILE = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.STOCK_TORCH_COMPILE)

The standard `torch.compile`

compilation pipeline.

###

`VLLM_COMPILE = 3`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.CompilationMode.VLLM_COMPILE)

Custom vLLM Inductor-based backend with caching, piecewise compilation, shape specialization, and custom passes.

##

`DynamicShapesConfig`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig)

Configuration to control/debug torch compile dynamic shapes.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.compute_hash)Provide a hash for DynamicShapesConfig.


Attributes:

-
([assume_32_bit_indexing](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.assume_32_bit_indexing)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)whether all tensor sizes can use 32 bit indexing.

-
([evaluate_guards](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.evaluate_guards)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A debug mode to detect and fail if Dynamo ever specializes a dynamic shape by

-
([type](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.type)

) –[DynamicShapesType](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType)Controls the type of dynamic shapes handling to use with torch.compile().


## Source code in `vllm/config/compilation.py`


###

`assume_32_bit_indexing = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.assume_32_bit_indexing)

whether all tensor sizes can use 32 bit indexing. `True`

requires PyTorch 2.10+

###

`evaluate_guards = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.evaluate_guards)

A debug mode to detect and fail if Dynamo ever specializes a dynamic shape by guarding on it. When True, dynamic shape guards are not dropped from dynamo. And a failure will be triggered if a recompilation ever happens due to that. This mode requires VLLM_USE_BYTECODE_HOOK to be 0. Enabling this allow observing the dynamic shapes guards in the tlparse artifacts also. When type is backed, aot_compile must be disabled for this mode to work. until this change picked up https://github.com/pytorch/pytorch/pull/169239.

###

`type = DynamicShapesType.BACKED`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.type)

Controls the type of dynamic shapes handling to use with torch.compile().

- BACKED: Default PyTorch behavior with potential guards ignored.
- UNBACKED: No guards guaranteed (most sound) but may throw data dependent errors.
- BACKED_SIZE_OBLIVIOUS: Experimental safer alternative to backed/unbacked.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesConfig.compute_hash)

Provide a hash for DynamicShapesConfig.

##

`DynamicShapesType`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType)

Types of dynamic shapes handling in torch.compile(). see Dynamic shapes and vllm guard dropping in torch_compile.md for more details.

Attributes:

-
–[BACKED](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType.BACKED)Use backed dynamic shapes. torch.compile() guards on backed dynamic

-
–[BACKED_SIZE_OBLIVIOUS](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType.BACKED_SIZE_OBLIVIOUS)Experimental flag that treats backed symbols as unbacked when explicit

-
–[UNBACKED](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType.UNBACKED)Use unbacked dynamic shapes. Guaranteed not to be guarded on and not


## Source code in `vllm/config/compilation.py`


###

`BACKED = 'backed'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType.BACKED)

Use backed dynamic shapes. torch.compile() guards on backed dynamic shapes and may add guards. Symbols are specialized to 0, 1, or >=2 even without encountering branching on those ranges.

###

`BACKED_SIZE_OBLIVIOUS = 'backed_size_oblivious'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType.BACKED_SIZE_OBLIVIOUS)

Experimental flag that treats backed symbols as unbacked when explicit unbacked handling is defined.

###

`UNBACKED = 'unbacked'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.DynamicShapesType.UNBACKED)

Use unbacked dynamic shapes. Guaranteed not to be guarded on and not 0/1 specialized, but may throw data dependent errors when branches require their value without explicit unbacked handling.

##

`PassConfig`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig)

Configuration for custom Inductor passes.

This is separate from general `CompilationConfig`

so that inductor passes don't all have access to full configuration - that would create a cycle as the `PassManager`

is set as a property of config.

You must pass PassConfig to VLLMConfig constructor via the CompilationConfig constructor. VLLMConfig's post_init does further initialization. If used outside of the VLLMConfig, some fields may be left in an improper state.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.compilation.PassConfig.compute_hash)Produces a hash unique to the pass configuration.

-
–[flashinfer_max_size](https://docs.vllm.ai#vllm.config.compilation.PassConfig.flashinfer_max_size)Returns the max communication size in bytes for flashinfer

-
–[log_enabled_passes](https://docs.vllm.ai#vllm.config.compilation.PassConfig.log_enabled_passes)Log the enabled custom fusion passes.


Attributes:

-
([eliminate_noops](https://docs.vllm.ai#vllm.config.compilation.PassConfig.eliminate_noops)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Eliminate no-op ops.

-
([enable_qk_norm_rope_fusion](https://docs.vllm.ai#vllm.config.compilation.PassConfig.enable_qk_norm_rope_fusion)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fused Q/K RMSNorm + RoPE pass.

-
([enable_sp](https://docs.vllm.ai#vllm.config.compilation.PassConfig.enable_sp)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable sequence parallelism. Requires TP>1. Automatically disabled

-
([fi_allreduce_fusion_max_size_mb](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fi_allreduce_fusion_max_size_mb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe threshold of the communicated tensor sizes under which

-
([fuse_act_padding](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_act_padding)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom RMSNorm + padding ops.

-
([fuse_act_quant](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_act_quant)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom SiluMul + quant ops.

-
([fuse_allreduce_rms](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_allreduce_rms)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable flashinfer allreduce fusion.

-
([fuse_attn_quant](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_attn_quant)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom Attention and MLAAttention + quant ops.

-
([fuse_gemm_comms](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_gemm_comms)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable async TP.

-
([fuse_mla_dual_rms_norm](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_mla_dual_rms_norm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse paired q/kv RMS norms in MLA attention.

-
([fuse_norm_quant](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_norm_quant)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom RMSNorm + quant ops.

-
([fuse_qk_norm_rope_kvcache](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_qk_norm_rope_kvcache)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse QK RMSNorm + RoPE + KV cache update into a single AITER HIP

-
([fuse_rope_kvcache](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_rope_kvcache)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the QK rope + KV cache ops.

-
([fuse_rope_kvcache_cat_mla](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_rope_kvcache_cat_mla)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fused MLA KV cache update with RoPE.

-
([rope_kvcache_fusion_max_token_num](https://docs.vllm.ai#vllm.config.compilation.PassConfig.rope_kvcache_fusion_max_token_num)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The threshold for ROCm AITER RoPE+KVCache fusion e.g. for small batch decode.

-
([sp_min_token_num](https://docs.vllm.ai#vllm.config.compilation.PassConfig.sp_min_token_num)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe minimum number of tokens above which vllm should use


## Source code in `vllm/config/compilation.py`


|
|

###

`eliminate_noops = Field(default=True)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.eliminate_noops)

Eliminate no-op ops.

###

`enable_qk_norm_rope_fusion = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.enable_qk_norm_rope_fusion)

Enable fused Q/K RMSNorm + RoPE pass.

###

`enable_sp = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.enable_sp)

Enable sequence parallelism. Requires TP>1. Automatically disabled if the model's hidden_size is too small for SP to be beneficial (threshold is device-capability dependent).

###

`fi_allreduce_fusion_max_size_mb = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fi_allreduce_fusion_max_size_mb)

The threshold of the communicated tensor sizes under which vllm should use flashinfer fused allreduce. Specified as a float in MB. Unspecified will fallback to default values which are compute capability and world size dependent. FI_ALLREDUCE_FUSION_MAX_SIZE_MB = { 90: { 2: 64, # 64MB 4: 2, # 2MB 8: 1, # 1MB }, 100: { 2: 64, # 64MB 4: 32, # 32MB 8: 1, # 1MB }, }, where key is the device capability

###

`fuse_act_padding = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_act_padding)

Fuse the custom RMSNorm + padding ops.

###

`fuse_act_quant = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_act_quant)

Fuse the custom SiluMul + quant ops.

###

`fuse_allreduce_rms = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_allreduce_rms)

Enable flashinfer allreduce fusion.

###

`fuse_attn_quant = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_attn_quant)

Fuse the custom Attention and MLAAttention + quant ops.

###

`fuse_gemm_comms = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_gemm_comms)

Enable async TP.

###

`fuse_mla_dual_rms_norm = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_mla_dual_rms_norm)

Fuse paired q/kv RMS norms in MLA attention.

###

`fuse_norm_quant = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_norm_quant)

Fuse the custom RMSNorm + quant ops.

###

`fuse_qk_norm_rope_kvcache = Field(default=None)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_qk_norm_rope_kvcache)

Fuse QK RMSNorm + RoPE + KV cache update into a single AITER HIP kernel. Supersedes both enable_qk_norm_rope_fusion and fuse_rope_kvcache for layers that support it. Auto-enabled at O1+ on ROCm for models with QK-norm (e.g. Qwen3-MoE).

###

`fuse_rope_kvcache = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_rope_kvcache)

Fuse the QK rope + KV cache ops.

###

`fuse_rope_kvcache_cat_mla = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.fuse_rope_kvcache_cat_mla)

Enable fused MLA KV cache update with RoPE.

###

`rope_kvcache_fusion_max_token_num = 256`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.rope_kvcache_fusion_max_token_num)

The threshold for ROCm AITER RoPE+KVCache fusion e.g. for small batch decode. Larger batch sizes e.g. during prefill will use the unfused kernels. Also applies to the fused QK-Norm+RoPE+KVCache pass.

###

`sp_min_token_num = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.sp_min_token_num)

The minimum number of tokens above which vllm should use sequence parallelism. Specified as an integer token count. Unspecified will fallback to default values which are compute capability and world size dependent.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/compilation.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.compute_hash)

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

## Source code in `vllm/config/compilation.py`


###

`flashinfer_max_size(world_size)`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.flashinfer_max_size)

Returns the max communication size in bytes for flashinfer allreduce fusion for the given world size. Returns None if world size is not supported by configs as it's not supported by flashinfer.

## Source code in `vllm/config/compilation.py`


###

`log_enabled_passes()`

[¶](https://docs.vllm.ai#vllm.config.compilation.PassConfig.log_enabled_passes)

Log the enabled custom fusion passes. This is called at the end of VLLMConfig post_init, after all defaults are finalized. TODO also log the compile ranges for which this is enabled.