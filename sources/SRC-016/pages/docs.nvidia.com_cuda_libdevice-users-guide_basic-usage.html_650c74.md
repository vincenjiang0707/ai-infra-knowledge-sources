source: https://docs.nvidia.com/cuda/libdevice-users-guide/basic-usage.html

#
2. Basic Usage[](https://docs.nvidia.com#basic-usage)

##
2.1. Linking with libdevice[](https://docs.nvidia.com#linking-with-libdevice)

The libdevice library ships as an LLVM bitcode library and is meant to be linked with the target module early in the compilation process. The standard process for linking with libdevice is to first link it with the target module, then run the standard LLVM optimization and code generation passes. This allows the optimizers to inline and perform analyses on the used library functions, and eliminate any used functions as dead code.

Users of libnvvm can link with libdevice by adding the appropriate libdevice module to the `nvvmProgram`

object being compiled. In addition, the following options for `nvvmCompileProgram`

affect the behavior of libdevice functions:

Parameter |
Values |
Description |
|---|---|---|
|
|
preserve denormal values, when performing single-precision floating-point operations |
|
flush denormal values to zero, when performing single-precision floating-point operations |
|
|
|
use a faster approximation for single-precision floating-point division and reciprocals |
|
use IEEE round-to-nearest mode for single-precision floating-point division and reciprocals |
|
|
|
use a faster approximation for single-precision floating-point square root |
|
use IEEE round-to-nearest mode for single-precision floating-point square root |

The following pseudo-code shows an example of linking an NVVM IR module with the libdevice library using libnvvm:

```
nvvmProgram prog;
size_t libdeviceModSize;
const char *libdeviceMod = loadFile('/path/to/libdevice.*.bc',
&libdeviceModSize);
const char *myIr = /* NVVM IR in text or binary format */;
size_t myIrSize = /* size of myIr in bytes */;
// Create NVVM program object
nvvmCreateProgram(&prog);
// Add libdevice module to program
nvvmAddModuleToProgram(prog, libdeviceMod, libdeviceModSize);
// Add custom IR to program
nvvmAddModuleToProgram(prog, myIr, myIrSize);
// Declare compile options
const char *options[] = { "-ftz=1" };
// Compile the program
nvvmCompileProgram(prog, 1, options);
```

It is the responsibility of the client program to locate and read the libdevice library binary (represented by the `loadFile`

function in the example).