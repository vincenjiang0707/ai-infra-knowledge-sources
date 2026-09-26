source: https://docs.nvidia.com/cupti/special-configurations/special-configurations.html

# 4. Special Configurations[#](https://docs.nvidia.com#special-configurations)

## 4.1. Multi-Instance GPU (MIG)[#](https://docs.nvidia.com#multi-instance-gpu-mig)

Multi-Instance GPU (MIG) is a feature that allows a GPU to be partitioned into multiple CUDA devices. The partitioning is carried out on two levels: First, a GPU can be split into one or multiple GPU Instances. Each GPU Instance claims ownership of one or more streaming multiprocessors (SM), a subset of the overall GPU memory, and possibly other GPU resources, such as the video encoders/decoders. Second, each GPU Instance can be further partitioned into one or more Compute Instances. Each Compute Instance has exclusive ownership of its assigned SMs of the GPU Instance. However, all Compute Instances within a GPU Instance share the GPU Instance’s memory and memory bandwidth. Every Compute Instance acts and operates as a CUDA device with a unique device ID. See the driver release notes as well as the documentation for the `nvidia-smi`

CLI tool for more information on how to configure MIG instances.

From the profiling perspective, a Compute Instance can be of one of two types: *isolated* or *shared*.

An *isolated* Compute Instance owns all of it’s assigned resources and does not share any GPU unit with another Compute Instance. In other words, the Compute Instance is of the same size as its parent GPU Instance and consequently does not have any other sibling Compute Instances. Tracing and Profiling works for isolated Compute Instances.

A *shared* Compute Instance uses GPU resources that can potentially also be accessed by other Compute Instances in the same GPU Instance. Due to this resource sharing, collecting profiling data from shared units is not permitted. Attempts to collect metrics from a shared unit will result in NaN values. Better error reporting will be done in a future release. Collecting metrics from GPU units that are exclusively owned by a shared Compute Instance is still possible. Tracing works for shared Compute Instances.

To allow users to determine which metrics are available on a target device, new APIs have been added which can be used to query counter availability before starting the profiling session. This is done by generating an image with the `cuptiProfilerGetCounterAvailability`

API and passing it to the `cuptiProfilerHostInitialize`

API during profiler host initialization.

All Compute Instances on a GPU share the same clock frequencies. To get consistent metric values with multi-pass collection, it is recommended to lock the GPU clocks during the profiling session. CLI tool `nvidia-smi`

can be used to configure a fixed frequency for the whole GPU by calling `nvidia-smi --lock-gpu-clocks=tdp,tdp`

. This sets the GPU clocks to the base TDP frequency until you reset the clocks by calling `nvidia-smi --reset-gpu-clocks`

.

## 4.2. NVIDIA Virtual GPU (vGPU)[#](https://docs.nvidia.com#nvidia-virtual-gpu-vgpu)

CUPTI supports tracing and profiling features on NVIDIA virtual GPUs (vGPUs).
Use the `cuptiProfilerDeviceSupported`

API to verify whether a given device and configuration are compatible with profiling.
If you want to use profiling features that NVIDIA vGPU supports, you must enable them for each vGPU VM that
requires them. These can be enabled by setting a vGPU plugin parameter `enable_profiling`

. How to set the
parameter for a vGPU VM depends on the hypervisor that you are using. Tracing is enabled by default and does
not require any specific setting.

To preserve tracing and profiling correctness, CUPTI blocks vGPU live migration while CUPTI is active. The
block starts when CUPTI performs lazy initialization and is released only when the application calls
`cuptiFinalize()`

or when the process exits. A live migration request issued while CUPTI is active can be
rejected or deferred by the vGPU stack. To allow live migration after CUPTI has been used, disable tracing or
profiling work as needed and call `cuptiFinalize()`

. On drivers that do not support live migration blocking
for CUDA tools, tracing results might not be accurate after virtual machine (VM) migration.

Refer to the NVIDIA Virtual GPU Software documentation for the list of
[supported GPUs](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#cuda-open-cl-support-vgpu),
how to [enable profiling features](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#enabling-cuda-toolkit-profilers-vgpu)
using the vGPU plugin parameter and for [limitations](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#limitations-with-cuda-toolkit-profilers-enabled)
on use of CUPTI with NVIDIA vGPU.

## 4.3. Windows Subsystem for Linux (WSL)[#](https://docs.nvidia.com#windows-subsystem-for-linux-wsl)

Windows Subsystem for Linux (WSL) lets you run native Linux applications, containers, and command-line tools
directly on Windows 10 and later. CUPTI supports the tracing APIs (*Activity* and *Callback*) on WSL 2 for Turing
and newer GPU architectures.
Profiling APIs are supported only on WSL 2 and on Windows 11; use the `cuptiProfilerDeviceSupported`

API to
verify that a given device and configuration are compatible with profiling.