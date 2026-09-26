source: https://docs.nvidia.com/deploy/driver-persistence/overview.html

# Overview[#](https://docs.nvidia.com#overview)

The NVIDIA kernel mode driver must be running and connected to a target GPU device before any user interactions with that device can take place. The driver behavior differs depending on the OS. Generally, if the kernel mode driver is not already running or connected to a target GPU, the invocation of any program that attempts to interact with that GPU will transparently cause the driver to load and/or initialize the GPU. When all GPU clients terminate the driver will then deinitialize the GPU. Driver load behavior is important for end users in two ways:

Application start latency

Applications that trigger GPU initilization may incur a short (order of 1-3 second) startup cost per GPU due to ECC scrubbing behavior. If the GPU is already initialized this scrubbing does not take place.

Preservation of driver state

If the driver deinitializes a GPU some non-persistent state associated with that GPU will be lost and revert back to defaults the next time the GPU is initialized. Refer to

[Data Persistence](https://docs.nvidia.com/data-persistence.html#data-persistence). To avoid this, the GPU should be kept initialized.

Default driver behavior differs between operating systems:

## Windows[#](https://docs.nvidia.com#windows)

On Windows the kernel mode driver is loaded at Windows startup and kept loaded until Windows shutdown. Consequently Windows users can mostly ignore the driver persistence implications described in this document.

Note

Driver reload events, or example due to TDR or new driver installation, will result in reset of non-persistent state.

## Linux[#](https://docs.nvidia.com#linux)

Under Linux systems where X runs by default on the target GPU, the kernel mode driver will generally be
initalized and kept alive from machine startup to shutdown, courtesy of the X process. On headless systems
or situations where no long-lived X-like client maintains a handle to the target GPU, the kernel mode driver
will initilize and deinitialize the target GPU each time a target GPU application starts and stops. In HPC
environments this situation is quite common. Since it is often desireable to keep the GPU initialized in
these cases, NVIDIA provides two options for changing driver behavior: [Persistence Mode (Legacy)](https://docs.nvidia.com/persistence-mode-legacy.html#persistence-mode)
and the [Persistence Daemon](https://docs.nvidia.com/persistence-daemon.html#persistence-daemon).