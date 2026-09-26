source: https://docs.nvidia.com/deploy/mps/index.html

# Multi-Process Service[#](https://docs.nvidia.com#multi-process-service)

The Multi-Process Service (MPS) is a lightweight runtime service, designed to transparently enable co-operative CUDA multi-process and multi-application workflows on NVIDIA GPUs. It consists of several components:

`nvidia-cuda-mps-control`

(Control Daemon Process) – The control daemon is responsible for starting and stopping the server, as well as coordinating connections between clients and servers.`nvidia-cuda-mps-server`

(Server Process) – The server is the clients’ shared connection to the GPU and owner of the GPU scheduling resources.`libcuda.so`

(Client Runtime) – The MPS client runtime is built into the CUDA Driver library and may be used transparently by any CUDA application.

Enabling MPS provides the benefit of improved GPU utilization and reduced GPU context switching. MPS also provides memory and SM partitioning capabilities, as well as priority and dynamic resource adjustment.
To learn more, start with the [Quick Start](https://docs.nvidia.com/quick-start.html#quick-start).

MPS v3 is a new, opt-in control daemon interface that replaces the interactive shell of Legacy MPS v2 with a
scriptable module verb command syntax, named servers and namespaces, and file-based configuration. All existing
Legacy MPS v2 functionality continues to work unchanged; MPS v3 is selected explicitly, see [MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface)
for more details.

## Organization of This Document[#](https://docs.nvidia.com#organization-of-this-document)

This document is organized as follows:

**Quick Start**– describes how to get started.**When to Use MPS**– describes what factors to consider when choosing to run an application with or choosing to deploy MPS for your users.**Architecture**– describes the client-server architecture of MPS in detail and how it multiplexes clients onto the GPU.**Common Tasks**– describes how to start, stop, and administer MPS, showing the Legacy MPS v2 and MPS v3 commands side by side for each task.**Troubleshooting Guide**– lists common MPS server and client errors along with their causes and recommended actions.**Legacy MPS v2 Interface**– reference for the Legacy MPS v2 control daemon commands, environment variables, and utilities.**MPS v3 Interface**– reference for the MPS v3 command-line interface, covering servers, clients, devices, SM partitions, and features.**MPS v3 Namespaces**– explains how namespaces subdivide a server’s resources and how clients are routed to them.**MPS v3 Configuration File**– describes the TOML file used to define servers, namespaces, partitions, and features at daemon startup.**MPS v3 Memory Partitioning**– describes how MPS v3 partitions device memory across clients.**Appendix: Environment Variables**– reference for the environment variables that configure MPS clients and daemons.**Appendix: Logging**– describes the MPS log files, their contents, and their locations.

### See Also[#](https://docs.nvidia.com#see-also)

Manpage for

`nvidia-cuda-mps-control (1)`