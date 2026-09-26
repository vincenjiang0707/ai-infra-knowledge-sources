source: https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/deprecation-notices/index.html

# Deprecation Notices[#](https://docs.nvidia.com#deprecation-notices)

## 1. Deprecation Notices[#](https://docs.nvidia.com#deprecation-notices)

Driver support for below NVENCODE API presets will be removed in future. So applications using below presets will stop working in a future driver version.

`NV_ENC_PRESET_DEFAULT_GUID`

`NV_ENC_PRESET_HP_GUID`

`NV_ENC_PRESET_HQ_GUID`

`NV_ENC_PRESET_BD_GUID`

`NV_ENC_PRESET_LOW_LATENCY_DEFAULT_GUID`

`NV_ENC_PRESET_LOW_LATENCY_HQ_GUID`

`NV_ENC_PRESET_LOW_LATENCY_HP_GUID`

`NV_ENC_PRESET_LOSSLESS_DEFAULT_GUID`

`NV_ENC_PRESET_LOSSLESS_HP_GUID`


Users are therefore recommended to move to the new presets. Please note that the sample applications in the SDK illustrate the new presets only. Refer to the migration guide for achieving the equivalent functionality for the presets.

Slice Mode = 1, Byte based Slice Encoding will be removed in the next SDK.

NVENCODE API does not support 32-bit applications on Blackwell. The support for 32-bit applications on ADA and earlier generation GPUs will be removed in the next SDK.

Hybrid (CUDA + CPU) JPEG decoding support will be removed in future. Users are therefore recommended to move to

[nvJPEG library](https://docs.nvidia.com/cuda/nvjpeg/index.html)for JPEG decoding.

Notices

Notice

This document is provided for information purposes only and shall not be regarded as a warranty of a certain functionality, condition, or quality of a product. NVIDIA Corporation (“NVIDIA”) makes no representations or warranties, expressed or implied, as to the accuracy or completeness of the information contained in this document and assumes no responsibility for any errors contained herein. NVIDIA shall have no liability for the consequences or use of such information or for any infringement of patents or other rights of third parties that may result from its use. This document is not a commitment to develop, release, or deliver any Material (defined below), code, or functionality.

NVIDIA reserves the right to make corrections, modifications, enhancements, improvements, and any other changes to this document, at any time without notice.

Customer should obtain the latest relevant information before placing orders and should verify that such information is current and complete.

NVIDIA products are sold subject to the NVIDIA standard terms and conditions of sale supplied at the time of order acknowledgment, unless otherwise agreed in an individual sales agreement signed by authorized representatives of NVIDIA and customer (“Terms of Sale”). NVIDIA hereby expressly objects to applying any customer general terms and conditions with regards to the purchase of the NVIDIA product referenced in this document. No contractual obligations are formed either directly or indirectly by this document.

NVIDIA products are not designed, authorized, or warranted to be suitable for use in medical, military, aircraft, space, or life support equipment, nor in applications where failure or malfunction of the NVIDIA product can reasonably be expected to result in personal injury, death, or property or environmental damage. NVIDIA accepts no liability for inclusion and/or use of NVIDIA products in such equipment or applications and therefore such inclusion and/or use is at customer’s own risk.

NVIDIA makes no representation or warranty that products based on this document will be suitable for any specified use. Testing of all parameters of each product is not necessarily performed by NVIDIA. It is customer’s sole responsibility to evaluate and determine the applicability of any information contained in this document, ensure the product is suitable and fit for the application planned by customer, and perform the necessary testing for the application in order to avoid a default of the application or the product. Weaknesses in customer’s product designs may affect the quality and reliability of the NVIDIA product and may result in additional or different conditions and/or requirements beyond those contained in this document. NVIDIA accepts no liability related to any default, damage, costs, or problem which may be based on or attributable to: (i) the use of the NVIDIA product in any manner that is contrary to this document or (ii) customer product designs.

Trademarks

NVIDIA, the NVIDIA logo, and cuBLAS, CUDA, CUDA Toolkit, cuDNN, DALI, DIGITS, DGX, DGX-1, DGX-2, DGX Station, DLProf, GPU, Jetson, Kepler, Maxwell, NCCL, Nsight Compute, Nsight Systems, NVCaffe, NVIDIA Deep Learning SDK, NVIDIA Developer Program, NVIDIA GPU Cloud, NVLink, NVSHMEM, PerfWorks, Pascal, SDK Manager, Tegra, TensorRT, TensorRT Inference Server, Tesla, TF-TRT, Triton Inference Server, Turing, and Volta are trademarks and/or registered trademarks of NVIDIA Corporation in the United States and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.