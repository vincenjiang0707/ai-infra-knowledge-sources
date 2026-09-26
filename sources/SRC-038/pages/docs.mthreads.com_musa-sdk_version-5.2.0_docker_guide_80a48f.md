source: https://docs.mthreads.com/musa-sdk/version-5.2.0/docker_guide

# 使用 Docker 进行 MUSA 开发

MUSA SDK 5.2.0 提供面向 Ubuntu 22.04 的官方分层容器镜像。镜像内已通过 APT 安装对应版本的 MUSA 组件，适合在容器中编译、运行和部署 MUSA 程序。推荐直接拉取官方镜像；如需定制构建，可使用[文末折叠的 Dockerfile](https://docs.mthreads.com#dockerfile)自行构建。

容器默认不包含 GPU 驱动，宿主机必须先安装兼容 MUSA SDK 5.2.0 的 Linux Driver。

如果您更希望直接在宿主机安装 MUSA SDK，请参见[安装指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/install_guide)。

## 前置条件[](https://docs.mthreads.com#前置条件)

**宿主机驱动**：已按[安装指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/install_guide)安装兼容 MUSA SDK 5.2.0 的 Linux Driver，并确认`mthreads-gmi`

可正常显示 GPU。**Docker**：宿主机已安装 Docker Engine，当前用户可执行`docker`

命令。**GPU 透传**：推荐安装[MT Container Toolkit](https://docs.mthreads.com/cloud-native/cloud-native-doc-online/install_guide/container_install)，以便容器自动获得设备节点和用户态驱动库。未安装时，需要手动挂载设备并映射`/usr/lib/x86_64-linux-gnu/libmusa.so*`

。

## 拉取官方镜像[](https://docs.mthreads.com#拉取官方镜像)

推荐直接从官方镜像仓库拉取，不必本地构建：

`docker pull registry.mthreads.com/mcconline/musa_sdk:5.2.0-base-ubuntu22.04-s5000`

docker pull registry.mthreads.com/mcconline/musa_sdk:5.2.0-runtime-ubuntu22.04-s5000

docker pull registry.mthreads.com/mcconline/musa_sdk:5.2.0-devel-ubuntu22.04-s5000



| 镜像 | 标签 |
|---|---|
`base` | `registry.mthreads.com/mcconline/musa_sdk:5.2.0-base-ubuntu22.04-s5000` |
`runtime` | `registry.mthreads.com/mcconline/musa_sdk:5.2.0-runtime-ubuntu22.04-s5000` |
`devel` | `registry.mthreads.com/mcconline/musa_sdk:5.2.0-devel-ubuntu22.04-s5000` |

开发请使用 `devel`

；只运行已编译程序时使用 `runtime`

。拉取后可执行 `docker images | grep musa_sdk`

确认镜像已在本地。

## 镜像分层[](https://docs.mthreads.com#镜像分层)

三层镜像按用途拆分，后一层继承前一层：

| 镜像 | 基础镜像 | 适用场景 |
|---|---|---|
`base` | `ubuntu:22.04` | 最小运行底座，仅包含 MUSA Runtime 与 Toolkit 公共配置 |
`runtime` | `base` | 运行已编译程序，包含数学库、muDNN、MCCL、MTML 等运行时库 |
`devel` | `runtime` | 容器内开发与构建，额外提供编译器、头文件、静态库和性能分析工具 |

当前镜像面向 **amd64**、**Ubuntu 22.04** 和 **MTT S5000（PH1）**。`runtime`

与 `devel`

中的通信库安装的是 `mccl-s5000`

，不适用于其他 GPU 代际。

### base[](https://docs.mthreads.com#base)

`base`

配置 MUSA APT 源�后安装：

| 软件包 | 版本 |
|---|---|
`musa-musart-5-2` | 5.2.0 |
`musa-toolkit-5-2-config-common` | 5.2.0 |

默认环境变量：

`export PATH=/usr/local/musa/bin:${PATH}`

export LD_LIBRARY_PATH=/usr/local/musa/lib:${LD_LIBRARY_PATH}



`runtime`

和 `devel`

继承上述环境变量，无需重复配置。

### runtime[](https://docs.mthreads.com#runtime)

`runtime`

在 `base`

之上安装运行态共享库：

| 软件包 | 版本 | 说明 |
|---|---|---|
`libmublas-5-2` | 1.13.0 | muBLAS |
`libmufft-5-2` | 1.12.0 | muFFT |
`libmurand-5-2` | 1.3.0 | muRAND |
`libmusolver-5-2` | 1.6.0 | muSOLVER |
`libmusparse-5-2` | 1.7.0 | muSPARSE |
`libmupp-5-2` | 1.13.0 | muPP |
`libmublaslt-5-2` | 1.13.0 | muBLASLt |
`libmtjpeg-5-2` | 1.0.5 | JPEG |
`libmudnn3-musa-5-2` | 3.4.0.0 | muDNN |
`musa-toolkit-cmake-5-2` | 5.2.0 | CMake 模块 |
`libmthreads-mtml` | 2.4.2 | MTML |
`mccl-s5000` | 2.4.0 | MCCL（S5000） |

### devel[](https://docs.mthreads.com#devel)

`devel`

只安装开发增量，不重复安装 `runtime`

中的同名运行时包。

开发工具：

| 软件包 | 版本 | 说明 |
|---|---|---|
`mtcc-5-2` | 5.2.0 | `mcc` 编译器 |
`moore-perf-system` | 1.8.0 | Moore Perf System |
`moore-perf-compute` | 1.3.0 | Moore Perf Compute |
`musify-5-2` | 1.3.0 | MUSIFY |
`musa-mapping-5-2` | 5.2.0 | MUSA Mapping |
`musa-mupti-5-2` | 1.3.0 | muPTI |

开发包（头文件与静态库）：

| 软件包 | 版本 |
|---|---|
`musa-mupti-dev-5-2` | 1.3.0 |
`musa-musart-dev-5-2` | 5.2.0 |
`libmublas-dev-5-2` | 1.13.0 |
`libmufft-dev-5-2` | 1.12.0 |
`libmurand-dev-5-2` | 1.3.0 |
`libmusolver-dev-5-2` | 1.6.0 |
`libmusparse-dev-5-2` | 1.7.0 |
`libmupp-dev-5-2` | 1.13.0 |
`libmublaslt-dev-5-2` | 1.13.0 |
`libmtjpeg-dev-5-2` | 1.0.5 |
`libmthreads-mtml-dev` | 2.4.2 |
`libmudnn3-dev-musa-5-2` | 3.4.0.0 |
`mccl-s5000-dev` | 2.4.0 |

镜像默认不包含以下组件，如需使用请在容器内按[安装指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/install_guide)另行安装：

- Torch-MUSA、Triton-MUSA、TileLang-MUSA、MATE
`deep-ep`

、`mtshmem`

- 容器内 GPU 驱动（DDK）

## 启动容器[](https://docs.mthreads.com#启动容器)

### 推荐：通过 Container Toolkit 启动[](https://docs.mthreads.com#推荐通过-container-toolkit-启动)

已安装 [MT Container Toolkit](https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/container_guide) 时，用环境变量把 GPU 和计算能力透传进容器：

`docker run --rm -it \`

-e MTHREADS_VISIBLE_DEVICES=all \

-e MTHREADS_DRIVER_CAPABILITIES=compute,utility \

--shm-size=16g \

-v "$PWD":/workspace \

-w /workspace \

registry.mthreads.com/mcconline/musa_sdk:5.2.0-devel-ubuntu22.04-s5000 \

bash



常用参数说明：

| 参数 | 说明 |
|---|---|
`MTHREADS_VISIBLE_DEVICES` | 指定可见 GPU，例如 `all` 、`0` 或 `0,1` |
`MTHREADS_DRIVER_CAPABILITIES` | 开发场景建议至少包含 `compute,utility` |
`--shm-size` | 容器内使用 MCCL 时建议增大共享内存 |
`-v` / `-w` | 挂载宿主机代码目录，并设为容器工作目录 |

只使用部分 GPU 时：

`docker run --rm -it \`

-e MTHREADS_VISIBLE_DEVICES=0 \

-e MTHREADS_DRIVER_CAPABILITIES=compute,utility \

-v "$PWD":/workspace \

-w /workspace \

registry.mthreads.com/mcconline/musa_sdk:5.2.0-devel-ubuntu22.04-s5000 \

bash



### 备选：手动挂载设备[](https://docs.mthreads.com#备选手动挂载设备)

未安装 Container Toolkit 时，需要手动挂载 GPU 设备，并把宿主机用户态驱动库映射进容器：

`docker run --rm -it \`

--device /dev/mtgpu0 \

--device /dev/dri \

-v /usr/lib/x86_64-linux-gnu/libmusa.so.1:/usr/lib/x86_64-linux-gnu/libmusa.so.1 \

--shm-size=16g \

-v "$PWD":/workspace \

-w /workspace \

registry.mthreads.com/mcconline/musa_sdk:5.2.0-devel-ubuntu22.04-s5000 \

bash



请按宿主机实际设备节点调整 `--device`

。多卡环境需要挂载对应的 `/dev/mtgpu*`

。

## 在容器中进行 MUSA 开发[](https://docs.mthreads.com#在容器中进行-musa-开发)

进入 `devel`

容器后，先确认工具链和设备可用：

`musa_version_query`

which mcc

ls /usr/local/musa/include

musaInfo



`musa_version_query`

中的 `musa_toolkits`

、`mcc`

、`musa_runtime`

版本应为 `5.2.0`

。`musaInfo`

应能列出宿主机上的 MTT S5000 设备。

### 编译并运行示例[](https://docs.mthreads.com#编译并运行示例)

以下示例与[快速开始](https://docs.mthreads.com/musa-sdk/version-5.2.0/programming_guide/getting_started_first_kernel)一致。在已挂载的工作目录中创建 `vectorAdd.mu`

后执行：

`mcc vectorAdd.mu -lmusart -L/usr/local/musa/lib -o vectorAdd`

./vectorAdd



多文件项目可以使用 CMake。`devel`

与 `runtime`

已安装 `musa-toolkit-cmake-5-2`

：

`cmake_minimum_required(VERSION 3.10)`

project(VectorAdd LANGUAGES CXX)


list(APPEND CMAKE_MODULE_PATH /usr/local/musa/cmake)

find_package(MUSA REQUIRED)


musa_add_executable(vectorAdd vectorAdd.mu)



`mkdir build && cd build`

cmake ..

make

./vectorAdd



### 选择镜像[](https://docs.mthreads.com#选择镜像)

| 任务 | 推荐镜像 |
|---|---|
| 编写、编译、调试 MUSA 程序 | `devel` |
| 使用 Moore Perf、MUSIFY、muPTI 做性能分析 | `devel` |
| 运行已编译的可执行文件 | `runtime` |
| 自定义更精简的业务镜像 | 以 `base` 或 `runtime` 为父镜像继续构建 |

基于 `runtime`

打包业务程序时，可把宿主机或 `devel`

容器中编译好的二进制复制进镜像：

`FROM registry.mthreads.com/mcconline/musa_sdk:5.2.0-runtime-ubuntu22.04-s5000`


WORKDIR /opt/app

COPY vectorAdd /opt/app/vectorAdd

CMD ["./vectorAdd"]



## 自行构建镜像[](https://docs.mthreads.com#self-build)

大多数��场景直接拉取官方镜像即可。仅在无法访问镜像仓库、需要锁定构建过程，或要基于官方 Dockerfile 定制时，才需要本地构建。

构建环境需要访问 `https://dl.mthreads.com/`

，以便安装 `musa-repo-jammy`

与各 APT 软件包。默认 APT 配置包：

`https://dl.mthreads.com/repo/repository/ubuntu2204/pool/jammy/amd64/musa-repo-jammy_1.0.0.11-1_all.deb`



### 准备 Dockerfile[](https://docs.mthreads.com#准备-dockerfile)

在工作目录中创建构建目录，并将下文折叠区域中的内容分别保存为三个文件：

`mkdir -p musa-sdk-5.2.0-docker`

cd musa-sdk-5.2.0-docker



| 文件名 | 对应镜像 |
|---|---|
`Dockerfile.base` | `base` |
`Dockerfile.runtime` | `runtime` |
`Dockerfile.devel` | `devel` |

`runtime`

的 `FROM`

指向 `base`

镜像，`devel`

的 `FROM`

指向 `runtime`

镜像。请按 `base`

→ `runtime`

→ `devel`

的顺序构建，并为本地镜像打上与 `FROM`

完全一致的标签，这样下一层构建会直接复用本机刚构建的镜像。

### 构建命令[](https://docs.mthreads.com#构建命令)

`docker build \`

-f Dockerfile.base \

-t registry.mthreads.com/mcconline/musa_sdk:5.2.0-base-ubuntu22.04-s5000 \

.



`base`

的默认 APT 源可通过构建参数覆盖：

`docker build \`

-f Dockerfile.base \

--build-arg MUSA_REPO_DEB_URL=https://dl.mthreads.com/repo/repository/ubuntu2204/pool/jammy/amd64/musa-repo-jammy_1.0.0.11-1_all.deb \

-t registry.mthreads.com/mcconline/musa_sdk:5.2.0-base-ubuntu22.04-s5000 \

.



`docker build \`

-f Dockerfile.runtime \

-t registry.mthreads.com/mcconline/musa_sdk:5.2.0-runtime-ubuntu22.04-s5000 \

.



`docker build \`

-f Dockerfile.devel \

-t registry.mthreads.com/mcconline/musa_sdk:5.2.0-devel-ubuntu22.04-s5000 \

.



构建完成后确认镜像：

`docker images | grep musa_sdk`



这些 Dockerfile 不从构建上下文复制源码，上下文可以是当前空目录。

### Dockerfile[](https://docs.mthreads.com#dockerfile)

## Dockerfile.base

`FROM ubuntu:22.04 AS base`


ENV MUSA_MUSART_PACKAGE_NAME=musa-musart-5-2

ENV MUSA_MUSART_VERSION=5.2.0

ENV MUSA_MUSART_PACKAGE=${MUSA_MUSART_PACKAGE_NAME}=${MUSA_MUSART_VERSION}

ENV MUSA_CONFIG_COMMON_PACKAGE_NAME=musa-toolkit-5-2-config-common

ENV MUSA_CONFIG_COMMON_VERSION=5.2.0

ENV MUSA_CONFIG_COMMON_PACKAGE=${MUSA_CONFIG_COMMON_PACKAGE_NAME}=${MUSA_CONFIG_COMMON_VERSION}


LABEL maintainer="Moore Threads <developers@mthreads.com>"


ARG MUSA_REPO_DEB_URL=https://dl.mthreads.com/repo/repository/ubuntu2204/pool/jammy/amd64/musa-repo-jammy_1.0.0.11-1_all.deb

ARG BASE_PACKAGES="ca-certificates wget"


RUN rm -f /etc/apt/apt.conf.d/20packagekit /etc/apt/apt.conf.d/docker-clean \

&& apt-get update \

&& apt-get install -y --no-install-recommends ${BASE_PACKAGES} \

&& wget -O /tmp/musa-repo.deb "${MUSA_REPO_DEB_URL}" \

&& dpkg -i /tmp/musa-repo.deb \

&& apt-get update \

&& apt-get install -y --no-install-recommends \

${MUSA_MUSART_PACKAGE} \

${MUSA_CONFIG_COMMON_PACKAGE} \

&& rm -f /tmp/musa-repo.deb \

&& rm -rf /var/lib/apt/lists/*


ENV PATH=/usr/local/musa/bin:${PATH}

ENV LD_LIBRARY_PATH=/usr/local/musa/lib:${LD_LIBRARY_PATH}



## Dockerfile.runtime

`FROM registry.mthreads.com/mcconline/musa_sdk:5.2.0-base-ubuntu22.04-s5000 AS base`


ENV MUSA_BLAS_PACKAGE_NAME=libmublas-5-2

ENV MUSA_BLAS_VERSION=1.13.0

ENV MUSA_BLAS_PACKAGE=${MUSA_BLAS_PACKAGE_NAME}=${MUSA_BLAS_VERSION}

ENV MUSA_FFT_PACKAGE_NAME=libmufft-5-2

ENV MUSA_FFT_VERSION=1.12.0

ENV MUSA_FFT_PACKAGE=${MUSA_FFT_PACKAGE_NAME}=${MUSA_FFT_VERSION}

ENV MUSA_RAND_PACKAGE_NAME=libmurand-5-2

ENV MUSA_RAND_VERSION=1.3.0

ENV MUSA_RAND_PACKAGE=${MUSA_RAND_PACKAGE_NAME}=${MUSA_RAND_VERSION}

ENV MUSA_SOLVER_PACKAGE_NAME=libmusolver-5-2

ENV MUSA_SOLVER_VERSION=1.6.0

ENV MUSA_SOLVER_PACKAGE=${MUSA_SOLVER_PACKAGE_NAME}=${MUSA_SOLVER_VERSION}

ENV MUSA_SPARSE_PACKAGE_NAME=libmusparse-5-2

ENV MUSA_SPARSE_VERSION=1.7.0

ENV MUSA_SPARSE_PACKAGE=${MUSA_SPARSE_PACKAGE_NAME}=${MUSA_SPARSE_VERSION}

ENV MUSA_PP_PACKAGE_NAME=libmupp-5-2

ENV MUSA_PP_VERSION=1.13.0

ENV MUSA_PP_PACKAGE=${MUSA_PP_PACKAGE_NAME}=${MUSA_PP_VERSION}

ENV MUSA_BLASLT_PACKAGE_NAME=libmublaslt-5-2

ENV MUSA_BLASLT_VERSION=1.13.0

ENV MUSA_BLASLT_PACKAGE=${MUSA_BLASLT_PACKAGE_NAME}=${MUSA_BLASLT_VERSION}

ENV MUSA_MTJPEG_PACKAGE_NAME=libmtjpeg-5-2

ENV MUSA_MTJPEG_VERSION=1.0.5

ENV MUSA_MTJPEG_PACKAGE=${MUSA_MTJPEG_PACKAGE_NAME}=${MUSA_MTJPEG_VERSION}

ENV MUSA_MUDNN_PACKAGE_NAME=libmudnn3-musa-5-2

ENV MUSA_MUDNN_VERSION=3.4.0.0

ENV MUSA_MUDNN_PACKAGE=${MUSA_MUDNN_PACKAGE_NAME}=${MUSA_MUDNN_VERSION}

ENV MUSA_CMAKE_PACKAGE_NAME=musa-toolkit-cmake-5-2

ENV MUSA_CMAKE_VERSION=5.2.0

ENV MUSA_CMAKE_PACKAGE=${MUSA_CMAKE_PACKAGE_NAME}=${MUSA_CMAKE_VERSION}

ENV MUSA_MTML_PACKAGE_NAME=libmthreads-mtml

ENV MUSA_MTML_VERSION=2.4.2

ENV MUSA_MTML_PACKAGE=${MUSA_MTML_PACKAGE_NAME}=${MUSA_MTML_VERSION}

ENV MUSA_MCCL_PACKAGE_NAME=mccl-s5000

ENV MUSA_MCCL_VERSION=2.4.0

ENV MUSA_MCCL_PACKAGE=${MUSA_MCCL_PACKAGE_NAME}=${MUSA_MCCL_VERSION}


LABEL maintainer="Moore Threads <developers@mthreads.com>"


RUN rm -f /etc/apt/apt.conf.d/20packagekit /etc/apt/apt.conf.d/docker-clean \

&& apt-get update \

&& apt-get install -y --no-install-recommends \

${MUSA_BLAS_PACKAGE} \

${MUSA_FFT_PACKAGE} \

${MUSA_RAND_PACKAGE} \

${MUSA_SOLVER_PACKAGE} \

${MUSA_SPARSE_PACKAGE} \

${MUSA_PP_PACKAGE} \

${MUSA_BLASLT_PACKAGE} \

${MUSA_MTJPEG_PACKAGE} \

${MUSA_MUDNN_PACKAGE} \

${MUSA_CMAKE_PACKAGE} \

${MUSA_MTML_PACKAGE} \

${MUSA_MCCL_PACKAGE} \

&& rm -rf /var/lib/apt/lists/*



## Dockerfile.devel

`FROM registry.mthreads.com/mcconline/musa_sdk:5.2.0-runtime-ubuntu22.04-s5000 AS base`


ENV MUSA_MTCC_PACKAGE_NAME=mtcc-5-2

ENV MUSA_MTCC_VERSION=5.2.0

ENV MUSA_MTCC_PACKAGE=${MUSA_MTCC_PACKAGE_NAME}=${MUSA_MTCC_VERSION}

ENV MUSA_PERF_SYSTEM_PACKAGE_NAME=moore-perf-system

ENV MUSA_PERF_SYSTEM_VERSION=1.8.0

ENV MUSA_PERF_SYSTEM_PACKAGE=${MUSA_PERF_SYSTEM_PACKAGE_NAME}=${MUSA_PERF_SYSTEM_VERSION}

ENV MUSA_PERF_COMPUTE_PACKAGE_NAME=moore-perf-compute

ENV MUSA_PERF_COMPUTE_VERSION=1.3.0

ENV MUSA_PERF_COMPUTE_PACKAGE=${MUSA_PERF_COMPUTE_PACKAGE_NAME}=${MUSA_PERF_COMPUTE_VERSION}

ENV MUSA_MUSIFY_PACKAGE_NAME=musify-5-2

ENV MUSA_MUSIFY_VERSION=1.3.0

ENV MUSA_MUSIFY_PACKAGE=${MUSA_MUSIFY_PACKAGE_NAME}=${MUSA_MUSIFY_VERSION}

ENV MUSA_MAPPING_PACKAGE_NAME=musa-mapping-5-2

ENV MUSA_MAPPING_VERSION=5.2.0

ENV MUSA_MAPPING_PACKAGE=${MUSA_MAPPING_PACKAGE_NAME}=${MUSA_MAPPING_VERSION}

ENV MUSA_MUPTI_PACKAGE_NAME=musa-mupti-5-2

ENV MUSA_MUPTI_VERSION=1.3.0

ENV MUSA_MUPTI_PACKAGE=${MUSA_MUPTI_PACKAGE_NAME}=${MUSA_MUPTI_VERSION}

ENV MUSA_MUPTI_DEV_PACKAGE_NAME=musa-mupti-dev-5-2

ENV MUSA_MUPTI_DEV_VERSION=1.3.0

ENV MUSA_MUPTI_DEV_PACKAGE=${MUSA_MUPTI_DEV_PACKAGE_NAME}=${MUSA_MUPTI_DEV_VERSION}

ENV MUSA_MUSART_DEV_PACKAGE_NAME=musa-musart-dev-5-2

ENV MUSA_MUSART_DEV_VERSION=5.2.0

ENV MUSA_MUSART_DEV_PACKAGE=${MUSA_MUSART_DEV_PACKAGE_NAME}=${MUSA_MUSART_DEV_VERSION}

ENV MUSA_BLAS_DEV_PACKAGE_NAME=libmublas-dev-5-2

ENV MUSA_BLAS_DEV_VERSION=1.13.0

ENV MUSA_BLAS_DEV_PACKAGE=${MUSA_BLAS_DEV_PACKAGE_NAME}=${MUSA_BLAS_DEV_VERSION}

ENV MUSA_FFT_DEV_PACKAGE_NAME=libmufft-dev-5-2

ENV MUSA_FFT_DEV_VERSION=1.12.0

ENV MUSA_FFT_DEV_PACKAGE=${MUSA_FFT_DEV_PACKAGE_NAME}=${MUSA_FFT_DEV_VERSION}

ENV MUSA_RAND_DEV_PACKAGE_NAME=libmurand-dev-5-2

ENV MUSA_RAND_DEV_VERSION=1.3.0

ENV MUSA_RAND_DEV_PACKAGE=${MUSA_RAND_DEV_PACKAGE_NAME}=${MUSA_RAND_DEV_VERSION}

ENV MUSA_SOLVER_DEV_PACKAGE_NAME=libmusolver-dev-5-2

ENV MUSA_SOLVER_DEV_VERSION=1.6.0

ENV MUSA_SOLVER_DEV_PACKAGE=${MUSA_SOLVER_DEV_PACKAGE_NAME}=${MUSA_SOLVER_DEV_VERSION}

ENV MUSA_SPARSE_DEV_PACKAGE_NAME=libmusparse-dev-5-2

ENV MUSA_SPARSE_DEV_VERSION=1.7.0

ENV MUSA_SPARSE_DEV_PACKAGE=${MUSA_SPARSE_DEV_PACKAGE_NAME}=${MUSA_SPARSE_DEV_VERSION}

ENV MUSA_PP_DEV_PACKAGE_NAME=libmupp-dev-5-2

ENV MUSA_PP_DEV_VERSION=1.13.0

ENV MUSA_PP_DEV_PACKAGE=${MUSA_PP_DEV_PACKAGE_NAME}=${MUSA_PP_DEV_VERSION}

ENV MUSA_BLASLT_DEV_PACKAGE_NAME=libmublaslt-dev-5-2

ENV MUSA_BLASLT_DEV_VERSION=1.13.0

ENV MUSA_BLASLT_DEV_PACKAGE=${MUSA_BLASLT_DEV_PACKAGE_NAME}=${MUSA_BLASLT_DEV_VERSION}

ENV MUSA_MTJPEG_DEV_PACKAGE_NAME=libmtjpeg-dev-5-2

ENV MUSA_MTJPEG_DEV_VERSION=1.0.5

ENV MUSA_MTJPEG_DEV_PACKAGE=${MUSA_MTJPEG_DEV_PACKAGE_NAME}=${MUSA_MTJPEG_DEV_VERSION}

ENV MUSA_MTML_DEV_PACKAGE_NAME=libmthreads-mtml-dev

ENV MUSA_MTML_DEV_VERSION=2.4.2

ENV MUSA_MTML_DEV_PACKAGE=${MUSA_MTML_DEV_PACKAGE_NAME}=${MUSA_MTML_DEV_VERSION}

ENV MUSA_MUDNN_DEV_PACKAGE_NAME=libmudnn3-dev-musa-5-2

ENV MUSA_MUDNN_DEV_VERSION=3.4.0.0

ENV MUSA_MUDNN_DEV_PACKAGE=${MUSA_MUDNN_DEV_PACKAGE_NAME}=${MUSA_MUDNN_DEV_VERSION}

ENV MUSA_MCCL_DEV_PACKAGE_NAME=mccl-s5000-dev

ENV MUSA_MCCL_DEV_VERSION=2.4.0

ENV MUSA_MCCL_DEV_PACKAGE=${MUSA_MCCL_DEV_PACKAGE_NAME}=${MUSA_MCCL_DEV_VERSION}


LABEL maintainer="Moore Threads <developers@mthreads.com>"


RUN rm -f /etc/apt/apt.conf.d/20packagekit /etc/apt/apt.conf.d/docker-clean \

&& apt-get update \

&& apt-get install -y --no-install-recommends \

${MUSA_MTCC_PACKAGE} \

${MUSA_PERF_SYSTEM_PACKAGE} \

${MUSA_PERF_COMPUTE_PACKAGE} \

${MUSA_MUSIFY_PACKAGE} \

${MUSA_MAPPING_PACKAGE} \

${MUSA_MUPTI_PACKAGE} \

${MUSA_MUPTI_DEV_PACKAGE} \

${MUSA_MUSART_DEV_PACKAGE} \

${MUSA_BLAS_DEV_PACKAGE} \

${MUSA_FFT_DEV_PACKAGE} \

${MUSA_RAND_DEV_PACKAGE} \

${MUSA_SOLVER_DEV_PACKAGE} \

${MUSA_SPARSE_DEV_PACKAGE} \

${MUSA_PP_DEV_PACKAGE} \

${MUSA_BLASLT_DEV_PACKAGE} \

${MUSA_MTJPEG_DEV_PACKAGE} \

${MUSA_MTML_DEV_PACKAGE} \

${MUSA_MUDNN_DEV_PACKAGE} \

${MUSA_MCCL_DEV_PACKAGE} \

&& rm -rf /var/lib/apt/lists/*



## 注意事项[](https://docs.mthreads.com#注意事项)

- 容器不包含 DDK。升级或重装宿主机驱动后，请重启容器，使容器内看到新的驱动库。
`base`

只有最小 Runtime，不能替代`runtime`

或`devel`

。- 当前镜像只安装
`mccl-s5000`

，面向 MTT S5000。S4000 等其他型号不在默认范围内。 - 自行构建时，构建机需要访问
`https://dl.mthreads.com/`

。如使用内网镜像源，请通过`MUSA_REPO_DEB_URL`

覆盖`base`

的 APT 配置包地址。 - 使用 MCCL 时，建议设置足够的
`--shm-size`

，并保证容器能访问正确的网络接口和`/sys`

拓扑。更多说明见[MCCL](https://docs.mthreads.com/musa-sdk/version-5.2.0/07_libraries/04_mccl/)。 - 镜像内如需 Torch-MUSA、Triton-MUSA 等 Python 组件，请按
[安装指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/install_guide)配置 PyPI 源后再安装。

## 常见问题[](https://docs.mthreads.com#常见问题)

## 构建 runtime 或 devel 时提示找不到基础镜像怎么办？

`runtime`

和 `devel`

的 `FROM`

使用固定标签。请先按本文构建 `base`

，再构建 `runtime`

，最后构建 `devel`

，并保证本地标签与 Dockerfile 中的 `FROM`

完全一致。也可以先 `docker pull`

对应的已发布镜像。

## 容器内 `musaInfo`

或程序无法看到 GPU 怎么办？

- 在宿主机执行
`mthreads-gmi`

，确认驱动已加载。 - 优先使用 MT Container Toolkit，并设置
`MTHREADS_VISIBLE_DEVICES`

。 - 未使用 Toolkit 时，检查
`--device`

是否挂载了`/dev/mtgpu*`

，以及是否映射了宿主机的`libmusa.so*`

。 - 升级宿主机驱动后，重启容器。

## 容器内找不到 `mcc`

怎么办？

`mcc`

只包含在 `devel`

镜像中。请确认启动的是 `5.2.0-devel-ubuntu22.04-s5000`

，而不是 `base`

或 `runtime`

。

## 为什么容器里没有 Triton、TileLang 或 Torch-MUSA？

当前 5.2.0 分层镜像只覆盖 MUSA Toolkit、数学库、muDNN、MCCL 和开发工具链。Python 生态组件需要在容器内按[安装指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/install_guide)另行安装。