# [Issue #2793] Issues with IDE Setup documentation and VSCode IntelliSense navigation in `__device__` code

source: https://github.com/NVIDIA/cutlass/issues/2793
state: closed | updated: 2026-09-21T16:52:07Z
labels: documentation, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

I am trying to set up my local development environment following the documentation at [IDE Setup](https://docs.nvidia.com/cutlass/media/docs/cpp/ide_setup.html), but I have encountered a few issues regarding the configuration correctness and IDE features (VSCode + Nsight Visual Studio Code Edition + [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)).

**1. Potential documentation error regarding `nvcc` flags**
The documentation mentions configuration options that seem to include `-xcuda` with `Compiler: /usr/local/cuda/bin/nvcc`. However, `nvcc` does not appear to support the `-xcuda` flag.
Could you please verify if the documentation is outdated or if this flag is intended for a specific compiler setup that isn't clearly distinguished?

**2. "Go to Definition" fails inside `__device__` functions**
I am using VSCode with the **Nsight Visual Studio Code Edition** plugin and have configured `c_cpp_properties.json` as suggested.
- **Working:** I can successfully use `Ctrl + Left Click` (Go to Definition) on CuTe structures like `TiledCopy` and `ThrCopy` when they are used inside the `main` function (host code).
- **Not Working:** The same "Go to Definition" feature fails when clicking on `TiledCopy` or `ThrCopy` inside `__device__` functions or kernels. The IDE does not seem to resolve the definition correctly in the device context.

**Request**
Could you please share a working `.vscode` configuration (specifically `c_cpp_properties.json` or `settings.json`) that is verified to support full code navigation (Go to Definition) for CuTe/Cutlass structures within both host and device code? Here is my configuration:
```json
// .vscode/c_cpp_properties.json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/src/cutlass/include",
                "${workspaceFolder}/src/cutlass/tools/util/include",
                "${workspaceFolder}/src/cutlass/examples/common"
            ],
            "defines": [
                "__CUDACC__",
                "__NVCC__",
                "__clang__",
                "__CUDACC_VER_MAJOR__=12",
                "__CUDACC_VER_MINOR__=8",
                "__CUDA_ARCH__=890",
                "__CUDA_ARCH_FEAT_SM89_ALL"
            ],
            "compilerPath": "/usr/local/cuda/bin/nvcc",
            "cStandard": "gnu17",
            "cppStandard": "gnu++17",
            "intelliSenseMode": "linux-gcc-x64"
        }
    ],
    "version": 4
}
```

Thanks!

## 评论 (2)

### github-actions[bot] · 2025-12-21

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-21

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
