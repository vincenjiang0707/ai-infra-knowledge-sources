source: https://docs.nvidia.com/cuda/cutile-python/compilation.html

# Compilation and Export[#](https://docs.nvidia.com#compilation-and-export)

When a kernel function marked with [ @ct.kernel](https://docs.nvidia.com/execution.html#cuda.tile.kernel) is launched
using

[, it is specialized and compiled just in time (JIT) for the concrete launch arguments. It is also possible to compile a kernel ahead of time (AOT) and export it as a CUDA binary (cubin) file, or as a TileIR bytecode file.](https://docs.nvidia.com/execution.html#cuda.tile.launch)

`ct.launch()`

While just-in-time compilation provides the convenience of automatic kernel specialization, ahead-of-time compilation requires the user to precisely describe the arguments for which the kernel is being compiled, including their types and additional constraints (assumptions) imposed on their values.

The main API entry point for ahead-of-time compilation
is [ cuda.tile.compilation.export_kernel()](https://docs.nvidia.com#cuda.tile.compilation.export_kernel):

- cuda.tile.compilation.export_kernel(
*kernel*,*signatures*,*output_file*,***,*gpu_code=None*,*output_format*,*bytecode_version=None*,Compile and export a kernel.

- Parameters:
**kernel**() – A kernel function to export.*cuda.tile.kernel***signatures**(*Sequence**[**cuda.tile.compilation.KernelSignature**]*) – A non-empty list of signatures for which to compile the kernel.**output_file**(*IO**|**str**|**bytes**|**os.PathLike*) – Either a filename or a binary file-like object to write the output to. To save the result in memory, you can pass an instance of the io.BytesIO standard library class.**gpu_code**(*str**|**None*) – Name of the target GPU for which to compile the kernel (e.g., “sm_100”). Required when output_format is “cubin”. It can be set to None when output_format is “tileir_bytecode” to export architecture-independent bytecode (requires a bytecode version of “13.3” or later).**output_format**(*str*) – Set to “cubin” to export a CUDA binary file, or “tileir_bytecode” to export a TileIR bytecode file.**bytecode_version**(*str**|**None*) – Set to None to automatically detect the latest TileIR bytecode version supported by the compiler (default). Otherwise, it must be a string of the form “major.minor” that specifies the version of the TileIR bytecode to use (e.g., “13.1”).



[#](https://docs.nvidia.com#cuda.tile.compilation.export_kernel)

## Kernel Signatures[#](https://docs.nvidia.com#kernel-signatures)

There are two ways to construct a [ KernelSignature](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature) object for use with

[. The recommended way is to do it explicitly, by instantiating a](https://docs.nvidia.com#cuda.tile.compilation.export_kernel)

`export_kernel()`

[object and providing a list of manually constructed](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature)

`KernelSignature`

[objects.](https://docs.nvidia.com#cuda.tile.compilation.ParameterConstraint)

`ParameterConstraint`

Alternatively, one may use [ KernelSignature.from_kernel_args()](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature.from_kernel_args) to obtain a signature
that would be used if the kernel was compiled just-in-time for the given example arguments.
While convenient, this approach may create undesired assumptions on kernel parameters. For example,
if the base address of an example array argument happens to be divisible by 16, an assumption may
be made that it will always be so. Launching the exported kernel with an array that doesn’t
satisfy this assumption would then result in undefined behavior. It is therefore recommended to limit
the use of this approach to testing or prototyping.

-
*class*cuda.tile.compilation.KernelSignature(*parameters*,*calling_convention*,*symbol=None*)[#](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature) Signature of a compiled kernel.

- Parameters:
**parameters**(*Sequence**[**ParameterConstraint**|**ConstantValue**|**tuple**]*) –For each parameter of the kernel’s Python function, a corresponding

instance.`ParameterConstraint`

Possible constraint classes are:

,`ScalarConstraint`

,`ArrayConstraint`

,`ListConstraint`

,`TupleConstraint`

,`ConstantConstraint`

`DataclassConstraint`

.A plain

(for example, a literal`ConstantValue`

`10`

), can be used as shorthand forwrapping the given value. Similarly, a plain`ConstantConstraint`

`tuple`

is shorthand for a.`TupleConstraint`

Each constraint must be compatible with annotations on the corresponding kernel parameter. For example, if a parameter is marked with

, then the corresponding constraint must be a`ct.Constant`

, or a nested`ConstantConstraint`

thereof (or a plain value according to the shorthand notation described above).`TupleConstraint`

**calling_convention**() –*CallingConvention*[Calling convention](https://docs.nvidia.com#compilation-callconv)to use.**symbol**(*str**|**None*) – Symbol name to use for the exported kernel. Set to None to automatically generate it from the Python function name and this signature, using a name mangling algorithm defined by the selected calling convention.


-
with_mangled_symbol(
*function_name*)[#](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature.with_mangled_symbol) Returns a copy of self with the symbol attribute replaced with a mangled name.

- Parameters:
**function_name**(*str*) – Function name to use as the base of the mangled symbol.- Returns:
KernelSignature

- Return type:


-
with_symbol(
*symbol*)[#](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature.with_symbol) Returns a copy of self with the symbol attribute replaced with the given value.

- Parameters:
**symbol**(*str**|**None*) – The new symbol name.- Returns:
KernelSignature

- Return type:


-
*static*from_kernel_args( *kernel*,*kernel_args*,*calling_convention*,***,*symbol=None*,Returns the signature that would be used if the kernel was compiled just-in-time for the given arguments.o

Warning

It is recommended to limit the use of this function to testing or prototyping. Deriving a kernel signature from example arguments may create unexpected assumptions on kernel parameters.

For example, if the base address of an example array argument happens to be divisible by 16, an assumption may be made that it will always be so. Launching the exported kernel with an array that doesn’t satisfy this assumption would result in undefined behavior.

- Parameters:
**kernel**() – A kernel function decorated with*cuda.tile.kernel*.`@ct.kernel`

**kernel_args**(*Sequence**[**Any**]*) – Tuple of kernel arguments, as if it were be passed to.`ct.launch()`

**calling_convention**() –*CallingConvention*[Calling convention](https://docs.nvidia.com#compilation-callconv)to use.**symbol**(*str**|**None*) – Specifies the symbol attribute of the returned signature. If set to None, the returned symbol will be automatically filled using a name mangling algorithm defined by the selected[calling convention](https://docs.nvidia.com#compilation-callconv).

- Returns:
KernelSignature

- Return type:


[#](https://docs.nvidia.com#cuda.tile.compilation.KernelSignature.from_kernel_args)

The [ ParameterConstraint](https://docs.nvidia.com#cuda.tile.compilation.ParameterConstraint) type alias is used as a type hint for a kernel parameter
constraint:

-
cuda.tile.compilation.ParameterConstraint
[#](https://docs.nvidia.com#cuda.tile.compilation.ParameterConstraint) alias of

|`ScalarConstraint`

|`ArrayConstraint`

|`ListConstraint`

|`TupleConstraint`

`DataclassConstraint`

|`ConstantConstraint`


-
*class*cuda.tile.compilation.ScalarConstraint(*dtype*)[#](https://docs.nvidia.com#cuda.tile.compilation.ScalarConstraint) Describes a scalar kernel parameter and associated compile-time assumptions.

- Parameters:
**dtype**() – Data type of the scalar.*DType*


-
*class*cuda.tile.compilation.ArrayConstraint( *dtype*,*ndim*,***,*index_dtype*,*stride_lower_bound_incl*,*alias_groups*,*may_alias_internally*,*stride_constant=None*,*shape_constant=None*,*stride_divisible_by=1*,*shape_divisible_by=1*,*base_addr_divisible_by=1*,Describes an array kernel parameter and associated compile-time assumptions.

- Parameters:
**dtype**() – Data type of the array.*DType***ndim**(*int*) – Number of dimensions of the array, also known as rank.**index_dtype**() – Data type used to represent array’s shape, strides and indices. Supported values are*DType*and`ct.int32`

. Using`ct.int64`

`int64`

enables support for arrays whose shape or stride values exceed the range of a 32-bit integer.**stride_lower_bound_incl**(*Sequence**[**int**|**None**]**|**int**|**None*) – For each dimension of the array, an optional inclusive lower bound for its stride. If all dimensions have the same lower bound, a single number can be passed instead of a sequence. For example, passing 0 specifies that all strides are non-negative.**alias_groups**(*Sequence**[**str**]*) – When set to an empty sequence, specifies that this array may not alias any other parameter. Otherwise, it must be a sequence of arbitrary strings, referred to as “alias groups”. Two parameters are allowed to alias each other if and only if they have an alias group in common.**may_alias_internally**(*bool*) – Indicates whether two distinct in-bounds indices are allowed to point to the same memory location. For example, this can happen if the array has a zero stride. For most arrays produced by major tensor libraries, this can be assumed to be false. Setting this to True may disable certain optimizations of loads and stores to/from this array.**stride_constant**(*Sequence**[**int**|**None**]**|**None*) – For each dimension of the array, an optional constant value of its stride. For example, if the array is known to have a C-contiguous layout, the stride of the last dimension can be set to 1, which may enable certain optimizations of loads and stores from/to this array. Can be set to None if none of the dimensions have known strides (this is the default).**shape_constant**(*Sequence**[**int**|**None**]**|**None*) – For each dimension of the array, an optional constant value of its shape. Can be set to None if none of the dimensions have known shapes. Requires`cutile_python_v2`

. If`shape_constant[i]`

is set,`shape_divisible_by[i]`

is redundant and must be compatible (i.e.,`shape_constant[i]`

must be divisible by`shape_divisible_by[i]`

); it is then ignored.**stride_divisible_by**(*Sequence**[**int**]**|**int*) – For each dimension of the array, a factor by which its stride is assumed to be divisible. The value is given in array elements, not bytes. For example, a value of 8 for a float16 array indicates divisibility by 16 bytes, since each element of the array is 2 bytes wide. Value of 1 indicates that no assumption is made regarding the stride divisibility (this is the default).**shape_divisible_by**(*Sequence**[**int**]**|**int*) – For each dimension of the array, a factor by which its length is assumed to be divisible. The value is given in array elements, not bytes. For example, a value of 8 for a float16 array indicates divisibility by 16 bytes, since each element of the array is 2 bytes wide. Value of 1 indicates that no assumption is made regarding the shape divisibility (this is the default).**base_addr_divisible_by**(*int*) – Factor by which the array’s base address is assumed to be divisible. Value of 1 indicates that no assumption is made regarding the base address divisibility (this is the default).



[#](https://docs.nvidia.com#cuda.tile.compilation.ArrayConstraint)

-
*class*cuda.tile.compilation.ListConstraint(*element*,***,*alias_groups*,*elements_may_alias*)[#](https://docs.nvidia.com#cuda.tile.compilation.ListConstraint) Describes a list kernel parameter and associated compile-time assumptions.

- Parameters:
**element**() – Describes the element of this list. Currently, this must be an ArrayConstraint, since only lists of arrays are supported as kernel arguments.*ArrayConstraint***alias_groups**(*Sequence**[**str**]*) – Describes which other parameters the storage of this list is allowed to alias. Note that this is different from`element.alias_groups`

, which sets aliasing assumptions on the list elements. When set to an empty sequence, specifies that this list may not alias any other parameter. Otherwise, it must be a sequence of arbitrary strings, referred to as “alias groups”. Two parameters are allowed to alias each other if and only if they have an alias group in common.**elements_may_alias**(*bool*) – Specifies whether two distinct elements of this list are allowed to alias each other.



-
*class*cuda.tile.compilation.TupleConstraint(*items*)[#](https://docs.nvidia.com#cuda.tile.compilation.TupleConstraint) Describes a tuple kernel parameter.

- Parameters:
**items**(*tuple**[**ScalarConstraint**|**ArrayConstraint**|**ListConstraint**|**TupleConstraint**|**DataclassConstraint**|**ConstantConstraint**,**...**]*) – Per-item constraints.


-
*class*cuda.tile.compilation.ConstantConstraint(*value*)[#](https://docs.nvidia.com#cuda.tile.compilation.ConstantConstraint) Specifies the constant value of a kernel parameter marked with

.`ct.Constant`

- Parameters:
**value**(*ConstantValue*) – The value of the compile-time constant.


-
cuda.tile.compilation.ConstantValue
[#](https://docs.nvidia.com#cuda.tile.compilation.ConstantValue) alias of

`bool`

|`int`

|`float`


## Calling Conventions[#](https://docs.nvidia.com#calling-conventions)

A calling convention defines three aspects of the binary interface provided by an exported kernel:

The binary format and the order of kernel arguments, e.g. as passed to the

`cuLaunchKernel()`

CUDA Driver API function.The set of supported parameter constraints.

The name mangling algorithm used to automatically derive a symbol name from the kernel’s function name and a kernel signature.


Two calling conventions are available: `cutile_python_v1`

and `cutile_python_v2`

.
Both pass binary kernel arguments in the same order as the kernel parameters are declared
in the Python kernel function, except that parameters annotated with
[ ct.Constant](https://docs.nvidia.com/execution.html#cuda.tile.Constant) are omitted.

`cutile_python_v2`

extends `cutile_python_v1`

with support for tuple parameters
([) and static shapes (the](https://docs.nvidia.com#cuda.tile.compilation.TupleConstraint)

`TupleConstraint`

`shape_constant`

field of
[). New code should use](https://docs.nvidia.com#cuda.tile.compilation.ArrayConstraint)

`ArrayConstraint`

`cutile_python_v2`

.The following table lists the supported parameter constraints and their binary formats.
Constraints marked v2 require `cutile_python_v2`

.

Constraint Class |
Binary Format of Arguments |
|---|---|
Passed as a single argument of the corresponding type. For example, if the constraint’s
dtype is `int32_t` ;
`ct.float64` |
|
Passed as 1 + 2n arguments, where n is the number of dimensions (ndim) of the array.
The first argument is the device pointer to the base of the array’s data. It is followed
by n arguments representing the shape of the array. Finally, the last n arguments
represent the strides of the array.
The type of shape and stride arguments is determined by the The |
|
`ArrayConstraint` |
Passed as two arguments: a device pointer to the base of the list data and an |
The tuple’s elements are passed as consecutive arguments, as if each element were
an individual top-level parameter. The binary format of each element follows the same
rules as its corresponding constraint type (
`ArrayConstraint` |
|
Omitted from the launch arguments. |

Calling conventions are represented by the [ CallingConvention](https://docs.nvidia.com#cuda.tile.compilation.CallingConvention) class: