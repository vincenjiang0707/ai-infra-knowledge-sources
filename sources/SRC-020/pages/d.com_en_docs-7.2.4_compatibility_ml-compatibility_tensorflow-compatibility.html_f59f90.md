source: https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/ml-compatibility/tensorflow-compatibility.html

# TensorFlow compatibility[#](https://rocm.docs.amd.com#tensorflow-compatibility)

2026-02-19

9 min read time

[TensorFlow](https://www.tensorflow.org/) is an open-source library for
solving machine learning, deep learning, and AI problems. It can solve many
problems across different sectors and industries, but primarily focuses on
neural network training and inference. It is one of the most popular deep
learning frameworks and is very active in open-source development.

## Support overview[#](https://rocm.docs.amd.com#support-overview)

The ROCm-supported version of TensorFlow is maintained in the official

[ROCm/tensorflow-upstream](https://github.com/ROCm/tensorflow-upstream)repository, which differs from the[tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)upstream repository.To get started and install TensorFlow on ROCm, use the prebuilt

[Docker images](https://rocm.docs.amd.com#tensorflow-docker-compat), which include ROCm, TensorFlow, and all required dependencies.See the

[ROCm TensorFlow installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/3rd-party/tensorflow-install.html)for installation and setup instructions.You can also consult the

[TensorFlow API versions](https://www.tensorflow.org/versions)list for additional context.


### Version support[#](https://rocm.docs.amd.com#version-support)

The [official TensorFlow repository](http://github.com/tensorflow/tensorflow)
includes full ROCm support. AMD maintains a TensorFlow [ROCm repository](http://github.com/rocm/tensorflow-upstream) in order to quickly add bug
fixes, updates, and support for the latest ROCm versions.

## Docker image compatibility[#](https://rocm.docs.amd.com#docker-image-compatibility)

AMD provides preconfigured Docker images with TensorFlow and the ROCm backend.
These images are published on [Docker Hub](https://hub.docker.com/r/rocm/tensorflow) and are the
recommended way to get started with deep learning with TensorFlow on ROCm.

To find the right image tag, see the [TensorFlow on ROCm installation
documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/3rd-party/tensorflow-install.html#tensorflow-docker-support) for a list of
available `rocm/tensorflow`

images.

## Critical ROCm libraries for TensorFlow[#](https://rocm.docs.amd.com#critical-rocm-libraries-for-tensorflow)

TensorFlow depends on multiple components and the supported features of those components can affect the TensorFlow ROCm supported feature set. The versions in the following table refer to the first TensorFlow version where the ROCm library was introduced as a dependency. The versions described are available in ROCm 7.2.4/7.2.3.

ROCm library |
Version |
Purpose |
Used in |
|---|---|---|---|
3.2.0 |
Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations. |
Accelerates operations like |
|
1.2.2 |
Extends hipBLAS with additional optimizations like fused kernels and integer tensor cores. |
Optimizes matrix multiplications and linear algebra operations used in layers like dense, convolutional, and RNNs in TensorFlow. |
|
4.2.0 |
Provides a C++ template library for parallel algorithms for reduction, scan, sort and select. |
Supports operations like |
|
1.0.22 |
Accelerates Fast Fourier Transforms (FFT) for signal processing tasks. |
Used for operations like signal processing, image filtering, and certain types of neural networks requiring FFT-based transformations. |
|
3.2.0 |
Provides GPU-accelerated direct linear solvers for dense and sparse systems. |
Optimizes linear algebra functions such as solving systems of linear equations, often used in optimization and training tasks. |
|
4.2.0 |
Optimizes sparse matrix operations for efficient computations on sparse data. |
Accelerates sparse matrix operations in models with sparse weight matrices or activations, commonly used in neural networks. |
|
3.5.1 |
Provides optimized deep learning primitives such as convolutions, pooling, normalization, and activation functions. |
Speeds up convolutional neural networks (CNNs) and other layers. Used
in TensorFlow for layers like |
|
2.27.7 |
Optimizes for multi-GPU communication for operations like AllReduce and Broadcast. |
Distributed data parallel training ( |
|
4.2.0 |
Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning. |
Reduction operations like |

## Supported and unsupported features[#](https://rocm.docs.amd.com#supported-and-unsupported-features)

The following section maps supported data types and GPU-accelerated TensorFlow features to their minimum supported ROCm and TensorFlow versions.

### Data types[#](https://rocm.docs.amd.com#data-types)

The data type of a tensor is specified using the `dtype`

attribute or
argument, and TensorFlow supports a wide range of data types for different use
cases.

The basic, single data types of [tf.dtypes](https://www.tensorflow.org/api_docs/python/tf/dtypes)
are as follows:

Data type |
Description |
Since TensorFlow |
Since ROCm |
|---|---|---|---|
|
16-bit bfloat (brain floating point). |
1.0.0 |
1.7 |
|
Boolean. |
1.0.0 |
1.7 |
|
128-bit complex. |
1.0.0 |
1.7 |
|
64-bit complex. |
1.0.0 |
1.7 |
|
64-bit (double precision) floating-point. |
1.0.0 |
1.7 |
|
16-bit (half precision) floating-point. |
1.0.0 |
1.7 |
|
32-bit (single precision) floating-point. |
1.0.0 |
1.7 |
|
64-bit (double precision) floating-point. |
1.0.0 |
1.7 |
|
16-bit (half precision) floating-point. |
2.0.0 |
2.0 |
|
Signed 16-bit integer. |
1.0.0 |
1.7 |
|
Signed 32-bit integer. |
1.0.0 |
1.7 |
|
Signed 64-bit integer. |
1.0.0 |
1.7 |
|
Signed 8-bit integer. |
1.0.0 |
1.7 |
|
Signed quantized 16-bit integer. |
1.0.0 |
1.7 |
|
Signed quantized 32-bit integer. |
1.0.0 |
1.7 |
|
Signed quantized 8-bit integer. |
1.0.0 |
1.7 |
|
Unsigned quantized 16-bit integer. |
1.0.0 |
1.7 |
|
Unsigned quantized 8-bit integer. |
1.0.0 |
1.7 |
|
Handle to a mutable, dynamically allocated resource. |
1.0.0 |
1.7 |
|
Variable-length string, represented as byte array. |
1.0.0 |
1.7 |
|
Unsigned 16-bit (word) integer. |
1.0.0 |
1.7 |
|
Unsigned 32-bit (dword) integer. |
1.5.0 |
1.7 |
|
Unsigned 64-bit (qword) integer. |
1.5.0 |
1.7 |
|
Unsigned 8-bit (byte) integer. |
1.0.0 |
1.7 |
|
Data of arbitrary type (known at runtime). |
1.4.0 |
1.7 |

### Features[#](https://rocm.docs.amd.com#features)

This table provides an overview of key features in TensorFlow and their availability in ROCm.

Module |
Description |
Since TensorFlow |
Since ROCm |
|---|---|---|---|
|
Operations for matrix and tensor computations, such as
|
1.4 |
1.8.2 |
|
GPU-accelerated building blocks for deep learning models, such as 2D
convolutions with |
1.0 |
1.8.2 |
|
GPU-accelerated functions for image preprocessing and augmentations,
such as resize images with |
1.1 |
1.8.2 |
|
GPU acceleration for Keras layers and models, including dense layers
( |
1.4 |
1.8.2 |
|
GPU-accelerated mathematical operations, such as sum across dimensions
with |
1.5 |
1.8.2 |
|
Functions for spectral analysis and signal transformations. |
1.13 |
2.1 |
|
GPU-accelerated data preprocessing for efficient input pipelines,
Prefetching with |
1.4 |
1.8.2 |
|
Enabling to scale computations across multiple devices on a single machine or across multiple machines. |
1.13 |
2.1 |
|
GPU-accelerated random number generation |
1.12 |
1.9.2 |
|
Enables dynamic tensor manipulation on GPUs. |
1.0 |
1.8.2 |
|
GPU-accelerated sparse matrix manipulations. |
1.9 |
1.9.0 |
|
GPU-accelerated NumPy-like API for numerical computations. |
2.4 |
4.1.1 |
|
Handling of variable-length sequences and ragged tensors with GPU support. |
1.13 |
2.1 |
|
Enable GPU-accelerated functions in optimization. |
1.14 |
2.4 |
|
Quantized operations for inference, accelerated on GPUs. |
1.12 |
1.9.2 |

### Distributed library features[#](https://rocm.docs.amd.com#distributed-library-features)

Enables developers to scale computations across multiple devices on a single machine or across multiple machines.

Feature |
Description |
Since TensorFlow |
Since ROCm |
|---|---|---|---|
|
Synchronous training across multiple workers using mirrored variables. |
2.0 |
3.0 |
|
Synchronous training across multiple GPUs on one machine. |
1.5 |
2.5 |
|
Efficiently trains models on Google TPUs. |
1.9 |
❌ |
|
Asynchronous training using parameter servers for variable management. |
2.1 |
4.0 |
|
Keeps variables on a single device and performs computation on multiple devices. |
2.3 |
4.1 |
|
Synchronous training across multiple devices and hosts. |
1.14 |
3.5 |
Distribution Strategies API |
High-level API to simplify distributed training configuration and execution. |
1.10 |
3.0 |

## Unsupported TensorFlow features[#](https://rocm.docs.amd.com#unsupported-tensorflow-features)

The following are GPU-accelerated TensorFlow features not currently supported by ROCm.

Feature |
Description |
Since TensorFlow |
|---|---|---|
Mixed Precision with TF32 |
Mixed precision with TF32 is used for matrix multiplications, convolutions, and other linear algebra operations, particularly in deep learning workloads like CNNs and transformers. |
2.4 |
|
Efficiently trains models on Google TPUs. |
1.9 |

## Use cases and recommendations[#](https://rocm.docs.amd.com#use-cases-and-recommendations)

The

[Training a Neural Collaborative Filtering (NCF) Recommender on an AMD GPU](https://rocm.blogs.amd.com/artificial-intelligence/ncf/README.html)blog post discusses training an NCF recommender system using TensorFlow. It explains how NCF improves traditional collaborative filtering methods by leveraging neural networks to model non-linear user-item interactions. The post outlines the implementation using the recommenders library, focusing on the use of implicit data (for example, user interactions like viewing or purchasing) and how it addresses challenges like the lack of negative values.The

[Creating a PyTorch/TensorFlow code environment on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/pytorch-tensorflow-env/README.html)blog post provides instructions for creating a machine learning environment for PyTorch and TensorFlow on AMD GPUs using ROCm. It covers steps like installing the libraries, cloning code repositories, installing dependencies, and troubleshooting potential issues with CUDA-based code. Additionally, it explains how to HIPify code (port CUDA code to HIP) and manage Docker images for a better experience on AMD GPUs. This guide aims to help data scientists and ML practitioners adapt their code for AMD GPUs.

For more use cases and recommendations, see the [ROCm Tensorflow blog posts](https://rocm.blogs.amd.com/blog/tag/tensorflow.html).