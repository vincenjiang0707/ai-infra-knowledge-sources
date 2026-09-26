source: https://docs.nvidia.com/deploy

# Deploy, monitor, and maintain NVIDIA GPUs in production

Reference documentation for driver and toolkit compatibility, GPU management and monitoring interfaces, and diagnosing GPU health, errors, and operational events on deployed systems.

## Compatibility, monitoring, and management

Plan upgrades, query GPU state, configure driver behavior, and share GPUs across processes.


### CUDA Compatibility

Using new CUDA Toolkit components on systems with older base installations, including minor version and forward compatibility.


### NVML API Reference Guide

The NVIDIA Management Library reference: a C-based API for monitoring and managing GPU device states.


### nvidia-smi

Man page for the NVIDIA System Management Interface command-line utility.


### Multi-Process Service (MPS)

Binary-compatible CUDA API implementation that lets cooperative multi-process applications, typically MPI jobs, share a GPU.


### Driver Persistence

Default kernel mode driver behavior and the options for keeping the driver persistent across GPU interactions.

## Health and diagnostics

Validate GPU health, interpret errors, and work through hardware failures.


### NVIDIA GPU Operational EventsNew

Structured operational event reporting for deployed GPUs.


### NVIDIA GPU Debug Guidelines

Error debug and diagnosis guidelines for getting servers back up and running.


### XID Errors

What Xid messages mean and how to use them when analyzing and resolving GPU problems.


### NVIDIA GPU Memory Error Management

Memory error recovery features introduced in the NVIDIA A100 and A800 GPUs.


### Dynamic Page Retirement

Automatic retirement of framebuffer pages containing degrading memory cells, and why it matters for board longevity.


### HW Field Diag

Verify GPU hardware integrity in the field. Required as part of the RMA process.


### RMA Process

The standardized process for identifying products that qualify for return merchandise authorization.


### GDS Support for NVMe Drives

Enabling GPUDirect Storage with NVMe drives using Linux PCI P2PDMA support.