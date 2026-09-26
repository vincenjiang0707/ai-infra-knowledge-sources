source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator.html

# Communicator[](https://docs.nvidia.com#communicator)

The [ Communicator](https://docs.nvidia.com/communicator/class.html#nccl.core.Communicator) class and its methods, organized by lifecycle
stage and operation kind:

[Communicator Class](https://docs.nvidia.com/communicator/class.html)— the class itself, its constructor, its per-instance properties, and the predefined teams.[Creation and Lifecycle Methods](https://docs.nvidia.com/communicator/lifecycle.html)— creating, splitting, growing, and tearing down communicators.[Collective Communication Methods](https://docs.nvidia.com/communicator/collectives.html)— collective communication methods (allreduce, broadcast, gather, …).[Point-to-Point and Signal Methods](https://docs.nvidia.com/communicator/p2p.html)— point-to-point and signal methods (send / recv / signal / wait_signal / put_signal).[Memory Registration Methods](https://docs.nvidia.com/communicator/registration.html)— buffer and window registration for zero-copy and RMA.[Device Communicator Setup](https://docs.nvidia.com/communicator/device_setup.html)— host-side bootstrap of a device communicator.[Status and Utility Methods](https://docs.nvidia.com/communicator/status.html)— error queries and resource cleanup.