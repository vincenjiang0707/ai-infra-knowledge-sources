# [Issue #81] NVCC Compilation Issue with PyTorch Extension on Torch 2.0.1 + cu117 and CUDA 11.8.0

source: https://github.com/mit-han-lab/llm-awq/issues/81
state: open | updated: 2024-10-05T21:41:33Z
labels: 

## 正文

I've encountered an error compiling a PyTorch extension using **`nvcc`**. Specifically, I'm on PyTorch **`2.0.1+cu117`** and CUDA **`11.8.0`**, and I've tried this on both **`A100`** and **`A40`** cards. The problem arises when I run **`python setup.py install`**.

The error I'm seeing is:
![1721692900415_ pic](https://github.com/mit-han-lab/llm-awq/assets/95149564/f55382e9-725e-4a77-8dd3-3502300112e5)
```
nvcc error   : 'cicc' died due to signal 9 (Kill signal)
error: command '/spack/2206/apps/linux-centos7-x86_64_v3/gcc-11.3.0/cuda-11.5.1-wyisbl5/bin/nvcc' failed with exit code 9
```

Additionally, there are warnings about a pointless comparison of unsigned integers with zero.

My troubleshooting so far:

1. Checked memory usage; I have 120G available, which should be more than enough.
2. Double-checked CUDA version **`11.8.0`** compatibility with our PyTorch build.

Despite these efforts, the issue persists. I'd appreciate any insights or advice you might have on this.

Thanks for your time and assistance!

## 评论 (4)

### belericant · 2023-08-30

Hey, I couldn't sucessfully reproduce your error on `A100` card with `Torch 2.0.1+cu117` and `CUDA 11.8.0` in a fresh venv. The differences I can see is that I am running `Python 3.10.12` on `Ubuntu 22.04.3 LTS`.

Output of `pip freeze`:
```
absl-py==1.4.0
accelerate==0.22.0
aiohttp==3.8.5
aiosignal==1.3.1
async-timeout==4.0.3
attributedict==0.3.0
attrs==23.1.0
-e git+https://github.com/mit-han-lab/llm-awq.git@2c775256f9a99eaeaf2d5bc312dbc5f714868f28#egg=awq
awq-inference-engine==0.0.0
blessings==1.7
cachetools==5.3.1
certifi==2023.7.22
chardet==5.2.0
charset-normalizer==3.2.0
click==8.1.7
cmake==3.27.2
codecov==2.1.13
colorama==0.4.6
coloredlogs==15.0.1
colour-runner==0.1.1
coverage==7.3.0
DataProperty==1.0.1
datasets==2.14.4
deepdiff==6.3.1
dill==0.3.7
distlib==0.3.7
filelock==3.12.3
frozenlist==1.4.0
fsspec==2023.6.0
huggingface-hub==0.16.4
humanfriendly==10.0
idna==3.4
inspecta==0.1.3
Jinja2==3.1.2
joblib==1.3.2
jsonlines==3.1.0
lit==16.0.6
lm-eval==0.3.0
MarkupSafe==2.1.3
mbstrdecoder==1.1.3
mpmath==1.3.0
multidict==6.0.4
multiprocess==0.70.15
networkx==3.1
nltk==3.8.1
numexpr==2.8.5
numpy==1.25.2
nvidia-cublas-cu11==11.10.3.66
nvidia-cuda-cupti-cu11==11.7.101
nvidia-cuda-nvrtc-cu11==11.7.99
nvidia-cuda-runtime-cu11==11.7.99
nvidia-cudnn-cu11==8.5.0.96
nvidia-cufft-cu11==10.9.0.58
nvidia-curand-cu11==10.2.10.91
nvidia-cusolver-cu11==11.4.0.1
nvidia-cusparse-cu11==11.7.4.91
nvidia-nccl-cu11==2.14.3
nvidia-nvtx-cu11==11.7.91
openai==0.27.10
ordered-set==4.1.0
packaging==23.1
pandas==2.0.3
pathvalidate==3.1.0
Pillow==10.0.0
platformdirs==3.10.0
pluggy==1.3.0
portalocker==2.7.0
protobuf==4.24.2
psutil==5.9.5
pyarrow==13.0.0
pybind11==2.11.1
pycountry==22.3.5
Pygments==2.16.1
pyproject-api==1.6.1
pytablewriter==1.0.0
python-dateutil==2.8.2
pytz==2023.3
PyYAML==6.0.1
regex==2023.8.8
requests==2.31.0
rootpath==0.1.1
rouge-score==0.1.2
sacrebleu==1.5.0
safetensors==0.3.3
scikit-learn==1.3.0
scipy==1.11.2
sentencepiece==0.1.99
six==1.16.0
sqlitedict==2.1.0
sympy==1.12
tabledata==1.3.1
tcolorpy==0.1.3
termcolor==2.3.0
texttable==1.6.7
threadpoolctl==3.2.0
tokenizers==0.13.3
toml==0.10.2
tomli==2.0.1
torch==2.0.1
torchvision==0.15.2
tox==4.11.0
tqdm==4.66.1
tqdm-multiprocess==0.0.11
transformers==4.32.1
triton==2.0.0
typepy==1.3.1
typing_extensions==4.7.1
tzdata==2023.3
urllib3==2.0.4
virtualenv==20.24.3
xxhash==3.3.0
yarl==1.9.2
zstandard==0.21.0
```

Here was my output of `setup,py install`:
```
running install
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/setuptools/command/easy_install.py:158: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
running bdist_egg
running egg_info
creating awq_inference_engine.egg-info
writing awq_inference_engine.egg-info/PKG-INFO
writing dependency_links to awq_inference_engine.egg-info/dependency_links.txt
writing requirements to awq_inference_engine.egg-info/requires.txt
writing top-level names to awq_inference_engine.egg-info/top_level.txt
writing manifest file 'awq_inference_engine.egg-info/SOURCES.txt'
reading manifest file 'awq_inference_engine.egg-info/SOURCES.txt'
writing manifest file 'awq_inference_engine.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_ext
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/utils/cpp_extension.py:388: UserWarning: The detected CUDA version (11.8) has a minor version mismatch with the version that was used to compile PyTorch (11.7). Most likely this shouldn't be a problem.
  warnings.warn(CUDA_MISMATCH_WARN.format(cuda_str_version, torch.version.cuda))
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/utils/cpp_extension.py:398: UserWarning: There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 11.8
  warnings.warn(f'There are no {compiler_name} version bounds defined for CUDA version {cuda_str_version}')
building 'awq_inference_engine' extension
creating /home/eric/llm-awq/awq/kernels/build
creating /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10
creating /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc
creating /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/layernorm
creating /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/position_embedding
creating /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/quantization
Emitting ninja build file /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/build.ninja...
Compiling objects...
Allowing ninja to set a default number of workers... (overridable by setting the environment variable MAX_JOBS=N)
[1/4] c++ -MMD -MF /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/pybind.o.d -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/TH -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/THC -I/home/eric/llm-awq/.venv/include -I/usr/include/python3.10 -c -c /home/eric/llm-awq/awq/kernels/csrc/pybind.cpp -o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/pybind.o -g -O3 -fopenmp -lgomp -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0
[2/4] /usr/bin/nvcc  -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/TH -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/THC -I/home/eric/llm-awq/.venv/include -I/usr/include/python3.10 -c -c /home/eric/llm-awq/awq/kernels/csrc/position_embedding/pos_encoding_kernels.cu -o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/position_embedding/pos_encoding_kernels.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_80,code=compute_80 -gencode=arch=compute_80,code=sm_80
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/core/TensorImpl.h(77): here

/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/ATen/core/qualified_name.h(73): here

[3/4] /usr/bin/nvcc  -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/TH -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/THC -I/home/eric/llm-awq/.venv/include -I/usr/include/python3.10 -c -c /home/eric/llm-awq/awq/kernels/csrc/layernorm/layernorm.cu -o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/layernorm/layernorm.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_80,code=compute_80 -gencode=arch=compute_80,code=sm_80
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/core/TensorImpl.h(77): here

/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/ATen/core/qualified_name.h(73): here

[4/4] /usr/bin/nvcc  -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/TH -I/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/THC -I/home/eric/llm-awq/.venv/include -I/usr/include/python3.10 -c -c /home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu -o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/quantization/gemm_cuda_gen.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_80,code=compute_80 -gencode=arch=compute_80,code=sm_80
/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(35): warning #177-D: variable "scaling_factors_shared" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(36): warning #177-D: variable "zeros_shared" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(39): warning #177-D: variable "blockIdx_x" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(53): warning #177-D: variable "ld_zero_flag" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(228): warning #177-D: variable "scaling_factors_shared" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(229): warning #177-D: variable "zeros_shared" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(233): warning #177-D: variable "blockIdx_x" was declared but never referenced

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(247): warning #177-D: variable "ld_zero_flag" was declared but never referenced

/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/core/TensorImpl.h(77): here

/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/include/ATen/core/qualified_name.h(73): here

/home/eric/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(22): warning #177-D: function "__pack_half2" was declared but never referenced

creating build/lib.linux-x86_64-3.10
x86_64-linux-gnu-g++ -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -g -fwrapv -O2 -Wl,-Bsymbolic-functions -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/layernorm/layernorm.o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/position_embedding/pos_encoding_kernels.o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/pybind.o /home/eric/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/quantization/gemm_cuda_gen.o -L/home/eric/llm-awq/.venv/lib/python3.10/site-packages/torch/lib -lc10 -ltorch -ltorch_cpu -ltorch_python -lcudart -lc10_cuda -ltorch_cuda -o build/lib.linux-x86_64-3.10/awq_inference_engine.cpython-310-x86_64-linux-gnu.so
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
copying build/lib.linux-x86_64-3.10/awq_inference_engine.cpython-310-x86_64-linux-gnu.so -> build/bdist.linux-x86_64/egg
creating stub loader for awq_inference_engine.cpython-310-x86_64-linux-gnu.so
byte-compiling build/bdist.linux-x86_64/egg/awq_inference_engine.py to awq_inference_engine.cpython-310.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying awq_inference_engine.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying awq_inference_engine.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying awq_inference_engine.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying awq_inference_engine.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying awq_inference_engine.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
writing build/bdist.linux-x86_64/egg/EGG-INFO/native_libs.txt
zip_safe flag not set; analyzing archive contents...
__pycache__.awq_inference_engine.cpython-310: module references __file__
creating dist
creating 'dist/awq_inference_engine-0.0.0-py3.10-linux-x86_64.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing awq_inference_engine-0.0.0-py3.10-linux-x86_64.egg
creating /home/eric/llm-awq/.venv/lib/python3.10/site-packages/awq_inference_engine-0.0.0-py3.10-linux-x86_64.egg
Extracting awq_inference_engine-0.0.0-py3.10-linux-x86_64.egg to /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Adding awq-inference-engine 0.0.0 to easy-install.pth file

Installed /home/eric/llm-awq/.venv/lib/python3.10/site-packages/awq_inference_engine-0.0.0-py3.10-linux-x86_64.egg
Processing dependencies for awq-inference-engine==0.0.0
Searching for torch==2.0.1
Best match: torch 2.0.1
Adding torch 2.0.1 to easy-install.pth file
Installing convert-caffe2-to-onnx script to /home/eric/llm-awq/.venv/bin
Installing convert-onnx-to-caffe2 script to /home/eric/llm-awq/.venv/bin
Installing torchrun script to /home/eric/llm-awq/.venv/bin

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for filelock==3.12.3
Best match: filelock 3.12.3
Adding filelock 3.12.3 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for networkx==3.1
Best match: networkx 3.1
Adding networkx 3.1 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for Jinja2==3.1.2
Best match: Jinja2 3.1.2
Adding Jinja2 3.1.2 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-nccl-cu11==2.14.3
Best match: nvidia-nccl-cu11 2.14.3
Adding nvidia-nccl-cu11 2.14.3 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-nvtx-cu11==11.7.91
Best match: nvidia-nvtx-cu11 11.7.91
Adding nvidia-nvtx-cu11 11.7.91 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cuda-cupti-cu11==11.7.101
Best match: nvidia-cuda-cupti-cu11 11.7.101
Adding nvidia-cuda-cupti-cu11 11.7.101 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cublas-cu11==11.10.3.66
Best match: nvidia-cublas-cu11 11.10.3.66
Adding nvidia-cublas-cu11 11.10.3.66 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for sympy==1.12
Best match: sympy 1.12
Adding sympy 1.12 to easy-install.pth file
Installing isympy script to /home/eric/llm-awq/.venv/bin

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cuda-nvrtc-cu11==11.7.99
Best match: nvidia-cuda-nvrtc-cu11 11.7.99
Adding nvidia-cuda-nvrtc-cu11 11.7.99 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cusolver-cu11==11.4.0.1
Best match: nvidia-cusolver-cu11 11.4.0.1
Adding nvidia-cusolver-cu11 11.4.0.1 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cufft-cu11==10.9.0.58
Best match: nvidia-cufft-cu11 10.9.0.58
Adding nvidia-cufft-cu11 10.9.0.58 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for triton==2.0.0
Best match: triton 2.0.0
Adding triton 2.0.0 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cuda-runtime-cu11==11.7.99
Best match: nvidia-cuda-runtime-cu11 11.7.99
Adding nvidia-cuda-runtime-cu11 11.7.99 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cusparse-cu11==11.7.4.91
Best match: nvidia-cusparse-cu11 11.7.4.91
Adding nvidia-cusparse-cu11 11.7.4.91 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-cudnn-cu11==8.5.0.96
Best match: nvidia-cudnn-cu11 8.5.0.96
Adding nvidia-cudnn-cu11 8.5.0.96 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for typing-extensions==4.7.1
Best match: typing-extensions 4.7.1
Adding typing-extensions 4.7.1 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for nvidia-curand-cu11==10.2.10.91
Best match: nvidia-curand-cu11 10.2.10.91
Adding nvidia-curand-cu11 10.2.10.91 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for MarkupSafe==2.1.3
Best match: MarkupSafe 2.1.3
Adding MarkupSafe 2.1.3 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for wheel==0.41.2
Best match: wheel 0.41.2
Adding wheel 0.41.2 to easy-install.pth file
Installing wheel script to /home/eric/llm-awq/.venv/bin

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for setuptools==59.6.0
Best match: setuptools 59.6.0
Adding setuptools 59.6.0 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for mpmath==1.3.0
Best match: mpmath 1.3.0
Adding mpmath 1.3.0 to easy-install.pth file

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for lit==16.0.6
Best match: lit 16.0.6
Adding lit 16.0.6 to easy-install.pth file
Installing lit script to /home/eric/llm-awq/.venv/bin

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Searching for cmake==3.27.2
Best match: cmake 3.27.2
Adding cmake 3.27.2 to easy-install.pth file
Installing cmake script to /home/eric/llm-awq/.venv/bin
Installing cpack script to /home/eric/llm-awq/.venv/bin
Installing ctest script to /home/eric/llm-awq/.venv/bin

Using /home/eric/llm-awq/.venv/lib/python3.10/site-packages
Finished processing dependencies for awq-inference-engine==0.0.0
```

### riaz · 2023-08-30

@belericant  What is the version of gcc and g++ in your environment?

I am getting the following error 

```
/usr/include/c++/11/bits/std_function.h:435:145: error: parameter packs not expanded with ‘...’:
  435 |         function(_Functor&& __f)
      |                                                                                                                                                 ^ 
/usr/include/c++/11/bits/std_function.h:435:145: note:         ‘_ArgTypes’
/usr/include/c++/11/bits/std_function.h:530:146: error: parameter packs not expanded with ‘...’:
  530 |         operator=(_Functor&& __f)
      |                                                                                                                                                  ^ 
/usr/include/c++/11/bits/std_function.h:530:146: note:         ‘_ArgTypes’
error: command '/usr/bin/nvcc' failed with exit code 1
```
Env: Ubuntu 22.04, nvcc - 11.5, cuda 12.0 , gcc  11 , g++ 11

### belericant · 2023-09-06

@riaz 
gcc/g++: `(Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0`
nvcc: `Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0`

From `nvidia-smi`:
```
NVIDIA-SMI 535.54.03    Driver Version: 535.54.03    CUDA Version: 12.2
```

### ShobhaRajanna · 2024-10-05

@riaz 
Error: Feature 'ldmatrix' requires target sm_75 or higher when building awq_inference_engine on Tesla V100
I am trying to build the `awq_inference_engine` on a system with Tesla V100 GPUs, but I'm encountering errors related to CUDA architecture compatibility. Specifically, the build fails with errors such as `Feature 'ldmatrix' requires .target sm_75 or higher` when compiling `gemm_cuda_gen.cu`.

Steps to reproduce:
1. Clone the repository.
2. Set up the environment (CUDA 11.7, Tesla V100 GPUs).
3. Run `python setup.py install`.
4. Compilation fails with the errors listed below.

ptxas /tmp/tmpxft_00022ba1_00000000-6_gemm_cuda_gen.ptx, line 596; error   : Feature 'ldmatrix' requires .target sm_75 or higher
ptxas /tmp/tmpxft_00022ba1_00000000-6_gemm_cuda_gen.ptx, line 604; error   : Modifier '.m8n8' requires .target sm_75 or higher

Environment:
- GPU: Tesla V100-SXM2
- CUDA Version: 11.7
- PyTorch Version: 2.x
- Operating System: Ubuntu 18.04

I tried modifying the `setup.py` to include the `-gencode arch=compute_70,code=sm_70` flags and conditionally compiling the CUDA code, but the issue persists. Is there a recommended way to disable features requiring sm_75 for older GPUs like the V100?







