source: https://docs.nvidia.com/gpudirect-storage/index.html

# NVIDIA GPUDirect Storage Documentation[#](https://docs.nvidia.com#get-started)

NVIDIA Magnum IO GPUDirect Storage (GDS) enables a direct DMA path between storage and GPU memory, avoiding a bounce buffer through the CPU. Find installation instructions, programming guides, API references, tuning guidance, and release notes for both the cuFile and cuObject interfaces.

[Get Started](https://docs.nvidia.com/getting-started/index.html)
[Install GDS](https://docs.nvidia.com/troubleshooting-guide/index.html)
[Release Notes](https://docs.nvidia.com/release-notes/index.html)
[cuFile API Reference](https://docs.nvidia.com/api-reference-guide/index.html)

## Choose your interface[#](https://docs.nvidia.com#choose-your-interface)

GDS documentation is organized around two interfaces. Pick the one that matches how your application reaches storage.

File-system-based GPUDirect Storage for local and distributed storage. Start here for installation, configuration, API usage, troubleshooting, and performance guidance.

Client and server APIs for object storage solutions that use GDS data paths. Start here if you are working with object storage deployments.

## Explore the documentation[#](https://docs.nvidia.com#explore-the-documentation)

Find GPUDirect Storage documentation by workflow, feature area, or reference type.

### Installation and drivers[#](https://docs.nvidia.com#installation-and-drivers)

[Getting Started](https://docs.nvidia.com/getting-started/index.html)— set up and validate a GDS environment with sample applications.[Installation and Troubleshooting Guide](https://docs.nvidia.com/troubleshooting-guide/index.html)— install GDS and diagnose deployment problems.[nvidia-fs Kernel Driver](https://docs.nvidia.com/nvidia_fs/index.html)— requirements, installation, and verification for the`nvidia-fs`

filesystem kernel driver.[Release Notes](https://docs.nvidia.com/release-notes/index.html)— platform support, fixes, known issues, and behavior changes.

### Programming and APIs[#](https://docs.nvidia.com#programming-and-apis)

[Overview Guide](https://docs.nvidia.com/overview-guide/index.html)— the GDS programming model, architecture, and supported usage patterns.[cuFile API Reference](https://docs.nvidia.com/api-reference-guide/index.html)— detailed cuFile API behavior, parameters, and return codes.[Design Guide](https://docs.nvidia.com/design-guide/index.html)— design considerations for building GDS-enabled applications.

### Configuration and performance[#](https://docs.nvidia.com#configuration-and-performance)

[Benchmarking and Configuration Guide](https://docs.nvidia.com/configuration-guide/index.html)— tune GDS parameters and measure throughput with GDSIO.[Best Practices Guide](https://docs.nvidia.com/best-practices-guide/index.html)— recommended patterns for getting the most out of GDS.[O_DIRECT Requirements Guide](https://docs.nvidia.com/o-direct-guide/index.html)— the conditions under which file systems can use the O_DIRECT path.

### Object storage (cuObject)[#](https://docs.nvidia.com#object-storage-apis)

[cuObject Overview](https://docs.nvidia.com/cuobject/index.html)— the object storage data path and how it uses GDS.[cuObjClient API Specification](https://docs.nvidia.com/cuobject/cuObjClient-api/index.html)— client-side object storage API.[cuObjServer API Specification](https://docs.nvidia.com/cuobject/cuObjServer-api/index.html)— server-side object storage API.

## Common tasks[#](https://docs.nvidia.com#common-tasks)

Set up a new GDS environment

Begin with [Getting Started](https://docs.nvidia.com/getting-started/index.html) for the setup flow.
Then use the [Installation and Troubleshooting Guide](https://docs.nvidia.com/troubleshooting-guide/index.html) and the
[Configuration Guide](https://docs.nvidia.com/configuration-guide/index.html) to prepare and validate the deployment.

Install or verify the kernel driver

For deployments that use the filesystem kernel driver, see the
[nvidia-fs Kernel Driver](https://docs.nvidia.com/nvidia_fs/index.html) guide for hardware and software
requirements, package availability, installation steps, and verification commands.

Integrate GDS into an application

Start with the [Overview Guide](https://docs.nvidia.com/overview-guide/index.html) to understand the
programming model, then use the [cuFile API Reference](https://docs.nvidia.com/api-reference-guide/index.html)
for detailed API behavior.

Tune and validate performance

Use the [Best Practices Guide](https://docs.nvidia.com/best-practices-guide/index.html),
[Design Guide](https://docs.nvidia.com/design-guide/index.html), and
[O_DIRECT Requirements Guide](https://docs.nvidia.com/o-direct-guide/index.html) to understand deployment
considerations, performance tradeoffs, and I/O requirements.

## How to use this documentation[#](https://docs.nvidia.com#how-to-use-this-documentation)

If you are new to GPUDirect Storage, start with **cuFile** unless you are specifically working with
object storage APIs. If you already know your deployment model, use the left navigation to move
directly to the guide or reference that matches your task.

For file-system-based deployments, the typical path is **Getting Started**, then **Installation and
Troubleshooting** or **Configuration**, followed by the **cuFile API Reference** and performance
guidance as needed.

For object-storage-based deployments, start with **cuObject** and then choose the client or server API
specification based on your role in the system.