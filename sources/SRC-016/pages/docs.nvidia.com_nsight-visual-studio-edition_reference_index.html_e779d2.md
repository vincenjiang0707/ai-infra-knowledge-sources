source: https://docs.nvidia.com/nsight-visual-studio-edition/reference/index.html

# Reference[#](https://docs.nvidia.com#reference)

Additional resources for NVIDIA Nsight VSE.

## Reference Topics[#](https://docs.nvidia.com#reference-topics)

This section provides additional information and resources for the NVIDIA Nsight Visual Studio Edition User Guide.

## Debugging External Applications[#](https://docs.nvidia.com#debugging-external-applications)

Early versions of NVIDIA Nsight™ VSE were only able to debug projects built in Visual C++. However, as of NVIDIA Nsight™ VSE 3.1, CUDA debugging is supported for both C++ and C# projects.

If you would like to use NVIDIA Nsight™ VSE to debug an application that is built in an environment other than C++ or C#, use the tutorial outlined below.

Using NVIDIA Nsight™ VSE Debugging with Other Project Types

In Visual Studio, create a “dummy” project by going to File > New > Project.

Select an Empty C++ Project.

Enter the name for your project and click OK.

Select the project’s Nsight User Properties to edit the default settings.

As an alternative, you can also go to the

**Project**menu >**Nsight User Properties**.Select Launch external program, and enter the path to the external program for the application that is to be debugged.

Configure any other launch optionswhich may be necessary for your particular debugging environment.

(For assistance, refer to

[Host Basics](https://docs.nvidia.com/install-setup/index.html#host).)Click OK to save your settings.

You can now begin debugging your application with NVIDIA Nsight™ VSE.

To do so, go to the Nsight menu or right-click on your project, then select the appropriate activity [Start CUDA Debugging, Start Graphics Debugging, etc.].


## Tesla Compute Cluster (TCC)[#](https://docs.nvidia.com#tesla-compute-cluster)

For most GPUs, you do not have to do anything specific in NVIDIA Nsight™ VSE to enable debugging on a Tesla Compute Cluster (TCC) device. You don’t have to modify your Visual Studio project or enable any specific setting. The TCC device simply shows up as a standard CUDA device. For some GPUs, the default mode is not TCC. See below for more information.

Note

Do not kill a process that is executing code on a TCC device and paused on a breakpoint, except through the normal Stop Debugging command (SHIFT+F5) in Visual Studio. Abnormal termination of a target application that is paused during a debugging session on a TCC device results in unpredictable behavior. It causes future calls to `cuCtxInit()`

to hang indefinitely, even though the killed process seems to terminate normally. The only way to recover is to reboot the target machine. See the latest release notes to learn about any changes in this behavior.

### Limitations[#](https://docs.nvidia.com#limitations)

There are 2 main limitations you will encounter when debugging code running on a TCC device:

There is no Vulkan, OpenGL, or Direct3D interop support.

You cannot have a display connected to an adapter when the underlying device is running in TCC mode. Physically connecting a display causes unpredictable behavior. Windows detects the TCC adapter as a “Standard VGA” device (which it is not), connected to the existing NVIDIA device. The unpredictable behavior results in having to reboot the entire system.


### Setting TCC Mode for Tesla Products[#](https://docs.nvidia.com#setting-tcc-mode-for-tesla-products)

NVIDIA GPUs can exist in one of three modes: **TCC**, **MCDM**, or **WDDM**. TCC and MCDM modes disables Windows graphics and is used in [headless](https://docs.nvidia.com/install-setup/index.html#setup-local-headless-gpu-debugging) configurations, whereas WDDM mode is required for Windows graphics. NVIDIA GPUs also come in three classes:

**GeForce**— typically defaults to WDDM mode; used in gaming graphics.**Quadro**— typically defaults to WDDM mode, but often used as TCC compute devices as well.**Tesla**— typically defaults to TCC mode, although MCDM is also available. Current drivers require a GRID license to enable WDDM on Tesla devices.

NVIDIA Nsight™ VSE [Compute debugging](https://docs.nvidia.com/cuda-debugger/index.html) does *not* require a specific driver mode.

The NVIDIA Control Panel will show you what mode your GPUs are in; alternately, you can use the `nvidia-smi`

command to generate a table that will display your GPUs and what mode they are using.

To change the TCC mode, use the NVIDIA SMI utility. This is located by default at `C:\Windows\System32\nvidia-smi.exe`

. Use the following syntax to change the TCC mode:

```
nvidia-smi -g {GPU_ID} -dm {0|1|2}
```

0 = WDDM

1 = TCC

2 = MCDM

Note

See [Compute Debugger Supported Configurations](https://docs.nvidia.com/install-setup/index.html#system-requirements-compute-debugger-configs) for details on supported GPUs and driver modes.

### About TCC[#](https://docs.nvidia.com#about-tcc)

The TCC (Tesla Compute Cluster) driver is a Windows driver that supports CUDA C/C++ applications. The driver enables remote desktop services, and reduces the CUDA kernel launch overhead on Windows. Note that the TCC driver disables graphics on the Tesla products.

The main purpose of TCC and the Tesla products is to aid applications that use CUDA to perform simulations, and large scale calculations (especially floating-point calculations), such as image generation for professional use and scientific fields of study.

The benefits of using the Tesla Compute Cluster driver package:

TCC drivers make it possible to use NVIDIA GPUs in nodes with non‐NVIDIA integrated graphics.

NVIDIA GPUs on systems running the TCC drivers will be available via Remote Desktop, both directly and via cluster management systems that rely on Remote Desktop.

NVIDIA GPUs will be available to applications running as a Windows service (in Session 0) on systems running the TCC drivers.


The TCC driver was specifically designed to be used with Microsoft’s Windows HPC Server 2008. However, NVIDIA’s TCC driver can be used with operating systems other than Windows HPC Server 2008. The NVIDIA TCC driver does not have the same pinned allocation limits or memory fragmentation behavior as WDDM. You can mix TCC drivers with XP-style display drivers.

For more information about supported operating systems, and compatibility with other NVIDIA drivers, refer to the documentation on NVIDIA Tesla:


[http://www.nvidia.com/object/tesla_computing_solutions.html]For more information about NVIDIA hardware compatibility on Windows HPC Server 2008, see:


[http://technet.microsoft.com/en-us/library/ff793340_ws.10_.aspx]To search the NVIDIA web site for Tesla drivers, see:


## Environment Variables[#](https://docs.nvidia.com#environment-variables)

NVIDIA Nsight™ VSE creates certain system environment variables that are useful when defining build properties. These are separate from the build macros defined by Visual Studio.

For more information about the list of macros available for build commands such as `$(OutDir)`

and `$(TargetName)`

, see the MSDN article on [Macros for Build Commands and Properties](http://msdn.microsoft.com/en-us/library/c02as0cs.aspx).

To see the environment variables related to CUDA paths:

Open the Advanced System Settings panel in the Control Panel.

Start > Control Panel.

Select System and Maintenance.

Select System.

In the left-hand pane, select Advanced system settings.

The System Properties window opens.


Click the Environment Variables button.

Under System Variables, scroll to see the variables that have CUDA in the name.

Click OK to close the window.


The Environment Variables window lists the system environment variables that begin with CUDA. These are variables that you can use in the project Property Pages to control various aspects of the build process.

## DirectCompute[#](https://docs.nvidia.com#directcompute)

Microsoft DirectCompute is an application programming interface (API) that supports general-purpose computing on graphics processing units on Microsoft Windows 7 and Windows 8.

NVIDIA’s Direct3D 11 GPUs support DirectCompute. This allows developers to harness the massive parallel computing power of NVIDIA GPUs to create compelling computing applications in consumer and professional markets.

See Also


Reference

## Troubleshooting NVIDIA Nsight Visual Studio Edition[#](https://docs.nvidia.com#troubleshooting-nvidia-nsight-visual-studio-edition)

**Problem:**

When I convert a project to a newer version of Visual Studio, I get build errors.

**Resolution:**

For more information on how to convert a project, see the [NVIDIA Developer Forums](http://devtalk.nvidia.com/).

Problem:

How do I get a diagnostic log(s) of the NVIDIA Nsight™ VSE for troubleshooting purposes?

Resolution:

Close Visual Studio.

Go to the following location, and delete any existing files:

%AppData%\NVIDIA Corporation\Nsight\Vsip\1.0\Logs

Edit

`Nvda.Diagnostics.nlog`

as follows.C:\\Program Files (x86)\\NVIDIA Corporation\\Nsight Visual Studio Edition 2023.2\\Host\\Common\\Configurations

Go to the last logger at the bottom of the file:

<logger name="*" minlevel="Error" writeTo="file-high-severity" />.

Change the

`minlevel`

attribute value from`"Error"`

to`"Trace"`

.Save the file.

Reproduce the problem, and send the following generated logs:

%AppData%\NVIDIA Corporation\Nsight\Vsip\1.0\Logs


**Problem:**

When breakpoints are set in source code, the CUDA Debugger pauses execution at locations unrelated to the breakpoints.

This can happen when more than one `__global__`

function (kernel) makes a call to a `__device__`

function within a single module, and both of the following are true:

the

`__device__`

function is not inlined.the different kernels call the exact same

`__device__`

function.

**Resolution:**

There are a couple of approaches you can take to work around this issue:

Force the

`__device__`

function to be inlined by applying the`__forceinline__`

keyword to the`__device__`

function. Note that using the`inline`

keyword does not force inlining in debug builds.Reorganize source code so that there is only one

`__global__`

function for each instance of the`__device__`

function. This means that each`.cu`

file that is compiled with the NVIDIA CUDA Compiler (nvcc.exe) should contain no more than one`__global__`

function. This works for both Driver API and CUDART applications. Be aware that there are other potential issues with this approach:Recommended: move commonly used

`__device__`

functions to common header files. Use the`#include`

statement to include the`__device__`

function in each`.cu`

file containing a`__global__`

function.Potential issue: If your source code contains declarations of a global variable in the following style:

__device__ int x;

and that variable is used by multiple

`__global__`

functions, then using multiple files to make multiple calls to the`__global__`

function is not a trivial work-around. In this case, we recommend eliminating global variables that are declared in that style from the source code, and making them kernel parameters instead.Potential issue: Each

`__constant__`

variable is associated with one CUDA module (a compiled`.cu`

file).If your source code is written in a way that multiple kernels depend on the same

`__constant__`

variable, and the host code side of your application dynamically updates that variable, then you will need some broader changes to your source code:For a CUDART application, when copying the

`__constant__`

variable into each`.cu`

file, give each variable a different name.Any host code that was updating the previously single instance of the variable must now update all the instances.




**Problem:**

My machine hangs when I use the CUDA Debugger locally on a single machine with 2 GPUs on it.

**Resolution:**

There are several possible issues that can cause a machine to hang when locally debugging on two GPUs with the NVIDIA Nsight™ VSE tools.

We recommend not having a display attached or a desktop running on the GPU on which you are debugging CUDA code, as having concurrent activities on a GPU can cause machine hangs. See [How To: Setup Local Headless GPU Debugging](https://docs.nvidia.com/install-setup/index.html#setup-local-headless-gpu-debugging) for more information.

**Problem:**

The GPU debugger hangs when I also use the CPU debugger.

**Resolution:**

Never use the same Visual Studio instance to run both the CUDA Debugger and the CPU debugger.

In general, make sure you only use either CUDA Debugger or CPU debugger, not both. Attaching the CPU debugger and hitting a CPU breakpoint during a CUDA debugging session will cause the CUDA Debugger to hang (until you resume the CPU process).

If you are careful, you can attach two separate Visual Studio instances (one CUDA, one CPU). While you are stopped in CPU code, the CUDA Debugger will hang. Once you resume the CPU code, CUDA Debugger will come back alive.

**Problem:**

I am unable to set and hit a breakpoint in my CUDA code.

**Resolution:**

Make sure to use the driver version specified in the release notes. This is the most common reason that breakpoints do not work. The driver must be installed on the machine where your application code runs.

Also, make sure your project uses a compatible CUDA toolkit. A compatible version of the CUDA toolkit generates symbolic information that allows the CUDA Debugger to properly debug your code when you use the `-G`

flag on the `nvcc`

command line. If you are using the CUDA Driver API, make sure that there are `.cubin.elf.o`

files alongside each of your compiled `.cubin`

files in the build output directory for your project. Projects using the CUDA Runtime API have the symbolic information embedded in the object file itself.

**Problem:**

I get the following error message:

```
Local debugging failed. Nsight is incompatible with WPF acceleration.Please see documentation about WPF acceleration. Run theDisableWpfHardwareAcceleration.reg in your Nsight installation.
```

**Resolution:**

Disable WPF D3D acceleration. For more information, see [Setup Local Debugging](https://docs.nvidia.com/install-setup/index.html#setup-local-headless-gpu-debugging).

If one or more applications are running with WPF hardware acceleration and you run the `.reg`

file, you could still have issues until those applications are restarted.

**Problem:**

My program ignores breakpoints set in CPU code when I debug a program by choosing Start CUDA Debugging from the Nsight menu.

**Resolution:**

The CUDA Debugger ignores breakpoints set in CPU code as it does not currently support debugging x86 or other CPU code.

**Problem:**

When I hit a CUDA breakpoint, I only break once on thread (0, 0, 0) in my CUDA kernel. If I hit Continue (F5), it never breaks again and the entire launch completes.

**Resolution:**

The default behavior of the CUDA Debugger is to break unconditionally on the first thread of a kernel. After that, the breakpoints have an implicit conditional based on the CUDA Focus Picker. If you would like to break on a different thread, use the CUDA Focus Picker to switch focus to the desired thread or set a conditional breakpoint so that the debugger stops only on the thread you specify. For more information on setting the conditional breakpoint, see [How To: Set GPU Breakpoints](https://docs.nvidia.com/cuda-control-gpu-execution/index.html#gpu-breakpoints). After you switch focus, the CUDA Debugger maintains the focus and breaks on breakpoints only in that thread for the duration of the kernel launch.

**Problem:**

I encounter an error when trying to copy and paste my shader code.

**Resolution:**

This can happen in Visual Studio 2012, when the Productivity Power Tools extension is being used. Disable the HTML Copy option, and you should be able to copy and paste normally in the shader editor.

Notices

Notice

ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.

Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication of otherwise under any patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all other information previously supplied. NVIDIA Corporation products are not authorized as critical components in life support devices or systems without express written approval of NVIDIA Corporation.

Trademarks

NVIDIA and the NVIDIA logo are trademarks or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.