source: https://docs.nvidia.com/nsight-visual-studio-edition/known-issues/index.html

# Known Issues[#](https://docs.nvidia.com#known-issues)

Known issues with NVIDIA Nsight Visual Studio Edition.

Debugging with NVIDIA Nsight™ VSE on the following GPU, WDDM driver and Windows version combination can lead to unexpected behavior:

The r580 driver released with the initial release of the CUDA Toolkit 13.0

GeForce RTX 50 series

Windows 11 24H2 (Build 26100) or later

Hardware scheduling enabled


Under these conditions:

The application being debugged may freeze in certain debugging scenarios including (but not limited to) stepping over barriers and attempting to break into the application in running state.

In rare cases, the system may hang or freeze. This is especially likely to occur when connecting to a remote machine using a remote desktop connection (RDP) or VNC for debugging.


To work around this issue, you use one of the following solutions:

Upgrade to the NVIDIA driver version 581.36 or newer.

Disable hardware scheduling, and

**reboot your system**.Downgrade to NVIDIA r576 driver,

**minor version r576.66 or earlier**.

Debugging with NVIDIA Nsight™ VSE with the following GPU, WDDM driver and Windows version combination can lead to a

**system-wide hang/freeze**.The r576.80 driver released with CUDA Toolkit 12.9 Update 2. Earlier versions of the driver do not have this issue.

GeForce RTX 50 series

Windows 11 24H2 (Build 26100) or later

Hardware scheduling enabled


To work around this issue:

Upgrade to the NVIDIA driver version 581.36 or newer.

Disable hardware scheduling, and

**reboot your system**.

Note

Attempting to start CUDA debugging after disabling hardware scheduling without rebooting

**may result in a system-wide hang/freeze**.Downgrade to the earlier version of the NVIDIA r576 driver (e.g. r576.66) or,


Opening gzipped coredump files in Nsight™ VSE is not currently supported. These files need to be uncompressed before they are opened in Nsight™ VSE.

While Microsoft Compute Driver Model (MCDM) is supported as of version 2024.2.0, debugging on Hopper architecture with MCDM enabled is not supported. This issue was resolved in 565.26 or later driver releases. (4578947)

The r555 WDDM driver released with the CUDA Toolkit 12.5 has a known issue when CUDA_ENABLE_COREDUMP_ON_EXCEPTION=1 that will prevent coredump file generation and may cause a segmentation fault. This is not an issue with earlier drivers (ie. r551) or other driver modes (TCC, MCDM).

This WDDM issue was resolved as of the 565.26 driver release. (4561899, 4658131)


When debugging programs built with OptiX/RTCore, with NVIDIA Nsight™ VSE version 2023.1.0 or earlier, it may be necessary to set the environment variable `OPTIX_FORCE_DEPRECATED_LAUNCHER` to 1. If breakpoints are unable to be hit, try setting this environment variable before starting your application.

In version 2020.3.0, Visual Studio breakpoint hit count support was introduced. As with normal conditional breakpoints, both the Visual Studio debugger and the NVIDIA debuggers take an increasing amount of time to run as the number of threads and iterations evaluating the breakpoint condition and count increase. Noticeable delays should be expected when using this breakpoint feature in heavily utilized code. (200666330)

When the display driver is in TCC mode, reading managed memory in the Memory window or visualizing expressions containing managed data can sometimes return stale data if those regions have been written to from the CPU side and have not been synchronized back to the GPU memory. This issue does not affect unmanaged memory and managed memory in WDDM driver mode. (DTNSV-593)

CUDA grid launch failures occur on Pascal GPUs when debugging with preemption enabled. A workaround for this issue is to use a second GPU for rendering the desktop, and use the Pascal GPU dedicated for compute work without a display attached. (55322)

If you are using NVIDIA Nsight™ VSE on a Windows 10 x64 machine, you cannot attach to a win32/x86 CUDA application. Only 64-bit CUDA applications are supported. (44794)

Half2 types are not supported for conditional breakpoints. (37814)

Firewall and anti-intrusion software (e.g., McAfee Host Intrusion Prevention) will not allow remote debugger connections. Please disable or add an exclusion for the Nsight Monitor. (22804)

In some cases, when the CUDA application is built with the “Generate Relocatable Device Code” option, and a CUDA kernel function is declared with the

`__global__ static`

attributes, the NVIDIA Nsight™ VSE debugger might not be able to display local variables inside that function. Users can workaround this issue by simply removing the`static`

qualifier on the function. (21914)You must enable Memory Checker before launching a process, and cannot change the setting while debugging (applies to Legacy Debugger only). (18935, 18937)

When the CUDA Debugger is used to debug CUDA applications which share resources with DirectX 9 (such as the “simpleD3D9” sample program), the debugger may display incorrect values for memory locations in those shared resources. This may happen when the GPU device executing the application is Compute Capability 2.0 or higher. Incorrect values for the contents of memory may be displayed in any debug window (Autos, Locals, Watch, Warp Watch, or Memory). This issue does not affect applications using Direct3D 11. (13899)

When using the CUDA Debugger with NVIDIA Nsight™ VSE, breakpoints will not be hit in source files whose full paths contain non-ASCII characters. Any path with a character code >= 128 is affected. (11429)

If you experience hangs or TDRs while locally debugging CUDA on a single GPU (or using the Software Preemption debugging mode in general), try disabling operating system features that use video hardware acceleration. For example, disabling Aero on Windows 7, changing to a high-contrast desktop theme on Windows 8, or disabling WPF acceleration.

Variables do not appear for source code that is not executed. This occurs because the compiler aggressively optimizes code even if you have not specified any compiler optimizations. As a result, the compiler removes any code that will not be executed from the output executable.

Breakpoints will hit multiple times on lines that have more than one inline function call. For example, setting a breakpoint on:

x = cos() + sin()

will generate three breakpoints on that line. One for the evaluation of the expression, plus one for each function on the line.

Unloading modules does not refresh the state of breakpoints set in that module. This means that those breakpoints do not show their latest state in Visual Studio when they have been unloaded.

The Visual Studio Breakpoint “Filter” option is not supported for CUDA GPU breakpoints.

The F5 hotkey (which is the default hotkey in Visual Studio for starting the CPU Debugger) does not start the CUDA Debugger. To start the CUDA Debugger, you must either change the key bindings or use the menu command: Nsight > Start CUDA Debugging.

There is no support for automatically performing a Build when launching the CUDA Debugger.

The Load Symbols option, or “Symbols settings,” in the Modules view is not supported for CUDA debugging.