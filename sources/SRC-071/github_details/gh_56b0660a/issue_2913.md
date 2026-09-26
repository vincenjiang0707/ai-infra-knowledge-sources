# [Issue #2913] [Feature Request] Add TileLang support to Compiler Explorer (Godbolt)

source: https://github.com/tile-ai/tilelang/issues/2913
state: closed | updated: 2026-08-25T06:11:22Z
labels: enhancement, help wanted

## 正文

### Required prerequisites

- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) and did not find an existing issue requesting TileLang support in Compiler Explorer.

### Motivation

[Compiler Explorer](https://godbolt.org/) provides an interactive way to experiment with code and inspect compiler output in the browser. It already supports GPU programming systems such as Triton and CuTe DSL.

Adding TileLang support would make it easier to:

- experiment with small TileLang kernels without setting up a local environment;
- inspect useful compiler outputs and transformations;
- compare TileLang versions or supported targets;
- share reproducible examples through Compiler Explorer links;
- help new users learn TileLang and help contributors investigate compiler behavior.

Issue #1895 discusses pass/IR dumping that could also be useful in a Compiler Explorer context, but this request is broader: making TileLang available as a supported language/compiler on the platform.

### Solution

Add TileLang support to Compiler Explorer so that users can enter a self-contained TileLang example and inspect useful compilation results in the browser.

The implementation approach is intentionally left open. Contributors and maintainers familiar with TileLang, TVM, and Compiler Explorer may be able to identify a better design than any solution proposed upfront.

### Alternatives

Users can currently run TileLang locally and inspect generated output using its existing debugging and inspection facilities. However, that does not provide the same discoverability, convenience, version comparison, or shareable browser-based experience.

### Additional context

- Compiler Explorer: https://godbolt.org/
- Compiler Explorer repository: https://github.com/compiler-explorer/compiler-explorer
- Related TileLang IR-dump request: #1895

Contributions and design suggestions from the community would be very welcome.

## 评论 (1)

### penguin-wwy · 2026-08-12

I’ve done a sample analysis of what it takes to bring TileLang to Compiler Explorer (CE), following the established pattern used by Triton and CuTe DSL.

* 1. What Compiler Explorer needs (CE side)
    CE supports Python GPU DSLs via an “interpretr exe + wrapper script” pattern: the compiler’s exe is the Python interpreter of a per-version venv, and CE runs `python3 -I <wrapper>.py --output_file out.s example.py`. Since CE production machines have no GPU, the wrapper must compile-only and dump intermediates.

* 2. GPU-less compilation

* 3. Source line ↔ output line linkage
    The eager frontend already stamps TIR nodes with spans, StmtMutator COW preserves them, though a few passes drop spans on newly created nodes. However, codegen never consumes spans — CodeGenTileLangCUDA/CodeGenC emit no #line/line markers, so generated CUDA C carries no source-line clues
  
I think following TODOs need to be completed.

- [ ] Codegen #line emission
  - #3048 
- [ ] Span propagation fixes
  -  #2966 
- [ ] Official compile-only entry point
  - #3045 
- [ ] Verify on the target environment
