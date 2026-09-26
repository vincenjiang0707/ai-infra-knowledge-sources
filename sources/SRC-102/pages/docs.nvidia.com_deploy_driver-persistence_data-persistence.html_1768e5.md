source: https://docs.nvidia.com/deploy/driver-persistence/data-persistence.html

# Data Persistence[#](https://docs.nvidia.com#data-persistence)

Different classes of driver state have different lifetime durations. It can be important to understand the differences, as this can affect the behavior of GPU management features like clock settings, ECC mode, and so on. Generally, driver state falls into the following categories. This is not intended to be an exhaustive list, but will cover common cases:

## GPU Initialization Lifecycle[#](https://docs.nvidia.com#gpu-initialization-lifecycle)

State of this type lasts from the time the driver initializes a GPU until the time the GPU is unititialized. This is the narrowest lifecycle, as the kernel driver itself is still loaded and may be managing other GPUs. The GPU typically initializes a GPU if a client application tries to access the GPU. The GPU is typically deinitialized after the last client exits.

State:

Compute Mode, Accounting Mode, Persistence Mode

Application Clocks, Application Clocks Permission Settings

SW-Based Power Capping Limit

Volatile ECC errors, Pending Retired Pages


## Kernel Driver Lifecycle[#](https://docs.nvidia.com#kernel-driver-lifecycle)

State of this type lasts from the time the driver loads until the time the driver unloads (or example, `rmmod`

).
In most environments this is the entire machine boot cycle. Exceptions include GPU reset events and driver installs.

State:

Accounting process data


## GPU Board Lifecycle[#](https://docs.nvidia.com#gpu-board-lifecycle)

State of this type lasts across boot cycles, as it is stored in the board’s persistent inforom. In some cases such state can be explicitly cleared, but in general this state is deemed to be persistent for the entire life of the board – or until next changed by the user.

State:

ECC Mode, Aggregate ECC errors, Retired Pages

GPU Operation Mode, Driver Model