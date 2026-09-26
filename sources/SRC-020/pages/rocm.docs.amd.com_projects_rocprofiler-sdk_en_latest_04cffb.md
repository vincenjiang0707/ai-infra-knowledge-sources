source: https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest

# ROCprofiler-SDK documentation[#](https://rocm.docs.amd.com#rocprofiler-sdk-documentation)

ROCprofiler-SDK is a tooling infrastructure for profiling general-purpose GPU compute applications running on the ROCm software.
It supports application tracing to provide a big picture of the GPU application execution and kernel counter collection to provide low-level hardware details from the performance counters.
The ROCprofiler-SDK library provides runtime-independent APIs for tracing runtime calls and asynchronous activities such as GPU kernel dispatches and memory moves. The tracing includes callback APIs for runtime API tracing and activity APIs for asynchronous activity records logging. To learn more, see
[What is ROCprofiler-SDK?](https://rocm.docs.amd.com/what-is-rocprofiler-sdk.html)

You can utilize the ROCprofiler-SDK to develop a tool for profiling and tracing HIP applications on ROCm software.

The code is open source and hosted at [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-sdk).

Note

The ROCprofiler-SDK repository for ROCm 7.0 and earlier is located at [ROCm/rocprofiler-sdk](https://github.com/ROCm/rocprofiler-sdk).

ROCprofiler-SDK uses a companion library called [AQLprofile](https://rocm.docs.amd.com/projects/aqlprofile/en/latest/index.html), that generates profiling command packets (AQL/PM4) for performance counters and SQ thread trace. For details, see the [AQLprofile docs](https://rocm.docs.amd.com/projects/aqlprofile/en/latest/index.html).

The documentation is structured as follows:

To contribute to the documentation, refer to
[Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the
[Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.