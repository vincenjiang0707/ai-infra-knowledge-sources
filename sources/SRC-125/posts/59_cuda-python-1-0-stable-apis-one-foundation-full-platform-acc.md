# cuda-python-1-0-stable-apis-one-foundation-full-platform-access

source: https://developer.nvidia.com/blog/cuda-python-1-0-stable-apis-one-foundation-full-platform-access/

For years, a Python developer who needed a GPU had two realistic choices: Learn NVIDIA CUDA C++ well enough to write an extension, set up a build toolchain, and maintain bindings back to Python, which most people never did; or move up the stack and let someone else’s library do it, namely PyTorch, CuPy, or RAPIDS.

The second option is why the Python GPU ecosystem thrives. But it has limits. The moment you need something the library above you doesn’t expose, you’re back to the first choice.

Because each library reached CUDA in its own way, getting two of them to cooperate on the same data took care. If CuPy allocated a block of GPU memory, what did it take for cuDF to work on that block, on the same stream, without copying it? The answer ran through interchange protocols and close attention to who owned what.

With CUDA 13.3, we released CUDA Python 1.0, the libraries and tools that give you the full CUDA platform from Python. Python is now a supported way to use the CUDA platform.

Here is what lands together:

`cuda.core`

1.0.0, Pythonic access to the CUDA runtime`cuda.compute`

1.0.0, CCCL’s parallel algorithms, callable from Python`cuda.bindings`

13.3.0, low-level 1:1 bindings to the CUDA C APIs, versioned to the CUDA Toolkit`cuda-pathfinder`

, which locates the CUDA components installed in your environment`nvmath-python`

1.0, NVIDIA’s math libraries in Python, under the same kind of stability commitment on its own release track

CUDA Python 1.0 names a milestone, not a version number you will type into `pip`

; the components are versioned independently, so the mismatched numbers above are deliberate.

The most consequential entry is `cuda.core`

. It is where CUDA’s basic vocabulary (devices, streams, buffers) becomes a set of ordinary Python objects, and that matters well beyond convenience: it gives every GPU library in Python a common foundation to build on, collaborate through, and share resources across. That idea is the thread running through the rest of this post.

## CUDA 1.0: Semantic versioning

CUDA Python 1.0 is not a rewrite and not a new product. Most of these libraries have been available and improving for a while. What changes with 1.0 is a commitment: *semantic versioning*.

In practice, that means:

- Breaking API changes happen only in major releases
- Minor releases add features
- Patch releases fix bugs
- Any public API scheduled for removal is deprecated first, in a minor release, with a clear replacement path

If you’ve hesitated to build on a library because you weren’t sure the API would survive the next upgrade, that guarantee is the headline. CUDA Python will keep tracking new CUDA capabilities as they ship, now under predictable versioning and deprecation rules.

## One foundation instead of many

To see what 1.0 changes, it helps to remember what came before it.

Reaching CUDA from Python used to mean choosing a binding layer, and there were several. Each was maintained by a different project, each covered a different slice of the API, and each had its own idea of what a stream or a device or an allocation was. If you wrote applications, you inherited whichever layer your dependencies happened to use. If you wrote libraries, you either adopted someone else’s or built your own, and the ecosystem accumulated one more. That is the thing that changed.

There is now one official, NVIDIA-maintained way to reach CUDA from Python. As of CUDA 13.3, CUDA Python and C++ stand as equal first-class citizens, with NVIDIA committing to maintain feature-complete parity going forward. Python is a supported way to use the CUDA platform.

The practical payoff is that libraries now compose rather than merely coexist. A Numba kernel and a `cuda.compute`

call can operate on the same GPU buffer in the same stream, because neither one brought a private CUDA layer along. Objects cross library boundaries because, underneath, they are the same objects. That is a shorter answer to the sharing question than any interchange protocol.

It also changes who gets to use advanced platform capabilities. A feature like green contexts, which partitions a GPU’s streaming multiprocessors so latency-sensitive kernels are shielded from throughput kernels, would previously have needed every interested library to bind and expose it independently. Now it lands in `cuda.core`

once, and everything built on `cuda.core`

can reach it.

If you build libraries that target CUDA, this is what changes your day-to-day: your effort goes into what makes your library distinctive rather than into a low-level layer someone else has already written. If you write applications, the benefit reaches you one level removed, as your dependencies converge on the same plumbing.

## The mental model: Three tiers on one foundation

CUDA Python is a collection of libraries that together cover the CUDA ecosystem from Python: low-level driver and runtime bindings, parallel algorithms, math libraries, communication libraries, and kernel-authoring tools. Figure 1, below, shows how they stack up. The clearest way to read the image is from the bottom up.

The runtime system is the foundation every other box rests on: device management, memory allocation, streams and synchronization, CUDA graphs, and JIT compilation.

`cuda-pathfinder`

sounds mundane until you remember how much time the Python GPU community has spent debugging which CUDA runtime a process really loaded.

Above that sit the CUDA libraries: Pythonic interfaces to the NVIDIA tuned host and device libraries. `cuda.compute`

brings CCCL’s host-callable parallel algorithms; `nvmath-python`

, also now at 1.0, brings the math libraries, with host APIs, device APIs, and low-level bindings; and NCCL4Py and NVSHMEM4P bring the communication libraries, NCCL and NVSHMEM.

None of them reimplements the CUDA layer underneath. They work in the same `cuda.core`

buffers, devices, and streams you would use directly, so NVSHMEM’s symmetric memory, for instance, comes back to you as a `cuda.core`

buffer. The shared foundation is not just guidance for the ecosystem; NVIDIA’s own libraries are built on it.

At the top is kernel authoring, for when you want to write the GPU code yourself. `numba-cuda`

is the SIMT language for Python kernels, and alongside it sit two newer domain-specific languages: `cutile-python`

, a CUDA tile language for the block model, and `cuteDSL`

, a CUTLASS language for Tensor Cores.

Two things worth clarifying:

First, you enter at the tier your problem requires, and you never have to learn the whole thing. Plenty of productive users never leave the library tier. Nothing about the diagram is a curriculum.

Second, the tiers are not a single versioned product. Each component moves on its own track, and a few pieces, including some of the newer kernel-authoring languages, are still experimental and not yet covered by the 1.0 semantic-versioning guarantees, though the intent is for them to come under the same commitments as they stabilize. That is worth knowing before you pin a production dependency on one.

## Three ways in

Almost everyone arrives at CUDA Python with one of three questions, and each one points at a different tier of the diagram. Here they are, ordered by how much you take on rather than by where they sit in the diagram.

### I just want optimized algorithms: `cuda.compute`


The fastest win is usually not writing a kernel at all. It is calling one that already exists and has been tuned by people who do that full time.

`cuda.compute`

brings the CUDA Core Compute Libraries (CCCL) parallel algorithms to Python as host-callable building blocks: sort, scan, reduce, transform, unique, histogram, top-k, and more. These are the same algorithms that back high-performance C++ CUDA code, and from Python they are ordinary function calls on GPU arrays you already have. A large share of numerical work turns out to be a composition of these patterns. Because `cuda.compute`

compiles them for the GPU you are actually running on, the same call works unchanged on the next generation of hardware.

Version 1.0 also makes them more expressive: you can now customize what an algorithm does with ordinary Python functions, including lambdas.

**Reach for this when**: your problem decomposes into well-known parallel patterns and you want results with the least new code.

### I want to write my own kernel in Python: Numba

Sometimes your logic does not match a prepackaged algorithm. In that case, you write the kernel yourself, and you can still do it in Python.

Numba compiles a subset of Python into GPU kernels: you mark a function with a decorator, and Numba generates GPU code from it. What you are writing is a kernel in the CUDA SIMT model, expressing the work of a single thread that the GPU then runs across many thousands at once. Making that mental shift is the main thing to learn, and it is a far smaller step than picking up C++ and a build system.

Numba CUDA MLIR is a new Numba-compatible kernel generator built on MLIR and the modern NVVM toolchain. It keeps the programming model you already know and replaces the compiler underneath, delivering faster warm JIT compiles and lower kernel-launch latency; for most code, moving to it is a one-line import change. It is newer than the 1.0 components, and not yet covered by the same semantic-versioning commitment.

**Reach for this when**: your computation does not fit a prepackaged algorithm and you want direct control over what each thread does.

### I need the driver and runtime APIs: `cuda.core`

, `cuda.bindings`


At the foundation sit two packages that hand you CUDA itself, and `cuda.core`

reaching 1.0 is the centerpiece of this release.

`cuda.core`

is a Pythonic interface to the CUDA runtime, covering devices, streams, programs, linkers, memory resources, and graphs, along with runtime compilation of CUDA C++ so a kernel can go from source to running without a separate build step. The emphasis belongs on *Pythonic*: resources are real Python objects and failures raise exceptions rather than returning error codes. Because it uses a standard CUDA context, it shares devices, streams, and memory with the rest of the Python GPU ecosystem, so your own kernels can run against CuPy arrays or PyTorch tensors without copying data.

Version 1.0 consolidates APIs that had been stabilizing over previous release cycles into a single supported surface, and adds three capabilities worth calling out:

**Green contexts**: Partition a GPU’s SMs into disjoint groups, as described earlier, so latency-sensitive kernels stay shielded from long-running throughput kernels in the same process.**Process checkpointing**: Snapshot the full CUDA state of a running process and restore it later.**Inter-process sharing (IPC)**: Share GPU memory between processes without copying through the host.

Beneath it, `cuda.bindings`

provides low-level bindings with full, 1:1 coverage of the CUDA host APIs, from the Driver and Runtime through the compiler, linker, and system libraries around them. It is versioned to the CUDA Toolkit. Where `cuda.core`

optimizes for Python ergonomics, `cuda.bindings`

optimizes for completeness: if it exists in the C API, you can reach it from Python.

**Reach for this when**: you are building a GPU library or integrating CUDA into an existing toolkit. Use`cuda.core`

for Pythonic productivity and`cuda.bindings`

when you need exhaustive access to the C APIs.

## The ecosystem is already converging

The best evidence that a shared foundation works is who’s already building on it. The NVIDIA communications and math libraries already all speak in `cuda.core`

objects, as described earlier. The wider ecosystem is converging too. CuPy gets a simpler build and a faster, smaller footprint when importing the module. PyTorch now depends on `cuda.bindings`

in its CUDA wheels.

Each library that moves onto the shared layer takes one more private binding layer out of your dependency graph. That is fewer version conflicts, fewer mysterious interop bugs, and fewer places for two libraries to disagree about which CUDA context they are in.

And because each component follows semantic versioning on its own track, taking a dependency on one of them doesn’t mean inheriting churn from the rest.

## Getting started

One command gets you the CUDA Python stack:

`pip install cuda-python cuda-cccl numba-cuda-mlir[cu13]`


That covers the CUDA Python components above, plus the MLIR-based Numba backend. Install `nvmath-python`

separately with `pip install nvmath-python[cu13]`

. The only system requirement is an up-to-date NVIDIA driver; a separate CUDA Toolkit installation is generally not required.

If you are deciding where to begin:

- If your work is data science, you may not need to reach this low at all. The RAPIDS libraries already cover that ground: cuDF accelerates pandas, Polars, and Apache Spark, and nx-cugraph backs NetworkX
- For optimized algorithms, start with
`cuda.compute`

- To write your own kernels in Python, start with Numba or Numba CUDA MLIR
- To reach the low-level driver and runtime APIs, start with
`cuda.core`

and`cuda.bindings`


From there, the [CUDA Python documentation](https://nvidia.github.io/cuda-python/latest/) and the [NVIDIA/cuda-python repository](https://github.com/NVIDIA/cuda-python) have installation guides, API references, and examples, and the [NVIDIA Accelerated Computing Hub](https://github.com/NVIDIA/accelerated-computing-hub) collects broader GPU-computing learning material.

The best part of the 1.0 milestone is that this decision is no longer high-stakes. Pick the tier that matches the problem in front of you, and know that the ground under it is stable.

*Acknowledgments*

*CUDA Python 1.0 reflects years of work by the CUDA Python product and engineering teams, who designed and built the libraries described here. Thanks as well to the reviewers across NVIDIA whose feedback sharpened both the release and this post, and to the open source contributors who filed issues, tested prereleases, and helped shape the APIs we are now committing to support.*

## Start the discussion at forums.developer.nvidia.com
