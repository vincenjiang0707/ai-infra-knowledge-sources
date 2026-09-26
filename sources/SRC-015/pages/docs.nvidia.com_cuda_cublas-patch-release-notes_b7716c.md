source: https://docs.nvidia.com/cuda/cublas-patch-release-notes/

cuBLAS Patches - Release Notes

# 1. Overview[](https://docs.nvidia.com#overview)

This section lists cuBLAS patch releases that were issued separately from CUDA Toolkit major and minor releases. Each entry describes the resolved issues included in that patch release.

## 1.1. cuBLAS: Patch Release 13.6.2[](https://docs.nvidia.com#cublas-patch-release-13-6-2)

**Applies to CUDA Toolkit 13.3 Update 1**

**Resolved Issues**Fixed an issue where cuBLASLt Grouped GEMM operations with

`CUBLAS_POINTER_MODE_HOST`

could produce incorrect results on Hopper GPUs when the number of waves was larger than 2. Introduced in CUDA Toolkit 13.2 Update 1 (cuBLAS 13.4.0). [*6681084*]Fixed an issue where

`cublasLtMatmul()`

could produce incorrect results on B300 and Rubin GPUs when the input matrices used the NVFP4 data type. This affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

and`CUBLASLT_ALGO_CONFIG_STAGES_ID`

equal to`CUBLASLT_MATMUL_STAGES_768xAUTO`

. [*CUB-10573*]


## 1.2. cuBLAS: Patch Release 13.6.1[](https://docs.nvidia.com#cublas-patch-release-13-6-1)

**Applies to CUDA Toolkit 13.3 Update 1**

**Resolved Issues**Fixed an issue where the cuBLASLt heuristics for the Grouped GEMM API returned sub-optimal algorithms when the C and D matrices had ordering

`CUBLASLT_ORDER_ROW`

. Introduced in CUDA Toolkit 13.3 Update 1 (cuBLAS 13.6.0). [*6335555*]Fixed an issue where executing multiple cuBLASLt Grouped GEMM operations that reused workspace on Hopper could lead to hangs or unspecified launch failures. Introduced in CUDA Toolkit 13.2 Update 1 (cuBLAS 13.4.0). [

*6456362*]Fixed an issue where using

`cublasLtMatmulAlgoGetHeuristic()`

while a non-default blocking stream was being captured resulted in`CUDNN_STATUS_INTERNAL_ERROR`

. Introduced in CUDA Toolkit 13.3 (cuBLAS 13.5.1). [*6288786*]Fixed an issue where GEMV-like operations (

`cublas<t>gemv()`

,`cublasLtMatmul()`

with M or N equal to 1, and so on) could return`CUBLAS_STATUS_NOT_SUPPORTED`

for certain shapes and workspace configurations. Introduced in CUDA Toolkit 13.3 (cuBLAS 13.5.1). [*6435705, 6418535*]Fixed an issue where strided batched GEMM operations using broadcast operands could perform out-of-bounds memory reads on sm120 and sm121 GPUs. This occurred when an input matrix shared across batches (through zero or overlapping strides) was smaller than a few hundred KB. While numerical accuracy remained unaffected, these invalid accesses could trigger compute-sanitizer warnings or, in rare instances, result in illegal memory access errors. Introduced in CUDA Toolkit 13.0 Update 2 (cuBLAS 13.1.0). [

*6040940, 5996751*]Fixed an issue where cuBLAS GEMM kernels on sm10x and sm12x might access device alpha and beta pointers before calling

`cudaGridDependencySynchronize()`

. This could result in a WAR hazard if the preceding PDL kernel produced alpha and beta values on the device after calling`cudaTriggerProgrammaticLaunchCompletion()`

. Introduced in CUDA Toolkit 13.0 Update 2 (cuBLAS 13.1.0). [*CUB-10409*]Fixed an issue where GEMV-like operations (

`cublas<t>gemv()`

,`cublasLtMatmul()`

with M or N equal to 1, and so on) could return incorrect results on sm120 and sm121 GPUs. This occurred when the matrix was transposed, its non-accumulation dimension was larger than 3145680, and`beta`

was not 0. Introduced in CUDA Toolkit 13.3 Update 1 (cuBLAS 13.6.0). [*CUB-10445*]


## 1.3. cuBLAS: Patch Release 13.4.2[](https://docs.nvidia.com#cublas-patch-release-13-4-2)

**Applies to CUDA Toolkit 13.2 Update 2**

**Resolved Issues**Fixed an issue where cuBLASLt Grouped GEMM operations with

`CUBLAS_POINTER_MODE_HOST`

could produce incorrect results on Hopper GPUs when the number of waves was larger than 2. Introduced in CUDA Toolkit 13.2 Update 1 (cuBLAS 13.4.0). [*6681084*]


## 1.4. cuBLAS: Patch Release 13.4.1[](https://docs.nvidia.com#cublas-patch-release-13-4-1)

**Applies to CUDA Toolkit 13.2 Update 1**

**Resolved Issues**Fixed an issue where

`cublasLtMatmul()`

ignored the tensor-wide scaling value specified by`CUBLASLT_MATMUL_DESC_D_SCALE_POINTER`

for NVFP4 matrix multiplications with NVFP4 output, resulting in incorrect results. This affected algorithms with`CUBLASLT_ALGO_CONFIG_ID = 66`

on GPUs with compute capability 10.x and 11.x. Introduced in CUDA Toolkit 13.2 Update 1 (cuBLAS 13.4.0). [6059292]


## 1.5. cuBLAS: Patch Release 13.2.2[](https://docs.nvidia.com#cublas-patch-release-13-2-2)

**Applies to CUDA Toolkit 13.1 Update 1**

**Resolved Issues**Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results when it ran concurrently with another kernel that used Tensor Memory. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

on GPUs with Compute Capability 10.x and 11.x, and had existed since cuBLAS 12.8. [*5807900, 5943783*]Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results or invalid memory access errors for large leading dimensions, specifically when the product of the data type size and the leading dimension of a matrix exceeded the bounds of a signed 32-bit integer. This issue affected GPUs with Compute Capability 9.0, 10.x, and 11.0, had existed since cuBLAS 12.6 Update 2, and affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9572*]Fixed an issue in the cuBLASLt Matmul API that caused FP8 kernels to hang on GPUs with Compute Capability 9.0 when

`beta != 0`

and`scale_C = 0`

. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9627*]Fixed an issue where some

`ztrmm`

kernels produced incorrect results when`m = 1`

and`side = r`

on NVIDIA Ada and Blackwell GeForce-class GPUs. [*5452663*]


## 1.6. cuBLAS: Patch Release 13.1.1[](https://docs.nvidia.com#cublas-patch-release-13-1-1)

**Applies to CUDA Toolkit 13.0 Update 2**

**Resolved Issues**Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results when it ran concurrently with another kernel that used Tensor Memory. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

on GPUs with Compute Capability 10.x and 11.x, and had existed since cuBLAS 12.8. [*5807900, 5943783*]Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results or invalid memory access errors for large leading dimensions, specifically when the product of the data type size and the leading dimension of a matrix exceeded the bounds of a signed 32-bit integer. This issue affected GPUs with Compute Capability 9.0, 10.x, and 11.0, had existed since cuBLAS 12.6 Update 2, and affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9572*]Fixed an issue in the cuBLASLt Matmul API that caused FP8 kernels to hang on GPUs with Compute Capability 9.0 when

`beta != 0`

and`scale_C = 0`

. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9627*]Fixed an issue where some

`ztrmm`

kernels produced incorrect results when`m = 1`

and`side = r`

on NVIDIA Ada and Blackwell GeForce-class GPUs. [*5452663*]


## 1.7. cuBLAS: Patch Release 12.9.2[](https://docs.nvidia.com#cublas-patch-release-12-9-2)

**Applies to CUDA Toolkit 12.9 Update 1**

**Resolved Issues**Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results when it ran concurrently with another kernel that used Tensor Memory. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

on GPUs with Compute Capability 10.x and 11.x, and had existed since cuBLAS 12.8. [*5807900, 5943783*]Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results or invalid memory access errors for large leading dimensions, specifically when the product of the data type size and the leading dimension of a matrix exceeded the bounds of a signed 32-bit integer. This issue affected GPUs with Compute Capability 9.0, 10.x, and 11.0, had existed since cuBLAS 12.6 Update 2, and affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9572*]Fixed an issue in the cuBLASLt Matmul API that caused FP8 kernels to hang on GPUs with Compute Capability 9.0 when

`beta != 0`

and`scale_C = 0`

. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9627*]Fixed an issue where some

`ztrmm`

kernels produced incorrect results when`m = 1`

and`side = r`

on NVIDIA Ada and Blackwell GeForce-class GPUs. [*5452663*]


## 1.8. cuBLAS: Patch Release 12.8.5[](https://docs.nvidia.com#cublas-patch-release-12-8-5)

**Applies to CUDA Toolkit 12.8 Update 1**

**Resolved Issues**Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results when it ran concurrently with another kernel that used Tensor Memory. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

on GPUs with Compute Capability 10.x and 11.x, and had existed since cuBLAS 12.8. [*5807900, 5943783*]Fixed an issue in

`cublasLtMatmul()`

that could lead to incorrect results or invalid memory access errors for large leading dimensions, specifically when the product of the data type size and the leading dimension of a matrix exceeded the bounds of a signed 32-bit integer. This issue affected GPUs with Compute Capability 9.0, 10.x, and 11.0, had existed since cuBLAS 12.6 Update 2, and affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9572*]Fixed an issue in the cuBLASLt Matmul API that caused FP8 kernels to hang on GPUs with Compute Capability 9.0 when

`beta != 0`

and`scale_C = 0`

. This issue affected only algorithms with`CUBLASLT_ALGO_CONFIG_ID`

equal to`66`

. [*CUB-9627*]Fixed an issue where some

`ztrmm`

kernels produced incorrect results when`m = 1`

and`side = r`

on NVIDIA Ada and Blackwell GeForce-class GPUs. [*5452663*]


# 2. Notices[](https://docs.nvidia.com#notices)

## 2.1. Notice[](https://docs.nvidia.com#notice)

This document is provided for information purposes only and shall not be regarded as a warranty of a certain functionality, condition, or quality of a product. NVIDIA Corporation (“NVIDIA”) makes no representations or warranties, expressed or implied, as to the accuracy or completeness of the information contained in this document and assumes no responsibility for any errors contained herein. NVIDIA shall have no liability for the consequences or use of such information or for any infringement of patents or other rights of third parties that may result from its use. This document is not a commitment to develop, release, or deliver any Material (defined below), code, or functionality.

NVIDIA reserves the right to make corrections, modifications, enhancements, improvements, and any other changes to this document, at any time without notice.

Customer should obtain the latest relevant information before placing orders and should verify that such information is current and complete.

NVIDIA products are sold subject to the NVIDIA standard terms and conditions of sale supplied at the time of order acknowledgement, unless otherwise agreed in an individual sales agreement signed by authorized representatives of NVIDIA and customer (“Terms of Sale”). NVIDIA hereby expressly objects to applying any customer general terms and conditions with regards to the purchase of the NVIDIA product referenced in this document. No contractual obligations are formed either directly or indirectly by this document.

NVIDIA products are not designed, authorized, or warranted to be suitable for use in medical, military, aircraft, space, or life support equipment, nor in applications where failure or malfunction of the NVIDIA product can reasonably be expected to result in personal injury, death, or property or environmental damage. NVIDIA accepts no liability for inclusion and/or use of NVIDIA products in such equipment or applications and therefore such inclusion and/or use is at customer’s own risk.

NVIDIA makes no representation or warranty that products based on this document will be suitable for any specified use. Testing of all parameters of each product is not necessarily performed by NVIDIA. It is customer’s sole responsibility to evaluate and determine the applicability of any information contained in this document, ensure the product is suitable and fit for the application planned by customer, and perform the necessary testing for the application in order to avoid a default of the application or the product. Weaknesses in customer’s product designs may affect the quality and reliability of the NVIDIA product and may result in additional or different conditions and/or requirements beyond those contained in this document. NVIDIA accepts no liability related to any default, damage, costs, or problem which may be based on or attributable to: (i) the use of the NVIDIA product in any manner that is contrary to this document or (ii) customer product designs.

No license, either expressed or implied, is granted under any NVIDIA patent right, copyright, or other NVIDIA intellectual property right under this document. Information published by NVIDIA regarding third-party products or services does not constitute a license from NVIDIA to use such products or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property rights of the third party, or a license from NVIDIA under the patents or other intellectual property rights of NVIDIA.

Reproduction of information in this document is permissible only if approved in advance by NVIDIA in writing, reproduced without alteration and in full compliance with all applicable export laws and regulations, and accompanied by all associated conditions, limitations, and notices.

THIS DOCUMENT AND ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE. TO THE EXTENT NOT PROHIBITED BY LAW, IN NO EVENT WILL NVIDIA BE LIABLE FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY DIRECT, INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF ANY USE OF THIS DOCUMENT, EVEN IF NVIDIA HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. Notwithstanding any damages that customer might incur for any reason whatsoever, NVIDIA’s aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms of Sale for the product.

## 2.2. OpenCL[](https://docs.nvidia.com#opencl)

OpenCL is a trademark of Apple Inc. used under license to the Khronos Group Inc.

## 2.3. Trademarks[](https://docs.nvidia.com#trademarks)

NVIDIA and the NVIDIA logo are trademarks or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.