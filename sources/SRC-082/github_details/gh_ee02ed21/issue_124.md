# [Issue #124] can not install awq CUDA kernels

source: https://github.com/mit-han-lab/llm-awq/issues/124
state: open | updated: 2025-07-18T08:52:29Z
labels: 

## 正文

I‘m trying to follow [this](https://github.com/mit-han-lab/llm-awq#install) to install awq.
But failed at step 3.

## My Env
```
OS: Windows 11
GPU: NVIDIA GeForce RTX4060
Driver Version: 536.40 
CUDA: 11.8
Python: 3.10.13
```

## Output:
```
(LangChain-chat) PS C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels> python .\setup.py install
running install
C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!
  self.initialize_options()
C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\cmd.py:66: EasyInstallDeprecationWarning: easy_install command is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` and ``easy_install``.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://github.com/pypa/setuptools/issues/917 for details.
        ********************************************************************************

!!
  self.initialize_options()
running bdist_egg
running egg_info
writing awq_inference_engine.egg-info\PKG-INFO
writing dependency_links to awq_inference_engine.egg-info\dependency_links.txt
writing requirements to awq_inference_engine.egg-info\requires.txt
writing top-level names to awq_inference_engine.egg-info\top_level.txt
reading manifest file 'awq_inference_engine.egg-info\SOURCES.txt'
writing manifest file 'awq_inference_engine.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_ext
C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\utils\cpp_extension.py:383: UserWarning: Error checking compiler version for cl: [WinError 2] 系统找不到指定的文件。
  warnings.warn(f'Error checking compiler version for {compiler}: {error}')
building 'awq_inference_engine' extension
Emitting ninja build file C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-310\Release\build.ninja...
Compiling objects...
Allowing ninja to set a default number of workers... (overridable by setting the environment variable MAX_JOBS=N)
[1/2] C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\nvcc --generate-dependencies-with-compile --dependency-output C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpy
thon-310\Release\csrc/quantization/gemm_cuda_gen.obj.d -std=c++17 --use-local-env -Xcompiler /MD -Xcompiler /wd4819 -Xcompiler /wd4251 -Xcompiler /wd4244 -Xcompiler /wd4267 -Xcompiler /wd4275 -Xcompiler /wd4018 -Xcompiler /wd4190 -X
compiler /wd4624 -Xcompiler /wd4067 -Xcompiler /wd4068 -Xcompiler /EHsc -Xcudafe --diag_suppress=base_class_has_different_dll_interface -Xcudafe --diag_suppress=field_without_dll_interface -Xcudafe --diag_suppress=dll_interface_conf
lict_none_assumed -Xcudafe --diag_suppress=dll_interface_conflict_dllexport_assumed -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\incl
ude\torch\csrc\api\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\TH -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\THC "-IC:\Program Files\NVIDIA GPU Computing Toolk
it\CUDA\v11.8\include" -IC:\Users\ashto\.conda\envs\LangChain-chat\include -IC:\Users\ashto\.conda\envs\LangChain-chat\Include "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\include" "-ID:\Progr
am Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\ATLMFC\include" "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-ID:\Windows Kits\10\include\10.0.22000.0\ucrt" "-ID:\Win
dows Kits\10\\include\10.0.22000.0\\um" "-ID:\Windows Kits\10\\include\10.0.22000.0\\shared" "-ID:\Windows Kits\10\\include\10.0.22000.0\\winrt" "-ID:\Windows Kits\10\\include\10.0.22000.0\\cppwinrt" -c C:\Users\ashto\PycharmProject
s\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu -o C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-310\Release\csrc/quantization/gemm_c
uda_gen.obj -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_
HALF_CONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_89,code=compute_89 -gencode=arch=compute_89,code=sm_89
FAILED: C:/Users/ashto/PycharmProjects/LangChain-chat/repositories/llm-awq/awq/kernels/build/temp.win-amd64-cpython-310/Release/csrc/quantization/gemm_cuda_gen.obj
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\nvcc --generate-dependencies-with-compile --dependency-output C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-3
10\Release\csrc/quantization/gemm_cuda_gen.obj.d -std=c++17 --use-local-env -Xcompiler /MD -Xcompiler /wd4819 -Xcompiler /wd4251 -Xcompiler /wd4244 -Xcompiler /wd4267 -Xcompiler /wd4275 -Xcompiler /wd4018 -Xcompiler /wd4190 -Xcompil
er /wd4624 -Xcompiler /wd4067 -Xcompiler /wd4068 -Xcompiler /EHsc -Xcudafe --diag_suppress=base_class_has_different_dll_interface -Xcudafe --diag_suppress=field_without_dll_interface -Xcudafe --diag_suppress=dll_interface_conflict_n
one_assumed -Xcudafe --diag_suppress=dll_interface_conflict_dllexport_assumed -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\to
rch\csrc\api\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\TH -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\THC "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUD
A\v11.8\include" -IC:\Users\ashto\.conda\envs\LangChain-chat\include -IC:\Users\ashto\.conda\envs\LangChain-chat\Include "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\include" "-ID:\Program Fil
es\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\ATLMFC\include" "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-ID:\Windows Kits\10\include\10.0.22000.0\ucrt" "-ID:\Windows K
its\10\\include\10.0.22000.0\\um" "-ID:\Windows Kits\10\\include\10.0.22000.0\\shared" "-ID:\Windows Kits\10\\include\10.0.22000.0\\winrt" "-ID:\Windows Kits\10\\include\10.0.22000.0\\cppwinrt" -c C:\Users\ashto\PycharmProjects\Lang
Chain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu -o C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-310\Release\csrc/quantization/gemm_cuda_ge
n.obj -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_C
ONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_89,code=compute_89 -gencode=arch=compute_89,code=sm_89
gemm_cuda_gen.cu
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_OPERATORS__”(用“/U__CUDA_NO_HALF_OPERATORS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_CONVERSIONS__”(用“/U__CUDA_NO_HALF_CONVERSIONS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_BFLOAT16_CONVERSIONS__”(用“/U__CUDA_NO_BFLOAT16_CONVERSIONS__”)
gemm_cuda_gen.cu
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_OPERATORS__”(用“/U__CUDA_NO_HALF_OPERATORS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_CONVERSIONS__”(用“/U__CUDA_NO_HALF_CONVERSIONS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_BFLOAT16_CONVERSIONS__”(用“/U__CUDA_NO_BFLOAT16_CONVERSIONS__”)
gemm_cuda_gen.cu
C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(170): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(172): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(175): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(175): error: "__volatile__" has already been declared in the current scope
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(178): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(169): warning #177-D: variable "addr" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(187): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(189): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(192): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(192): error: "__volatile__" has already been declared in the current scope
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(195): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(186): warning #177-D: variable "addr" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(205): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(208): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(213): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(216): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(34): warning #177-D: variable "ZERO" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(44): warning #177-D: variable "blockIdx_x" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(48): warning #177-D: variable "A_shared_warp" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(49): warning #177-D: variable "B_shared_warp" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(65): warning #177-D: variable "ld_zero_flag" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=128]"
(284): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(170): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(172): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(175): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(175): error: "__volatile__" has already been declared in the current scope
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(178): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(169): warning #177-D: variable "addr" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(187): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(189): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(192): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(192): error: "__volatile__" has already been declared in the current scope
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(195): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(186): warning #177-D: variable "addr" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(205): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(208): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(213): error: identifier "__asm__" is undefined
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(216): error: expected a ")"
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(34): warning #177-D: variable "ZERO" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(44): warning #177-D: variable "blockIdx_x" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(48): warning #177-D: variable "A_shared_warp" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(49): warning #177-D: variable "B_shared_warp" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(65): warning #177-D: variable "ld_zero_flag" was declared but never referenced
          detected during instantiation of "void gemm_forward_4bit_cuda_m128n64k32<G>(int, half *, int *, half *, int *, int, int, int, half *) [with G=64]"
(289): here

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\quantization\gemm_cuda_gen.cu(21): warning #177-D: function "__pack_half2" was declared but never referenced

28 errors detected in the compilation of "C:/Users/ashto/PycharmProjects/LangChain-chat/repositories/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu".
[2/2] C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\nvcc --generate-dependencies-with-compile --dependency-output C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpy
thon-310\Release\csrc/layernorm/layernorm.obj.d -std=c++17 --use-local-env -Xcompiler /MD -Xcompiler /wd4819 -Xcompiler /wd4251 -Xcompiler /wd4244 -Xcompiler /wd4267 -Xcompiler /wd4275 -Xcompiler /wd4018 -Xcompiler /wd4190 -Xcompile
r /wd4624 -Xcompiler /wd4067 -Xcompiler /wd4068 -Xcompiler /EHsc -Xcudafe --diag_suppress=base_class_has_different_dll_interface -Xcudafe --diag_suppress=field_without_dll_interface -Xcudafe --diag_suppress=dll_interface_conflict_no
ne_assumed -Xcudafe --diag_suppress=dll_interface_conflict_dllexport_assumed -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\tor
ch\csrc\api\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\TH -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\THC "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA
\v11.8\include" -IC:\Users\ashto\.conda\envs\LangChain-chat\include -IC:\Users\ashto\.conda\envs\LangChain-chat\Include "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\include" "-ID:\Program File
s\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\ATLMFC\include" "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-ID:\Windows Kits\10\include\10.0.22000.0\ucrt" "-ID:\Windows Ki
ts\10\\include\10.0.22000.0\\um" "-ID:\Windows Kits\10\\include\10.0.22000.0\\shared" "-ID:\Windows Kits\10\\include\10.0.22000.0\\winrt" "-ID:\Windows Kits\10\\include\10.0.22000.0\\cppwinrt" -c C:\Users\ashto\PycharmProjects\LangC
hain-chat\repositories\llm-awq\awq\kernels\csrc\layernorm\layernorm.cu -o C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-310\Release\csrc/layernorm/layernorm.obj -D__CUDA_
NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U
__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_89,code=compute_89 -gencode=arch=compute_89,code=sm_89
FAILED: C:/Users/ashto/PycharmProjects/LangChain-chat/repositories/llm-awq/awq/kernels/build/temp.win-amd64-cpython-310/Release/csrc/layernorm/layernorm.obj
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin\nvcc --generate-dependencies-with-compile --dependency-output C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-3
10\Release\csrc/layernorm/layernorm.obj.d -std=c++17 --use-local-env -Xcompiler /MD -Xcompiler /wd4819 -Xcompiler /wd4251 -Xcompiler /wd4244 -Xcompiler /wd4267 -Xcompiler /wd4275 -Xcompiler /wd4018 -Xcompiler /wd4190 -Xcompiler /wd4
624 -Xcompiler /wd4067 -Xcompiler /wd4068 -Xcompiler /EHsc -Xcudafe --diag_suppress=base_class_has_different_dll_interface -Xcudafe --diag_suppress=field_without_dll_interface -Xcudafe --diag_suppress=dll_interface_conflict_none_ass
umed -Xcudafe --diag_suppress=dll_interface_conflict_dllexport_assumed -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\torch\csr
c\api\include -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\TH -IC:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\include\THC "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8
\include" -IC:\Users\ashto\.conda\envs\LangChain-chat\include -IC:\Users\ashto\.conda\envs\LangChain-chat\Include "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\include" "-ID:\Program Files\Micr
osoft Visual Studio\2022\Community\VC\Tools\MSVC\14.35.32215\ATLMFC\include" "-ID:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-ID:\Windows Kits\10\include\10.0.22000.0\ucrt" "-ID:\Windows Kits\10\
\include\10.0.22000.0\\um" "-ID:\Windows Kits\10\\include\10.0.22000.0\\shared" "-ID:\Windows Kits\10\\include\10.0.22000.0\\winrt" "-ID:\Windows Kits\10\\include\10.0.22000.0\\cppwinrt" -c C:\Users\ashto\PycharmProjects\LangChain-c
hat\repositories\llm-awq\awq\kernels\csrc\layernorm\layernorm.cu -o C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\build\temp.win-amd64-cpython-310\Release\csrc/layernorm/layernorm.obj -D__CUDA_NO_HAL
F_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA
_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_89,code=compute_89 -gencode=arch=compute_89,code=sm_89
layernorm.cu
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_OPERATORS__”(用“/U__CUDA_NO_HALF_OPERATORS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_CONVERSIONS__”(用“/U__CUDA_NO_HALF_CONVERSIONS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_BFLOAT16_CONVERSIONS__”(用“/U__CUDA_NO_BFLOAT16_CONVERSIONS__”)
layernorm.cu
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include\cuda\std\detail\libcxx\include\support\atomic\atomic_msvc.h(15): warning C4005: “_Compiler_barrier”: 宏重定义
D:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/include\xatomic.h(55): note: 参见“_Compiler_barrier”的前一个定义
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_OPERATORS__”(用“/U__CUDA_NO_HALF_OPERATORS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_HALF_CONVERSIONS__”(用“/U__CUDA_NO_HALF_CONVERSIONS__”)
cl: 命令行 warning D9025 :正在重写“/D__CUDA_NO_BFLOAT16_CONVERSIONS__”(用“/U__CUDA_NO_BFLOAT16_CONVERSIONS__”)
layernorm.cu
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include\cuda\std\detail\libcxx\include\support\atomic\atomic_msvc.h(15): warning C4005: “_Compiler_barrier”: 宏重定义
D:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/include\xatomic.h(55): note: 参见“_Compiler_barrier”的前一个定义
C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\layernorm\reduction.cuh(81): error: identifier "HALF_FLT_MAX" is undefined in device code

C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\csrc\layernorm\reduction.cuh(81): error: identifier "HALF_FLT_MAX" is undefined in device code

2 errors detected in the compilation of "C:/Users/ashto/PycharmProjects/LangChain-chat/repositories/llm-awq/awq/kernels/csrc/layernorm/layernorm.cu".
ninja: build stopped: subcommand failed.
Traceback (most recent call last):
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\utils\cpp_extension.py", line 2100, in _run_ninja_build
    subprocess.run(
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['ninja', '-v']' returned non-zero exit status 1.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\ashto\PycharmProjects\LangChain-chat\repositories\llm-awq\awq\kernels\setup.py", line 31, in <module>
    setup(
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\__init__.py", line 107, in setup
    return distutils.core.setup(**attrs)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\core.py", line 185, in setup
    return run_commands(dist)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\core.py", line 201, in run_commands
    dist.run_commands()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\dist.py", line 969, in run_commands
    self.run_command(cmd)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\dist.py", line 1234, in run_command
    super().run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\install.py", line 80, in run
    self.do_egg_install()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\install.py", line 129, in do_egg_install
    self.run_command('bdist_egg')
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\dist.py", line 1234, in run_command
    super().run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\bdist_egg.py", line 164, in run
    cmd = self.call_command('install_lib', warn_dir=0)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\bdist_egg.py", line 150, in call_command
    self.run_command(cmdname)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\dist.py", line 1234, in run_command
    super().run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\install_lib.py", line 11, in run
    self.build()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\command\install_lib.py", line 111, in build
    self.run_command('build_ext')
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\dist.py", line 1234, in run_command
    super().run_command(command)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\build_ext.py", line 84, in run
    _build_ext.run(self)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\command\build_ext.py", line 345, in run
    self.build_extensions()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\utils\cpp_extension.py", line 873, in build_extensions
    build_ext.build_extensions(self)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\command\build_ext.py", line 467, in build_extensions
    self._build_extensions_serial()
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\command\build_ext.py", line 493, in _build_extensions_serial
    self.build_extension(ext)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\command\build_ext.py", line 246, in build_extension
    _build_ext.build_extension(self, ext)
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\setuptools\_distutils\command\build_ext.py", line 548, in build_extension
    objects = self.compiler.compile(
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\utils\cpp_extension.py", line 845, in win_wrap_ninja_compile
    _write_ninja_file_and_compile_objects(
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\utils\cpp_extension.py", line 1774, in _write_ninja_file_and_compile_objects
    _run_ninja_build(
  File "C:\Users\ashto\.conda\envs\LangChain-chat\lib\site-packages\torch\utils\cpp_extension.py", line 2116, in _run_ninja_build
    raise RuntimeError(message) from e
RuntimeError: Error compiling objects for extension
```

## 评论 (9)

### kzleong · 2024-05-12

Hi, I'm facing this issue as well on Windows (no issues on Linux), do you happen to remember the fix?

### Millie-Xu · 2024-05-22

I'm also facing this issue as well on Windows, can anyone help me？

### ktotam1 · 2024-06-09

I'm also facing this issue on Windows 11, CUDA 12.1 torch 2.3.1

### jqXiong · 2024-06-25

我也遇到这个问题了，有没有解决方案

### harleyszhang · 2024-11-03

试试减小 MAX_JOBS=2，改为这样编译，我自己是 6gb 显存卡上编译成功了。
MAX_JOBS=2 python setup.py install

### Gokulakrishnan-DL-CV · 2024-11-21

@harleyszhang can you explain what you meant to propose as the fix?


### Gokulakrishnan-DL-CV · 2024-11-21

@kzleong When you say, you didn't face any issues with linux, what gpu was that laptop using?


### Gokulakrishnan-DL-CV · 2024-11-21

@Millie-Xu @ktotam1 Have you guys been able to fix this errror?


### zztong814 · 2025-07-18

> 我也遇到这个问题了，有没有解决方案

请问解决了吗
