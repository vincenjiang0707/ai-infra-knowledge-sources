source: https://docs.vllm.ai/en/latest/getting_started/installation/cpu/
lastmod: 2026-09-23

# CPU[¶](https://docs.vllm.ai#cpu)

vLLM is a Python library that supports the following CPU variants. Select your CPU type to see vendor specific instructions:

vLLM supports basic model inferencing and serving on x86 CPU platform, with data types FP32, FP16 and BF16.

vLLM offers basic model inferencing and serving on Arm CPU platform, with support for NEON, data types FP32, FP16 and BF16.

vLLM has experimental support for macOS with Apple Silicon. For now, users must build from source to natively run on macOS.

Currently the CPU implementation for macOS supports FP32 and FP16 datatypes.

GPU-Accelerated Inference with vLLM-Metal

For GPU-accelerated inference on Apple Silicon using Metal, check out [vllm-metal](https://github.com/vllm-project/vllm-metal), a community-maintained hardware plugin that uses MLX as the compute backend.

vLLM has experimental support for s390x architecture on IBM Z platform. For now, users must build from source to natively run on IBM Z platform.

Currently, the CPU implementation for s390x architecture supports FP32, BF16 and FP16, as well as AWQ and GPTQ 4-bit quantization and compressed-tensors INT8 W8A8.

## Technical Discussions[¶](https://docs.vllm.ai#technical-discussions)

The main discussions happen in the `#sig-cpu`

channel of [vLLM Slack](https://slack.vllm.ai/).

When open a Github issue about the CPU backend, please add `[CPU Backend]`

in the title and it will be labeled with `cpu`

for better awareness.

## Requirements[¶](https://docs.vllm.ai#requirements)

- Python: 3.10 -- 3.13

- OS: Linux
- CPU flags:
`avx512f`

(Recommended),`avx2`

(Limited features)

Tip

Use `lscpu`

to check the CPU flags.

- OS: Linux
- Compiler:
`gcc/g++ >= 12.3.0`

(optional, recommended) - Instruction Set Architecture (ISA): NEON support is required

- OS:
`macOS Sonoma`

or later - SDK:
`XCode 15.4`

or later with Command Line Tools - Compiler:
`Apple Clang >= 15.0.0`


Note

The macOS CPU build is smoke-tested in CI on the latest GA Apple Silicon runner; other macOS or Apple Clang versions are best-effort.

- OS:
`Linux`

- SDK:
`gcc/g++ >= 14.0.0`

or later with Command Line Tools - Instruction Set Architecture (ISA): VXE support is required. Works with Z15 and above.
- Build from source python packages (no pre-built s390x wheels):
`torchvision`

,`llvmlite`

,`numba`

,`opencv-python-headless`

,`hf-xet`


## Set up using Python[¶](https://docs.vllm.ai#set-up-using-python)

### Create a new Python environment[¶](https://docs.vllm.ai#create-a-new-python-environment)

It's recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`

. After installing `uv`

, you can create a new Python environment using the following commands:

### Pre-built wheels[¶](https://docs.vllm.ai#pre-built-wheels)

When specifying the index URL, please make sure to use the `cpu`

variant subdirectory. For example, the nightly build index is: `https://wheels.vllm.ai/nightly/cpu/`

.

Pre-built vLLM wheels for x86 with AVX512/AVX2 are available since version 0.17.0. To install release wheels:

export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
# use uv
uv pip install "https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_34_x86_64.whl" --torch-backend cpu


## pip

set `LD_PRELOAD`


Before use vLLM CPU installed via wheels, make sure Intel OpenMP is added to `LD_PRELOAD`

:

#### Install the latest code[¶](https://docs.vllm.ai#install-the-latest-code)

To install the wheel built from the latest main branch:

uv pip install vllm --extra-index-url https://wheels.vllm.ai/nightly/cpu --index-strategy first-index --torch-backend cpu


#### Install specific revisions[¶](https://docs.vllm.ai#install-specific-revisions)

If you want to access the wheels for previous commits (e.g. to bisect the behavior change, performance regression), you can specify the commit hash in the URL:

Pre-built vLLM wheels for Arm are available since version 0.11.2. These wheels contain pre-compiled C++ binaries.

export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
uv pip install "https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_34_aarch64.whl" --torch-backend cpu


## pip

The `uv`

approach works for vLLM `v0.6.6`

and later. A unique feature of `uv`

is that packages in `--extra-index-url`

have [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes). If the latest public release is `v0.6.6.post1`

, `uv`

's behavior allows installing a commit before `v0.6.6.post1`

by specifying the `--extra-index-url`

. In contrast, `pip`

combines packages from `--extra-index-url`

and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version.

#### Install the latest code[¶](https://docs.vllm.ai#install-the-latest-code_1)

LLM inference is a fast-evolving field, and the latest code may contain bug fixes, performance improvements, and new features that are not released yet. To allow users to try the latest code without waiting for the next release, vLLM provides working pre-built Arm CPU wheels for every commit since `v0.11.2`

on [https://wheels.vllm.ai/nightly](https://wheels.vllm.ai/nightly). For native CPU wheels, this index should be used:

`https://wheels.vllm.ai/nightly/cpu/vllm`


To install from nightly index, run:

uv pip install vllm --extra-index-url https://wheels.vllm.ai/nightly/cpu --index-strategy first-index --torch-backend cpu


## pip (there's a caveat)

Using `pip`

to install from nightly indices is *not supported*, because `pip`

combines packages from `--extra-index-url`

and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version. In contrast, `uv`

gives the extra index [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes).

If you insist on using `pip`

, you have to specify the full URL (link address) of the wheel file (which can be obtained from https://wheels.vllm.ai/nightly/cpu/vllm).

#### Install specific revisions[¶](https://docs.vllm.ai#install-specific-revisions_1)

If you want to access the wheels for previous commits (e.g. to bisect the behavior change, performance regression), you can specify the commit hash in the URL:

Currently, there are no pre-built Apple silicon CPU wheels.

Currently, there are no pre-built IBM Z CPU wheels.

### Build wheel from source[¶](https://docs.vllm.ai#build-wheel-from-source)

#### Set up using Python-only build (without compilation)[¶](https://docs.vllm.ai#python-only-build)

This method requires [pre-built wheels](https://docs.vllm.ai#pre-built-wheels) for your platform.

Please refer to the instructions for [Python-only build on GPU](https://docs.vllm.ai/gpu/#python-only-build), and replace the build commands with:

VLLM_USE_PRECOMPILED=1 VLLM_PRECOMPILED_WHEEL_VARIANT=cpu VLLM_TARGET_DEVICE=cpu uv pip install --editable .


#### Full build (with compilation)[¶](https://docs.vllm.ai#full-build)

Install recommended compiler. We recommend to use `gcc/g++ >= 12.3.0`

as the default compiler to avoid potential problems. For example, on Ubuntu 22.4, you can run:

sudo apt-get update -y
sudo apt-get install -y gcc-12 g++-12 libnuma-dev
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12


It's recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`

. After installing `uv`

, you can create a new Python environment using the following commands:

Clone the vLLM project:

Install the required dependencies:

uv pip install -r requirements/build/cpu.txt --torch-backend cpu --index-strategy unsafe-best-match
uv pip install -r requirements/cpu.txt --torch-backend cpu --index-strategy unsafe-best-match


## pip

Build and install vLLM:

If you want to develop vLLM, install it in editable mode instead.

Optionally, build a portable wheel which you can then install elsewhere:

set `LD_PRELOAD`


Before using vLLM CPU installed via wheels, make sure TCMalloc and Intel OpenMP are installed and added to `LD_PRELOAD`

:

# install TCMalloc, Intel OpenMP is installed with vLLM CPU
sudo apt-get install -y --no-install-recommends libtcmalloc-minimal4
# manually find the path
sudo find / -iname *libtcmalloc_minimal.so.4
sudo find / -iname *libiomp5.so
TC_PATH=...
IOMP_PATH=...
# add them to LD_PRELOAD
export LD_PRELOAD="$TC_PATH:$IOMP_PATH:$LD_PRELOAD"


Troubleshooting

**NumPy ≥2.0 error**: Downgrade using`pip install "numpy<2.0"`

.**CMake picks up CUDA**: Add`CMAKE_DISABLE_FIND_PACKAGE_CUDA=ON`

to prevent CUDA detection during CPU builds, even if CUDA is installed.`AMD`

requires at least 4th gen processors (Zen 4/Genoa) or higher to support[AVX512](https://www.phoronix.com/review/amd-zen4-avx512)to run vLLM on CPU.- If you receive an error such as:
`Could not find a version that satisfies the requirement torch==X.Y.Z+cpu+cpu`

, consider updating[pyproject.toml](https://github.com/vllm-project/vllm/blob/main/pyproject.toml)to help pip resolve the dependency.

First, install the recommended compiler. We recommend using `gcc/g++ >= 12.3.0`

as the default compiler to avoid potential problems. For example, on Ubuntu 22.4, you can run:

sudo apt-get update -y
sudo apt-get install -y --no-install-recommends ccache git curl wget ca-certificates gcc-12 g++-12 libtcmalloc-minimal4 libnuma-dev ffmpeg libsm6 libxext6 libgl1 jq lsof
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12


Second, clone the vLLM project:

Third, install required dependencies:

uv pip install -r requirements/build/cpu.txt --torch-backend cpu --index-strategy unsafe-best-match
uv pip install -r requirements/cpu.txt --torch-backend cpu --index-strategy unsafe-best-match


## pip

Finally, build and install vLLM:

If you want to develop vLLM, install it in editable mode instead.

Testing has been conducted on AWS Graviton3 instances for compatibility.

set `LD_PRELOAD`


Before use vLLM CPU installed via wheels, make sure TCMalloc is installed and added to `LD_PRELOAD`

:

After installation of XCode and the Command Line Tools, which include Apple Clang, execute the following commands to build and install vLLM from source.

git clone https://github.com/vllm-project/vllm.git
cd vllm
uv pip install -r requirements/cpu.txt
uv pip install -e .


Note

On macOS the `VLLM_TARGET_DEVICE`

is automatically set to `cpu`

, which is currently the only supported device.

Troubleshooting

If the build fails with errors like the following where standard C++ headers cannot be found, try to remove and reinstall your [Command Line Tools for Xcode](https://developer.apple.com/download/all/).

[...] fatal error: 'map' file not found
1 | #include <map>
| ^~~~~
1 error generated.
[2/8] Building CXX object CMakeFiles/_C.dir/csrc/cpu/pos_encoding.cpp.o
[...] fatal error: 'cstddef' file not found
10 | #include <cstddef>
| ^~~~~~~~~
1 error generated.


If the build fails with C++11/C++17 compatibility errors like the following, the issue is that the build system is defaulting to an older C++ standard:

[...] error: 'constexpr' is not a type
[...] error: expected ';' before 'constexpr'
[...] error: 'constexpr' does not name a type


**Solution**: Your compiler might be using an older C++ standard. Edit `cmake/cpu_extension.cmake`

and add `set(CMAKE_CXX_STANDARD 17)`

before `set(CMAKE_CXX_STANDARD_REQUIRED ON)`

.

To check your compiler's C++ standard support:

On Apple Clang 16 you should see:`#define __cplusplus 201703L`

Install the following packages from the package manager before building the vLLM. For example on RHEL 9.6:

dnf install -y \
which procps findutils tar vim git patch xz ninja-build \
gcc-toolset-14 gcc-toolset-14-binutils gcc-toolset-14-libatomic-devel zlib-devel \
libjpeg-turbo-devel libtiff-devel libpng-devel libwebp-devel freetype-devel harfbuzz-devel \
openssl-devel openblas openblas-devel autoconf automake libtool cmake numpy libsndfile \
clang llvm-devel llvm-static clang-devel


Build and install `numactl`

from source:

curl -LO https://github.com/numactl/numactl/archive/refs/tags/v2.0.19.tar.gz
tar -xvzf v2.0.19.tar.gz
cd numactl-2.0.19
./autogen.sh && ./configure && make && make install
cd ..


Install rust>=1.80 which is needed for `outlines-core`

, `uvloop`

, and `hf-xet`

python packages installation.

Execute the following commands to build and install vLLM from source.

Tip

Pre-built wheels are not available for s390x for the following packages. Build them from source before building vLLM: `torchvision`

, `llvmlite`

, `numba`

, `opencv-python-headless`

, `hf-xet`

. See `docker/Dockerfile.s390x`

for exact versions and build commands used in each multi-stage build.

LLVM 20 required for llvmlite

`llvmlite v0.47`

requires LLVM 20, but UBI 9.6 repos ship LLVM 21 which is not compatible. You must build LLVM 20 from source before building `llvmlite`

:

curl -LO https://github.com/llvm/llvm-project/releases/download/llvmorg-20.1.8/llvm-project-20.1.8.src.tar.xz
tar -xf llvm-project-20.1.8.src.tar.xz
cmake -G Ninja -S llvm-project-20.1.8.src/llvm -B llvm-build \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_INSTALL_PREFIX=/opt/llvm20 \
-DLLVM_TARGETS_TO_BUILD="SystemZ" \
-DLLVM_ENABLE_RTTI=ON \
-DLLVM_BUILD_TOOLS=OFF \
-DLLVM_BUILD_UTILS=ON \
-DLLVM_BUILD_EXAMPLES=OFF \
-DLLVM_BUILD_TESTS=OFF \
-DLLVM_INCLUDE_TESTS=OFF \
-DLLVM_INCLUDE_EXAMPLES=OFF \
-DLLVM_INCLUDE_BENCHMARKS=OFF
ninja -C llvm-build install


Then build `llvmlite`

pointing to LLVM 20:

uv pip install -v \
/path/to/torchvision.whl \
/path/to/llvmlite.whl \
/path/to/numba.whl \
/path/to/opencv_python_headless.whl \
/path/to/hf_xet.whl \
-r requirements/build/cpu.txt \
-r requirements/cpu.txt \
--torch-backend cpu \
--index-strategy unsafe-best-match && \
VLLM_TARGET_DEVICE=cpu VLLM_CPU_MOE_PREPACK=0 python setup.py bdist_wheel && \
uv pip install dist/*.whl


## pip

pip install -v \
--extra-index-url https://download.pytorch.org/whl/cpu \
/path/to/torchvision.whl \
/path/to/llvmlite.whl \
/path/to/numba.whl \
/path/to/opencv_python_headless.whl \
/path/to/hf_xet.whl \
-r requirements/build/cpu.txt \
-r requirements/cpu.txt && \
VLLM_TARGET_DEVICE=cpu VLLM_CPU_MOE_PREPACK=0 python setup.py bdist_wheel && \
pip install dist/*.whl


set `LD_PRELOAD`

for TCMalloc

For best memory allocation performance, build and install [gperftools](https://github.com/gperftools/gperftools) (TCMalloc) from source and add it to `LD_PRELOAD`

:

# Build and install TCMalloc from source
curl -LO https://github.com/gperftools/gperftools/releases/download/gperftools-2.16/gperftools-2.16.tar.gz
tar -xzf gperftools-2.16.tar.gz
cd gperftools-2.16
./configure --enable-minimal && make -j$(nproc) && sudo make install
sudo ldconfig
cd ..
# Add to LD_PRELOAD
export LD_PRELOAD="/usr/local/lib/libtcmalloc_minimal.so.4:$LD_PRELOAD"


The Docker image (`Dockerfile.s390x`

) already includes TCMalloc and sets `LD_PRELOAD`

automatically.

## Set up using Docker[¶](https://docs.vllm.ai#set-up-using-docker)

### Pre-built images[¶](https://docs.vllm.ai#pre-built-images)

You can pull the latest available CPU image from Docker Hub:

To pull an image for a specific vLLM version:

export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
docker pull vllm/vllm-openai-cpu:v${VLLM_VERSION}-x86_64


All available image tags are here: [https://hub.docker.com/r/vllm/vllm-openai-cpu/tags](https://hub.docker.com/r/vllm/vllm-openai-cpu/tags)

You can run these images via:

To pull the latest image from Docker Hub:

To pull an image with a specific vLLM version:

export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
docker pull vllm/vllm-openai-cpu:v${VLLM_VERSION}-arm64


All available image tags are here: [https://hub.docker.com/r/vllm/vllm-openai-cpu/tags](https://hub.docker.com/r/vllm/vllm-openai-cpu/tags).

You can run these images via:

docker run \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-p 8000:8000 \
--env "HF_TOKEN=<secret>" \
vllm/vllm-openai-cpu:latest-arm64 <args...>


You can also access the latest code with Docker images. These are not intended for production use and are meant for CI and testing only. They will expire after several days.

The latest code can contain bugs and may not be stable. Please use it with caution.

Currently, there are no pre-built Arm silicon CPU images.

Currently, there are no pre-built IBM Z CPU images.

### Build image from source[¶](https://docs.vllm.ai#build-image-from-source)

#### Building for your target CPU[¶](https://docs.vllm.ai#building-for-your-target-cpu)

docker build -f docker/Dockerfile.cpu \
--build-arg VLLM_CPU_X86=<false (default)|true> \ # For cross-compilation
--tag vllm-cpu-env \
--target vllm-openai .


#### Building with AMD Zen optimizations[¶](https://docs.vllm.ai#building-with-amd-zen-optimizations)

For AMD Zen 4 / Zen 5 hosts (`linux/amd64`

only), use the `vllm-openai-zen`

target. It extends the default `vllm-openai`

image and adds `zentorch`

via the `vllm[zen]`

extra so `ZenCpuPlatform`

auto-activates at runtime:

The resulting image accepts the same arguments and environment variables as `vllm-openai`

(see [Launching the OpenAI server](https://docs.vllm.ai#launching-the-openai-server) below); no extra flag is needed to engage Zen optimizations. See [AMD Zen optimizations](https://docs.vllm.ai/#amd-zen-optimizations) for runtime behavior and the supported-dtype caveats.

#### Launching the OpenAI server[¶](https://docs.vllm.ai#launching-the-openai-server)

#### Building for your target ARM CPU[¶](https://docs.vllm.ai#building-for-your-target-arm-cpu)

docker build -f docker/Dockerfile.cpu \
--platform=linux/arm64 \
--build-arg VLLM_CPU_ARM_BF16=<false (default)|true> \
--tag vllm-cpu-env \
--target vllm-openai .


Auto-detection by default

By default, ARM CPU instruction sets (BF16, NEON, etc.) are automatically detected from the build system's CPU flags. The `VLLM_CPU_ARM_BF16`

build argument is used for cross-compilation:

`VLLM_CPU_ARM_BF16=true`

- Force-enable ARM BF16 support (build with BF16 regardless of build system capabilities)`VLLM_CPU_ARM_BF16=false`

- Rely on auto-detection (default)

##### Examples[¶](https://docs.vllm.ai#examples)

###### Auto-detection build (native ARM)[¶](https://docs.vllm.ai#auto-detection-build-native-arm)

# Building on ARM64 system - platform auto-detected
docker build -f docker/Dockerfile.cpu \
--tag vllm-cpu-arm64 \
--target vllm-openai .


###### Cross-compile for ARM with BF16 support[¶](https://docs.vllm.ai#cross-compile-for-arm-with-bf16-support)

# Building on ARM64 for newer ARM CPUs with BF16
docker build -f docker/Dockerfile.cpu \
--build-arg VLLM_CPU_ARM_BF16=true \
--tag vllm-cpu-arm64-bf16 \
--target vllm-openai .


###### Cross-compile from x86_64 to ARM64 with BF16[¶](https://docs.vllm.ai#cross-compile-from-x86_64-to-arm64-with-bf16)

# Requires Docker buildx with ARM emulation (QEMU)
docker buildx build -f docker/Dockerfile.cpu \
--platform=linux/arm64 \
--build-arg VLLM_CPU_ARM_BF16=true \
--build-arg max_jobs=4 \
--tag vllm-cpu-arm64-bf16 \
--target vllm-openai \
--load .


ARM BF16 requirements

ARM BF16 support requires ARMv8.6-A or later (FEAT_BF16). Supported on AWS Graviton3/4, AmpereOne, and other recent ARM processors.

#### Launching the OpenAI server[¶](https://docs.vllm.ai#launching-the-openai-server_1)

docker run --rm \
--security-opt seccomp=unconfined \
--cap-add SYS_NICE \
--shm-size=4g \
-p 8000:8000 \
-e VLLM_CPU_KVCACHE_SPACE=<KV cache space> \
-e VLLM_CPU_OMP_THREADS_BIND=<CPU cores for inference> \
vllm-cpu-arm64 \
meta-llama/Llama-3.2-1B-Instruct \
--dtype=bfloat16 \
other vLLM OpenAI server arguments


Alternative to --privileged

Instead of `--privileged=true`

, use `--cap-add SYS_NICE --security-opt seccomp=unconfined`

for better security.

docker build -f docker/Dockerfile.s390x \
--tag vllm-cpu-env .
# Launch OpenAI server
docker run --rm \
--security-opt seccomp=unconfined \
--cap-add SYS_NICE \
--shm-size 4g \
-p 8000:8000 \
-e VLLM_CPU_KVCACHE_SPACE=<KV cache space> \
-e VLLM_CPU_OMP_THREADS_BIND=<CPU cores for inference> \
vllm-cpu-env \
--model meta-llama/Llama-3.2-1B-Instruct \
--dtype bfloat16 \
other vLLM OpenAI server arguments


Tip

Alternatively, `--privileged=true`

also works but is broader and not generally recommended.

## AMD Zen optimizations[¶](https://docs.vllm.ai#amd-zen-optimizations)

On AMD Zen CPUs, vLLM auto-selects `ZenCpuPlatform`

(a subclass of `CpuPlatform`

) which dispatches linear layers through [ zentorch](https://github.com/amd/ZenDNN-pytorch-plugin)'s ZenDNN-optimized kernels. See the FAQ entry

[How do I enable AMD Zen optimizations?](https://docs.vllm.ai#how-do-i-enable-amd-zen-optimizations)for the install command.

### Detection rules[¶](https://docs.vllm.ai#detection-rules)

`ZenCpuPlatform`

is selected when **all** of the following hold:

- vLLM is built for CPU
`/proc/cpuinfo`

reports`AuthenticAMD`

and`avx512`

`import zentorch`

succeeds

Otherwise, vLLM falls back to the default `CpuPlatform`

(oneDNN / sgl-kernel paths).

### Supported dtypes[¶](https://docs.vllm.ai#supported-dtypes)

`float16`

is **not** supported on `ZenCpuPlatform`

. `ZenCpuPlatform.supported_dtypes`

advertises only `bfloat16`

and `float32`

, so models declared with `torch_dtype=float16`

are auto-downcast to `bfloat16`

at load time with the standard `"Your device 'cpu' doesn't support torch.float16. Falling back to torch.bfloat16 for compatibility."`

warning emitted from `vllm/config/model.py`

.

### Environment variables[¶](https://docs.vllm.ai#environment-variables)

`VLLM_ZENTORCH_WEIGHT_PREPACK`

(default`1`

): eagerly prepacks linear weights into ZenDNN's blocked layout at model load time, eliminating per-inference layout conversion overhead. Set to`0`

to disable.

### Docker[¶](https://docs.vllm.ai#docker)

The `vllm-openai-zen`

Docker target (in `docker/Dockerfile.cpu`

) extends the default `vllm-openai`

image with `vllm[zen]`

. Build it with `docker build -f docker/Dockerfile.cpu --target vllm-openai-zen .`

— see [Building with AMD Zen optimizations](https://docs.vllm.ai#building-with-amd-zen-optimizations) for the full command and run instructions.

### Reference[¶](https://docs.vllm.ai#reference)

For the design rationale, see [ RFC #35089: In-Tree AMD Zen CPU Backend via zentorch](https://github.com/vllm-project/vllm/issues/35089).

## Related runtime environment variables[¶](https://docs.vllm.ai#related-runtime-environment-variables)

`VLLM_CPU_KVCACHE_SPACE`

: specify the KV Cache size (e.g,`VLLM_CPU_KVCACHE_SPACE=40`

means 40 GiB space for KV cache), larger setting will allow vLLM to run more requests in parallel. This parameter should be set based on the hardware configuration and memory management pattern of users. Default value is`0`

.`VLLM_CPU_OMP_THREADS_BIND`

: specify the CPU cores dedicated to the OpenMP threads, can be set as CPU id lists,`auto`

(by default), or`nobind`

(to disable binding to individual CPU cores and to inherit user-defined OpenMP variables). For example,`VLLM_CPU_OMP_THREADS_BIND=0-31`

means there will be 32 OpenMP threads bound on 0-31 CPU cores.`VLLM_CPU_OMP_THREADS_BIND=0-31|32-63`

means there will be 2 tensor parallel processes, 32 OpenMP threads of rank0 are bound on 0-31 CPU cores, and the OpenMP threads of rank1 are bound on 32-63 CPU cores. By setting to`auto`

, the OpenMP threads of each rank are bound to the CPU cores in each NUMA node respectively. If set to`nobind`

, the number of OpenMP threads is determined by the standard`OMP_NUM_THREADS`

environment variable.`VLLM_CPU_NUM_OF_RESERVED_CPU`

: specify the total number of CPU cores which are not dedicated to OpenMP threads. The variable only takes effect when`VLLM_CPU_OMP_THREADS_BIND`

is set to`auto`

. By default, x86, ARM, and RISC-V reserve`local_world_size`

CPUs in total, while PowerPC and S390X retain a one-CPU default. When KV transfer is enabled, one additional CPU is reserved per local rank. Reserved CPUs are distributed across the local ranks.`CPU_VISIBLE_MEMORY_NODES`

: specify visible NUMA memory nodes for vLLM CPU workers, similar to`CUDA_VISIBLE_DEVICES`

. The variable only takes effect when VLLM_CPU_OMP_THREADS_BIND is set to`auto`

. The variable provides more control for the auto thread-binding feature, such as masking nodes and changing nodes binding sequence.`VLLM_ZENTORCH_WEIGHT_PREPACK`

(AMD Zen only): whenis active, eagerly prepack linear weights into ZenDNN's blocked layout at model load time, eliminating per-inference layout conversion overhead. Default is`ZenCpuPlatform`

`1`

(enabled). See[AMD Zen optimizations](https://docs.vllm.ai#amd-zen-optimizations).

## FAQ[¶](https://docs.vllm.ai#faq)

### Which `dtype`

should be used?[¶](https://docs.vllm.ai#which-dtype-should-be-used)

- Currently, vLLM CPU uses model default settings as
`dtype`

. However, due to unstable float16 support in torch CPU, it is recommended to explicitly set`dtype=bfloat16`

if there are any performance or accuracy problem. - On AMD Zen CPUs (
),`ZenCpuPlatform`

`float16`

is**not**supported. Only`bfloat16`

and`float32`

are accepted; models declared with`float16`

are auto-downcast to`bfloat16`

at model load time. See[AMD Zen optimizations](https://docs.vllm.ai#amd-zen-optimizations).

### How to launch a vLLM service on CPU?[¶](https://docs.vllm.ai#how-to-launch-a-vllm-service-on-cpu)

- When using the online serving, it is recommended to reserve 1-2 CPU cores for the serving framework to avoid CPU oversubscription. For example, on a platform with 32 physical CPU cores, reserving CPU 31 for the framework and using CPU 0-30 for inference threads:

export VLLM_CPU_KVCACHE_SPACE=40
export VLLM_CPU_OMP_THREADS_BIND=0-30
vllm serve facebook/opt-125m --dtype=bfloat16


or using default auto thread binding:

export VLLM_CPU_KVCACHE_SPACE=40
export VLLM_CPU_NUM_OF_RESERVED_CPU=1
vllm serve facebook/opt-125m --dtype=bfloat16


Note, it is recommended to manually reserve 1 CPU for vLLM front-end process when `world_size == 1`

.

### What are supported models on CPU?[¶](https://docs.vllm.ai#what-are-supported-models-on-cpu)

For the full and up-to-date list of models validated on CPU platforms, please see the official documentation: [Supported Models on CPU](https://docs.vllm.ai/models/hardware_supported_models/cpu/)

### How to find benchmark configuration examples for supported CPU models?[¶](https://docs.vllm.ai#how-to-find-benchmark-configuration-examples-for-supported-cpu-models)

For any model listed under [Supported Models on CPU](https://docs.vllm.ai/models/hardware_supported_models/cpu/), optimized runtime configurations are provided in the vLLM Benchmark Suite’s CPU test cases, defined in cpu test cases as serving-tests-cpu.json. Full test cases for Text-only models, Multi-Modal models and Embedded models are in cpu Text-Only test cases as serving-tests-cpu-text.json, cpu Multi-Modal test cases as serving-tests-cpu-multimodal.json and cpu Embedded test cases as serving-tests-cpu-embed.json.

For details on how these optimized configurations are determined, see: [ performance-benchmark-details](https://github.com/vllm-project/vllm/blob/main/.buildkite/performance-benchmarks/README.md#performance-benchmark-details). To benchmark the supported models using these optimized settings, follow the steps in [running vLLM Benchmark Suite manually](https://docs.vllm.ai/benchmarking/dashboard/#manually-trigger-the-benchmark) and run the Benchmark Suite on a CPU environment.

Below is an example command to benchmark all CPU-supported models using optimized configurations.

The benchmark results will be saved in `./benchmark/results/`

. In the directory, the generated `.commands`

files contain all example commands for the benchmark.

We recommend configuring tensor-parallel-size to match the number of NUMA nodes on your system. Note that the current release does not support tensor-parallel-size=6. To determine the number of NUMA nodes available, use the following command:

For performance reference, users may also consult the [vLLM Performance Dashboard](https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm&deviceName=cpu) , which publishes default-model CPU results produced using the same Benchmark Suite.

#### Dry-Run[¶](https://docs.vllm.ai#dry-run)

For users only need to get the optimized runtime configurations without running benchmark, a Dry-Run mode is provided. By passing an environment variable DRY_RUN=1 with run-performance-benchmarks.sh, all commands will be generated under `./benchmark/results/`

.

By providing different JSON file, users can get runtime configurations for different models such as Embedded Models.

ON_CPU=1 SERVING_JSON=serving-tests-cpu-embed.json DRY_RUN=1 bash .buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh


By providing MODEL_FILTER and DTYPE_FILTER, only commands for related model ID and Data Type will be generated.

ON_CPU=1 SERVING_JSON=serving-tests-cpu-text.json DRY_RUN=1 MODEL_FILTER=meta-llama/Llama-3.1-8B-Instruct DTYPE_FILTER=bfloat16 bash .buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh


### How do I enable AMD Zen optimizations?[¶](https://docs.vllm.ai#how-do-i-enable-amd-zen-optimizations)

On an AMD Zen 4 / Zen 5 CPU, install the CPU wheel with the `zen`

extra so vLLM pulls the tested `zentorch`

version for that release:

export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
uv pip install "vllm[zen]" --extra-index-url https://wheels.vllm.ai/${VLLM_VERSION}/cpu --index-strategy first-index --torch-backend cpu


vLLM auto-detects the platform and routes linear layers through ZenDNN-optimized kernels - no flag needed. To verify it is engaged, look for the platform-selection line in the server's startup logs:

For per-backend dispatch details (which kernel each linear layer was bound to), re-run with `VLLM_LOGGING_LEVEL=DEBUG`

and grep for `CPU unquantized GEMM dispatch`

.

See [AMD Zen optimizations](https://docs.vllm.ai#amd-zen-optimizations) for detection rules, supported dtypes, and the `VLLM_ZENTORCH_WEIGHT_PREPACK`

knob.

### How to decide `VLLM_CPU_OMP_THREADS_BIND`

?[¶](https://docs.vllm.ai#how-to-decide-vllm_cpu_omp_threads_bind)

-
Default

`auto`

thread-binding is recommended for most cases. Ideally, each OpenMP thread will be bound to a dedicated physical core respectively, threads of each rank will be bound to the same NUMA node respectively, and the default reserved CPUs will be kept for other vLLM components. On x86, ARM, and RISC-V,`local_world_size`

CPUs are reserved in total, plus one additional CPU per local rank when KV transfer is enabled. If you have any performance problems or unexpected binding behaviours, please try to bind threads as following. -
On a hyper-threading enabled platform with 16 logical CPU cores / 8 physical CPU cores:


## Commands

$ lscpu -e # check the mapping between logical CPU cores and physical CPU cores
# The "CPU" column means the logical CPU core IDs, and the "CORE" column means the physical core IDs. On this platform, two logical cores are sharing one physical core.
CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE MAXMHZ MINMHZ MHZ
0 0 0 0 0:0:0:0 yes 2401.0000 800.0000 800.000
1 0 0 1 1:1:1:0 yes 2401.0000 800.0000 800.000
2 0 0 2 2:2:2:0 yes 2401.0000 800.0000 800.000
3 0 0 3 3:3:3:0 yes 2401.0000 800.0000 800.000
4 0 0 4 4:4:4:0 yes 2401.0000 800.0000 800.000
5 0 0 5 5:5:5:0 yes 2401.0000 800.0000 800.000
6 0 0 6 6:6:6:0 yes 2401.0000 800.0000 800.000
7 0 0 7 7:7:7:0 yes 2401.0000 800.0000 800.000
8 0 0 0 0:0:0:0 yes 2401.0000 800.0000 800.000
9 0 0 1 1:1:1:0 yes 2401.0000 800.0000 800.000
10 0 0 2 2:2:2:0 yes 2401.0000 800.0000 800.000
11 0 0 3 3:3:3:0 yes 2401.0000 800.0000 800.000
12 0 0 4 4:4:4:0 yes 2401.0000 800.0000 800.000
13 0 0 5 5:5:5:0 yes 2401.0000 800.0000 800.000
14 0 0 6 6:6:6:0 yes 2401.0000 800.0000 800.000
15 0 0 7 7:7:7:0 yes 2401.0000 800.0000 800.000
# On this platform, it is recommended to only bind openMP threads on logical CPU cores 0-7 or 8-15
$ export VLLM_CPU_OMP_THREADS_BIND=0-7
$ python examples/basic/offline_inference/basic.py


- When deploying vLLM CPU backend on a multi-socket machine with NUMA and enable tensor parallel or pipeline parallel, each NUMA node is treated as a TP/PP rank. So be aware to set CPU cores of a single rank on the same NUMA node to avoid cross NUMA node memory access.

### How to decide `VLLM_CPU_KVCACHE_SPACE`

?[¶](https://docs.vllm.ai#how-to-decide-vllm_cpu_kvcache_space)

This value is 4GB by default. Larger space can support more concurrent requests, longer context length. However, users should take care of memory capacity of each NUMA node. The memory usage of each TP rank is the sum of `weight shard size`

and `VLLM_CPU_KVCACHE_SPACE`

, if it exceeds the capacity of a single NUMA node, the TP worker will be killed with `exitcode 9`

due to out-of-memory.

### How to do performance tuning for vLLM CPU?[¶](https://docs.vllm.ai#how-to-do-performance-tuning-for-vllm-cpu)

First of all, please make sure the thread-binding and KV cache space are properly set and take effect. You can check the thread-binding by running a vLLM benchmark and observing CPU cores usage via `htop`

.

Use multiples of 32 as `--block-size`

, which is 128 by default.

Inference batch size is an important parameter for the performance. A larger batch usually provides higher throughput, a smaller batch provides lower latency. Tuning the max batch size starting from the default value to balance throughput and latency is an effective way to improve vLLM CPU performance on specific platforms. There are two important related parameters in vLLM:

`--max-num-batched-tokens`

, defines the limit of token numbers in a single batch, has more impacts on the first token performance. The default value is set as:- Offline Inference:
`4096 * world_size`

- Online Serving:
`2048 * world_size`


- Offline Inference:
`--max-num-seqs`

, defines the limit of sequence numbers in a single batch, has more impacts on the output token performance.- Offline Inference:
`256 * world_size`

- Online Serving:
`128 * world_size`


- Offline Inference:

vLLM CPU supports data parallel (DP), tensor parallel (TP) and pipeline parallel (PP) to leverage multiple CPU sockets and memory nodes. For more details of tuning DP, TP and PP, please refer to [Optimization and Tuning](https://docs.vllm.ai/configuration/optimization/). For vLLM CPU, it is recommended to use DP, TP and PP together if there are enough CPU sockets and memory nodes.

### Which quantization configs does vLLM CPU support?[¶](https://docs.vllm.ai#which-quantization-configs-does-vllm-cpu-support)

- vLLM CPU supports quantizations:
- AWQ (x86, s390x)
- GPTQ (x86, s390x)
- compressed-tensor INT8 W8A8 (x86, s390x only)


### Why do I see `get_mempolicy: Operation not permitted`

when running in Docker?[¶](https://docs.vllm.ai#why-do-i-see-get_mempolicy-operation-not-permitted-when-running-in-docker)

In some container environments (like Docker), NUMA-related syscalls used by vLLM (e.g., `get_mempolicy`

, `migrate_pages`

) are blocked/denied in the runtime's default seccomp/capabilities settings. This may lead to warnings like `get_mempolicy: Operation not permitted`

. Functionality is not affected, but NUMA memory binding/migration optimizations may not take effect and performance can be suboptimal.

To enable these optimizations inside Docker with the least privilege, you can follow below tips:

docker run ... --cap-add SYS_NICE --security-opt seccomp=unconfined ...
# 1) `--cap-add SYS_NICE` is to address `get_mempolicy` EPERM issue.
# 2) `--security-opt seccomp=unconfined` is to enable `migrate_pages` for `numa_migrate_pages()`.
# Actually, `seccomp=unconfined` bypasses the seccomp for container,
# if it's unacceptable, you can customize your own seccomp profile,
# based on docker/runtime default.json and add `migrate_pages` to `SCMP_ACT_ALLOW` list.
# reference : https://docs.docker.com/engine/security/seccomp/


Alternatively, running with `--privileged=true`

also works but is broader and not generally recommended.

In K8S, the following configuration can be added to workload yaml to achieve the same effect as above: