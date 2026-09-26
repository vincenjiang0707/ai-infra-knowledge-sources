source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/system-setup/index.html

# System setup for AI workloads on ROCm[#](https://rocm.docs.amd.com#system-setup-for-ai-workloads-on-rocm)

2026-02-19

1 min read time

Before you begin training or inference on AMD Instinct™ GPUs, complete the following system setup and validation steps to ensure optimal performance.

## Prerequisite system validation[#](https://rocm.docs.amd.com#prerequisite-system-validation)

First, confirm that your system meets all software and hardware prerequisites.
See [Prerequisite system validation before running AI workloads](https://rocm.docs.amd.com/prerequisite-system-validation.html).

## Docker images for AMD Instinct GPUs[#](https://rocm.docs.amd.com#docker-images-for-amd-instinct-gpus)

AMD provides prebuilt Docker images for AMD Instinct™ MI300X and MI325X GPUs. These images include ROCm-enabled deep learning frameworks and essential software components. They support single-node and multi-node configurations and are ready for training and inference workloads out of the box.

### Multi-node training[#](https://rocm.docs.amd.com#multi-node-training)

For instructions on enabling multi-node training, see [Multi-node setup for AI workloads](https://rocm.docs.amd.com/multi-node-setup.html).

## System optimization and validation[#](https://rocm.docs.amd.com#system-optimization-and-validation)

Before running workloads, verify that the system is configured correctly and operating at peak efficiency. Recommended steps include:

Disabling NUMA auto-balancing

Running system benchmarks to validate hardware performance


For details on running system health checks, see [System health benchmarks for AI workloads](https://rocm.docs.amd.com/system-health-check.html).