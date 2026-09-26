# [Issue #44] Error in building SwiftTransformers with torch 2.2.4

source: https://github.com/LLMServe/DistServe/issues/44
state: open | updated: 2024-11-13T02:16:22Z
labels: 

## 正文

Hi,

I tried building SwiftTransformers in an environment setup using `pip install vllm`. 
I'm getting the following error.

```
[ 80%] Linking CXX static library libxformers_kernel.a
[ 80%] Built target xformers_kernel
[ 81%] Building CXX object src/csrc/layer/CMakeFiles/layer.dir/attention.cc.o
[ 81%] Building CXX object src/csrc/layer/CMakeFiles/layer.dir/ffn.cc.o
[ 82%] Building CXX object src/csrc/layer/CMakeFiles/layer.dir/gated_ffn.cc.o
[ 83%] Linking CXX static library liblayer.a
[ 83%] Built target layer
[ 84%] Building CXX object src/csrc/model/gpt/CMakeFiles/model_gpt.dir/gpt_weight.cc.o
[ 84%] Building CXX object src/csrc/model/gpt/CMakeFiles/model_gpt.dir/gpt.cc.o
[ 86%] Building CXX object src/csrc/model/gpt/CMakeFiles/model_gpt.dir/gptop_base.cc.o
[ 86%] Building CXX object src/unittest/layer/CMakeFiles/unittest_layer_para.dir/parallel_ffn.cc.o
[ 87%] Building CXX object src/unittest/layer/CMakeFiles/unittest_layer_para.dir/parallel_attention.cc.o
[ 88%] Linking CXX executable ../../../bin/unittest_layer_para
/usr/bin/ld: /root/anaconda3/envs/swiftllm/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so: undefined reference to `ncclCommRegister'
/usr/bin/ld: /root/anaconda3/envs/swiftllm/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so: undefined reference to `ncclCommDeregister'
collect2: error: ld returned 1 exit status
make[2]: *** [src/unittest/layer/CMakeFiles/unittest_layer_para.dir/build.make:150: bin/unittest_layer_para] Error 1
make[1]: *** [CMakeFiles/Makefile2:1161: src/unittest/layer/CMakeFiles/unittest_layer_para.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 89%] Linking CXX static library libmodel_gpt.a
[ 89%] Built target model_gpt
make: *** [Makefile:156: all] Error 2
```


Here is the output of `conda list`

```
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
accelerate                0.33.0                   pypi_0    pypi
aiohttp                   3.9.5                    pypi_0    pypi
aiohttp-cors              0.7.0                    pypi_0    pypi
aiosignal                 1.3.1                    pypi_0    pypi
annotated-types           0.6.0                    pypi_0    pypi
anyio                     4.3.0                    pypi_0    pypi
async-timeout             4.0.3                    pypi_0    pypi
attrs                     23.2.0                   pypi_0    pypi
audioread                 3.0.1                    pypi_0    pypi
blas                      1.0                         mkl  
bzip2                     1.0.8                h5eee18b_5  
ca-certificates           2024.7.4             hbcca054_0    conda-forge
cachetools                5.3.3                    pypi_0    pypi
cccl                      2.3.1                h6103f9b_0    conda-forge
certifi                   2024.7.4                 pypi_0    pypi
cffi                      1.17.0                   pypi_0    pypi
charset-normalizer        3.3.2                    pypi_0    pypi
click                     8.1.7                    pypi_0    pypi
cloudpickle               3.0.0                    pypi_0    pypi
colorful                  0.5.6                    pypi_0    pypi
contourpy                 1.2.1                    pypi_0    pypi
cuda-cccl                 12.4.127             ha770c72_1    conda-forge
cuda-cccl_linux-64        12.4.127             ha770c72_1    conda-forge
cuda-compiler             12.1.0                        0    nvidia
cuda-cudart               12.1.55                       0    nvidia
cuda-cudart-dev           12.1.55                       0    nvidia
cuda-cudart-static        12.1.55                       0    nvidia
cuda-cuobjdump            12.1.55                       0    nvidia
cuda-cupti                12.1.105                      0    nvidia
cuda-cupti-static         12.4.127             ha770c72_1    conda-forge
cuda-cuxxfilt             12.1.55                       0    nvidia
cuda-driver-dev           12.1.55                       0    nvidia
cuda-libraries            12.1.0                        0    nvidia
cuda-libraries-dev        12.1.0                        0    nvidia
cuda-libraries-static     12.1.0                        0    nvidia
cuda-minimal-build        12.1.0                        0    nvidia
cuda-nvcc                 12.1.66                       0    nvidia
cuda-nvprune              12.1.55                       0    nvidia
cuda-nvrtc                12.1.105                      0    nvidia
cuda-nvrtc-dev            12.1.55                       0    nvidia
cuda-nvrtc-static         12.1.55                       0    nvidia
cuda-nvtx                 12.1.105                      0    nvidia
cuda-opencl               12.4.127                      0    nvidia
cuda-opencl-dev           12.1.56                       0    nvidia
cuda-profiler-api         12.1.55                       0    nvidia
cuda-runtime              12.1.0                        0    nvidia
cuda-version              12.4                 h3060b56_3    conda-forge
cupy-cuda12x              13.3.0                   pypi_0    pypi
cycler                    0.12.1                   pypi_0    pypi
datasets                  2.21.0                   pypi_0    pypi
decorator                 5.1.1                    pypi_0    pypi
dill                      0.3.8                    pypi_0    pypi
diskcache                 5.6.3                    pypi_0    pypi
distlib                   0.3.8                    pypi_0    pypi
distro                    1.9.0                    pypi_0    pypi
distserve                 0.0.1                     dev_0    <develop>
exceptiongroup            1.2.0                    pypi_0    pypi
fastapi                   0.112.1                  pypi_0    pypi
fastrlock                 0.8.2                    pypi_0    pypi
filelock                  3.13.1          py310h06a4308_0  
fonttools                 4.53.1                   pypi_0    pypi
frozenlist                1.4.1                    pypi_0    pypi
fsspec                    2024.6.1                 pypi_0    pypi
gguf                      0.9.1                    pypi_0    pypi
gmp                       6.2.1                h295c915_3  
gmpy2                     2.1.2           py310heeb90bb_0  
google-api-core           2.18.0                   pypi_0    pypi
google-auth               2.29.0                   pypi_0    pypi
googleapis-common-protos  1.63.0                   pypi_0    pypi
grpcio                    1.62.1                   pypi_0    pypi
h11                       0.14.0                   pypi_0    pypi
httpcore                  1.0.5                    pypi_0    pypi
httptools                 0.6.1                    pypi_0    pypi
httpx                     0.27.0                   pypi_0    pypi
huggingface-hub           0.24.6                   pypi_0    pypi
idna                      3.7                      pypi_0    pypi
importlib-metadata        8.4.0                    pypi_0    pypi
iniconfig                 2.0.0                    pypi_0    pypi
intel-openmp              2023.1.0         hdb19cb5_46306  
interegular               0.3.3                    pypi_0    pypi
jinja2                    3.1.3           py310h06a4308_0  
jiter                     0.5.0                    pypi_0    pypi
joblib                    1.4.2                    pypi_0    pypi
jsonschema                4.21.1                   pypi_0    pypi
jsonschema-specifications 2023.12.1                pypi_0    pypi
kiwisolver                1.4.5                    pypi_0    pypi
lark                      1.2.2                    pypi_0    pypi
lazy-loader               0.4                      pypi_0    pypi
ld_impl_linux-64          2.38                 h1181459_1  
libcublas                 12.1.0.26                     0    nvidia
libcublas-dev             12.1.0.26                     0    nvidia
libcublas-static          12.1.0.26                     0    nvidia
libcufft                  11.0.2.4                      0    nvidia
libcufft-dev              11.0.2.4                      0    nvidia
libcufft-static           11.0.2.4                      0    nvidia
libcufile                 1.9.1.3                       0    nvidia
libcufile-dev             1.6.0.25                      0    nvidia
libcufile-static          1.6.0.25                      0    nvidia
libcurand                 10.3.5.147                    0    nvidia
libcurand-dev             10.3.2.56                     0    nvidia
libcurand-static          10.3.2.56                     0    nvidia
libcusolver               11.4.4.55                     0    nvidia
libcusolver-dev           11.4.4.55                     0    nvidia
libcusolver-static        11.4.4.55                     0    nvidia
libcusparse               12.0.2.55                     0    nvidia
libcusparse-dev           12.0.2.55                     0    nvidia
libcusparse-static        12.0.2.55                     0    nvidia
libffi                    3.4.4                h6a678d5_0  
libgcc-ng                 11.2.0               h1234567_1  
libgfortran-ng            13.2.0               h69a702a_0    conda-forge
libgfortran5              13.2.0               ha4646dd_0    conda-forge
libgomp                   11.2.0               h1234567_1  
libnpp                    12.0.2.50                     0    nvidia
libnpp-dev                12.0.2.50                     0    nvidia
libnpp-static             12.0.2.50                     0    nvidia
libnvjitlink              12.1.105                      0    nvidia
libnvjitlink-dev          12.1.55                       0    nvidia
libnvjpeg                 12.1.1.14                     0    nvidia
libnvjpeg-dev             12.1.0.39                     0    nvidia
libnvjpeg-static          12.3.1.117           ha770c72_1    conda-forge
librosa                   0.10.2.post1             pypi_0    pypi
libstdcxx-ng              11.2.0               h1234567_1  
libuuid                   1.41.5               h5eee18b_0  
linkify-it-py             2.0.3                    pypi_0    pypi
llvm-openmp               14.0.6               h9e868ea_0  
llvmlite                  0.43.0                   pypi_0    pypi
lm-format-enforcer        0.10.6                   pypi_0    pypi
markdown-it-py            3.0.0                    pypi_0    pypi
markupsafe                2.1.3           py310h5eee18b_0  
matplotlib                3.9.2                    pypi_0    pypi
mdit-py-plugins           0.4.1                    pypi_0    pypi
mdurl                     0.1.2                    pypi_0    pypi
memray                    1.13.4                   pypi_0    pypi
mkl                       2023.1.0         h213fc3f_46344  
mpc                       1.1.0                h10f8cd9_1  
mpfr                      4.0.2                hb69a4c5_1  
mpi                       1.0                       mpich    conda-forge
mpi4py                    3.1.3           py310h37cc914_1    conda-forge
mpich                     4.0.2              h846660c_100    conda-forge
mpmath                    1.3.0           py310h06a4308_0  
mscclpp                   0.5.2                    pypi_0    pypi
msgpack                   1.0.8                    pypi_0    pypi
msgspec                   0.18.6                   pypi_0    pypi
multidict                 6.0.5                    pypi_0    pypi
multiprocess              0.70.16                  pypi_0    pypi
ncurses                   6.4                  h6a678d5_0  
nest-asyncio              1.6.0                    pypi_0    pypi
netifaces                 0.11.0                   pypi_0    pypi
networkx                  3.1             py310h06a4308_0  
numba                     0.60.0                   pypi_0    pypi
numpy                     1.26.4                   pypi_0    pypi
nvidia-cublas-cu12        12.1.3.1                 pypi_0    pypi
nvidia-cuda-cupti-cu12    12.1.105                 pypi_0    pypi
nvidia-cuda-nvrtc-cu12    12.1.105                 pypi_0    pypi
nvidia-cuda-runtime-cu12  12.1.105                 pypi_0    pypi
nvidia-cudnn-cu12         9.1.0.70                 pypi_0    pypi
nvidia-cufft-cu12         11.0.2.54                pypi_0    pypi
nvidia-curand-cu12        10.3.2.106               pypi_0    pypi
nvidia-cusolver-cu12      11.4.5.107               pypi_0    pypi
nvidia-cusparse-cu12      12.1.0.106               pypi_0    pypi
nvidia-ml-py              12.560.30                pypi_0    pypi
nvidia-nccl-cu12          2.20.5                   pypi_0    pypi
nvidia-nvjitlink-cu12     12.6.20                  pypi_0    pypi
nvidia-nvtx-cu12          12.1.105                 pypi_0    pypi
openai                    1.42.0                   pypi_0    pypi
opencensus                0.11.4                   pypi_0    pypi
opencensus-context        0.1.3                    pypi_0    pypi
openssl                   3.0.13               h7f8727e_0  
outlines                  0.0.46                   pypi_0    pypi
packaging                 24.0                     pypi_0    pypi
pandas                    2.2.2                    pypi_0    pypi
pillow                    10.4.0                   pypi_0    pypi
pip                       23.3.1          py310h06a4308_0  
platformdirs              4.2.0                    pypi_0    pypi
pluggy                    1.5.0                    pypi_0    pypi
pooch                     1.8.2                    pypi_0    pypi
prettytable               3.11.0                   pypi_0    pypi
prometheus-client         0.20.0                   pypi_0    pypi
prometheus-fastapi-instrumentator 7.0.0                    pypi_0    pypi
proto-plus                1.23.0                   pypi_0    pypi
protobuf                  4.25.3                   pypi_0    pypi
psutil                    5.9.0           py310h5eee18b_0  
py-cpuinfo                9.0.0                    pypi_0    pypi
py-spy                    0.3.14                   pypi_0    pypi
pyairports                2.1.1                    pypi_0    pypi
pyarrow                   17.0.0                   pypi_0    pypi
pyasn1                    0.6.0                    pypi_0    pypi
pyasn1-modules            0.4.0                    pypi_0    pypi
pycountry                 24.6.1                   pypi_0    pypi
pycparser                 2.22                     pypi_0    pypi
pydantic                  2.8.2                    pypi_0    pypi
pydantic-core             2.20.1                   pypi_0    pypi
pygments                  2.18.0                   pypi_0    pypi
pyparsing                 3.1.2                    pypi_0    pypi
pytest                    8.3.2                    pypi_0    pypi
python                    3.10.14              h955ad1f_0  
python-dateutil           2.9.0.post0              pypi_0    pypi
python-dotenv             1.0.1                    pypi_0    pypi
python_abi                3.10                    2_cp310    conda-forge
pytorch-cuda              12.1                 ha16c6d3_5    pytorch
pytorch-mutex             1.0                        cuda    pytorch
pytz                      2024.1                   pypi_0    pypi
pyyaml                    6.0.1           py310h5eee18b_0  
pyzmq                     26.2.0                   pypi_0    pypi
ray                       2.34.0                   pypi_0    pypi
readline                  8.2                  h5eee18b_0  
referencing               0.34.0                   pypi_0    pypi
regex                     2024.4.16                pypi_0    pypi
requests                  2.32.3                   pypi_0    pypi
rich                      13.7.1                   pypi_0    pypi
rpds-py                   0.18.0                   pypi_0    pypi
rsa                       4.9                      pypi_0    pypi
safetensors               0.4.3                    pypi_0    pypi
scikit-learn              1.5.1                    pypi_0    pypi
scipy                     1.14.1                   pypi_0    pypi
sentencepiece             0.2.0                    pypi_0    pypi
setuptools                68.2.2          py310h06a4308_0  
six                       1.16.0                   pypi_0    pypi
smart-open                7.0.4                    pypi_0    pypi
sniffio                   1.3.1                    pypi_0    pypi
soundfile                 0.12.1                   pypi_0    pypi
soxr                      0.5.0                    pypi_0    pypi
sqlite                    3.41.2               h5eee18b_0  
starlette                 0.37.2                   pypi_0    pypi
swiftllm                  0.0.1                     dev_0    <develop>
swiftllm-c                0.0.1                     dev_0    <develop>
sympy                     1.12            py310h06a4308_0  
tbb                       2021.8.0             hdb19cb5_0  
textual                   0.77.0                   pypi_0    pypi
threadpoolctl             3.5.0                    pypi_0    pypi
tiktoken                  0.7.0                    pypi_0    pypi
tk                        8.6.12               h1ccaba5_0  
tokenizers                0.19.1                   pypi_0    pypi
tomli                     2.0.1                    pypi_0    pypi
torch                     2.4.0                    pypi_0    pypi
torchvision               0.19.0                   pypi_0    pypi
tqdm                      4.66.5                   pypi_0    pypi
transformers              4.44.2                   pypi_0    pypi
triton                    3.0.0                    pypi_0    pypi
typing-extensions         4.12.2                   pypi_0    pypi
tzdata                    2024.1                   pypi_0    pypi
uc-micro-py               1.0.3                    pypi_0    pypi
urllib3                   2.2.1                    pypi_0    pypi
uvicorn                   0.29.0                   pypi_0    pypi
uvloop                    0.20.0                   pypi_0    pypi
virtualenv                20.25.3                  pypi_0    pypi
vllm                      0.5.5                    pypi_0    pypi
vllm-flash-attn           2.6.1                    pypi_0    pypi
watchfiles                0.23.0                   pypi_0    pypi
wcwidth                   0.2.13                   pypi_0    pypi
websockets                13.0                     pypi_0    pypi
wheel                     0.41.2          py310h06a4308_0  
wrapt                     1.16.0                   pypi_0    pypi
xformers                  0.0.27.post2             pypi_0    pypi
xxhash                    3.5.0                    pypi_0    pypi
xz                        5.4.6                h5eee18b_0  
yaml                      0.2.5                h7b6447c_0  
yarl                      1.9.4                    pypi_0    pypi
zipp                      3.20.0                   pypi_0    pypi
zlib                      1.2.13               h5eee18b_0  

```

## 评论 (1)

### lahmuller · 2024-11-13

Hi, @gursimar. I encountered the similar problem. Have you resolved it now?
