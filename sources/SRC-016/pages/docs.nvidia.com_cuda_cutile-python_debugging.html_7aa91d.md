source: https://docs.nvidia.com/cuda/cutile-python/debugging.html

# Debugging[#](https://docs.nvidia.com#debugging)

## Exception Types[#](https://docs.nvidia.com#exception-types)

-
cuda.tile.TileSyntaxError
[#](https://docs.nvidia.com#cuda.tile.TileSyntaxError) alias of

`UnsupportedSyntaxError`


-
cuda.tile.TileTypeError
[#](https://docs.nvidia.com#cuda.tile.TileTypeError) alias of

`TypeCheckingError`


-
cuda.tile.TileValueError
[#](https://docs.nvidia.com#cuda.tile.TileValueError) alias of

`InvalidValueError`


-
cuda.tile.TileUnsupportedFeatureError
[#](https://docs.nvidia.com#cuda.tile.TileUnsupportedFeatureError) alias of

`UnsupportedFeatureError`


-
cuda.tile.TileCompilerExecutionError
[#](https://docs.nvidia.com#cuda.tile.TileCompilerExecutionError) alias of

`CompilerExecutionError`


-
cuda.tile.TileCompilerTimeoutError
[#](https://docs.nvidia.com#cuda.tile.TileCompilerTimeoutError) alias of

`CompilerTimeoutError`


## Compiler Timeout[#](https://docs.nvidia.com#compiler-timeout)

-
cuda.tile.compiler_timeout(
*timeout_sec*)[#](https://docs.nvidia.com#cuda.tile.compiler_timeout) Context manager that temporarily sets the compiler timeout.

Note

This function is not thread-safe. It modifies global state shared by all threads.

Example:

with ct.compiler_timeout(10): ct.launch(stream, grid, kernel, args)


## Environment Variables[#](https://docs.nvidia.com#environment-variables)

The following environment variables are useful when the above exceptions are encountered during kernel development.

Set `CUDA_TILE_ENABLE_CRASH_DUMP=1`

to enable dumping
an archive including the TileIR bytecode
for submitting a bug report on [ TileCompilerExecutionError](https://docs.nvidia.com#cuda.tile.TileCompilerExecutionError)
or

[.](https://docs.nvidia.com#cuda.tile.TileCompilerTimeoutError)

`TileCompilerTimeoutError`

Set `CUDA_TILE_COMPILER_TIMEOUT_SEC`

to limit the
time the TileIR compiler tileiras can take.

Set `CUDA_TILE_LOGS=CUTILEIR`

to print cuTile Python
IR during compilation to stderr. This is useful when
debugging [ TileTypeError](https://docs.nvidia.com#cuda.tile.TileTypeError).

Set `CUDA_TILE_TEMP_DIR`

to configure the directory
for storing temporary files.

Set `CUDA_TILE_CACHE_DIR`

to configure the directory
for the bytecode-to-cubin disk cache. Compiled cubins
are cached here to avoid recompilation of unchanged
kernels. Set to `0`

, `off`

, `none`

, or an empty
string to disable caching. Defaults to
`~/.cache/cutile-python`

.

Set `CUDA_TILE_CACHE_SIZE`

to configure the maximum
disk cache size in bytes. Oldest entries are evicted
when the cache exceeds this limit. Defaults to
2 GB (2147483648).

## Inspecting the Compilation Cache[#](https://docs.nvidia.com#inspecting-the-compilation-cache)

Use the `cutile-cache log`

command to page through cached compilations in
most-recently-accessed order. Each entry shows the kernel’s mangled name,
compiler version, compilation date and duration, CUBIN size, and optimization
remarks:

```
cutile-cache log
```

Compilation remarks are captured in YAML format when using `tileiras`

13.4
or newer. Entries produced by earlier cuTile Python or compiler versions remain
readable but may show metadata as unavailable.