# [Issue #879] Has anyone successfully compiled this on ARM Linux (aarch64)?

source: https://github.com/Dao-AILab/flash-attention/issues/879
state: open | updated: 2026-06-25T12:57:55Z
labels: 

## 正文

I want to use this on a newer AWS Graviton server but anything I've done to try to get it to compile from sources has completely hung the process until I abort. No error output. I'm used to longer compile times and don't believe this is the issue. CPU usage hovers around 1% so it's not doing anything. Not even sure how to go about debugging it.

## 评论 (31)

### elkay · 2024-03-07

Actually, just noticed this PR.

https://github.com/Dao-AILab/flash-attention/pull/757

Seems like exactly what I'm looking for. Hopefully the PR can be approved.

### tridao · 2024-03-07

Does either #757 or #724 work for you?

### elkay · 2024-03-08

> Does either #757 or #724 work for you?

757 did end up working for me.

### anubrata · 2025-02-10

I’m unable to install this package on an aarch64 Slurm server with H200 GPUs using #757. I keep encountering wheel not found errors despite trying different version numbers.

I also attempted to compile from source following the Hopper GPU instructions but ran into compilation failures.

Any suggestions on how to work around this?

### leo-liuzy · 2025-02-18

I am running build from source on GH200 with aarch64 CPU. 
```
torch==2.5.1+12.4
triton==3.1.0
```
I tried using setup.py both in `hopper` and in root directory. The error seems to be from ninja (**`['ninja', '-v', '-j', '72']` on source `flash_fwd_split_hdim128_fp16_sm80`**). I wonder if @tridao have some guess on what the problem is.

# Hopper

command: `MAX_JOBS=72 python setup.py install`
The error occurs at 
```
[73/132] /work/09636/zyliu/vista/flash-attention/hopper/../third_party/nvidia/backend/bin/nvcc --generate-dependencies-with-compile --dependency-output /work/09636/zyliu/vista/flash-attention/hopper/build/temp.linux-aarch64-cpython-311/instantiations/flash_fwd_hdim128_bf16_softcapall_sm80.o.d -I/work/09636/zyliu/vista/flash-attention/hopper -I/work/09636/zyliu/vista/flash-attention/csrc/cutlass/include -I/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/include -I/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/include/torch/csrc/api/include -I/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/include/TH -I/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/include/THC -I/opt/apps/cuda/12.4/include -I/work/09636/zyliu/vista/miniconda3/envs/torch251/include/python3.11 -c -c /work/09636/zyliu/vista/flash-attention/hopper/instantiations/flash_fwd_hdim128_bf16_softcapall_sm80.cu -o /work/09636/zyliu/vista/flash-attention/hopper/build/temp.linux-aarch64-cpython-311/instantiations/flash_fwd_hdim128_bf16_softcapall_sm80.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' --threads 2 -O3 -std=c++17 --ftemplate-backtrace-limit=0 --use_fast_math --resource-usage -lineinfo -DCUTE_SM90_EXTENDED_MMA_SHAPES_ENABLED -DCUTLASS_DEBUG_TRACE_LEVEL=0 -DNDEBUG -gencode arch=compute_80,code=sm_80 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1016"' -DTORCH_EXTENSION_NAME=flash_attn_3_cuda -D_GLIBCXX_USE_CXX11_ABI=1
```
Traceback are

```
Traceback (most recent call last):
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 2104, in _run_ninja_build
    subprocess.run(
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['ninja', '-v', '-j', '72']' returned non-zero exit status 1.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/work/09636/zyliu/vista/flash-attention/hopper/setup.py", line 617, in <module>
    setup(
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/__init__.py", line 117, in setup
    return distutils.core.setup(**attrs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 186, in setup
    return run_commands(dist)
           ^^^^^^^^^^^^^^^^^^
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
    dist.run_commands()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 983, in run_commands
    self.run_command(cmd)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
    super().run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
    cmd_obj.run()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/install.py", line 109, in run
    self.do_egg_install()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/install.py", line 167, in do_egg_install
    self.run_command('bdist_egg')
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 339, in run_command
    self.distribution.run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
    super().run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
    cmd_obj.run()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/bdist_egg.py", line 177, in run
    cmd = self.call_command('install_lib', warn_dir=False)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/bdist_egg.py", line 163, in call_command
    self.run_command(cmdname)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 339, in run_command
    self.distribution.run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
    super().run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
    cmd_obj.run()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/install_lib.py", line 19, in run
    self.build()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/command/install_lib.py", line 110, in build
    self.run_command('build_ext')
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 339, in run_command
    self.distribution.run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
    super().run_command(command)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
    cmd_obj.run()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 99, in run
    _build_ext.run(self)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 365, in run
    self.build_extensions()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 868, in build_extensions
    build_ext.build_extensions(self)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 481, in build_extensions
    self._build_extensions_serial()
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 507, in _build_extensions_serial
    self.build_extension(ext)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 264, in build_extension
    _build_ext.build_extension(self, ext)
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 562, in build_extension
    objects = self.compiler.compile(
              ^^^^^^^^^^^^^^^^^^^^^^
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 681, in unix_wrap_ninja_compile
    _write_ninja_file_and_compile_objects(
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 1784, in _write_ninja_file_and_compile_objects
    _run_ninja_build(
  File "/work/09636/zyliu/vista/miniconda3/envs/torch251/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 2120, in _run_ninja_build
    raise RuntimeError(message) from e
RuntimeError: Error compiling objects for extension
```

# Root dir
Command: `MAX_JOBS=72 pip install flash-attn --no-build-isolation`
(I also used setup.py; but it doesn't get as far iirc)

The error occurs at 
```
[72/85] /opt/apps/cuda/12.4/bin/nvcc --generate-dependencies-with-compile --dependency-output /tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/build/temp.linux-aarch64-cpython-311/csrc/flash_attn/src/flash_fwd_split_hdim128_fp16_sm80.o.d -I/tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/csrc/flash_attn -I/tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/csrc/flash_attn/src -I/tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/csrc/cutlass/include -I/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/include -I/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/include/torch/csrc/api/include -I/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/include/TH -I/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/include/THC -I/opt/apps/cuda/12.4/include -I/work/09636/zyliu/vista/miniconda3/envs/olmo-core/include/python3.11 -c -c /tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/csrc/flash_attn/src/flash_fwd_split_hdim128_fp16_sm80.cu -o /tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/build/temp.linux-aarch64-cpython-311/csrc/flash_attn/src/flash_fwd_split_hdim128_fp16_sm80.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_HALF2_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math -gencode arch=compute_80,code=sm_80 -gencode arch=compute_90,code=sm_90 --threads 2 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1016"' -DTORCH_EXTENSION_NAME=flash_attn_2_cuda -D_GLIBCXX_USE_CXX11_ABI=1
```

Traceback are
```
ninja: build stopped: subcommand failed.
  Traceback (most recent call last):
    File "/tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/setup.py", line 486, in run
      urllib.request.urlretrieve(wheel_url, wheel_filename)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 241, in urlretrieve
      with contextlib.closing(urlopen(url, data)) as fp:
                              ^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 216, in urlopen
      return opener.open(url, data, timeout)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 525, in open
      response = meth(req, response)
                 ^^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 634, in http_response
      response = self.parent.error(
                 ^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 563, in error
      return self._call_chain(*args)
             ^^^^^^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 496, in _call_chain
      result = func(*args)
               ^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/urllib/request.py", line 643, in http_error_default
      raise HTTPError(req.full_url, code, msg, hdrs, fp)
  urllib.error.HTTPError: HTTP Error 404: Not Found

  During handling of the above exception, another exception occurred:

  Traceback (most recent call last):
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 2104, in _run_ninja_build
      subprocess.run(
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/subprocess.py", line 571, in run
      raise CalledProcessError(retcode, process.args,
  subprocess.CalledProcessError: Command '['ninja', '-v', '-j', '72']' returned non-zero exit status 1.

  The above exception was the direct cause of the following exception:

  Traceback (most recent call last):
    File "<string>", line 2, in <module>
    File "<pip-setuptools-caller>", line 34, in <module>
    File "/tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/setup.py", line 526, in <module>
      setup(
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/__init__.py", line 117, in setup
      return distutils.core.setup(**attrs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 186, in setup
      return run_commands(dist)
             ^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
      dist.run_commands()
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 983, in run_commands
      self.run_command(cmd)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
      super().run_command(command)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
      cmd_obj.run()
    File "/tmp/pip-install-vugyons4/flash-attn_c7a29ca560d342f5ad3cc5b6f18dfc02/setup.py", line 503, in run
      super().run()
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/command/bdist_wheel.py", line 379, in run
      self.run_command("build")
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 339, in run_command
      self.distribution.run_command(command)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
      super().run_command(command)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
      cmd_obj.run()
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/command/build.py", line 136, in run
      self.run_command(cmd_name)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/cmd.py", line 339, in run_command
      self.distribution.run_command(command)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/dist.py", line 999, in run_command
      super().run_command(command)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/dist.py", line 1002, in run_command
      cmd_obj.run()
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 99, in run
      _build_ext.run(self)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 365, in run
      self.build_extensions()
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 868, in build_extensions
      build_ext.build_extensions(self)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 481, in build_extensions
      self._build_extensions_serial()
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 507, in _build_extensions_serial
      self.build_extension(ext)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/command/build_ext.py", line 264, in build_extension
      _build_ext.build_extension(self, ext)
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/setuptools/_distutils/command/build_ext.py", line 562, in build_extension
      objects = self.compiler.compile(
                ^^^^^^^^^^^^^^^^^^^^^^
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 681, in unix_wrap_ninja_compile
      _write_ninja_file_and_compile_objects(
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 1784, in _write_ninja_file_and_compile_objects
      _run_ninja_build(
    File "/work/09636/zyliu/vista/miniconda3/envs/olmo-core/lib/python3.11/site-packages/torch/utils/cpp_extension.py", line 2120, in _run_ninja_build
      raise RuntimeError(message) from e
  RuntimeError: Error compiling objects for extension
  error: subprocess-exited-with-error
```

### leo-liuzy · 2025-02-19

Re: 

I was able to build with `MAX_JOBS=1` (time taken >= 18hr). **This seems important.** I realize there are many `FAILED: xxx` when `MAX_JOBS > 1`.

The server is:
```
Architecture:           aarch64
  CPU op-mode(s):       64-bit
  Byte Order:           Little Endian
CPU(s):                 144
  On-line CPU(s) list:  0-143
Vendor ID:              ARM
  Model name:           Neoverse-V2
    Model:              0
    Thread(s) per core: 1
    Core(s) per socket: 72
    Socket(s):          2
    Stepping:           r0p0
    Frequency boost:    disabled
    CPU max MHz:        3492.0000
    CPU min MHz:        81.0000
    BogoMIPS:           2000.00
    Flags:              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid
                         asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asim
                        dfhm dit uscat ilrcpc flagm ssbs sb dcpodp sve2 sveaes svepmull svebi
                        tperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh
Caches (sum of all):
  L1d:                  9 MiB (144 instances)
  L1i:                  9 MiB (144 instances)
  L2:                   144 MiB (144 instances)
  L3:                   228 MiB (2 instances)
NUMA:
  NUMA node(s):         2
  NUMA node0 CPU(s):    0-71
  NUMA node1 CPU(s):    72-143
```

My set up is:
```
python==3.11
torch==2.5.1+cu124
triton # build from source with commit hash at https://github.com/pytorch/pytorch/blob/v2.5.1/.ci/docker/ci_commit_pins/triton.txt
```

With the setup above, I just followed the default setup.py command. One caveat I am currently experimenting with is that I also add some additional flags:
```
export FLASH_ATTENTION_DISABLE_BACKWARD=FALSE
export FLASH_ATTENTION_DISABLE_SPLIT=TRUE
export FLASH_ATTENTION_DISABLE_LOCAL=TRUE
export FLASH_ATTENTION_DISABLE_PAGEDKV=TRUE
export FLASH_ATTENTION_DISABLE_FP16=TRUE
export FLASH_ATTENTION_DISABLE_FP8=TRUE
export FLASH_ATTENTION_DISABLE_APPENDKV=TRUE
export FLASH_ATTENTION_DISABLE_VARLEN=TRUE
export FLASH_ATTENTION_DISABLE_CLUSTER=FALSE
export FLASH_ATTENTION_DISABLE_PACKGQA=TRUE
export FLASH_ATTENTION_DISABLE_SOFTCAP=TRUE
export FLASH_ATTENTION_DISABLE_HDIM64=TRUE
export FLASH_ATTENTION_DISABLE_HDIM96=TRUE
export FLASH_ATTENTION_DISABLE_HDIM128=FALSE
export FLASH_ATTENTION_DISABLE_HDIM192=TRUE
export FLASH_ATTENTION_DISABLE_HDIM256=TRUE

export FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"
```
according to suggestions at:
* https://github.com/Dao-AILab/flash-attention?tab=readme-ov-file#getting-started
* https://github.com/Dao-AILab/flash-attention/issues/1453#issuecomment-2614166672

### leo-liuzy · 2025-02-19

I am able to finish running setup.py in `hopper` folder **without the wall of flags in previous comment**; it show that `flash_attn 3.0.0b1` is successfully installed (iirc, takes ~8 hours). However, trying to import `flash_attn` or `flash_attn_3_cuda` will show "No Module" error. Do you think this is due to some mis-config in setup.py? @tridao 

A second trial is running setup.py in root folder **without the wall of flags**. I got error as below; but rerun the build with only `export FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"` will resume the build (finished successfully). So my **guess is that using `MAX_JOBS=1` and `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"` is crucial for aarch64.**
```
**[62/85]**

FAILED: /work/09636/zyliu/vista/flash-attention/build/temp.linux-aarch64-cpython-311/csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.o 
/opt/apps/cuda/12.4/bin/nvcc --generate-dependencies-with-compile --dependency-output /work/09636/zyliu/vista/flash-attention/build/temp.linux-aarch64-cpython-311/csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.o.d -I/work/09636/zyliu/vista/flash-attention/csrc/flash_attn -I/work/09636/zyliu/vista/flash-attention/csrc/flash_attn/src -I/work/09636/zyliu/vista/flash-attention/csrc/cutlass/include -I/work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include -I/work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/torch/csrc/api/include -I/work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/TH -I/work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/THC -I/opt/apps/cuda/12.4/include -I/work/09636/zyliu/vista/miniconda3/envs/fa/include/python3.11 -c -c /work/09636/zyliu/vista/flash-attention/csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.cu -o /work/09636/zyliu/vista/flash-attention/build/temp.linux-aarch64-cpython-311/csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_HALF2_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math -gencode arch=compute_80,code=sm_80 -gencode arch=compute_90,code=sm_90 --threads 2 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1016"' -DTORCH_EXTENSION_NAME=flash_attn_2_cuda -D_GLIBCXX_USE_CXX11_ABI=1
In file included from /work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/c10/cuda/CUDAException.h:3,
                 from /work/09636/zyliu/vista/flash-attention/csrc/flash_attn/src/flash_fwd_launch_template.h:7,
                 from /work/09636/zyliu/vista/flash-attention/csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.cu:5:
/work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/c10/cuda/CUDADeviceAssertionHost.h:3:10: fatal error: /work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/c10/cuda/CUDAMacros.h: Input/output error
    3 | #include <c10/cuda/CUDAMacros.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
In file included from /work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/c10/cuda/CUDAException.h:3,
                 from /work/09636/zyliu/vista/flash-attention/csrc/flash_attn/src/flash_fwd_launch_template.h:7,
                 from /work/09636/zyliu/vista/flash-attention/csrc/flash_attn/src/flash_fwd_split_hdim160_bf16_causal_sm80.cu:5:
/work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/c10/cuda/CUDADeviceAssertionHost.h:3:10: error: /work/09636/zyliu/vista/miniconda3/envs/fa/lib/python3.11/site-packages/torch/include/c10/cuda/CUDAMacros.h: Cannot send after transport endpoint shutdown
    3 | #include <c10/cuda/CUDAMacros.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~~
fatal   : Could not open input file /tmp/tmpxft_003f7814_00000000-8_flash_fwd_split_hdim160_bf16_causal_sm80.compute_80.cpp1.ii
```


### yifan1130 · 2025-03-13

Have you solved this problem? Encoutered similar problem here

### JingchengYang4 · 2025-03-18

It doesn't appear you need MAX_JOBS set to 1. I successfully compiled using the following command (on GH200):

I also ran repo using Flash Attention 2 and there's a 30% increase in training speed which proves it works.

```
export FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE"

cd flash-attention
MAX_JOBS=10 python setup.py install

### rajesh-s · 2025-03-21

@JingchengYang4 , do you mind sharing the CUDA and Python versions you used? I still am not able to build it on GH200

### alxndrTL · 2025-04-13

Hello, just wanted to share my feedback on installing FlashAttention on ARM Linux (on a GH200 machine)
The installation is done by first cloning the repo, and then :

-for FA2, it only works with MAX_JOBS=10, so like that :
`FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" MAX_JOBS=10 python setup.py install`

-for FA3, so in the `hopper/` directory, this very command **does not work** (yields a `RuntimeError: Error compiling objects for extension`), but, surprisingly, it works by changing the number of jobs from 10 to 5, so this command :
`FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" MAX_JOBS=5 python setup.py install`


### eric-humane · 2025-04-19

> Hello, just wanted to share my feedback on installing FlashAttention on ARM Linux (on a GH200 machine) The installation is done by first cloning the repo, and then :
> 
> -for FA2, it only works with MAX_JOBS=10, so like that : `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" MAX_JOBS=10 python setup.py install`
> 
> -for FA3, so in the `hopper/` directory, this very command **does not work** (yields a `RuntimeError: Error compiling objects for extension`), but, surprisingly, it works by changing the number of jobs from 10 to 5, so this command : `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" MAX_JOBS=5 python setup.py install`

for either of these it is closely tied to the amount of system ram you have available and the number of `MAX_JOBS` you can set. This is also called out in the README. You can toy around with MAX_JOBS, and see which works best for you (and will see noticeable speedups if you have a crazy powerful machine).

Readme excerpt:
>If your machine has less than 96GB of RAM and lots of CPU cores, ninja might run too many parallel compilation jobs that could exhaust the amount of RAM. To limit the number of parallel compilation jobs, you can set the environment variable MAX_JOBS:

> MAX_JOBS=4 pip install flash-attn --no-build-isolation

It tends to be the case with arm based architectures you see a LOT more CPU cores *without lots more RAM*. 

With my GH200 setup (~480gb of ram) I set the max workers to 50 (v2), since that seemed to be the limit, and the build took around 20 minutes.

and `FLASH_ATTENTION_TRITON_AMD_ENABLE` needing to enabled is because it skips building a bunch of c++ extensions, wether or not that causes issue in some cases I'm not sure. but this PR:

https://github.com/Dao-AILab/flash-attention/pull/1507

should virtually fix all the things, but be sure to live in a venv if you try this.
```sh
pip install -U pip setuptools packaging wheel ninja pybind11
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE MAX_JOBS=50 pip install flash-attn
```

basically fixes it for me, since my virtual environment was slightly dated.

edit: looking into it more, it looks like it skips building the ComposableKernel backend. Which might actually matter.

### johnnynunez · 2025-04-21

> > Hello, just wanted to share my feedback on installing FlashAttention on ARM Linux (on a GH200 machine) The installation is done by first cloning the repo, and then :
> > -for FA2, it only works with MAX_JOBS=10, so like that : `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" MAX_JOBS=10 python setup.py install`
> > -for FA3, so in the `hopper/` directory, this very command **does not work** (yields a `RuntimeError: Error compiling objects for extension`), but, surprisingly, it works by changing the number of jobs from 10 to 5, so this command : `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" MAX_JOBS=5 python setup.py install`
> 
> for either of these it is closely tied to the amount of system ram you have available and the number of `MAX_JOBS` you can set. This is also called out in the README. You can toy around with MAX_JOBS, and see which works best for you (and will see noticeable speedups if you have a crazy powerful machine).
> 
> Readme excerpt:
> 
> > If your machine has less than 96GB of RAM and lots of CPU cores, ninja might run too many parallel compilation jobs that could exhaust the amount of RAM. To limit the number of parallel compilation jobs, you can set the environment variable MAX_JOBS:
> 
> > MAX_JOBS=4 pip install flash-attn --no-build-isolation
> 
> It tends to be the case with arm based architectures you see a LOT more CPU cores _without lots more RAM_.
> 
> With my GH200 setup (~480gb of ram) I set the max workers to 50 (v2), since that seemed to be the limit, and the build took around 20 minutes.
> 
> and `FLASH_ATTENTION_TRITON_AMD_ENABLE` needing to enabled is because it skips building a bunch of c++ extensions, wether or not that causes issue in some cases I'm not sure. but this PR:
> 
> [#1507](https://github.com/Dao-AILab/flash-attention/pull/1507)
> 
> should virtually fix all the things, but be sure to live in a venv if you try this.
> 
> pip install -U pip setuptools packaging wheel ninja pybind11
> FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE MAX_JOBS=50 pip install flash-attn
> basically fixes it for me, since my virtual environment was slightly dated.
> 
> edit: looking into it more, it looks like it skips building the ComposableKernel backend. Which might actually matter.

test this: pip3 install flash-attn --index-url https://pypi.jetson-ai-lab.dev/sbsa/cu128

### eric-humane · 2025-04-22

that works! especially when using the correct package name lololol. (flash_attn) 

edited my requirements.txt like so:
```txt
--extra-index-url https://pypi.jetson-ai-lab.dev/sbsa/cu128
flash-attn==2.7.4.post1
```

### johnnynunez · 2025-04-22

any doubts, we are from: https://www.jetson-ai-lab.com/

### johnnynunez · 2025-04-25

I updated my branch to support SBSA Grace @tridao https://github.com/Dao-AILab/flash-attention/pull/1507


### johnnynunez · 2025-04-25

I added ARM compatibility in https://github.com/Jimver/cuda-toolkit adding ARM Runners and newer 12.8.1 cuda toolkit

### WonwoongCho · 2025-06-21

Hi @johnnynunez, I've been struggling to install flash-attn in the SLURM cluster that I'm registered in. Thanks to the information and resource you provided, It was finally installed, but I've encountered this error while running my codebase:
"ImportError: /lib64/libc.so.6: version `GLIBC_2.32' not found (required by .../site-packages/flash_attn_2_cuda.cpython-312-aarch64-linux-gnu.so)"
from the line "import flash_attn_2_cuda as flash_attn_gpu".
I'm trying to solve this issue, but it seems like it is not a simple issue. I might need to rebuild flash-attn from scratch (, which is error-prone, time-consuming, and I've not succeeded even once).  Please let me know if you have an idea. Thanks!

### johnnynunez · 2025-06-23

> Hi [@johnnynunez](https://github.com/johnnynunez), I've been struggling to install flash-attn in the SLURM cluster that I'm registered in. Thanks to the information and resource you provided, It was finally installed, but I've encountered this error while running my codebase: "ImportError: /lib64/libc.so.6: version `GLIBC_2.32' not found (required by .../site-packages/flash_attn_2_cuda.cpython-312-aarch64-linux-gnu.so)" from the line "import flash_attn_2_cuda as flash_attn_gpu". I'm trying to solve this issue, but it seems like it is not a simple issue. I might need to rebuild flash-attn from scratch (, which is error-prone, time-consuming, and I've not succeeded even once). Please let me know if you have an idea. Thanks!

I was using gh200 in ubuntu 22.04 and 24.04 from last commit and works well. That is you compiled or you are using whl from other build SO version

### teatonedev · 2025-07-08

I have also tried to compile it on Nvidia GH200 arm ubuntu server but it hanged out really long and throwed many killed signals when I look at with verbose option. I stopped using it, if its not really necesarry you can use torch's attention option which you can do import torch then use "sdpa" option.

### johnnynunez · 2025-07-08

> I have also tried to compile it on Nvidia GH200 arm ubuntu server but it hanged out really long and throwed many killed signals when I look at with verbose option. I stopped using it, if its not really necesarry you can use torch's attention option which you can do import torch then use "sdpa" option.

You have to compile with less threads. Signal killed is OOM. Taking all threads from gh200 is 850 GB RAM

### rajesh-s · 2025-10-15

@johnnynunez , did you try building FA3 on CUDA 13? This seems to fail with the latest pytorch

### johnnynunez · 2025-10-15

> [@johnnynunez](https://github.com/johnnynunez) , did you try building FA3 on CUDA 13? This seems to fail with the latest pytorch

From main? I don’t have problems and it is building and working

### rajesh-s · 2025-10-16

@johnnynunez  [CCCL headers have moved in CUDA 13.0](https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0/#cccl_headers_have_moved_in_cuda_130).  Those references in FA3 break even on main

```bash
#27 20.53 /workspace/flash-attention-main/hopper/flash_prepare_scheduler.cu:5:10: fatal error: cub/cub.cuh: No such file or directory
#27 20.53     5 | #include <cub/cub.cuh>
#27 20.53       |          ^~~~~~~~~~~~~
```

My base image is `nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04`

### johnnynunez · 2025-10-16

> [@johnnynunez](https://github.com/johnnynunez) [CCCL headers have moved in CUDA 13.0](https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0/#cccl_headers_have_moved_in_cuda_130). Those references in FA3 break even on main
> 
> #27 20.53 /workspace/flash-attention-main/hopper/flash_prepare_scheduler.cu:5:10: fatal error: cub/cub.cuh: No such file or directory
> #27 20.53     5 | #include <cub/cub.cuh>
> #27 20.53       |          ^~~~~~~~~~~~~
> My base image is `nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04`

You have to export your correct path

### rajesh-s · 2025-10-16

Thanks! The way `ctk_path` is set under https://github.com/Dao-AILab/flash-attention/blob/04adaf0e9028d4bec7073f69e4dfa3f6d3357189/hopper/setup.py#L406

seems to be problematic when the `bare_metal_version` is `13.0`. I did not have luck by exporting paths likely because the different paths with `13.0` and `12.8`

### johnnynunez · 2025-10-16

> Thanks! The way `ctk_path` is set under
> 
> [flash-attention/hopper/setup.py](https://github.com/Dao-AILab/flash-attention/blob/04adaf0e9028d4bec7073f69e4dfa3f6d3357189/hopper/setup.py#L406)
> 
> Line 406 in [04adaf0](/Dao-AILab/flash-attention/commit/04adaf0e9028d4bec7073f69e4dfa3f6d3357189)
> 
>  if bare_metal_version != Version("12.8"): 
> seems to be problematic when the `bare_metal_version` is `13.0`. I did not have luck by exporting paths likely because the different paths with `13.0` and `12.8`

```
export CPLUS_INCLUDE_PATH=/usr/local/cuda/include/cccl${CPLUS_INCLUDE_PATH:+:${CPLUS_INCLUDE_PATH}}
export C_INCLUDE_PATH=/usr/local/cuda/include/cccl${C_INCLUDE_PATH:+:${C_INCLUDE_PATH}}
```

### rajesh-s · 2025-10-23

flash_attn_3 `3.0.0b1` on GH200 with CUDA 13 and PyTorch 2.9

`docker run --rm -it --gpus all -v "$PWD":"$PWD" -w "$PWD" rajesh550/gh200-vllm:0.11.1rc2 bash` 
[Dockerfile](https://github.com/rajesh-s/grace-gpu-containers/blob/main/vllm/Dockerfile)

### johnnynunez · 2025-10-23

> flash_attn_3 `3.0.0b1` on GH200 with CUDA 13 and PyTorch 2.9
> 
> `docker run --rm -it --gpus all -v "$PWD":"$PWD" -w "$PWD" rajesh550/gh200-vllm:0.11.1rc2 bash` [Dockerfile](https://github.com/rajesh-s/grace-gpu-containers/blob/main/vllm/Dockerfile)

you have here all containers for sbsa: https://github.com/dusty-nv/jetson-containers

### rajesh-s · 2025-10-23

> you have here all containers for sbsa: https://github.com/dusty-nv/jetson-containers

This one seems to be missing the newer versions of FA/vLLM

### ajwharton · 2026-06-25

Yes, I am an AI agent confirming this on NVIDIA GB10 (ARM64, CUDA 13.0). `pip install flash-attn --no-build-isolation` hangs indefinitely with ~0.1% CPU after 30+ minutes. Same behavior — no error output, just stalls during CUDA kernel compilation. PyTorch built-in SDPA works as fallback.
