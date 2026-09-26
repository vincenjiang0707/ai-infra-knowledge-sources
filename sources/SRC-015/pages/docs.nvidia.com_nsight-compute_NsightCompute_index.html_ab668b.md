source: https://docs.nvidia.com/nsight-compute/NsightCompute/index.html

# 4. Nsight Compute[#](https://docs.nvidia.com#nsight-compute)

The User Guide for Nsight Compute.

## 4.1. Introduction[#](https://docs.nvidia.com#introduction)

NVIDIA Nsight Compute (UI) User Manual: Detailed documentation on views, controls, and workflows.

### 4.1.1. Overview[#](https://docs.nvidia.com#overview)

This document is a user guide to the next-generation NVIDIA Nsight Compute profiling tools. NVIDIA Nsight Compute is an interactive kernel profiler for CUDA applications. It provides detailed performance metrics and API debugging via a user interface and command line tool. In addition, its baseline feature allows users to compare results within the tool. NVIDIA Nsight Compute provides a customizable and data-driven user interface and metric collection and can be extended with analysis scripts for post-processing results.

**Important Features**

Interactive kernel profiler and API debugger

Graphical profile report

Result comparison across one or multiple reports within the tool

Fast Data Collection

UI and Command Line interface

Fully customizable reports and analysis rules


## 4.2. Quickstart[#](https://docs.nvidia.com#quickstart)

The following sections provide brief step-by-step guides of how to setup and run NVIDIA Nsight Compute to collect profile information. All directories are relative to the base directory of NVIDIA Nsight Compute, unless specified otherwise.

The UI executable is called ncu-ui. A shortcut with this name is located in the base directory of the NVIDIA Nsight Compute installation. The actual executable is located in the folder `host\windows-desktop-win7-x64`

on Windows or `host/linux-desktop-glibc_2_11_3-x64`

on Linux. By default, when installing from a Linux `.run`

file, NVIDIA Nsight Compute is located in `/usr/local/cuda-<cuda-version>/nsight-compute-<version>`

. When installing from a `.deb`

or `.rpm`

package, it is located in `/opt/nvidia/nsight-compute/<version>`

to be consistent with [Nsight Systems](https://developer.nvidia.com/nsight-systems). In Windows, the default path is `C:\Program Files\NVIDIA Corporation\Nsight Compute <version>`

.

After starting NVIDIA Nsight Compute, by default the *Welcome Page* is opened. The *Start* section allows the user to start a new activity, open an existing report, create a new project or load an existing project. The *Continue* section provides links to recently opened reports and projects. The *Explore* section provides information about what is new in the latest release, as well as links to additional training. See [Environment](https://docs.nvidia.com/index.html#options-environment) on how to change the start-up action.

### 4.2.1. Interactive Profile Activity[#](https://docs.nvidia.com#interactive-profile-activity)

**Launch the target application from NVIDIA Nsight Compute**When starting NVIDIA Nsight Compute, the

*Welcome Page*will appear. Click on*Quick Launch*to open the*Connection*dialog. If the*Connection*dialog doesn’t appear, you can open it using the*Connect*button from the main toolbar, as long as you are not currently connected. Select your target platform on the left-hand side and your connection target (machine) from the*Connection*drop down. If you have your local target platform selected,`localhost`

will become available as a connection. Use the + button to add a new connection target. Then, continue by filling in the details in the*Launch*tab. In the*Activity*panel, select the Interactive Profile activity to initiate a session that allows controlling the execution of the target application and selecting the kernels of interest interactively. Press*Launch*to start the session.**Launch the target application with tools instrumentation from the command line**The ncu can act as a simple wrapper that forces the target application to load the necessary libraries for tools instrumentation. The parameter

`--mode=launch`

specifies that the target application should be launched and suspended before the first instrumented API call. That way the application waits until we connect with the UI.$ ncu --mode=launch CuVectorAddDrv.exe

**Launch NVIDIA Nsight Compute and connect to target application**Select the target machine at the top of the dialog to connect and update the list of attachable applications. By default,

*localhost*is pre-selected if the target matches your current local platform. Select the*Attach*tab and the target application of interest and press*Attach*. Once connected, the layout of NVIDIA Nsight Compute changes into stepping mode that allows you to control the execution of any calls into the instrumented API. When connected, the*API Stream*window indicates that the target application waits before the very first API call.**Control application execution**Use the

*API Stream*window to step the calls into the instrumented API. The dropdown at the top allows switching between different CPU threads of the application.*Step In*(F11),*Step Over*(F10), and*Step Out*(Shift + F11) are available from the*Debug*menu or the corresponding toolbar buttons. While stepping, function return values and function parameters are captured.Use

*Resume*(F5) and*Pause*to allow the program to run freely. Freeze control is available to define the behavior of threads currently not in focus, i.e. selected in the thread drop down. By default, the*API Stream*stops on any API call that returns an error code. This can be toggled in the*Debug*menu by*Break On API Error*.**Isolate a kernel launch**To quickly isolate a kernel launch for profiling, use the

*Run to Next Kernel*button in the toolbar of the*API Stream*window to jump to the next kernel launch. The execution will stop before the kernel launch is executed.**Profile a kernel launch**Once the execution of the target application is suspended at a kernel launch, additional actions become available in the UI. These actions are either available from the menu or from the toolbar. Please note that the actions are disabled, if the API stream is not at a qualifying state (not at a kernel launch or launching on an unsupported GPU). To profile, press

*Profile Kernel*and wait until the result is shown in the[Profiler Report](https://docs.nvidia.com/index.html#profiler-report). Profiling progress is reported in the lower right corner status bar.Instead of manually selecting

*Profile*, it is also possible to enable*Auto Profile*from the*Profile*menu. If enabled, each kernel matching the current kernel filter (if any) will be profiled using the current section configuration. This is especially useful if an application is to be profiled unattended, or the number of kernel launches to be profiled is very large. Sections can be enabled or disabled using the[Metric Selection](https://docs.nvidia.com/index.html#tool-window-sections-info)tool window.*Profile Series*allows to configure the collection of a set of profile results at once. Each result in the set is profiled with varying parameters. Series are useful to investigate the behavior of a kernel across a large set of parameters without the need to recompile and rerun the application many times.

For a detailed description of the options available in this activity, see [Interactive Profile Activity](https://docs.nvidia.com/index.html#connection-activity-interactive).

### 4.2.2. Non-Interactive Profile Activity[#](https://docs.nvidia.com#non-interactive-profile-activity)

**Launch the target application from NVIDIA Nsight Compute**When starting NVIDIA Nsight Compute, the

*Welcome Page*will appear. Click on*Start Activity*to open the*Start Activity*dialog. If the*Start Activity*dialog doesn’t appear, you can open it using the*Start Activity*button from the main toolbar, as long as you are not currently connected. Select your target platform on the left-hand side and your localhost from the*Connection*drop down. Then, fill in the launch details. In the*Activity*panel, select the*Profile*activity to initiate a session that pre-configures the profile session and launches the command line profiler to collect the data. Provide the*Output File*name to enable starting the session with the*Launch*button.**Additional Launch Options**For more details on these options, see

[Command Line Options](https://docs.nvidia.com/NsightComputeCli/index.html#command-line-options). The options are grouped into tabs: The*Filter*tab exposes the options to specify which kernels should be profiled. Options include the kernel regex filter, the number of launches to skip, and the total number of launches to profile. The*Sections*tab allows you to select which sections should be collected for each kernel launch. Hover over a section to see its description as a tool-tip. To change the sections that are enabled by default, use the[Metric Selection](https://docs.nvidia.com/index.html#tool-window-sections-info)tool window. The*Sampling*tab allows you to configure sampling options for each kernel launch. The*Other*tab includes the option to collect NVTX information or custom metrics via the`--metrics`

option.

For a detailed description of the options available in this activity, see [Profile Activity](https://docs.nvidia.com/index.html#connection-activity-non-interactive).

### 4.2.3. System Trace Activity[#](https://docs.nvidia.com#system-trace-activity)

**Launch the target application from NVIDIA Nsight Compute**When starting NVIDIA Nsight Compute, the

*Welcome Page*will appear. Click on*Start Activity*to open the*Start Activity*dialog. If the*Start Activity*dialog doesn’t appear, you can open it using the*Start Activity*button from the main toolbar, as long as you are not currently connected. Select your local target platform on the left-hand side and your localhost from the*Connection*drop down. Then, fill in the launch details. In the*Activity*panel, select the*System Trace*activity to initiate a session with pre-configured settings. Press*Launch*to start the session.**Additional Launch Options**For more details on these options, see

[System-Wide Profiling Options](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#linux-system-wide-profiling-options).Once the session is completed, the

[Nsight Systems](https://docs.nvidia.com/nsight-systems/UserGuide/index.html)report is opened in a new document. By default, the timeline view is shown. It provides detailed information of the activity of the CPU and GPUs and helps understanding the overall behavior and performance of application. Once a CUDA kernel is identified to be on the critical path and not meeting the performance expectations, right click on the kernel launch on timeline and select*Profile Kernel*from the context menu. A new[Start Activity](https://docs.nvidia.com/index.html#connection-dialog)opens up that is already preconfigured to profile the selected kernel launch. Proceed with optimizing the selected kernel using[Non-Interactive Profile Activity](https://docs.nvidia.com/index.html#quick-start-non-interactive)

## 4.3. Start Activity Dialog[#](https://docs.nvidia.com#start-activity-dialog)

Use the *Start Activity Dialog* to launch and attach to applications on your local and remote platforms. Start by selecting the *Target Platform* for profiling. By default (and if supported) your local platform will be selected. Select the platform on which you would like to start the target application or connect to a running process.

When using a remote platform, you will be asked to select or create a *Connection* in the top drop down. To create a new connection, select *+* and enter your connection details. When using the local platform, *localhost* will be selected as the default and no further connection settings are required. You can still create or select a remote connection, if profiling will be on a remote system of the same platform. Use the *Device Information* button to view system, GPU, and CUDA information for the selected device.

Depending on your target platform, select either *Launch* or *Remote Launch* to launch an application for profiling on the target. Note that *Remote Launch* will only be available if supported on the target platform.

Fill in the following launch details for the application:

**Application Executable:**Specifies the root application to launch. Note that this may not be the final application that you wish to profile. It can be a script or launcher that creates other processes.**Working Directory:**The directory in which the application will be launched.**Command Line Arguments:**Specify the arguments to pass to the application executable.**Environment:**The environment variables to set for the launched application.

Select *Attach* to attach the profiler to an application already running on the target platform. This application must have been started using another NVIDIA Nsight Compute CLI instance. The list will show all application processes running on the target system which can be attached. Select the refresh button to re-create this list.

Finally, select the *Activity* to be run on the target for the launched or attached application. Note that not all activities are necessarily compatible with all targets and connection options. Currently, the following activities exist:

### 4.3.1. Remote Connections[#](https://docs.nvidia.com#remote-connections)

Remote devices that support SSH can also be configured as a target in the *Start Activity Dialog*. To configure a remote device, ensure an SSH-capable *Target Platform* is selected, then press the *+* button. The following configuration dialog will be presented.

NVIDIA Nsight Compute supports both password and private key authentication methods. In this dialog, select the authentication method and enter the following information:

**Password****IP/Host Name:**The IP address or host name of the target device.**User Name:**The user name to be used for the SSH connection.**Password:**The user password to be used for the SSH connection.**Port:**The port to be used for the SSH connection. (The default value is 22)**Deployment Directory:**The directory to use on the target device to deploy supporting files. The specified user must have write permissions to this location.**Connection Name:**The name of the remote connection that will show up in the*Start Activity Dialog*. If not set, it will default to <User>@<Host>:<Port>.

**Private Key****IP/Host Name:**The IP address or host name of the target device.**User Name:**The user name to be used for the SSH connection.**SSH Private Key:**The private key that is used to authenticate to SSH server.**SSH Key Passphrase:**The passphrase for your private key.**Port:**The port to be used for the SSH connection. (The default value is 22)**Deployment Directory:**The directory to use on the target device to deploy supporting files. The specified user must have write permissions to this location.**Connection Name:**The name of the remote connection that will show up in the*Start Activity Dialog*. If not set, it will default to <User>@<Host>:<Port>.


In addition to keyfiles specified by path and plain password authentication, NVIDIA Nsight Compute supports keyboard-interactive authentication, standard keyfile path searching and SSH agents.

You can also specify placeholders in the *Deployment Directory* field. These placeholders will be replaced with the actual values when the connection is used. The following placeholders are supported.

Placeholder |
Description |
|---|---|
%C |
User cache directory. Resolves to $XDG_CACHE_HOME, if empty resolves to $HOME/.cache |
%E |
User config directory. Resolves to $XDG_CONFIG_HOME, if empty resolves to $HOME/.config |
%h |
User home directory. Resolves to $HOME, if empty resolves to /root |
%H |
Host name. Resolves to $HOSTNAME, if empty resolves to host |
%T |
Temporary directory. Resolves to $TMPDIR, if empty resolves to /tmp |
%u |
User name. Resolves to $USER, if empty resolves to root |
%S |
State directory. Resolves to $XDG_STATE_HOME, if empty resolves to $HOME/.local/state |

For example, if you specify the *Deployment Directory* as *%T/nsight-compute*, the actual directory used will be */tmp/nsight-compute* on the remote device.

When all information is entered, click the *Add* button to make use of this new connection.

When a remote connection is selected in the *Start Activity Dialog*, the *Application Executable* file browser will browse the remote file system using the configured SSH connection, allowing the user to select the target application on the remote device.

When an activity is launched on a remote device, the following steps are taken:

The command line profiler and supporting files are copied into the

*Deployment Directory*on the remote device. (Only files that do not exist or are out of date are copied.)Communication channels are opened to prepare for the traffic between the UI and the

*Application Executable*.For

*Interactive Profile*activities, a*SOCKS proxy*is started on the host machine.For

*Non-Interactive Profile*activities, a remote forwarding channel is opened on the target machine to tunnel profiling information back to the host.

The

*Application Executable*is executed on the remote device.For

*Interactive Profile*activities, a connection is established to the remote application and the profiling session begins.For

*Non-Interactive Profile*activities, the remote application is executed under the command line profiler and the specified report file is generated.

For non-interactive profiling activities, the generated report file is copied back to the host, and opened.


The progress of each of these steps is presented in the *Progress Log*.

Note that once either activity type has been launched remotely, the tools necessary for further profiling sessions can be found in the *Deployment Directory* on the remote device.

On Linux and Mac host platforms, NVIDIA Nsight Compute supports SSH remote profiling on target machines which are not directly addressable from the machine the UI is running on through the `ProxyJump`

and `ProxyCommand`

SSH options.

These options can be used to specify intermediate hosts to connect to or actual commands to run to obtain a socket connected to the SSH server on the target host and can be added to your SSH configuration file.

Note that for both options, NVIDIA Nsight Compute runs external commands and does not implement any mechanism to authenticate to the intermediate hosts using the credentials entered in the [Start Activity Dialog](https://docs.nvidia.com/index.html#connection-dialog). These credentials will only be used to authenticate to the final target in the chain of machines.

When using the `ProxyJump`

option NVIDIA Nsight Compute uses the *OpenSSH client* to establish the connection to the intermediate hosts. This means that in order to use `ProxyJump`

or `ProxyCommand`

, a version of OpenSSH supporting these options must be installed on the host machine.

A common way to authenticate to the intermediate hosts in this case is to use a *SSH agent* and have it hold the private keys used for authentication.

Since the *OpenSSH SSH client* is used, you can also use the *SSH askpass* mechanism to handle these authentications in an interactive manner.

It might happen on slow networks that connections used for remote profiling through SSH time out. If this is the case, the `ConnectTimeout`

option can be used to set the desired timeout value.

A known limitation of the remote profiling through SSH is that problems may arise if NVIDIA Nsight Compute tries to do remote profiling through *SSH* by connecting to the same machine it is running on. In this case, the workaround is to do local profiling through `localhost`

.

For more information about available options for the *OpenSSH client* and the ecosystem of tools it can be used with for authentication refer to the official [manual pages](https://www.openssh.com/manual.html).

### 4.3.2. Interactive Profile Activity[#](https://docs.nvidia.com#connection-activity-interactive)

The *Interactive Profile* activity allows you to initiate a session that controls the execution of the target application, similar to a debugger. You can step API calls and workloads (CUDA kernels), pause and resume, and interactively select the kernels of interest and which metrics to collect.

This activity does currently not support profiling or attaching to child processes.

**Enable CPU Call Stack**Collect the CPU-sided Call Stack at the location of each profiled kernel launch.

**CPU Call Stack Types**If “Enable CPU Call Stack” is set to “Yes”, the type(s) of call stack may be selected here.

**Enable NVTX Support**Collect NVTX information provided by the application or its libraries. Required to support stepping to specific NVTX contexts.

**Disable Profiling Start/Stop**Ignore calls to

`cu(da)ProfilerStart`

or`cu(da)ProfilerStop`

made by the application.**Enable Profiling From Start**Enables profiling from the application start. Disabling this is useful if the application calls

`cu(da)ProfilerStart`

and kernels before the first call to this API should not be profiled. Note that disabling this does not prevent you from manually profiling kernels.**Cache Control**Control the behavior of the GPU caches during profiling. Allowed values: For

*Flush All*, all GPU caches are flushed before each kernel replay iteration during profiling. While metric values in the execution environment of the application might be slightly different without invalidating the caches, this mode offers the most reproducible metric results across the replay passes and also across multiple runs of the target application.For

*Flush None*, no GPU caches are flushed during profiling. This can improve performance and better replicates the application behavior if only a single kernel replay pass is necessary for metric collection. However, some metric results will vary depending on prior GPU work, and between replay iterations. This can lead to inconsistent and out-of-bounds metric values.**Clock Control**Control the behavior of the GPU clocks during profiling. Allowed values: For

*Base*, GPC and memory clocks are locked to their respective base frequency during profiling. This has no impact on thermal throttling. For*Boost*, GPC and memory clocks are locked to their respective turbo boost frequency during profiling. If setting boost clock is not supported by the GPU or driver, falls back to locking clocks to ‘base’ if possible. For*Force-Boost*, GPC and memory clocks are locked to their respective turbo boost frequency during profiling. Supports Ampere+ on NVIDIA kernel mode driver 560 and Turing+ on driver 580 or newer. For*None*, no GPC or memory frequencies are changed during profiling.**Import Source**Enables permanently importing available source files into the report. Missing source files are searched in

[Source Lookup](https://docs.nvidia.com/index.html#options-source-lookup)folders. Source information must be embedded in the executable, e.g. via the`-lineinfo`

compiler option. Imported files are used in the*CUDA-C*view on the[Source Page](https://docs.nvidia.com/index.html#profiler-report-source-page).

**Graph Profiling**Set if CUDA graphs should be stepped and profiled as individual

*Nodes*or as complete*Graphs*. See the[Profiling Guide](https://docs.nvidia.com/ProfilingGuide/index.html#graph-profiling)for more information on this mode.

**Pipeline Boost State**Control the Tensor Core boost state. It is recommended to set the stable Tensor Core boosting for application profiling, ensuring predictive run-to-run performance. By default, the boost state is set to

`Auto`

, which attempts to set the stable boost state on supported platforms and drivers.

### 4.3.3. Profile Activity[#](https://docs.nvidia.com#profile-activity)

The *Profile* activity provides a traditional, pre-configurable profiler. After configuring which kernels to profile, which metrics to collect, etc, the application is run under the profiler without interactive control. The activity completes once the application terminates. For applications that normally do not terminate on their own, e.g. interactive user interfaces, you can cancel the activity once all expected kernels are profiled.

This activity does not support attaching to processes previously launched via NVIDIA Nsight Compute. These processes will be shown grayed out in the *Attach* tab.

**Output File**Path to report file where the collected profile should be stored. If not present, the report extension

`.ncu-repz`

is added automatically. The placeholder`%i`

is supported for the filename component. It is replaced by a sequentially increasing number to create a unique filename. This maps to the`--export`

command line option.**Force Overwrite**If set, existing report file are overwritten. This maps to the

`--force-overwrite`

command line option.**Target Processes**Select the processes you want to profile. In mode

*Application Only*, only the root application process is profiled. In mode*all*, the root application process and all its child processes are profiled. This maps to the`--target-processes`

command line option.**Replay Mode**Select the method for replaying kernel launches multiple times. In mode

*Kernel*, individual kernel launches are replayed transparently during the single execution of the target application. In mode*Application*, the entire target application is relaunched multiple times. In each iteration, additional data for the target kernel launches is collected. Application replay requires the program execution to be deterministic. This maps to the`--replay-mode`

command line option. See the[Profiling Guide](https://docs.nvidia.com/ProfilingGuide/index.html#kernel-replay)for more details on the replay modes.

**Graph Profiling**Set if CUDA graphs should be profiled as individual

*Nodes*or as complete*Graphs*.

**Additional Options**All remaining options map to their command line profiler equivalents. See the

[Command Line Options](https://docs.nvidia.com/NsightComputeCli/index.html#command-line-options)for details.

### 4.3.4. Reset[#](https://docs.nvidia.com#reset)

Entries in the connection dialog are saved as part of the current [project](https://docs.nvidia.com/index.html#projects). When working in a custom project, simply close the project to reset the dialog.

When not working in a custom project, entries are stored as part of the *default project*. You can delete all information from the default project by closing NVIDIA Nsight Compute and then [deleting the project file from disk](https://docs.nvidia.com/index.html#projects).

## 4.5. Nsight Copilot[#](https://docs.nvidia.com#nsight-copilot)

Nsight Copilot is an AI-powered chat assistant integrated into NVIDIA Nsight Compute. It can answer questions related to NVIDIA Nsight Compute, CUDA, and NVIDIA GPUs, and can provide explanations about profile results and performance optimizations.

Nsight Copilot is powered by Large Language Models (LLMs) and may not always provide accurate answers. Carefully evaluate the relevance of each answer to your specific problem.

### 4.5.1. Getting Started[#](https://docs.nvidia.com#getting-started)

#### Opening the Nsight Copilot Tool Window[#](https://docs.nvidia.com#opening-the-nsight-copilot-tool-window)

The Nsight Copilot tool window can be opened from several locations:

**Tools menu:**Select*Tools > Nsight Copilot…*from the main menu.**Keyboard shortcut:**Press*F9*.**Toolbar button:**Click the Nsight Copilot button in the report navigation toolbar.**Search bar:**Click the search bar and switch to*Nsight Copilot*mode (see[Search and Chat Bar](https://docs.nvidia.com/index.html#nsight-copilot-search-chat-bar)).**Copilot buttons:**Throughout the profiler report, Copilot buttons appear next to items that can be explained by Nsight Copilot. Clicking one opens the tool window and sends a pre-formulated query (see[Pre-formulated Report Queries](https://docs.nvidia.com/index.html#nsight-copilot-report-queries)).

#### Installation[#](https://docs.nvidia.com#installation)

If the Nsight Copilot package is not installed, an installation prompt is shown when the tool window is opened. The prompt reads “Nsight Copilot Package Not Installed” and provides an *Install* button.

Clicking *Install* opens the installation dialog:

Select the Nsight Copilot package from

*Version to Install*. The bundled version is included with the current Nsight Compute installation; previously downloaded updates appear as additional entries when available.Select a Python interpreter (Python 3.11 through 3.13 is required). A virtual environment will be created automatically.

Click

*Install*to begin the installation. Installation progress can be viewed in the expandable*Installation Progress*section, which also reports details of any errors that may occur.When installation completes successfully, click

*Finish*.

Note

The installation installs several Python packages into a virtual environment via pip. Key packages include: `grpcio`

, `langchain`

, `langchain-openai`

, `langchain-nvidia-ai-endpoints`

, `langgraph`

, `openai`

, `jinja2`

, `pyyaml`

, `requests`

, `tabulate`

, `tiktoken`

, and their dependencies. For a complete list of packages, inspect the installed virtual environment. Users install these packages at their own discretion.

#### Authentication[#](https://docs.nvidia.com#authentication)

Nsight Copilot requires authentication with an NVIDIA Developer account.

Click the

*Sign in*button or open the vertical ellipsis menu in the toolbar and select*Sign in*.Enter your NVIDIA Developer account credentials in the authentication page.

Once signed in, the vertical ellipsis menu shows your full email address at the top.


To sign out, open the vertical ellipsis menu and select *Sign out*. A confirmation dialog warns that all chats will be removed.

#### Configuration[#](https://docs.nvidia.com#configuration)

Nsight Copilot settings are available under *Tools > Options > Nsight Copilot*. They can also be opened from the vertical ellipsis menu in the Nsight Copilot tool window by selecting *Nsight Copilot Settings*.

Setting |
Description |
|---|---|
|
The currently installed Nsight Copilot package version. This value is read-only and shows “(not installed)” until the package has been installed. |
|
When enabled, Nsight Compute checks for Nsight Copilot updates on startup. |
|
Runs an immediate update check for Nsight Copilot. |
|
Reinstalls the Nsight Copilot version that ships with the current Nsight Compute installation. |
|
Deletes downloaded Nsight Copilot update artifacts from the local downloads folder. |

### 4.5.2. Chat Interface[#](https://docs.nvidia.com#chat-interface)

#### Sending Queries[#](https://docs.nvidia.com#sending-queries)

Enter your question in the input field at the bottom of the Copilot tool window. Press *Enter* or click the *Send* button to submit the query. You can also attach a profile result as context to your queries for context-aware responses (see [Context Attachment](https://docs.nvidia.com/index.html#nsight-copilot-context)).

While a response is being generated, it is streamed in real time. The *Send* button changes to a *Stop* button, which can be clicked to cancel the query. Cancelled queries and their partial responses are removed from the chat history; the language model will not be aware of them in subsequent queries.

Previous queries are available from a history dropdown in the input field. Click the input field to see autocomplete suggestions from earlier queries.

#### Search and Chat Bar[#](https://docs.nvidia.com#search-and-chat-bar)

When Nsight Copilot is available, the search bar can also be used to start a chat with Nsight Copilot.

Clicking the search bar opens a floating input widget with a mode selection popup. Two modes are available:

**Search:**Performs a universal search across Nsight Compute (documentation, metrics, options, etc.).**Nsight Copilot:**Sends the query to the Nsight Copilot chat.

You can switch modes by selecting a radio button in the popup, or by typing a command prefix:

`/search <query>`

— sends the query to universal search.`/chat <query>`

— sends the query to Nsight Copilot.

If no prefix is typed, the currently selected mode is used.

#### Pre-formulated Report Queries[#](https://docs.nvidia.com#pre-formulated-report-queries)

On the profiler report Details page, Copilot buttons appear next to section headers and rule entries. Clicking one of these buttons opens the Nsight Copilot tool window and sends a pre-formulated query to explain the selected item.

**Section button:**Asks Nsight Copilot to explain the section in detail.**Rule button:**Asks Nsight Copilot to explain the rule in detail.

The focused profile result is automatically attached as context to the query so that the response takes the specific profiling data into account.

#### Agent Transparency[#](https://docs.nvidia.com#agent-transparency)

During response generation, Nsight Copilot may show its processing steps in a collapsible “thinking” widget within the response. This allows you to follow the agent’s workflow.

Click the toggle to expand or collapse the processing steps. When collapsed, only the most recent step is shown.

#### References[#](https://docs.nvidia.com#references)

Responses may include references to source documents that were used to generate the answer. These appear in a collapsible *References* section below the response.

#### Response Actions[#](https://docs.nvidia.com#response-actions)

Each bot response provides a set of action buttons:

Button |
Description |
|---|---|
|
Re-runs the query to get a new response. |
|
Copies the response text to the clipboard. |
|
Rates the response as helpful. The query and response are sent to help improve Nsight Copilot. |
|
Rates the response as not helpful. The query and response are sent to help improve Nsight Copilot. |
|
Saves the current chat history to a file. |

Feedback is not available for cancelled responses.

#### Managing Chats[#](https://docs.nvidia.com#managing-chats)

Nsight Copilot supports multiple concurrent chat sessions. Each chat maintains its own conversation history and context.

**New Chat:**Click the*+*button to create a new chat session. Chats are named “Chat 1”, “Chat 2”, etc. by default.**Rename:**Click the chat name in the selector to edit it.**Switch:**Use the chat selector dropdown to switch between chats.**Delete:**Click the*paper-bin*button. A confirmation is required before the chat is removed.

### 4.5.3. Context Attachment[#](https://docs.nvidia.com#context-attachment)

Nsight Copilot can use profile results as context when answering queries. This enables context-aware responses that reference specific profiling data, metrics, and performance characteristics from your report.

#### Attaching Context[#](https://docs.nvidia.com#attaching-context)

To attach a profile result as context, click the *Attach Context* button below the input field. This selects a profile result from an open report and includes it in subsequent queries.

When context is attached, the selected context is displayed below the input field. The profile result filename is shown.

Context is also attached automatically when using the Copilot buttons on the Details page (see [Pre-formulated Report Queries](https://docs.nvidia.com/index.html#nsight-copilot-report-queries)).

#### Including and Excluding Context[#](https://docs.nvidia.com#including-and-excluding-context)

The eye icon next to the selected context toggles whether the context is included in queries:

**Included**(eye icon active): The context data is sent with each query.**Excluded**(eye icon inactive, text shown with strikethrough): The context is kept but not sent with queries.

This allows you to temporarily exclude context without detaching it entirely. This is helpful when asking general questions that are not related to your profile data.

### 4.5.4. Limitations[#](https://docs.nvidia.com#limitations)

The following limitations apply to the current version of Nsight Copilot:

**Report must be saved to disk:**A profile report must be saved to disk before it can be used as context for Nsight Copilot queries.**Source code requires import:**For source code information to be available in context, the profile must have been collected with the`--import-source yes`

option.**Data sent to the LLM:**Some extracted report data (such as metrics and section summaries) is sent to the language model for processing. The report file itself is not uploaded.

## 4.6. Tool Windows[#](https://docs.nvidia.com#tool-windows)

### 4.6.1. API Statistics[#](https://docs.nvidia.com#api-statistics)

The *API Statistics* window is available when NVIDIA Nsight Compute is connected to a target application. It opens by default as soon as the connection is established. It can be re-opened using *Debug > API Statistics* from the main menu.

Whenever the target application is suspended, it shows a summary of tracked API calls with some statistical information, such as the number of calls, their total, average, minimum and maximum duration. Note that this view cannot be used as a replacement for [Nsight Systems](https://developer.nvidia.com/nsight-systems) when trying to optimize CPU performance of your application.

The *Reset* button deletes all statistics collected to the current point and starts a new collection. Use the *Export to CSV* button to export the current statistics to a CSV file.

### 4.6.2. API Stream[#](https://docs.nvidia.com#api-stream)

The *API Stream* window is available when NVIDIA Nsight Compute is connected to a target application. It opens by default as soon as the connection is established. It can be re-opened using *Debug > API Stream* from the main menu.

Whenever the target application is suspended, the window shows the history of API calls and traced kernel launches. The currently suspended API call or kernel launch (activity) is marked with a yellow arrow. If the suspension is at a subcall, the parent call is marked with a green arrow. The API call or kernel is suspended before being executed.

For each activity, further information is shown such as the kernel name or the function parameters (*Func Parameters*) and return value (*Func Return*). Note that the function return value will only become available once you step out or over the API call.

Use the *Current Thread* dropdown to switch between the active threads. The dropdown shows the thread ID followed by the current API name. One of several options can be chosen in the trigger dropdown, which are executed by the adjacent *>>* button. *Run to Next Kernel* resumes execution until the next kernel launch is found in any enabled thread. *Run to Next API Call* resumes execution until the next API call matching *Next Trigger* is found in any enabled thread. *Run to Next Range Start* resumes execution until the next start of an active profiler range is found. Profiler ranges are defined by using the `cu(da)ProfilerStart/Stop`

API calls. *Run to Next Range Stop* resumes execution until the next stop of an active profiler range is found. The *API Level* dropdown changes which API levels are shown in the stream. The *Export to CSV* button exports the currently visible stream to a CSV file.

### 4.6.3. Baselines[#](https://docs.nvidia.com#baselines)

The *Baselines* tool window can be opened by clicking the *Baselines* entry in the *Profile* menu. It provides a centralized place from which to manage configured baselines. (Refer to [Baselines](https://docs.nvidia.com/index.html#baselines), for information on how to create baselines from profile results.)

The baseline visibility can be controlled by clicking on the check box in a table row. When the check box is checked, the baseline will be visible in the summary header as well as all graphs in all sections. When unchecked the baseline will be hidden and will not contribute to metric difference calculations.

The baseline color can be changed by double-clicking on the color swatch in the table row. The color dialog which is opened provides the ability to choose an arbitrary color as well as offers a palette of predefined colors associated with the stock baseline color rotation.

The baseline name can be changed by double-clicking on the *Name* column in the table row. The name must not be empty and must be less than the *Maximum Baseline Name Length* as specified in the options dialog.

The z-order of a selected baseline can be changed by clicking the *Move Baseline Up* and *Move Baseline Down* buttons in the tool bar. When a baseline is moved up or down its new position will be reflected in the report header as well as in each graph. Currently, only one baseline may be moved at a time.

The selected baselines may be removed by clicking on the *Clear Selected Baselines* button in the tool bar. All baselines can be removed at once by clicking on the *Clear All Baselines* button, from either the global tool bar or the tool window tool bar.

The configured baselines can be saved to a file by clicking on the *Save Baselines* button in the tool bar. By default baseline files use the `.ncu-bln`

extension. Baseline files can be opened locally and/or shared with other users.

Baseline information can be loaded by clicking on the *Load Baselines* button in the tool bar. When a baseline file is loaded, currently configured baselines will be replaced. A dialog will be presented to the user to confirm this operation when necessary.

Differences between the current result and the baselines can be visualized with graphical bars for metrics in Details page section headers. Use the *Difference Bars* drop down to select the visualization mode. Bars are extending from left to right and have a fixed maximum.

### 4.6.4. Metric Details[#](https://docs.nvidia.com#metric-details)

The *Metric Details* tool window can be opened using the *Metric Details* entry in the *Profile* menu or the respective tool bar button.
When a report and the tool window are open, a metric can be selected in the report to display additional information and its value for the current result in the tool window.
It also contains a search bar to look up metrics in the focused report’s current result.

Report metrics can be selected on the [Details Page](https://docs.nvidia.com/index.html#profiler-report-details-page) or on the [Raw Page](https://docs.nvidia.com/index.html#profiler-report-raw-page).
The window will show basic information (name, unit and raw value of the metric) as well as additional information, such as its extended description.
Note that all shown values are for the respective metric in the current result, even if a different result in e.g. the Raw Page is selected.

For results collected for [Green Contexts](https://docs.nvidia.com/ProfilingGuide/index.html#cuda-green-contexts) applications,
the *Metric Details* tool window also shows an additional row with the *Attribution* level of
the selected performance metric (e.g., Context or Green Context, if applicable).

The search bar can be used to open metrics in the focused report. It shows available matches as you type. The entered string must match from the start of the metric name.

By default, selecting or searching for a new metric updates the current *Default Tab*. You can click the pin button located in the upper-left corner of the tab control to create a copy of the default tab, unless the same metric is already pinned. This makes it possible to save multiple tabs and quickly switch between them to compare values.

Some metrics contain [Instance Values](https://docs.nvidia.com/ProfilingGuide/index.html#metrics-structure). When available, they are listed in the tool window. Instance values can have a *Correlation ID* that allows correlating the individual value with its associated entity, e.g. a function address or instruction name.

For metrics collected with [PM sampling](https://docs.nvidia.com/ProfilingGuide/index.html#pm-sampling), the correlation ID is the GPU timestamp in nanoseconds. It is shown relative to the first timestamp for this metric.
Note that the instance values for PM sampling metrics are currently not [context-switched](https://docs.nvidia.com/ProfilingGuide/index.html#context-switch-trace) , even if this is enabled in the corresponding timeline UI.

### 4.6.5. Launch Details[#](https://docs.nvidia.com#launch-details)

The *Launch Details* tool window can be opened using the *Launch Details* entry
in the *Profile* menu or the respective tool bar button. When a result
containing multiple sub-launches is selected and this tool window is open, it
will display information about each sub-launch contained in the result.

This tool window is split into two sections:

a header displaying information applying to the result as a whole

a body displaying information specific to the viewed sub-launch


#### Header[#](https://docs.nvidia.com#header)

On the left side of its header, this tool window displays the selected result’s name and the number of sub-launches it is comprised of.

The right side contains a combo box that allows selection of the sub-launch the body should represent. Each element of the combo box contains an index for the sub-launch as well as the name of the function that it launched if available.

#### Body[#](https://docs.nvidia.com#body)

The body of this tool window displays a table with sub-launch-specific metrics. This table has four columns:

*Metric Name*: the name of the metric*Metric Unit*: the unit for metric values*Instance Value*: the value of this metric for the selected sub-launch*Aggregate Value*: the aggregate value for this metric over all sub-launches in the selected result

### 4.6.6. Function Stats[#](https://docs.nvidia.com#function-stats)

The *Function Stats* tool window presents a hierarchical tree view of all functions in your profile result with top stalls for each function and source line.
This window is connected with the PM Sampling timeline and automatically updates to show data for the selected time range in the timeline.

#### Accessing Function Stats[#](https://docs.nvidia.com#accessing-function-stats)

- The Function Stats tool window can be opened using:
The

*Function Stats*entry in the*Profile*menu. See[Main Menu](https://docs.nvidia.com/index.html#main-menu)for details.The main tool bar button



#### Basic Workflow[#](https://docs.nvidia.com#basic-workflow)

Profile with PM Warp Sampling enabled (default: on).

Open the tool window using the

**Function Stats**tool bar button.Expand a function to see per-source-line statistics.

Sort by a column (default is sorted by

**All Samples**).Click a function or source line to navigate to it on the Source page (if available).


Note

The source view is not updated with the warp sampling data collected with PM sampling.

#### Understanding the Function Stats Tree[#](https://docs.nvidia.com#understanding-the-function-stats-tree)

The view displays a hierarchical tree with two levels:

**Function entries**(top-level): Each function appears as a parent row showing aggregate statistics across all source lines.**Source line entries**(children): Expand a function to see per-source-line breakdown in`filename:line`

format. Up to 10 source lines with the highest sample counts are shown. If a selection results in more than 10 source lines, the remaining ones are aggregated into an**Other**entry.

The columns include:

**Name**: The function name (for top-level entries) or source location in `filename:line`

format (for child entries). Click to navigate to the corresponding location on the Source page.

**Samples (All)**: Reports the samples collected for this entry as % of total samples collected. This also includes all the stall reasons as a stacked bar chart.

**Samples (Not Issued)**: Reports the samples collected for this entry as % of total samples collected where warps were not issued. This also includes all the stall reasons as a stacked bar chart.

**Top Stall #1**: Reports the stall reason with the highest incidence for the entry.

**Top Stall #2**: Reports the stall reason with the second highest incidence for the entry.

**Top Stall #3**: Reports the stall reason with the third highest incidence for the entry.

Note

By default, the tree is **sorted by All Samples in decreasing order**.
When there is only one function in the view, it is automatically expanded to show all source lines.

See the *Warp Stall Reasons* tables in the [Metrics Reference](https://docs.nvidia.com/ProfilingGuide/index.html#warp-stall-reasons) for a description of the individual warp scheduler states.

#### Data Source[#](https://docs.nvidia.com#data-source)

Collection is performed by PM Sampling with warp-state sampling enabled (

**default**).The shipped

`PmSampling.section`

file comes pre-configured with PM Sampling and Warp State Sampling metrics required to enable this window.At least one

**PM Sampling**metric is required with the attribute`PmWarpSampling`

declared (`Visible`

or`Hidden`

) to enable PM Warp Sampling data collection for this window. Use:`PmWarpSampling: Visible`

— show the metric with the timeline UI.`PmWarpSampling: Hidden`

— hide the metric in the timeline UI but still collected.

The feature is

**enabled by default**on all GPUs GA10X and newer. Disable globally with`--disable-pm-warp-sampling`

.Only

**one**PM Sampling pass with warp-state sampling is supported per profile session.**Note:**`warpsampling:`

metrics alone do**not**populate the per-function view; at least one**PM Sampling**metric with the attribute`PmWarpSampling`

must be present.

#### Metric Naming[#](https://docs.nvidia.com#metric-naming)

Warp Stall Sampling metrics are the **same underlying source counter metrics**; they are requested by prefixing the counter name with `warpsampling:`

to indicate collection via the PM Sampling path (**PM Warp Sampling**) and to render them on a timeline.
Example:
- `warpsampling:smsp__pcsamp_warps_issue_stalled_barrier`


In addition, a new group of **Warp Sampling** metrics that can be collected in this mode is available:
- group:smsp__pmwarpsamp_warp_stall_reasons

### 4.6.7. NVTX[#](https://docs.nvidia.com#nvtx)

The *NVTX* window is available when NVIDIA Nsight Compute is connected to a target application. If closed, it can be re-opened using *Debug > NVTX* from the main menu. Whenever the target application is suspended, the window shows the state of all active NVTX domains and ranges in the currently selected thread. Note that [NVTX](https://devblogs.nvidia.com/cuda-pro-tip-generate-custom-application-profile-timelines-nvtx/) information is only tracked if the launching command line profiler instance was started with `--nvtx`

or NVTX was enabled in the NVIDIA Nsight Compute launch dialog.

Use the *Current Thread* dropdown in the [API Stream](https://docs.nvidia.com/index.html#tool-window-api-stream) window to change the currently selected thread. NVIDIA Nsight Compute supports NVTX named resources, such as threads, CUDA devices, CUDA contexts, etc. If a resource is named using NVTX, the appropriate UI elements will be updated.

### 4.6.8. CPU Call Stack[#](https://docs.nvidia.com#cpu-call-stack)

The *CPU Call Stack* window is available when NVIDIA Nsight Compute is connected to a target application.
If closed, it can be re-opened using *Debug > CPU Call Stack* from the main menu.
Whenever the target application is suspended, the window shows all enabled CPU call stacks for the currently selected thread.

Use the *Call Stack Type* dropdown menu to switch between stack types in case multiple stack types were enabled (e.g., *Native*, *Python*).
Note that Python call stack collection requires CPython version 3.9 or later.

### 4.6.9. Resources[#](https://docs.nvidia.com#resources)

The *Resources* window is available when NVIDIA Nsight Compute is connected to a target application. It shows information about the currently known resources, such as CUDA devices, CUDA streams or kernels. The window is updated every time the target application is suspended. If closed, it can be re-opened using *Debug > Resources* from the main menu.

Using the dropdown on the top, different views can be selected, where each view is specific to one kind of resource (context, stream, kernel, …). The *Filter* edit allows you to create filter expressions using the column headers of the currently selected resource.

The resource table shows all information for each resource instance. Each instance has a unique ID, the *API Call ID* when this resource was created, its handle, associated handles, and further parameters. When a resource is destroyed, it is removed from its table.

#### Memory Allocations[#](https://docs.nvidia.com#memory-allocations)

When using the asynchronous malloc/free APIs, the resource view for *Memory Allocation* will also include the memory objects created in this manner. These memory objects have a non-zero memory pool handle. The *Mode* column will indicate which code path was taken during the allocation of the corresponding object. The modes are:

REUSE_STREAM_SUBPOOL: The memory object was allocated in memory that was previously freed. The memory was backed by the memory pool set as current for the stream on which the allocation was made.

USE_EXISTING_POOL_MEMORY: The memory object was allocated in memory that was previously freed. The memory is backed by the default memory pool of the stream on which the allocation was made.

REUSE_EVENT_DEPENDENCIES: The memory object was allocated in memory that was previously freed in another stream of the same context. A stream ordering dependency of the allocating stream on the free action existed. Cuda events and null stream interactions can create the required stream ordered dependencies.

REUSE_OPPORTUNISTIC: The memory object was allocated in memory that was previously freed in another stream of the same context. However, no dependency between the free and allocation existed. This mode requires that the free be already committed at the time the allocation is requested. Changes in execution behavior might result in different modes for multiple runs of the application.

REUSE_INTERNAL_DEPENDENCIES: The memory object was allocated in memory that was previously freed in another stream of the same context. New internal stream dependencies may have been added in order to establish the stream ordering required to reuse a piece of memory previously released.

REQUEST_NEW_ALLOCATION: New memory had to be allocated for this memory object as no viable reusable pool memory was found. The allocation performance is comparable to using the non-asynchronous malloc/free APIs.


#### Graphviz DOT and SVG exports[#](https://docs.nvidia.com#graphviz-dot-and-svg-exports)

Some of the shown *Resources* can also be exported to *GraphViz DOT* or SVG* files using the `Export to GraphViz`

or `Export to SVG`

buttons.

When exporting *OptiX traversable handles*, the traversable graph node types will be encoded using shapes and colors as described in the following table.

Node Type |
Shape |
Color |
|---|---|---|
IAS |
Hexagon |
#8DD3C7 |
Triangle GAS |
Box |
#FFFFB3 |
AABB GAS |
Box |
#FCCDE5 |
Curve GAS |
Box |
#CCEBC5 |
Sphere GAS |
Box |
#BEBADA |
Static Transform |
Diamond |
#FB8072 |
SRT Transform |
Diamond |
#FDB462 |
Matrix Motion Transform |
Diamond |
#80B1D3 |
Error |
Paralellogram |
#D9D9D9 |

### 4.6.10. CUDA Graph Viewer[#](https://docs.nvidia.com#cuda-graph-viewer)

The *CUDA Graph Viewer* tool window provides real-time visualization and inspection of CUDA Graphs.
Access it through the *CUDA Graph Viewer* entry in the *Profile* menu or via the toolbar button.
By default, the viewer opens automatically upon graph creation. To disable this behavior, navigate
to *Tools > Options > Profile > CUDA Graph Viewer > Auto-Open Graph Viewer* and set it to *No*.

The window provides two tabs:

**Source Graph**: Displays the original graph structure as defined in the application source code before instantiation.**Instantiated Graph**: Shows the graph as it exists after instantiation and optimization by the CUDA runtime. This view may differ from the source graph due to runtime optimizations, node merging, or dependency resolution.

Use the dropdown menu to select which graph to view when multiple graphs are active. Toggle node
and edge labels with the *Show/Hide Labels* button, and hover over nodes, edges, or the canvas to
view detailed tooltips. The graph layouts use hierarchical layout algorithms optimized for
readability and may differ from those generated by `cudaGraphDebugDotPrint`

or exported
as [DOT or SVG](https://docs.nvidia.com/index.html#graphviz-dot-and-svg-exports) from the *Resources* window.

A legend overlay is available via the legend icon, showing node shapes, edge styles, group borders, and color meanings. Hover over the icon to view it, or click the pin button to keep it open.

**Interactive Profiling**

When profiling CUDA Graph workloads in an interactive session, the viewer automatically opens and displays graphs as the target application creates them. As nodes are added through CUDA API calls, the viewer updates in real-time to highlight newly created nodes. When an instantiated graph is launched, the viewer tracks execution state — highlighting nodes currently being executed and visually distinguishing completed nodes from pending ones. Execution flow through conditional and child graph nodes is clearly indicated.

**Profile Report Analysis**

When opening a profile report containing CUDA Graph data, the viewer automatically displays the
associated graphs. Selecting a *Kernel* or *Graph* result in the
[Summary Page](https://docs.nvidia.com/index.html#profiler-report-summary-page) or
[Raw Page](https://docs.nvidia.com/index.html#profiler-report-raw-page) highlights the corresponding graph node.

In the *Instantiated Graph* tab, you can also click on a kernel node to navigate to its profiled
result in the report, or double-click to open the *Details* page directly. Clickable nodes display
a pointing-hand cursor. If the clicked node does not have an associated profiled result (for
example, non-kernel nodes or kernels that were skipped during profiling), an info banner is
displayed. Nodes in the *Source Graph* tab are not clickable.

### 4.6.11. Device Information[#](https://docs.nvidia.com#device-information)

The *Device Information* tool window displays system, GPU, and CUDA information for the selected device connection. Access it through the *Device Information* button (info icon) in the [Start Activity Dialog](https://docs.nvidia.com/index.html#connection-dialog) or via *Connection > Device Information* from the main menu.

The window provides three tabs for viewing device details:

**System**Displays operating system information including OS name, CPU architecture, hostname, IP addresses, and collection timestamp.

**GPU**Shows GPU-related information including driver version, CUDA version, and detailed properties for each detected GPU.

**CUDA**Shows CUDA device attributes for each detected GPU, queried from the CUDA driver. The attributes are grouped into sections covering compute capability and SM count, memory, thread and block limits, registers and shared memory, compute feature support, and other device properties.


Use the connection dropdown at the top to select a different device. Information is automatically collected when you select a device. Use the refresh button to manually update the information for the currently selected device.

The Device Information window supports both local and remote device connections. For remote devices, the system automatically deploys a collector binary via SSH and retrieves the information. Remote Windows targets are not supported.

### 4.6.12. Search[#](https://docs.nvidia.com#search)

The *Search* tool window can be opened using the *Search* entry in the *Tools* menu, or from the tool bar’s search bar.
It can be used to search for terms throughout Nsight Compute.

Your queries can also be searched in the online developer forums, providing you with additional information and help.

Enter your query into the tool menu’s or window’s search bar and press *Enter* or use the *Start search* button.
Available sources are checked for matches in the background and results are displayed in the tool window’s table.
While a search is running, you can press the *Cancel search* button to stop it.
Previous searches are available from a history dropdown that is shown when clicking the tool window’s search bar with the mouse.
Select a history entry to replace the current search bar content with it.

Each result is associated with the original source. While some results are plain text, others are links that can be clicked to jump to the location and see them in context. Below is a (non-comprehensive) list of supported sources. The list of available sources may be extended in the future.

Local

**Documentation****Knowledgebase**entries**Metrics**in the focused reportNsight Compute UI

**Options**Loaded

**Sections**Online

**Developer Forums**entries

### 4.6.13. Metric Selection[#](https://docs.nvidia.com#metric-selection)

The *Metric Selection* window can be opened from the main menu using *Profile > Metric Selection*. It tracks all metric sets, sections and rules currently loaded in NVIDIA Nsight Compute, independent from a specific connection or report. The directory to load those files from can be configured in the [Profile](https://docs.nvidia.com/index.html#options-profile) options dialog. It is used to inspect available sets, sections and rules, as well as to configure which should be collected, and which rules should be applied. You can also specify a comma separated list of individual metrics, that should be collected. The window has two views, which can be selected using the dropdown in its header.

The **Metric Sets** view shows all available metric sets. Each set is associated with a number of metrics sections. You can choose a set appropriate to the level of detail for which you want to collect performance metrics. Sets which collect more detailed information normally incur higher runtime overhead during profiling.

When enabling a set in this view, the associated metric sections are enabled in the *Metric Sections/Rules* view. When disabling a set in this view, the associated sections in the *Metric Sections/Rules* view are disabled. If no set is enabled, or if sections are manually enabled/disabled in the *Metric Sections/Rules* view, the <*custom*> entry is marked active to represent that no section set is currently enabled. Note that the *basic* set is enabled by default.

Whenever a kernel is profiled manually, or when auto-profiling is enabled, only sections enabled in the **Metric Sections/Rules** view and individual metrics specified in input box are collected. Similarly, whenever rules are applied, only rules enabled in this view are active.

The enabled states of sections and rules are persisted across NVIDIA Nsight Compute launches. The *Reload* button reloads all sections and rules from disk again. If a new section or rule is found, it will be enabled if possible. If any errors occur while loading a rule, they will be listed in an extra entry with a warning icon and a description of the error.

Use the *Enable All* and *Disable All* checkboxes to enable or disable all sections and rules at once. The Filter text box can be used to filter what is currently shown in the view. It does not alter activation of any entry.

The table shows sections and rules with their activation status, their relationship and further parameters, such as associated metrics or the original file on disk. Rules associated with a section are shown as children of their section entry. Rules independent of any section are shown under an additional *Independent Rules* entry.

Clicking an entry in the table’s *Filename* column opens this file as a document. It can be edited and saved (ctrl + s) directly in NVIDIA Nsight Compute. After editing the file, *Reload* must be selected to apply those changes. Document also supports text search (ctrl + f), zoom in (ctrl + mouse scroll down), zoom out (ctrl + mouse scroll up) functionalities.

When a section or rule file is modified, the entry in the *State* column will show *User Modified* to reflect that it has been modified from its default state. When a *User Modified* row is selected, the *Restore* button will be enabled. Clicking the Restore button will restore the entry to its default state and automatically *Reload* the sections and rules.

Similarly, when a stock section or rule file is removed from the configured *Sections Directory* (specified in the [Profile](https://docs.nvidia.com/index.html#options-profile) options dialog), the *State* column will show *User Deleted*. *User Deleted* files can also be restored using the *Restore* button.

Section and rule files that are created by the user (and not shipped with NVIDIA Nsight Compute) will show up as *User Created* in the *state column*.

See the [Sections and Rules](https://docs.nvidia.com/ProfilingGuide/index.html#sections-and-rules) for the list of default sections for NVIDIA Nsight Compute.

### 4.6.14. Nsight Copilot[#](https://docs.nvidia.com#tool-window-nsight-copilot)

The *Nsight Copilot* tool window provides an AI-powered chat assistant for questions about NVIDIA Nsight Compute, CUDA, NVIDIA GPUs, and profile results. It can be opened via the *Tools* menu, the *F9* keyboard shortcut, or the toolbar. For details, see [Nsight Copilot](https://docs.nvidia.com/index.html#nsight-copilot).

## 4.7. Profiler Report[#](https://docs.nvidia.com#profiler-report)

The profiler report contains all the information collected during profiling for each kernel launch. In the user interface, it consists of a header with general information, as well as controls to switch between report pages or individual collected launches.

### 4.7.1. Header[#](https://docs.nvidia.com#profiler-report-header)

The top of the report shows a table with information about the selected profile result (as *Current*) and potentially additional [baselines](https://docs.nvidia.com/index.html#tool-window-baselines).
For many values in this table, tooltips provide additional information or data, e.g., the tooltip of the column *Attributes* provides additional information about the context type and resources used for the launch.

The *Result* dropdown can be used to switch between all collected kernel launches. The information displayed in each page commonly represents the selected launch instance. On some pages (e.g. *Raw*), information for all launches is shown and the selected instance is highlighted. You can type in this dropdown to quickly filter and find a kernel launch.

The *Apply Filters* button opens the filter dialog. You can use more than one filter to narrow down your results. On the filter dialog, enter your filter parameters and press OK button. The *Launch* dropdown, [Summary Page](https://docs.nvidia.com/index.html#profiler-report-summary-page) table, and [Raw Page](https://docs.nvidia.com/index.html#profiler-report-raw-page) table will be filtered accordingly. Select the arrow dropdown to access the *Clear Filters* button, which removes all filters.

Underneath the current and baseline results are the tabs for switching between the report pages. The pages themselves are explained in detail in the [next section](https://docs.nvidia.com/index.html#profiler-report-pages).

Each group button to the right of the page tabs opens a context menu that features related actions. Some actions may be enabled only when the related report page is selected.

Compare

**Add Baseline**promotes the current result in focus to become the baseline of all other results from this report and any other report opened in the same instance of NVIDIA Nsight Compute.**Clear Baselines**removes all currently active baselines. You may also use the[Baselines](https://docs.nvidia.com/index.html#tool-window-baselines)tool window to manage baseline for comparison.**Source Comparison**navigates to the[Source Comparison](https://docs.nvidia.com/index.html#source-comparison)document in case at least two profile results are available for comparison.

Tools

**Occupancy Calculator**opens the[Occupancy Calculator](https://docs.nvidia.com/index.html#occupancy-calculator)in a new document.**Metric Details Windows**opens the[Metric Details](https://docs.nvidia.com/index.html#tool-window-metric-details)tool window. When the window is open and a metric is selected elsewhere in the report, it shows detailed information about it.**Launch Details Windows**opens the[Launch Details](https://docs.nvidia.com/index.html#tool-window-launch-details)tool window. When the window is open and a result containing multiple sub-launches is selected, it displays information about each sub-launch in the result.**CUDA Graph Viewer**opens the[CUDA Graph Viewer](https://docs.nvidia.com/index.html#tool-window-cuda-graph-viewer)tool window. When the window is open and a result containing a CUDA Graph is selected, it displays the graph in the viewer.

View

**Show/Hide Rules Output**toggles the visibility of rule results.**Show/Hide Section Descriptions**toggles the visibility of section descriptions on the Details and Session pages.**Show/Hide Green Context Markers**toggles the visibility of markers for*attributable*Green Context metrics.`**Expand Sections**expands all sections to show their body contents, not only header and rule output. Note that sections may have multiple bodies and the visible one can be chosen using the dropdown in the section header.**Collapse Sections**collapses all sections to show only their header and rule output.

Export

**Copy as Image**- Copies the contents of the page to the clipboard as an image.**Save as Image**- Saves the contents of the page to a file as an image.**Save as PDF**- Saves the contents of the page to a file as a PDF.**Export to CSV**- Exports the contents of the page to CSV format.

More (three bars icon)

**Apply Rules**applies all rules available for this report. If rules had been applied previously, those results will be replaced. By default, rules are applied immediately once the kernel launch has been profiled. This can be changed in the options under*Tools > Options > Profile > Report UI > Apply Applicable Rules Automatically*.**Reset to Default**resets the page to a default state by removing any persisted settings.


### 4.7.2. Report Pages[#](https://docs.nvidia.com#report-pages)

Use the *Page* dropdown in the header to switch between the report pages.

By default, when opening a report with a single profile result, the [Details Page](https://docs.nvidia.com/index.html#profiler-report-details-page) is shown. When opening a report with multiple results, the [Summary Page](https://docs.nvidia.com/index.html#profiler-report-summary-page) is selected instead. You can change the default report page in the [Profile](https://docs.nvidia.com/index.html#options-profile) options.

#### Summary Page[#](https://docs.nvidia.com#summary-page)

The *Summary* page shows a table of all collected results in the report, as well as a list of the most important rule outputs (*Prioritized Rules*) which are ordered by the estimated speedup that could potential be obtained by following their guidance. *Prioritized Rules* are shown by default and can be toggled with the [R] button on the upper right of the page.

The *Summary Table* gives you a quick comparison overview across all profiled workloads. It contains a number of important, pre-selected metrics which can be customized as explained below. Its columns can be sorted by clicking the column header. You can transpose the table with the *Transpose* button. Aggregate of all results per each counter metric is shown in the table header along with the column name. You can change the aggregated values by selecting the desired results for multiple metrics simultaneously. When selecting any entry by single-click, a list of its *Prioritized Rules* will be shown below the table. Double-click any entry to make the result the currently active one and switch to the [Details Page](https://docs.nvidia.com/index.html#profiler-report-details-page) page to inspect its performance data.
By default, kernel demangled names are simplified, renamed and shown in an optimized manner. This behavior can be changed with [Rename Demangled Names](https://docs.nvidia.com/index.html#options-profile) option. If an auto-simplified name is not useful, you can rename it through a configuration file.
You can also persist the updated names directly in the report by double-clicking on the name, renaming and saving the report.
Use [Rename Kernels Config Path](https://docs.nvidia.com/index.html#options-profile) option to specify the configuration file which should be used while importing renamed kernels or exporting demangled names with mappings to rename them. To export names to a new file, click *Export* button and use *Rename Kernels Config* option.
Hovering over a demangled name cell shows the full name in a tooltip and lets you open the kernel renaming config file from there.
See [Kernel Renaming](https://docs.nvidia.com/NsightComputeCli/index.html#kernel-renaming) for more details on configuration file usage.
For results associated with CUDA Graphs, clicking on the result opens the [CUDA Graph Viewer](https://docs.nvidia.com/index.html#tool-window-cuda-graph-viewer) tool window. The viewer displays the instantiated graph structure and automatically highlights the graph node from which the selected kernel was launched, making it easy to understand the execution context within the graph topology.

You can configure the list of metrics included in this table in the [Profile](https://docs.nvidia.com/index.html#options-profile) options dialog. If a metric has multiple instance values, the number of instances is shown after its standard value. A metric with ten instance values could for example look like this: `35.48 {10}`

. In the [Profile](https://docs.nvidia.com/index.html#options-profile) options dialog, you can select that all instance values should be shown individually. You can also inspect the instances values of a metric result in the [Metric Details](https://docs.nvidia.com/index.html#tool-window-metric-details) tool window.

In addition to metrics, you can also configure the table to include any of the following properties:

##### Properties[#](https://docs.nvidia.com#properties)


[#]

`property__api_call_id`

ID of the API call associated with this profile result.


`property__block_size`

Block Size. If the result contains multiple launches, this will contain the maximum value for each dimension of the block.


`property__creation_time`

Local collection time.


`property__demangled_name`

Kernel demangled name, potentially renamed.


`property__device_name`

GPU device name.


`property__estimated_speedup`

Maximal relative speedup achievable for this profile result as estimated by the guided analysis rules.


`property__function_name`

Kernel function name.


`property__grid_dimensions`

Grid Dimensions. If the result contains multiple launches, this will contain the maximum value for each dimension of the grid.


`property__grid_offset`

Grid Offset.


`property__grid_size`

Grid Size. If the result contains multiple launches, this will contain the maximum value for each dimension of the grid.


`property__issues_detected`

Number of issues detected by guided analysis rules for this profile result.


`property__kernel_id`

Kernel ID.


`property__mangled_name`

Kernel mangled name.


`property__original_demangled_name`

Original kernel demangled name without any renaming.


`property__process_name`

Process name.


`property__range_name`

Range name.


`property__result_type`

Result Type. This property shows workload type and execution model of the profile result.


`property__runtime_improvement`

Runtime improvement corresponding to the estimated speedup.


`property__series_id`

ID of the profile series.


`property__series_parameters`

Profile series parameters.


`property__thread_id`

CPU thread ID.


For [Range Replay](https://docs.nvidia.com/ProfilingGuide/index.html#range-replay) reports, a smaller set of columns is shown by default, as not all apply to such results.

For the currently selected metric result the *Prioritized Rules* show the most impactful rule results with respect to the estimated potential speedup. Clicking on any of the rule names on the left allows you to easily navigate to the containing section on the details page. With the downward-facing arrow on the right a table with the relevant *key performance indicators* can be toggled. This table contains the metrics which should be tracked when optimizing performance according to the rule guidance.

#### Details Page[#](https://docs.nvidia.com#details-page)

##### Overview[#](https://docs.nvidia.com#id7)

The *Details* page is the main page for all metric data collected during a kernel launch. The page is split into individual sections.
Each section consists of a header table and an optional body that can be expanded. You can expand or collapse the body of each section by clicking on its respective header.
The sections are completely user defined and can be changed easily by updating their respective files.
For more information on customizing sections, see the [Customization Guide](https://docs.nvidia.com/CustomizationGuide/index.html#abstract).
For a list of sections shipped with NVIDIA Nsight Compute, see [Sections and Rules](https://docs.nvidia.com/ProfilingGuide/index.html#sections-and-rules).

By default, once a new profile result is collected, all applicable rules are applied. Any rule results will be shown as *Recommendations* on this page. Most rule results will contain an optimization advice along with an estimate of the improvement that could be achieved when successfully implementing this advice. Other rule results will be purely informative or have a warning icon to indicate a problem that occurred during execution (e.g., an optional metric that could not be collected). Results with error icons typically indicate an error while applying the rule.

Estimates of potential improvement are shown below the rule result’s name and exist in two types. *Global estimates* (“Est. Speedup”) are an approximation of the decrease in workload runtime, whereas *local estimates* (“Est. Local Speedup”) are an approximation of the increase in efficiency of the hardware utilization of the particular performance problem the rule addresses.

If a rule result references another report section, it will appear as a link in the recommendation. Select the link to scroll to the respective section. If the section was not collected in the same profile result, enable it in the [Metric Selection](https://docs.nvidia.com/index.html#tool-window-sections-info) tool window.

You can add or edit comments in each section of the *Details* view by clicking on the comment button (speech bubble). The comment icon will be highlighted in sections that contain a comment. Comments are persisted in the report and are summarized in the [Comments Page](https://docs.nvidia.com/index.html#profiler-report-comments-page).

Besides their header, sections typically have one or more *bodies* with additional charts or tables. Click the triangle *Expander* icon in the top-left corner of each section to show or hide those. If a section has multiple bodies, a dropdown in their top-right corner allows you to switch between them.

##### Memory[#](https://docs.nvidia.com#memory)

If enabled, the *Memory Workload Analysis* section contains a Memory chart that visualizes data transfers, cache hit rates, instructions and memory requests. More information on how to use and read this chart can be found in the [Profiling Guide](https://docs.nvidia.com/ProfilingGuide/index.html#memory-chart).

##### Occupancy[#](https://docs.nvidia.com#occupancy)

You can open the [Occupancy Calculator](https://docs.nvidia.com/index.html#occupancy-calculator) by clicking on the calculator button in the report header or in the header of the *Occupancy Section*.

##### Range Replay[#](https://docs.nvidia.com#range-replay)

Note that for [Range Replay](https://docs.nvidia.com/ProfilingGuide/index.html#range-replay) results some UI elements, analysis rules, metrics or section body items such as charts or tables might not be available, as they only apply to kernel launch-based results. The filters can be checked in the corresponding section files.

##### Rooflines[#](https://docs.nvidia.com#rooflines)

If enabled, the *GPU Speed Of Light Roofline Chart* section contains a Roofline chart that is particularly helpful for visualizing kernel performance at a glance. (To enable roofline charts in the report, ensure that the section is enabled when profiling.) More information on how to use and read this chart can be found in [Roofline Charts](https://docs.nvidia.com/ProfilingGuide/index.html#roofline-charts). NVIDIA Nsight Compute ships with several different definitions for roofline charts, including hierarchical rooflines. These additional rooflines are defined in different section files. While not part of the *full* section set, a new section set called *roofline* was added to collect and show all rooflines in one report. The idea of hierarchical rooflines is that they define multiple ceilings that represent the limiters of a hardware hierarchy. For example, a hierarchical roofline focusing on the memory hierarchy could have ceilings for the throughputs of the L1 cache, L2 cache and device memory. If the achieved performance of a kernel is limited by one of the ceilings of a hierarchical roofline, it can indicate that the corresponding unit of the hierarchy is a potential bottleneck.

The roofline chart can be zoomed and panned for more effective data analysis, using the controls in the table below.
When the [Metric Details](https://docs.nvidia.com/index.html#tool-window-metric-details) tool window is open, you can click on an achieved value in the chart to see its metric formula in the tool window.

Zoom In |
Zoom Out |
Zoom Reset |
Pan |
|---|---|---|---|
|
|
|
|

##### Source[#](https://docs.nvidia.com#source)

Sections such as *Source Counters* can contain source hot spot tables. These tables indicate the N highest or lowest values of one or more metrics in your kernel source code. Select the location links to navigate directly to this location in the [Source Page](https://docs.nvidia.com/index.html#profiler-report-source-page). Hover the mouse over a value to see which metrics contribute to it.

##### Timelines[#](https://docs.nvidia.com#timelines)

When collecting metrics with [PM sampling](https://docs.nvidia.com/ProfilingGuide/index.html#pm-sampling), they can be viewed in a *timeline*. The timeline shows metrics selected in the respective section file or on the command line with their labels/names and their values over time.

Different metrics may be collected in different passes (replays) of the workload, as only a limited number of them can be sampled in the same pass. Context switch trace is used to filter the collected data to only include samples from the profiled contexts and to align it in the timeline.

You can hover the mouse over a metric row label to see further information on the metrics in the row. Hovering over a sample on the timeline shows the metric values at that timestamp within the current row. With the [Metric Details](https://docs.nvidia.com/index.html#tool-window-metric-details) tool window open, click to select a value on the timeline and show the metric and all its raw timestamps (absolute and relative) correlated values in the tool window.

You can also use the [Metric Details](https://docs.nvidia.com/index.html#tool-window-metric-details) tool window to inspect profiler metrics generated during PM sampling. These provide information about the used sampling intervals, buffer sizes, dropped samples and other properties for each collection pass. A detailed list can be found in the [metrics reference](https://docs.nvidia.com/ProfilingGuide/index.html#metrics-reference).

The timeline has a context menu for further actions regarding copying, zooming or adjusting the viewed data:


Metric rows on the timeline can be scaled (y-axis) based on a theoretical HW peak, or based on the maximum profiled value in the workload. Select the

Scale to Peak/Scale to Max Valueoptions in the context menu to switch between the two modes. Note that HW peak info may not be available for all rows.When zoomed out, the bar height may be reduced to represent that multiple samples are aggregated into one bar. The

Show/Hide Max Barsoptions in the context menu can be used to enable/disable showing the maximum value for each time range across all samples in that range, even when zoomed out.In addition, the

Enable/Disable Context Switch Filteroption can be used to enable or disable the filtering of the timeline data with[context switch]information, if it is available. When the context switch filter is enabled (the default), samples from each pass group are only shown for the active contexts. When the context switch filter is disabled, the raw collected sampling data is shown along with a separate row for each pass group’s context switch trace.When the context menu option is not available, the report does not include context switch trace data. In this case, the option

Enable/Disable Workload Alignmentis shown instead if workload execution trace is available. When enabled, it aligns all passes based on their first workload execution timestamp.

The timeline row Workload Execution shows each kernel’s start and end timestamp. When the context switch filter is enabled, kernel execution is only shown for one of the passes for the active contexts. When the context switch filter is disabled, kernel execution is shown for all the passes.

#### Source Page[#](https://docs.nvidia.com#source-page)

The *Source* page correlates assembly (SASS) with high-level code such as CUDA-C, Python or PTX. In addition, it displays instruction-correlated metrics to help pinpoint performance problems in your code.

The page can be switched between different *Views* to focus on a specific source layer or see two layers side-by-side. This includes SASS, PTX and Source (CUDA-C, Fortran, Python, …), as well as their combinations. Which options are available depends on the source information embedded into the executable.

The high-level Source (CUDA-C) view is available if the application was built with the `-lineinfo`

or `--generate-line-info`

nvcc flag to correlate SASS and source. When using separate linking at the ELF level, there is no PTX available in the ELF that would correspond to the final SASS. As such, NVIDIA Nsight Compute does not show any PTX even though it would be available statically in the executable and could be shown with `cuobjdump -all -lptx`

. However, this is a pre-linked version of the PTX and cannot be reliably used for correlation.

##### Metrics[#](https://docs.nvidia.com#metrics)

###### Metrics Correlation[#](https://docs.nvidia.com#metrics-correlation)

The page is most useful when inspecting performance information and metrics correlated with your code. Metrics are shown in columns, which can be enabled or disabled using the *Column Chooser* accessible using the column header right click menu.

To not move out of view when scrolling horizontally, columns can be fixed. By default, the *Source* column is fixed to the left, enabling easy inspection of all metrics correlated to a source line. To change fixing of columns, right click the column header and select *Freeze* or *Unfreeze*, respectively.

The heatmap on the right-hand side of each view can be used to quickly identify locations with high metric values of the currently selected metric in the dropdown. The heatmap uses a black-body radiation color scale where black denotes the lowest mapped value and white the highest, respectively. The current scale is shown when clicking and holding the heatmap with the right mouse button.

By default, applicable metrics are shown as percentage values relative to their sum across the launch. A bar is filling from left to right to indicate the value at a specific source location relative to this metric’s maximum within the launch. The [%] and [+-] buttons can be used to switch the display from relative to absolute and from abbreviated absolute to full-precision absolute, respectively. For relative values and bars, the [circle/pie] button can be used to switch the display between relative to global (launch) and relative to local (function/file) scope. This button is disabled when the view is collapsed, as percentages are always relative to the global launch scope in this case.

###### Pre-Defined Source Metrics[#](https://docs.nvidia.com#pre-defined-source-metrics)

**Metric Pipelines**The

[metric pipelines](https://docs.nvidia.com/ProfilingGuide/index.html#pipelines)this instruction (can) execute in. Some instructions can execute in one of multiple pipelines, and the decision is dynamic at runtime. Some instructions execute in both of two pipelines, and the association is static. Other instructions execute in only a single pipeline.**Scoreboard Dependencies**See

[Instructions & Scoreboards Table](https://docs.nvidia.com/NsightCompute/index.html#profiler-report-source-page-additional-tables)for information on the scoreboard dependencies.**Live Registers**Number of registers that need to be kept valid by the compiler. A high value indicates that many registers are required at this code location, potentially increasing the register pressure and the maximum number of register required by the kernel.

The total number of registers reported as

`launch__registers_per_thread`

may be significantly higher than the maximum live registers. The compiler may need to allocate specific registers that can creates holes in the allocation, thereby affecting`launch__registers_per_thread`

, even if the maximum live registers is smaller. This may happen due to ABI restrictions, or restrictions enforced by particular hardware instructions. The compiler may not have a complete picture of which registers may be used in either callee or caller and has to obey ABI conventions, thereby allocating different registers even if some register could have theoretically been re-used.**Attributed Stalls**Number of warp stall samples of type long/short scoreboard not issued, attributed to this scoreboard producer location.

Use this to identify source locations that cause the most stalls. The stalls are attributed to the producer location, which is the location of the line that produced the scoreboard. This may not be the same as the location of the instruction that is stalled, as it may be waiting on a scoreboard produced by another line.

**Instruction Mix/Category**Instruction Mix (high-level source) or Instruction Category (SASS) show the breakdown of, or the instruction category, respectively, for each line.

**Warp Stall Sampling (All Samples)**[[1]](https://docs.nvidia.com#fn1)The number of samples from the

[Statistical Sampler](https://docs.nvidia.com/ProfilingGuide/index.html#statistical-sampler)at this program location.**Warp Stall Sampling (Not-issued Samples)**[[2]](https://docs.nvidia.com#fn2)The number of samples from the

[Statistical Sampler](https://docs.nvidia.com/ProfilingGuide/index.html#statistical-sampler)at this program location on cycles the warp scheduler issued no instructions. Note that*(Not Issued)*samples may be taken on a different profiling pass than*(All)*samples mentioned above, so their values do not strictly correlate.This metric is only available on devices with compute capability 7.0 or higher.

**Instructions Executed**Number of times the source (instruction) was executed per individual warp, independent of the number of participating threads within each warp.

**Thread Instructions Executed**Number of times the source (instruction) was executed by any thread, regardless of predicate presence or evaluation.

**Predicated-On Thread Instructions Executed**Number of times the source (instruction) was executed by any active, predicated-on thread. For instructions that are executed unconditionally (i.e. without predicate), this is the number of active threads in the warp, multiplied with the respective

*Instructions Executed*value.**Avg. Threads Executed**Average number of thread-level executed instructions per warp, regardless of their predicate.

**Avg. Predicated-On Threads Executed**Average number of predicated-on thread-level executed instructions per warp.

**Divergent Branches**Number of divergent branch targets, including fallthrough. Incremented only when there are two or more active threads with divergent targets. Divergent branches can lead to warp stalls due to resolving the branch or instruction cache misses.

**Information on Memory Operations****Label****Name****Description**Address Space

memory_type

The accessed address space (global/local/shared).

Access Operation

memory_access_type

The type of memory access (e.g. load or store).

Access Size

memory_access_size_type

The size of the memory access, in bits.

L1 Tag Requests Global

memory_l1_tag_requests_global

Number of L1 tag requests generated by global memory instructions.

L1 Conflicts Shared N-Way

derived__memory_l1_conflicts_shared_nway

Average N-way conflict in L1 per shared memory instruction. A 1-way access has no conflicts and resolves in a single pass. Note: This is a derived metric which can not be collected directly.

L1 Wavefronts Shared Excessive

derived__memory_l1_wavefronts_shared_excessive

Excessive number of wavefronts in L1 from shared memory instructions, because not all not predicated-off threads performed the operation. Note: This is a derived metric which can not be collected directly.

L1 Wavefronts Shared

memory_l1_wavefronts_shared

Number of wavefronts in L1 from shared memory instructions.

L1 Wavefronts Shared Ideal

memory_l1_wavefronts_shared_ideal

Ideal number of wavefronts in L1 from shared memory instructions, assuming each not predicated-off thread performed the operation.

L2 Theoretical Sectors Global Excessive

derived__memory_l2_theoretical_sectors_global_excessive

Excessive theoretical number of sectors requested in L2 from global memory instructions, because not all not predicated-off threads performed the operation. Note: This is a derived metric which can not be collected directly.

L2 Theoretical Sectors Global

memory_l2_theoretical_sectors_global

Theoretical number of sectors requested in L2 from global memory instructions.

L2 Theoretical Sectors Global Ideal

memory_l2_theoretical_sectors_global_ideal

Ideal number of sectors requested in L2 from global memory instructions, assuming each not predicated-off thread performed the operation.

L2 Theoretical Sectors Local

memory_l2_theoretical_sectors_local

Theoretical number of sectors requested in L2 from local memory instructions.

All

*L1/L2 Sectors/Wavefronts/Requests*metrics give the number of achieved (actually required), ideal, and excessive (achieved - ideal) sectors/wavefronts/requests.*Ideal*metrics indicate the number that would needed, given each not predicated-off thread performed the operation of given width.*Excessive*metrics indicate the required surplus over the ideal case. Reducing divergence between threads can reduce the excess amount and result in less work for the respective HW units.

Several of the above metrics on memory operations were renamed in version 2021.2 as follows:

|
|
memory_l2_sectors_global |
memory_l2_theoretical_sectors_global |
memory_l2_sectors_global_ideal |
memory_l2_theoretical_sectors_global_ideal |
memory_l2_sectors_local |
memory_l2_theoretical_sectors_local |
memory_l1_sectors_global |
memory_l1_tag_requests_global |
memory_l1_sectors_shared |
memory_l1_wavefronts_shared |
memory_l1_sectors_shared_ideal |
memory_l1_wavefronts_shared_ideal |

**L2 Explicit Evict Policy Metrics**Starting with the NVIDIA Ampere architecture the eviction policy of the L2 cache can be tuned to match the kernel’s access pattern. The eviction policy can be either set implicitly for a memory window (for more details see

[CUaccessProperty](https://docs.nvidia.com/cuda/cuda-runtime-api/structcudaAccessPolicyWindow.html)) or set explicitly per executed memory instruction. If set explicitly, the desired eviction behavior for the cases of an L2 cache hit or miss are passed as input to the instruction. For more details refer to CUDA’s[Cache Eviction Priority Hints](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#cache-eviction-priority-hints).**Label****Name****Description**L2 Explicit Evict Policies

smsp__inst_executed_memdesc_explicit_evict_type

Comma separated list of configured explicit eviction policies. As the policies can be set dynamically at runtime, this list includes all policies that were part of any executed instruction.

L2 Explicit Hit Policy Evict First

smsp__inst_executed_memdesc_explicit_hitprop_evict_first

Number of times a memory instruction was executed by any warp which had the

`evict_first`

policy set in case the access leads to a cache hit in L2. Data cached with this policy will be first in the eviction priority order and will likely be evicted when cache eviction is required. This policy is suitable for streaming data.L2 Explicit Hit Policy Evict Last

smsp__inst_executed_memdesc_explicit_hitprop_evict_last

Number of times a memory instruction was executed by any warp which had the

`evict_last`

policy set in case the access leads to a cache hit in L2. Data cached with this policy will be last in the eviction priority order and will likely be evicted only after other data with`evict_normal`

or`evict_first`

eviction policy is already evicted. This policy is suitable for data that should remain persistent in cache.L2 Explicit Hit Policy Evict Normal

smsp__inst_executed_memdesc_explicit_hitprop_evict_normal

Number of times a memory instruction was executed by any warp which had the

`evict_normal`

(default) policy set in case the access leads to a cache hit in L2.L2 Explicit Hit Policy Evict Normal Demote

smsp__inst_executed_memdesc_explicit_hitprop_evict_normal_demote

Number of times a memory instruction was executed by any warp which had the

`evict_normal_demote`

policy set in case the access leads to a cache hit in L2.L2 Explicit Miss Policy Evict First

smsp__inst_executed_memdesc_explicit_missprop_evict_first

Number of times a memory instruction was executed by any warp which had the

`evict_first`

policy set in case the access leads to a cache miss in L2. Data cached with this policy will be first in the eviction priority order and will likely be evicted cache eviction is required. This policy is suitable for streaming data.L2 Explicit Miss Policy Evict Normal

smsp__inst_executed_memdesc_explicit_missprop_evict_normal

Number of times a memory instruction was executed by any warp which had the

`evict_normal`

(default) policy set in case the access leads to a cache miss in L2.**Individual Warp Stall Sampling Metrics**All

*stall_**metrics show the information combined in*Warp Stall Sampling*individually. See[Statistical Sampler](https://docs.nvidia.com/ProfilingGuide/index.html#statistical-sampler)for their descriptions.See the

[Customization Guide](https://docs.nvidia.com/CustomizationGuide/index.html#abstract)on how to add additional metrics for this view and the[Metrics Reference](https://docs.nvidia.com/ProfilingGuide/index.html#metrics-reference)for further information on available metrics.

###### Register Dependencies[#](https://docs.nvidia.com#register-dependencies)

Dependencies between registers are displayed in the SASS view. When a register is read, all the potential addresses where it could have been written are found. The links between these lines are drawn in the view. All dependencies for registers, predicates, uniform registers and uniform predicates are shown in their respective columns.

The picture above shows some dependencies for a simple CUDA kernel. On the first row, which is line 9 of the SASS code, we can see *writes* on registers R2 and R3, represented by *filled triangles pointing to the left*. These registers are then read on lines 17, 20 and 23, and this is represented by *regular triangles pointing to the right*. There are also some lines where both types of triangles are on the same line, which means that a read and a write occured for the same register.

The lines are colored with a gradient that helps visualizing how long the dependencies are.

Dependencies across source files and functions are not tracked.

The Register Dependencies Tracking feature is enabled by default, but can be disabled completely in *Tools > Options > Profile > Report Source Page > Enable Register Dependencies*.

##### Profiles[#](https://docs.nvidia.com#profiles)

The icon next to the *View* dropdown can be used to manage *Source View Profiles*.

This button opens a dialog that shows you the list of saved source view profiles. Such profiles can be created using the `+`

button in the dialog. Profiles let you store the column properties of all views in the report to a file. Such properties include column visibility, freeze state, width, order and the selected navigation metric. Double-click on a saved profile to apply it to any opened report. This updates the column properties mentioned above from the selected profile in all views.

Profiles are useful for configuring views to your preferences, or for a certain use case. Start by choosing metric columns from the *Column Chooser*. Next, configure other properties like freezing column, changing width or order and setting a heatmap metric in the *Navigation* dropdown before creating the profile. Once a profile is created, you can always use this profile on any opened report to hide all non-required columns or to restore your configured properties.
Simply select the profile from the source view profiles dialog and apply it. You can also make the profile default by clicking on the *star* button to automatically apply it while opening a report.

Note that the column properties are stored separately for each *View* in the profile and when applied, only those views will be updated which are present in the selected profile. You will not see the metric columns that are not available in your report even if those were configured to be visible in the source profile you have applied.

##### Additional Tables[#](https://docs.nvidia.com#additional-tables)

###### Instructions & Dependencies Table[#](https://docs.nvidia.com#instructions-dependencies-table)

If **Scoreboard Dependencies** is selected, this table shows the following information for the selected line:

**Self Instruction Mix**: The breakdown of all instruction categories. Use this to understand the composition of the selection, and which instruction categories have the most (scoreboard) warp stalls.**Input Scoreboard Dependencies**: The scoreboard-driven data dependencies of the selection. Data dependencies are predecessor operations that need to complete before code in the selection can proceed. Use this to understand on which instructions the selection is waiting (stalled) on.The

*Attributed Stalls*column shows the number of warp stalls from the selection attributed to this dependency. As a result, dependencies causing more stalls in the selection are sorted higher in the table. This data is also available in the source views to locate lines causing the most stalls.**Output Scoreboard Dependencies**: The consumers of scoreboards produced by the selection. A scoreboard producer is an operation producing a scoreboard a consumer is waiting on. Use this to understand who is waiting (stalled) on the selection. Note that these lines may wait for other instructions than the current selection, too.

Scoreboards are used to synchronize data dependencies, state updates and ensure memory ordering. This includes true data dependencies (read-after-write) and anti-dependencies (write-after-read).

Relative percentage values in these tables are calculated based on the total value of the respective data in the entire view, not just in the selection.

The *Dependencies* tables show in their *Scoreboards* columns which of the GPU’s six scoreboards are responsible for the dependency.
Use the *Scoreboard Dependencies* column in the SASS view to see individual scoreboard dependencies between assembly instructions.
Lines at the same offset in this column are for the same scoreboard.

The *Scoreboard Stalls* column uses different colors to distinguish between long and short scoreboard warp stalls.

If **Register Dependencies** is selected, this table shows the following information for the selected line:

**Self Instruction Mix**: The breakdown of all instruction categories. Use this to understand the composition of the selection.**Input Register Dependencies**: The general purpose register-driven data dependencies of the selection. Data dependencies are predecessor operations that need to complete before code in the selection can proceed. Use this to understand which instructions produce/write registers the selection is waiting to consume/read.The

*Attributed Live Registers*column shows the number of live general-purpose registers attributed to instructions of this category. This is the maximum number of live registers across all consumers of dependencies from this producer. This data is also available in the source views to locate lines causing the most live registers.The

*Output Registers*column shows the number of register dependencies produced by instructions of this category. This is the sum of all general-purpose registers written by this producer. This data is also available in the source views to locate lines producing the most dependencies.**Output Register Dependencies**: This table lists all consumers/readers of general-purpose registers produced/written by the selected line. A register producer is an operation writing a register a consumer is waiting on for reading. Use this to understand which instructions are waiting on the selection to produce/write registers. Note that these lines may wait for other instructions than the current selection, too.

For both scoreboard and register views, the dependencies are grouped by location and instruction category. If the location does not match the selected line, it is shown as a clickable link. Clicking on the link will navigate to the corresponding line. If the selection is in a high-level (e.g., CUDA, Python) view, the locations are mapped to the high-level language if possible. If not possible due to missing correlation information, or if the selection is in the SASS view, the locations are shown in the low-level language.

###### Inline Functions Table[#](https://docs.nvidia.com#inline-functions-table)

This table shows all call sites where the selected function from the *Source* view is inlined.

In the *Source* view, correlated metric values of every inline function source line are an aggregation of metric values of related SASS lines from all call sites. The table provides such SASS lines info for each call site individually to help in identifying which call site contributes how much to the overall metric values.

###### Source Markers Table[#](https://docs.nvidia.com#source-markers-table)

The code in the different *Views* can also contain warnings, errors or just notifications that are displayed as *Source Markers* in the left header, as shown below. These can be generated from multiple sources, but as of now only NvRules are supported.

This table shows all lines containing *Source Markers* in the open View. The user can click on the line number to navigate to the corresponding line in the view.

###### Statistics Table[#](https://docs.nvidia.com#statistics-table)

This table allows the user to select multiple lines in the source code above and calculate a variety of statistics. They can be used to check if anything seems unusual, like an unexpected gap between minimum and maximum.

Cells will be empty if the metric has either not been collected or its statistical value is not meaningful in the context of the calculation. For example, a memory access or any other non-numeric metric can’t have a minimum or maximum since there is no defined order.

##### Limitations[#](https://docs.nvidia.com#profiler-report-source-page-limitations)

Graph Profiling

When profiling complete CUDA graphs, instruction-level source metrics are not available.

#### Context Page[#](https://docs.nvidia.com#context-page)

The *CPU Call Stack* section of this report page shows the CPU call stack(s) for the executing CPU thread at the time the kernel was launched. For this information to show up in the profiler report, the option to collect CPU call stacks had to be enabled in the [Connection Dialog](https://docs.nvidia.com/index.html#connection-dialog) or using the corresponding NVIDIA Nsight Compute CLI command line parameter.

NVIDIA Nsight Compute supports to collect *native* CPU call stacks as well as call stacks for *Python* applications.
Either or both types can be selected in the *Activity* menu of the [Connection Dialog](https://docs.nvidia.com/index.html#connection-dialog) (via the “CPU Call Stack Types” option),
or using the NVIDIA Nsight Compute [CLI command line parameter](https://docs.nvidia.com/NsightComputeCli/index.html#command-line-options-launch) –call-stack-type.
In case both types are enabled, a dropdown menu will appear to select the desired call stack type.

Note that Python call stack collection requires CPython version 3.9 or later.

The *NVTX State* section of this report page shows the NVTX context when the kernel was launched. All thread-specific information is with respect to the thread of the kernel’s launch API call. Note that NVTX information is only collected if the profiler is started with NVTX support enabled, either in the [Connection Dialog](https://docs.nvidia.com/index.html#connection-dialog) or using the NVIDIA Nsight Compute CLI command line parameter.

This page has been renamed from “Call Stack / NVTX Page”.

#### Raw Page[#](https://docs.nvidia.com#raw-page)

The *Raw* page shows a list of all collected metrics with their units per profiled kernel launch. It can be exported, for example, to CSV format for further analysis. The page features a filter edit to quickly find specific metrics. You can transpose the table of kernels and metrics by using the *Transpose* button.

If a metric has multiple instance values, the number of instances is shown after the standard value. This metric for example has ten instance values: `35.48 {10}`

. You can select in the [Profile](https://docs.nvidia.com/index.html#options-profile) options dialog that all instance values should be shown individually or inspect the metric result in the [Metric Details](https://docs.nvidia.com/index.html#tool-window-metric-details) tool window.

#### Session Page[#](https://docs.nvidia.com#session-page)

This *Session* page contains basic information about the report and the machine, as well as device attributes of all devices for which launches were profiled. When switching between launch instances, the respective device attributes are highlighted.

### 4.7.3. Metrics and Units[#](https://docs.nvidia.com#metrics-and-units)

Numeric metric values are shown in various places in the report, including the header and tables and charts on most pages. NVIDIA Nsight Compute supports various ways to display those metrics and their values.

When available and applicable to the UI component, metrics are shown along with their unit. This is to make it apparent if a metric represents cycles, threads, bytes/s, and so on. The unit will normally be shown in rectangular brackets, e.g. `Metric Name [bytes] 128`

.

By default, units are scaled automatically so that metric values are shown with a reasonable order of magnitude. Units are scaled using their SI-factors, i.e. byte-based units are scaled using a factor of 1000 and the prefixes K, M, G, etc. Time-based units are also scaled using a factor of 1000, with the prefixes n, u and m. This scaling can be disabled in the [Profile](https://docs.nvidia.com/index.html#options-profile) options.

Metrics which could not be collected are shown as `n/a`

and assigned a warning icon. If the metric floating point value is out of the regular range (i.e. `nan`

(Not a number) or `inf`

(infinite)), they are also assigned a warning icon. The exception are metrics for which these values are expected and which are allow-listed internally.

### 4.7.4. Filtered Profiler Report[#](https://docs.nvidia.com#filtered-profiler-report)

A filtered profiler report is a subset of the full profiler report. You can save filtered or selected results from the full profiler report to a new file.
To save the filtered results, you can use the File > Save Filtered Results As menu option, which will save the [Filtered Results](https://docs.nvidia.com/NsightCompute/index.html#profiler-report-header-filter-dialog) to a new file.
Alternatively, you can select one or more results on the [Summary Page](https://docs.nvidia.com/NsightCompute/index.html#summary-page) or [Raw Page](https://docs.nvidia.com/NsightCompute/index.html#raw-page) and save them to a new file using the File > Save Selected Results As menu option or the right-click Save Result(s) menu option.

## 4.8. Baselines[#](https://docs.nvidia.com#id11)

NVIDIA Nsight Compute supports diffing collected results across one or multiple reports using Baselines. Each result in any report can be promoted to a baseline. This causes metric values from all results in all reports to show the difference to the baseline. If multiple baselines are selected simultaneously, metric values are compared to the average across all current baselines. Baselines are not stored with a report and are only available as long as the same NVIDIA Nsight Compute instance is open, unless they are saved to a `ncu-bln`

file from the [Baselines tool window](https://docs.nvidia.com/index.html#tool-window-baselines).

Select *Add Baseline* to promote the current result in focus to become a baseline. If a baseline is set, most metrics on the [Details Page](https://docs.nvidia.com/index.html#profiler-report-details-page), [Raw Page](https://docs.nvidia.com/index.html#profiler-report-raw-page) and [Summary Page](https://docs.nvidia.com/index.html#profiler-report-summary-page) show two values: the current value of the result in focus, and the corresponding value of the baseline or the percentage of change from the corresponding baseline value. (Note that an infinite percentage gain, *inf%*, may be displayed when the baseline value for the metric is zero, while the focus value is not.)

If multiple baselines are selected, each metric will show the following notation:

```
<focus value> (<difference to baselines average [%]>, z=<standard score>@<number of values>)
```

The standard score is the difference between the current value and the average across all baselines, normalized by the standard deviation. If the number of metric values contributing to the standard score equals the number of results (current and all baselines), the @<number of values> notation is omitted.

Baseline added for the current result in focus is always shown on the top. However, the actual order of added baselines is shown in the [Baselines tool window](https://docs.nvidia.com/index.html#tool-window-baselines).

Double-clicking on a baseline name allows the user to edit the displayed name. Edits are committed by pressing `Enter/Return`

or upon loss of focus, and abandoned by pressing `Esc`

. Hovering over the baseline color icon allows the user to remove this specific baseline from the list.

Use the *Clear Baselines* entry from the dropdown button, the [Profile](https://docs.nvidia.com/index.html#options-profile) menu, or the corresponding toolbar button to remove all baselines.

Baseline changes can also be made in the [Baselines tool window](https://docs.nvidia.com/index.html#tool-window-baselines).

## 4.9. Standalone Source Viewer[#](https://docs.nvidia.com#standalone-source-viewer)

NVIDIA Nsight Compute includes a standalone source viewer for *cubin* files. This view is identical to the [Source Page](https://docs.nvidia.com/index.html#profiler-report-source-page), except that it won’t include any performance metrics.

Cubin files can be opened from the *File* > *Open* main menu command. The SM Selection dialog will be shown before opening the standalone source view. If available, the SM version present in the file name is pre-selected. For example, if your file name is `mergeSort.sm_80.cubin`

then SM 8.0 will be pre-selected in the dialog. Choose the appropriate SM version from the drop down menu if it’s not included in the file name.

Click Ok button to open [Standalone Source Viewer](https://docs.nvidia.com/index.html#cubin-viewer).

## 4.10. Source Comparison[#](https://docs.nvidia.com#source-comparison)

Source comparison provides a way to see the source files of two profile results side by side. It enables to quickly identify source differences and understand changes in metric values.

To compare two results side by side add one result as a baseline, navigate to the other result, and then click the *Source Comparison* button located in the report header.

For example, if you want to compare kernel XYZ from report R1 with kernel XYZ from report R2, first open report R1, add the profile result for kernel XYZ as baseline, open report R2, choose kernel XYZ, and then click the Source Comparison button.

Source comparison will be shown only with first added baseline result.

Currently only high-level Source (CUDA-C) view, SASS view, and Tile IR view are supported for comparison. The source difference heatmap is located on the very left side. Each of its partitions represents a side of the source diff. Clicking on the heatmap will scroll to the respective source line.

Navigation to the previous or next difference is supported using the navigation buttons or the keyboard shortcuts *Ctrl + 1* and *Ctrl + 2*.

On the SASS view, the *Diff By* drop down menu allows you to choose the diff basis based on either *Opcode* or *Full Instruction*. For the latter, all instruction modifiers and arguments are considered for the comparison in addition to the opcode.

## 4.11. Report Merge Tool[#](https://docs.nvidia.com#report-merge-tool)

NVIDIA Nsight Compute provides a *Report Merge Tool* utility that enables users to combine multiple Nsight Compute reports with the `.ncu-rep`

extension into a single file.
It is particularly useful for multi-GPU systems and scenarios when comparing and analyzing several reports individually becomes impractical.
The report created with ReportMergeTool is fully compatible with Nsight Compute, and can be used for visualization and analysis in the UI and on the command line.

There are 2 options for using the MergeTool.

**Launching from the UI menu**Select the Merge Tool item from Tools in the

[Main Menu](https://docs.nvidia.com/index.html#main-menu).**Launching from the Command Line**Call the binary in

`$NCU_INSTALL_PATH/extras/ReportUtils/ReportMergeTool`

.It accepts a directory as an input, and it will merge all the reports under that directory. Other features follow exactly the same logic as the UI.


### 4.11.1. File Selection Tab[#](https://docs.nvidia.com#file-selection-tab)

This tab handles the selection of reports and allows to set the output name and/or path for the resulting merged report. There are 2 ways of selecting report files to merge.

**Selecting from system files**This option shows a hierarchical view of

`.ncu-rep`

files in the system, and the containing folders. Individual reports can be selected together with entire folders. The*Report Directory*input changes the root directory of the hierarchical view.**Selecting from currently open reports**When some reports are already open in Nsight Compute, MergeTool will suggest to merge them first. To change select from the system files, set

*Select from*combo box item to*System Files*, or use the*Report Directory*selector.

### 4.11.2. Metric Filters Tab[#](https://docs.nvidia.com#metric-filters-tab)

This tab guides the selection and merging process of individual metrics.
Selecting the *Merge Operation* defines which metrics are merged and kept across all report results.
*Aggregation Operation* then tells how these metrics are merged, and how the resulting value is calculated from multiple values.
For any other filtering operation metric names can be provided in *Results* text box, or *Metric Sets/Sections* can be selected.

Metric Merge Operations

Metric Merge Operations dictate how the metric set for matching results is maintained in the merged report.

**Union**keeps all the metrics that appear at least once across the matching results in all reports. There can only be one metric set per result, metrics that don’t exist in some reports will appear empty in those cases.**Intersection**keeps only the metrics that exist in all matching results across the reports. This option guarantees that no metrics will have missing values in the output. Note that if reports contain no matching results, they cannot be merged, which may result in some metrics being empty in the final output.

Aggregation Operations

Whenever two or more report results are merged, the metric values are aggregated. Aggregation operations tell the MergeTool how the metrics are combined together. As a result, the merged report will contain one of these four options as a metric value.

**Average**of the combined metric values**Sum****Minimum****Maximum**

Metric Selection: Metric List, Sets, Sections

Apart from Merge Operations, the metric list for the output report can be manipulated using filtering.
The simplest way to set the metric list is to enter the metrics as a comma-separated list in the *Metrics* text box.

Additionally, metric sets and sections can be used, by loading a view similar to [Metric Selection](https://docs.nvidia.com/index.html#metric-selection).
Selecting the sets and sections modifies the appearance of the reports by changing the sections that are displayed on the *Details* page.
The metrics of the reports are not affected.
To remove unwanted sections, select the *Remove Unselected Sections* checkbox.

### 4.11.3. Result Filters Tab[#](https://docs.nvidia.com#result-filters-tab)

This tab guides the selection and merging process of individual results.
It allows to select the [Merge Operation](https://docs.nvidia.com/index.html#mergetool-results-merge-op) to define which results are merged and kept.

For any other filtering operations result names can be provided in the *Results* text box as a comma-separated list.
If this list is set, only the provided results will appear in the output.

#### Result Merge Operations[#](https://docs.nvidia.com#result-merge-operations)

Result merge operations, similarly to the metric merge operations, tell the MergeTool which results to keep and which results to discard. Additionally, they can manage the merge process by matching the results from the merged reports. The matched results are the ones that will be aggregated together into a single result. The four available options provide control over which results are merged together and how to handle unmatched results.

**Union**merges only matching results from every report, keeps unmatched results as is. When multiple iterations of the same kernel appear in a report, they are kept separate and are only merged with the corresponding iteration of this kernel in other reports.*For example:*Merging Report1 with results name {kernel_A, kernel_B} and Report2 with {kernel_A, kernel_C} results in {kernel_Amerged, kernel_B, kernel_C}. i.e.,\(\{A, B\} + \{A, C\} = \{A^{merged}, B, C\}\)

*Note:*if multiple results share the same name, only matching ones are merged. i.e.,\(\{A_{1}, A_{2}, A_{3}\} + \{A_{1}, A_{2}\} = \{A_{1}^{merged}, A_{2}^{merged}, A_{3}\}\)

**Intersection**merges matching results from every report in the same way as*Union*does, but discards all the unmatched results.\(\{A, B\} + \{A, C\} = \{A^{merged}\}\)

**Collapse**merges all results sharing the same name. When multiple iterations of the same kernel appear in a report, merges them together.\(\{A_{1}, A_{2}, A_{3}\} + \{A_{1}, A_{2}\} = \{A^{merged}\}\)

**Concat**keeps all the results in their original form and saves them in a single file, no metric aggregation is done.\(\{A, B\} + \{A, C\} = \{A_{1}, B, A_{2}, C\}\)


#### Merged Report[#](https://docs.nvidia.com#merged-report)

To be able to track how a merged report was created, each merged report contains a comment with the list of reports that were merged, the merge operation, the aggregation operation and the sections that were selected.

## 4.12. Clustering Window[#](https://docs.nvidia.com#clustering-window)

The **Clustering Window** helps you analyze and compare multiple profiling reports by grouping similar reports together. This makes it easier to identify performance patterns and find relationships between different profiling sessions.

### 4.12.1. How to Use Clustering[#](https://docs.nvidia.com#how-to-use-clustering)

**Open Clustering Window**: From the main menu, select*Tools*>*Clustering Window*. The window can be docked or undocked like other tool windows.**Select Reports**: Click*Select Reports*and choose multiple`.ncu-rep`

files from the file dialog.**Configure Parameters**(Optional):*Minimum Cluster Size*: How many reports are needed to form a cluster (default: 3, minimum allowed: 2)*Maximum Cluster Size*: Maximum reports per cluster (0 = no limit)

**Run Analysis**: Click*Cluster Reports*to analyze the selected reports and generate clusters.

### 4.12.2. Clustering Tree[#](https://docs.nvidia.com#clustering-tree)

The clustering tree shows how reports are grouped together hierarchically:

**Reports and Clusters**: Individual reports are shown as leaf nodes in the tree with unique IDs, and clusters are shown as nodes with a**+**sign.**Selecting Clusters**: Click the**+**nodes to select a cluster for merging. Selected clusters will be shown in green, and the corresponding entries in the similarity matrix below will be highlighted with a dotted border.**Highlighting**: When you hover over any cluster or report in the tree, the corresponding entries are highlighted in the tree and the similarity matrix below.

The tree structure helps you understand:

Which reports are most similar to each other (grouped in the same cluster)

The hierarchical relationships between different groups of reports

How the clustering algorithm has organized your data


### 4.12.3. Similarity Matrix[#](https://docs.nvidia.com#similarity-matrix)

The similarity matrix displays a grid showing how similar each pair of reports is between each other. This matrix is used to generate the clustering tree - reports with higher similarity scores are grouped closer together in the tree structure.

**Rows and Columns**: Each row displays a report name along with its ID, while columns show report IDs that are used in the Clustering Tree.**Similarity Scores**: Each cell contains a similarity value calculated based on the metric values from the reports.**Color Coding**:Darker colors indicate higher similarity between reports

Lighter colors indicate lower similarity

The highlighted entries in the similarity matrix are the ones that are being hovered over in the clustering tree.


**Similarity Score Values**: Hover over any cell to see the exact similarity score between those two reports.

Control Buttons

*Select Reports*opens a file dialog to choose the`.ncu-rep`

files you want to analyze.*Run Clustering*starts the clustering analysis using the selected reports and current parameters.*Reset to Default*restores clustering parameters to their default values.*Clear Clusters*clears the current cluster selection.*Suggest Clusters*automatically recommends optimal clustering parameters based on your data characteristics. The suggestion will cover most of the reports, but outliers may be excluded.*Merge Clusters*creates a merged report from the selected clusters. The merged reports can be processed using the[Report Merge Tool](https://docs.nvidia.com/index.html#report-merge-tool.html)for further analysis and customization.

## 4.13. Occupancy Calculator[#](https://docs.nvidia.com#occupancy-calculator)

NVIDIA Nsight Compute provides an *Occupancy Calculator* that allows you to compute the multiprocessor occupancy of a GPU for a given CUDA kernel. It replaces the previously provided CUDA Occupancy Calculator spreadsheet.

The Occupancy Calculator can be opened directly from a profile report or as a new activity. The occupancy calculator data can be saved to a file using *File > Save*. By default, the file uses the `.ncu-occ`

extension. The occupancy calculator file can be opened using *File > Open File*

**Launching from the Connection Dialog**Select the Occupancy Calculator activity from the connection dialog. You can optionally specify an occupancy calculator data file, which is used to initialize the calculator with the data from the saved file. Click the

*Launch*button to open the Occupancy Calculator.**Launching from the Profiler Report**The Occupancy Calculator can be opened from the

*Profiler Report*using the calculator button located in the report header or in the header of the*Occupancy*section on the*Detail Page*.

The user interface consists of an input section as well as tables and graphs that display information about GPU occupancy. To use the calculator, change the input values in the input section, click the *Apply* button and examine the tables and graphs.

### 4.13.1. Tables[#](https://docs.nvidia.com#tables)

The tables show the occupancy, as well as the number of active threads, warps, and thread blocks per multiprocessor, and the maximum number of active blocks on the GPU.

### 4.13.2. Utilization[#](https://docs.nvidia.com#utilization)

These stacked bar graphs show the portion of resources that is allocated to the blocks, the unallocated portion due to some other resource being a limiter, and lastly the unused portion that has the size less than the minimum amount required by a block.

### 4.13.3. Graphs[#](https://docs.nvidia.com#graphs)

The graphs show the occupancy for your chosen block size as a blue circle, and for all other possible block sizes as a line graph. The “Show As” option allows you to switch between the occupancy in percent and absolute number of warps on Y-axis. When you hover over the graphs, the nearest data point will be highlighted and its X and Y-axis values will appear in a tooltip.

### 4.13.4. GPU Data[#](https://docs.nvidia.com#gpu-data)

The *GPU Data* shows the properties of all supported devices.

## 4.14. Green Contexts support[#](https://docs.nvidia.com#green-contexts-support)

NVIDIA Nsight Compute provides a number of features to ease the analysis of applications using
[CUDA Green Contexts](https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__GREEN__CONTEXTS.html#group__CUDA__GREEN__CONTEXTS), see
the [Profiling Guide](https://docs.nvidia.com/ProfilingGuide/index.html#special-configurations-green-contexts) for an overview about
profiling such applications.

To identify Green Context results quickly, the icon of the *Attributes* button in the [Profiler Report Header](https://docs.nvidia.com/index.html#profiler-report-header)
turns into a *leaf* for Green Context results. Clicking on this button navigates to the *Launch Statistics* section of the result (if available),
which contains [additional metrics](https://docs.nvidia.com/ProfilingGuide/index.html#id28) related to the Green Context (e.g., its ID and the number of SMs used).
Some of this information is also available from the tooltip when hovering over the *Attributes* button.

To distinguish between Green-Contexts *attributable* and *non-attributable* metrics when navigating the [Details page](https://docs.nvidia.com/index.html#details-page), *Green Context markers*
may be used. These can be toggled via the *View* menu of the [Report Header](https://docs.nvidia.com/index.html#profiler-report-header) and adds a *leaf* icon
behind *attributable* metrics in all section headers. When hovering over attributable metrics, the tooltip also shows a hint about the
scaling of such metrics.
Additionally, the [Metrics Details](https://docs.nvidia.com/index.html#metric-details) tool window shows an *Attribution* row for metrics of Green Context results.

If a report contains Green Context results, the [Session page](https://docs.nvidia.com/index.html#session-page) includes an additional *Green Context Resources* section.
It contains a table with information about the resources used by each Green Context, such as the TPCs
and workqueue resources
assigned to it.
The *Result IDs* column allows you to navigate to each profile result that uses the corresponding Green Context.

When profiling Green Context applications interactively, the [Resources](https://docs.nvidia.com/index.html#resources) tool window also allows to track
the state of all Green Contexts, their resources, as well as their associated streams.

## 4.15. Acceleration Structure Viewer[#](https://docs.nvidia.com#acceleration-structure-viewer)

The *Acceleration Structure Viewer* allows inspection of acceleration structures built using the OptiX API. In modern ray tracing APIs like OptiX, *acceleration structures* are data structures describing the rendered scene’s geometries that will be intersected when performing ray tracing operations. More information concerning acceleration structures can be found in the [OptiX programming guide](https://raytracing-docs.nvidia.com/optix7/guide/index.html#acceleration_structures#acceleration-structures).

It is the responsibility of the user to set these up and pass them to the OptiX API which translates them to internal data structures that perform well on modern GPUs. The description created by the user can be very error-prone and it is sometimes hard to understand why the rendered result is not as expected. The *Acceleration Structure Viewer* is a component allowing OptiX users to inspect the acceleration structures they build before launching a ray tracing pipeline.

The *Acceleration Structure Viewer* is opened through a button in the [Resources](https://docs.nvidia.com/index.html#tool-window-resources) window. The button will only be available when the currently viewed resource is *OptiX: TraversableHandles*. It opens the currently selected handle.

The viewer is multi-paned: it shows a hierarchical view of the acceleration structure on the left, a graphical view of the acceleration structure in the middle, and controls and options on the right. In the hierarchical tree view on the left of the viewer the *instance acceleration structures (IAS)*, *geometry acceleration structures (GAS)*, child instances and child geometries are shown. In addition to this, some general properties for each of them is shown such as their primitive count, surface area and size on the device.

In the hierarchical view on the left of the *Acceleration Structure Viewer*, the following information is displayed where applicable.

Column |
Description |
|---|---|
Name |
An identifier for each row in the hierarchy. Click on the check box next to the name to show or hide the selected geometry or hierarchy. Double-click on this entry to jump to the item in the rendering view. |
# Prims |
The number of primitives that make up this acceleration structure. |
Surface Area |
A calculation of the total surface area for the AABB that bounds the particular entry. |
Size |
The size of the output buffer on the device holding this |

Performance analysis tools are accessible in the bottom left corner on the main view. These tools help identify potential performance problems that are outlined in the [RTX Ray Tracing Best Practices Guide](https://developer.nvidia.com/blog/best-practices-using-nvidia-rtx-ray-tracing). These analysis tools aim to give a broad picture of acceleration structures that may exhibit sub-optimal performance. To find the most optimal solution, profiling and experimentation is recommended but these tools may paint a better picture as to why one structure performs poorly compared to another.

Action |
Description |
|---|---|
Instance Overlaps |
Identifies instance AABBs that overlap with other instances in 3D. Consider merging GASes when instance world-space AABBs overlap significantly to potentially increase performance. |
Instance Heatmap |
This allows you to set the threshold used by the AABB heatmap rendered in the visualizer. |

### 4.15.2. Filtering and Highlighting[#](https://docs.nvidia.com#filtering-and-highlighting)

The acceleration structure view supports acceleration structure filtering as well as highlighting of data matching particular characteristics. The checkboxes next to each geometry allow users to toggle the rendering of each traversable.

Geometry instances can also be selected by clicking on them in the main graphical view. Additionally, right clicking in the main graphical view gives options to hide or show all geometry, hide the selected geometry, or hide all but the selected geometry.

Beyond filtering, the view also supports highlight-based identification of geometry specified with particular flags. Checking each highlight option will identify those resources matching that flag, colorizing for easy identification. Clicking an entry in this section will dim all geometry that does **not** meet the filter criteria allowing items that match the filter to standout. Selecting multiple filters requires the passing geometry to meet all selected filters (e.g., AND logic). Additionally, the heading text will be updated to reflect the number of items that meet this filter criteria.

### 4.15.3. Rendering Options[#](https://docs.nvidia.com#rendering-options)

Under the highlight controls, additional rendering options are available. These include methods to control the geometry colors and the ability to toggle the drawing of wireframes for meshes and AABBs.

### 4.15.4. Exporting[#](https://docs.nvidia.com#exporting)

The data displayed in the acceleration structure viewer document can be saved to file. Exporting an *Acceleration Structure Viewer* document allows for persisting the data you have collected beyond the immediate analysis session. This capability is particularly valuable for comparing different revisions of your geometry or sharing with others. Bookmarks are persisted as well.

## 4.16. Options[#](https://docs.nvidia.com#options)

NVIDIA Nsight Compute options can be accessed via the main menu under *Tools* > *Options*. All options are persisted on disk and available the next time NVIDIA Nsight Compute is launched. When an option is changed from its default setting, its label will become bold. You can use the *Restore Defaults* button to restore all options to their default values.

### 4.16.1. Profile[#](https://docs.nvidia.com#profile)

#### Report Sections[#](https://docs.nvidia.com#report-sections)

Configure the directories and import settings for section files and rules.

Option Name |
Description |
Values |
|---|---|---|
Sections Directory |
Directory from which to import section files and rules. Relative paths are with respect to the NVIDIA Nsight Compute installation directory. |
|
Include Sub- Directories |
Recursively include section files and rules from sub-directories. |
Yes (Default)/No |

#### Report Rules[#](https://docs.nvidia.com#report-rules)

Configure how rules are applied and reloaded during profiling sessions.

Option Name |
Description |
Values |
|---|---|---|
Apply Applicable Rules Automatically |
Automatically apply active and applicable rules. |
Yes (Default)/No |
Reload Rules Before Applying |
Force a rule reload before applying the rule to ensure changes in the rule script are recognized. |
Yes/No (Default) |

#### Report UI[#](https://docs.nvidia.com#report-ui)

Customize the user interface behavior for report viewing and navigation.

Option Name |
Description |
Values |
|---|---|---|
Default Report Page |
The report page to show when a report is generated or opened. |
|
Function Name Mode |
Determines how function/kernel names are shown. |
|
NVTX Rename Mode |
Determines how NVTX information is used for renaming. Range replay results are always renamed when possible. |
|
Show Metrics Aggregation |
Show aggregate of all results per each counter metric in the table header and aggregated value of randomly selected metrics in the bottom-right label. |
Yes (Default)/No |
Show Y-axis labels |
Display Y-axis labels on the timeline to improve the interpretation of minimum and maximum metric value. |
Yes (Default)/No |
Rename Demangled Names |
Perform auto-simplification on kernel demangled names or import renamed names from a configuration file. |
Yes (Default)/No |
Rename Kernels Config Path |
Use a configuration file to rename multiple demangled names and export demangled names from the report. |
ncu-kernel-renames.yaml |

#### Report Baselines[#](https://docs.nvidia.com#report-baselines)

Configure baseline display settings for result comparison.

Option Name |
Description |
Values |
|---|---|---|
Maximum Baseline Name Length |
The maximum length of baseline names. |
1..N (Default: 40) |
Number of Full Baselines to Display |
Number of baselines to display in the report header with all details in addition to the current result or the baseline added for the current result. |
0..N (Default: 2) |

#### Report Metrics[#](https://docs.nvidia.com#report-metrics)

Configure how metrics are displayed and processed in reports.

Option Name |
Description |
Values |
|---|---|---|
Auto-Convert Metric Units |
Auto-adjust displayed metric units and values (e.g. Bytes to KBytes). |
Yes (Default)/No |
Show Instanced Metric Values |
Show the individual values of instanced metrics in tables. |
Yes/No (Default) |
Show Metrics As Floating Point |
Show all numeric metrics as floating-point numbers. |
Yes/No (Default) |
Show Knowledge Base Information |
Show information from the knowledge base in (metric) tooltips to explain terminology. Note: Nsight Compute needs to be restarted for this option to take effect. |
Yes (Default)/No |

#### Report Summary Page[#](https://docs.nvidia.com#report-summary-page)

Configure settings for the Summary page in reports.

Option Name |
Description |
Values |
|---|---|---|
Metrics/ Properties |
List of metrics and properties to show on the summary page. Comma-separated list of metric entries. Each entry has the format {Label:MetricName}. |

#### Report Details Page[#](https://docs.nvidia.com#report-details-page)

Configure settings for the Details page in reports.

Option Name |
Description |
Values |
|---|---|---|
Default Section Body Visibility |
Controls the default visibility of section bodies when opening a report. |
Default (Default)/All |

#### Report Source Page[#](https://docs.nvidia.com#report-source-page)

Configure settings for the Source page view.

Option Name |
Description |
Values |
|---|---|---|
Delay Load ‘Source’ Page |
Delays loading the content of the report page until the page becomes visible. Avoids processing costs and memory overhead until the report page is opened. |
Yes/No (Default) |
Show Single File For Multi-File Sources |
Shows a single file in each Source page view, even for multi-file sources. |
Yes/No (Default) |
Show Only Executed Functions |
Shows only executed functions in the source page views. Disabling this can impact performance. |
Yes (Default)/No |
Default Metric Value Mode |
Default setting for the mode in which the metric values are displayed. |
Relative (Default)/Absolute |
Default Metric Precision Mode |
Default setting for the precision in which absolute metric values are displayed. |
Abbreviated (Default)/Full |
Auto-Resolve Remote Source Files |
Automatically try to resolve remote source files on the source page (e.g. via SSH) if the connection is still registered. |
Yes/No (Default) |
Enable Register Dependencies |
Track dependencies between SASS registers/predicates and display them in the SASS view. |
Yes (Default)/No |
SASS Analysis Size Threshold (KB) |
Enable SASS flow graph analysis for functions below this threshold. SASS analysis is required for Live Register and Register Dependency information. Set to -1 to enable analysis for all functions. |
-1..N (Default: 1024) |
Enable ELF Verification |
Enable ELF (cubin) verification to run every time before SASS analysis. This should only be enabled when working with applications compiled before CUDA 11.0 or when encountering source page issues. |
Yes/No (Default) |

#### API Stream View[#](https://docs.nvidia.com#api-stream-view)

Configure settings for the API Stream View.

Option Name |
Description |
Values |
|---|---|---|
API Call History |
Number of recent API calls shown in API Stream View. |
1..N (Default: 100) |

#### CUDA Graph Viewer[#](https://docs.nvidia.com#options-profile-graph-viewer)

Configure settings for the CUDA Graph Viewer.

Option Name |
Description |
Values |
|---|---|---|
Auto-Open Graph Viewer |
Automatically open the CUDA Graph Viewer when CUDA graphs are detected during profiling or when opening reports containing CUDA graph results. |
Yes (Default)/No |

### 4.16.2. Fonts and Colors[#](https://docs.nvidia.com#fonts-and-colors)

#### Fonts[#](https://docs.nvidia.com#fonts)

Configure the fonts used throughout the application interface. General fonts affect all UI elements except code, while code fonts are specifically used for source code display and similar content.

Option Name |
Description |
Values |
|---|---|---|
General Font |
General font used for all non-code UI elements. |
Select an installed font via “Change…” button. (Default: Roboto@9pt) |
Code Font |
Font used for source code and code-like UI elements. |
Select an installed font via “Change…” button. (Default: Cascadia Mono@9pt) |

#### Colors[#](https://docs.nvidia.com#colors)

Customize the visual appearance of the application through theme selection and color scale preferences. These settings affect the overall look and feel of the interface and how data is represented visually.

Option Name |
Description |
Values |
|---|---|---|
Color Theme |
The currently selected application color theme. |
|
Default Color Scale |
Default color map used to represent a qualitative scale of values. |
|

### 4.16.3. Environment[#](https://docs.nvidia.com#environment)

#### Visual Experience[#](https://docs.nvidia.com#visual-experience)

Configure how NVIDIA Nsight Compute handles display and windowing behaviors, particularly for multi-monitor setups.

Option Name |
Description |
Values |
|---|---|---|
Use Enhanced Windowing Experience |
Disable Mixed DPI Scaling if unwanted artifacts are detected when using monitors with different DPIs. Requires app restart. |
Yes (Default)/No |

#### Windowing[#](https://docs.nvidia.com#windowing)

Control window behavior and management settings.

Option Name |
Description |
Values |
|---|---|---|
Floating Windows Always on Top |
Configure floating tool windows to always stay on top of the main window. Requires app restart. |
Yes/No (Default) |

#### Documents Folder[#](https://docs.nvidia.com#documents-folder)

Configure where NVIDIA Nsight Compute stores project files and documentation.

Option Name |
Description |
Values |
|---|---|---|
Documents Folder |
The folder where projects and documents will be saved. |

#### Startup Behavior[#](https://docs.nvidia.com#startup-behavior)

Define how NVIDIA Nsight Compute behaves when launched.

Option Name |
Description |
Values |
|---|---|---|
At Startup |
What to do when the host is launched. |
|

#### Updates[#](https://docs.nvidia.com#updates)

Configure version update notification settings.

Option Name |
Description |
Values |
|---|---|---|
Show version update notifications |
Show notifications when a new version of this product is available. |
Yes (Default)/No |

### 4.16.4. Connection[#](https://docs.nvidia.com#connection)

Connection properties are grouped into *Target Connection Options* and *Host Connection Properties*.

#### Target Connection Properties[#](https://docs.nvidia.com#target-connection-properties)

The *Target Connection Properties* determine how the host connects to the target application during an *Interactive Profile Activity*. This connection is used to transfer profile information to the host during the profile session.

Option Name |
Description |
Values |
|---|---|---|
Base Port |
Base port used to establish a connection from the host to the target application during an |
1-65535 (Default: 49152) |
Maximum Ports |
Maximum number of ports to try (starting from |
2-65534 (Default: 64) |

#### Host Connection Properties[#](https://docs.nvidia.com#host-connection-properties)

The *Host Connection Properties* determine how the command line profiler will connect to the host application during a *Profile Activity*. This connection is used to transfer profile information to the host during the profile session.

Option Name |
Description |
Values |
|---|---|---|
Base Port |
Base port used to establish a connection from the command line profiler to the host application during a |
1-65535 (Default: 50152) |
Maximum Ports |
Maximum number of ports to try (starting from |
1-100 (Default: 10) |

#### SSH ProxyJump Connection Properties[#](https://docs.nvidia.com#ssh-proxyjump-connection-properties)

The *SSH ProxyJump Connection Properties* configure how NVIDIA Nsight Compute handles connections through SSH jump hosts. This is useful when profiling applications on target machines that are not directly accessible and require connecting through intermediate SSH servers. The ProxyJump feature allows for secure, multi-hop SSH connections while maintaining the profiling functionality.

Option Name |
Description |
Values |
|---|---|---|
Process Scan Timeout (seconds) |
Maximum time to try searching for attachable process when using SSH ProxyJump connection. |
1-65535 (Default: 10) |

### 4.16.5. Timeline[#](https://docs.nvidia.com#timeline)

#### Basic Settings[#](https://docs.nvidia.com#basic-settings)

The *Timeline Basic Settings* control the visualization and behavior of the Timeline view in NVIDIA Nsight Compute.

Option Name |
Description |
Values |
|---|---|---|
Show correlation arrows |
Show arrows on correlated items on the Timeline |
Yes (Default)/No |

### 4.16.6. Source Lookup[#](https://docs.nvidia.com#source-lookup)

The Source Lookup options control how NVIDIA Nsight Compute locates and validates CUDA source files when displaying source code in the Source page. These settings are particularly important for debugging and profiling sessions where source files may have moved from their original compilation locations or when working with different development environments. The options help ensure accurate source code resolution and provide flexibility in handling file location mismatches.

Option Name |
Description |
Values |
|---|---|---|
Program Source Locations |
Set program source search paths. These paths are used to resolve CUDA-C source
files on the Source page if the respective file cannot be found in its original
location. Files which cannot be found are marked with a |
|
Ignore File Properties |
Ignore file properties (e.g. timestamp, size) for source resolution. If this is
disabled, all file properties like modification timestamp and file size are
checked against the information stored by the compiler in the application during
compilation. If a file with the same name exists on a source lookup path, but
not all properties match, it won’t be used for resolution (and a |
Yes/No (Default) |

### 4.16.7. Send Feedback…[#](https://docs.nvidia.com#send-feedback)

Option Name |
Description |
Values |
|---|---|---|
Collect Usage and Platform Data |
Choose whether or not you wish to allow NVIDIA Nsight Compute to collect usage and platform data. |
Yes (Default)/No |

## 4.17. Projects[#](https://docs.nvidia.com#projects)

NVIDIA Nsight Compute uses *Project Files* to group and organize profiling reports. At any given time, only one project can be open in NVIDIA Nsight Compute. Collected reports are automatically assigned to the current project. Reports stored on disk can be assigned to a project at any time. In addition to profiling reports, related files such as notes or source code can be associated with the project for future reference.

Note that only references to reports or other files are saved in the project file. Those references can become invalid, for example when associated files are deleted, removed or not available on the current system, in case the project file was moved itself.

NVIDIA Nsight Compute uses the `ncu-proj`

file extension for project files.

When no custom project is current, a *default project* is used to store e.g. the current [Start Activity Dialog](https://docs.nvidia.com/index.html#connection-dialog) entries. To remove all information from the default project, you must close NVIDIA Nsight Compute and then delete the file from disk.

On Windows, the file is located at

`<USER>\AppData\Local\NVIDIA Corporation\NVIDIA Nsight Compute\`

On Linux, the file is located at

`<USER>/.local/share/NVIDIA Corporation/NVIDIA Nsight Compute/`

On macOS, the file is located at

`<USER>/Library/Application Support/NVIDIA Corporation/NVIDIA Nsight Compute/`


### 4.17.1. Project Dialogs[#](https://docs.nvidia.com#project-dialogs)

**New Project**

Creates a new project. The project must be given a name, which will also be used for the project file. You can select the location where the project file should be saved on disk. Select whether a new directory with the project name should be created in that location.

### 4.17.2. Project Explorer[#](https://docs.nvidia.com#project-explorer)

The *Project Explorer* window allows you to inspect and manage the current project. It shows the project name as well as all *Items* (profile reports and other files) associated with it. Right-click on any entry to see further actions, such as adding, removing or grouping items. Type in the *Search project* toolbar at the top to filter the currently shown entries.

## 4.18. Visual Studio Integration Guide[#](https://docs.nvidia.com#visual-studio-integration-guide)

This guide provides information on using NVIDIA Nsight Compute within Microsoft Visual Studio, using the [NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration) Visual Studio extension, allowing for a seamless development workflow.

### 4.18.1. Visual Studio Integration Overview[#](https://docs.nvidia.com#visual-studio-integration-overview)

NVIDIA Nsight Integration is a Visual Studio extension that allows you to access the power of NVIDIA Nsight Compute from within Visual Studio.

When NVIDIA Nsight Compute is installed along with NVIDIA Nsight Integration, NVIDIA Nsight Compute activities will appear under the NVIDIA ‘Nsight’ menu in the Visual Studio menu bar. These activities launch NVIDIA Nsight Compute with the current project settings and executable.

For more information about using NVIDIA Nsight Compute from within Visual Studio, please visit

Notices

Notices

ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.

Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication of otherwise under any patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all other information previously supplied. NVIDIA Corporation products are not authorized as critical components in life support devices or systems without express written approval of NVIDIA Corporation.

Trademarks

NVIDIA and the NVIDIA logo are trademarks or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.

## Comments Page#

The

Commentspage aggregates all section comments in a single view and allows the user to edit those comments on any launch instance or section, as well as on the overall report. Comments are persisted with the report. If a section comment is added, the comment icon of the respective section in the Details Page will be highlighted.