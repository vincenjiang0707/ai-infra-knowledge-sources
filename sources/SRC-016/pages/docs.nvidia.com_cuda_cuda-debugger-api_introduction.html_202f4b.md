source: https://docs.nvidia.com/cuda/cuda-debugger-api/introduction.html

# Introduction[](https://docs.nvidia.com#introduction)

This document describes the API for the set routines and data structures available in the CUDA library to any debugger.

Starting with 3.0, the CUDA debugger API includes several major changes, of which only few are directly visible to end-users:

Performance is greatly improved, both with respect to interactions with the debugger and the performance of applications being debugged.

The format of cubins has changed to ELF and, as a consequence, most restrictions on debug compilations have been lifted. More information about the new object format is included below.


The debugger API has significantly changed, reflected in the CUDA-GDB sources.

## Debugger API[](https://docs.nvidia.com#debugger-api)

The CUDA Debugger API was developed with the goal of adhering to the following principles:

Policy free

Explicit

Axiomatic

Extensible

Machine oriented


Being explicit is another way of saying that we minimize the assumptions we make. As much as possible the API reflects machine state, not internal state.

There are two major “modes” of the devices: stopped or running. We switch between these modes explicitly with suspendDevice and resumeDevice, though the machine may suspend on its own accord, for example when hitting a breakpoint.

Only when stopped, can we query the machine’s state. Warp state includes which function is it runnning, which block, which lanes are valid, etc.

As of CUDA 6.0, state collection functions in the debug API will return CUDBG_ERROR_RUNNING_DEVICE if called without first calling the suspendDevice entry point to ensure the device is stopped.

Clients of the debug API should suspend all devices before servicing a [CUDBGEvent](https://docs.nvidia.com/structCUDBGEvent.html). A valid CUDBGEvent is only guaranteed to be returned after the notification callback set using [CUDBGAPI_st::setNotifyNewEventCallback()](https://docs.nvidia.com/group__EVENT.html#group__EVENT_1g70ab97b9fa45d6fac14f4586091cdfb6) is executed. Any debug API entry point will return CUDBG_ERROR_RECURSIVE_API_CALL when the call is made from within the notification callback set using [CUDBGAPI_st::setNotifyNewEventCallback()](https://docs.nvidia.com/group__EVENT.html#group__EVENT_1g70ab97b9fa45d6fac14f4586091cdfb6).

## ELF and DWARF[](https://docs.nvidia.com#elf-and-dwarf)

CUDA applications are compiled in ELF binary format.

Starting with CUDA 6.0, DWARF device information is obtained through an API call of [CUDBGAPI_st::getElfImageByHandle](https://docs.nvidia.com/group__DWARF.html#group__DWARF_1g8a0dea7d77a03b528f5da58e7ed9bb4a) using the handle exposed from [CUDBGEvent](https://docs.nvidia.com/structCUDBGEvent.html) of type CUDBG_EVENT_ELF_IMAGE_LOADED. This means that the information is not available until runtime, after the CUDA driver has loaded. The DWARF device information lifetime is valid until it is unloaded, which presents a [CUDBGEvent](https://docs.nvidia.com/structCUDBGEvent.html) of type CUDBG_EVENT_ELF_IMAGE_UNLOADED.

In CUDA 5.5 and earlier, the DWARF device information was returned as part of the `CUDBGEvent`

of type CUDBG_EVENT_ELF_IMAGE_LOADED. The pointers presented in CUDBGEvent55 were read-only pointers to memory managed by the debug API. The memory pointed to was implicitly scoped to the lifetime of the loading CUDA context. Accessing the returned pointers after the context was destroyed resulted in undefined behavior.

DWARF device information contains physical addresses for all device memory regions except for code memory. The address class field (DW_AT_address_class) is set for all device variables, and is used to indicate the memory segment type (ptxStorageKind). The physical addresses must be accessed using several segment-specific API calls.

For memory reads, see:

`CUDBGAPI_st::readCodeMemory()`

`CUDBGAPI_st::readConstMemory()`

`CUDBGAPI_st::readGlobalMemory()`

`CUDBGAPI_st::readParamMemory()`

`CUDBGAPI_st::readSharedMemory()`

`CUDBGAPI_st::readLocalMemory()`

`CUDBGAPI_st::readTextureMemory()`


For memory writes, see:

`CUDBGAPI_st::writeGlobalMemory()`

`CUDBGAPI_st::writeParamMemory()`

`CUDBGAPI_st::writeSharedMemory()`

`CUDBGAPI_st::writeLocalMemory()`


Access to code memory requires a virtual address. This virtual address is embedded for all device code sections in the device ELF image. See the API call:

`CUDBGAPI_st::readVirtualPC()`


Here is a typical DWARF entry for a device variable located in memory:

```
<2><321>: Abbrev Number: 18 (DW_TAG_formal_parameter)
DW_AT_decl_file : 27
DW_AT_decl_line : 5
DW_AT_name : res
DW_AT_type : <2c6>
DW_AT_location : 9 byte block: 3 18 0 0 0 0 0 0 0 (DW_OP_addr: 18)
DW_AT_address_class: 7
```

The above shows that variable ‘res’ has an address class of 7 (ptxParamStorage). Its location information shows it is located at address 18 within the parameter memory segment.

Local variables are no longer spilled to local memory by default. The DWARF now contains variable-to-register mapping and liveness information for all variables. It can be the case that variables are spilled to local memory, and this is all contained in the DWARF information which is ULEB128 encoded (as a DW_OP_regx stack operation in the DW_AT_location attribute).

Here is a typical DWARF entry for a variable located in a local register:

```
<3><359>: Abbrev Number: 20 (DW_TAG_variable)
DW_AT_decl_file : 27
DW_AT_decl_line : 7
DW_AT_name : c
DW_AT_type : <1aa>
DW_AT_location : 7 byte block: 90 b9 e2 90 b3 d6 4 (DW_OP_regx: 160631632185)
DW_AT_address_class: 2
```

This shows variable ‘c’ has address class 2 (ptxRegStorage) and its location can be found by decoding the ULEB128 value, DW_OP_regx: 160631632185. See cuda-tdep.c in the cuda-gdb source drop for information on decoding this value and how to obtain which physical register holds this variable during a specific device PC range.

Access to physical registers liveness information requires a 0-based physical PC. See the API call:

`CUDBGAPI_st::readPC()`


## ABI Support[](https://docs.nvidia.com#abi-support)

ABI support is handled through the following thread API calls:

`CUDBGAPI_st::readCallDepth()`

`CUDBGAPI_st::readReturnAddress()`

`CUDBGAPI_st::readVirtualReturnAddress()`


The return address is not accessible on the local stack and the API call must be used to access its value.

For more information, please refer to the ABI documentation titled “Fermi ABI: Application Binary Interface”.

## Exception Reporting[](https://docs.nvidia.com#exception-reporting)

Some kernel exceptions are reported as device events and accessible via the API call:

`CUDBGAPI_st::readLaneException()`


The reported exceptions are listed in the CUDBGException_t enum type. Each prefix, (Device, Warp, Lane), refers to the precision of the exception. That is, the lowest known execution unit that is responsible for the origin of the exception. All lane errors are precise; the exact instruction and lane that caused the error are known. Warp errors are typically within a few instructions of where the actual error occurred, but the exact lane within the warp is not known. On device errors, we *may* know the *kernel* that caused it. Explanations about each exception type can be found in the documentation of the struct.

Exception reporting is only supported on Fermi (sm_20 or greater).

## Attaching and Detaching[](https://docs.nvidia.com#attaching-and-detaching)

The debug client must take the following steps to attach to a running CUDA application:

Attach to the CPU process corresponding to the CUDA application. The CPU part of the application will be frozen at this point.

Check to see if the

`CUDBG_DEBUGGER_INITIALIZED`

variable is accessible from the memory space of the application. If not, it implies that the application has not loaded the CUDA driver, and the attaching to the application is complete.If the

`CUDBG_DEBUGGER_INITIALIZED`

variable is accessible and non-zero, then the attach procedure is finished.-
Check the existence and value of the global variable

`CUDBG_INITIATE_DEBUGGER_ATTACH_PROCEDURE_FD`

:If it doesn’t exist, then proceed with “Legacy debugger initialization” described below.

On Linux, if it’s less than zero, then the CUDA driver has not fully initialized yet. The attach process should be retried later, once this variable is greater than or equal to zero.

If its value is greater than or equal to zero, then proceed with debugger initialization as described below.


Legacy debugger initialization: If the

`CUDBG_INITIATE_DEBUGGER_ATTACH_PROCEDURE_FD`

variable is not present or is less than zero:


Make a dynamic (inferior) function call to the function

`cudbgApiAttach()`

, e.g. by using`ptrace(2)`

on Linux. This causes a helper process to be forked off from the application, which assists in attaching to the CUDA process.Ensure that the initialization of the CUDA debug API is complete, or wait till API initialization is successful (i.e. call the

`initialize()`

API method until it succeeds).Make the

`initializeAttachStub()`

API call to initialize the helper process that was forked off from the application earlier.

If the

`CUDBG_INITIATE_DEBUGGER_ATTACH_PROCEDURE_FD`

variable is greater than or equal to zero:


Insert a breakpoint in the

`CUDBG_REPORT_ATTACH_PROCEDURE_FINISHED`

function.Open the application’s file descriptor whose number is given in

`CUDBG_INITIATE_DEBUGGER_ATTACH_PROCEDURE_FD`

variable and write a single byte to it.On Linux, this can be achieved by using the

`/proc`

filesystem and the fd file`/proc/PID/FD`

.Resume all the threads of the attached program.

Wait until the

`CUDBG_REPORT_ATTACH_PROCEDURE_FINISHED`

breakpoint is hit, remove the breakpoint and then stop/freeze all of the threads again.Call the

`initialize()`

API method. It should now succeed.

-
Read the value of the

`CUDBG_RESUME_FOR_ATTACH_DETACH`

variable from the memory space of the application:If the value is non-zero, resume the CUDA application so that more data can be collected about the application and sent to the debugger. When the application is resumed, the debug client can expect to receive various CUDA events from the CUDA application. Once all state has been collected, the debug client will receive the event

`CUDBG_EVENT_ATTACH_COMPLETE`

.If the value is zero, there is no more attach data to collect. Set the

`CUDBG_IPC_FLAG_NAME`

variable to 1 in the application’s process space, which enables further events from the CUDA application.

At this point, attaching to the CUDA application is complete and all GPUs belonging to the CUDA application will be suspended.


The debug client must take the following steps to detach from a running CUDA application:

Check to see if the

`CUDBG_IPC_FLAG_NAME`

variable is accessible from the memory space of the application, and that the CUDA debug API is initialized. If either of these conditions is not met, treat the application as CPU-only and detach from the application.Next, make the

`clearAttachState`

API call to prepare the CUDA debug API for detach.Make a dynamic (inferior) function call to the function

`cudbgApiDetach()`

in the memory space of the application, e.g. by using ptrace(2) on Linux. This causes CUDA driver to setup state for detach.Read the value of the

`CUDBG_RESUME_FOR_ATTACH_DETACH`

variable from the memory space of the application. If the value is non-zero, make the`requestCleanupOnDetach`

API call.Set the

`CUDBG_DEBUGGER_INITIALIZED`

variable to 0 in the memory space of the application. This makes sure the debugger is reinitialized from scratch if the debug client re-attaches to the application in the future.If the value of the

`CUDBG_RESUME_FOR_ATTACH_DETACH`

variable was found to be non-zero in step 4, delete all breakpoints and resume the CUDA application. This allows the CUDA driver to perform cleanups before the debug client detaches from it. Once the cleanup is complete, the debug client will receive the event`CUDBG_EVENT_DETACH_COMPLETE`

.Set the

`CUDBG_IPC_FLAG_NAME`

variable to zero in the memory space of the application. This prevents any more callbacks from the CUDA application to the debugger.The client must then finalize the CUDA debug API.

Finally, detach from the CPU part of the CUDA application. At this point all GPUs belonging to the CUDA application will be resumed.