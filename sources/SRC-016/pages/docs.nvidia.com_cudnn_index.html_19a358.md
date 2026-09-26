source: https://docs.nvidia.com/cudnn/index.html

The [NVIDIA CUDA](https://developer.nvidia.com/cudnn)®[ Deep Neural Network (cuDNN)](https://developer.nvidia.com/cudnn) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, attention, matmul, pooling, and normalization.

Current status, software versions, and known issues for NVIDIA cuDNN.

This document provides step-by-step instructions on how to install NVIDIA cuDNN.


This library is a context-based API that allows for easy multi-threading and (optional) interoperability with CUDA streams. This API lists the data types and API functions per sub-library.

This document explains how to use the NVIDIA cuDNN library. While the NVIDIA cuDNN Library API provides per-function API documentation, the Developer Guide gives a more informal end-to-end story about cuDNN’s key capabilities and how to use them.


This document describes the error reporting and API logging utilities for recording the cuDNN API execution and error information. It also helps answer the most commonly asked questions regarding typical use cases.

This document lists the supported versions of the OS, NVIDIA CUDA, the CUDA driver, and the hardware for the latest NVIDIA cuDNN release.


This document contains specific license terms and conditions for NVIDIA cuDNN. By accepting this agreement, you agree to comply with all the terms and conditions applicable to the specific product(s) included herein.


Click on the green buttons that describe your target platform. Only supported platforms will be shown.

The cuDNN Frontend (FE) API is a C++ header-only library that wraps the

[cuDNN C backend API](https://docs.nvidia.com/deeplearning/cudnn/api/cudnn-graph-library.html#backend-descriptor-types). Both the FE and backend APIs are entry points to the same set of functionality that is commonly referred to as the "[graph API](https://docs.nvidia.com/deeplearning/cudnn/developer/graph-api.html)".
Join the NVIDIA Developer Program.

Explore cuDNN forums.

Access the latest NVIDIA cuDNN announcements, news, downloads, and training.

Find more news and tutorials.