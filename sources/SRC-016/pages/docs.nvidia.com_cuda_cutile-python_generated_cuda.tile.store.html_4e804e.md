source: https://docs.nvidia.com/cuda/cutile-python/generated/cuda.tile.store.html

# cuda.tile.store[#](https://docs.nvidia.com#cuda-tile-store)

- cuda.tile.store(
*array*,*/*,*index*,*tile*,***,*order='C'*,*check_bounds=True*,*latency=None*,*allow_tma=None*,*memory_order=MemoryOrder.WEAK*,*memory_scope=MemoryScope.NONE*,Stores a tile value into the array at the index of its

[tile space](https://docs.nvidia.com/data.html#data-element-tile-space).The

[tile space](https://docs.nvidia.com/data.html#data-element-tile-space)is the result of partitioning the array into a grid of tiles with equal size defined by the shape of the tile.For example, given a tile t of shape

`(tm, tn)`

and array of shape`(M, N)`

:# tile `t` has shape (tm, tn) ct.store(array, (i, j), t)

The above call to store will store elements according to:

array[i * tm + x, i * tn + y] = t[x, y] (for 0<=x<tm, 0<=y<tn)

For a tile that partially extends beyond the array boundaries, out-of-bound elements are ignored. If the tile lies entirely outside the array, the behavior is undefined.

- Parameters:
**index**(*tuple**[**int**,**...**]*) – An index in the[tile space](https://docs.nvidia.com/data.html#data-element-tile-space)of`array`

.`shape`

is inferred from the`tile`

argument.**tile**() – The*Tile*[tile](https://docs.nvidia.com/data.html#data-tiles-and-scalars)to store. The rank of the tile must match rank of the array, unless it is a scalar or 0d tile.**order**(*"C"**or**"F"**, or**tuple**[**const int**,**...**]*) – Order of axis mapping. See.`load()`

**check_bounds**(*const bool*) – Whether to bounds-check the tile against the array boundaries. When`False`

, the tile is assumed to stay fully within bounds and the out-of-bounds check is skipped, producing a faster store; violating this assumption is undefined behavior. Defaults to`True`

. Setting it to`False`

requires tileiras 13.4+.**latency**(*int**,**optional*) – A hint indicating how heavy DRAM traffic will be. It shall be an integer between 1 (low) and 10 (high). By default, the compiler will infer the latency.**allow_tma**(*bool**,**optional*) – If False, the store will not use TMA. By default, TMA is allowed.**memory_order**() – Memory ordering semantics for the store. Defaults to*MemoryOrder*`MemoryOrder.WEAK`

. Valid values:`WEAK`

,`RELAXED`

,`RELEASE`

.**memory_scope**() – The scope of threads that participate in memory ordering. Only meaningful when*MemoryScope*`memory_order`

is not`WEAK`

.


Examples

Store into 1D array, partial out of bound store is ignored.

@ct.kernel def kernel(x): tile = ct.ones((4,), dtype=x.dtype) ct.store(x, (0,), tile) ct.store(x, (1,), tile * 2) x = torch.zeros(6, dtype=torch.int32, device='cuda:0') ct.launch(stream, (1,), kernel, (x,)) print(x.tolist())

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel def kernel(x): tile = ct.ones((4,), dtype=x.dtype) ct.store(x, (0,), tile) ct.store(x, (1,), tile * 2) x = torch.zeros(6, dtype=torch.int32, device='cuda:0') ct.launch(stream, (1,), kernel, (x,)) print(x.tolist()) torch.cuda.synchronize()

Output

[1, 1, 1, 1, 2, 2]

When storing with a scalar (0d tile), it is broadcasted to the rank of the array.

@ct.kernel def kernel(x): ct.store(x, (0, 0), tile=0) ct.store(x, (0, 1), tile=1) ct.store(x, (1, 0), tile=2) ct.store(x, (1, 1), tile=3) x = torch.zeros(4, dtype=torch.int32, device='cuda:0').reshape(2, 2) ct.launch(stream, (1,), kernel, (x,)) print(x.tolist())

import cuda.tile as ct import torch torch.cuda.init() stream = torch.cuda.current_stream() @ct.kernel def kernel(x): ct.store(x, (0, 0), tile=0) ct.store(x, (0, 1), tile=1) ct.store(x, (1, 0), tile=2) ct.store(x, (1, 1), tile=3) x = torch.zeros(4, dtype=torch.int32, device='cuda:0').reshape(2, 2) ct.launch(stream, (1,), kernel, (x,)) print(x.tolist()) torch.cuda.synchronize()

Output

[[0, 1], [2, 3]]

See also


[#](https://docs.nvidia.com#cuda.tile.store)