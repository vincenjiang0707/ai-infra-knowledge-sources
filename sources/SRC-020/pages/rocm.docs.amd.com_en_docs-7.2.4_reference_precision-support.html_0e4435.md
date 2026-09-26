source: https://rocm.docs.amd.com/en/docs-7.2.4/reference/precision-support.html

# Data types and precision support[#](https://rocm.docs.amd.com#data-types-and-precision-support)

2026-02-19

9 min read time

This topic summarizes the data types supported on AMD GPUs and
ROCm libraries, along with corresponding [HIP](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/index.html) data types.

## Integral types[#](https://rocm.docs.amd.com#integral-types)

The signed and unsigned integral types supported by ROCm are listed in the following table.

Type name |
HIP type |
Description |
|---|---|---|
int8 |
|
A signed or unsigned 8-bit integer |
int16 |
|
A signed or unsigned 16-bit integer |
int32 |
|
A signed or unsigned 32-bit integer |
int64 |
|
A signed or unsigned 64-bit integer |

## Floating-point types[#](https://rocm.docs.amd.com#floating-point-types)

The floating-point types supported by ROCm are listed in the following table.

Type name |
HIP type |
Description |
|---|---|---|
float4 (E2M1) |
`__hip_fp4_e2m1` |
A 4-bit floating-point number with |
float6 (E3M2) |
`__hip_fp6_e3m2` |
A 6-bit floating-point number with |
float6 (E2M3) |
`__hip_fp6_e2m3` |
A 6-bit floating-point number with |
float8 (E4M3) |
`__hip_fp8_e4m3_fnuz` ,`__hip_fp8_e4m3` |
An 8-bit floating-point number with |
float8 (E5M2) |
`__hip_fp8_e5m2_fnuz` ,`__hip_fp8_e5m2` |
An 8-bit floating-point number with |
float16 |
|
A 16-bit floating-point number that conforms to the IEEE 754-2008 half-precision storage format. |
bfloat16 |
|
A shortened 16-bit version of the IEEE 754 single-precision storage format. |
tensorfloat32 |
Not available |
A floating-point number that occupies 32 bits or less of storage, providing improved range compared to half (16-bit) format, at (potentially) greater throughput than single-precision (32-bit) formats. |
float32 |
|
A 32-bit floating-point number that conforms to the IEEE 754 single-precision storage format. |
float64 |
|
A 64-bit floating-point number that conforms to the IEEE 754 double-precision storage format. |

Note

The float8 and tensorfloat32 types are internal types used in calculations in Matrix Cores and can be stored in any type of the same size.

CDNA3 natively supports FP8 FNUZ (E4M3 and E5M2), which differs from the customized FP8 format used with NVIDIA H100 (

[FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433)).In some AMD documents and articles, float8 (E5M2) is referred to as bfloat8.

The

[low precision floating point types page](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/reference/low_fp_types.html)describes how to use these types in HIP with examples.

## Level of support definitions[#](https://rocm.docs.amd.com#level-of-support-definitions)

In the following sections, icons represent the level of support. These icons, described in the following table, are also used in the library data type support pages.

Icon |
Definition |
|---|---|
NA |
Not applicable |
❌ |
Not supported |
⚠️ |
Partial support |
✅ |
Full support |

Note

Full support means that the type is supported natively or with hardware emulation.

Native support means that the operations for that type are implemented in hardware. Types that are not natively supported are emulated with the available hardware. The performance of non-natively supported types can differ from the full instruction throughput rate. For example, 16-bit integer operations can be performed on the 32-bit integer ALUs at full rate; however, 64-bit integer operations might need several instructions on the 32-bit integer ALUs.

Any type can be emulated by software, but this page does not cover such cases.


## Data type support by hardware architecture[#](https://rocm.docs.amd.com#data-type-support-by-hardware-architecture)

AMD’s GPU lineup spans multiple architecture generations:

CDNA1 such as MI100

CDNA2 such as MI210, MI250, and MI250X

CDNA3 such as MI300A, MI300X, and MI325X

CDNA4 such as MI350X and MI355X

RDNA2 such as PRO W6800 and PRO V620

RDNA3 such as RX 7900XT and RX 7900XTX

RDNA4 such as RX 9070 and RX 9070XT


### HIP C++ type implementation support[#](https://rocm.docs.amd.com#hip-c-type-implementation-support)

The HIP C++ types available on different hardware platforms are listed in the following table.

HIP C++ Type |
CDNA1 |
CDNA2 |
CDNA3 |
CDNA4 |
RDNA2 |
RDNA3 |
RDNA4 |
|---|---|---|---|---|---|---|---|
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
❌ |
❌ |
❌ |
✅ |
❌ |
❌ |
❌ |
|
❌ |
❌ |
❌ |
✅ |
❌ |
❌ |
❌ |
|
❌ |
❌ |
❌ |
✅ |
❌ |
❌ |
❌ |
|
❌ |
❌ |
✅ |
❌ |
❌ |
❌ |
❌ |
|
❌ |
❌ |
✅ |
❌ |
❌ |
❌ |
❌ |
|
❌ |
❌ |
❌ |
✅ |
❌ |
❌ |
✅ |
|
❌ |
❌ |
❌ |
✅ |
❌ |
❌ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
|
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |
✅ |

Note

Library support for specific data types is contingent upon hardware support. Even if a ROCm library indicates support for a particular data type, that type will only be fully functional if the underlying hardware architecture (as shown in the table above) also supports it. For example, fp8 types are only available on architectures shown with a checkmark in the relevant rows.

### Compute units support[#](https://rocm.docs.amd.com#compute-units-support)

The following table lists data type support for compute units.

Type name |
int8 |
int16 |
int32 |
int64 |
|---|---|---|---|---|
CDNA1 |
✅ |
✅ |
✅ |
✅ |
CDNA2 |
✅ |
✅ |
✅ |
✅ |
CDNA3 |
✅ |
✅ |
✅ |
✅ |
CDNA4 |
✅ |
✅ |
✅ |
✅ |
RDNA2 |
✅ |
✅ |
✅ |
✅ |
RDNA3 |
✅ |
✅ |
✅ |
✅ |
RDNA4 |
✅ |
✅ |
✅ |
✅ |

Type name |
float4 |
float6 (E2M3) |
float6 (E3M2) |
float8 (E4M3) |
float8 (E5M2) |
|---|---|---|---|---|---|
CDNA1 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA2 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA3 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA4 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA2 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA3 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA4 |
❌ |
❌ |
❌ |
❌ |
❌ |

Type name |
float16 |
bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|
CDNA1 |
✅ |
✅ |
❌ |
✅ |
✅ |
CDNA2 |
✅ |
✅ |
❌ |
✅ |
✅ |
CDNA3 |
✅ |
✅ |
❌ |
✅ |
✅ |
CDNA4 |
✅ |
✅ |
❌ |
✅ |
✅ |
RDNA2 |
✅ |
✅ |
❌ |
✅ |
✅ |
RDNA3 |
✅ |
✅ |
❌ |
✅ |
✅ |
RDNA4 |
✅ |
✅ |
❌ |
✅ |
✅ |

### Matrix core support[#](https://rocm.docs.amd.com#matrix-core-support)

The following table lists data type support for AMD GPU matrix cores.

Type name |
int8 |
int16 |
int32 |
int64 |
|---|---|---|---|---|
CDNA1 |
✅ |
❌ |
❌ |
❌ |
CDNA2 |
✅ |
❌ |
❌ |
❌ |
CDNA3 |
✅ |
❌ |
❌ |
❌ |
CDNA4 |
✅ |
❌ |
❌ |
❌ |
RDNA2 |
✅ |
❌ |
❌ |
❌ |
RDNA3 |
✅ |
❌ |
❌ |
❌ |
RDNA4 |
✅ |
❌ |
❌ |
❌ |

Type name |
float4 |
float6 (E2M3) |
float6 (E3M2) |
float8 (E4M3) |
float8 (E5M2) |
|---|---|---|---|---|---|
CDNA1 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA2 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA3 |
❌ |
❌ |
❌ |
✅ |
✅ |
CDNA4 |
✅ |
✅ |
✅ |
✅ |
✅ |
RDNA2 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA3 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA4 |
❌ |
❌ |
❌ |
✅ |
✅ |

Type name |
float16 |
bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|
CDNA1 |
✅ |
✅ |
❌ |
✅ |
❌ |
CDNA2 |
✅ |
✅ |
❌ |
✅ |
✅ |
CDNA3 |
✅ |
✅ |
✅ |
✅ |
✅ |
CDNA4 |
✅ |
✅ |
✅ |
✅ |
✅ |
RDNA2 |
✅ |
✅ |
❌ |
❌ |
❌ |
RDNA3 |
✅ |
✅ |
❌ |
❌ |
❌ |
RDNA4 |
✅ |
✅ |
❌ |
❌ |
❌ |

### Atomic operations support[#](https://rocm.docs.amd.com#atomic-operations-support)

The following table lists which data types are supported for atomic
operations on AMD GPUs. The atomics operation type behavior is affected by the
memory locations, memory granularity, or scope of operations. For detailed
various support of atomic read-modify-write (atomicRMW) operations collected on
the [Hardware atomics operation support](https://rocm.docs.amd.com/gpu-atomics-operation.html#hw-atomics-operation-support)
page.

Type name |
int8 |
int16 |
int32 |
int64 |
|---|---|---|---|---|
CDNA1 |
❌ |
❌ |
✅ |
✅ |
CDNA2 |
❌ |
❌ |
✅ |
✅ |
CDNA3 |
❌ |
❌ |
✅ |
✅ |
RDNA3 |
❌ |
❌ |
✅ |
✅ |
RDNA4 |
❌ |
❌ |
✅ |
✅ |

Type name |
float4 |
float6 (E2M3) |
float6 (E3M2) |
float8 (E4M3) |
float8 (E5M2) |
|---|---|---|---|---|---|
CDNA1 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA2 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA3 |
❌ |
❌ |
❌ |
❌ |
❌ |
CDNA4 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA2 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA3 |
❌ |
❌ |
❌ |
❌ |
❌ |
RDNA4 |
❌ |
❌ |
❌ |
❌ |
❌ |

Type name |
2 x float16 |
2 x bfloat16 |
tensorfloat32 |
float32 |
float64 |
|---|---|---|---|---|---|
CDNA1 |
✅ |
✅ |
❌ |
✅ |
❌ |
CDNA2 |
✅ |
✅ |
❌ |
✅ |
✅ |
CDNA3 |
✅ |
✅ |
❌ |
✅ |
✅ |
CDNA4 |
✅ |
✅ |
❌ |
✅ |
✅ |
RDNA2 |
❌ |
❌ |
❌ |
✅ |
❌ |
RDNA3 |
❌ |
❌ |
❌ |
✅ |
❌ |
RDNA4 |
✅ |
✅ |
❌ |
✅ |
❌ |

Note

You can emulate atomic operations using software for cases that are not natively supported. Software-emulated atomic operations have a high negative performance impact when they frequently access the same memory address.

## Data type support in ROCm libraries[#](https://rocm.docs.amd.com#data-type-support-in-rocm-libraries)

ROCm library support for int8, float8 (E4M3), float8 (E5M2), int16, float16, bfloat16, int32, tensorfloat32, float32, int64, and float64 is listed in the following tables.

### Libraries input/output type support[#](https://rocm.docs.amd.com#libraries-input-output-type-support)

The following tables list ROCm library support for specific input and output data types. Select a library from the below table to view the supported data types.

For more information, please visit [Composable Kernel](https://rocm.docs.amd.com/projects/composable_kernel/en/docs-7.2.4/reference/Composable_Kernel_supported_scalar_types.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
int32 |
✅ |
float4 |
✅ |
float6 (E2M3) |
✅ |
float6 (E3M2) |
✅ |
float8 (E4M3) |
✅ |
float8 (E5M2) |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [MIGraphX](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-7.2.4/reference/MIGraphX-cpp.html).

Data Type |
Support |
|---|---|
int8 |
⚠️ |
int16 |
✅ |
int32 |
✅ |
int64 |
✅ |
float8 (E4M3) |
✅ |
float8 (E5M2) |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [MIOpen](https://rocm.docs.amd.com/projects/MIOpen/en/docs-7.2.4/reference/datatypes.html).

Data Type |
Support |
|---|---|
int8 |
⚠️ |
int32 |
⚠️ |
float8 (E4M3) |
⚠️ |
float8 (E5M2) |
⚠️ |
float16 |
✅ |
bfloat16 |
⚠️ |
float32 |
✅ |
float64 |
⚠️ |

For more information, please visit [RCCL](https://rocm.docs.amd.com/projects/rccl/en/docs-7.2.4/api-reference/library-specification.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
int32 |
✅ |
int64 |
✅ |
float8 (E4M3) |
✅ |
float8 (E5M2) |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [hipBLAS](https://rocm.docs.amd.com/projects/hipBLAS/en/docs-7.2.4/reference/data-type-support.html).

Data Type |
Support |
|---|---|
float16 |
⚠️ |
bfloat16 |
⚠️ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-7.2.4/reference/data-type-support.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
float4 |
✅ |
float6 (E2M3) |
✅ |
float6 (E3M2) |
✅ |
float8 (E4M3) |
✅ |
float8 (E5M2) |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |

For more information, please visit hipFFT.

Data Type |
Support |
|---|---|
float32 |
✅ |
float64 |
✅ |

For more information, please visit [hipRAND](https://rocm.docs.amd.com/projects/hipRAND/en/docs-7.2.4/api-reference/data-type-support.html).

Data Type |
Support |
|---|---|
int8 |
Output only |
int16 |
Output only |
int32 |
Output only |
int64 |
Output only |
float16 |
Output only |
float32 |
Output only |
float64 |
Output only |

For more information, please visit [hipSOLVER](https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-7.2.4/reference/precision.html).

Data Type |
Support |
|---|---|
float32 |
✅ |
float64 |
✅ |

For more information, please visit [hipSPARSE](https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-7.2.4/reference/precision.html).

Data Type |
Support |
|---|---|
float32 |
✅ |
float64 |
✅ |

For more information, please visit [hipSPARSELt](https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-7.2.4/reference/data-type-support.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
float8 (E4M3) |
✅ |
float8 (E5M2) |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |

For more information, please visit [rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/docs-7.2.4/reference/data-type-support.html).

Data Type |
Support |
|---|---|
float16 |
⚠️ |
bfloat16 |
⚠️ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/docs-7.2.4/reference/api.html).

Data Type |
Support |
|---|---|
float16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [rocRAND](https://rocm.docs.amd.com/projects/rocRAND/en/docs-7.2.4/api-reference/data-type-support.html).

Data Type |
Support |
|---|---|
int8 |
Output only |
int16 |
Output only |
int32 |
Output only |
int64 |
Output only |
float16 |
Output only |
float32 |
Output only |
float64 |
Output only |

For more information, please visit [rocSOLVER](https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-7.2.4/reference/precision.html).

Data Type |
Support |
|---|---|
float32 |
✅ |
float64 |
✅ |

For more information, please visit [rocSPARSE](https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-7.2.4/reference/precision.html).

Data Type |
Support |
|---|---|
float32 |
✅ |
float64 |
✅ |

For more information, please visit [rocWMMA](https://rocm.docs.amd.com/projects/rocWMMA/en/docs-7.2.4/api-reference/api-reference-guide.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
int32 |
Output only |
float8 (E4M3) |
Input only |
float8 (E5M2) |
Input only |
float16 |
✅ |
bfloat16 |
✅ |
tensorfloat32 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [Tensile](https://rocm.docs.amd.com/projects/Tensile/en/docs-7.2.4/src/reference/precision-support.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
int32 |
✅ |
float8 (E4M3) |
✅ |
float8 (E5M2) |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
tensorfloat32 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit hipCUB.

Data Type |
Support |
|---|---|
int8 |
✅ |
int16 |
✅ |
int32 |
✅ |
int64 |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [hipTensor](https://rocm.docs.amd.com/projects/hipTensor/en/docs-7.2.4/api-reference/api-reference.html).

Data Type |
Support |
|---|---|
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit [rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/data-type-support.html).

Data Type |
Support |
|---|---|
int8 |
✅ |
int16 |
✅ |
int32 |
✅ |
int64 |
✅ |
float16 |
✅ |
bfloat16 |
✅ |
float32 |
✅ |
float64 |
✅ |

For more information, please visit rocThrust.

Data Type |
Support |
|---|---|
int8 |
✅ |
int16 |
✅ |
int32 |
✅ |
int64 |
✅ |
float16 |
⚠️ |
bfloat16 |
⚠️ |
float32 |
✅ |
float64 |
✅ |

Note

The meaning of partial support depends on the library. Please refer to the individual libraries’ documentation for more information.

Note

As random number generation libraries, rocRAND and hipRAND only specify output data types for the random values they generate, with no need for input data types.

Note

hipBLASLt supports additional data types as internal compute types, which may
differ from the supported input/output types shown in the tables above. While
TensorFloat32 is not supported as an input or output type in this library, it
is available as an internal compute type. For complete details on supported
compute types, refer to the [hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-7.2.4/reference/data-type-support.html)
documentation.

### hipDataType enumeration[#](https://rocm.docs.amd.com#hipdatatype-enumeration)

The `hipDataType`

enumeration defines data precision types and is primarily
used when the data reference itself does not include type information, such as
in `void*`

pointers. This enumeration is mainly utilized in BLAS libraries.
The HIP type equivalents of the `hipDataType`

enumeration are listed in the
following table with descriptions and values.

hipDataType |
HIP type |
Value |
Description |
|---|---|---|---|
|
|
3 |
8-bit real signed integer. |
|
|
8 |
8-bit real unsigned integer. |
|
|
20 |
16-bit real signed integer. |
|
|
22 |
16-bit real unsigned integer. |
|
|
10 |
32-bit real signed integer. |
|
|
12 |
32-bit real unsigned integer. |
|
|
0 |
32-bit real single precision floating-point. |
|
|
1 |
64-bit real double precision floating-point. |
|
|
2 |
16-bit real half precision floating-point. |
|
|
14 |
16-bit real bfloat16 precision floating-point. |
|
|
28 |
8-bit real float8 precision floating-point (OCP version). |
|
|
29 |
8-bit real bfloat8 precision floating-point (OCP version). |
|
|
31 |
6-bit real float6 precision floating-point. |
|
|
32 |
6-bit real bfloat6 precision floating-point. |
|
|
33 |
4-bit real float4 precision floating-point. |
|
|
1000 |
8-bit real float8 precision floating-point (FNUZ version). |
|
|
1001 |
8-bit real bfloat8 precision floating-point (FNUZ version). |

The full list of the `hipDataType`

enumeration listed in [library_types.h](https://github.com/ROCm/hip/blob/amd-staging/include/hip/library_types.h).