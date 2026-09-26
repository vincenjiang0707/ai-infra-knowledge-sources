source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/system-setup/system-health-check.html

# System health benchmarks for AI workloads[#](https://rocm.docs.amd.com#system-health-benchmarks-for-ai-workloads)

2026-02-19

2 min read time

Before running AI workloads, it is important to validate that your AMD hardware is configured correctly and is performing optimally. This topic outlines several system health benchmarks you can use to test key aspects like GPU compute capabilities (FLOPS), memory bandwidth, and interconnect performance. Many of these tests are part of the ROCm Validation Suite (RVS).

## ROCm Validation Suite (RVS) tests[#](https://rocm.docs.amd.com#rocm-validation-suite-rvs-tests)

RVS provides a collection of tests, benchmarks, and qualification tools, each targeting a specific subsystem of the system under test. It includes tests for GPU stress and memory bandwidth.

### Install ROCm Validation Suite[#](https://rocm.docs.amd.com#install-rocm-validation-suite)

To get started, install RVS. For example, on an Ubuntu system with ROCm already installed, run the following command:

```
sudo apt update
sudo apt install rocm-validation-suite
```

See the [ROCm Validation Suite installation instructions](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/install/installation.html),
and [System validation tests](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html)
in the Instinct documentation for more detailed instructions.

### Benchmark, stress, and qualification tests[#](https://rocm.docs.amd.com#benchmark-stress-and-qualification-tests)

The GPU stress test runs various GEMM computations as workloads to stress the GPU FLOPS performance and check whether it meets the configured target GFLOPS.

Run the benchmark, stress, and qualification tests included with RVS. See the [Benchmark, stress, qualification](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html#benchmark-stress-qualification)
section of the Instinct documentation for usage instructions.

### BabelStream test[#](https://rocm.docs.amd.com#babelstream-test)

BabelStream is a synthetic GPU benchmark based on the STREAM benchmark for
CPUs, measuring memory transfer rates to and from global device memory.
BabelStream tests are included with the RVS package as part of the [BABEL module](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/conceptual/rvs-modules.html#babel-benchmark-test-babel-module).

For more information, see [Performance benchmarking](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html#babelstream)
in the Instinct documentation.

## RCCL tests[#](https://rocm.docs.amd.com#rccl-tests)

The ROCm Communication Collectives Library (RCCL) enables efficient multi-GPU
communication. The [ROCm/rccl-tests](https://github.com/ROCm/rccl-tests) suite benchmarks
the performance and verifies the correctness of these collective operations.
This helps ensure optimal scaling for multi-GPU tasks.

To get started, build RCCL-tests using the official instructions in the README at

[ROCm/rccl-tests](https://github.com/ROCm/rccl-tests?tab=readme-ov-file#build)or use the following commands:git clone https://github.com/ROCm/rccl-tests.git cd rccl-tests make

Run the suggested RCCL tests – see

[RCCL benchmarking](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/network/rdma-benchmarking.html#rccl-benchmarking-results)in the AMD Instinct customer acceptance guide.

## TransferBench test[#](https://rocm.docs.amd.com#transferbench-test)

TransferBench is a standalone utility for benchmarking simultaneous data transfer performance between various devices in the system, including CPU-to-GPU and GPU-to-GPU (peer-to-peer). This helps identify potential bottlenecks in data movement between the host system and the GPUs, or between GPUs, which can impact end-to-end latency.

To get started, use the instructions in the

[TransferBench documentation](https://rocm.docs.amd.com/projects/TransferBench/en/latest/install/install.html#install-transferbench)or use the following commands:git clone https://github.com/ROCm/TransferBench.git cd TransferBench CC=hipcc make

Run the suggested TransferBench tests – see

[TransferBench benchmarking](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/common/system-validation.html#transferbench)in the Instinct performance benchmarking documentation for instructions.