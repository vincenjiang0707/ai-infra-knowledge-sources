source: https://docs.nvidia.com/cuda/cutile-python/execution.html

# Execution Model[#](https://docs.nvidia.com#execution-model)

## Abstract Machine[#](https://docs.nvidia.com#abstract-machine)

A *tile kernel* is executed by logical thread [blocks](https://docs.nvidia.com#block) organized in a 1D,
2D, or 3D *grid*.

Each *block* runs on a subset of a GPU defined by the underlying compiler implementation.
Every [block](https://docs.nvidia.com#block) executes the body of the [kernel](https://docs.nvidia.com#execution-tile-kernels):
scalar operations run serially on a single thread, while array operations
run collectively in parallel across all threads of the [block](https://docs.nvidia.com#block).

Tile programs express [block](https://docs.nvidia.com#block)-level parallelism only with no exposure to
individual threads within the block.

Explicit synchronization or communication within a [block](https://docs.nvidia.com#block) is not permitted,
but is allowed between different [blocks](https://docs.nvidia.com#block).

A [block](https://docs.nvidia.com#block) defines the unit of execution and a [tile](https://docs.nvidia.com/data.html#data-tiles-and-scalars) defines unit of data,
which shall not be confused. A single block may operate on multiple [tiles](https://docs.nvidia.com/data.html#data-tiles-and-scalars)
with different shapes originating from different [global arrays](https://docs.nvidia.com/data.html#data-global-arrays).

## Execution Spaces[#](https://docs.nvidia.com#execution-spaces)

cuTile code runs on one or more *targets*. A target is an execution environment
defined by its hardware resources and programming model.

The set of targets where a construct can be used is called its *execution space*.
cuTile defines three execution spaces:

*Host code*— all CPU targets.*SIMT code*— all CUDA SIMT targets. (Historically called*device code*; we avoid that term to prevent ambiguity.)*Tile code*— all CUDA tile targets.

Some constructs span multiple execution spaces. For example,
[ cdiv()](https://docs.nvidia.com/generated/cuda.tile.cdiv.html#cuda.tile.cdiv) is usable in both host code and tile code.

A function whose decorator explicitly specifies its execution space is called
an *annotated function*.

## Tile Functions[#](https://docs.nvidia.com#tile-functions)

-
*class*cuda.tile.function(*func=None*,*/*,***,*host=False*,*tile=True*)[#](https://docs.nvidia.com#cuda.tile.function) *Tile functions*are functions that are usable in[tile code](https://docs.nvidia.com#tile-code).This decorator indicates what

[execution spaces](https://docs.nvidia.com#execution-execution-spaces)a function can be called from. With no arguments, it denotes a tile-only function.When an unannotated function is called by a

[tile function](https://docs.nvidia.com#execution-tile-functions), tile shall be added to the unannotated function’s execution space. This process is recursive. No explicit annotation is required.The types usable as parameters to a

[tile function](https://docs.nvidia.com#execution-tile-functions)are described in the[data model](https://docs.nvidia.com/data.html#data-data-model).

## Tile Kernels[#](https://docs.nvidia.com#execution-tile-kernels)

-
*class*cuda.tile.kernel(*function=None*,*/*,***kwargs*)[#](https://docs.nvidia.com#cuda.tile.kernel) A

*tile kernel*is a function executed by each[block](https://docs.nvidia.com#block)in a[grid](https://docs.nvidia.com#grid).Functions with this decorator are

[kernels](https://docs.nvidia.com#execution-tile-kernels).[Kernels](https://docs.nvidia.com#execution-tile-kernels)are the entry points of[tile code](https://docs.nvidia.com#tile-code). Their[execution space](https://docs.nvidia.com#execution-execution-spaces)shall be only[tile code](https://docs.nvidia.com#tile-code); they cannot be called from[host code](https://docs.nvidia.com#host-code).Kernels cannot be called directly. Instead, use

to queue a kernel for execution over a grid.`launch()`

The types usable as parameters to a

[kernel](https://docs.nvidia.com#execution-tile-kernels)are described in the[data model](https://docs.nvidia.com/data.html#data-data-model).- Parameters:
**num_ctas**– Number of CTAs in a CGA. Must be a power of 2 between 1 and 16, inclusive. Default: None (auto).**occupancy**– Expected number of active CTAs per SM, [1, 32]. Default: None (auto).**opt_level**– Optimization level [0, 3], default 3.**num_worker_warps**– Number of warps in the CUDA core warp groups in a warp-specialized kernel. The compiler may add warps (e.g., for asynchronous memory transfers) that are not counted here. This value does not represent the total warp count. It’s worth tuning when a warp-specialized kernel has high register pressure that other approaches cannot resolve. Normalization-style kernels with large tiles are the canonical cases. Must be either 4 or 8. Default: None (auto). Since CTK 13.3. Ignored with a warning otherwise.


Target-specific values for the compiler options above can be provided using a

object.`ByTarget`

-
replace_hints(
***hints*)[#](https://docs.nvidia.com#cuda.tile.kernel.replace_hints) Return a new kernel with updated compiler hints.

Notes:

Because hints affects compilation, the returned object will have its own JIT cache.

Examples:

@ct.kernel(occupancy=2) def kernel(): pass # compile ct.launch(torch.cuda.current_stream(), (1,), kernel, ()) # cache hit ct.launch(torch.cuda.current_stream(), (1,), kernel, ()) new_kernel = kernel.replace_hints(occupancy=4) # compile with new hints ct.launch(torch.cuda.current_stream(), (1,), new_kernel, ()) # cache hit ct.launch(torch.cuda.current_stream(), (1,), new_kernel, ())

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel(occupancy=2) def kernel(): pass # compile ct.launch(torch.cuda.current_stream(), (1,), kernel, ()) # cache hit ct.launch(torch.cuda.current_stream(), (1,), kernel, ()) new_kernel = kernel.replace_hints(occupancy=4) # compile with new hints ct.launch(torch.cuda.current_stream(), (1,), new_kernel, ()) # cache hit ct.launch(torch.cuda.current_stream(), (1,), new_kernel, ()) torch.cuda.synchronize()



- cuda.tile.launch(
*stream*,*grid*,*kernel*,*kernel_args*,*/*,***,*programmatic_dependent_launch=False*,Launch a cuTile kernel.


[#](https://docs.nvidia.com#cuda.tile.launch)

## Python Subset[#](https://docs.nvidia.com#python-subset)

[Tile code](https://docs.nvidia.com#tile-code) supports a subset of the Python language.
There is no Python runtime within [tile code](https://docs.nvidia.com#tile-code).

Only Python features explicitly listed in this document are supported. Many features — such as exceptions, and coroutines — are not supported today.

### Object Model & Lifetimes[#](https://docs.nvidia.com#object-model-lifetimes)

All objects created within [tile code](https://docs.nvidia.com#tile-code) are immutable.
Any operation that would conceptually modify an object instead creates and returns a new object.
Attributes cannot be added to objects dynamically.

Global [arrays](https://docs.nvidia.com/data.html#data-global-arrays) are views that can read and write global device memory, but the views themselves
are also immutable.

The caller of a [kernel](https://docs.nvidia.com#execution-tile-kernels) must ensure that:

### Control Flow[#](https://docs.nvidia.com#control-flow)

Python control flow statements (`if`

, `for`

, `while`

, etc.) are usable in [tile code](https://docs.nvidia.com#tile-code)
and can be arbitrarily nested.

#### Current limitations[#](https://docs.nvidia.com#current-limitations)

[Tile code](https://docs.nvidia.com#tile-code) imposes additional restrictions on control flow:

`step`

must be strictly positive.Negative-step ranges such as

`range(10, 0, -1)`

are not supported today. Passing a negative step indirectly via a variable may cause undefined behavior.

## Tile Parallelism[#](https://docs.nvidia.com#tile-parallelism)

When a [block](https://docs.nvidia.com#block) executes a function that takes [tiles](https://docs.nvidia.com/data.html#data-tiles-and-scalars) as parameters, it may
parallelize evaluation across the [block](https://docs.nvidia.com#block)’s execution resources.

## Constantness[#](https://docs.nvidia.com#constantness)

### Constant Expressions & Objects[#](https://docs.nvidia.com#constant-expressions-objects)

Some facilities require parameters whose values are known at compile time.
*Constant expressions* produce *constant objects* suitable for such parameters.
Constant expressions are:

A literal object.

Integer arithmetic expressions where all the operands are literal objects.

A local object or parameter that is assigned from a literal object or constant expression.

A global object that is defined at the time of compilation or launch.


By default, numeric constants are *loosely typed*: integer constants have
infinite precision and floating-point constants are stored in IEEE 754 double
precision, until used in a context that requires a specific-width type.

A *strictly typed* constant is created by calling a dtype constructor,
e.g. `ct.int16(5)`

. Combining a strictly typed constant with a loosely typed
constant yields a strictly typed constant:
`ct.int16(5) + 2`

produces a strictly typed `int16`

constant 7.

Combining two strictly typed constants also produces a strictly typed constant,
with the regular [type promotion](https://docs.nvidia.com/data.html#data-arithmetic-promotion) rules applied.
For example, `ct.int16(5) + ct.int32(7)`

produces a strictly typed `int32`

constant 12.

### Constant Embedding[#](https://docs.nvidia.com#constant-embedding)

If a [kernel](https://docs.nvidia.com#execution-tile-kernels) parameter is *constant embedded*, then:

Every use of the parameter behaves as if replaced by its literal value.

A distinct

[machine representation](https://docs.nvidia.com/interoperability.html#interoperability-machine-representation)of the[kernel](https://docs.nvidia.com#execution-tile-kernels)is generated for each unique value of the parameter. Note: The[kernel](https://docs.nvidia.com#execution-tile-kernels)is compiled once per unique value, even if JIT caching is enabled.

## Type Annotations[#](https://docs.nvidia.com#type-annotations)

Kernel parameter type annotations use `typing.Annotated`

metadata to control
constant embedding, array shape and index metadata, the integer dtype of scalar
parameters, and list element types.

### Constant Annotations[#](https://docs.nvidia.com#constant-annotations)

```
import cuda.tile as ct
```

```
def needs_constant(x: ct.Constant):
pass
def needs_constant_int(x: ct.Constant[int]):
pass
```

-
*class*cuda.tile.ConstantAnnotation[#](https://docs.nvidia.com#cuda.tile.ConstantAnnotation) A

`typing.Annotated`

metadata class indicating that an object shall be[constant embedded](https://docs.nvidia.com#execution-constant-embedding).If an object of this class is passed as a metadata argument to a

`typing.Annotated`

type hint on a parameter, then the parameter shall be a constant embedded.

-
cuda.tile.Constant
[#](https://docs.nvidia.com#cuda.tile.Constant) A type hint indicating that a value shall be

[constant embedded](https://docs.nvidia.com#execution-constant-embedding). It can be used either with (`Constant[int]`

) or without (`Constant`

, meaning a constant of any type) an underlying type hint.alias of

`Annotated`

[`T`

, ConstantAnnotation()]

### Array Annotations[#](https://docs.nvidia.com#array-annotations)

-
*class*cuda.tile.ArrayAnnotation( ***,*index_dtype=<DType 'int32'>*,*static_shape_dims=()*,*static_stride_dims=()*,A

`typing.Annotated`

metadata class for array parameters.-
index_dtype
[#](https://docs.nvidia.com#cuda.tile.ArrayAnnotation.index_dtype) Data type for shape and stride values. Must be

`int32`

or`int64`

. Use`int64`

to enable support for tensors whose shape or stride values exceed the range of a 32-bit integer.

-
static_shape_dims
[#](https://docs.nvidia.com#cuda.tile.ArrayAnnotation.static_shape_dims) Shape dimensions to specialize to their launch-time values, making them compile-time constants inside the kernel.

- Type:
tuple[int, …]



-
static_stride_dims
[#](https://docs.nvidia.com#cuda.tile.ArrayAnnotation.static_stride_dims) Stride dimensions to specialize to their launch-time values, making them compile-time constants inside the kernel. This is the sole source of static strides for the array: once any dimension is listed, the dispatcher stops inferring

`stride == 1`

for*every*dimension of it, so list the contiguous dimension explicitly to keep it a compile-time constant.- Type:
tuple[int, …]



Example:

@ct.kernel def my_kernel( x: Annotated[ct.Array, ct.ArrayAnnotation(static_shape_dims=(0,))], y: Annotated[ct.Array, ct.ArrayAnnotation(static_shape_dims=(0, -1))], z: Annotated[ct.Array, ct.ArrayAnnotation(static_stride_dims=(0, -1))], ): # x.shape[0] is a compile-time constant # y.shape[0] and y.shape[-1] are compile-time constants # z.strides[0] and z.strides[-1] are compile-time constants ... # Reusable alias combining int64 indexing with a static dimension: BigStaticDim0 = Annotated[ ct.Array, ct.ArrayAnnotation(index_dtype=ct.int64, static_shape_dims=(0,)) ]

-
index_dtype

[#](https://docs.nvidia.com#cuda.tile.ArrayAnnotation)

-
cuda.tile.IndexedWithInt64
[#](https://docs.nvidia.com#cuda.tile.IndexedWithInt64) A type hint indicating that an array uses i64 for shape and stride.

Example:

@ct.kernel def my_kernel(big: ct.IndexedWithInt64, small): # big.shape[i] is i64, small.shape[i] is i32 ...

alias of

`Annotated`

[`T`

,(index_dtype=`ArrayAnnotation`

`int64`

, static_shape_dims=(), static_stride_dims=())]

### Scalar Annotations[#](https://docs.nvidia.com#scalar-annotations)

-
cuda.tile.ScalarInt64
[#](https://docs.nvidia.com#cuda.tile.ScalarInt64) A type hint indicating that a scalar integer parameter uses int64.

By default, integer kernel parameters are inferred as int32. Use this annotation to force int64 inference for parameters that need the wider range.

Example:

@ct.kernel def my_kernel(small_int, large_int: ct.ScalarInt64): # small_int is inferred as int32 # large_int is inferred as int64 ...

alias of

`Annotated`

[`T`

,`ScalarAnnotation`

(dtype=`int64`

)]

### List Annotations[#](https://docs.nvidia.com#list-annotations)

-
*class*cuda.tile.ListAnnotation(***,*element*)[#](https://docs.nvidia.com#cuda.tile.ListAnnotation) A

`typing.Annotated`

metadata class for list parameters.-
element
[#](https://docs.nvidia.com#cuda.tile.ListAnnotation.element) Annotation for the list’s element type. Must be an

or an`ArrayAnnotation`

`Annotated`

type whose metadata contains an(e.g.`ArrayAnnotation`

).`IndexedWithInt64`

- Type:
Any



-
element