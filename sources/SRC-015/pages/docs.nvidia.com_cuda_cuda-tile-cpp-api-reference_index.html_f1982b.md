source: https://docs.nvidia.com/cuda/cuda-tile-cpp-api-reference/index.html

# CUDA Tile C++ API Reference[](https://docs.nvidia.com#cuda-tile-c-api-reference)

CUDA Tile C++ is a tile programming extension to the CUDA C++ language. In Tile C++, intra-block
parallelism is expressed through elementwise operations on **tiles**. The compiler automatically
parallelizes tile code across multiple threads while utilizing advanced hardware capabilities such
as Tensor Memory Accelerators (TMA) and Tensor Cores. By leveraging the high level abstractions
provided by Tile C++, a tile kernel can remain performance portable across NVIDIA GPU architectures
without modification.

```
#include "cuda_tile.h"
__tile_global__ void vectorAdd(float* __restrict__ a, float* __restrict__ b, float* __restrict__ out, std::size_t n) {
namespace ct = cuda::tiles;
using namespace ct::literals;
a = assume_aligned(a, 16_ic);
b = assume_aligned(b, 16_ic);
out = assume_aligned(out, 16_ic);
auto idx = ct::bid().x;
auto view_a = ct::partition_view{ct::tensor_span{a, ct::extents{n}}, ct::shape{1024_ic}};
auto view_b = ct::partition_view{ct::tensor_span{b, ct::extents{n}}, ct::shape{1024_ic}};
auto view_out = ct::partition_view{ct::tensor_span{out, ct::extents{n}}, ct::shape{1024_ic}};
auto tile_a = view_a.load_masked(idx);
auto tile_b = view_b.load_masked(idx);
auto tile_out = tile_a + tile_b;
view_out.store_masked(tile_out, idx);
}
```

This reference manual describes the foundational APIs for working with CUDA Tile C++. For a tutorial on the tile language extensions and tile programming paradigm, see the CUDA Programming Guide.