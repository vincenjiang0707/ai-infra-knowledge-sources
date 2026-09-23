# helion-x-%f0%9f%a4%97-hf-kernels-building-and-shipping-out-of-the-box-performant-kernels

source: https://pytorch.org/blog/helion-x-%f0%9f%a4%97-hf-kernels-building-and-shipping-out-of-the-box-performant-kernels/

### Featured projects

### TL;DR

The HuggingFace Kernels project now has Helion support. This blog walks through how to build, autotune, and ship performant and portable Helion kernels via the Hugging Face Kernels project, allowing users to consume these kernels seamlessly.

## Introduction

[Helion](https://github.com/pytorch/helion) is a high-level DSL for writing high-performance, portable kernels for machine learning. The [🤗 Kernels](https://huggingface.co/docs/kernels/en/index) project lets kernel developers package and distribute their kernels on the Hugging Face Hub platform in a consistent and reproducible manner. It also lets kernel users consume these kernels seamlessly without managing dependency hell.

In this post, we will discuss how Helion is supported within the Kernels project, how users can benefit from first-class autotuning support in Helion, and how to ship pre-tuned kernel configs to reduce cold-start times. We will also show examples of Helion kernels and how tuning them for specific problem sizes can yield performance benefits.

P.S.: Throughout the rest of the post, we will refer to the **Kernels** project with “k” in capital letters to distinguish it from actual “kernels”.

## Intro: Helion

Helion is a tiled DSL for writing performant ML kernels. The programming model is often described as “PyTorch with tiles” – the kernel operates on PyTorch tensors, and tile-level operations are specified via ordinary PyTorch tensor operators. As a quick example, the following function shows a tiled matmul implemented in Helion:

What makes Helion desirable is not just its concise syntax but what it leaves deliberately unspecified. When you write `hl.tile`

, you say only that the iteration space should be tiled – not how large the tiles are, or how their data is fetched from memory. Helion turns these decisions into a search space to be autotuned over. Crucially, the autotuner does not merely sweep numerical parameters like tile sizes, it also searches over lowering strategies – the actual implementation of the kernel: which memory-access pattern to use (pointer arithmetic, block pointers, TMA), how to order and flatten nested loops, whether a reduction should be persistent or looped, and more. In Triton or CUDA, switching between these choices means rewriting the kernel entirely; in Helion the optimal choice is found algorithmically.

This autotuning process is why a Helion kernel can often outperform a hand-written kernel in a lower-level language, when benchmarked on a large set of shapes. With that said, autotuning is sometimes a lengthy process, so it is beneficial to have an established approach for shipping a kernel bundled with pre-tuned configs. This is where the Kernels project comes in.

## Intro: Kernels

The current landscape of kernel packaging and distribution is fragmented, characterized by inconsistent source structures, disparate tooling, and limited compatibility support. Consequently, users often face arduous build times, even when pre-built wheels are available.

The Kernels project addresses these challenges by establishing a standardized, unified packaging and build process for both AoT and JIT kernels. The project is divided into two primary components:

: A tool for developers to reliably package and distribute kernels across different framework versions and system configurations. It enforces standards to ensure predictable source structures, build reproducibility, native PyTorch compatibility, and easy community sharing.`kernel-builder`

: A consumer-facing Python library that allows users to effortlessly load ready-to-use kernels without dependency management issues via a simple command like`kernels`

`get_kernel("org/name", version=1)`

, much like pulling a model or dataset from the Hugging Face Hub.

For kernel users, we want to provide a seamless experience of loading kernels and getting them ready to use right away. Let’s take a look at an example of how one could load the popular Flash-Attention 3 kernel:

We provide prebuilt binaries for a comprehensive compatibility matrix of ahead-of-time kernels, such as Flash Attention 3. This is quite beneficial to end users, particularly when the kernel’s upstream repository may not have a specific build available.

Users can browse a wide variety of kernels on the Hugging Face Hub platform: [hf.co/kernels](http://hf.co/kernels):

We refer to this collection of kernels as the **Kernels Hub**.

## Packaging and using Helion in Kernels

Helion kernels are plain Python. They compile themselves the first time you call them, so there is nothing for `kernel-builder`

to compile ahead of time. Helion provides utilities to tune these kernels for specific workloads and hardware (more on that in a bit) so that users can tune once and reuse later. Helion kernels are also *noarch *kernels: you ship the source, and Helion does the rest on the user’s machine.

In this section, we discuss how to scaffold and structure a Helion kernel for building with `kernel-builder`

.

### Start from the scaffold

`kernel-builder init`

gives you a working kernel project to edit:

Note the `--`

before the directory name. `--backends`

takes any number of values, so without the separator the directory name is read as another backend.

The scaffold assumes a compiled kernel, so delete the parts you don’t need:

That leaves three files to edit.

`build.toml`


Two things worth paying heed to:

`python-depends = ["helion"]`

records that the kernel needs Helion at runtime. When someone loads the kernel,`kernels`

checks that Helion is importable and gives a clear error if it isn’t.`[torch-noarch]`

says there is no ahead-of-time compilation.

`torch-ext/vector_add_helion/__init__.py`


`torch-ext/vector_add_helion/__init__.py`

This example here uses a hardcoded config, pinned via `config=`

. In a later section we’ll go into details on pre-tuning and shipping a decision tree of configs covering a large set of shapes.

`flake.nix`


`flake.nix`

The scaffolded one needs no changes:

### Build and publish

Build and publish the builds to the Hub:

The build produces one directory per backend, each holding your `__init__.py`

alongside a generated `metadata.json`

that carries the Helion dependency forward:

Below is an example of the published kernel on the Hub: [sayakpaul/vector-add-helion](https://huggingface.co/kernels/sayakpaul/vector-add-helion).

### Using the kernel

Users would need Helion installed (`pip install helion`

) and a version of `kernels`

that knows about it. Older releases reject the dependency outright with `unsupported kernel dependency: helion`

.

## Pre-tuning and Shipping Pre-tuned configs

To ensure the shipped Helion kernel performs well on different input problem shapes and different GPU generations, it’s often beneficial to pre-tune them. The workflow has three steps:

- tune the kernel across a representative set of shapes,
- let Helion build a decision tree that maps each shape to its best config
- ship that tree beside your kernel.

At load time, Helion reads the tree (stored as a plain python file next to the kernel source file) and picks a config per call – no tuning on the user’s machine. To do this, the first kernel source change is a decorator:

Write a small script that calls the kernel on every shape you want covered during pre-tuning:

Then hand that script to Helion’s AOT runner:

The runner drives `bench.py`

, accomplishing three phases:

**Collect:** autotunes each shape independently,

**Measure:** re-benchmarks every discovered config on every shape

**Build:** selects the smallest set of configs that keeps each shape within –threshold of its own best (1.01 = within 1%), up to –max-configs. If one config satisfies every shape, that’s all you ship; if shapes diverge, you get a tree of several.

The runner produces a plain-Python file next to your kernel source, named `_helion_aot_<source-module>_<device>_<compute>.py`

, which can be shipped together with the kernel source file alongside other files in the build on the Hub. So the resulting file structure may look like this:

When a consumer uses `get_kernel`

to access this kernel and call it on a tensor, Helion will use the decision tree to identify a pre-tuned config that fits the runtime input shape.

## Examples

### Attention

In [HelionDSL/attention](https://huggingface.co/kernels/HelionDSL/attention), we show an example of a pre-tuned Helion attention kernel, shipped via Kernels. It includes pre-tuned configs for NVIDIA H100s, created using the workflow and structure described above. We measured the performance of these pre-tuned configs, comparing against the FLASH backend of PyTorch’s `scaled_dot_product_attention`

implementation on an H100. This shipped kernel outperforms SDPA on 19 out of 19 of the pre-tuned shapes, with a geomean speed-up of **1.20**. On held-out shapes not seen during tuning, the kernel outperforms SDPA on 9 out of 10 shapes, with a geomean speed-up of **1.17**.

### Linear Attention

In [HelionDSL/linear-attention](https://huggingface.co/kernels/HelionDSL/linear-attention) we ship seven pre-tuned linear-attention kernels: linear attention, simple GLA, retention, GLA, delta rule, gated delta rule, and KDA. It includes pre-tuned configs for NVIDIA B200s. We [measured the performance](https://gist.github.com/tarinduj/4e1178840ffea453c5c72ce9e33cc5f2) of these pre-tuned configs against FLA. Across the six pre-tuned shapes the shipped kernels are faster than flash-linear-attention on all seven variants, with a geomean speed-up of **1.41** on device time (CUDA-graph replay) and **1.33** end to end (including CPU dispatch). On six held-out shapes not seen during tuning, the geomean speed-up is **1.35** on device time and **1.31** end to end. Forward and backward together give a geomean speed-up of **1.55** on the pre-tuned shapes.


**Conclusion**

In this post, we discussed the Helion, a high-level DSL from Meta, and the Kernels project from Hugging Face. We also showed how the two projects complement each other to ease the process of how compute-optimized kernels are developed, distributed, and used. We welcome you to try out Helion and publish your cool Helion kernel on the Hub 🤗

**Acknowledgments:** Thanks to Daniël de Kok and Lysandre Debut for reviewing the post.
