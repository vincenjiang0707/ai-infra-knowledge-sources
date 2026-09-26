source: https://docs.nvidia.com/cuda/cutile-python/generated/release_notes.html

# Release Notes[#](https://docs.nvidia.com#release-notes)

## 1.6.0 (2026-09-09)[#](https://docs.nvidia.com#release-1-6-0)

This release adds support for CTK 13.4 features, including programmatic
dependent launch, unchecked memory accesses, `ct.insert()`

, and
`float8_e5m3fnu`

scale dtype support for FP4 block-scaled MMA on Rubin. It
also adds finer control over compilation and execution with static array
strides and portable TileIR bytecode export. It expands the supported Python
subset with user-defined context managers, dataclass methods, `break`

in
non-static loops, and integer `divmod`

. Autotuning, JAX interoperability,
diagnostics, and floating-point behavior are also improved.

### CTK 13.4 features[#](https://docs.nvidia.com#ctk-13-4-features)

Add Programmatic Dependent Launch support with

,`ct.grid_dependency_control_launch_dependents()`

, and the`ct.grid_dependency_control_wait()`

`programmatic_dependent_launch`

option for.`ct.launch()`

Add a

`check_bounds`

option to,`ct.load()`

, and the`ct.store()`

and`TiledView.load()`

methods. It defaults to`TiledView.store()`

`True`

. Setting it to`False`

declares that every tile element is within the array bounds and skips bounds checking for faster access.Add

and`ct.insert()`

to create a new tile by replacing a subtile of a larger tile. This operation is the inverse of`Tile.insert()`

. The original tile remains unchanged.`ct.extract()`

Add

`float8_e5m3fnu`

scale dtype support for FP4 block-scaled MMA on Rubin (`sm_107`

).

### Features[#](https://docs.nvidia.com#features)

Add support for specializing array stride dimensions to their launch-time values, making them compile-time constants inside the kernel. Use

as`ct.ArrayAnnotation`

`Annotated`

metadata and list the dimensions to specialize, for example,`Annotated[ct.Array, ct.ArrayAnnotation(static_stride_dims=(0, 1))]`

. Once any static stride is specified, the dispatcher stops automatically inferring`stride == 1`

for all dimensions, so list the contiguous dimension explicitly if it should remain a compile-time constant.Add

, which statically asserts that a value is a compile-time constant.`ct.ensure_constant()`

Add IEEE rounding-mode support to floating-point

`astype()`

conversions.Add a

`propagate_nan`

option to,`ct.min()`

,`ct.max()`

,`ct.argmin()`

,`ct.argmax()`

, and`ct.minimum()`

. By default, NaN values are ignored. When enabled, a NaN propagates, min/max/minimum/maximum return NaN and argmin/argmax return the index of the first NaN.`ct.maximum()`


### Python features[#](https://docs.nvidia.com#python-features)

Add support for

`break`

in non-static`for`

loops.Add support for user-defined context managers created with

`@contextlib.contextmanager`

.Add support for user-defined dataclass methods:

`__post_init__()`

,`__call__()`

,`__getitem__()`

,`__setitem__()`

,`__repr__()`

, and`__str__()`

.Add

, as well as support for built-in`ct.divmod()`

`divmod()`

, for integer inputs only.Allow basic symbolic expressions to be constructed inside

.`ct.static_eval()`


### Enhancements[#](https://docs.nvidia.com#enhancements)

An array dimension whose stride is inferred to be one is no longer encoded as a static stride in the array’s type unless it is explicitly selected with

`ArrayAnnotation(static_stride_dims=...)`

. This allows more permissive type unification in control flow.Allow

to accept a function for its`ct.tune.exhaustive_search()`

`kernel`

argument that maps each configuration to the kernel to tune. Passing a fixed kernel continues to work as before.Allow

to export TileIR bytecode without specifying`export_kernel()`

`gpu_code`

when`output_format="tileir_bytecode"`

. This requires bytecode version 13.3 or later.Specialize the sliced axis produced by

to a compile-time constant dimension when both`Array.slice()`

`start`

and`stop`

are compile-time constants.On TileIR 13.4 or later, lower

`x ** y`

and`ct.pow(x, y)`

to integer-exponent`FPowI`

when`x`

is an unrestricted float and`y`

is an integer whose value range fits in a signed 32-bit integer. Other cases continue to promote the exponent to floating point and use`FPowF`

.Improve the diagnostic for a function whose return type differs across control-flow paths.

Change the second element of each entry in

from an exception class name to the exception class itself.`TuningResult.failures`


### Bug Fixes[#](https://docs.nvidia.com#bug-fixes)

Make

and`ct.argmin()`

ignore NaN values by default, consistent with`ct.argmax()`

`ct.min()`

and`ct.max()`

.Fix

compiling kernels for CUDA device 0 rather than for the device being launched on. Kernels are now compiled for the launch device’s architecture. Devices with the same architecture can still share a compiled kernel.`ct.launch()`

Fix an

`AttributeError`

when compiler crash dumps are enabled with`CUDA_TILE_ENABLE_CRASH_DUMP=1`

.Fix an internal compiler error when a runtime loop conditionally updates a loop-carried scalar.


### Tooling[#](https://docs.nvidia.com#tooling)

Add

`cutile-cache log`

, a command-line interface for inspecting compilation history. Cache metadata includes mangled kernel names, compiler versions, compilation dates and durations, and, with TileIR 13.4,`tileiras`

compiler remarks.

### Ecosystem[#](https://docs.nvidia.com#ecosystem)

Add support for tuple parameters in the JAX FFI integration.


## 1.5.0 (2026-07-08)[#](https://docs.nvidia.com#release-1-5-0)

This release adds finer control over kernel specialization by making selected array shape dimensions compile-time constants and declaring scalar divisibility assumptions. Autotuning is faster and can isolate hanging kernels. The supported Python subset now includes tuple comprehensions, tuple-valued kernel arguments, enums, dictionaries, and variadic keyword parameters.

### Features[#](https://docs.nvidia.com#id1)

Add

, a compiler hint that declares an integer scalar to be divisible by a constant. The compiler propagates this fact through arithmetic, which can prove the alignment of derived indices and pointer offsets and enable wider memory operations.`ct.assume_divisible_by(x, divisor)`

Add support for specializing array shape dimensions to their launch-time values, making them compile-time constants inside the kernel. Use

as`ct.ArrayAnnotation`

`Annotated`

metadata and list the dimensions to specialize, for example,`Annotated[ct.Array, ct.ArrayAnnotation(static_shape_dims=(0, -1))]`

.Add the

`single_run_timeout_sec`

argument toto prevent a hanging kernel from stalling the entire search.`ct.tune.exhaustive_search()`

Add support for passing Python tuples as kernel arguments. Elements may be arrays, scalars, lists, or nested tuples. Annotations may apply to the entire tuple or individual elements:

`ct.Constant[tuple[int, float]]`

makes the whole tuple compile-time constant, while`tuple[ct.Constant[int], float]`

makes only the first element constant.

### Python features[#](https://docs.nvidia.com#id2)

Add support for tuple comprehensions.

Add support for the

`in`

and`not in`

operators on tuples.Add limited support for dictionaries, variadic keyword parameters in user-defined functions (for example,

`def foo(**kwargs)`

), and dictionary unpacking (for example,`foo(x, **y)`

).Add comparison and constructor support for Python

`enum.Enum`

inside kernels. Enum members can be compared with`==`

and`!=`

and constructed from a constant value, such as`Color(0)`

.Add support for printing dataclass instances.

Allow frozen dataclass instances to be used as globals in device code.


### Bug Fixes[#](https://docs.nvidia.com#id3)

Fix a bug in automatic propagation of divisibility when an assumed variable created in a block is used outside that block.

Fix a bug where strictly typed numeric constants (for example,

`ct.uint32(-3)`

,`ct.int8(300)`

, and`ct.float16(0.2)`

) were not converted according to their dtype. Out-of-range integers are now wrapped to the dtype’s range, and floating-point values are rounded or clamped according to the dtype’s precision and range.Honor wrappers installed on user-defined functions, including wrappers added by decorators that use

`functools.wraps()`

.Reject repeated axes in the

`order`

arguments of`load()`

,`store()`

, and`num_tiles()`

.

### Enhancements[#](https://docs.nvidia.com#id4)

Extend

with optional`ct.arange()`

`start`

and`step`

arguments:`ct.arange(size, start=0, step=1, dtype=...)`

.`size`

must be a constant integer, while`start`

and`step`

may be dynamic values. For example,`ct.arange(8, start=7, step=-1, dtype=ct.int32)`

creates a reversed range.Improve exhaustive search performance by stopping early for slow configurations.


### ABI Changes[#](https://docs.nvidia.com#abi-changes)

Introduce

for kernels with static shape annotations or tuple arguments.`calling convention v2`


## 1.4.0 (2026-05-26)[#](https://docs.nvidia.com#release-1-4-0)

This release highlights compatibility with CTK 13.3 which introduces Hopper(sm_90) GPU support, block-scaled MMA, new float dtypes, pack/unpack operations, atomic store operations, load and store with advanced indexing, tiled view with gapped or overlapped tile access, and support for large arrays and scalars. It also adds support for Python 3.14 including free-threading, star “*” expression, and frozen dataclasses, as well as integration with JAX.

### CTK 13.3 features[#](https://docs.nvidia.com#ctk-13-3-features)

Support Hopper (sm_90 family) GPUs.

Add

`float8_e8m0fnu`

and`float4_e2m1fn`

restricted float dtype.Add

operation for block-scaled matrix multiply-accumulate.`ct.mma_scaled()`

Add

operation that flattens a tile and reinterprets its raw bytes as a 1D uint8 tile;`ct.pack_to_bytes()`

is the inverse of`ct.unpack_from_bytes()`

.`ct.pack_to_bytes()`

Add

and`ct.load_advanced_indexing()`

for gathering/scattering along one dimension while slicing on other dimensions.`ct.store_advanced_indexing()`

Add

and more atomic methods on`atomic_store_add`

for performing element-wise atomic read-modify-write operations on a tiled view at a given tile index.`TiledView`

Add support for

with`Array.tiled_view()`

`traversal_steps`

for creating a tiled space with overlapped or spaced tiles.now accepts a`ByTarget`

`default`

value that applies to all architectures (e.g.`ByTarget(sm_100=8, default=2)`

), allowing generated TileIR bytecode to be independent of the GPU architecture.Add

for creating a tile from a scalar (yielding a 0-d tile) or a (possibly nested) tuple of scalars whose nesting determines the tile’s shape.`ct.astile()`

Support large arrays (>2B elements):

New

annotation for array kernel parameters whose shape or stride values exceed the range of a 32-bit integer. Arrays without the annotation continue to use`ct.IndexedWithInt64`

`int32`

for shape and stride.New

annotation that forces a scalar integer kernel parameter to be inferred as`ct.ScalarInt64`

`int64`

instead of the default`int32`

.

Add

`use_fast_acc`

option toto enable fast accumulation mode for FP8 inputs (`ct.mma()`

`float8_e4m3fn`

,`float8_e5m2`

) on Hopper GPUs.Add a new kernel hint

`num_worker_warps`

to.`ct.kernel`

now supports`ct.atomic_add()`

`bfloat16`

operands on Hopper (sm_90) and newer architectures.Optional

`rounding_mode`

parameter for(supports`ct.exp()`

`RoundingMode.FULL`

and`RoundingMode.APPROX`

for f32).

### Python features[#](https://docs.nvidia.com#id5)

Add Python 3.14 and Python 3.14t (free-threading) support.

Add support for frozen dataclasses.

Add support for passing a tuple as a starred function argument, e.g.

`foo(a, *b, c)`

.Add support for variadic parameters in user-defined functions, e.g.

`def foo(*args)`

.

### Enhancements[#](https://docs.nvidia.com#id6)

now raises a compile-time`ct.extract()`

`TileTypeError`

when a constant index is out of bounds for the tile grid. Dynamic indices are unaffected.and the`ct.floordiv()`

`//`

operator now support floating-point operands.

### Ecosystem[#](https://docs.nvidia.com#id7)

Add support for JAX via

.`ct.jax.cutile_call()`


## 1.3.0 (2026-04-20)[#](https://docs.nvidia.com#release-1-3-0)

### Features[#](https://docs.nvidia.com#id8)

Add API for ahead-of-time compilation and export via

.`compilation.export_kernel()`


See the[Compilation and Export](https://docs.nvidia.com/compilation.html)section for more details.Add API for autotuning via

and the following helpers:`tune.exhaustive_search()`

Add API

to get a new kernel with updated hints.`kernel.replace_hints()`

Add API function

for temporarily setting the timeout on the tileiras compiler.`compiler_timeout()`


See the[Autotuning](https://docs.nvidia.com/performance.html#autotuning)section for more details.

Add API

to create a tiled view of an array with a fixed tile shape and padding mode.`Array.tiled_view()`


### Enhancements[#](https://docs.nvidia.com#id9)

Add support for specifying

`memory_order`

and`memory_scope`

on`cuda.tile.load`

and`cuda.tile.store`

operations.Improve

`print()`

to handle tuple and nested fstring.

### Bug Fixes[#](https://docs.nvidia.com#id10)

Fix a bug where restricted float dtype with simple reduce and scan did not raise proper

`TileTypeError`

.

### ABI Changes[#](https://docs.nvidia.com#id11)

Change kernel ABI convention to omit parameters annotated with

`cuda.tile.Constant`

.

## 1.2.0 (2026-03-05)[#](https://docs.nvidia.com#release-1-2-0)

### CTK 13.2 features[#](https://docs.nvidia.com#ctk-13-2-features)

Support Ampere and Ada (sm80 family) GPUs.

Support

`pip install cuda-tile[tileiras]`

to use`tileiras`

from Python environment without system-wide CTK installation.Add

`ct.atan2(y, x)`

operation for computing the arctangent of y/x.Add optional

`rounding_mode`

parameter for`ct.tanh()`

, supporting`RoundingMode.FULL`

and`RoundingMode.APPROX`

.Compiling FP8 operations for sm80 family GPUs will raise

`TileUnsupportedFeatureError`

.Setting

`opt_level=0`

on`ct.kernel`

is no longer required for`ct.printf()`

and`ct.print()`

.

### Features[#](https://docs.nvidia.com#id12)

Add

`ct.static_iter`

keyword that enables compile-time`for`

loops.Add

`ct.static_assert`

keyword that can be used to assert that a condition is true at compile time.Add

`ct.static_eval`

keyword that enables compile-time evaluation using the host Python interpreter.Add

`ct.scan()`

for custom scan.Add

`ct.isnan()`

.Add

`print()`

and`ct.print()`

that supports python-style print and f-strings.Add optional

`mask`

parameter to`ct.gather()`

and`ct.scatter()`

for custom boolean masking.Operator

`+`

can now be used to concatenate tuples.Support unpacking nested tuples (e.g.,

`a, (b, c) = t`

) and using square brackets for unpacking (e.g.,`[a, b] = 1, 2`

).Add bytecode-to-cubin disk cache to avoid recompilation of unchanged kernels. Controlled by

`CUDA_TILE_CACHE_DIR`

and`CUDA_TILE_CACHE_SIZE`

.

### Bug Fixes[#](https://docs.nvidia.com#id13)

Fix a bug where

`nan != nan`

returns False.Fix “potentially undefined variable

`$retval`

” error when a helper function returns after a`while`

loop that contains no early return.Fix the missing column indicator in error messages when the underlined text is only one character wide.

Add a missing check for unpacking a tuple with too many values. For example,

`a, b = 1, 2, 3`

now raises an error instead of silently discarding the extra value.Fix a bug where the promoted dtype of uint16 and uint64 was incorrectly set to uint32.


### Enhancements[#](https://docs.nvidia.com#id14)

Erase the distinction between scalars and zero-dimensional tiles. They are now completely interchangeable.

`~x`

for const boolean`x`

will raise a TypeError to prevent inconsistent results compared to`~x`

on a boolean Tile.Add

`TileUnsupportedFeatureError`

to the public API.

## 1.1.0 (2026-01-30)[#](https://docs.nvidia.com#release-1-1-0)

### Features[#](https://docs.nvidia.com#id15)

Add support for nested functions and lambdas.

Add support for custom reduction via

`ct.reduce()`

.Add

`Array.slice(axis, start, stop)`

to create a view of an array sliced along a single axis. The result shares memory with the original array (no data copy).

### Bug Fixes[#](https://docs.nvidia.com#id16)

Fix reductions with multiple axes specified in non-increasing order.

Fix a bug when pattern matching (FusedMultiplyAdd) attempts to remove a value that is used by the new operation.


### Enhancements[#](https://docs.nvidia.com#id17)

Allow assignments with type annotations. Type annotations are ignored.

Support constructors of built-in numeric types (bool, int, float), e.g.,

`float('inf')`

.Lift the ban on recursive helper function calls. Instead, add a limit on recursion depth. Add a new exception class

`TileRecursionError`

, thrown at compile time when the recursion limit is reached during function call inlining.Improve error messages for type mismatches in control flow statements.

Relax type checking rules for variables that are assigned a different type depending on the branch taken: it is now only an error if the variable is used afterwards.

Stricter rules for potentially-undefined variable detection: if a variable is first assigned inside a

`for`

loop, and then used after the loop, it is now an error because the loop may take zero iterations, resulting in a use of an undefined variable.Include a full cuTile traceback in error messages. Improve formatting of code locations; include function names, remove unnecessary characters to reduce line lengths.

Delay the loading of CUDA driver until kernel launch.

Expose the

`TileError`

base class in the public API.Add

`ct.abs()`

for completeness.

## 1.0.1 (2025-12-18)[#](https://docs.nvidia.com#release-1-0-1)

### Bug Fixes[#](https://docs.nvidia.com#id18)

Fix a bug in hash function that resulted in potential performance regression for kernels with many specializations.

Fix a bug where an if statement within a loop can trigger an internal compiler error.

Fix SliceType

`__eq__`

comparison logic.

### Enhancements[#](https://docs.nvidia.com#id19)

Improve error message for

`ct.cat()`

.Support

`is not None`

comparison.

## 1.0.0 (2025-12-02)[#](https://docs.nvidia.com#release-1-0-0)

Initial release.