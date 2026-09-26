source: https://docs.nvidia.com/cuda/cutile-python/generated/cuda.tile.load.html

# cuda.tile.load[#](https://docs.nvidia.com#cuda-tile-load)

- cuda.tile.load(
*array*,*/*,*index*,*shape*,***,*order='C'*,*padding_mode=PaddingMode.UNDETERMINED*,*check_bounds=True*,*latency=None*,*allow_tma=None*,*memory_order=MemoryOrder.WEAK*,*memory_scope=MemoryScope.NONE*,Loads a tile from the array which is partitioned into a

[tile space](https://docs.nvidia.com/data.html#data-element-tile-space).The

[tile space](https://docs.nvidia.com/data.html#data-element-tile-space)is the result of partitioning the array into a grid of equally sized tiles specified by shape.For example, partitoning a 2D array of shape

`(M, N)`

using tile shape`(tm, tn)`

results in a 2D tile space of size`(cdiv(M, tm), cdiv(N, tn))`

. An index into this tile space using index`(i, j)`

produces a tile of size`(tm, tn)`

:t = ct.load(array, (i, j), (tm, tn)) # `t` has shape (tm, tn)

The result tile t will be computed according to

t[x, y] = array[i * tm + x, j * tn + y] (for all 0<=x<tm, 0<=y<tn)

For a tile that partially extends beyond the array boundaries, out-of-bound elements are filled according to padding_mode. If the tile lies entirely outside the array, the behavior is undefined.

order is used to map the tile axis to the array axis. The transposed example of the above call to load would be:

ct.load(array, (j, i), shape=(tn, tm), order=(1, 0))

The result tile t will be computed according to

t[y, x] = array[i * tm + x, j * tn + y]

- Parameters:
**index**(*tuple**[**int**,**...**]*) – An index in the[tile space](https://docs.nvidia.com/data.html#data-element-tile-space)of`shape`

from`array`

.**shape**(*tuple**[**const int**,**...**]*) – A tuple of const integers definining the shape of the tile.**order**(*"C"**or**"F"**, or**tuple**[**const int**,**...**]*) –Permutation applied to array axes before the logical

[tile space](https://docs.nvidia.com/data.html#data-element-tile-space)is constructed. Can be specified either as a tuple of constants, or as one of the two special string literal values:”C” is an alias for

`(0, 1, 2, ...)`

, i.e. no permutation applied;”F” is an alias for

`(..., 2, 1, 0)`

, i.e. axis order is reversed.

**padding_mode**() – The value used to pad the tile when it extends beyond the array boundaries. By default, the padding value is undetermined.*PaddingMode***check_bounds**(*const bool*) – Whether to bounds-check the tile against the array boundaries. When`False`

, the tile is assumed to stay fully within bounds and the out-of-bounds check is skipped, producing a faster load; violating this assumption is undefined behavior. Since no out-of-bound elements can occur in this case,`padding_mode`

is ignored. Defaults to`True`

. Setting it to`False`

requires tileiras 13.4+.**latency**(*const int*) – A hint indicating how heavy DRAM traffic will be. It shall be an integer between 1 (low) and 10 (high). By default, the compiler will infer the latency.**allow_tma**(*const bool*) – If False, the load will not use TMA. By default, TMA is allowed.**memory_order**() – Memory ordering semantics for the load. Defaults to*MemoryOrder*`MemoryOrder.WEAK`

. Valid values:`WEAK`

,`RELAXED`

,`ACQUIRE`

.**memory_scope**() – The scope of threads that participate in memory ordering. Only meaningful when*MemoryScope*`memory_order`

is not`WEAK`

.

- Return type:

Examples

Load from an 1D array.

@ct.kernel def kernel(x): zero_pad = ct.PaddingMode.ZERO print(ct.load(x, (0,), shape=4)) print(ct.load(x, (1,), shape=4)) print(ct.load(x, (2,), shape=4, padding_mode=zero_pad)) x = torch.arange(10, device='cuda:0') ct.launch(stream, (1,), kernel, (x,))

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel def kernel(x): zero_pad = ct.PaddingMode.ZERO print(ct.load(x, (0,), shape=4)) print(ct.load(x, (1,), shape=4)) print(ct.load(x, (2,), shape=4, padding_mode=zero_pad)) x = torch.arange(10, device='cuda:0') ct.launch(stream, (1,), kernel, (x,)) torch.cuda.synchronize()

Output

[0, 1, 2, 3] [4, 5, 6, 7] [8, 9, 0, 0]

Load from a 2D array in transposed order.

@ct.kernel def kernel(x): print(ct.load(x, (0, 0), shape=(1, 4), order='F')) print(ct.load(x, (1, 0), shape=(1, 4), order='F')) print(ct.load(x, (2, 0), shape=(1, 4), order='F')) print(ct.load(x, (3, 0), shape=(1, 4), order='F')) x = torch.arange(16, device='cuda:0').reshape(4, 4) ct.launch(stream, (1,), kernel, (x,))

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel def kernel(x): print(ct.load(x, (0, 0), shape=(1, 4), order='F')) print(ct.load(x, (1, 0), shape=(1, 4), order='F')) print(ct.load(x, (2, 0), shape=(1, 4), order='F')) print(ct.load(x, (3, 0), shape=(1, 4), order='F')) x = torch.arange(16, device='cuda:0').reshape(4, 4) ct.launch(stream, (1,), kernel, (x,)) torch.cuda.synchronize()

Output

[[0, 4, 8, 12]] [[1, 5, 9, 13]] [[2, 6, 10, 14]] [[3, 7, 11, 15]]

Load from a 3D array with last 2 axes transposed.

@ct.kernel def kernel(x): print(ct.load(x, (0, 0, 0), shape=(1, 2, 2), order=(0, 2, 1))) print(ct.load(x, (1, 0, 0), shape=(1, 2, 2), order=(0, 2, 1))) x = torch.arange(8, device='cuda:0').reshape(2, 2, 2) ct.launch(stream, (1,), kernel, (x,))

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel def kernel(x): print(ct.load(x, (0, 0, 0), shape=(1, 2, 2), order=(0, 2, 1))) print(ct.load(x, (1, 0, 0), shape=(1, 2, 2), order=(0, 2, 1))) x = torch.arange(8, device='cuda:0').reshape(2, 2, 2) ct.launch(stream, (1,), kernel, (x,)) torch.cuda.synchronize()

Output

[[[0, 2], [1, 3]]] [[[4, 6], [5, 7]]]

Load a single scalar.

@ct.kernel def kernel(x): for i in range(10): tile = ct.load(x, (i,), shape=()) print(tile, end=" ") print() x = torch.arange(10, device='cuda:0') ct.launch(stream, (1,), kernel, (x,))

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel def kernel(x): for i in range(10): tile = ct.load(x, (i,), shape=()) print(tile, end=" ") print() x = torch.arange(10, device='cuda:0') ct.launch(stream, (1,), kernel, (x,)) torch.cuda.synchronize()

Output

0 1 2 3 4 5 6 7 8 9

See also


[#](https://docs.nvidia.com#cuda.tile.load)