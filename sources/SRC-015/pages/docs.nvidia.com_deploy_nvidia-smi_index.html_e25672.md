source: https://docs.nvidia.com/deploy/nvidia-smi/index.html

nvidia-smi - NVIDIA System Management Interface program

nvidia-smi [OPTION1 [ARG1]] [OPTION2 [ARG2]] ...

nvidia-smi (also NVSMI) provides monitoring and management capabilities for each of NVIDIA's Tesla, Quadro, GRID and GeForce devices from Fermi and higher architecture families. GeForce Titan series devices are supported for most functions with very limited information provided for the remainder of the Geforce brand. NVSMI is a cross platform tool that supports all standard NVIDIA driver-supported Linux distros, as well as 64bit versions of Windows starting with Windows Server 2008 R2. Metrics can be consumed directly by users via stdout, or provided by file via CSV and XML formats for scripting purposes.

Note that much of the functionality of NVSMI is provided by the underlying NVML C-based library. See the NVIDIA developer website link below for more information about NVML. NVML-based python bindings are also available.

The output of NVSMI is not guaranteed to be backwards compatible. However, both NVML and the Python bindings are backwards compatible, and should be the first choice when writing any tools that must be maintained across NVIDIA driver releases.

**NVML SDK:**
*https://docs.nvidia.com/deploy/nvml-api/index.html*

**Python bindings:**
*http://pypi.python.org/pypi/nvidia-ml-py/*

Print usage information and exit.

Print version information and exit.

List each of the NVIDIA GPUs in the system, along with their UUIDs.

List each of the excluded NVIDIA GPUs in the system, along with their UUIDs.

Show a summary of GPUs connected to the system in a multi-column format.

Target a specific GPU.

Log to the specified file, rather than to stdout.

Probe until Ctrl+C at specified second interval.

Display GPU or Unit info. Displayed info includes all data listed in
the (*GPU ATTRIBUTES*) or (*UNIT ATTRIBUTES*) sections of
this document. Some devices and/or environments don't support all
possible information. Any unsupported data is indicated by a "N/A" in
the output. By default information for all available GPUs or Units is
displayed. Use the **-i** option to restrict the output to
a single GPU or Unit.

Display Unit data instead of GPU data. Unit data is only available for NVIDIA S-class Tesla enclosures.

Display data for a single specified GPU or Unit. The specified id may be the GPU/Unit's 0-based index in the natural enumeration returned by the driver, the GPU's board serial number, the GPU's UUID, or the GPU's PCI bus ID (as domain:bus:device.function in hex). It is recommended that users desiring consistency use either UUID or PCI bus ID, since device enumeration ordering is not guaranteed to be consistent between reboots and board serial number might be shared between multiple GPUs on the same board.

Redirect query output to the specified file in place of the default stdout. The specified file will be overwritten.

Produce XML output in place of the default human-readable format.
Both GPU and Unit query outputs conform to corresponding DTDs. These are
available via the **--dtd** flag.

Use with **-x**. Embed the DTD in the XML output.

Produces an encrypted debug log for use in submission of bugs back to NVIDIA.

Display only selected information: MEMORY, UTILIZATION, ECC, TEMPERATURE, POWER, CLOCK, COMPUTE, PIDS, PERFORMANCE, SUPPORTED_CLOCKS, PAGE_RETIREMENT, ACCOUNTING, ENCODER_STATS, SUPPORTED_GPU_TARGET_TEMP, VOLTAGE, FBC_STATS, ROW_REMAPPER, GSP_FIRMWARE_VERSION, POWER_SMOOTHING, POWER_PROFILES Flags can be combined with comma e.g. "MEMORY,ECC". Sampling data with max, min and avg is also returned for POWER, UTILIZATION and CLOCK display types. Doesn't work with -u/--unit or -x/--xml-format flags.

Continuously report query data at the specified interval, rather than
the default of just once. The application will sleep in-between queries.
Note that on Linux ECC error or Xid error events will print out during
the sleep period if the -x flag was not specified. Pressing Ctrl+C at
any time will abort the loop, which will otherwise run indefinitely. If
no argument is specified for the **-l** form a default
interval of 5 seconds is used.

Same as -l,--loop but in milliseconds.

Allows the caller to pass an explicit list of properties to query.

Information about GPU. Pass comma separated list of properties you want to query. e.g. --query-gpu=pci.bus_id,persistence_mode. Call --help-query-gpu for more info.

List of supported clocks. Call --help-query-supported-clocks for more info.

List of currently active compute processes. Call --help-query-compute-apps for more info.

List of accounted compute processes. Call --help-query-accounted-apps for more info. This query is not supported on vGPU host.

List of GPU device memory pages that have been retired. Call --help-query-retired-pages for more info.

Information about remapped rows. Call --help-query-remapped-rows for more info.

Comma separated list of format options:

csv - comma separated values (MANDATORY)

noheader - skip first line with column headers

nounits - don't print units for numerical values

Display data for a single specified GPU. The specified id may be the GPU's 0-based index in the natural enumeration returned by the driver, the GPU's board serial number, the GPU's UUID, or the GPU's PCI bus ID (as domain:bus:device.function in hex). It is recommended that users desiring consistency use either UUID or PCI bus ID, since device enumeration ordering is not guaranteed to be consistent between reboots and board serial number might be shared between multiple GPUs on the same board.

Redirect query output to the specified file in place of the default stdout. The specified file will be overwritten.

Continuously report query data at the specified interval, rather than
the default of just once. The application will sleep in-between queries.
Note that on Linux ECC error or Xid error events will print out during
the sleep period if the -x flag was not specified. Pressing Ctrl+C at
any time will abort the loop, which will otherwise run indefinitely. If
no argument is specified for the **-l** form a default
interval of 5 seconds is used.

Same as -l,--loop but in milliseconds.

Set the persistence mode for the target GPUs. See the (*GPU
ATTRIBUTES*) section for a description of persistence mode. Requires
root. Will impact all GPUs unless a single GPU is specified using the -i
argument. The effect of this operation is immediate. However, it does
not persist across reboots. After each reboot persistence mode will
default to "Disabled". Available on Linux only.

Set the ECC mode for the target GPUs. See the (*GPU
ATTRIBUTES*) section for a description of ECC mode. Requires root.
Will impact all GPUs unless a single GPU is specified using the -i
argument. This setting takes effect after the next reboot and is
persistent.

Reset the ECC error counters for the target GPUs. See the (*GPU
ATTRIBUTES*) section for a description of ECC error counter types.
Available arguments are 0\|VOLATILE or 1\|AGGREGATE. Requires root. Will
impact all GPUs unless a single GPU is specified using the -i argument.
The effect of this operation is immediate. Clearing aggregate counts is
not supported on Ampere+

Set the compute mode for the target GPUs. See the (*GPU
ATTRIBUTES*) section for a description of compute mode. Requires
root. Will impact all GPUs unless a single GPU is specified using the -i
argument. The effect of this operation is immediate. However, it does
not persist across reboots. After each reboot compute mode will reset to
"DEFAULT".

Modify the driver model. For Windows only. Requires administrator
privileges. -dm will fail if a display is attached, but -fdm will force
the driver model to change. Will impact all GPUs unless a single GPU is
specified using the -i argument. A driver restart is issued for all GPUs
on the system for the change to take effect, regardless of which GPU(s)
had their driver model changed. The '--no-driver-restart' flag can be
used to opt out of the driver restart, which will need an explicit
restart or reboot for the change to take effect. A reboot will be
required if the driver restart fails. See **Driver Model**
for more information on Windows driver models. An error message
indicates that setting the field failed.

Set GPU Operation Mode: 0/ALL_ON, 1/COMPUTE, 2/LOW_DP Supported on
GK110 M-class and X-class Tesla products from the Kepler family. Not
supported on Quadro and Tesla C-class products. LOW_DP and ALL_ON are
the only modes supported on GeForce Titan devices. Requires
administrator privileges. See *GPU Operation Mode* for more
information about GOM. GOM changes take effect after reboot. The reboot
requirement might be removed in the future. Compute only GOMs don't
support WDDM (Windows Display Driver Model)

Trigger a reset of one or more GPUs. Can be used to clear GPU HW and SW state in situations that would otherwise require a machine reboot. Typically useful if a double bit ECC error has occurred. Optional -i switch can be used to target one or more specific devices. Without this option, all GPUs are reset. Requires root. There can't be any applications using these devices (e.g. CUDA application, graphics application like X server, monitoring application like other instance of nvidia-smi). There also can't be any compute applications running on any other GPU in the system if individual GPU reset is not feasible.

Starting with the NVIDIA Ampere architecture, GPUs with NVLink connections can be individually reset. On Ampere NVSwitch systems, Fabric Manager is required to facilitate reset. On Hopper and later NVSwitch systems, the dependency on Fabric Manager to facilitate reset is removed.

If Fabric Manager is not running, or if any of the GPUs being reset are based on an architecture preceding the NVIDIA Ampere architecture, any GPUs with NVLink connections to a GPU being reset must also be reset in the same command. This can be done either by omitting the -i switch, or using the -i switch to specify the GPUs to be reset. If the -i option does not specify a complete set of NVLink GPUs to reset, this command will issue an error identifying the additional GPUs that must be included in the reset command.

Specific details are outlined in the tables below:

NVSwitch systems:

```
GPU Family | Fabric Manager running | Fabric Manager not running
------------|------------------------------|------------------------------
Pre-Ampere | All PEER connected GPUs must | All PEER connected GPUs must
| be reset in same command. | be reset in same command
Ampere+ | Each GPU can be reset | All PEER connected GPUs must
| individually | be reset in same command
```


Direct connected NVLink systems: (FM is not supported, as no NVSwitch HW is present)

```
GPU Family | Capabilities
------------|-------------------------------------------------------
Pre-Ampere | All PEER connected GPUs must be reset in same command
Ampere+ | Each GPU can be reset individually
```


GPU reset is not guaranteed to work in all cases. It is not recommended for production environments at this time. In some situations there may be HW components on the board that fail to revert back to an initial state following the reset request. This is more likely to be seen on Fermi-generation products vs. Kepler, and more likely to be seen if the reset is being performed on a hung GPU.

Following a reset, it is recommended that the health of each reset GPU be verified before further use. If any GPU is not healthy a complete reset should be instigated by power cycling the node.

Reset triggered without extra arguments, will be a default Function Level Reset (FLR). To issue a Bus Reset, use -r bus. For certain platforms only Function Level Reset is possible.

On Windows, GPU reset is implemented as a driver restart. When used with the -i option, only the specified GPU(s) will have their driver restarted. Without the -i option, all GPUs on the system will have their driver restarted. The driver restart will disable and re-enable the affected devices. This operation requires administrator privileges. GPU reset operation will not be supported on MIG enabled vGPU guests.

Visit *http://developer.nvidia.com/gpu-deployment-kit* to
download the GDK.

Switch GPU Virtualization Mode. Sets GPU virtualization mode to 3/VGPU or 4/VSGA. Virtualization mode of a GPU can only be set when it is running on a hypervisor.

Specifies <minGpuClock,maxGpuClock> clocks as a pair (e.g. 1500,1500) that defines closest desired locked GPU clock speed in MHz. Input can also use be a singular desired clock value (e.g. <GpuClockValue>). Optionally, --mode can be supplied to specify the clock locking modes. Supported on Volta+. Requires root.

This mode is the default clock locking mode and provides the highest possible frequency accuracies supported by the hardware.

The clock locking algorithm leverages close loop controllers to achieve frequency accuracies with improved perf per watt for certain class of applications. Due to convergence latency of close loop controllers, the frequency accuracies may be slightly lower than default mode 0.

Provides information on the style of memory clock locking support that this GPU supports (not supported, deferred, or runtime modifiable). Note: If a settling time is required between runtime switches, this settling time information will also be provided.

Specifies <minMemClock,maxMemClock> clocks as a pair (e.g.
5100,5100) that defines the range of desired locked Memory clock speed
in MHz. Input can also be a singular desired clock value (e.g.
<MemClockValue>). Requires root. **Note: this option does
not work on GPUs based on NVIDIA Hopper architectures; to lock memory
clocks on those systems use --lock-memory-clocks-deferred
instead.**

Resets the GPU clocks to the default value. Supported on Volta+. Requires root.

Resets the memory clocks to the default value. Supported on Volta+. Requires root.

This option is deprecated and will be removed in in a future CUDA release. Please use -lmc for locking memory clocks and -lgc for locking graphics clocks. Specifies maximum <memory,graphics> clocks as a pair (e.g. 2000,800) that defines GPU's speed while running applications on a GPU. Supported on Maxwell-based GeForce and from the Kepler+ family in Tesla/Quadro/Titan devices. Requires root.

This option is deprecated and will be removed in in a CUDA future release. Resets the applications clocks to the default value. Supported on Maxwell-based GeForce and from the Kepler+ family in Tesla/Quadro/Titan devices. Requires root.

Specifies the memory clock that defines the closest desired Memory Clock in MHz. The memory clock takes effect the next time the GPU is initialized. This can be guaranteed by unloading and reloading the kernel module. Requires root.

Resets the memory clock to default value. Driver unload and reload is required for this to take effect. This can be done by unloading and reloading the kernel module. Requires root.

Applies a negative frequency offset in MHz to the graphics clock VF curve for deterministic performance tuning. The offset value must be a negative integer within the allowed range specific to the GPU. Only supported on Rubin and newer architectures. Requires administrator privileges.

Displays the current VF derate offset and the allowed graphics clock VF curve offset range for the GPU. Only supported on Rubin and newer architectures.

Specifies maximum power limit in watts. Accepts integer and floating point numbers. it takes an optional argument --scope. Only on supported devices from Kepler family. Value needs to be between Min and Max Power Limit as reported by nvidia-smi. Requires root.

Specifies the scope of the power limit. Following are the options: 0/GPU: This only changes power limits for the GPU. 1/Module: This changes the power limits for the module containing multiple components. E.g. GPU and CPU. 2/GPU Base: This changes the GPU base power setting.

Overrides or restores default CUDA clocks. Available arguments are: 0\|RESTORE_DEFAULT or 1\|OVERRIDE. Requires root.

Enables or disables GPU Accounting. With GPU Accounting one can keep track of usage of resources throughout lifespan of a single process. Only on supported devices from Kepler family. Requires administrator privileges. Available arguments are 0\|DISABLED or 1\|ENABLED.

Clears all processes accounted so far. Only on supported devices from Kepler family. Requires administrator privileges.

This option is deprecated and will be removed in a future CUDA release. Set the default auto boost policy to 0/DISABLED or 1/ENABLED, enforcing the change only after the last boost client has exited. Only on certain Tesla devices from the Kepler+ family and Maxwell-based GeForce devices. Requires root.

This option is deprecated and will be removed in a future CUDA release. Allow non-admin/root control over auto boost mode. Available arguments are 0\|UNRESTRICTED, 1\|RESTRICTED. Only on certain Tesla devices from the Kepler+ family and Maxwell-based GeForce devices. Requires root.

Enables or disables Multi Instance GPU mode. Only supported on devices based on the NVIDIA Ampere architecture. Requires root. Available arguments are 0\|DISABLED or 1\|ENABLED.

Set GPU Target Temperature for a GPU in degrees celsius. Target temperature should be within limits supported by GPU. These limits can be retrieved by using query option with SUPPORTED_GPU_TARGET_TEMP. Requires Root.

Set the hostname associated with device. Should be a maximum length of 64 characters (including the terminating NULL character). Requires root.

Retrieves the hostname associated with the device.

Modify a single specified GPU. The specified id may be the GPU/Unit's 0-based index in the natural enumeration returned by the driver, the GPU's board serial number, the GPU's UUID, or the GPU's PCI bus ID (as domain:bus:device.function in hex). It is recommended that users desiring consistency use either UUID or PCI bus ID, since device enumeration ordering is not guaranteed to be consistent between reboots and board serial number might be shared between multiple GPUs on the same board.

Return a non-zero error for warnings.

Set the LED indicator state on the front and back of the unit to the
specified color. See the (*UNIT ATTRIBUTES*) section for a
description of the LED states. Allowed colors are 0\|GREEN and 1\|AMBER.
Requires root.

Modify a single specified Unit. The specified id is the Unit's 0-based index in the natural enumeration returned by the driver.

Display Device or Unit DTD.

Redirect query output to the specified file in place of the default stdout. The specified file will be overwritten.

Display Unit DTD instead of device DTD.

Display topology information about the system. Use "nvidia-smi topo -h" for more information. Linux only. Shows all GPUs NVML is able to detect but CPU and NUMA node affinity information will only be shown for GPUs with Kepler or newer architectures. Note: GPU enumeration is the same as NVML.

Display and modify the GPU drain states. A drain state is one in which the GPU is no longer accepting new clients, and is used while preparing to power down the GPU. Use "nvidia-smi drain -h" for more information. Linux only.

Display nvlink information. Use "nvidia-smi nvlink -h" for more information.

Query and control clocking behavior. Use "nvidia-smi clocks --help" for more information.

Display information on GRID virtual GPUs. Use "nvidia-smi vgpu -h" for more information.

Provides controls for MIG management. "nvidia-smi mig -h" for more information.

Provides controls for boost sliders management. "nvidia-smi boost-slider -h" for more information.

Provides queries for power hint. "nvidia-smi power-hint -h" for more information.

Display events that have occurred since driver load. Use "nvidia-smi event-log -h" for more information.

Read base64-encoded CPER events since driver load. Use "nvidia-smi cper -h" for more information.

Provides control and queries for confidential compute. "nvidia-smi conf-compute -h" for more information.

Provides controls and information for power smoothing. "nvidia-smi power-smoothing -h" for more information.

Profiles controls and information for workload power profiles. "nvidia-smi power-profiles -h" for more information.

Display Encoder Sessions information. "nvidia-smi encodersessions -h" for more information.

Return code reflects whether the operation succeeded or failed and what was the reason of failure.

Return code 0 - Success

Return code 2 - A supplied argument or flag is invalid

Return code 3 - The requested operation is not available on target device

Return code 4 - The current user does not have permission to access this device or perform this operation

Return code 6 - A query to find an object was unsuccessful

Return code 8 - A device's external power cables are not properly attached

Return code 9 - NVIDIA driver is not loaded

Return code 10 - NVIDIA Kernel detected an interrupt issue with a GPU

Return code 12 - NVML Shared Library couldn't be found or loaded

Return code 13 - Local version of NVML doesn't implement this function

Return code 14 - infoROM is corrupted

Return code 15 - The GPU has fallen off the bus or has otherwise become inaccessible

Return code 255 - Other error or internal driver error occurred

The following list describes all possible data returned by the
**-q** device query option. Unless otherwise noted all
numerical results are base 10 and unitless.

The current system timestamp at the time nvidia-smi was invoked. Format is "Day-of-week Month Day HH:MM:SS Year".

Deprecated; use **KMD Version** instead.

The version of the installed 'Kernel Mode Driver' (aka the NVIDIA display driver). This is an alphanumeric string.

Deprecated; use **CUDA UMD Version** instead.

The CUDA 'User Mode Driver' version. This is the latest CUDA version supported by the driver. This is usually, but not always, the version of the CUDA toolkit installed on the system. This is an alphanumeric string.

The number of NVIDIA GPUs in the system.

The official product name of the GPU. This is an alphanumeric string. For all products.

The official brand of the GPU. This is an alphanumeric string. For all products.

The official architecture name of the GPU. This is an alphanumeric string. For all products.

This field is deprecated, and will be removed in a future release.

A flag that indicates whether a physical display (e.g. monitor) is currently connected to any of the GPU's connectors. "Yes" indicates an attached display. "No" indicates otherwise.

A flag that indicates whether a display is initialized on the GPU's (e.g. memory is allocated on the device for display). Display can be active even when no monitor is physically attached. "Enabled" indicates an active display. "Disabled" indicates otherwise.

A flag that indicates whether persistence mode is enabled for the GPU. Value is either "Enabled" or "Disabled". When persistence mode is enabled the NVIDIA driver remains loaded even when no active clients, such as X11 or nvidia-smi, exist. This minimizes the driver load latency associated with running dependent apps, such as CUDA programs. For all CUDA-capable products. Linux only.

A field that indicates which addressing mode is currently active. The value is "ATS" or "HMM" or "None". When the mode is "ATS", system allocated memory like malloc is addressable from the GPU via Address Translation Services. This means there is effectively a single set of page tables used by both the CPU and the GPU. When the mode is "HMM", system allocated memory like malloc is addressable from the GPU via software-based mirroring of the CPU's page tables, on the GPU. When the mode is "None", neither ATS nor HMM is active. Linux only.

MIG Mode configuration status

MIG mode currently in use - NA/Enabled/Disabled

Pending configuration of MIG Mode - Enabled/Disabled

When MIG is enabled, each MIG device has the following attributes displayed:

Unique identifier for this MIG device within its parent GPU.

Identifier of the GPU instance that this MIG device belongs to.

Identifier of the compute instance within the GPU instance.

Hardware engines allocated to this MIG device. These are shared among compute instances associated with the same GPU instance.


Multiprocessor count

Number of SMs (Streaming Multiprocessors)



Copy Engine count

Number of copy engines



Encoder count

Number of video encoders



Decoder count

Number of video decoders



OFA count

Number of OFAs (Optical Flow Accelerators)



JPG count

Number of JPEG encoders/decoders


ECC error counts for this MIG device.


SRAM uncorrectable errors

Number of uncorrectable errors detected in any of the SRAMs.


FB memory allocation and usage of this MIG device. This is shared among the compute instances associated with the same GPU instance.


Total

Total size of FB memory.



Reserved

Reserved size of FB memory.



Used

Used size of FB memory.



Free

Available size of FB memory.


BAR1 memory allocation and usage of this MIG device. This is shared among the compute instances associated with the same GPU instance.


Total

Total size of BAR1 memory.



Used

Used size of BAR1 memory.



Free

Available size of BAR1 memory.


A flag that indicates whether accounting mode is enabled for the GPU. Value is either "Enabled" or "Disabled". When accounting is enabled statistics are calculated for each compute process running on the GPU. Statistics can be queried during the lifetime or after termination of the process. The execution time of process is reported as 0 while the process is in running state and updated to actual execution time after the process has terminated. See --help-query-accounted-apps for more info.

Returns the size of the circular buffer that holds list of processes that can be queried for accounting stats. This is the maximum number of processes that accounting information will be stored for before information about oldest processes will get overwritten by information about new processes.

On Windows, the TCC, WDDM and MCDM driver models are supported. The driver model can be changed with the (-dm) or (-fdm) flags. The TCC driver model is optimized for compute applications i.e. kernel launch times will be quicker with TCC. The WDDM driver model is designed for graphics applications and is not recommended for compute applications. Linux does not support multiple driver models, and will always have the value of "N/A". A driver restart will be attempted for all the devices to allow the driver model change to take effect. The '--no-driver-restart' flag can be used to prevent the driver restart in which case the driver model change will take effect on the next reboot.

The driver model currently in use. Always "N/A" on Linux.

The driver model that will be used on the next reboot. Always "N/A" on Linux.

This number matches the serial number physically printed on each board. It is a globally unique immutable alphanumeric value.

This value is the globally unique immutable alphanumeric identifier of the GPU. It does not correspond to any physical label on the board.

This value is the Per Device Identifier of the GPU. It is a 64-bit value that provides uniqueness guarantee for the GPU.

The minor number for the device is such that the NVIDIA device node file for each GPU will have the form /dev/nvidia[minor number]. Available only on Linux platform.

The BIOS of the GPU board.

Whether or not this GPU is part of a multiGPU board.

The unique board ID assigned by the driver. If two or more GPUs have the same board ID and the above "MultiGPU" field is true then the GPUs are on the same board.

The unique part number of the GPU's board

The unique part number of the GPU

Unique FRU part number of the GPU

Platform Information are compute tray platform specific information. They are GPU's positional index and platform identifying information.

**Chassis Serial Number**

Serial Number of the chassis containing this GPU.

**Slot Number**

The slot number in the chassis containing this GPU (includes switches).

**Tray Index**

The tray index within the compute slots in the chassis containing this GPU (does not include switches).

**Host ID**

Index of the node within the slot containing this GPU.

**Peer Type**

Platform indicated NVLink-peer type (e.g. switch present or not).

**Module Id**

ID of this GPU within the node.

**GPU Fabric GUID**

Fabric ID for this GPU.

Version numbers for each object in the GPU board's inforom storage. The inforom is a small, persistent store of configuration and state data for the GPU. All inforom version fields are numerical. It can be useful to know these version numbers because some GPU features are only available with inforoms of a certain version or higher.

If any of the fields below return Unknown Error additional Inforom verification check is performed and appropriate warning message is displayed.

Global version of the infoROM image. Image version just like VBIOS version uniquely describes the exact version of the infoROM flashed on the board in contrast to infoROM object version which is only an indicator of supported features.

Version for the OEM configuration data.

Version for the ECC recording data.

Version for the power management data.

Inforom checksum validation ("valid", "invalid", "N/A") Only available via --query-gpu inforom.checksum_validation

Information about flushing of the blackbox data to the inforom storage.

The timestamp of the latest flush of the BBX Object during the current run.

The duration of the latest flush of the BBX Object during the current run.

The cumulative amount of time stored in the BBX tracking GPU driver lifetime.

GOM allows one to reduce power usage and optimize GPU throughput by disabling GPU features.

Each GOM is designed to meet specific user needs.

In "All On" mode everything is enabled and running at full speed.

The "Compute" mode is designed for running only compute tasks. Graphics operations are not allowed.

The "Low Double Precision" mode is designed for running graphics applications that don't require high bandwidth double precision.

GOM can be changed with the (--gom) flag.

Supported on GK110 M-class and X-class Tesla products from the Kepler family. Not supported on Quadro and Tesla C-class products. Low Double Precision and All On modes are the only modes available for supported GeForce Titan products.

The GOM currently in use.

The GOM that will be used on the next reboot.

The C2C mode of the GPU.

Reset status of the GPU. This functionality is deprecated.

Requested functionality has been deprecated

Requested functionality has been deprecated

Action to take to clear fault that previously happened. It is not
intended for determining which fault triggered recovery action.

Possible values: None, Reset, Reboot, Drain P2P, Drain and Reset

**None**

No recovery action needed

**Reset**

Example scenario - Uncontained HBM/SRAM UCE

The GPU has encountered a fault that requires a reset to recover.

Terminate all GPU processes, reset the GPU using 'nvidia-smi -r', and
the GPU can be used again by starting new GPU processes.

**Reboot**

Example scenario - UVM fatal error

The GPU has encountered a fault may have left the OS in an inconsistent
state.

Reboot the operating system to restore the OS back to a consistent
state.

Node reboot required.

Application cannot restart without node reboot

OS warm reboot is sufficient (no need for AC/DC cycle)

**Drain P2P**

Example scenario - N/A

The GPU has encountered a fault that requires all peer-to-peer traffic
to be quiesced.

Terminate all GPU processes that conduct peer-to-peer traffic and
disable UVM persistence mode.

Disable job scheduling (no new jobs), stop all applications when
convenient, if persistence mode is enabled, disable it

Once all peer-to-peer traffic are drained, query
NVML_FI_DEV_GET_GPU_RECOVERY_ACTION again, which will return one of the
other actions.

If still DRAIN_P2P, then GPU reset.

**Drain and Reset**

Example scenario - Contained HBM UCE

Reset Recommended.

The GPU has encountered a fault that results the GPU to temporarily
operate at a reduced capacity, such as part of its frame buffer memory
being offlined, or some of its MIG partitions down.

No new work should be scheduled on the GPU, but existing work that
didn't get affected are safe to continue until they finish or reach a
good checkpoint.

Safe to restart application (memory capacity will be reduced due to
dynamic page offlining), but need to eventually reset (to get row
remap).

Asserted only for UCE row remaps.

After all existing work have drained, reset the GPU to regain its full
capacity.

Firmware version of GSP. This is an alphanumeric string.

Basic PCI info for the device. Some of this information may change whenever cards are added/removed/moved in a system. For all products.

PCI bus number, in hex

PCI device number, in hex

PCI domain number, in hex

PCI Base classcode, in hex

PCI Sub classcode, in hex

PCI vendor device id, in hex

PCI Sub System id, in hex

PCI bus id as "domain:bus:device.function", in hex

The PCIe link generation and bus width.

Not all platforms use PCI Express as the primary data path between the host and the GPU; some use another interconnect, such as C2C on certain integrated configurations. On those platforms, PCIe metrics here may not be representative of the primary data path bandwidth. Refer to C2C bandwidth metrics when applicable.

The current link generation and width. These may be reduced when the GPU is not in use.

The maximum link generation and width possible with this GPU and system configuration. For example, if the GPU supports a higher PCIe generation than the system supports then this reports the system PCIe generation.

Information related to Bridge Chip on the device. The bridge chip firmware is only present on certain boards and may display "N/A" for some newer multiGPUs boards.

The type of bridge chip. Reported as N/A if doesn't exist.

The firmware version of the bridge chip. Reported as N/A if doesn't exist.

The number of PCIe replays since reset.

The number of PCIe replay number rollovers since reset. A replay number rollover occurs after 4 consecutive replays and results in retraining the link.

The GPU-centric transmission throughput across the PCIe bus in MB/s over the past 20ms. Only supported on Maxwell architectures and newer.

The GPU-centric receive throughput across the PCIe bus in MB/s over the past 20ms. Only supported on Maxwell architectures and newer.

The PCIe atomic capabilities of outbound/inbound operations of the GPU.

The fan speed value is the percent of the product's maximum noise tolerance fan speed that the device's fan is currently intended to run at. This value may exceed 100% in certain cases. Note: The reported speed is the intended fan speed. If the fan is physically blocked and unable to spin, this output will not match the actual fan speed. Many parts do not report fan speeds because they rely on cooling via fans in the surrounding enclosure. For all discrete products with dedicated fans.

The current performance state for the GPU. States range from P0 (maximum performance) to P12 (minimum performance).

Retrieves information about factors that are reducing the frequency of clocks.

If all event reasons are returned as "Not Active" it means that clocks are running as high as possible.

This option is deprecated and will be removed in a future CUDA release. Nothing is running on the GPU and the clocks are dropping to Idle state.

This option is deprecated and will be removed in a future CUDA release. GPU clocks are limited by applications clocks setting. E.g. can be changed using nvidia-smi --applications-clocks=<Desired Clock Freq in MHz>

SW Power Scaling algorithm is reducing the clocks below requested clocks because the GPU is consuming too much power. E.g. SW power cap limit can be changed with nvidia-smi --power-limit=<Power Limit Value in W>

This option will be removed a future CUDA release. HW Slowdown is engaged, reducing the core clocks by a factor of 2 or more. It is active if either HW Thermal Slowdown or HW Power Brake are active.

HW Thermal Slowdowns are reducing the core clocks by a factor of 2 or more due to temperature being too high.

External Power Brake Assertion is triggered (e.g. by the system power supply).

This GPU has been added to a Sync boost group with nvidia-smi or DCGM in order to maximize performance per watt. All GPUs will be limited by the frequency which can be achieved by the slowest GPU. Look at the throttle reasons for other GPUs in the system to see why those GPUs are holding this one at lower clocks.

SW Thermal capping algorithm is reducing clocks below requested clocks because GPU temperature is higher than Max Operating Temp

This field will be removed in a future CUDA release. GPU clocks are limited by current setting of Display clocks. Only supported on Volta devices.

Counters, in microseconds, for the amount of time factors have been reducing the frequency of clocks.

Amount of time SW Power Scaling algorithm has reduced the clocks below requested clocks because the GPU was consuming too much power.

Amount of time the clock frequency of this GPU was reduced to match the minimum possible clock across the sync boost group.

Amount of time SW Thermal capping algorithm has reduced clocks below requested clocks because GPU temperature was higher than Max Operating Temp.

Amount of time HW Thermal Slowdown was engaged, reducing the core clocks by a factor of 2 or more, due to temperature being too high.

Amount of time External Power Brake Assertion was triggered (e.g. by the system power supply).

A flag that indicates whether sparse operation mode is enabled for the GPU. Value is either "Enabled" or "Disabled". Reported as "N/A" if not supported.

On-board frame buffer memory information. Reported total memory can be affected by ECC state. If ECC does affect the total available memory, memory is decreased by several percent, due to the requisite parity bits. The driver may also reserve a small amount of memory for internal use, even without active work on the GPU. On systems where GPUs are NUMA nodes, the accuracy of FB memory utilization provided by nvidia-smi depends on the memory accounting of the operating system. This is because FB memory is managed by the operating system instead of the NVIDIA GPU driver. Typically, pages allocated from FB memory are not released even after the process terminates to enhance performance. In scenarios where the operating system is under memory pressure, it may resort to utilizing FB memory. Such actions can result in discrepancies in the accuracy of memory reporting. For all products.

Total size of FB memory.

Reserved size of FB memory.

Used size of FB memory.

Available size of FB memory.

BAR1 is used to map the FB (device memory) so that it can be directly accessed by the CPU or by 3rd party devices (peer-to-peer on the PCIe bus).

Total size of BAR1 memory.

Used size of BAR1 memory.

Available size of BAR1 memory.

The compute mode flag indicates whether individual or multiple compute applications may run on the GPU.

"Default" means multiple contexts are allowed per device.

"Exclusive Process" means only one context is allowed per device, usable from multiple threads at a time.

"Prohibited" means no contexts are allowed per device (no compute apps).

"EXCLUSIVE_PROCESS" was added in CUDA 4.0. Prior CUDA releases supported only one exclusive mode, which is equivalent to "EXCLUSIVE_THREAD" in CUDA 4.0 and beyond.

For all CUDA-capable products.

Utilization rates report how busy each GPU is over time, and can be used to determine how much an application is using the GPUs in the system. Note: On MIG-enabled GPUs, querying the utilization of encoder, decoder, jpeg, ofa, gpu, and memory is not currently supported.

Note: During driver initialization when ECC is enabled one can see high GPU and Memory Utilization readings. This is caused by ECC Memory Scrubbing mechanism that is performed during driver initialization.

Percent of time over the past sample period during which one or more kernels was executing on the GPU. The sample period may be between 1 second and 1/6 second depending on the product.

Percent of time over the past sample period during which global (device) memory was being read or written. The sample period may be between 1 second and 1/6 second depending on the product.

Percent of time over the past sample period during which the GPU's video encoder was being used. The sampling rate is variable and can be obtained directly via the nvmlDeviceGetEncoderUtilization() API

Percent of time over the past sample period during which the GPU's video decoder was being used. The sampling rate is variable and can be obtained directly via the nvmlDeviceGetDecoderUtilization() API

Percent of time over the past sample period during which the GPU's JPEG decoder was being used. The sampling rate is variable and can be obtained directly via the nvmlDeviceGetJpgUtilization() API

Percent of time over the past sample period during which the GPU's OFA (Optical Flow Accelerator) was being used. The sampling rate is variable and can be obtained directly via the nvmlDeviceGetOfaUtilization() API

Encoder Stats report the count of active encoder sessions, along with the average Frames Per Second (FPS) and average latency (in microseconds) for all these active sessions on this device.

The total number of active encoder sessions on this device.

The average Frame Per Sencond (FSP) of all active encoder sessions on this device.

The average latency in microseconds of all active encoder sessions on this device.

A flag that indicates whether DRAM Encryption support is enabled. May be either "Enabled" or "Disabled". Changes to DRAM Encryption mode require a reboot. Requires Inforom ECC object.

The DRAM Encryption mode that the GPU is currently operating under.

The DRAM Encryption mode that the GPU will operate under after the next reboot.

A flag that indicates whether ECC support is enabled. May be either "Enabled" or "Disabled". Changes to ECC mode require a reboot. Requires Inforom ECC object version 1.0 or higher.

The ECC mode that the GPU is currently operating under.

The ECC mode that the GPU will operate under after the next reboot.

NVIDIA GPUs can provide error counts for various types of ECC errors. Some ECC errors are either single or double bit, where single bit errors are corrected and double bit errors are uncorrectable. Texture memory errors may be correctable via resend or uncorrectable if the resend fails. These errors are available across two timescales (volatile and aggregate). Single bit ECC errors are automatically corrected by the HW and do not result in data corruption. Double bit errors are detected but not corrected. Please see the ECC documents on the web for information on compute application behavior when double bit errors occur. Volatile error counters track the number of errors detected since the last driver load. Aggregate error counts persist indefinitely and thus act as a lifetime counter.

A note about volatile counts: On Windows this is once per boot. On Linux this can be more frequent. On Linux the driver unloads when no active clients exist. Hence, if persistence mode is enabled or there is always a driver client active (e.g. X11), then Linux also sees per-boot behavior. If not, volatile counts are reset each time a compute app is run.

Tesla and Quadro products pre-volta can display total ECC error counts, as well as a breakdown of errors based on location on the chip. The locations are described below. Location-based data for aggregate error counts requires Inforom ECC object version 2.0. All other ECC counts require ECC object version 1.0.

Errors detected in global device memory.

Errors detected in register file memory.

Errors detected in the L1 cache.

Errors detected in the L2 cache.

Parity errors detected in texture memory.

Total errors detected across entire chip. Sum of **Device
Memory**, **Register File**, **L1
Cache**, **L2 Cache** and **Texture
Memory**.

On Turing the output is such:

Number of correctable errors detected in any of the SRAMs

Number of uncorrectable errors detected in any of the SRAMs

Number of correctable errors detected in the DRAM

Number of uncorrectable errors detected in the DRAM

On Ampere+ The categorization of SRAM errors has been expanded upon. SRAM errors are now categorized as either parity or SEC-DED (single error correctable/double error detectable) depending on which unit hit the error. A histogram has been added that categorizes what unit hit the SRAM error. Additionally a flag has been added that indicates if the threshold for the specific SRAM has been exceeded.

Number of uncorrectable errors detected in SRAMs that are parity protected

Number of uncorrectable errors detected in SRAMs that are SEC-DED protected

Details about the sources of Aggregate uncorrectable SRAM errors

Errors that occurred in the L2 cache

Errors that occurred in the SM

Errors that occurred in a microcontroller (PMU/GSP etc...)

Errors that occrred in any PCIE related unit

Errors occuring in anything else not covered above

If one of the repair flags is pending, check the GPU Recovery action and take the appropriate steps.

Indicates if a Channel repair is pending

Indicates if a TPC repair is pending

Indicates if there is unrepairable memory

NVIDIA GPUs can retire pages of GPU device memory when they become unreliable. This can happen when multiple single bit ECC errors occur for the same page, or on a double bit ECC error. When a page is retired, the NVIDIA driver will hide it such that no driver, or application memory allocations can access it.

**Double Bit ECC** The number of GPU device memory pages
that have been retired due to a double bit ECC error.

**Single Bit ECC** The number of GPU device memory pages
that have been retired due to multiple single bit ECC errors.

**Pending** Checks if any GPU device memory pages are
pending blacklist on the next reboot. Pages that are retired but not yet
blacklisted can still be allocated, and may cause further reliability
issues.

NVIDIA GPUs can remap rows of GPU device memory when they become unreliable. This can happen when a single uncorrectable ECC error or multiple correctable ECC errors occur on the same row. When a row is remapped, the NVIDIA driver will remap the faulty row to a reserved row. All future accesses to the row will access the reserved row instead of the faulty row. This feature is available on Ampere+

**Correctable Error** The number of rows that have been
remapped due to correctable ECC errors.

**Uncorrectable Error** The number of rows that have
been remapped due to uncorrectable ECC errors.

**Pending** Indicates whether or not a row is pending
remapping. The GPU must be reset for the remapping to go into
effect.

**Remapping Failure Occurred** Indicates whether or not
a row remapping has failed in the past.

**Bank Remap Availability Histogram** Each memory bank
has a fixed number of reserved rows that can be used for row remapping.
The histogram will classify the remap availability of each bank into
Maximum, High, Partial, Low and None. Maximum availability means that
all reserved rows are available for remapping while None means that no
reserved rows are available. Correctable row remappings don't count
towards the availability histogram since row remappings due to
correctable row remappings can be evicted by an uncorrectable row
remapping.

Readings from temperature sensors on the board. All readings are in degrees C. Not all products support all reading types. In particular, products in module form factors that rely on case fans or passive cooling do not usually provide temperature readings. See below for restrictions.

T.Limit: The T.Limit sensor measures the current margin in degree Celsius to the maximum operating temperature. As such it is not an absolute temperature reading rather a relative measurement.

Not all products support T.Limit sensor readings.

When supported, nvidia-smi reports the current T.Limit temperature as a signed value that counts down. A T.Limit temperature of 0 C or lower indicates that the GPU may optimize its clock based on thermal conditions. Further, when the T.Limit sensor is supported, available temperature thresholds are also reported relative to T.Limit (see below) instead of absolute measurements.

Core GPU temperature. For all discrete and S-class products.

Current margin in degrees Celsius from the maximum GPU operating temperature.

The temperature at which a GPU will shutdown.

The T.Limit temperature below which a GPU may shutdown. Since shutdown can only triggered by the maximum GPU temperature it is possible for the current T.Limit to be more negative than this threshold.

The temperature at which a GPU HW will begin optimizing clocks due to thermal conditions, in order to cool.

The T.Limit temperature at or below which GPU HW may optimize its clocks for thermal conditions. Since this clock adjustment can only triggered by the maximum GPU temperature it is possible for the current T.Limit to be more negative than this threshold.

The temperature at which GPU SW will optimize its clock for thermal conditions.

The T.Limit temperature below which GPU SW will optimize its clock for thermal conditions.

The current target temperature for the GPU, in degrees Celsius. This
is the temperature the GPU will attempt to maintain under load, when
supported. Target temperature is user-configurable on supported devices
using nvidia-smi options such as `-gtt`

or
`--gpu-target-temp`

. Not supported on all devices.

Current temperature of GPU memory. Only available on supported devices.

The temperature at which GPU SW will optimize its memory clocks for thermal conditions. Only available on supported devices.

Power readings help to shed light on the current power usage of the GPU, and the factors that affect that usage. When power management is enabled the GPU limits power draw under load to fit within a predefined power envelope by manipulating the current performance state. See below for limits of availability.

The average power draw for the entire board for the last second, in watts. Only supported on Ampere (except GA100) or newer devices.

The last measured power draw for the entire board, in watts.

The GPU Ceiling Power limit determines the maximum power that the GPU can draw.


Current Power Limit - Current GPU Ceiling Power limit requested by software like nvidia-smi, in watts.

Requested Power Limit - GPU Ceiling Power limit currently enforced by the power management algorithm, in watts.

Default Power Limit - Default GPU Ceiling Power limit, in watts.


The GPU Base Power setting determines the maximum power that the GPU can draw without steering available power from another component (e.g. a supported NVIDIA CPU).


Current Base Power - Current GPU Base Power setting requested by software like nvidia-smi, in watts.

Requested Base Power - GPU Base Power setting currently enforced by the power management algorithm, in watts.

Default Base Power - Default GPU Base Power setting, in watts.


The minimum value in watts that power limit can be set to.

The maximum value in watts that power limit can be set to.

Power readings help to shed light on the current power usage of the Module, and the factors that affect that usage. A module is GPU + supported NVIDIA CPU + other components which consume power. When power management is enabled, the Module limits power draw under load to fit within a predefined power envelope by manipulating the current performance state. Supported on Hopper and newer datacenter products.

The average power draw for the entire module for the last second, in watts.

The last measured power draw for the entire module, in watts.

The power limit requested by software, in watts, for the whole module. Set by software such as nvidia-smi. Power Limit can be adjusted using -pl,--power-limit= switches with -s/--scope=1.

The power management algorithm's power ceiling, in watts. Total module power draw is manipulated by the power management algorithm such that it stays under this value. This limit is the minimum of various limits such as the software limit listed above.

The default power management algorithm's power ceiling, in watts. Module Power Limit will be set back to Default Power Limit after driver unload.

The minimum value in watts that module power limit can be set to.

The maximum value in watts that module power limit can be set to.

Information about GPU memory power consumption.

The average power draw for the GPU memory subsystem over the last second, in watts.

The last measured power draw for the GPU memory subsystem, in watts.

Power Smoothing related definitions and currently set values. This feature allows users to tune power parameters to minimize power fluctuations in large datacenter environments.

Value is "Yes" if the feature is enabled and "No" if the feature is not enabled.

Value is "Yes" if the Delayed Power Smoothing feature is supported and "No" if the feature is not supported.

The current privilege for the user. Value is 0, 1 or 2. Note that the higher the privilege level, the more information the user will have access to.

Values are "Enabled" or "Disabled". Indicates if ramp down hysteresis value will be honored (when enabled) or ignored (when disabled).

The last read value of the Total Module Power, in watts.

The last read value of the Total Module Power floor, in watts.

The highest percentage value for which the Percent TMP Floor can be set.

The lowest percentage value for which the Percent TMP Floor can be set.

As this feature is used, the circuitry which drives the feature wears down. This value gives the percentage of the remaining lifetime of this hardware.

The current value of the primary power floor, in watts. This value is calculated by doing TMP Ceiling * (% TMP FLoor value).

The current value of the secondary power floor, in watts. This is the power floor that is applied during active workload periods on the GPU when primary floor activation window multiplier is set to a non-zero value.

This is the minimum primary floor activation offset accepted by the driver specified in watts. This is a static field.

This is the minimum absolute raw value specified in watts that the driver will use for switching between primary and secondary floor. This point is calculated as 'secondary power floor + primary floor activation offset', and then computed value is floored to 'min primary floor activation point' by the driver at run time. This value is used to avoid setting of switch point too low accidentally.

This is the multiplier unit specified in ms for other multipliers in the profile (primary floor activation window multiplier and primary floor target window multiplier). This is a static field.

This value is the total number of Preset Profiles supported.

Values for the currently acvive power smoothing preset profile.

The percentage of the TMP Ceiling, which is used to set the TMP floor, for the currently active preset profile. For example, if max TMP is 1000 W, and the % TMP floor is 50%, then the min TMP value will be 500 W. This value is in the range [Min % TMP Floor, Max % TMP Floor].

The ramp up rate, measured in mW/s, for the currently active preset profile.

The ramp down rate, measured in mW/s, for the currently active preset profile.

The ramp down hysteresis value, in ms, for the currently active preset profile.

The secondary power floor, measured in watts, for the currently active preset profile. This is the power floor that will be applied during active workload periods on the GPU when primary floor activation window multiplier is set to a non-zero value.

The time multiplier for the activation moving average window size for the currently active preset profile. This is the 'X' ms time multiplier for the activation moving average window size. The activation moving average is compared against the (secondary floor + primary floor activation offset value) to determine if the controller should switch from the secondary floor to the primary floor. Setting this to 0 will disable switching to the secondary floor.

The time multiplier for the target moving average window size for the currently active preset profile. This is the 'X' ms time multiplier for the target moving average window size. When set to non-zero value, the target moving average power determines the primary floor. When set to 0, driver will use the Floor percentage instead to derive the primary floor.

The primary Floor Activation Offset, measured in watts, for the currently active preset profile. If the target moving average falls below the secondary floor plus this offset, the primary floor will be activated.

The number of the active preset profile.

Admin overrides allow users with sufficient permissions to preempt the values of the currently active preset profile. If an admin override is set for one of the fields, then this value will be used instead of any other configured value.

The admin override value for % TMP Floor. This value is in the range [Min % TMP Floor, Max % TMP Floor].

The admin override value for ramp up rate, measured in mW/s.

The admin override value for ramp down rate, measured in mW/s.

The admin override value for ramp down hysteresis value, in ms.

The admin override value for secondary power floor, measured in watts. This is the power floor that will be applied during active workload periods on the GPU when primary floor activation window multiplier is set to a non-zero value.

The admin override value for primary time multiplier for the activation moving average window size. This is the 'X' ms time multiplier for the activation moving average window size. The activation moving average is compared against the (secondary floor + primary floor activation offset value) to determine if the controller should switch from the secondary floor to the primary floor. Setting this to 0 will disable switching to the secondary floor.

The admin override value for primary time multiplier for the target moving average window size. This is the 'X' ms time multiplier for the target moving average window size. When set to non-zero value, the target moving average power determines the primary floor. When set to 0, driver will use the Floor percentage instead to derive the primary floor.

The admin override value for primary Floor Activation Offset, measured in watts. If the target moving average falls below the secondary floor plus this offset, the primary floor will be activated.

Indicates whether State-Of-Charge Power Smoothing feature is enabled (Enabled/Disabled).

Pre-tuned GPU profiles help to provide immediate, optimized configurations for Datacenter use cases. This sections includes information about the currently requested on enfornced power profiles.

The list of user requested profiles.

Since many of the profiles have conflicting goals, some configurations of requested profiles are incompatible. This is the list of the requested profiles which are currently enforced.

The EDPp multiplier expressed as a percentage. This feature is meant for system administrators and cannot be configured via NVML or nvidia-smi.

Current frequency at which parts of the GPU are running. All readings are in MHz. Note that it is possible for clocks to report a lower freqency than the lowest frequency that can be set by SW due to HW optimizations in certain scenarios.

Current frequency of graphics (shader) clock.

Current frequency of SM (Streaming Multiprocessor) clock.

Current frequency of memory clock.

Current frequency of video (encoder + decoder) clocks.

Applications Clocks will be removed in a future CUDA release. Please use -lmc/-lgc for locking memory/graphics clocks and -rmc/-rgc to reset memory/graphcis clocks. User specified frequency at which applications will be running at. Can be changed with [-ac \| --applications-clocks] switches.

User specified frequency of graphics (shader) clock.

User specified frequency of memory clock.

Default frequency at which applications will be running at. Application clocks can be changed with [-ac \| --applications-clocks] switches. Application clocks can be set to default using [-rac \| --reset-applications-clocks] switches.

Default frequency of applications graphics (shader) clock.

Default frequency of applications memory clock.

The Memory Clock value in MHz that takes effect the next time the GPU is initialized. This can be guaranteed by unloading and reloading the kernel module.

Maximum frequency at which parts of the GPU are design to run. All readings are in MHz. Current P0 clocks (reported in Clocks section) can differ from max clocks by few MHz.

Maximum frequency of graphics (shader) clock.

Maximum frequency of SM (Streaming Multiprocessor) clock.

Maximum frequency of memory clock.

Maximum frequency of video (encoder + decoder) clock.

Maximum customer boost frequency at which parts of the GPU are designed to run. All readings are in MHz.

Maximum customer boost frequency of graphics (shader) clock.

User-specified settings for automated clocking changes such as auto boost.

Indicates whether auto boost mode is currently enabled for this GPU (On) or disabled for this GPU (Off). Shows (N/A) if boost is not supported. Auto boost allows dynamic GPU clocking based on power, thermal and utilization. When auto boost is disabled the GPU will attempt to maintain clocks at precisely the Current Application Clocks settings (whenever a CUDA context is active). With auto boost enabled the GPU will still attempt to maintain this floor, but will opportunistically boost to higher clocks when power, thermal and utilization headroom allow. This setting persists for the life of the CUDA context for which it was requested. Apps can request a particular mode either via an NVML call (see NVML SDK) or by setting the CUDA environment variable CUDA_AUTO_BOOST. This feature is deprecated and will be removed in a future CUDA release.

Indicates the default setting for auto boost mode, either enabled (On) or disabled (Off). Shows (N/A) if boost is not supported. Apps will run in the default mode if they have not explicitly requested a particular mode. Note: Auto Boost settings can only be modified if "Persistence Mode" is enabled, which is NOT by default. This feature is deprecated and will be removed in a future CUDA release.

GPU Fabric information

**State**

Indicates the state of the GPU's handshake with the
nvidia-fabricmanager (a.k.a. GPU fabric probe)

Possible values: Completed, In Progress, Not Started, Not supported

**Status**

Status of the GPU fabric probe response from the
nvidia-fabricmanager.

Possible values: NVML_SUCCESS or one of the failure codes.

**Clique ID**

A clique is a set of GPUs that can communicate to each other over
NVLink.

The GPUs belonging to the same clique share the same clique ID.

Clique ID will only be valid for NVLink multi-node systems.

**Cluster UUID**

UUID of an NVLink multi-node cluster to which this GPU belongs.

Cluster UUID will be zero for NVLink single-node systems.

**Health**

Summary - Summary of Fabric Health <Healthy, Unhealthy, Limited
Capacity>

Bandwidth - is the GPU NVLink bandwidth degraded
<Degraded/Full>

Route Recovery in progress - is NVLink route recovery in progress
<True/False>

Route Unhealthy - is NVLink route recovery failed or aborted
<True/False>

Access Timeout Recovery - is NVLink access timeout recovery in progress
<True/False>

Incorrect Configuration - Incorrect Configuration status <Incorrect
SystemGuid, Incorrect Chassis Serial Number, No Partition, Insufficient
Nvlink Resources, Incompatible GPU Firmware, Invalid Location, GPU State
Invalid, None>

Partition Assigned - is the GPU NVLink partition correctly assigned
<True/False>

List of processes having Compute, Graphics, or Other resource usage on the device. Compute processes are reported on all the fully supported products. Reporting for Graphics processes is limited to the supported products starting with Kepler architecture. Other processes include both traditional context-based processes and processes using context-less GPU resource allocation (e.g., VMM APIs).

Represents NVML Index of the device.

Represents GPU Instance Index of the MIG device (if enabled).

Represents Compute Instance Index of the MIG device (if enabled).

Represents Process ID corresponding to the active Compute, Graphics, or Other process utilizing GPU resources.

Displayed as "C" for Compute Process, "G" for Graphics Process, "M" for MPS ("Multi-Process Service") Compute Process, "O" for Other Process (processes using GPU resources through RM subdevice allocation, including context-less operations), and "C+G" or "M+C" for processes having both Compute and Graphics or MPS Compute and Compute contexts.

Represents process name for the Compute, MPS Compute, Graphics, or Other process.

Amount of memory used by the GPU context, which represents FB memory usage for discrete GPUs or system memory usage for integrated GPUs. Not available on Windows when running in WDDM mode because Windows KMD manages all the memory not NVIDIA driver.

The "nvidia-smi dmon" command-line is used to monitor one or more GPUs (up to 16 devices) plugged into the system. This tool allows the user to see one line of monitoring data per monitoring cycle. The output is in concise format and easy to interpret in interactive mode. The output data per line is limited by the terminal size. It is supported on Tesla, GRID, Quadro and limited GeForce products for Kepler or newer GPUs under bare metal 64 bits Linux. By default, the monitoring data includes Power Usage, Temperature, SM clocks, Memory clocks and Utilization values for SM, Memory, Encoder, Decoder, JPEG and OFA. It can also be configured to report other metrics such as frame buffer memory usage, bar1 memory usage, power/thermal violations and aggregate single/double bit ecc errors. If any of the metric is not supported on the device or any other error in fetching the metric is reported as "-" in the output data. The user can also configure monitoring frequency and the number of monitoring iterations for each run. There is also an option to include date and time at each line. All the supported options are exclusive and can be used together in any order. Note: On MIG-enabled GPUs, querying the utilization of encoder, decoder, jpeg, ofa, gpu, and memory is not currently supported.

**Usage:**

The "nvidia-smi daemon" starts a background process to monitor one or
more GPUs plugged in to the system. It monitors the requested GPUs every
monitoring cycle and logs the file in compressed format at the user
provided path or the default location at /var/log/nvstats/. The log file
is created with system's date appended to it and of the format
nvstats-YYYYMMDD. The flush operation to the log file is done every
alternate monitoring cycle. Daemon also logs it's own PID at
/var/run/nvsmi.pid. By default, the monitoring data to persist includes
Power Usage, Temperature, SM clocks, Memory clocks and Utilization
values for SM, Memory, Encoder, Decoder, JPEG and OFA. The daemon tools
can also be configured to record other metrics such as frame buffer
memory usage, bar1 memory usage, power/thermal violations and aggregate
single/double bit ecc errors.The default monitoring cycle is set to 10
secs and can be configured via command-line. It is supported on Tesla,
GRID, Quadro and GeForce products for Kepler or newer GPUs under bare
metal 64 bits Linux. The daemon requires root privileges to run, and
only supports running a single instance on the system. All of the
supported options are exclusive and can be used together in any order.
Note: On MIG-enabled GPUs, querying the utilization of encoder, decoder,
jpeg, ofa, gpu, and memory is not currently supported.
**Usage:**

The "nvidia-smi replay" command-line is used to extract/replay all or
parts of log file generated by the daemon. By default, the tool tries to
pull the metrics such as Power Usage, Temperature, SM clocks, Memory
clocks and Utilization values for SM, Memory, Encoder, Decoder, JPEG and
OFA. The replay tool can also fetch other metrics such as frame buffer
memory usage, bar1 memory usage, power/thermal violations and aggregate
single/double bit ecc errors. There is an option to select a set of
metrics to replay, If any of the requested metric is not maintained or
logged as not-supported then it's shown as "-" in the output. The format
of data produced by this mode is such that the user is running the
device monitoring utility interactively. The command line requires
mandatory option "-f" to specify complete path of the log filename, all
the other supported options are exclusive and can be used together in
any order. Note: On MIG-enabled GPUs, querying the utilization of
encoder, decoder, jpeg, ofa, gpu, and memory is not currently supported.
**Usage:**

The "nvidia-smi pmon" command-line is used to monitor compute and graphics processes running on one or more GPUs (up to 16 devices) plugged into the system. This tool allows the user to see the statistics for all the running processes on each device at every monitoring cycle. The output is in concise format and easy to interpret in interactive mode. The output data per line is limited by the terminal size. It is supported on Tesla, GRID, Quadro and limited GeForce products for Kepler or newer GPUs under bare metal 64 bits Linux. By default, the monitoring data for each process includes the pid, command name and average utilization values for SM, Memory, Encoder and Decoder since the last monitoring cycle. It can also be configured to report frame buffer memory usage for each process. If there is no process running for the device, then all the metrics are reported as "-" for the device. If any of the metric is not supported on the device or any other error in fetching the metric is also reported as "-" in the output data. The user can also configure monitoring frequency and the number of monitoring iterations for each run. There is also an option to include date and time at each line. All the supported options are exclusive and can be used together in any order. Note: On MIG-enabled GPUs, querying the utilization of encoder, decoder, jpeg, ofa, gpu, and memory is not currently supported.

**Usage:**

List topology information about the system's GPUs, how they connect to each other, their CPU and memory affinities as well as qualified NICs capable of RDMA.

Note: On some systems, a NIC is used as a PCI bridge for the NVLINK switches and is not useful from a networking or RDMA point of view. The nvidia-smi topo command will filter the NIC's ports/PCIe sub-functions out of the topology matrix by examining the NIC's sysfs entries. On some kernel versions, nvidia-smi requires root privileges to read these sysfs entries.

Legend:

X = Self

SYS = Connection traversing PCIe as well as the SMP interconnect between
NUMA nodes (e.g., QPI/UPI)

NODE = Connection traversing PCIe as well as the interconnect between
PCIe Host Bridges within a NUMA node

PHB = Connection traversing PCIe as well as a PCIe Host Bridge
(typically the CPU)

PXB = Connection traversing multiple PCIe switches (without traversing
the PCIe Host Bridge)

PIX = Connection traversing a single PCIe switch NV# = Connection
traversing a bonded set of # NVLinks


Shows all the GPUs connected with the given GPU using the specified
traversal path. The traversal path values are:

0 = A single PCIe switch on a dual GPU board

1 = A single PCIe switch

2 = Multiple PCIe switches

3 = A PCIe host bridge

4 = An on-CPU interconnect link between PCIe host bridges

5 = An SMP interconnect link between NUMA nodes


Shows the P2P status between all GPUs, given a capability. Capability
values are:

r - p2p read capability

w - p2p write capability

n - p2p nvlink capability

a - p2p atomics capability

p - p2p pcie capability


Displays a matrix of PCI connections between all GPUs and NVME devices in the system with the following legend:

Legend:

X = Self

SYS = Connection traversing PCIe as well as the SMP interconnect between
NUMA nodes (e.g., QPI/UPI)

NODE = Connection traversing PCIe as well as the interconnect between
PCIe Host Bridges within a NUMA node

PHB = Connection traversing PCIe as well as a PCIe Host Bridge
(typically the CPU)

PXB = Connection traversing multiple PCIe bridges (without traversing
the PCIe Host Bridge)

PIX = Connection traversing at most a single PCIe bridge


Displays a GPU-GPU connectivity matrix showing the connections between GPUs in the system. This matrix uses fixed-width spacing and includes the following legend:

Legend:

X = Self

SYS = Connection traversing PCIe as well as the SMP interconnect between
NUMA nodes (e.g., QPI/UPI)

NODE = Connection traversing PCIe as well as the interconnect between
PCIe Host Bridges within a NUMA node

PHB = Connection traversing PCIe as well as a PCIe Host Bridge
(typically the CPU)

PXB = Connection traversing multiple PCIe bridges (without traversing
the PCIe Host Bridge)

PIX = Connection traversing at most a single PCIe bridge

NV# = Connection traversing a bonded set of # NVLinks


Displays a GPU-NIC connectivity matrix showing the connections between GPUs and NICs in the system. Includes an enhanced NIC legend showing:

ibdev: InfiniBand device name

netdev: Network device name (from sysfs)

PCI: PCI bus address

SLOT: PCIe slot number (from sysfs, if available)

The "nvidia-smi nvlink" command-line is used to manage the GPU's Nvlinks. It provides options to set and query Nvlink information.

**Usage:**

PLR Xmit Retry Blocks - Number of PLR Xmit Retry Blocks

The "nvidia-smi c2c" command-line is used to manage the GPU's C2C Links. It provides options to query C2C Link information.

**Usage:**

The "nvidia-smi vgpu" command reports on GRID vGPUs executing on supported GPUs and hypervisors (refer to driver release notes for supported platforms). Summary reporting provides basic information about vGPUs currently executing on the system. Additional options provide detailed reporting of vGPU properties, per-vGPU reporting of SM, Memory, Encoder, Decoder, Jpeg, and OFA utilization, and per-GPU reporting of supported and creatable vGPUs. Periodic reports can be automatically generated by specifying a configurable loop frequency to any command. Note: On MIG-enabled GPUs, querying the utilization of encoder, decoder, jpeg, ofa, gpu, and memory is not currently supported.

**Usage:**

The privileged "nvidia-smi mig" command-line is used to manage MIG-enabled GPUs. It provides options to create, list and destroy GPU instances and compute instances.

**Usage:**

The privileged "nvidia-smi boost-slider" command-line is used to manage boost slider on GPUs. It provides options to list and control boost sliders.

**Usage:**

The privileged "nvidia-smi power-hint" command-line is used to query power hint on GPUs.

**Usage:**

The "nvidia-smi conf-compute" command-line is used to manage confidential compute. It provides options to set and query confidential compute.

**Usage:**

The "nvidia-smi gpm" command-line is used to manage GPU performance monitoring unit. It provides options to query and set the stream state.

**Usage:**

The "nvidia-smi pci" command-line is used to manage GPU PCI counters. It provides options to query and clear PCI counters.

**Usage:**

The "nvidia-smi power-smoothing" command-line is used to manage Power Smoothing related data on the GPU. It provides options to set Power Smoothing related data and query the preset profile definitions.

**Usage:**

The "nvidia-smi power-profiles" command-line is used to manage Workload Power Profiles related data on the GPU. It provides options to update Power Profiles data and query the supported Power Profiles.

**Usage:**

The "nvidia-smi rusd" command-line is used to manage GPU RUSD settings. It provides options to set RUSD settings. RUSD is Read only User Shared Data buffer that keeps GPU metrics.

**Usage:**

**1) Display help menu**

**nvidia-smi rusd -h**

Displays help menu for using the command-line. Example:

```
nvidia-smi rusd -h
rusd -- RUSD settings section
Usage: nvidia-smi rusd [options]
Options include:
[-h | --help]: Display help information
[-i | --id]: Enumeration index, PCI bus ID or UUID.
[-spm | --set-polling-mask]: Set polling mask for the given comma-separated list of metric groups
Groups are "none", "clock", "performance", "memory", "power", "thermal", "pci", "fan", "proc_util", "all"
```


**2) Set RUSD poll mask**

**nvidia-smi rusd -i <GPU index> -spm
<mask_value>**

Set RUSD poll mask Example:

```
nvidia-smi rusd -spm all
nvidia-smi rusd -spm clock,performance
nvidia-smi rusd -spm none
```


The "nvidia-smi prm" command-line is used to read GPU PRM registers and counters. This option is only available on GPUs based on NVIDIA Blackwell or newer architectures.

**Usage:**

**1) Display help menu**

**nvidia-smi prm -h**

Displays the help menu for using the command-line. Example:

```
nvidia-smi prm -h
[-h | --help]: Display help information
[-i | --index]: GPU index; mandatory if "-n, --name" is selected
[-l | --list]: List all supported PRM registers and counters
[-n | --name]: PRM Register name; mandatory if any of "-f" or "-p" are selected
[-f | --info]: List all supported PRM parameters for the given register or counter
[-p | --params]: PRM input parameters, if any; parameters are a comma-separated list of <key>=<value> pairs
```


**2) List supported PRM registers**

**nvidia-smi prm --list**

Displays the list of supported GPU PRM registers and counters. Example:

```
nvidia-smi prm --list
Supported PRM registers:
GHPKT
MCAM
MGIR
MLPC
MORD
MPSCR
MTCAP
MTECR
MTEIM
MTEWE
MTIE
MTIM
MTRC_CAP
MTRC_CONF
MTRC_CTRL
MTSR
PAOS
PDDR
PGUID
PLIB
PLTC
PMAOS
PMLP
PMTU
PPAOS
PPCNT
PPHCR
PPLM
PPLR
PPRM
PPRT
PPSLC
PPSLS
PPTT
PTYS
SLRG
SLTP
Supported PRM counters:
CLI name Description
link_down_events PPCNT.(physical_layer_counters).link_down_events
oper_recovery PPRM.oper_recovery
plr_rcv_code_err PPCNT.(plr_counters_group).plr_rcv_code_err
plr_rcv_codes PPCNT.(plr_counters_group).plr_rcv_codes
plr_rcv_uncorrectable_code PPCNT.(plr_counters_group).plr_rcv_uncorrectable_code
plr_retry_codes PPCNT.(plr_counters_group).plr_retry_codes
plr_sync_events PPCNT.(plr_counters_group).plr_sync_events
plr_xmit_codes PPCNT.(plr_counters_group).plr_xmit_codes
plr_xmit_retry_events PPCNT.(plr_counters_group).plr_xmit_retry_events
port_xmit_wait PPCNT.(portcounters_attribute_group).port_xmit_wait
successful_recovery_events PPCNT.(physical_layer_counters).successful_recovery_events
time_between_last_2_recoveries PPCNT.(recovery_counters).time_between_last_2_recoveries
time_since_last_recovery PPCNT.(recovery_counters).time_since_last_recovery
total_successful_recovery_events PPCNT.(recovery_counters).total_successful_recovery_events
```


**3) List supported input parameters for a given PRM register
or counter**

**nvidia-smi prm -n <register> -f** or
**nvidia-smi prm -c <counter> -f**

Lists the supported input parameters (if any) for the given PRM register or counter. Example:

```
nvidia-smi prm -n PPCNT -f
Supported PRM parameters for register PPCNT:
grp
port_type
lp_msb
pnat
local_port
swid
prio_tc
grp_profile
plane_ind
counters_cap
lp_gl
clr
```


Note that some registers do not take any input parameters; in this
case the output of the above command will be **'[NONE]'**.
Example:

```
nvidia-smi prm -n MGIR -f
Supported PRM parameters for register MGIR:
[NONE]
```


**4) Read GPU PRM register**

**nvidia-smi prm -i <GPU-index> -n <register> -p
<Comma-separated list of key EQUALS value pairs>**

Reads the specified GPU PRM register with the given input parameters and outputs to the screen. Note that the output may not include all information in the register. Example:

```
nvidia-smi prm -i 0 -n PPCNT -p=local_port=1,pnat=1,grp=35
PPCNT:
grp = 35, port_type = 0, lp_msb = 0, pnat = 1, local_port = 1, swid = 0
prio_tc = 0, grp_profile = 0, plane_ind = 0, counters_cap = 0, lp_gl = 0, clr = 0
```


**5) Read GPU PRM counter**

**nvidia-smi prm -i <GPU-index> -c <counter> -p
<Comma-separated list of key EQUALS value pairs>**

Reads the specified GPU PRM counter with the given input parameters and outputs to the screen. Example:

```
nvidia-smi prm -i 0 -c plr_rcv_codes -p "local_port=1"
plr_rcv_codes ==> 0x64aace03ff
```


The "nvidia-smi soc" command-line is used to manage system on chip (SoC) metrics It provides options to query SoC metrics. This SoC section is only available on Tegra Linux system.

**Usage:**

**1) Display help menu**

**nvidia-smi soc -h**

Displays help menu for using the command-line.

Example:

```
nvidia-smi soc -h
soc -- System on Chip section
Usage: nvidia-smi soc [options]
Options include:
[-h | --help]: Display help information
[-q | --query]: Query SoC metrics
```


**2) Query Soc Metrics**

**nvidia-smi soc -q**

Query SoC metrics.

Example:

```
nvidia-smi soc -q
Memory:
MemTotal: 128.83 GiB
MemFree: 89.43 GiB
CPU:
cpu0:
clock: 972MHz
utilization: 0%
cpu1:
clock: 972MHz
utilization: 0%
cpu2:
clock: 972MHz
utilization: 0%
cpu3:
clock: 972MHz
utilization: 0%
cpu4:
clock: 972MHz
utilization: 0%
cpu5:
clock: 972MHz
utilization: 0%
cpu6:
clock: 972MHz
utilization: 0%
cpu7:
clock: 972MHz
utilization: 0%
cpu8:
clock: 1350MHz
utilization: 0%
cpu9:
clock: 1674MHz
utilization: 0%
cpu10:
clock: 972MHz
utilization: 0%
cpu11:
clock: 972MHz
utilization: 0%
cpu12:
clock: 972MHz
utilization: 0%
cpu13:
clock: 972MHz
utilization: 0%
Memory Controller:
utilization: 0%
clock: 4266MHz
Video Image Compositor:
state: off
Programmable Vision Accelerator:
state: off
Audio Processing Engine:
Clock: 300 MHz
Thermal info:
cpu-thermal: 59.22C
tj-thermal: 60.41C
soc012-thermal: 58.47C
soc345-thermal: 60.41C
Power info:
VDD_GPU: 5145 mW
VDD_CPU_SOC_MSS: 5937 mW
VIN_SYS_5V0: 4939 mW
```


The following list describes all possible data returned by the
**-q -u** unit query option. Unless otherwise noted all
numerical results are base 10 and unitless.

The current system timestamp at the time nvidia-smi was invoked. Format is "Day-of-week Month Day HH:MM:SS Year".

The version of the installed NVIDIA display driver. Format is "Major-Number.Minor-Number".

Information about any Host Interface Cards (HIC) that are installed in the system.

The version of the firmware running on the HIC.

The number of attached Units in the system.

The official product name of the unit. This is an alphanumeric value. For all S-class products.

The product identifier for the unit. This is an alphanumeric value of the form "part1-part2-part3". For all S-class products.

The immutable globally unique identifier for the unit. This is an alphanumeric value. For all S-class products.

The version of the firmware running on the unit. Format is "Major-Number.Minor-Number". For all S-class products.

The LED indicator is used to flag systems with potential problems. An LED color of AMBER indicates an issue. For all S-class products.

The color of the LED indicator. Either "GREEN" or "AMBER".

The reason for the current LED color. The cause may be listed as any combination of "Unknown", "Set to AMBER by host system", "Thermal sensor failure", "Fan failure" and "Temperature exceeds critical limit".

Temperature readings for important components of the Unit. All readings are in degrees C. Not all readings may be available. For all S-class products.

Air temperature at the unit intake.

Air temperature at the unit exhaust point.

Air temperature across the unit board.

Readings for the unit power supply. For all S-class products.

Operating state of the PSU. The power supply state can be any of the following: "Normal", "Abnormal", "High voltage", "Fan failure", "Heatsink temperature", "Current limit", "Voltage below UV alarm threshold", "Low-voltage", "I2C remote off command", "MOD_DISABLE input" or "Short pin transition".

PSU voltage setting, in volts.

PSU current draw, in amps.

Fan readings for the unit. A reading is provided for each fan, of which there can be many. For all S-class products.

The state of the fan, either "NORMAL" or "FAILED".

For a healthy fan, the fan's speed in RPM.

A list of PCI bus ids that correspond to each of the GPUs attached to the unit. The bus ids have the form "domain:bus:device.function", in hex. For all S-class products.

On Linux, NVIDIA device files may be modified by nvidia-smi if run as root. Please see the relevant section of the driver README file.

The **-a** and **-g** arguments are now
deprecated in favor of **-q** and **-i**,
respectively. However, the old arguments still work for this
release.

Query attributes for all GPUs once, and display in plain text to stdout.

Query UUID and persistence mode of all GPUs in the system.

Query ECC errors and power consumption for GPU 0 at a frequency of 10 seconds, indefinitely, and record to the file out.log.

Set the compute mode to "PROHIBITED" for GPU with UUID "GPU-b2f5f1b745e3d23d-65a3a26d-097db358-7303e0b6-149642ff3d219f8587cde3a8".

Query attributes for all Units once, and display in XML format with embedded DTD to stdout.

Write the Unit DTD to nvsmi_unit.dtd.

Display supported clocks of all GPUs.

Set applications clocks to 2500 MHz memory, and 745 MHz graphics.

Create a MIG GPU instance on profile ID 19.

Create a MIG GPU instance on profile ID 19 at placement start index 2.

List all boost sliders for all GPUs.

Set vboost to value 1 for all GPUs.

List clock range, temperature range and supported profiles of power hint.

Query power hint with graphics clock at 1350MHz, temperature at 60C and profile ID at 0.

Query power hint with graphics clock at 1350MHz, memory clock at 1216MHz, temperature at -5C and profile ID at 1.

Removed deprecated graphics voltage value from Voltage section of 'nvidia-smi -q'

Removed deprecated GPU Reset Status from 'nvidia-smi -q' output

Deprecated GPU Fabric State and Status from 'nvidia-smi -q'

On systems where GPUs are NUMA nodes, the accuracy of FB memory utilization provided by nvidia-smi depends on the memory accounting of the operating system. This is because FB memory is managed by the operating system instead of the NVIDIA GPU driver. Typically, pages allocated from FB memory are not released even after the process terminates to enhance performance. In scenarios where the operating system is under memory pressure, it may resort to utilizing FB memory. Such actions can result in discrepancies in the accuracy of memory reporting.

On Linux GPU Reset can't be triggered when there is pending GOM change.

On Linux GPU Reset may not successfully change pending ECC mode. A full reboot may be required to enable the mode change.

On Linux platforms that configure NVIDIA GPUs as NUMA nodes, enabling persistence mode or resetting GPUs may print 'Warning: persistence mode is disabled on device' if nvidia-persistenced is not running, or if nvidia-persistenced cannot access files in the NVIDIA driver's procfs directory for the device (/proc/driver/nvidia/gpus/<PCI config='' address>=''>/). During GPU reset and driver reload, this directory will be deleted and recreated, and outstanding references to the deleted directory, such as mounts or shells, can prevent processes from accessing files in the new directory.

There might be a slight discrepency between volatile/aggregate ECC counters if recovery action was not taken

The GPU hostname commands are currently only supported on compatible GB200 platforms.

On Windows, "nvidia-smi topo -p2p" reports the theoretical peer-to-peer capabilities recognized by the GPU driver and does not account for limitations from the specified devices or platform configuration.

Added -lmci/--lock-memory-clock-info command which communicates policy on how memory clock is locked for a given GPU

Added new topology subcommands to break up **'nvidia-smi
topo -m'** into focussed commands:

**'nvidia-smi topo -cpu'**: Display CPU/MEM affinity and
NUMA node ID for all GPUs, if applicable

**'nvidia-smi topo -gpu'**: Display GPU-GPU connectivity
matrix

**'nvidia-smi topo -nic'**: Display GPU-NIC connectivity
matrix with enhanced legend

**'nvidia-smi topo -all'**: Display complete topology
(GPUs, NICs, NVMe)

The new topology commands feature enhanced NIC legend (netdev name, PCI address, PCIe slot number) and improved matrix formatting with fixed-width spacing for better readability and machine parsing

Added support for displaying events that have occurred since
driver load via a new command: **'nvidia-smi event-log'**.
Use "nvidia-smi event-log -h" for more information.

Added support for reading base64-encoded CPER events since driver
load via a new command: **'nvidia-smi cper'**. Use
"nvidia-smi cper -h" for more information.

Added legend item 'DR - Disabled by regkey' to
**'nvidia-smi topo -p2p'**

Added new fields to nvidia-smi nvlink -e

PLR Xmit Blocks

PLR Xmit Retry Blocks

Clarified temperature limit reporting labels in nvidia-smi

Renamed 'GPU T.Limit Temp' to 'GPU Current T.Limit Temp'

Appended 'Specification' to static thresholds:

GPU Shutdown/Slowdown/Max Operating T.Limit Temp

GPU Target Temperature

Added support for SW Thermal Slowdown clock event reason on Thor Jetson platforms

Added new nvidia-smi nvlink --dataRate command to display nvlink data rate

Added support for querying and setting GPU base power.

Get/Set through nvidia-smi --power-limit, --query, and --query-gpu flags

Can set requested GPU base power with '<b>nvidia-smi -pl XXXX --scope=2</b>'

Can get GPU base power settings with '<b>nvidia-smi -q -d POWER</b>'

Added new '<b>--query-gpu</b>' options for GPU base power:

**gpu.base.current**

**gpu.base.requested**

**gpu.base.default**

**gpu.base.min**

**gpu.base.max**

Moved GPU Power Limit fields in the 'GPU Power Readings' section to the 'GPU Ceiling Power Limit' sub-section.

Fields are moved in the text output to the 'GPU Ceiling Power Limit' section.

Fields are still kept in the old location for the XML output, but will be removed in a future release.

Affects the following '<b>nvidia-smi --query-gpu</b>' fields under the 'GPU Power Readings' section:

**current_power_limit**

**requested_power_limit**

**default_power_limit**

Added 'MMA stall %' metric to **'nvidia-smi dmon -s n'**
to monitor MMA stall percentage

Added **'nvidia-smi --set-vf-derate'** and
**'nvidia-smi --get-vf-derate-info'** commands to apply and
query the graphics clock VF curve frequency derate.

Added new --query-gpu option for State-Of-Charge Power Smoothing feature enablement status:

power_smoothing.soc_power_smoothing_enabled

Added new fields to nvidia-smi nvlink -e

Raw BER Lane 0

Raw BER Lane 1

Raw BER Total

Raw Errors Lane 0

Raw Errors Lane 1

Renamed 'NVLE' to 'NVLink Encryption' in **'nvidia-smi
nvlink --info'**

Added a new command to read GPU PRM counters: **'nvidia-smi
prm -c'**

Added new Nvlink version print, 6.0 to **'nvidia-smi nvlink
-info'**

Added new --query-gpu options for Power Smoothing:

power_smoothing.enabled

power_smoothing.priv_level

power_smoothing.imm_ramp_down

power_smoothing.tmp_floor

power_smoothing.tmp_ceil

power_smoothing.hw_lifetime_remaining_percent

power_smoothing.max_percent_tmp_floor

power_smoothing.min_percent_tmp_floor

power_smoothing.num_preset_profiles

power_smoothing.active_profile

power_smoothing.curr_profile.percent_tmp_floor

power_smoothing.curr_profile.ramp_up_rate

power_smoothing.curr_profile.ramp_down_rate

power_smoothing.curr_profile.ramp_down_hysteresis

power_smoothing.admin_override.percent_tmp_floor

power_smoothing.admin_override.ramp_up_rate

power_smoothing.admin_override.ramp_down_rate

power_smoothing.admin_override.ramp_down_hysteresis

Added support for **'nvidia-smi topo'** on
Windows

Added New GPU Recovery output for Imex Domain

Added new field '--query-gpu=bbx.time_run' to 'nvidia-smi -q' which shows the cumulative number of seconds a GPU has been running with the driver loaded.

Added automatic driver restart support to the driver model change
command (**'-dm'** or **'--driver-model'**) on
Windows. Added a flag '--no-driver-restart' to the driver model change
command to skip the automatic restart.

Added support for **'nvidia-smi -r'** or
**'nvidia-smi --gpu-reset'** command to allow driver
restart of specific devices (using '-i') or all devices on
Windows.

Modified version information: deprecated **Driver
Version** and **CUDA Version** in favor of
**KMD Version** and **CUDA UMD Version**
respectively to more accurately reflect the source of the version
information.

Added a new field 'weight' to 'nvidia-smi vgpu -sl' to query the vGPU software weight for each runlist

Removed support of disabling ARR mode from 'nvidia-smi vgpu set-scheduler-state' command

Removed ARR Mode field from 'nvidia-smi vgpu -ss' command which reports the vGPU software scheduler state

Added support for inclusion of NIC data-direct devices in
**'nvidia-smi topo -m'**

Added support to display System on Chip metrics via a new
command: **'nvidia-smi soc'** (support only on Tegra Linux
system)

Added support for setting RUSD (Read only User Shared Data)
settings via a new command: **'nvidia-smi rusd'**

Deprecated Applications Clocks, including:

Current Applications Clocks frequencies for Memory and Graphics clocks

Default Applications Clocks frequencies for Memory and Graphics clocks

The -ac option to set Applications Clocks frequencies for Memory and Graphics clocks

The -rac option to reset Applications Clocks frequencies for Memory and Graphics clocks

Added Nvlink version to 'nvidia-smi nvlink -info' output

Added new option 'nvidia-smi power-profiles -or' to set and overwrite the requested power profiles.

Added new field 'EDPp Multipler' to 'nvidia-smi -q', which expresses the EDPp ratio as a percentage.

Added new field '--query-gpu=edpp_multipler' to retrieve the multipler.

Added Unrepairable memory status to ECC field: 'nvidia-smi -q -d ECC'

Modified the 'FB Memory Usage', 'BAR1 Memory Usage' fields in the 'nvidia-smi -q' output to 'Shared FB Memory Usage', 'Shared BAR1 Usage' respectively to indicate they are shared among the MIG devices associated with the same GPU instance.

Added a new sub-option '-ei' to 'nvidia-smi vgpu -sl' to query the vGPU software scheduler logs on the user provided engine.

Added new '--query-gpu' options for Delayed Power Smoothing:

power_smoothing.supported

power_smoothing.primary_power_floor

power_smoothing.secondary_power_floor

power_smoothing.min_primary_floor_activation_offset

power_smoothing.min_primary_floor_activation_point

power_smoothing.window_multiplier

power_smoothing.curr_profile.secondary_power_floor

power_smoothing.curr_profile.primary_floor_act_window_multiplier

power_smoothing.curr_profile.primary_floor_tar_window_multiplier

power_smoothing.curr_profile.primary_floor_act_offset

power_smoothing.admin_override.secondary_power_floor

power_smoothing.admin_override.primary_floor_act_window_multiplier

power_smoothing.admin_override.primary_floor_tar_window_multiplier

power_smoothing.admin_override.primary_floor_act_offset

Added 4 new configurable profile fields in 'nvidia-smi power-smoothing'.

Added Device NVLINK Encryption status in the new nvlink info command 'nvidia-smi nvlink -info'

Added Muti-GPU mode NVLINK Encryption (NVLE) in 'nvidia-smi conf-compute -mgm' and 'nvidia-smi conf-compute -q'

Added Nvlink Firmware Version info to the nvlink info command 'nvidia-smi nvlink -info'

Added Channel/TPC repair pending flags to ECC field: 'nvidia-smi -q -d ECC'

Removed deprecated graphics voltage value from Voltage section of 'nvidia-smi -q'

Removed deprecated GPU Reset Status from 'nvidia-smi -q' output

Added a new option to read GPU PRM registers: **'nvidia-smi
prm'**

Added a new 'Bus' reset option to the existing reset command:
**'nvidia-smi -r bus'**

Added a new output field called 'GPU PDI' to the 'nvidia-smi -q' output

Added a new cmdline option '--columns' or '-col' to display the summary in multi-column format.

Modified the 'Memory-Usage', 'BAR1-Usage' headers in the MIG device table to 'Shared Memory-Usage', 'Shared BAR1-Usage' respectively to indicate they are shared among the MIG devices associated with the same GPU instance.

Updated GPU Fabric output from 'nvidia-smi -q' output:

Added Incorrect Configuration and Summary fields to Fabric Health output

Added support for NVIDIA Jetson Thor platform

Note that the following features are currently not supported on Jetson Thor:

Clock queries and commands

Power queries and commands

Thermal and temperature queries

Per-process utilization via 'nvidia-smi pmon'

SOC memory utilization

Added new Incorrect Configuration Strings to Fabric Health output

Incompatible Gpu Firmware

Invalid Location

Added new command line options '--get-hostname' and '--set-hostname' to get and set GPU hostnames, respectively.

Added new Incorrect Configuration Strings to Fabric Health output

GPU State Invalid

Added new Partition Assigned field to Fabric Health output

Added new --query-gpu option inforom.checksum_validation to check the inforom checksum validation (nvidia-smi --query-gpu inforom.checksum_validation)

Updated 'nvidia-smi -q' to print both 'Instantaneous Power Draw' and 'Average Power Draw' in all cases where 'Power Draw' used to be printed.

Added support to nvidia-smi c2c -e to display C2C Link Errors

Added support to nvidia-smi c2c -gLowPwrInfo to display C2C Link Power state

Added new fields for Clock Event Reason Counters which can be queries with 'nvidia-smi -q' or with the 'nvidia-smi -q -d PERFORMANCE' display flag.

Added new query GPU options for Clock Event Reason Counters: 'nvidia-smi --query-gpu=clocks_event_reasons_counters.{sw_power_cap,sw_thermal_slowdown,sync_boost,hw_thermal_slowdown,hw_power_brake_slowdown}'

Added new fields for MIG timeslicing which can be queried with 'nvidia-smi -q'

Added a new cmdline option '-smts' to 'nvidia-smi vgpu' to set vGPU MIG timeslice mode

Added a new sub-option '-gi' to 'nvidia-smi vgpu -c' to query the currently creatable vGPU types on the user provided GPU Instance

Added a new sub-option '-gi' to 'nvidia-smi vgpu -q' to query detailed information of the currently active vGPU instances on the user provided GPU Instance

Added a new sub-option '-gi' to 'nvidia-smi vgpu -ss' to query the vGPU software scheduler state on the user provided GPU Instance

Added a new sub-option '-gi' to 'nvidia-smi vgpu -sl' to query the vGPU software scheduler logs on the user provided GPU Instance

Added a new cmdline option '-ghm' to 'nvidia-smi vgpu' to get vGPU heterogeneous mode on the user provided GPU Instance

Added a new sub-option '-gi' to 'nvidia-smi vgpu -shm' to set the vGPU heterogeneous mode on the user provided GPU Instance

Added new field for max instances per GPU Instance which can be queried with 'nvidia-smi vgpu -s -v'

Added a new sub-option '-gi' to 'nvidia-smi vgpu set-scheduler-state' to set the vGPU software scheduler state on the user provided GPU Instance.

Added a new sub-option '-gi' to 'nvidia-smi vgpu -c -v' to query detailed information of the creatable vGPU types on the user provided GPU Instance

Added a new cmdlin option '--query-gpu-instance-vgpu-scheduler-logs' to 'nvidia-smi vgpu' to get the vGPU software scheduler logs on the user provided GPU Instance in CSV format. See nvidia-smi vgpu --help-gpu-instance-vgpu-query-scheduler-logs for details.

Added new cmdline option '-\sLWidth' and '-\gLWidth' to 'nvidia-smi nvlink'

Added new ability to display Nvlink sleep state with 'nvidia-smi nvlink -\s for Blackwell and onward generations'

Added new query GPU options for average/instant module power draw: 'nvidia-smi --query-gpu=module.power.draw.{average,instant}'

Added new query GPU options for default/max/min module power limits: 'nvidia-smi --query-gpu=module.power.{default_limit,max_limit,min_limit}'

Added new query GPU options for module power limits: 'nvidia-smi --query-gpu=module.power.limit'

Added new query GPU options for enforced module power limits: 'nvidia-smi --query-gpu=module.enforced.power.limit'

Added new query GPU aliases for GPU Power options

Added a new command to get confidential compute info: 'nvidia-smi conf-compute -q'

Added new Power Profiles section in nvidia-smi -q and corresponding -d display flag POWER_PROFILES

Added new Power Profiles option 'nvidia-smi power-profiles' to get/set power profiles related information.

Added the platform information query to 'nvidia-smi -q'

Added the platform information query to 'nvidia-smi --query-gpu platform'

Added new Power Smoothing option 'nvidia-smi power-smoothing' to set power smoothing related values.

Added new Power Smoothing section in nvidia-smi -q and corresponding -d display flag POWER_SMOOTHING

Deprecated graphics voltage value from Voltage section of nvidia-smi -q. Voltage now always displays as 'N/A' and will be removed in a future release.

Added new topo option nvidia-smi topo -nvme to display GPUs vs NVMes connecting path.

Changed help string for the command 'nvidia-smi topo -p2p -p' from 'prop' to 'pcie' to better describe the p2p capability.

Added new command 'nvidia-smi pci -gCnt' to query PCIe RX/TX Bytes.

Added EGM capability display under new Capabilities section in nvidia-smi -q command.

Add multiGpuMode dipsplay via nvidia-smi via 'nvidia-smi conf-compute --get-multigpu-mode' or 'nvidia-smi conf-compute -mgm'

GPU Reset Status in nvidia-smi -q has been deprecated. GPU Recovery action provides all the necessary actions

nvidia-smi -q will now display Dram encryption state

nvidia-smi -den/--dram-encryption 0/1 to disable/enable dram encryption

Added new status to nvidia fabric health. nvidia-smi -q will display 3 new fields in Fabric Health - Route Recovery in progress, Route Unhealthy and Access Timeout Recovery

In nvidia-smi -q Platform Info - RACK GUID is changed to Platform Info - RACK Serial Number

In nvidia-smi --query-gpu new option for gpu_recovery_action is added

Added new counters for Nvlink5 in nvidia-smi nvlink -e:

Effective Errors to get sum of the number of errors in each Nvlink packet

Effective BER to get Effective BER for effective errors

FEC Errors - 0 to 15 to get count of symbol errors that are corrected

Added a new output field called 'GPU Fabric GUID' to the 'nvidia-smi -q' output

Added a new property called 'platform.gpu_fabric_guid' to 'nvidia-smi --query-gpu'

Updated 'nvidia-smi nvlink -gLowPwrInfo' command to display the Power Threshold Range and Units

Added the reporting of vGPU homogeneous mode to 'nvidia-smi -q'.

Added the reporting of homogeneous vGPU placements to 'nvidia-smi vgpu -s -v', complementing the existing reporting of heterogeneous vGPU placements.

Added 'Atomic Caps Inbound' in the PCI section of 'nvidia-smi -q'.

Updated ECC and row remapper output for options '--query-gpu' and '--query-remapped-rows'.

Added support for events including ECC single-bit error storm, DRAM retirement, DRAM retirement failure, contained/nonfatal poison and uncontained/fatal poison.

Added support in 'nvidia-smi nvlink -e' to display NVLink5 error counters

Added a new cmdline option to print out version information: --version

Added ability to print out only the GSP firmware version with'nvidia-smi -q -d'. Example commandline: nvidia-smi -q -d GSP_FIRMWARE_VERSION

Added support to query pci.baseClass and pci.subClass. See nvidia-smi --help-query-gpu for details.

Added PCI base and sub classcodes to 'nvidia-smi -q' output.

Added new cmdline option '--format' to 'nvidia-smi dmon' to support 'csv', 'nounit' and 'noheader' format specifiers

Added a new cmdline option '--gpm-options' to 'nvidia-smi dmon' to support GPM metrics report in MIG mode

Added the NVJPG and NVOFA utilization report to 'nvidia-smi pmon'

Added the NVJPG and NVOFA utilization report to 'nvidia-smi -q -d utilization'

Added the NVJPG and NVOFA utilization report to 'nvidia-smi vgpu -q' to report NVJPG/NVOFA utilization on active vgpus

Added the NVJPG and NVOFA utilization report to 'nvidia-smi vgpu -u' to periodically report NVJPG/NVOFA utilization on active vgpus

Added the NVJPG and NVOFA utilization report to 'nvidia-smi vgpu -p' to periodically report NVJPG/NVOFA utilization on running processs of active vgpus

Added a new cmdline option '-shm' to 'nvidia-smi vgpu' to set vGPU heterogeneous mode

Added the reporting of vGPU heterogeneous mode in 'nvidia-smi -q'

Added ability to call 'nvidia-smi mig -lgip' and 'nvidia-smi mig -lgipp' to work without requiring MIG being enabled

Added support to query confidential compute key rotation threshold info.

Added support to set confidential compute key rotation max attacker advantage.

Added a new cmdline option '--sparse-operation-mode' to 'nvidia-smi clocks' to set the sparse operation mode

Added the reporting of sparse operation mode to 'nvidia-smi -q -d PERFORMANCE'

Added support to query the timestamp and duration of the latest flush of the BBX object to the inforom storage.

Added support for reporting out GPU Memory power usage.

Updated the SRAM error status reported in the ECC query 'nvidia-smi -q -d ECC'

Added support to query and report the GPU JPEG and OFA (Optical Flow Accelerator) utilizations.

Removed deprecated 'stats' command.

Added support to set the vGPU software scheduler state.

Renamed counter collection unit to gpu performance monitoring.

Added new C2C Mode reporting to device query.

Added back clock_throttle_reasons to --query-gpu to not break backwards compatibility

Added support to get confidential compute CPU capability and GPUs capability.

Added support to set confidential compute unprotected memory and GPU ready state.

Added support to get confidential compute memory info and GPU ready state.

Added support to display confidential compute devtools mode, environment and feature status.

Added support to query power.draw.average and power.draw.instant. See nvidia-smi --help-query-gpu for details.

Added support to get the vGPU software scheduler state.

Added support to get the vGPU software scheduler logs.

Added support to get the vGPU software scheduler capabilities.

Renamed Clock Throttle Reasons to Clock Event Reasons.

Added support to query and set counter collection unit stream state.

Add new 'Reserved' memory reporting to the FB memory output

Added support to query power hint

Removed support for -acp,--application-clock-permissions option

Add option to specify placement when creating a MIG GPU instance.

Added support to query and control boost slider

Added --lock-memory-clock and --reset-memory-clock command to lock to closest min/max Memory clock provided and ability to reset Memory clock

Allow fan speeds greater than 100% to be reported

Added topo support to display NUMA node affinity for GPU devices

Added support to create MIG instances using profile names

Added support to create the default compute instance while creating a GPU instance

Added support to query and disable MIG mode on Windows

Removed support of GPU reset(-r) command on MIG enabled vGPU guests

Added support for Multi Instance GPU (MIG)

Added support to individually reset NVLink-capable GPUs based on the NVIDIA Ampere architecture

Support for Volta and Turing architectures, bug fixes, performance improvements, and new features

Added nvlink support to expose the publicly available NVLINK NVML APIs

Added clocks sub-command with synchronized boost support

Updated nvidia-smi stats to report GPU temperature metric

Updated nvidia-smi dmon to support PCIe throughput

Updated nvidia-smi daemon/replay to support PCIe throughput

Updated nvidia-smi dmon, daemon and replay to support PCIe Replay Errors

Added GPU part numbers in nvidia-smi -q

Removed support for exclusive thread compute mode

Added Video (encoder/decode) clocks to the Clocks and Max Clocks display of nvidia-smi -q

Added memory temperature output to nvidia-smi dmon

Added --lock-gpu-clock and --reset-gpu-clock command to lock to closest min/max GPU clock provided and reset clock

Added --cuda-clocks to override or restore default CUDA clocks

Added topo support to display affinities per GPU

Added topo support to display neighboring GPUs for a given level

Added topo support to show pathway between two given GPUs

Added 'nvidia-smi pmon' command-line for process monitoring in scrolling format

Added '--debug' option to produce an encrypted debug log for use in submission of bugs back to NVIDIA

Fixed reporting of Used/Free memory under Windows WDDM mode

The accounting stats is updated to include both running and terminated processes. The execution time of running process is reported as 0 and updated to actual value when the process is terminated.

Added reporting of PCIe replay counters

Added support for reporting Graphics processes via nvidia-smi

Added reporting of PCIe utilization

Added dmon command-line for device monitoring in scrolling format

Added daemon command-line to run in background and monitor devices as a daemon process. Generates dated log files at /var/log/nvstats/

Added replay command-line to replay/extract the stat files generated by the daemon tool

Added reporting of temperature threshold information.

Added reporting of brand information (e.g. Tesla, Quadro, etc.)

Added support for K40d and K80.

Added reporting of max, min and avg for samples (power, utilization, clock changes). Example commandline: nvidia-smi -q -d power,utilization, clock

Added nvidia-smi stats interface to collect statistics such as power, utilization, clock changes, xid events and perf capping counters with a notion of time attached to each sample. Example commandline: nvidia-smi stats

Added support for collectively reporting metrics on more than one GPU. Used with comma separated with '-i' option. Example: nvidia-smi -i 0,1,2

Added support for displaying the GPU encoder and decoder utilizations

Added nvidia-smi topo interface to display the GPUDirect communication matrix (EXPERIMENTAL)

Added support for displayed the GPU board ID and whether or not it is a multiGPU board

Removed user-defined throttle reason from XML output

Added reporting of minor number.

Added reporting BAR1 memory size.

Added reporting of bridge chip firmware.

Added new --applications-clocks-permission switch to change permission requirements for setting and resetting applications clocks.

Added reporting of Display Active state and updated documentation to clarify how it differs from Display Mode and Display Active state

For consistency on multi-GPU boards nvidia-smi -L always displays UUID instead of serial number

Added machine readable selective reporting. See SELECTIVE QUERY OPTIONS section of nvidia-smi -h

Added queries for page retirement information. See --help-query-retired-pages and -d PAGE_RETIREMENT

Renamed Clock Throttle Reason User Defined Clocks to Applications Clocks Setting

On error, return codes have distinct non zero values for each error class. See RETURN VALUE section

nvidia-smi -i can now query information from healthy GPU when there is a problem with other GPU in the system

All messages that point to a problem with a GPU print pci bus id of a GPU at fault

New flag --loop-ms for querying information at higher rates than once a second (can have negative impact on system performance)

Added queries for accounting procsses. See --help-query-accounted-apps and -d ACCOUNTING

Added the enforced power limit to the query output

Added reporting of GPU Operation Mode (GOM)

Added new --gom switch to set GPU Operation Mode

Reformatted non-verbose output due to user feedback. Removed pending information from table.

Print out helpful message if initialization fails due to kernel module not receiving interrupts

Better error handling when NVML shared library is not present in the system

Added new --applications-clocks switch

Added new filter to --display switch. Run with -d SUPPORTED_CLOCKS to list possible clocks on a GPU

When reporting free memory, calculate it from the rounded total and used memory so that values add up

Added reporting of power management limit constraints and default limit

Added new --power-limit switch

Added reporting of texture memory ECC errors

Added reporting of Clock Throttle Reasons

Clearer error reporting for running commands (like changing compute mode)

When running commands on multiple GPUs at once N/A errors are treated as warnings.

nvidia-smi -i now also supports UUID

UUID format changed to match UUID standard and will report a different value.

Report VBIOS version.

Added -d/--display flag to filter parts of data

Added reporting of PCI Sub System ID

Updated docs to indicate we support M2075 and C2075

Report HIC HWBC firmware version with -u switch

Report max(P0) clocks next to current clocks

Added --dtd flag to print the device or unit DTD

Added message when NVIDIA driver is not running

Added reporting of PCIe link generation (max and current), and link width (max and current).

Getting pending driver model works on non-admin

Added support for running nvidia-smi on Windows Guest accounts

Running nvidia-smi without -q command will output non verbose version of -q instead of help

Fixed parsing of -l/--loop= argument (default value, 0, to big value)

Changed format of pciBusId (to XXXX:XX:XX.X - this change was visible in 280)

Parsing of busId for -i command is less restrictive. You can pass 0:2:0.0 or 0000:02:00 and other variations

Changed versioning scheme to also include 'driver version'

XML format always conforms to DTD, even when error conditions occur

Added support for single and double bit ECC events and XID errors (enabled by default with -l flag disabled for -x flag)

Added device reset -r --gpu-reset flags

Added listing of compute running processes

Renamed power state to performance state. Deprecated support exists in XML output only.

Updated DTD version number to 2.0 to match the updated XML output

On Linux, the driver README is installed as /usr/share/doc/NVIDIA_GLX-1.0/README.txt

NVIDIA Corporation

Copyright 2011-2026 NVIDIA Corporation