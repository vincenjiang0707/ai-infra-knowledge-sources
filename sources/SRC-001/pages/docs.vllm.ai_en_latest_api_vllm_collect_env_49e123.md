source: https://docs.vllm.ai/en/latest/api/vllm/collect_env/
lastmod: 2026-09-24

#

`vllm.collect_env`

[¶](https://docs.vllm.ai#vllm.collect_env)

Functions:

-
–[get_cudnn_version](https://docs.vllm.ai#vllm.collect_env.get_cudnn_version)Return a list of libcudnn.so; it's hard to tell which one is being used.

-
–[get_intel_graphics_compiler_version](https://docs.vllm.ai#vllm.collect_env.get_intel_graphics_compiler_version)Return Intel Graphics Compiler (IGC) version.

-
–[get_level_zero_driver_version](https://docs.vllm.ai#vllm.collect_env.get_level_zero_driver_version)Return Level Zero driver version.

-
–[get_level_zero_loader_version](https://docs.vllm.ai#vllm.collect_env.get_level_zero_loader_version)Return Level Zero loader runtime version.

-
–[get_oneapi_ccl_version](https://docs.vllm.ai#vllm.collect_env.get_oneapi_ccl_version)Return oneAPI Collective Communications Library (oneCCL) version.

-
–[get_oneapi_compiler_version](https://docs.vllm.ai#vllm.collect_env.get_oneapi_compiler_version)Return Intel oneAPI DPC++/C++ Compiler version via icpx.

-
–[get_pip_packages](https://docs.vllm.ai#vllm.collect_env.get_pip_packages)Return

`pip list`

output. Note: will also find conda-installed pytorch and numpy packages. -
–[get_rocm_version](https://docs.vllm.ai#vllm.collect_env.get_rocm_version)Returns the ROCm version if available, otherwise 'N/A'.

-
–[get_sycl_version](https://docs.vllm.ai#vllm.collect_env.get_sycl_version)Return SYCL/DPC++ compiler build version.

-
–[run](https://docs.vllm.ai#vllm.collect_env.run)Return (return-code, stdout, stderr).

-
–[run_and_parse_first_match](https://docs.vllm.ai#vllm.collect_env.run_and_parse_first_match)Run command using run_lambda, returns the first regex match if it exists.

-
–[run_and_read_all](https://docs.vllm.ai#vllm.collect_env.run_and_read_all)Run command using run_lambda; reads and returns entire output if rc is 0.


##

`get_cudnn_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_cudnn_version)

Return a list of libcudnn.so; it's hard to tell which one is being used.

## Source code in `vllm/collect_env.py`


##

`get_intel_graphics_compiler_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_intel_graphics_compiler_version)

##

`get_level_zero_driver_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_level_zero_driver_version)

##

`get_level_zero_loader_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_level_zero_loader_version)

##

`get_oneapi_ccl_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_oneapi_ccl_version)

##

`get_oneapi_compiler_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_oneapi_compiler_version)

Return Intel oneAPI DPC++/C++ Compiler version via icpx.

##

`get_pip_packages(run_lambda, patterns=None)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_pip_packages)

Return `pip list`

output. Note: will also find conda-installed pytorch and numpy packages.

## Source code in `vllm/collect_env.py`


##

`get_rocm_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_rocm_version)

##

`get_sycl_version(run_lambda)`

[¶](https://docs.vllm.ai#vllm.collect_env.get_sycl_version)

##

`run(command)`

[¶](https://docs.vllm.ai#vllm.collect_env.run)

Return (return-code, stdout, stderr).

## Source code in `vllm/collect_env.py`


##

`run_and_parse_first_match(run_lambda, command, regex)`

[¶](https://docs.vllm.ai#vllm.collect_env.run_and_parse_first_match)

Run command using run_lambda, returns the first regex match if it exists.

## Source code in `vllm/collect_env.py`


##

`run_and_read_all(run_lambda, command)`

[¶](https://docs.vllm.ai#vllm.collect_env.run_and_read_all)

Run command using run_lambda; reads and returns entire output if rc is 0.