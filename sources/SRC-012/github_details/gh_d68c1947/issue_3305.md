# [Issue #3305] [Bug] convert weight  Qwen3-Coder-30B-A3B-Instruct  q4f16_ft  KeyError

source: https://github.com/mlc-ai/mlc-llm/issues/3305
state: closed | updated: 2026-01-25T17:34:06Z
labels: bug

## 正文

## 🐛 Bug

When I convert Qwen3-Coder-30B-A3B-Instruct by q4f16_ft, I got following error.

## To Reproduce

Steps to reproduce the behavior:

just run:
mlc_llm convert_weight Qwen3-Coder-30B-A3B-Instruct --quantization q4f16_ft -o my-Qwen3-Coder-30B-A3B-Instruct-q4f16_ft-MLC/

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): CUDA
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Ubuntu
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...): Orin
 - How you installed MLC-LLM (`conda`, source): source
 - How you installed TVM-Unity (`pip`, source): source
 - Python version (e.g. 3.10): 3.11
 - GPU driver version (if applicable): NVIDIA-SMI 540.4.0                Driver Version: 540.4.0
 - CUDA/cuDNN version (if applicable): 12.6
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
```yaml
 BUILD_STATIC_RUNTIME: OFF
BUILD_DUMMY_LIBTVM: OFF
COMPILER_RT_PATH: 3rdparty/compiler-rt
CUDA_VERSION: 12.6
DLPACK_PATH: 3rdparty/dlpack/include
DMLC_PATH: 3rdparty/dmlc-core/include
GIT_COMMIT_HASH: b5736b32584c2c6f5caed655869c799ab494e6e3
```
GIT_COMMIT_TIME: 2025-08-09 16:49:10 -0400
```yaml
HIDE_PRIVATE_SYMBOLS: ON
INDEX_DEFAULT_I64: ON
INSTALL_DEV: OFF
LLVM_VERSION: 20.1.8
MLIR_VERSION: NOT-FOUND
PICOJSON_PATH: 3rdparty/picojson
RANG_PATH: 3rdparty/rang/include
ROCM_PATH: /opt/rocm
SUMMARIZE: OFF
TVM_CXX_COMPILER_PATH: /usr/bin/c++
USE_ALTERNATIVE_LINKER: AUTO
USE_ARM_COMPUTE_LIB_GRAPH_EXECUTOR: OFF
USE_ARM_COMPUTE_LIB: OFF
USE_BLAS: none
USE_BNNS: OFF
USE_BYODT_POSIT: OFF
USE_COREML: OFF
USE_CPP_RPC: OFF
USE_CPP_RTVM: OFF
USE_CUBLAS: ON
USE_CUDA: ON
USE_NVTX: OFF
USE_NCCL: OFF
USE_MSCCL: OFF
USE_CUDNN: ON
USE_CUSTOM_LOGGING: OFF
USE_CUTLASS: ON
USE_AMX: OFF
USE_DNNL: OFF
USE_FALLBACK_STL_MAP: OFF
USE_GTEST: AUTO
USE_HEXAGON: OFF
USE_HEXAGON_RPC: OFF
USE_HEXAGON_SDK: /path/to/sdk
USE_HEXAGON_GTEST: /path/to/hexagon/gtest
USE_HEXAGON_EXTERNAL_LIBS: OFF
USE_IOS_RPC: OFF
USE_KHRONOS_SPIRV: OFF
USE_LIBBACKTRACE: AUTO
USE_LIBTORCH: OFF
USE_LLVM: llvm-config --ignore-libllvm --link-static
USE_MLIR: OFF
USE_METAL: OFF
USE_MIOPEN: OFF
USE_MKL: OFF
USE_MRVL: OFF
USE_MSVC_MT: OFF
USE_NNPACK: OFF
USE_OPENCL: OFF
USE_OPENCL_ENABLE_HOST_PTR: OFF
USE_OPENCL_EXTN_QCOM: NOT-FOUND
USE_OPENCL_GTEST: /path/to/opencl/gtest
USE_OPENMP: none
USE_PAPI: OFF
USE_RANDOM: ON
TVM_DEBUG_WITH_ABI_CHANGE: OFF
TVM_LOG_BEFORE_THROW: OFF
USE_ROCBLAS: OFF
USE_HIPBLAS: OFF
USE_ROCM: OFF
USE_RCCL: OFF
USE_RPC: ON
USE_RTTI: ON
USE_RUST_EXT: OFF
USE_SORT: ON
USE_SPIRV_KHR_INTEGER_DOT_PRODUCT: OFF
USE_TENSORFLOW_PATH: none
USE_TENSORRT_CODEGEN: OFF
USE_TENSORRT_RUNTIME: OFF
USE_TFLITE: OFF
USE_THREADS: ON
USE_THRUST: ON
USE_CURAND: OFF
USE_VULKAN: OFF
USE_CLML: OFF
TVM_CLML_VERSION: 
USE_CLML_GRAPH_EXECUTOR: OFF
USE_UMA: OFF
USE_MSC: OFF
USE_CCACHE: AUTO
USE_NVSHMEM: OFF
USE_NNAPI_CODEGEN: OFF
USE_NNAPI_RUNTIME: OFF
BACKTRACE_ON_SEGFAULT: OFF
```
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (5)

### capyun · 2025-08-15

Sorry, I forget my error info.

Traceback (most recent call last):
  File "/home/smartsens/miniconda3/envs/mlc/bin/mlc_llm", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/__main__.py", line 38, in main
    cli.main(sys.argv[2:])
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/cli/convert_weight.py", line 88, in main
    convert_weight(
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/interface/convert_weight.py", line 182, in convert_weight
    _convert_args(args)
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/interface/convert_weight.py", line 146, in _convert_args
    tvmjs.dump_ndarray_cache(
  File "/home/smartsens/sdz/tvm-unity/python/tvm/contrib/tvmjs.py", line 273, in dump_ndarray_cache
    for k, origin_v in param_generator:
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/interface/convert_weight.py", line 129, in _param_generator
    for name, param in loader.load(device=args.device, preshard_funcs=preshard_funcs):
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/loader/huggingface_loader.py", line 121, in load
    for name, loader_param in self._load_or_quantize(mlc_name, param, device):
  File "/home/smartsens/sdz/mlc-llm/python/mlc_llm/loader/huggingface_loader.py", line 165, in _load_or_quantize
    q_params = self.quantize_param_map.map_func[mlc_name](param)
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: 'model.layers.47.mlp.gate.weight'

### capyun · 2025-08-15

bug fix:
modify ft_quantization.py line126 as following, Previously, self.quant_map.param_map[weight_name] = [f"{name}.q_weight", f"{name}.q_scale"] was placed outside the if condition.

                if isinstance(node, nn.Linear):
                    weight_name = f"{name}.weight"
                    if (
                        # pylint: disable=too-many-boolean-expressions
                        is_final_fc(name)
                        or node.out_dtype == "float32"
                        or (self.config.quantize_dtype == "int4" and node.out_features % 8 != 0)
                        or (self.config.quantize_dtype == "int8" and node.out_features % 4 != 0)
                    ):
                        # Under any of the conditions we fall back to GroupQuantize
                        # For `is_final_fc()` see https://github.com/mlc-ai/mlc-llm/issues/1723
                        # If simply skipping lm_head quantization degrades performance
                        # Other requirements are from CUTLASS
                        logger.info(
                            'Fallback to GroupQuantize for nn.Linear: "%s", '
                            + "weight.shape: %s, out_dtype: %s",
```python
                            bold(name),
                            node.weight.shape,
                            node.out_dtype,
                        )
                        group_quantize = self.config.fallback_group_quantize()
                        self.quant_map.param_map[weight_name] = [f"{name}.q_weight", f"{name}.q_scale"]
                        self.quant_map.map_func[weight_name] = group_quantize.quantize_weight
                        return GroupQuantizeLinear.from_linear(node, group_quantize)
                    if not is_moe_gate(name, node):
                        # print("yun---weight_name", weight_name)
                        self.quant_map.param_map[weight_name] = [f"{name}.q_weight", f"{name}.q_scale"]
                        self.quant_map.map_func[weight_name] = self.config.quantize_weight
                        return FTQuantizeLinear.from_linear(node, self.config)
```

### rankaiyx · 2025-08-18

How much improvement does q4f16_ft have compared to q4f16_1?

### capyun · 2025-08-21

> How much improvement does q4f16_ft have compared to q4f16_1?q4f16_ft 与 q4f16_1 相比有多少改进？

No improvement, lol.

### MasterJH5574 · 2026-01-25

Hi @capyun @rankaiyx, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
