source: https://docs.nvidia.com/deploy/driver-persistence/background.html

# Background[#](https://docs.nvidia.com#background)

The NVIDIA GPU driver has historically followed Unix design philosophies by only initializing software and hardware state when the user has configured the system to do so. Traditionally, this configuration was done via the X Server and the GPUs were only initialized when the X Server (on behalf of the user) requested that they be enabled. This is very important for the ability to reconfigure the GPUs without a reboot (for example, changing SLI mode or bus settings, especially in the AGP days).

More recently, this has proven to be a problem within compute-only environments, where X is not used and the GPUs are accessed via transient instantiations of the CUDA library. This results in the GPU state being initialized and deinitialized more often than the user truly wants and leads to long load times for each CUDA job, on the order of seconds.

NVIDIA previously provided Persistence Mode to solve this issue. This is a kernel-level solution that can
be configured using `nvidia-smi`

. This approach would prevent the kernel module from fully unloading software
and hardware state when no user software was using the GPU. However, this approach creates subtle interaction
problems with the rest of the system that have made maintenance difficult.

The purpose of the NVIDIA Persistence Daemon is to replace this kernel-level solution with a more robust user-space solution. This enables compute-only environments to more closely resemble the historically typical graphics environments that the NVIDIA GPU driver was designed around.