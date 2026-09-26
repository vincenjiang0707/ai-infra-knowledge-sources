source: https://rocm.docs.amd.com/en/latest/reference/system-optimization/gpu-isolation.html

# GPU isolation techniques[#](https://rocm.docs.amd.com#gpu-isolation-techniques)

Restricting the access of applications to a subset of GPUs, aka isolating GPUs allows users to hide GPU resources from programs. The programs by default will only use the “exposed” GPUs ignoring other (hidden) GPUs in the system.

There are multiple ways to achieve isolation of GPUs in the ROCm software stack, differing in which applications they apply to and the security they provide. This page serves as an overview of the techniques.

## Environment variables[#](https://rocm.docs.amd.com#environment-variables)

The runtimes in the ROCm software stack read these environment variables to
select the exposed or default device to present to applications using them.
See [ROCm environment variables](https://rocm.docs.amd.com/environment-variables/index.html#env-variables-reference) for more information.

Environment variables shouldn’t be used for isolating untrusted applications, as an application can reset them before initializing the runtime.

`ROCR_VISIBLE_DEVICES`

[#](https://rocm.docs.amd.com#rocr-visible-devices)

A list of device indices or UUIDs that will be exposed to applications.

Runtime : ROCm Software Runtime. Applies to all applications using the user mode ROCm software stack.

```
export ROCR_VISIBLE_DEVICES="0,GPU-4b2c1a9f-8d3e-6f7a-b5c9-2e4d8a1f6c3b"
```

`GPU_DEVICE_ORDINAL`

[#](https://rocm.docs.amd.com#gpu-device-ordinal)

Devices indices exposed to OpenCL and HIP applications.

Runtime
: ROCm Compute Language Runtime (`ROCclr`

). Applies to applications and runtimes
using the `ROCclr`

abstraction layer including HIP and OpenCL applications.

```
export GPU_DEVICE_ORDINAL="0,2"
```

`HIP_VISIBLE_DEVICES`

[#](https://rocm.docs.amd.com#hip-visible-devices)

Device indices exposed to HIP applications.

Runtime: HIP runtime. Applies only to applications using HIP on the AMD platform.

```
export HIP_VISIBLE_DEVICES="0,2"
```

`CUDA_VISIBLE_DEVICES`

[#](https://rocm.docs.amd.com#cuda-visible-devices)

Provided for CUDA compatibility, has the same effect as `HIP_VISIBLE_DEVICES`

on the AMD platform.

Runtime : HIP or CUDA Runtime. Applies to HIP applications on the AMD or NVIDIA platform and CUDA applications.

`OMP_DEFAULT_DEVICE`

[#](https://rocm.docs.amd.com#omp-default-device)

Default device used for OpenMP target offloading.

Runtime : OpenMP Runtime. Applies only to applications using OpenMP offloading.

```
export OMP_DEFAULT_DEVICE="2"
```

## Docker[#](https://rocm.docs.amd.com#docker)

Docker uses Linux kernel namespaces to provide isolated environments for
applications. This isolation applies to most devices by default, including
GPUs. To access them in containers explicit access must be granted, please see
docker-access-gpus-in-container for details.
Specifically refer to [Restricting GPU access](https://rocm.docs.amd.com/install/docker-containers.html#docker-restrict-gpus) on exposing just a subset
of all GPUs.

Docker isolation is more secure than environment variables, and applies
to all programs that use the `amdgpu`

kernel module interfaces.
Even programs that don’t use the ROCm runtime, like graphics applications
using OpenGL or Vulkan, can only access the GPUs exposed to the container.

## GPU passthrough to virtual machines[#](https://rocm.docs.amd.com#gpu-passthrough-to-virtual-machines)

Virtual machines achieve the highest level of isolation, because even the kernel of the virtual machine is isolated from the host. Devices physically installed in the host system can be passed to the virtual machine using PCIe passthrough. This allows for using the GPU with a different operating systems like a Windows guest from a Linux host.

Setting up PCIe passthrough is specific to the hypervisor used. ROCm
supports [VMware ESXi](https://www.vmware.com/products/esxi-and-esx.html)
for select GPUs.