# [Issue #9129] [Misc]: CMake Clean-up / Refactor Tasks

source: https://github.com/vllm-project/vllm/issues/9129
state: open | updated: 2026-09-22T09:54:09Z
labels: help wanted, good first issue, keep-open, unstale

## 正文

In an effort to make the CMake more readable, stable and easy to use we have a few tasks we'd like to work on, creating a GitHub issue here to track that progress, some planned changes/investigations:

- [ ] Rename `define_gpu_extension_target`, currently this is used for CPU extensions too so the name is now misleading
- [ ] Add a CI test of local builds, i.e. `pip install -e .`
- [ ]  Warn that PTX builds are not currently supported (post https://github.com/vllm-project/vllm/pull/8845), currently if there is a `+PTX` in `TORCH_CUDA_ARCH_LIST` this will be ignored. We should warn when this is the case. Alternatively we can add support for PTX builds although this is generally not desirable since PTX increases the wheel size by quite a bit (PTX is larger than SASS), and we already build for all currently supported arches.
- [ ]  Have vllm-flash-attn use [ExternalProject](https://cmake.org/cmake/help/latest/module/ExternalProject.html) currently vllm-flash-attn uses the parent CMake scope which creates many footguns since it is in a separate repo, using `ExternalProject` will mean that the vllm-flash-attn will be run in a separate CMake scope/process
  - [ ] It might be even better to revert to the FlashMLA approach, where CMake code lives in vllm.
- [ ] Look into removing early returns in CMakeLists.txt (potentially move backends into its own files)
- [ ] Potential build both C++ and CUDA extensions when building for CUDA and using torch dispatcher to dispatch between the two, https://github.com/vllm-project/vllm/pull/8424

## 评论 (20)

### github-actions[bot] · 2025-01-06

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### LucasWilkinson · 2025-01-06

keep open

### github-actions[bot] · 2025-04-07

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### LucasWilkinson · 2025-04-07

Keep open

### ProExpertProg · 2025-05-30

Btw, I think what we could do for FA is move the CMake build system to vllm completely (like we do for FlashMLA). That will remove the foot-guns, and if we return vllm-flash-attn to the flash-attention build system, reduce the diff with upstream 

### github-actions[bot] · 2025-08-29

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### ProExpertProg · 2025-09-05

not stale

### machafer · 2025-12-17

Hi all, I’d like to help by taking one small item from this tracking issue. which subtask you’ll take first? Thanks!

### mhetrerajat · 2025-12-19

> Look into removing early returns in CMakeLists.txt (potentially move backends into its own files)

Hi, I would like to pick above task if no one is assigned to it yet. Thanks ! 

### ProExpertProg · 2025-12-23

I just reordered the items, please start at the top and go down the list. The first few item should be pretty short!

### mhetrerajat · 2025-12-23

@ProExpertProg @LucasWilkinson 

Hey! I noticed the first item (renaming `define_gpu_extension_target`) was completed in #28026, so I'd like to take a crack at the next one - adding a CI test for local builds (`pip install -e .`).

**My understanding**: Right now the CI tests run against pre-built Docker images, so if someone accidentally breaks the build system (CMakeLists.txt, cmake/, csrc/), the tests still pass and we only find out when the Docker image build fails separately. This test would catch that earlier by actually building from source.

Based on the current CI setup (CPU-only tests in GitHub Actions, GPU/specialized hardware in Buildkite), I'm thinking this should go in Buildkite since the main goal is testing CUDA and AMD/ROCm builds. The macOS smoke test in GitHub Actions already covers the CPU build path.

**A couple of questions:**

1. How thorough should it be? Just verify the build succeeds, or also run a quick inference smoke test like the macOS workflow does?

2. Should it run on every PR, or only when build-related files change? I'm thinking we could use `source_file_dependencies` to trigger only on changes to CMakeLists.txt, cmake/*, csrc/*, setup.py, etc.

Happy to adjust based on what makes sense. Thanks!

### ProExpertProg · 2025-12-23

1. Let's do a smoke test
2. I think we should guard on changes to `csrc` & build files 

### semil007 · 2026-02-04

Hi, I’d like to help with a small part of this tracking issue and I’m planning to improve documentation around the CMake build system,clarifying CPU vs CUDA extension behavior and common pitfalls.
Please let me know if this approach sounds reasonable?.


### jungledesh · 2026-02-05

Hi, 

I'd like to work on item #4 - migrating vllm-flash-attn to use ExternalProject for isolated scoping. 

Happy to discuss the FlashMLA-style alternative too if preferred. 

Is it still open? 

@ProExpertProg @LucasWilkinson 

Update: Submitted a PR, migrating vllm-flash-attn to use ExternalProject. 
Review if acceptable, otherwise, we can go FlashMLA-style.

### TensorDevLJ · 2026-07-12

Hi! I'd like to contribute to this tracking issue. I see several items have already been completed by linked PRs. Is there a remaining cleanup task from this issue that is still available for a first-time contributor? I'd be happy to pick up one of the remaining items.

### shanewidanagama · 2026-08-11

/assign @shanewidanagama
I'd like to start working on this.

### williamclymire-tamu · 2026-08-20

Hi, this is my first time trying to step into the OSS community. I'd like to help out with some cleanup here. I noticed the -static-global-template-stub=false version check is repeated 9 times in CMakeLists.txt. I can pull it into a helper function in cmake/utils.cmake and replace the duplicates. No behavior change.

### dhanushsure07-droid · 2026-08-25

Hi! I'd like to make my first contribution to vLLM.

I'd be interested in working on the task of renaming
`define_gpu_extension_target`, since it is also used for CPU
extensions and the current name is misleading.

Would it be okay for me to work on this as a small standalone
contribution under this tracking issue?

### spgsroot · 2026-08-31

Opened #54532 for the `pip install -e .` CI smoke test item, per @ProExpertProg's guidance (smoke test, gated on csrc & build-file changes). New Buildkite step on intel_cpu building the `vllm-src` stage of Dockerfile.cpu, editable-installing, and smoke-checking `import vllm` from outside the tree + `vllm serve --help`. Verified no existing CI covers this: macOS smoke test is cron-only, and current CPU steps install a prebuilt wheel without the source tree.

### akshatgit07 · 2026-09-22

Hi! I’m a first-time vLLM contributor and I’d like to work on the small subtask to rename `define_gpu_extension_target`, since it is also used for CPU extensions. I plan to identify all definitions and call sites, choose a clearer name with maintainer guidance, update them consistently, and run the relevant build/configuration checks. Is this subtask still available and wanted? If so, I’d be happy to take it.
