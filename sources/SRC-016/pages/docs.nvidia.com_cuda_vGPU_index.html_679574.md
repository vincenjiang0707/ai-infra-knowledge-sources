source: https://docs.nvidia.com/cuda/vGPU/index.html

vGPUs and CUDA

vGPUs that support CUDA

This page describes the support for CUDA® on NVIDIA® virtual GPU software.

#
1. Overview[](https://docs.nvidia.com#overview)

For more information on NVIDIA virtual GPU software, visit [https://docs.nvidia.com/grid/index.html](https://docs.nvidia.com/grid/index.html).

##
1.1. vGPU[](https://docs.nvidia.com#vgpu)

The following vGPU releases support CUDA:

|
|
|---|---|
CUDA 12.6 |
Not supported |
CUDA 12.5 |
Not supported |
CUDA 12.4 Update 1 (12.4.1) |
|
CUDA 12.4 |
|
CUDA 12.3 Update 2 (12.3.2) |
Not supported |
CUDA 12.3 Update 1 (12.3.1) |
Not supported |
CUDA 12.3 |
Not supported |
CUDA 12.2 Update 1 (12.2.1) |
|
CUDA 12.2 |
|
CUDA 12.1 Update 1 (12.1.1) |
|
CUDA 12.1 |
|
CUDA 12.0 Update 1 (12.0.1) |
|
CUDA 12.0 |
|
CUDA 11.8 |
|
CUDA 11.7 Update 1 (11.7.1) |
|
CUDA 11.7 |
|
CUDA 11.6 Update 1 (11.6.1) |
|
CUDA 11.6 |
|
CUDA 11.5 Update 2 (11.5.2) |
|
CUDA 11.5 Update 1 (11.5.1) |
|
CUDA 11.5 |
|
CUDA 11.4 Update 4 (11.4.4) |
|
CUDA 11.4 Update 3 (11.4.3 |
|
CUDA 11.4 Update 2 (11.4.2) |
|
CUDA 11.4 Update 1 (11.4.1) |
|
CUDA 11.4 |
|
CUDA 11.3 Update 1 (11.3.1) |
Not supported |
CUDA 11.3 |
Not supported |
CUDA 11.2 Update 1 (11.2.1) |
Not supported |
CUDA 11.2 |
|
CUDA 11.1 Update 1 (11.1.1) |
Not supported |
CUDA 11.1 |
Not supported |
CUDA 11.0 |
|
CUDA 10.2 |
|
CUDA 10.1 Update 2 (10.1.243) |
Not supported |
CUDA 10.1 Update 1 |
|
CUDA 10.1 general release (10.1.105) |
|
CUDA 10.0.130 |
|
CUDA 9.2 (9.2.148 Update 1) |
Not supported |
CUDA 9.2 (9.2.88) |
Not supported |
CUDA 9.1 (9.1.85) |
|
CUDA 9.0 (9.0.176) |

Some CUDA features might not be supported by your version of NVIDIA virtual GPU software. For details, follow the link in the table to the documentation for your version.

##
1.2. Notices[](https://docs.nvidia.com#notices)

###
1.2.1. Notice[](https://docs.nvidia.com#notice)

This document is provided for information purposes only and shall not be regarded as a warranty of a certain functionality, condition, or quality of a product. NVIDIA Corporation (“NVIDIA”) makes no representations or warranties, expressed or implied, as to the accuracy or completeness of the information contained in this document and assumes no responsibility for any errors contained herein. NVIDIA shall have no liability for the consequences or use of such information or for any infringement of patents or other rights of third parties that may result from its use. This document is not a commitment to develop, release, or deliver any Material (defined below), code, or functionality.

NVIDIA reserves the right to make corrections, modifications, enhancements, improvements, and any other changes to this document, at any time without notice.

Customer should obtain the latest relevant information before placing orders and should verify that such information is current and complete.

NVIDIA products are sold subject to the NVIDIA standard terms and conditions of sale supplied at the time of order acknowledgement, unless otherwise agreed in an individual sales agreement signed by authorized representatives of NVIDIA and customer (“Terms of Sale”). NVIDIA hereby expressly objects to applying any customer general terms and conditions with regards to the purchase of the NVIDIA product referenced in this document. No contractual obligations are formed either directly or indirectly by this document.

NVIDIA products are not designed, authorized, or warranted to be suitable for use in medical, military, aircraft, space, or life support equipment, nor in applications where failure or malfunction of the NVIDIA product can reasonably be expected to result in personal injury, death, or property or environmental damage. NVIDIA accepts no liability for inclusion and/or use of NVIDIA products in such equipment or applications and therefore such inclusion and/or use is at customer’s own risk.

NVIDIA makes no representation or warranty that products based on this document will be suitable for any specified use. Testing of all parameters of each product is not necessarily performed by NVIDIA. It is customer’s sole responsibility to evaluate and determine the applicability of any information contained in this document, ensure the product is suitable and fit for the application planned by customer, and perform the necessary testing for the application in order to avoid a default of the application or the product. Weaknesses in customer’s product designs may affect the quality and reliability of the NVIDIA product and may result in additional or different conditions and/or requirements beyond those contained in this document. NVIDIA accepts no liability related to any default, damage, costs, or problem which may be based on or attributable to: (i) the use of the NVIDIA product in any manner that is contrary to this document or (ii) customer product designs.

No license, either expressed or implied, is granted under any NVIDIA patent right, copyright, or other NVIDIA intellectual property right under this document. Information published by NVIDIA regarding third-party products or services does not constitute a license from NVIDIA to use such products or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property rights of the third party, or a license from NVIDIA under the patents or other intellectual property rights of NVIDIA.

Reproduction of information in this document is permissible only if approved in advance by NVIDIA in writing, reproduced without alteration and in full compliance with all applicable export laws and regulations, and accompanied by all associated conditions, limitations, and notices.

THIS DOCUMENT AND ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE. TO THE EXTENT NOT PROHIBITED BY LAW, IN NO EVENT WILL NVIDIA BE LIABLE FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY DIRECT, INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF ANY USE OF THIS DOCUMENT, EVEN IF NVIDIA HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. Notwithstanding any damages that customer might incur for any reason whatsoever, NVIDIA’s aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms of Sale for the product.

###
1.2.2. OpenCL[](https://docs.nvidia.com#opencl)

OpenCL is a trademark of Apple Inc. used under license to the Khronos Group Inc.

###
1.2.3. Trademarks[](https://docs.nvidia.com#trademarks)

NVIDIA and the NVIDIA logo are trademarks or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.