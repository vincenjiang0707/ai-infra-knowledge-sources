# [Issue #2574] [Installation]: Wheels compiled with MACA flags cannot be installed on identically configured machines

source: https://github.com/kvcache-ai/Mooncake/issues/2574
state: open | updated: 2026-09-23T03:15:40Z
labels: stale

## 正文

### Installation errors

## Background

This issue was discovered during development and deployment on Muxi GPU platforms. When building the Mooncake Transfer Engine wheel package with MACA compilation parameters enabled, the generated installation package cannot be deployed normally on other devices with the same hardware and software environment configuration.

## Issue Description

When we build the wheel with `-DMACA` compilation flags, the output wheel package installs successfully on other machines with identical Muxi GPU hardware and system environments. However, an error is raised during TE initialization when running Python scripts.

The detailed error log is provided below:

```
terminate called after throwing an instance of 'spdlog::spdlog_ex'
  what(): logger with name 'KFI' already exists what(): logger with name 'KFI' already exists                                    Aborted (core dumped)
```

## Root Cause

The `auditwheel repair` command automatically bundles all dependent shared libraries (including MACA runtime libraries `libmccl.so*`, `libmcruntime.so*`) into the wheel package by default during the packaging process.

At runtime, the bundled MACA runtime libraries attempt to initialize their own logger named `KFI` upon loading. However, the Mooncake Transfer Engine framework has already initialized a logger with the exact same `KFI` name in the current process. Since spdlog does not allow creating duplicate loggers with identical names, it throws an `spdlog::spdlog_ex` exception with the message *"logger with name 'KFI' already exists"*, which triggers a process abort during TE initialization

## Proposed Solution
Add MACA-related runtime libraries to the exclusion list of the `auditwheel repair` command in the wheel build script, following the same pattern as the existing excluded third-party libraries.

The modified packaging command is as follows:
```bash
${AUDITWHEEL_CMD} repair ${OUTPUT_DIR}/*.whl \
    --exclude libcurl.so* \
    --exclude libfabric.so* \
    --exclude libefa.so* \
    ...
    --exclude libaccl_barex.so* \
    --exclude liburma.so* \
+    --exclude libmccl.so* \
 +   --exclude libmcruntime.so*
```

## Environment Information

- Hardware: Muxi GPU
- Build flag: `-DMACA` enabled
- Component: Mooncake Transfer Engine (TE) wheel packaging
- Tool: auditwheel

### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (3)

### github-actions[bot] · 2026-06-23

Thanks for opening this issue, @XiangGuiXiao!

| Field | Value |
|-------|-------|
| **Issue** | #2574 |
| **GitHub user ID** | `184745144` |
| **Reporter** | @XiangGuiXiao |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### XiangGuiXiao · 2026-06-24

Mooncake version: 0.3.11 (this issue affects all versions when built with the -DMACA flag

Steps to reproduce:
1. Build the Mooncake Transfer Engine with the `-DUSE_MACA` compile flag enabled.
2. Run `scripts/build_wheel.sh` to generate the Python wheel package.
3. Copy the generated wheel file to another machine with identical Muxi GPU hardware and system environment, then install it via pip.
4. Run a Python script that calls the API to initialize the Mooncake TE transport engine and use the register/transfer  API .
5. The process aborts with core dump, throwing an spdlog exception: `logger with name 'KFI' already exists`.

### github-actions[bot] · 2026-09-23

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
