source: https://rocm.docs.amd.com/en/latest/install/docker-containers.html

# Run ROCm Docker containers[#](https://rocm.docs.amd.com#run-rocm-docker-containers)

Docker is a popular way to run ROCm workloads in a consistent, reproducible environment. There are two ways to expose AMD GPUs to Docker containers:

[AMD Container Runtime Toolkit](https://rocm.docs.amd.com#docker-with-toolkit)— simplifies GPU access within Docker environments, enhances device discovery, and enables better integration with modern container technologies.[Manual Docker device passthrough](https://rocm.docs.amd.com#docker-manual)— passes GPU device nodes directly to the container with`--device`

. No toolkit required.

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

Regardless of which approach you use, the following are required on the host system:

On Linux, the AMD GPU driver (

`amdgpu-dkms`

). See[Install AMD ROCm 10.0.0](https://rocm.docs.amd.com/rocm.html)for driver installation guidance for your environment.

## With the AMD Container Runtime Toolkit[#](https://rocm.docs.amd.com#with-the-amd-container-runtime-toolkit)

The [AMD Container Runtime Toolkit](https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/overview.html)
provides two mechanisms for GPU injection: CDI (recommended) and the
amd-container-runtime. Both require installing the toolkit first.

Install the toolkit by following the

[Quick Start Guide (AMD Container Runtime Toolkit docs)](https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/quick-start-guide.html).See

[Running Workloads (AMD Container Runtime Toolkit docs)](https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/running-workloads.html)to get started running containerized ROCm applications on AMD GPUs.

## Without the AMD Container Runtime Toolkit[#](https://rocm.docs.amd.com#without-the-amd-container-runtime-toolkit)

If you prefer not to install the AMD Container Runtime Toolkit, or you’re using older
versions of Docker Engine, you can pass GPU device nodes directly to the
container using Docker’s `--device`

flag. This approach requires no
additional software beyond Docker.

```
docker run -it --rm \
--device /dev/kfd \
--device /dev/dri \
--security-opt seccomp=unconfined \
<image>
```

The purpose of each option:

`--device /dev/kfd`

The main compute interface, shared by all GPUs.

`--device /dev/dri`

Contains the Direct Rendering Interface (DRI) device nodes for each GPU. Passing the whole directory grants access to all GPUs. To restrict access to specific GPUs, see

[Restricting GPU access](https://rocm.docs.amd.com#docker-restrict-gpus).`--security-opt seccomp=unconfined`

(optional)Enables memory mapping. Recommended for HPC workloads that use

`numactl`

for GPU/CPU affinity mappings. See[Optional security options (Docker docs)](https://docs.docker.com/reference/cli/docker/container/run/#security-opt).

### Restricting GPU access[#](https://rocm.docs.amd.com#restricting-gpu-access)

Tip

[AMD Container Runtime Toolkit](https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/overview.html)
simplifies GPU selection, removing the need to manually map the render
nodes. This is recommended if your use case needs fine-grained GPU
selection. See [Running Workloads (AMD Container Toolkit Runtime docs)](https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/running-workloads.html#running-workloads)
for more information.

By default, `--device /dev/dri`

grants access to all GPUs on the system.
To limit a container to specific GPUs, pass their individual render nodes instead.

List available render nodes on the host:

```
ls /dev/dri/render*
```

GPU render nodes are typically named `renderD128`

, `renderD129`

, and so on.
Pass them individually alongside `/dev/kfd`

:

```
docker run --device /dev/kfd \
--device /dev/dri/renderD128 \
--device /dev/dri/renderD129 \
<image>
```

Note

When GPUs are partitioned (for example, an Instinct MI300X or MI350X in DPX, QPX,
or CPX mode), each partition appears as a separate render node. In CPX mode,
`renderD128`

through `renderD136`

are partitions of the first physical GPU,
and `renderD137`

is the second GPU. Account for this when selecting render nodes.
See [GPU partitioning](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/overview.html)
for details.

## Docker Compose[#](https://rocm.docs.amd.com#docker-compose)

Docker Compose can simplify complex Docker invocations. See [Docker Compose
usage](https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/docker-compose.html)
for AMD Container Toolkit configuration examples.

For manual Docker device passthrough, use the `devices`

key in your Compose file:

```
services:
myapp:
image: <image>
devices:
- /dev/kfd
- /dev/dri
```

## Verifying GPU access[#](https://rocm.docs.amd.com#verifying-gpu-access)

Inside any container with ROCm installed, `rocminfo`

and `amd-smi list`

enumerate only the GPUs passed into that container. On the host, they enumerate
all ROCm-capable GPUs.

[rocminfo](https://rocm.docs.amd.com/projects/rocminfo/en/latest/index.html) and [amd-smi](https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html) are provided
by the ROCm Core SDK. Run either tool to confirm the expected GPUs are
visible.

## Docker images[#](https://rocm.docs.amd.com#docker-images)

The [ROCm Docker repository](https://github.com/ROCm/ROCm-docker) hosts Dockerfiles
for building ROCm-capable containers. Pre-built images are available on
[Docker Hub](https://hub.docker.com/u/rocm):

`rocm/rocm-terminal`

— minimal image with prerequisites to build HIP applications, without any libraries.[ROCm dev images](https://hub.docker.com/u/rocm?page=1&search=dev-)— a variety of OS and ROCm version combinations, suitable as a base for building applications.The ROCm

[AI ecosystem](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/)provides Docker images for popular inference frameworks.