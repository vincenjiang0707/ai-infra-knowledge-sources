source: https://rocm.docs.amd.com/en/latest/components/profilers-and-debuggers.html

# ROCm profiling and debugging tools[#](https://rocm.docs.amd.com#rocm-profiling-and-debugging-tools)

ROCm profiling and debugging tools help you measure GPU application performance, identify bottlenecks, and diagnose execution faults.

For an overview of the profiling tools, their relationships, and how to use
them together, see [ROCm profiling tools overview](https://rocm.docs.amd.com/profiling-tools-overview.html). For guidance on choosing the right tool for your performance investigation, see
[Choosing the right ROCm profiling tool](https://rocm.docs.amd.com/profiling-tools-selection.html).

[ROCdbgapi 0.80.0](https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-10.0.0/)– ROCm debugger API library.[ROCgdb 16.3](https://rocm.docs.amd.com/projects/ROCgdb/en/docs-10.0.0/)– Source-level debugger for Linux, based on the GNU Debugger (GDB).[ROCm Compute Profiler 3.8.0](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/)– Kernel-level profiling for machine learning and high performance computing (HPC) workloads.[ROCm Systems Profiler 1.8.0](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-10.0.0/)– Comprehensive profiling and tracing of applications running on the CPU or the CPU and GPU.[ROCprofiler-SDK 1.3.5](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-10.0.0/)– Toolkit for developing analysis tools for profiling and tracing GPU compute applications.[ROCr Debug Agent 2.1.0](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-10.0.0/)– Prints the state of all AMD GPU wavefronts that caused a queue error by sending a SIGQUIT signal to the process while the program is running.

Note

In addition to the profiling tools included in the ROCm Core SDK, AMD provides standalone visualization and analysis tools that help developers explore, interpret, and gain deeper insights from collected performance data. These tools are distributed separately and complement the ROCm profiling workflow.

[ROCm Optiq](https://rocm.docs.amd.com/projects/roc-optiq/en/latest/index.html)is a unified tool for visualizing and analyzing performance data collected by ROCm Systems Profiler and ROCm Compute Profiler, providing insight into both system-level behavior and kernel-level performance for applications running on the ROCm stack. It is distributed separately as part of[ROCm Extras](https://rocm.docs.amd.com/extras.html).[ROCprof Compute Viewer](https://rocm.docs.amd.com/projects/rocprof-compute-viewer/en/latest/index.html)visualizes and analyzes GPU thread trace data collected using`rocprofv3`

, helping developers understand low-level GPU execution behavior, identify performance bottlenecks, and optimize kernel efficiency.