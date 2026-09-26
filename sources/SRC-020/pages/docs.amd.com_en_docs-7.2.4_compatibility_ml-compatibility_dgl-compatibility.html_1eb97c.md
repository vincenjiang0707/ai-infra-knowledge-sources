source: https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/ml-compatibility/dgl-compatibility.html

# DGL compatibility[#](https://rocm.docs.amd.com#dgl-compatibility)

2026-02-19

6 min read time

Deep Graph Library ([DGL](https://www.dgl.ai/)) is an easy-to-use, high-performance, and scalable
Python package for deep learning on graphs. DGL is framework agnostic, meaning
that if a deep graph model is a component in an end-to-end application, the rest of
the logic is implemented using PyTorch.

DGL provides a high-performance graph object that can reside on either CPUs or GPUs. It bundles structural data features for better control and provides a variety of functions for computing with graph objects, including efficient and customizable message passing primitives for Graph Neural Networks.

## Support overview[#](https://rocm.docs.amd.com#support-overview)

The ROCm-supported version of DGL is maintained in the official

[ROCm/dgl](https://github.com/ROCm/dgl)repository, which differs from the[dmlc/dgl](https://github.com/dmlc/dgl)upstream repository.To get started and install DGL on ROCm, use the prebuilt

[Docker images](https://rocm.docs.amd.com#dgl-docker-compat), which include ROCm, DGL, and all required dependencies.See the

[ROCm DGL installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/3rd-party/dgl-install.html)for installation and setup instructions.You can also consult the upstream

[Installation guide](https://www.dgl.ai/pages/start.html)for additional context.


## Compatibility matrix[#](https://rocm.docs.amd.com#compatibility-matrix)

AMD validates and publishes [DGL images](https://hub.docker.com/r/rocm/dgl/tags)
with ROCm backends on Docker Hub. The following Docker image tags and associated
inventories represent the latest available DGL version from the official Docker Hub.
Click the to view the image on Docker Hub.

## Key ROCm libraries for DGL[#](https://rocm.docs.amd.com#key-rocm-libraries-for-dgl)

DGL on ROCm depends on specific libraries that affect its features and performance. Using the DGL Docker container or building it with the provided Docker file or a ROCm base image is recommended. If you prefer to build it yourself, ensure the following dependencies are installed:

ROCm library |
ROCm 7.0.0 Version |
ROCm 6.4.x Version |
Purpose |
|---|---|---|---|
1.1.0 |
1.1.0 |
Enables faster execution of core operations like matrix multiplication (GEMM), convolutions and transformations. |
|
3.0.0 |
2.4.0 |
Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations. |
|
1.0.0 |
0.12.0 |
hipBLASLt is an extension of the hipBLAS library, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores. |
|
4.0.0 |
3.4.0 |
Provides a C++ template library for parallel algorithms for reduction, scan, sort and select. |
|
1.0.20 |
1.0.18 |
Provides GPU-accelerated Fast Fourier Transform (FFT) operations. |
|
3.0.0 |
2.12.0 |
Provides fast random number generation for GPUs. |
|
3.0.0 |
2.4.0 |
Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD). |
|
4.0.1 |
3.2.0 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
|
0.2.4 |
0.2.3 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
|
2.0.0 |
1.5.0 |
Optimizes for high-performance tensor operations, such as contractions. |
|
3.5.0 |
3.4.0 |
Optimizes deep learning primitives such as convolutions, pooling, normalization, and activation functions. |
|
2.13.0 |
2.12.0 |
Adds graph-level optimizations, ONNX models and mixed precision support and enable Ahead-of-Time (AOT) Compilation. |
|
3.3.0 |
3.2.0 |
Optimizes acceleration for computer vision and AI workloads like preprocessing, augmentation, and inferencing. |
|
3.3.0 |
2.2.0 |
Accelerates the data pipeline by offloading intensive preprocessing and augmentation tasks. rocAL is part of MIVisionX. |
|
2.26.6 |
2.22.3 |
Optimizes for multi-GPU communication for operations like AllReduce and Broadcast. |
|
1.0.0 |
0.10.0 |
Provides hardware-accelerated data decoding capabilities, particularly for image, video, and other dataset formats. |
|
1.1.0 |
0.8.0 |
Provides hardware-accelerated JPEG image decoding and encoding. |
|
2.0.0 |
1.9.10 |
Speeds up data augmentation, transformation, and other preprocessing steps. |
|
4.0.0 |
3.3.0 |
Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning. |
|
2.0.0 |
1.7.0 |
Accelerates warp-level matrix-multiply and matrix-accumulate to speed up matrix multiplication (GEMM) and accumulation operations with mixed precision support. |

## Supported features with ROCm 7.0.0[#](https://rocm.docs.amd.com#supported-features-with-rocm-7-0-0)

Many functions and methods available upstream are also supported in DGL on ROCm. Instead of listing them all, support is grouped into the following categories to provide a general overview.

DGL Base

DGL Backend

DGL Data

DGL Dataloading

DGL Graph

DGL Function

DGL Ops

DGL Sampling

DGL Transforms

DGL Utils

DGL Distributed

DGL Geometry

DGL Mpops

DGL NN

DGL Optim

DGL Sparse

GraphBolt


## Unsupported features with ROCm 7.0.0[#](https://rocm.docs.amd.com#unsupported-features-with-rocm-7-0-0)

TF32 Support (only supported for PyTorch 2.7 and above)

Kineto/ROCTracer integration


## Unsupported functions with ROCm 7.0.0[#](https://rocm.docs.amd.com#unsupported-functions-with-rocm-7-0-0)

`bfs`

`format`

`multiprocess_sparse_adam_state_dict`

`half_spmm`

`segment_mm`

`gather_mm_idx_b`

`sample_labors_prob`

`sample_labors_noprob`

`sparse_admin`


## Use cases and recommendations[#](https://rocm.docs.amd.com#use-cases-and-recommendations)

DGL can be used for Graph Learning, and building popular graph models like GAT, GCN, and GraphSage. Using these models, a variety of use cases are supported:

Recommender systems

Network Optimization and Analysis

1D (Temporal) and 2D (Image) Classification

Drug Discovery


For use cases and recommendations, refer to the [AMD ROCm blog](https://rocm.blogs.amd.com/),
where you can search for DGL examples and best practices to optimize your workloads on AMD GPUs.

Although multiple use cases of DGL have been tested and verified, a few have been outlined in the

[DGL in the Real World: Running GNNs on Real Use Cases](https://rocm.blogs.amd.com/artificial-intelligence/dgl_blog2/README.html)blog post, which walks through four real-world graph neural network (GNN) workloads implemented with the Deep Graph Library on ROCm. It covers tasks ranging from heterogeneous e-commerce graphs and multiplex networks (GATNE) to molecular graph regression (GNN-FiLM) and EEG-based neurological diagnosis (EEG-GCNN). For each use case, the authors detail: the dataset and task, how DGL is used, and their experience porting to ROCm. It is shown that DGL codebases often run without modification, with seamless integration of graph operations, message passing, sampling, and convolution.The

[Graph Neural Networks (GNNs) at Scale: DGL with ROCm on AMD Hardware](https://rocm.blogs.amd.com/artificial-intelligence/why-graph-neural/README.html)blog post introduces the Deep Graph Library (DGL) and its enablement on the AMD ROCm platform, bringing high-performance graph neural network (GNN) training to AMD GPUs. DGL bridges the gap between dense tensor frameworks and the irregular nature of graph data through a graph-first, message-passing abstraction. Its design ensures scalability, flexibility, and interoperability across frameworks like PyTorch and TensorFlow. AMD’s ROCm integration enables DGL to run efficiently on HIP-based GPUs, supported by prebuilt Docker containers and open-source repositories. This marks a major step in AMD’s mission to advance open, scalable AI ecosystems beyond traditional architectures.

You can pre-process datasets and begin training on AMD GPUs through:

Single-GPU training/inference

Multi-GPU training


## Previous versions[#](https://rocm.docs.amd.com#previous-versions)

See [DGL version history](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/3rd-party/previous-versions/dgl-history.html) to find documentation for previous releases
of the `ROCm/dgl`

Docker image.