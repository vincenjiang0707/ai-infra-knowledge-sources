# [Issue #10] Lecture3 - Issue with building CUDA code for RGB to Grayscale

source: https://github.com/gpu-mode/lectures/issues/10
state: closed | updated: 2024-07-29T23:51:31Z
labels: 

## 正文

Hi,

I am new to CUDA, so this might probably be a beginners issue!

I am following Jeremy's tutorial on building/writing CUDA code for rgb->gray scale and followed his notebook, but am failing when calling `module = load_cuda(cuda_src, cpp_src, ['rgb_to_grayscale'], verbose=True) `

Here's the trace stack:

```
Using /hdd4/srinath2/.cache/torch_extensions/py312_cu121 as PyTorch extensions root...
Creating extension directory /hdd4/srinath2/.cache/torch_extensions/py312_cu121/inline_ext...
Detected CUDA files, patching ldflags
Emitting ninja build file /hdd4/srinath2/.cache/torch_extensions/py312_cu121/inline_ext/build.ninja...
Building extension module inline_ext...
Allowing ninja to set a default number of workers... (overridable by setting the environment variable MAX_JOBS=N)
[1/3] /usr/bin/nvcc --generate-dependencies-with-compile --dependency-output cuda.cuda.o.d -DTORCH_EXTENSION_NAME=inline_ext -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/torch/csrc/api/include -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/TH -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/THC -isystem /hdd4/srinath2/.conda/envs/llm_env/include/python3.12 -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_86,code=compute_86 -gencode=arch=compute_86,code=sm_86 --compiler-options '-fPIC' -std=c++17 -c /hdd4/srinath2/.cache/torch_extensions/py312_cu121/inline_ext/cuda.cu -o cuda.cuda.o 
FAILED: cuda.cuda.o 
/usr/bin/nvcc --generate-dependencies-with-compile --dependency-output cuda.cuda.o.d -DTORCH_EXTENSION_NAME=inline_ext -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/torch/csrc/api/include -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/TH -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/THC -isystem /hdd4/srinath2/.conda/envs/llm_env/include/python3.12 -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_86,code=compute_86 -gencode=arch=compute_86,code=sm_86 --compiler-options '-fPIC' -std=c++17 -c /hdd4/srinath2/.cache/torch_extensions/py312_cu121/inline_ext/cuda.cu -o cuda.cuda.o 
cc1plus: fatal error: cuda_runtime.h: No such file or directory
compilation terminated.
[2/3] c++ -MMD -MF main.o.d -DTORCH_EXTENSION_NAME=inline_ext -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/torch/csrc/api/include -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/TH -isystem /hdd4/srinath2/.conda/envs/llm_env/lib/python3.12/site-packages/torch/include/THC -isystem /hdd4/srinath2/.conda/envs/llm_env/include/python3.12 -D_GLIBCXX_USE_CXX11_ABI=0 -fPIC -std=c++17 -c /hdd4/srinath2/.cache/torch_extensions/py312_cu121/inline_ext/main.cpp -o main.o 
ninja: build stopped: subcommand failed.
Output exceeds the [size limit](command:workbench.action.openSettings?[). Open the full output data [in a text editor](command:workbench.action.openLargeOutput?a2bafd1a-0c2d-45d8-a6c5-9afaf39345f4)
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
File ~/.conda/envs/llm_env/lib/python3.12/site-packages/torch/utils/cpp_extension.py:2096, in _run_ninja_build(build_directory, verbose, error_prefix)
   2095     stdout_fileno = 1
-> 2096     subprocess.run(
   2097         command,
   2098         stdout=stdout_fileno if verbose else subprocess.PIPE,
   2099         stderr=subprocess.STDOUT,
   2100         cwd=build_directory,
   2101         check=True,
   2102         env=env)
   2103 except subprocess.CalledProcessError as e:
   2104     # Python 2 and 3 compatible way of getting the error object.

File ~/.conda/envs/llm_env/lib/python3.12/subprocess.py:571, in run(input, capture_output, timeout, check, *popenargs, **kwargs)
    570     if check and retcode:
--> 571         raise CalledProcessError(retcode, process.args,
    572                                  output=stdout, stderr=stderr)
    573 return CompletedProcess(process.args, retcode, stdout, stderr)

CalledProcessError: Command '['ninja', '-v']' returned non-zero exit status 1.

The above exception was the direct cause of the following exception:

RuntimeError                              Traceback (most recent call last)
...
   2110 if hasattr(error, 'output') and error.output:  # type: ignore[union-attr]
   2111     message += f": {error.output.decode(*SUBPROCESS_DECODE_ARGS)}"  # type: ignore[union-attr]
-> 2112 raise RuntimeError(message) from e

RuntimeError: Error building extension 'inline_ext'
```

Please let me know how to debug/proceed further.

Thanks a ton for this resource :)

## 评论 (10)

### andreaskoepf · 2024-02-17

> fatal error: cuda_runtime.h: No such file or directory

The problem is that `cuda_runtime.h` wasn't found. Do you have the cuda toolkit installed? On ubuntu machines this header normally can be found at  `/usr/local/cuda/include/cuda_runtime.h` (the `/usr/local/cuda` normally is a symlink managed by `update-alternatives`).

### NamburiSrinath · 2024-02-25

Hi @andreaskoepf,

Sorry for the delay in response.  

I can indeed see the file `/usr/local/cuda/include/cuda_runtime.h` (attached screenshot)

<img width="636" alt="Screen Shot 2024-02-24 at 10 34 49 PM" src="https://github.com/cuda-mode/lectures/assets/40389487/d8da1d65-133c-41b3-ab00-3994754d7042">

Please let me know if you would need additional details to debug!

### CoffeeVampir3 · 2024-04-01

I'm having a similar issue in the same place,
```
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
File [~/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py:2096](http://localhost:8888/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py#line=2095), in _run_ninja_build(build_directory, verbose, error_prefix)
   2095     stdout_fileno = 1
-> 2096     subprocess.run(
   2097         command,
   2098         stdout=stdout_fileno if verbose else subprocess.PIPE,
   2099         stderr=subprocess.STDOUT,
   2100         cwd=build_directory,
   2101         check=True,
   2102         env=env)
   2103 except subprocess.CalledProcessError as e:
   2104     # Python 2 and 3 compatible way of getting the error object.

File [~/miniforge3/lib/python3.10/subprocess.py:526](http://localhost:8888/home/blackroot/miniforge3/lib/python3.10/subprocess.py#line=525), in run(input, capture_output, timeout, check, *popenargs, **kwargs)
    525     if check and retcode:
--> 526         raise CalledProcessError(retcode, process.args,
    527                                  output=stdout, stderr=stderr)
    528 return CompletedProcess(process.args, retcode, stdout, stderr)

CalledProcessError: Command '['ninja', '-v']' returned non-zero exit status 1.

The above exception was the direct cause of the following exception:

RuntimeError                              Traceback (most recent call last)
Cell In[8], line 1
----> 1 module = load_cuda(cuda_src, cpp_src, ['rgb_to_grayscale'], verbose=True)

Cell In[4], line 2, in load_cuda(cuda_src, cpp_src, funcs, opt, verbose)
      1 def load_cuda(cuda_src, cpp_src, funcs, opt=False, verbose=False):
----> 2     return load_inline(cuda_sources=[cuda_src], cpp_sources=[cpp_src], functions=funcs,
      3                        extra_cuda_cflags=["-O2"] if opt else [], verbose=verbose, name="inline_ext")

File [~/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py:1635](http://localhost:8888/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py#line=1634), in load_inline(name, cpp_sources, cuda_sources, functions, extra_cflags, extra_cuda_cflags, extra_ldflags, extra_include_paths, build_directory, verbose, with_cuda, is_python_module, with_pytorch_error_handling, keep_intermediates, use_pch)
   1631     _maybe_write(cuda_source_path, "\n".join(cuda_sources))
   1633     sources.append(cuda_source_path)
-> 1635 return _jit_compile(
   1636     name,
   1637     sources,
   1638     extra_cflags,
   1639     extra_cuda_cflags,
   1640     extra_ldflags,
   1641     extra_include_paths,
   1642     build_directory,
   1643     verbose,
   1644     with_cuda,
   1645     is_python_module,
   1646     is_standalone=False,
   1647     keep_intermediates=keep_intermediates)

File [~/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py:1710](http://localhost:8888/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py#line=1709), in _jit_compile(name, sources, extra_cflags, extra_cuda_cflags, extra_ldflags, extra_include_paths, build_directory, verbose, with_cuda, is_python_module, is_standalone, keep_intermediates)
   1706                 hipified_sources.add(hipify_result[s_abs].hipified_path if s_abs in hipify_result else s_abs)
   1708             sources = list(hipified_sources)
-> 1710         _write_ninja_file_and_build_library(
   1711             name=name,
   1712             sources=sources,
   1713             extra_cflags=extra_cflags or [],
   1714             extra_cuda_cflags=extra_cuda_cflags or [],
   1715             extra_ldflags=extra_ldflags or [],
   1716             extra_include_paths=extra_include_paths or [],
   1717             build_directory=build_directory,
   1718             verbose=verbose,
   1719             with_cuda=with_cuda,
   1720             is_standalone=is_standalone)
   1721 finally:
   1722     baton.release()

File [~/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py:1823](http://localhost:8888/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py#line=1822), in _write_ninja_file_and_build_library(name, sources, extra_cflags, extra_cuda_cflags, extra_ldflags, extra_include_paths, build_directory, verbose, with_cuda, is_standalone)
   1821 if verbose:
   1822     print(f'Building extension module {name}...', file=sys.stderr)
-> 1823 _run_ninja_build(
   1824     build_directory,
   1825     verbose,
   1826     error_prefix=f"Error building extension '{name}'")

File [~/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py:2112](http://localhost:8888/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/utils/cpp_extension.py#line=2111), in _run_ninja_build(build_directory, verbose, error_prefix)
   2110 if hasattr(error, 'output') and error.output:  # type: ignore[union-attr]
   2111     message += f": {error.output.decode(*SUBPROCESS_DECODE_ARGS)}"  # type: ignore[union-attr]
-> 2112 raise RuntimeError(message) from e

RuntimeError: Error building extension 'inline_ext'
```

cuda_runtime.h is found but it just fails with no real indications, the most readable error looking like some sort of syntax issue but that doesn't make much sense.

```
/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/include/ATen/core/boxing/impl/boxing.h:41:104: error: expected primary-expression before ‘>’ token
   41 | struct has_ivalue_to<T, guts::void_t<decltype(std::declval<IValue>().to<T>())>>
      |                                                                                                        ^
/home/blackroot/miniforge3/lib/python3.10/site-packages/torch/include/ATen/core/boxing/impl/boxing.h:41:107: error: expected primary-expression before ‘)’ token
   41 | struct has_ivalue_to<T, guts::void_t<decltype(std::declval<IValue>().to<T>())>>
      |                                                                                                           ^
ninja: build stopped: subcommand failed.
```

Haven't been able to hunt down a fix if you've got any ideas. Cheers

### oclivegriffin · 2024-04-11

I had a similar issue, running this code cell at the start, and possibly restarting the instance, worked for me
```
!apt-get install ninja-build
!pip install wurlitzer
```

might also want to try this afterwards if the above doesn't work:
```
!pip uninstall -y torch torchvision
!pip install torch torchvision
```

### CoffeeVampir3 · 2024-04-17

I managed to get things working by compiling the latest pytorch+12.4 using magma124 from source, it appears the issue was related to the pytorch+cuda 12.1 binaries.

### dkaberna · 2024-07-29

> I managed to get things working by compiling the latest pytorch+12.4 using magma124 from source, it appears the issue was related to the pytorch+cuda 12.1 binaries.

Can you please tell me what versions of gcc, etc that you are using?  I'm getting same issue now. 

### CoffeeVampir3 · 2024-07-29

> > I managed to get things working by compiling the latest pytorch+12.4 using magma124 from source, it appears the issue was related to the pytorch+cuda 12.1 binaries.
> 
> Can you please tell me what versions of gcc, etc that you are using? I'm getting same issue now.

Sure thing, I'm on endeavour os (arch) so my GCC and drivers are rolling, currently:

```
➜  ~ gcc --version
gcc (GCC) 14.1.1 20240522
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
```
➜  ~ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Thu_Jun__6_02:18:23_PDT_2024
Cuda compilation tools, release 12.5, V12.5.82
Build cuda_12.5.r12.5/compiler.34385749_0
```

Changing the system to use pyenv is another recommendation I can make, as I had trouble getting the binary versions of torch to figure out how to use the torch extension compiler, but pyenv fixed that issue for me. (Was previously using miniforge)

Finally if using conda the magma from <https://anaconda.org/pytorch/magma-cuda124> and installing torch from source (Am currently running 2.3.1) had me on a working environment. Using pyenv I found this not to be necessary. Hope it helps.


### dkaberna · 2024-07-29

> > > I managed to get things working by compiling the latest pytorch+12.4 using magma124 from source, it appears the issue was related to the pytorch+cuda 12.1 binaries.
> > 
> > 
> > Can you please tell me what versions of gcc, etc that you are using? I'm getting same issue now.
> 
> Sure thing, I'm on endeavour os (arch) so my GCC and drivers are rolling, currently:
> 
> ```
> ➜  ~ gcc --version
> gcc (GCC) 14.1.1 20240522
> Copyright (C) 2024 Free Software Foundation, Inc.
> This is free software; see the source for copying conditions.  There is NO
> warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
> ```
> 
> ```
> ➜  ~ nvcc --version
> nvcc: NVIDIA (R) Cuda compiler driver
> Copyright (c) 2005-2024 NVIDIA Corporation
> Built on Thu_Jun__6_02:18:23_PDT_2024
> Cuda compilation tools, release 12.5, V12.5.82
> Build cuda_12.5.r12.5/compiler.34385749_0
> ```
> 
> Changing the system to use pyenv is another recommendation I can make, as I had trouble getting the binary versions of torch to figure out how to use the torch extension compiler, but pyenv fixed that issue for me. (Was previously using miniforge)
> 
> Finally if using conda the magma from https://anaconda.org/pytorch/magma-cuda124 and installing torch from source (Am currently running 2.3.1) had me on a working environment. Using pyenv I found this not to be necessary. Hope it helps.

Thank you - this is such a pain...wish it was as easy as what Jeremy wrote on his twitter. :(

### dkaberna · 2024-07-29

> > > > I managed to get things working by compiling the latest pytorch+12.4 using magma124 from source, it appears the issue was related to the pytorch+cuda 12.1 binaries.
> > > 
> > > 
> > > Can you please tell me what versions of gcc, etc that you are using? I'm getting same issue now.
> > 
> > 
> > Sure thing, I'm on endeavour os (arch) so my GCC and drivers are rolling, currently:
> > ```
> > ➜  ~ gcc --version
> > gcc (GCC) 14.1.1 20240522
> > Copyright (C) 2024 Free Software Foundation, Inc.
> > This is free software; see the source for copying conditions.  There is NO
> > warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > ```
> > ➜  ~ nvcc --version
> > nvcc: NVIDIA (R) Cuda compiler driver
> > Copyright (c) 2005-2024 NVIDIA Corporation
> > Built on Thu_Jun__6_02:18:23_PDT_2024
> > Cuda compilation tools, release 12.5, V12.5.82
> > Build cuda_12.5.r12.5/compiler.34385749_0
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > Changing the system to use pyenv is another recommendation I can make, as I had trouble getting the binary versions of torch to figure out how to use the torch extension compiler, but pyenv fixed that issue for me. (Was previously using miniforge)
> > Finally if using conda the magma from https://anaconda.org/pytorch/magma-cuda124 and installing torch from source (Am currently running 2.3.1) had me on a working environment. Using pyenv I found this not to be necessary. Hope it helps.
> 
> Thank you - this is such a pain...wish it was as easy as what Jeremy wrote on his twitter. :(

Sorry, couple more questions.  What nvidia-driver and cuda-toolkit version are you using?  Did you install everything within pyenv, or were there certain things you installed outside of pyenv and within the host system?

### CoffeeVampir3 · 2024-07-29

> > > > > I managed to get things working by compiling the latest pytorch+12.4 using magma124 from source, it appears the issue was related to the pytorch+cuda 12.1 binaries.
> > > > 
> > > > 
> > > > Can you please tell me what versions of gcc, etc that you are using? I'm getting same issue now.
> > > 
> > > 
> > > Sure thing, I'm on endeavour os (arch) so my GCC and drivers are rolling, currently:
> > > ```
> > > ➜  ~ gcc --version
> > > gcc (GCC) 14.1.1 20240522
> > > Copyright (C) 2024 Free Software Foundation, Inc.
> > > This is free software; see the source for copying conditions.  There is NO
> > > warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
> > > ```
> > > 
> > > 
> > >     
> > >       
> > >     
> > > 
> > >       
> > >     
> > > 
> > >     
> > >   
> > > ```
> > > ➜  ~ nvcc --version
> > > nvcc: NVIDIA (R) Cuda compiler driver
> > > Copyright (c) 2005-2024 NVIDIA Corporation
> > > Built on Thu_Jun__6_02:18:23_PDT_2024
> > > Cuda compilation tools, release 12.5, V12.5.82
> > > Build cuda_12.5.r12.5/compiler.34385749_0
> > > ```
> > > 
> > > 
> > >     
> > >       
> > >     
> > > 
> > >       
> > >     
> > > 
> > >     
> > >   
> > > Changing the system to use pyenv is another recommendation I can make, as I had trouble getting the binary versions of torch to figure out how to use the torch extension compiler, but pyenv fixed that issue for me. (Was previously using miniforge)
> > > Finally if using conda the magma from https://anaconda.org/pytorch/magma-cuda124 and installing torch from source (Am currently running 2.3.1) had me on a working environment. Using pyenv I found this not to be necessary. Hope it helps.
> > 
> > 
> > Thank you - this is such a pain...wish it was as easy as what Jeremy wrote on his twitter. :(
> 
> Sorry, couple more questions. What nvidia-driver and cuda-toolkit version are you using? Did you install everything within pyenv, or were there certain things you installed outside of pyenv and within the host system?

If you're on arch, I'd recommend <https://archlinux.org/packages/extra/x86_64/magma-cuda/> which installs to the system. There's also <https://archlinux.org/packages/extra/x86_64/python-pytorch-cuda/> which I don't use, but you can take a look at what is installed from the package list.

I'm using the drivers:
Driver Version: 555.58.02      CUDA Version: 12.5 

I installed torch using pyenv on 3.12.4
`pyenv global 3.12.4`

