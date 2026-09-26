source: https://rocm.docs.amd.com/en/latest/install/rocm-runfile-installer.html

# ROCm Runfile Installer[#](https://rocm.docs.amd.com#rocm-runfile-installer)

The ROCm Runfile Installer installs ROCm, the AMD GPU Driver, or a combination of the two on a system with or without network or internet access. Unlike all other installation methods, the ROCm Runfile Installer can install ROCm and the AMD GPU Driver without using a native Linux package management system.

The key advantage of using the ROCm Runfile Installer is its offline installation support. Many system environments have network or internet access restrictions, making installation via normal package management difficult. Furthermore, some installation environments might also have general restrictions on package management usage. Therefore, the ROCm Runfile Installer lets you perform a completely self-contained ROCm software installation.

The ROCm Runfile Installer includes these features:

An optional easy-to-use user interface for configuring the installation

An optional command line interface for the installation

Offline (air-gapped) ROCm and AMD GPU Driver installation (requires the prior installation of dependencies)

Packageless ROCm and AMD GPU Driver install without native package management

A single self-contained installer for all supported Linux distributions

Multi-architecture GPU support with selective installation and uninstall

Flexible component selection (core, development tools, SDK, OpenCL)

Graphics support option for Mesa/OpenGL workloads

Configurable installation location for the ROCm install


## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

The ROCm Runfile Installer requires the following configuration:

Installation of dependency requirements for the ROCm runtime

Installation of dependency requirements for the AMD GPU Driver (optional)

Sufficient storage space for the installation (100 GB of free space recommended)

A supported Linux distribution


## Dependency requirements[#](https://rocm.docs.amd.com#dependency-requirements)

The ROCm Runfile installer has a specific set of dependent OS-based packages that must be pre-installed on the system before you can use ROCm after the installation.

The installer can print a list of the OS packages that are missing dependencies. It can also auto-install dependencies if apt/dnf/zypper is configured to use standard network connections or an air-gapped source or mirror. Optionally when installing the OS, an air-gapped system may get these dependencies from the OS ISO files or other network installation technologies.

### Dependency list[#](https://rocm.docs.amd.com#dependency-list)

You can determine the dependent packages from the ROCm Runfile Installer [Pre-Install Configuration Settings](https://rocm.docs.amd.com#pre-install-configuration-settings) menu in the GUI or from the command line by using the `deps=list rocm`

argument for ROCm or the `deps=list amdgpu`

argument for the AMD GPU Driver (see [Dependency options](https://rocm.docs.amd.com#dependency-options)). This list, which indicates all packages required for the ROCm runtime or the AMD GPU Driver, is displayed and saved to a file named `deps_list.txt`

in the root `rocm-installer`

directory.

The `deps_list.txt`

file is not directly usable by the package manager. The file lists the packages per line indicating the name of the package or versioning required to meet the dependency requirement.
Some dependencies might show multiple packages separated by the `|`

symbol, meaning that any package from the list satisfies the package dependency. For example, the `libgcc-dev`

dependency might be `libgcc-5-dev | libgcc-7-dev`

, meaning that either `libgcc-5-dev`

or `libgcc-7-dev`

can be installed to satisfy the corresponding dependency.

### Dependency installation[#](https://rocm.docs.amd.com#dependency-installation)

You can choose to automatically install via ROCm Runfile Installer or manually install the dependency list (`deps_list.txt`

) as part of the pre-installation stage for ROCm or the AMD GPU Driver.

**Auto-installation**of the dependency list is handled by using the**Install Dependencies**option of the[Pre-Install Configuration Settings](https://rocm.docs.amd.com#pre-install-configuration-settings)menu in the GUI or from the command line using the`deps=install rocm`

or`deps=install amdgpu`

argument (see[Dependency options](https://rocm.docs.amd.com#dependency-options)). For runfile auto-install of dependencies, OS-based repositories must be properly configured for package manager usage by the installer either via standard internet connectivity or an air-gapped setup for offline installation.**Manual installation**of the dependency list require users or system administrators separately install the OS packages listed in`deps_list.txt`

.

## Supported Linux distributions[#](https://rocm.docs.amd.com#supported-linux-distributions)

The ROCm Runfile Installer supports the following Linux distributions and versions:

Ubuntu: 22.04, 24.04, 26.04

RHEL: 8.10, 9.4, 9.6, 9.8, 10.0, 10.2

SLES: 15.7, 16.0

Debian: 12, 13

Oracle Linux: 8.10, 9.8, 10.2

Rocky Linux: 9.8


Important

The new ROCm runfile installer is a universal installer that supports all listed distributions from a single
`.run`

file. There is no need to download distribution-specific builds as was required in previous versions.

## Getting started[#](https://rocm.docs.amd.com#getting-started)

The ROCm Runfile Installer is distributed as a self-extracting `.run`

file.
To install ROCm, launch the installer from any directory on the system.

### Downloading the ROCm Runfile Installer[#](https://rocm.docs.amd.com#downloading-the-rocm-runfile-installer)

Download the ROCm Runfile Installer from [repo.radeon.com](https://repo.radeon.com/) using the following command:

```
wget https://repo.radeon.com/rocm/installer/rocm-runfile-installer/rocm-rel-<rocm-version>/<installer-file>
```

Substitute values specific to your installation for the following placeholders:

```
<rocm-version> = ROCm version number for the installer (for example, 10.0)
<installer-file> = The installer .run file
```

For example, to download ROCm 10.0 of the ROCm Runfile Installer:

```
wget https://repo.radeon.com/rocm/installer/rocm-runfile-installer/rocm-rel-10.0/rocm-installer-10.0.0-4.run
```

### Running the ROCm Runfile Installer[#](https://rocm.docs.amd.com#running-the-rocm-runfile-installer)

After downloading the ROCm Runfile Installer, run it from a terminal using
[GUI install](https://rocm.docs.amd.com#gui-install) or [Command line install](https://rocm.docs.amd.com#command-line-install). See the sections below for more details.

You can obtain help, version, architecture, or component information using the following installer `.run`

file argument options:

```
bash rocm-installer-10.0.0-4.run help
bash rocm-installer-10.0.0-4.run version
bash rocm-installer-10.0.0-4.run buildinfo
bash rocm-installer-10.0.0-4.run gfx=list
bash rocm-installer-10.0.0-4.run compo=list
```

The `help`

, `version`

, `buildinfo`

, `gfx=list`

, and `compo=list`

commands run without extracting the installer contents.
For all other argument options, or if no arguments are specified, the installer `.run`

file self-extracts
to the current working directory where the `.run`

file is executing.
The self-extraction process creates a new directory named `rocm-installer`

containing the content
and tools required for the installation. The `rocm-installer`

directory also includes a `logs`

directory for recording the installation process. For more information, see [Log files](https://rocm.docs.amd.com#log-files) below.

Note

The installer self-extraction process might take a significant amount of time due to the size of the installer content and the decompression process.

## Install methods[#](https://rocm.docs.amd.com#install-methods)

The ROCm Runfile Installer provides two methods for running the ROCm installation:

[GUI install](https://rocm.docs.amd.com#gui-install): The GUI installation includes a visual interface for configuring the installation, letting you specify the pre- and post-installation requirements. In addition, the GUI provides feedback and guidance for setting up the installation. This method is recommended for new and intermediate installer users.[Command line install](https://rocm.docs.amd.com#command-line-install): The command line interface installation method provides a direct terminal-based approach for configuring and running the installation. This method is recommended for more advanced installer users and automation scenarios.

## GUI install[#](https://rocm.docs.amd.com#gui-install)

Launch the GUI-based installation of the ROCm Runfile Installer from the terminal command line without arguments as follows:

```
bash rocm-installer-10.0.0-4.run
```

### GUI[#](https://rocm.docs.amd.com#gui)

Use the Runfile Installer GUI to configure the installation, from the pre- to post-install options.

Starting from the **Main** menu, the user interface contains multiple menus and sub-menus for each stage
of the installation process.

### Using the GUI[#](https://rocm.docs.amd.com#using-the-gui)

Start the ROCm Runfile Installer user interface from the terminal and launch the **Main** menu.
While navigating through the user interface menus, use the **Done** option to return to the previous menu.
Some menus have a **Help** option to display more information about the elements within the current menu.

Follow these steps to install ROCm and the AMD GPU Driver:

**(Optional)**Install dependencies:Enter the

**Pre-Install Configuration**menu.Select the

**ROCm**checkbox,**Driver**checkbox, or both to specify the dependency type.**(Optional)**Select the**Graphics**checkbox if you need graphics support for Mesa/OpenGL workloads.If using the installer to install missing required dependencies, select

**Install Dependencies**.To manually install the required dependencies, select

**Display Dependencies**to list all the dependencies or**Validate Dependencies**to only list the missing dependencies on the current system. Quit the installer using**DONE->F1**and separately install the required dependencies, which will be listed in the`deps_list.txt`

file at the**File**location. After completing this task, restart the ROCm Runfile Installer and proceed to step 2.

Set the ROCm options:

Enter the

**ROCm Options**menu.Set

**Install ROCm**to**yes**to include ROCm components in the installation.**(Optional)**Enter the**ROCm Device**submenu to select GPU architectures. By default, the installer auto-detects your GPU.Enter the

**ROCm Components**submenu to select component categories.**(Optional)**Select**Uninstall ROCm**to uninstall a previous Runfile installation or specific architectures.Leave the

**ROCm Install Path**field set to the default location (`/opt`

) to install ROCm to`/opt/rocm/core-x.y.z`

or set the install location to a valid existing directory.

Set the AMD GPU Driver options:

Enter the

**Driver Options**menu.Set

**Install Driver**to**yes**to include the AMD GPU Driver in the installation.**(Optional)**Select**Start on install**to load the driver after installation.**(Optional)**Select**Uninstall Driver**to uninstall a previous Runfile installation.

Set the post-install options:

Set the method of enabling permission for GPU access to

**Add video,render group**or**Add udev rule**.Set the

**Post ROCm setup**to**yes**to include configuration of ROCm post-installation, which is recommended and enabled by default. Set to**no**to exclude the post-installation.


## Command line install[#](https://rocm.docs.amd.com#command-line-install)

The command line install interface can be used as an alternative to the menu-based ROCm Runfile Installer GUI to reduce user interaction during the installation and enable automation scenarios.

Run the ROCm Runfile Installer from the terminal command line as follows:

```
bash rocm-installer-10.0.0-4.run <options>
```

The `<options>`

parameter can be set to these options:

User help/information

`help`

: Displays information on how to use the ROCm Runfile Installer.`version`

: Displays the current version of the ROCm Runfile Installer.`buildinfo`

: Display ROCm build information (theRock commit, GitHub run ID, and so on).

Runfile options

`noexec`

: Disable all installer execution. Extract the`.run`

file content only.`noexec-cleanup`

: Disable cleanup after installer execution. Keep all`.run`

extracted and runtime files.

Dependencies

`deps=<arg> <compo>`

:`<arg>`

:`list <compo>`

: Lists the required dependencies for the install`<compo>`

.`validate <compo>`

: Validates which required dependencies are installed or not installed for`<compo>`

.`install-only <compo>`

: Installs the required dependencies only for`<compo>`

.`install <compo>`

: Installs with the required dependencies for`<compo>`

.

`<compo>`

: Install component (`rocm`

/`amdgpu`

/`rocm amdgpu`

).


Install

`rocm`

: Enable ROCm components install.`amdgpu`

: Enable AMD GPU Driver install.`force`

: Force the ROCm and AMD GPU Driver install.`graphics`

: Enable graphics support by installing`amdgpu-lib`

for Mesa/OpenGL.`target=<directory>`

: The target directory path for the ROCm components install (default:`/opt`

).`gfx=<arch>`

: GPU architecture to install.`<arch>`

: Architecture specification (for example,`gfx942`

,`gfx1100`

,`gfx950`

).Special values:

`gfx=all`

: Install all available architectures.`gfx=list`

: Show available architectures in the installer.`gfx=list-installed`

: Show currently installed architectures (checks`/opt`

by default; use with`target=<path>`

to check a different location).`gfx=show`

: Detect and display GPU information.

Multiple architectures:

`gfx=gfx942,gfx950`

(comma-separated).If not specified, auto-detects GPU and installs matching architecture.


`compo=<component_list>`

: Comma-separated list of ROCm components to install.Available components:

`core`

,`core-dev`

,`dev-tools`

,`core-sdk`

,`opencl`

.Default:

`core`

(if not specified).`compo=list`

: Show available component categories.Examples:

`compo=core`

,`compo=core,dev-tools`

,`compo=core-sdk`

.


Post-install

`postrocm`

: Run the post-installation ROCm configuration. By default, post-install runs automatically with`rocm`

installation. Use this to run post-install after installing with`nopostrocm`

.`nopostrocm`

: Disable post ROCm installation configuration. Use this flag to skip post-install processing.`amdgpu-start`

: Start the AMD GPU Driver after the install.`gpu-access=<access_type>`

`<access_type>`

:`user`

: Adds the current user to the`render,video`

group for GPU access.`all`

: Grants GPU access to all users on the system using`udev`

rules.



Uninstall

`uninstall-rocm (target=<directory>)`

: Uninstall ROCm.(

`target=<directory>`

): Optional target directory for the ROCm uninstall (default:`/opt/rocm/core-x.y.z`

).Multi-architecture selective uninstall:

`gfx=<arch>`

: Uninstall specific architecture (for example,`gfx=gfx1100`

).`gfx=all`

: Uninstall all architectures.Base components remain until last architecture is removed.



`uninstall-amdgpu`

: Uninstall the AMD GPU Driver.

Information/Debug

`findrocm`

: Search for a ROCm installation.`manifest`

: List the version of all ROCm components included in the installer.`manifest=<gfx>`

: List components for specific GFX architecture (for example,`manifest=gfx1100`

,`manifest=base`

).`prompt`

: Run the installer with user prompts.`assumeyes`

: Automatically answer yes to all prompts (useful for automation/scripting).`verbose`

: Run the installer with verbose logging.


Note

The installer can be used with multiple `<options>`

combinations to enable specific stages of the
ROCm install process (pre-installation and post-installation). The exception is any option that uses the
keyword `-only`

will apply that option only and no others. Some
informational options are also single-option commands.

### Command line interface[#](https://rocm.docs.amd.com#command-line-interface)

The command line interface for the ROCm Runfile Installer is based on the
`<options>`

list provided to the installer `.run`

file.

#### Basic installation examples[#](https://rocm.docs.amd.com#basic-installation-examples)

This example demonstrates how to perform a basic ROCm installation with auto-detected GPU architecture:

```
bash rocm-installer-10.0.0-4.run rocm
```

This example demonstrates how to perform a typical ROCm installation with dependencies installed, specific GPU architecture, and post-install configuration:

```
bash rocm-installer-10.0.0-4.run deps=install gfx=gfx942 rocm
```

This example demonstrates how to install ROCm to a custom location with GPU access configuration:

```
bash rocm-installer-10.0.0-4.run deps=install target="$HOME/myrocm" gfx=gfx942 rocm gpu-access=all
```

#### Multi-architecture installation examples[#](https://rocm.docs.amd.com#multi-architecture-installation-examples)

Install multiple GPU architectures:

```
bash rocm-installer-10.0.0-4.run gfx=gfx942,gfx950,gfx1100 rocm
```

Install all available architectures:

```
bash rocm-installer-10.0.0-4.run gfx=all rocm
```

#### Component selection examples[#](https://rocm.docs.amd.com#component-selection-examples)

Install core components only (default):

```
bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm
```

Install core SDK with dependencies:

```
bash rocm-installer-10.0.0-4.run deps=install compo=core-sdk gfx=gfx942 rocm
```

Install multiple components:

```
bash rocm-installer-10.0.0-4.run compo=core,dev-tools gfx=gfx942 rocm
```

#### Graphics support example[#](https://rocm.docs.amd.com#graphics-support-example)

Install with graphics support for Mesa/OpenGL:

```
bash rocm-installer-10.0.0-4.run deps=install gfx=gfx942 rocm graphics
```

#### AMD GPU Driver installation examples[#](https://rocm.docs.amd.com#amd-gpu-driver-installation-examples)

Install AMD GPU Driver only:

```
bash rocm-installer-10.0.0-4.run amdgpu
```

Install AMD GPU Driver with dependencies:

```
bash rocm-installer-10.0.0-4.run deps=install amdgpu
```

#### Combined installation examples[#](https://rocm.docs.amd.com#combined-installation-examples)

Install both ROCm and AMD GPU Driver:

```
bash rocm-installer-10.0.0-4.run deps=install gfx=gfx942 rocm amdgpu gpu-access=all
```

Install to custom location with all components:

```
bash rocm-installer-10.0.0-4.run deps=install target="$HOME/myrocm" gfx=gfx942 rocm amdgpu gpu-access=all
```

#### Runfile options[#](https://rocm.docs.amd.com#runfile-options)

The ROCm Runfile Installer is a self-extracting `.run`

file with a few options for controlling the extraction process.
When the installer `.run`

file starts execution, the extraction process begins with a checksum validation to verify
the integrity of the `.run`

file. If there are no errors, it begins extracting and decompressing the package contents.
The contents are output to a new directory named `rocm-installer`

, located in the current working directory.

Usually, when extraction and decompression are complete, execution begins automatically by either starting up the GUI
(if no arguments are provided) or executing the `rocm-installer.sh`

script with all command line arguments.
The `rocm-installer.sh`

script is in the extracted `rocm-installer`

directory.

When the GUI exits or the command line completes execution, the Runfile installer will automatically clean up the
`rocm-installer`

directory and delete all content except for the log files and the `deps_list.txt`

file.

In some cases, you might want to execute multiple commands from the same extraction and save the time required
to verify the checksum and extract and decompress the package contents of the `.run`

file.
Two command line options let you disable the `.run`

cleanup process: `noexec`

and `noexec-cleanup`

.

`noexec`

The

`noexec`

option is a single command line argument that lets the checksum and extraction process complete and then exits without starting the GUI or executing the`rocm-installer.sh`

script. All content will be maintained after the exit. You can then use the`rocm-installer.sh`

script directly from the command line without specifying the`.run`

file name.For example, extract the

`.run`

file and then use`rocm-installer.sh`

instead of`rocm-installer-10.0.0-4.run`

to install ROCm and the AMD GPU Driver separately:bash rocm-installer-10.0.0-4.run noexec cd rocm-installer bash rocm-installer.sh gfx=gfx942 rocm bash rocm-installer.sh amdgpu

Note

If the

`noexec`

option is used, all other`<options>`

on the command line will be ignored.`noexec-cleanup`

The

`noexec-cleanup`

option disables the cleanup process after the GUI or command line interface exits. Unlike the`noexec`

option, all command line arguments are processed as normal, but no content is deleted upon exit or completion. At this point, you can switch to using the`rocm-installer.sh`

script within the`rocm-installer`

directory to avoid re-extracting the contents.

#### Dependency options[#](https://rocm.docs.amd.com#dependency-options)

Like the GUI **Pre-Install Configuration** menu, the command line interface can list,
validate, and install the required dependencies. At the command line, add the `deps=<arg> <compo>`

option to the
list of `<options>`

for the `.run`

file. The `<compo>`

option can include any combination of the
`rocm`

, `amdgpu`

, and `graphics`

tags.

The `graphics`

option is intended for non-Instinct GPUs such as AMD Radeon or Ryzen GPUs/APUs to enable mixed
graphics and compute support for Mesa/OpenGL workloads.

`deps=list <rocm/amdgpu/graphics>`

This dependency option lists all the dependencies required for the

`.run`

file-based ROCm installation, AMDGPU installation, graphics support, or any combination. It lists all required (Debian or RPM) packages that require pre-installation on the system. The additional`rocm`

,`amdgpu`

, or`graphics`

parameter is a requirement for the`deps=list`

option that instructs the installer to list only the dependencies required by ROCm, the AMD GPU Driver, graphics support, or any combination.Running

`deps=list`

causes the installer to quit after listing the dependencies.`deps=list`

can combine`rocm`

,`amdgpu`

, and`graphics`

and output the combined list of required dependencies.Use

`deps=list <rocm/amdgpu/graphics>`

as a single`<options>`

parameter:bash rocm-installer-10.0.0-4.run deps=list rocm bash rocm-installer-10.0.0-4.run deps=list amdgpu bash rocm-installer-10.0.0-4.run deps=list graphics bash rocm-installer-10.0.0-4.run deps=list rocm amdgpu graphics

Note

The list of required packages can be installed separately from the Runfile Installer.

`deps=validate <rocm/amdgpu/graphics>`

This dependency option verifies whether any of the

*required*ROCm, AMD GPU Driver, or graphics support packages in the dependency list are already installed on the system running the command. The output is a list of any missing dependency packages that require installation.Running

`deps=validate`

causes the installer to quit after listing the missing dependencies.`deps=validate`

can combine`rocm`

,`amdgpu`

, and`graphics`

and output the combined list of missing dependencies.Use

`deps=validate <rocm/amdgpu/graphics>`

as a single`<options>`

parameter:bash rocm-installer-10.0.0-4.run deps=validate rocm bash rocm-installer-10.0.0-4.run deps=validate amdgpu bash rocm-installer-10.0.0-4.run deps=validate graphics bash rocm-installer-10.0.0-4.run deps=validate rocm amdgpu graphics

Note

The list of missing packages can be installed separately from the Runfile Installer.

`deps=install`

This dependency option validates and installs any required packages in the dependency list for ROCm, the AMD GPU Driver, graphics support, or any combination that are missing on the system running the command. This dependency option is not a single

`<options>`

parameter and can be added to a list of other options for the installer. The`deps=install`

option expects at least one of the`rocm`

,`amdgpu`

, or`graphics`

`<options>`

parameters to also be present in the list to enable the pre-installation of required dependencies before the Runfile Installer installs ROCm, the AMD GPU Driver, or graphics support.For example, to install the dependencies and ROCm, the command line is as follows:

bash rocm-installer-10.0.0-4.run deps=install rocm

To install the dependencies and the AMD GPU Driver, the command line is as follows:

bash rocm-installer-10.0.0-4.run deps=install amdgpu

To install the dependencies for graphics support, the command line is as follows:

bash rocm-installer-10.0.0-4.run deps=install graphics

To install the dependencies for ROCm, AMD GPU Driver, and graphics support, the command line is as follows:

bash rocm-installer-10.0.0-4.run deps=install rocm amdgpu graphics

Note

The installer can be set to only install dependencies and then quit. In this case, add

`-only`

to the`deps=install`

option:bash rocm-installer-10.0.0-4.run deps=install-only rocm bash rocm-installer-10.0.0-4.run deps=install-only amdgpu bash rocm-installer-10.0.0-4.run deps=install-only graphics bash rocm-installer-10.0.0-4.run deps=install-only rocm amdgpu graphics


#### Install options[#](https://rocm.docs.amd.com#install-options)

Like the GUI **ROCm Options** menu, the ROCm Runfile Installer can be configured to install ROCm with specific
architectures, components, and installation locations.

`rocm`

At the command line, add the

`rocm`

option to enable ROCm installation.Note

This option must be in the list of

`.run <options>`

for ROCm component installation.For example, to install ROCm with auto-detected GPU architecture:

bash rocm-installer-10.0.0-4.run rocm

`target=<directory>`

This install option is used to set the target directory where ROCm will be installed. The

`target`

option is only used as an option for ROCm installation and is not required for an AMD GPU Driver install.When

`target=<directory>`

is not specified in the`<options>`

list, the installer uses the default installation path of`/opt`

. This results in a ROCm installation at`/opt/rocm/core-x.y.z`

.You can change the default location and set the ROCm component installation directory using the

`target=<directory>`

option. The`<directory>`

argument must be a valid and absolute path to a directory on the system executing the ROCm Runfile Installer.For example, to install ROCm to the default

`/opt/rocm/core-x.y.z`

location (explicit):bash rocm-installer-10.0.0-4.run target="/opt" gfx=gfx942 rocm

To install ROCm to a directory called

`amd/myrocm`

in the`$USER`

directory:bash rocm-installer-10.0.0-4.run target="$HOME/myrocm" gfx=gfx942 rocm

`gfx=<arch>`

This install option specifies the GPU architecture to install. The installer includes architecture-specific components for different AMD GPU families.

Single architecture installation:

bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm bash rocm-installer-10.0.0-4.run gfx=gfx1100 rocm bash rocm-installer-10.0.0-4.run gfx=gfx950 rocm

Multiple architecture installation (comma-separated):

bash rocm-installer-10.0.0-4.run gfx=gfx942,gfx950,gfx1100 rocm

Install all available architectures:

bash rocm-installer-10.0.0-4.run gfx=all rocm

Auto-detect GPU (default if

`gfx=`

not specified):bash rocm-installer-10.0.0-4.run rocm

Architecture information commands:

bash rocm-installer-10.0.0-4.run gfx=show # Detect and display GPU info bash rocm-installer-10.0.0-4.run gfx=list # List available architectures bash rocm-installer-10.0.0-4.run gfx=list-installed # Show installed architectures

`compo=<component_list>`

This install option specifies which ROCm component categories to install. Components can be specified individually or as comma-separated lists.

Available components:

`core`

: Core ROCm components (default)`core-dev`

: Core development components`dev-tools`

: Developer tools`core-sdk`

: Core SDK components`opencl`

: OpenCL runtime

Single component installation:

bash rocm-installer-10.0.0-4.run compo=core gfx=gfx942 rocm bash rocm-installer-10.0.0-4.run compo=core-sdk gfx=gfx942 rocm

Multiple component installation (comma-separated):

bash rocm-installer-10.0.0-4.run compo=core,dev-tools gfx=gfx942 rocm bash rocm-installer-10.0.0-4.run compo=core-sdk,opencl gfx=gfx942 rocm

List available components:

bash rocm-installer-10.0.0-4.run compo=list

If

`compo=`

is not specified, the installer defaults to installing the`core`

component.`graphics`

This install option enables graphics support for Mesa/OpenGL workloads. When specified, the installer includes the

`amdgpu-lib`

package.bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm graphics bash rocm-installer-10.0.0-4.run deps=install gfx=gfx942 rocm graphics

`amdgpu`

At the command line, add the

`amdgpu`

option to enable AMD GPU Driver installation.Note

This option must be in the list of

`.run <options>`

for ROCm component installation. The AMD GPU Driver is installed for the currently running Linux kernel version. To install the AMD GPU Driver for a different kernel, reboot to the specific Linux kernel and reinstall the AMD GPU Driver using the runfile.For example, to install the AMD GPU Driver with no other options:

bash rocm-installer-10.0.0-4.run amdgpu

Note

Both

`rocm`

and`amdgpu`

can be combined in the`<options>`

list to install both components. For this case, the command line is as follows:bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm amdgpu

`force`

The

`force`

install option can be added to the`<options>`

list for the case of multiple pre-existing Runfile installs of ROCm. Add this option to disable any installer prompts that ask for confirmation to continue with the ROCm install if there are currently one or more Runfile ROCm installations already on the system.

#### Post-install options[#](https://rocm.docs.amd.com#post-install-options)

Similar to the GUI **Post-Install Options** menu, the post-install options can configure the ROCm Runfile Installer
to apply additional post-installation options after completing the installation.
At the command line, add one or more of the post-installation options to the `<options>`

list for the `.run`

file.

`postrocm`

This post-install option applies any post-installation configuration settings for ROCm following installation on the target system. The post-installation configuration includes any symbolic link creation, library configuration, and script execution required to use the ROCm runtime.

By default, post-install runs automatically when you use the

`rocm`

install option. You only need to explicitly use`postrocm`

in these scenarios:You installed with

`nopostrocm`

and now want to run post-install separately.You want to run post-install on an existing installation.


To run post-install separately after installing with

`nopostrocm`

:bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm nopostrocm bash rocm-installer-10.0.0-4.run postrocm

The post-install takes into account the install location of ROCm, which you may specify with the addition of the

`target=`

option. By default, if`target=`

is not provided, the default location of`/opt`

will be used to apply the post-installation:bash rocm-installer-10.0.0-4.run postrocm

For installation locations other than

`/opt`

, use the`target=`

option:bash rocm-installer-10.0.0-4.run target=/custom/path postrocm

ROCm installations using the Runfile installer can specify not only the location, but also the GPU architecture (

`gfx=`

) and ROCm components (`compo=`

). Post-installation takes this into account and will auto-detect the architectures and components installed at a location if not provided with the`postrocm`

option. However, if a user needs to specify either architecture or components, then`gfx=`

and`compo=`

options may be used with the`postrocm`

option.Run post-install with a specific architecture:

bash rocm-installer-10.0.0-4.run gfx=gfx942 postrocm

Run post-install with a specific component:

bash rocm-installer-10.0.0-4.run compo=core-sdk postrocm

Note

Adding the

`postrocm`

option (or relying on the default behavior with`rocm`

) is highly recommended to guarantee proper functioning of the ROCm components and applications.`nopostrocm`

This post-install option disables the automatic post-install configuration that normally runs when you use the

`rocm`

install option. Use this when you want to install ROCm without running the post-install scripts.bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm nopostrocm

You can run the post-install later using the

`postrocm`

option (see above).`gpu-access=<access_type>`

This post-install option sets the GPU resource access permissions. ROCm runtime libraries and applications might need access to the GPU. This requires setting the access permission to the

`video`

and`render`

groups using the`<access_type>`

.If the ROCm installation is for a single user, then set the

`<access_type>`

for the`gpu-access`

option to`user`

.For example, to add the current user (

`$USER`

) to the`video,render`

group for GPU access for a ROCm installation, the command line is as follows:bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm gpu-access=user

In cases where a system administrator is installing ROCm for multiple users, they might want to enable GPU access permission for all users. For this case, set the

`<access_type>`

for the`gpu-access`

option to`all`

:bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm gpu-access=all

Note

Adding the

`gpu-access`

option to the`<options>`

list is recommended for using ROCm. A typical ROCm installation includes one of the`gpu-access`

types.

#### Uninstall options[#](https://rocm.docs.amd.com#uninstall-options)

These options configure the ROCm Runfile Installer to uninstall a previous ROCm or AMD GPU Driver installation.

`uninstall-rocm (target=<directory>) (gfx=<arch>)`

This option configures the ROCm Runfile Installer to uninstall a previous ROCm installation. For multi-architecture installations, you can selectively uninstall specific architectures or all architectures.

Uninstall with auto-detection of architecture:

To uninstall ROCm from the default location (

`/opt/rocm/core-x.y.z`

):bash rocm-installer-10.0.0-4.run uninstall-rocm

To uninstall ROCm from a custom location:

bash rocm-installer-10.0.0-4.run target="$HOME/myrocm/rocm-x.y.z" uninstall-rocm

Uninstall with architecture selection:

Selective uninstall of one or more GPU architectures installed to a location. Using

`gfx=`

, you can specify the architecture or architectures to uninstall. Only gfx-specific components will be removed for multi-installs, with common components remaining until the final architecture is uninstalled.To uninstall a specific architecture:

bash rocm-installer-10.0.0-4.run gfx=gfx1100 uninstall-rocm bash rocm-installer-10.0.0-4.run target="$HOME/myrocm" gfx=gfx942 uninstall-rocm

To uninstall all architectures:

bash rocm-installer-10.0.0-4.run gfx=all uninstall-rocm


Note

The

`uninstall-rocm`

option can only remove ROCm if it was installed using the ROCm Runfile Installer. Traditional package-based ROCm installs will not be removed.`uninstall-amdgpu`

This option configures the ROCm Runfile Installer to uninstall a previous AMD GPU Driver installation.

To uninstall the AMD GPU Driver from the system, use the following command line:

bash rocm-installer-10.0.0-4.run uninstall-amdgpu

Note

The

`uninstall-amdgpu`

option can only remove the AMD GPU Driver if it was installed using the ROCm Runfile Installer. Traditional package-based AMD GPU Driver installs will not be removed.

#### Information and debug options[#](https://rocm.docs.amd.com#information-and-debug-options)

The ROCm Runfile Installer command line interface includes options for information output or debugging.

`findrocm`

This information option searches the install system for any existing installations of ROCm. Any install locations are output to the terminal and the type of installation is indicated (Runfile or Package manager).

Use

`findrocm`

as a standalone`<options>`

parameter:bash rocm-installer-10.0.0-4.run findrocm

`manifest`

This information option lists the version of each ROCm component included in the installer. The

`manifest`

option causes the Runfile Installer to quit after listing the ROCm components.Use

`manifest`

as a standalone`<options>`

parameter:bash rocm-installer-10.0.0-4.run manifest

To list components for a specific architecture:

bash rocm-installer-10.0.0-4.run manifest=gfx942 bash rocm-installer-10.0.0-4.run manifest=gfx1100 bash rocm-installer-10.0.0-4.run manifest=base

`buildinfo`

This information option displays theRock build information, including commit hash, GitHub run ID, build date, and other build metadata.

Use

`buildinfo`

as a standalone`<options>`

parameter:bash rocm-installer-10.0.0-4.run buildinfo

`prompt`

This debug option enables user prompts in the installer. At specific, critical points of the installation process, the installer halts execution and prompts the user to either continue with the install or exit.

`assumeyes`

This automation option automatically answers yes to all prompts. This is useful for automation and scripting scenarios where user interaction is not desired.

bash rocm-installer-10.0.0-4.run deps=install gfx=gfx942 rocm assumeyes

`verbose`

This debug option enables verbose logging during ROCm Runfile Installer execution.

For example, to install ROCm with user prompts and verbose logging:

bash rocm-installer-10.0.0-4.run target="/opt" gfx=gfx942 rocm prompt verbose


## Log files[#](https://rocm.docs.amd.com#log-files)

By default, the ROCm Runfile Installer GUI and command line interfaces record the output execution in log files.
These log files are created in the `rocm-installer/logs`

directory.

The `rocm-installer`

directory is created when the ROCm Runfile Installer self-extracts
to the current working directory where it is being executed.

## Troubleshooting[#](https://rocm.docs.amd.com#troubleshooting)

The following are common issues and solutions for the ROCm Runfile Installer.

**Issue:**Installer fails with “missing dependencies” error**Solution:**Use`deps=validate rocm`

to see which dependencies are missing, then either:Install them manually using your package manager

Use

`deps=install rocm`

to have the installer install them (requires internet connection)

**Issue:**GPU not detected or wrong architecture selected**Solution:**Use`gfx=show`

to see detected GPUs, then manually specify the correct architecture:bash rocm-installer-10.0.0-4.run gfx=gfx942 rocm

**Issue:**Post-install configuration was skipped**Solution:**Run post-install separately:bash rocm-installer-10.0.0-4.run postrocm

**Issue:**Cannot access GPU after installation**Solution:**Ensure GPU access permissions are set. Either:Add your user to the video/render groups:

`bash rocm-installer-10.0.0-4.run gpu-access=user`

Grant access to all users:

`bash rocm-installer-10.0.0-4.run gpu-access=all`

Log out and log back in for group membership changes to take effect


**Issue:**Multi-architecture installation conflicts**Solution:**Check installed architectures:

`bash rocm-installer-10.0.0-4.run gfx=list-installed`

Remove specific architecture if needed:

`bash rocm-installer-10.0.0-4.run gfx=gfx1100 uninstall-rocm`

Reinstall with correct architecture selection