source: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/deployment-considerations.html

# Deployment Considerations[#](https://docs.nvidia.com#deployment-considerations)

MIG functionality is provided as part of the NVIDIA GPU driver. The minimum driver version are given below:

GPU |
CUDA Version |
NVIDIA Driver Version |
|---|---|---|
A100 / A30 |
CUDA 11 |
R525 (>= 525.53) or later |
H100 / H200 |
CUDA 12 |
R450 (>= 450.80.02) or later |
B200 |
CUDA 12 |
R570 (>= 570.133.20) or later |
RTX PRO 6000 Blackwell (All editions) RTX PRO 5000 Blackwell |
CUDA 12 |
R575 (>= 575.51.03) or later |

## System Considerations[#](https://docs.nvidia.com#system-considerations)

The following system considerations are relevant for when the GPU is in MIG mode.

MIG is supported only on Linux operating system distributions supported by CUDA. It is also recommended to use the latest NVIDIA Datacenter Linux. Refer to the

[quick start guide](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/index.html).Note

Also note the device nodes and

`nvidia-capabilities`

for exposing the MIG devices. The`/proc`

mechanism for system-level interfaces is deprecated as of 450.51.06 and it is recommended to use the`/dev`

based system-level interface for controlling access mechanisms of MIG devices through cgroups. This functionality is available starting with 450.80.02+ drivers.Supported configurations include:

Bare-metal, including containers

GPU pass-through virtualization to Linux guests on top of supported hypervisors

vGPU on top of supported hypervisors


MIG allows multiple vGPUs (and thereby VMs) to run in parallel on a single A100, while preserving the isolation guarantees that vGPU provides. For more information on GPU partitioning using vGPU and MIG, refer to the

[technical brief](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/solutions/resources/documents1/TB-10226-001_v01.pdf).Setting MIG mode on the A100/A30 requires a GPU reset (and thus super-user privileges). Once the GPU is in MIG mode, instance management is then dynamic. Note that the setting is on a per-GPU basis.

On NVIDIA Ampere architecture GPUs, similar to ECC mode, MIG mode setting is persistent across reboots until the user toggles the setting explicitly

All daemons holding handles on driver modules need to be stopped before MIG enablement.

This is true for systems such as DGX which may be running system health monitoring services such as

[nvsm](https://docs.nvidia.com/nvidia-system-management-nvsm/)or GPU health monitoring or telemetry services such as DCGM.Toggling MIG mode requires the

`CAP_SYS_ADMIN`

capability. Other MIG management, such as creating and destroying instances, requires superuser by default, but can be delegated to non-privileged users by adjusting permissions to MIG capabilities in`/proc/`

.

## Application Considerations[#](https://docs.nvidia.com#application-considerations)

Users should note the following considerations when the GPU is in MIG mode:

No graphics APIs are supported (for example, OpenGL, Vulkan and so on). The exception to this is RTX Pro 6000 Blackwell GPUs where certain MIG profiles support graphics.

With driver R570, Only P2P between MIG instances on the same GPU is supported. P2P between MIG instances on different GPUs, or between MIG instances to non-MIG mode GPU devices are not supported.

CUDA IPC across GPU instances is not supported. CUDA IPC across Compute instances is supported.

CUDA debugging (e.g. using cuda-gdb) and memory/race checking (for example, using cuda-memcheck or compute-sanitizer) is supported.

CUDA MPS is supported on top of MIG. The only limitation is that the maximum number of clients (48) is lowered proportionally to the Compute Instance size.

GPUDirect RDMA is supported when used from GPU Instances.

NCCL is currently not supported with MIG.

Profiling of shared GPU resources is not supported, This is an existing limitation.