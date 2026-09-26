# [Issue #3581] [BUG] 02_dump_reg_shmem faults on sm_120: Fragment is 2-byte aligned but accessed through a 16-byte-aligned pointer

source: https://github.com/NVIDIA/cutlass/issues/3581
state: open | updated: 2026-09-13T07:55:58Z
labels: bug, ? - Needs Triage, CUTLASS C++

## 正文

> **Correction (2026-09-13).** My original report framed this as an `nvcc` codegen bug specific to
> `sm_120`. That framing was wrong, and I have rewritten this issue. Further testing showed the
> codegen is identical on `sm_80`/`sm_90`/`sm_100`/`sm_120`, and that the underlying defect is on the
> CUTLASS side: the iterators access `Fragment` through a type that requires 16-byte alignment, while
> `Fragment` itself is only 2-byte aligned. Details and a verified fix below.

## Summary

`examples/02_dump_reg_shmem` aborts on `sm_120` with `cudaErrorMisalignedAddress` (error 716); the
example prints `Failed` and exits `255`. Reproduced on `main` @ `147295a3` with the stock example.

Root cause: `PredicatedTileIterator` reinterprets its `Fragment` (a plain `cutlass::Array`, 2-byte
aligned for `half_t`) as a 16-byte-aligned `AlignedArray` and accesses it 128 bits at a time. When the
compiler homes that fragment in local memory, it allocates the frame slot using the *declared*
alignment (2 → offset `+0xc`) but emits the stores using the *cast-implied* alignment (16 →
`STL.128`). The slot ends up at `12 (mod 16)`, so the 16-byte store is misaligned and the kernel
faults. Aligning the fragment moves the slot to `+0x10` and the example completes.

## Environment

| | |
|---|---|
| GPU | NVIDIA GeForce RTX 5060, compute capability 12.0 (`sm_120`), driver 591.86 |
| Toolkit | CUDA 13.3 — nvcc V13.3.73 (`cuda_13.3.r13.3/compiler.38244171_0`) |
| OS | Linux (Ubuntu 26.04 LTS under WSL2), x86_64 |
| CUTLASS | `main` @ `147295a3`, unmodified (`git status` clean) |

## Where the alignment requirement comes from

The example itself is not at fault — `examples/02_dump_reg_shmem/dump_reg_shmem.cu:85` only declares

```cpp
typename GmemIterator::Fragment frag;
```

The requirement is imposed by the iterator
(`include/cutlass/transform/threadblock/predicated_tile_iterator.h`):

| Line | Code | Alignment |
|---|---|---|
| [181](https://github.com/NVIDIA/cutlass/blob/main/include/cutlass/transform/threadblock/predicated_tile_iterator.h#L181) | `using AccessType = AlignedArray<Element, AccessSize, (AccessSize * sizeof_bits<Element>::value / 8)>;` | **16 bytes** (for `half_t`, `AccessSize == 8`) |
| [191](https://github.com/NVIDIA/cutlass/blob/main/include/cutlass/transform/threadblock/predicated_tile_iterator.h#L191) | `using Fragment = cutlass::Array<Element, ThreadMap::Iterations::kCount * ThreadMap::kElementsPerAccess>;` | **2 bytes** — `cutlass::Array` has no `alignas` (`include/cutlass/array.h:101`; only `AlignedArray` at `array.h:2867` declares one) |
| [327](https://github.com/NVIDIA/cutlass/blob/main/include/cutlass/transform/threadblock/predicated_tile_iterator.h#L327) | `AccessType *frag_ptr = reinterpret_cast<AccessType *>(&frag);` | casts the 2-byte-aligned object to the 16-byte-aligned type |

So the library relies on an alignment its own `Fragment` type does not declare. That dependency is
invisible to a caller who simply declares `typename GmemIterator::Fragment frag;`, which is the
documented idiom — and it is the reason the example breaks without any misuse on the caller's side.

## Evidence

**SASS of `kernel_dump` (`cuobjdump -sass`), stock example — the local slot is at `+0xc`:**

```sass
STL.128 [R1+0xc], R52 ;
STL.128 [R1+0x1c], R48 ;
STL.128 [R1+0x2c], R44 ;
STL.128 [R1+0x3c], R40 ;
STL.128 [R1+0x4c], R36 ;
STL.128 [R1+0x5c], R32 ;
STL.128 [R1+0x6c], R28 ;
STL.128 [R1+0x7c], R24 ;
```

Every offset is `≡ 12 (mod 16)`; `STL.128` requires a 16-byte-aligned address, and the kernel faults
at the first one.

**With the fragment aligned, the slot moves and the fault disappears:**

| | fragment slot | `STL.128` offsets | result |
|---|---|---|---|
| stock | `+0xc` | `0xc, 0x1c, … 0x7c` (all `≡12 mod 16`) | fault, exit 255 |
| `alignas(16)` | `+0x10` | `0x10, 0x20, … 0x80` (all 16-byte aligned) | **completes, exit 0** |

**Not architecture-specific.** Compiling the reproducer below for `sm_80`, `sm_90`, `sm_100` and
`sm_120` produces the identical 8 × `STL.128` at `[R1+0xc … R1+0x7c]`. The codegen is
architecture-independent; whether it faults depends on the runtime frame base, and on `sm_120` it
does. (I could only *execute* on `sm_120` — other architectures were compile-only.)

## Proposed fix

Minimal, verified on `sm_120`:

```cpp
// examples/02_dump_reg_shmem/dump_reg_shmem.cu:85
alignas(16) typename GmemIterator::Fragment frag;
```

However this only protects the example. Since `AccessType` is 16-byte aligned for every user of
`PredicatedTileIterator` (and the other iterators with the same pattern), the more principled fix
would be to declare the alignment on the `Fragment` typedef itself — e.g. make it an `AlignedArray`,
or add `alignas` — so that any caller declaring `Fragment frag;` is safe. That is a wider change, so
I'd rather leave the choice to the maintainers.

## Exposure (why this is not caught elsewhere)

A fragment that never has its address taken stays in registers and never touches local memory. Real
GEMM kernels therefore don't hit this. The fault needs the fragment's address to escape to a
non-inlined function — which is exactly what the dump/debug path does (`cutlass::debug::dump_fragment`,
`printf`). That is consistent with it showing up in this example and seemingly nowhere else.

## Note on the compiler side

I filed this with NVIDIA's compiler team as well. Their assessment was that the
`reinterpret_cast` to a 16-byte-aligned type is a source-level alignment promise that the object does
not satisfy, and therefore source-level UB rather than a codegen defect. I accept that reading — it
is why I have rewritten this issue rather than insisting on a compiler bug. The remaining point for
CUTLASS is narrower: the library should not depend on an alignment guarantee its own type does not
make.

<details>
<summary>Minimal reproducer (no CUTLASS)</summary>

The program below reproduces the same codegen and fault on `sm_120`. Note that the `Frame` layout is
deliberately constructed to place the fragment at `+0xc` **in order to demonstrate the misaligned
store** — it is not a claim that CUTLASS declares any such layout. In the real kernel the `+0xc`
offset is chosen by the compiler's frame allocator, not by the source.

```cpp
// repro_stl128.cu — nvcc sm_120: 16-byte local stores (STL.128) to
//                   frame offsets 12 (mod 16)  =>  misaligned address.
// Build & run (CUDA 13.3, sm_120):
//   nvcc repro_stl128.cu -arch=sm_120 -std=c++17 -O2 -o repro_stl128 && ./repro_stl128
// =>  sm_120 result: misaligned address     (exit 255)

#include <cstdint>
#include <cstdio>

struct Frag {
  unsigned short f[64];   // 128 bytes, 2-byte alignment (mimics cutlass::half_t[64])
};

// The 8-byte and 4-byte slots in front force the fragment to offset +0xc,
// legal for a 2-byte-aligned object, illegal for a 16-byte store.
struct Frame {
  unsigned long long a;   // +0x0
  unsigned b;             // +0x8
  Frag f;                 // +0xc
};

__device__ __noinline__ void take8(unsigned long long* p) { *p ^= 1ull; }
__device__ __noinline__ void take4(unsigned* p)           { *p ^= 1u; }

__device__ __forceinline__ void load(Frag& frag, uint4 const* src, int tid) {
  uint4* p = reinterpret_cast<uint4*>(frag.f);  // 128-bit view of the fragment
#pragma unroll
  for (int i = 0; i < 8; ++i) p[i] = src[tid * 8 + i];
}

__device__ __noinline__ void dump(Frag const& f, unsigned* sink) {
  unsigned s = 0;
  if (threadIdx.x == 0 && blockIdx.x == 0) printf("dump");  // printf frame is part of the trigger
#pragma unroll
  for (int i = 0; i < 64; ++i) s ^= f.f[i];
  *sink = s;
}

__global__ void kernel(uint4 const* src, unsigned* sink) {
  Frame fr;
  take8(&fr.a);                 // addresses escape to __noinline__ callees,
  take4(&fr.b);                 // so Frame is homed in addressable local memory
  load(fr.f, src, threadIdx.x); // 128-bit reg groups stored home via STL.128
  dump(fr.f, sink + threadIdx.x);
}

int main() {
  uint4* src; unsigned* sink;
  cudaMalloc(&src, sizeof(uint4) * 8 * 32);
  cudaMalloc(&sink, sizeof(unsigned) * 32);
  cudaMemset(src, 1, sizeof(uint4) * 8 * 32);
  kernel<<<1, 32>>>(src, sink);
  cudaError_t err = cudaDeviceSynchronize();
  printf("sm_120 result: %s\n", cudaGetErrorString(err));
  return err == cudaSuccess ? 0 : -1;
}
```

</details>

Happy to open a PR for the example-level fix, or to test a `Fragment`-level change if you'd prefer
that route.


## 评论 (4)

### roma5087 · 2026-09-04

Can this be assigned to me?

### random25160765-collab · 2026-09-04

but it is a compiler problem

### random25160765-collab · 2026-09-13

After communicating with the people at NVIDIA, I believe this is not a compiler issue, but rather a bug caused by the source code hitting C++ UB. The previous issue has already been modified. (filed with NVIDIA's compiler team; they assessed it as source-level UB)

### random25160765-collab · 2026-09-13

One clarification on my correction above, and a status update.

Clarification: the source that hits UB here is CUTLASS's own iterator, not the example's user code.

The example instantiates PredicatedTileIterator with layout::ColumnMajor (dump_reg_shmem.cu:156). That
specialization (predicated_tile_iterator.h:415) declares its Fragment at :453 and delegates to the
underlying PitchLinear implementation, which is where the mismatch lives:

  :181  using AccessType = AlignedArray<Element, AccessSize,
                                        (AccessSize * sizeof_bits<Element>::value / 8)>;  // 16 bytes for half_t
  :191  using Fragment = cutlass::Array<Element, ...>;                                   // no alignas -> 2 bytes
  :327  AccessType *frag_ptr = reinterpret_cast<AccessType *>(&frag);

So the library accesses a 2-byte-aligned object through a 16-byte-aligned type. The example only
declares `typename GmemIterator::Fragment frag;` — the documented idiom — and fails with stock
upstream code on sm_120.

@roma5087 thanks for offering — I've opened a PR with the verified fix so it isn't duplicated:
https://github.com/NVIDIA/cutlass/pull/3633

The PR is the minimal example-level fix (alignas(16) at dump_reg_shmem.cu:85). Whether the Fragment
typedef itself should declare the alignment its accessors require affects every caller and is left to
the maintainers.
