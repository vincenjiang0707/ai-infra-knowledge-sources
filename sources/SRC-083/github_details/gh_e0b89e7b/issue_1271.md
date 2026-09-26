# [Issue #1271] ROCm Backend Status Tracker

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1271
state: closed | updated: 2026-02-23T21:16:07Z
labels: ROCm, Cross Platform

## 正文

This issue summarizes and tracks the current status of ROCm enablement for BitsandBytes.

- [x] Enable ROCm backend for bitsandbytes - Supported from ROCm 6.1
       https://github.com/TimDettmers/bitsandbytes/pull/1207
       Updated CUDA backend to work seamlessly for ROCm. Added hipified versions of CUDA kernels and ops which allows to use optimized HIP kernels for AMD GPUs. Cmake build updated for ROCm and also enabled key features in bitsandbytes functional and autograd api
- [x] Update ROCm install instructions in official bitsandbytes documentation
       https://github.com/TimDettmers/bitsandbytes/pull/1244
       Bitsandbytes can be built for ROCm backend by setting COMPUTE_BACKEND to 'hip' in the cmake command. The instructions to get supported dockers and steps to build ROCm enabled bitsandbytes are present in the [installation](https://github.com/TimDettmers/bitsandbytes/blob/multi-backend-refactor/docs/source/installation.mdx) doc of [multi-backend-refactor](https://github.com/TimDettmers/bitsandbytes/tree/multi-backend-refactor) branch.
- [x] Provide AMD GPU to public CI
       AMD GPU has been successfully added into Huggingface CI for ROCm backend testing
- [x] Enable ROCm build in public CI 
      https://github.com/TimDettmers/bitsandbytes/pull/1255
      Added a new CI job to build bitsandbytes with ROCm backend for push/pull requests to main branch, releases and manually triggered jobs 
- [x] Provide packaging/wheels support for ROCm 
      https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1299
       Updated shared libs and wheels build jobs for ROCm. The new updates will create ROCm specific .so files, which will be packaged into bitsandbytes wheels. In addition to this, the documentation is updated with steps to install bitsandbytes through newly built packages.
- [x] Update Debug Messages/Diagnostic Functions for ROCm
       https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1333
       The diagnostic functions which aid users with debug messages related to installation failures are updated for ROCm. Also, added additional messages for igemmlt failures and a fix to clean up runner disk space for CI jobs.
- [x] Enable packaging for ROCm 6.2
       https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1367
       Wheels packaging is enabled for ROCm 6.2. Users can use pip install directly for ROCm 6.2 after this change.

The completed changes are in multi-backend-refactor branch and will be merged into main once multi-backend design is finalized.

cc: @Titus-von-Koeller @sunway513 @amathews-amd

## 评论 (4)

### Titus-von-Koeller · 2024-07-25

@pnunna93 

PyTorch 2.4 is built with ROCm 6.1, we should be sure that the bundled ROCm binaries are compatible with the newest PyTorch release that just came out.

### Titus-von-Koeller · 2024-07-26

@pnunna93 I'm planning to do the alpha release with prebuilt wheels in the beginning of next week. Do you think you'll have the last item on this list checked by then? I think it would be important to prioritize this so we can move forward and get more user feedback.

### pnunna93 · 2024-07-26

@Titus-von-Koeller Sure, I have been ironing out some details and got most of the info I need. I will start testing and open a PR early next week.

### matthewdouglas · 2026-02-23

I'm going to close this as we've started shipping ROCm wheels to PyPI since [v0.49.0](https://github.com/bitsandbytes-foundation/bitsandbytes/releases/tag/0.49.0). We can track more specific issues separately, but we'll consider this feature request complete.
