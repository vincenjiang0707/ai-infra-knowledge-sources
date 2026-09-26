source: https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-preset-migration-guide/index.html

# NVENC Preset Migration Guide[#](https://docs.nvidia.com#nvenc-preset-migration-guide)

## 1. Introduction[#](https://docs.nvidia.com#introduction)

This document provides table to map the NVENCODE API settings (specifically, preset and rate control mode) from Video Codec SDK 9.1 and earlier to the closest equivalent NVENCODE API settings in Video Codec SDK 10.0 and later. This table can be used as a migration guide to migrate to the new NVENCODE API preset architecture introduced in Video Codec SDK 10.0.

In general, it is strongly recommended to use the newer presets and NVENCODE API settings based on desired performance/quality trade-off. It is highly likely that your application may benefit from better quality encoding or higher performance by directly using the new NVENCODE presets, as the new APIs provide much more flexibility than earlier and are easy to understand.

Please use the mapping tables in this document only in situations where exactly same performance/quality is desired as was obtained in the older presets.

[Table 1](https://docs.nvidia.com/table-hevc) and [Table 2](https://docs.nvidia.com/table-h264) show the mapping between older and newer presets exposed in the NVENCODE API for HEVC and H.264, respectively. Note that there is no support for older presets in AV1

A combination of older preset (Column 1), rate control (RC) mode (Column 2) and resolution (Column 3) can be mapped to a new parameters of NVENCODE API: tuning info (Column 4), RC Mode (Column 5), preset (Column 7&9) and multipass (Column 6&8). The newer preset and multipass values will vary based on GPU Architecture and appropriate GPU architecture column must be selected.

In some cases, additional settings need to be included for exact mapping, and they are mentioned in columns Features 1 (Column 10 in [Table 1](https://docs.nvidia.com/table-hevc) and Column 12 in [Table 2](https://docs.nvidia.com/table-h264)) and Features 2 (Column 11 in [Table 1](https://docs.nvidia.com/table-hevc) and Column 13 in [Table 2](https://docs.nvidia.com/table-h264)).

As an example, if someone is using HEVC HQ Preset with VBR_HQ RC Mode for a 1080p encoding on Turing platform, this corresponds to Row 18 in [Table 1](https://docs.nvidia.com/table-hevc). The closest settings as per the new NVENCODE API is P6 Preset, RC Mode VBR, Multipass set to 1, FrameIntervalP set to 1, IDR Period set to 60 and GOP Length set to 60.

It is important to note that Features 1 and Features 2 are just indicated to get an exact feature match on older presets and most applications would set these based on needs. For example, GOP length may be set to a larger value depending upon the application needs.

## 2. HEVC Preset Migration Table[#](https://docs.nvidia.com#hevc-preset-migration-table)

Settings in Video Codec SDK 9.1 and earlier |
Equivalent settings in Video Codec SDK 10.0 and later |
|||||||||
|---|---|---|---|---|---|---|---|---|---|---|
Old Preset |
Old RC Mode |
Resolution |
Tuning Info |
RC Mode |
Ampere/ Turing Multi Pass |
Ampere/ Turing Preset |
Pascal/ Maxwell MultiPass |
Pascal/ Maxwell Preset |
Features 1 |
Features 2 |
HP |
VBR |
720 |
High Quality |
VBR |
0 |
P1 |
0 |
P4 |
frameIntervalP 1 |
|
HP |
VBR |
1080 |
High Quality |
VBR |
0 |
P1 |
0 |
P4 |
idr period 60 |
|
HP |
VBR |
2160 |
High Quality |
VBR |
0 |
P1 |
0 |
P4 |
gop length 60 |
|
HP |
VBR_HQ |
720 |
High Quality |
VBR |
1 |
P1 |
1 |
P4 |
||
HP |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P1 |
1 |
P4 |
||
HP |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P1 |
1 |
P4 |
||
Default |
VBR |
720 |
High Quality |
VBR |
0 |
P5 |
0 |
P5 |
||
Default |
VBR |
1080 |
High Quality |
VBR |
0 |
P5 |
0 |
P5 |
||
Default |
VBR |
2160 |
High Quality |
VBR |
0 |
P5 |
0 |
P5 |
||
Default |
VBR_HQ |
720 |
High Quality |
VBR |
1 |
P5 |
2 |
P5 |
||
Default |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
||
Default |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
||
HQ |
VBR |
720 |
High Quality |
VBR |
0 |
P6 |
0 |
P6 |
||
HQ |
VBR |
1080 |
High Quality |
VBR |
0 |
P6 |
0 |
P6 |
||
HQ |
VBR |
2160 |
High Quality |
VBR |
0 |
P5 |
0 |
P6 |
||
HQ |
VBR_HQ |
720 |
High Quality |
VBR |
1 |
P6 |
2 |
P6 |
||
HQ |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P6 |
1 |
P6 |
||
HQ |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P5 |
1 |
P6 |
||
LowLatencyHP |
CBR |
720 |
Low Latency |
CBR |
0 |
P2 |
0 |
P4 |
||
LowLatencyHP |
CBR |
1080 |
Low Latency |
CBR |
0 |
P2 |
0 |
P4 |
||
LowLatencyHP |
CBR |
2160 |
Low Latency |
CBR |
0 |
P1 |
0 |
P4 |
||
LowLatencyHP |
CBR_HQ |
720 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
||
LowLatencyHP |
CBR_HQ |
1080 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
||
LowLatencyHP |
CBR_HQ |
2160 |
Ultra Low Latency |
CBR |
1 |
P1 |
1 |
P4 |
||
LowLatencyHP |
CBR2LD |
720 |
Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
||
LowLatencyHP |
CBR2LD |
1080 |
Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
||
LowLatencyHP |
CBR2LD |
2160 |
Low Latency |
CBR |
1 |
P1 |
1 |
P4 |
||
LowLatencyDefault |
CBR |
720 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
||
LowLatencyDefault |
CBR |
1080 |
Low Latency |
CBR |
0 |
P3 |
0 |
P4 |
||
LowLatencyDefault |
CBR |
2160 |
Low Latency |
CBR |
0 |
P2 |
0 |
P4 |
||
LowLatencyDefault |
CBR_HQ |
720 |
Ultra Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
||
LowLatencyDefault |
CBR_HQ |
1080 |
Ultra Low Latency |
CBR |
1 |
P3 |
1 |
P4 |
||
LowLatencyDefault |
CBR_HQ |
2160 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
||
LowLatencyDefault |
CBR_LOWDELAY_HQ |
720 |
Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
||
LowLatencyDefault |
CBR_LOWDELAY_HQ |
1080 |
Low Latency |
CBR |
1 |
P3 |
1 |
P4 |
||
LowLatencyDefault |
CBR_LOWDELAY_HQ |
2160 |
Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
||
LowLatencyHQ |
CBR |
720 |
Low Latency |
CBR |
0 |
P5 |
0 |
P6 |
||
LowLatencyHQ |
CBR |
1080 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
||
LowLatencyHQ |
CBR |
2160 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
||
LowLatencyHQ |
CBR_HQ |
720 |
Ultra Low Latency |
CBR |
2 |
P5 |
2 |
P6 |
||
LowLatencyHQ |
CBR_HQ |
1080 |
Ultra Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
||
LowLatencyHQ |
CBR_HQ |
2160 |
Ultra Low Latency |
CBR |
1 |
P4 |
1 |
P4 |
||
LowLatencyHQ |
CBR_LOWDELAY_HQ |
720 |
Low Latency |
CBR |
2 |
P5 |
2 |
P6 |
||
LowLatencyHQ |
CBR_LOWDELAY_HQ |
1080 |
Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
||
LowLatencyHQ |
CBR_LOWDELAY_HQ |
2160 |
Low Latency |
CBR |
1 |
P4 |
1 |
P4 |
||
BD |
VBR |
720 |
High Quality |
VBR |
0 |
P5 |
0 |
P5 |
frameIntervalP 1 |
outputseiBufferPeriod 1 |
BD |
VBR |
1080 |
High Quality |
VBR |
0 |
P5 |
0 |
P5 |
idr period 60 |
outputseiPictureTime 1 |
BD |
VBR |
2160 |
High Quality |
VBR |
0 |
P5 |
0 |
P6 |
gop length 60 |
outputAud 1 |
BD |
VBR_HQ |
720 |
High Quality |
VBR |
1 |
P5 |
2 |
P5 |
||
BD |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
||
BD |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
||
LosslessHP |
CQP |
720 |
Lossless |
CQP |
X |
P3 |
X |
P3 |
frameIntervalP 1 |
|
LosslessHP |
CQP |
1080 |
Lossless |
CQP |
X |
P3 |
X |
P3 |
idr period 30 |
|
LosslessHP |
CQP |
2160 |
Lossless |
CQP |
X |
P3 |
X |
P3 |
gop length 30 |
|
LosslessDefault |
CQP |
720 |
Lossless |
CQP |
X |
P5 |
X |
P5 |
||
LosslessDefault |
CQP |
1080 |
Lossless |
CQP |
X |
P5 |
X |
P5 |
||
LosslessDefault |
CQP |
2160 |
Lossless |
CQP |
X |
P5 |
X |
P5 |

## 3. H264 Preset Migration Table[#](https://docs.nvidia.com#h264-preset-migration-table)

Settings in Video Codec SDK 9.1 and earlier |
Equivalent settings in Video Codec SDK 10.0 and later |
|||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
Old Preset |
Old RC Mode |
Resol- ution |
Tuning Info |
RC Mode |
Ampere/ Turing Multi- Pass |
Ampere/ Turing Preset |
Pascal/ Maxwell Multi- Pass |
Pascal/ Maxwell Preset |
Kepler Multi- Pass |
Kepler preset |
Features 1 |
Features 2 |
HP |
VBR |
720 |
High Quality |
VBR |
0 |
P2 |
0 |
P1 |
0 |
P1 |
frameIntervalP 1 |
|
HP |
VBR |
1080 |
High Quality |
VBR |
0 |
P2 |
0 |
P1 |
0 |
P1 |
idr period 30 |
|
HP |
VBR |
2160 |
High Quality |
VBR |
0 |
P2 |
0 |
P1 |
0 |
P1 |
gop length 30 |
|
HP |
VBR_HQ |
720 |
High Quality |
VBR |
1 |
P2 |
1 |
P1 |
2 |
P1 |
||
HP |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P2 |
1 |
P1 |
2 |
P1 |
||
HP |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P2 |
1 |
P1 |
2 |
P1 |
||
Default |
VBR |
720 |
High Quality |
VBR |
0 |
P3 |
0 |
P3 |
0 |
P3 |
sliceMode 3 |
|
Default |
VBR |
1080 |
High Quality |
VBR |
0 |
P3 |
0 |
P3 |
0 |
P3 |
sliceModeData 4 |
|
Default |
VBR |
2160 |
High Quality |
VBR |
0 |
P3 |
0 |
P3 |
0 |
P3 |
||
Default |
VBR_HQ |
720 |
High Quality |
VBR |
2 |
P3 |
2 |
P3 |
2 |
P3 |
||
Default |
VBR_HQ |
1080 |
High Quality |
VBR |
2 |
P3 |
2 |
P3 |
2 |
P3 |
||
Default |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P4 |
1 |
P3 |
2 |
P3 |
||
HQ |
VBR |
720 |
High Quality |
VBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
HQ |
VBR |
1080 |
High Quality |
VBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
HQ |
VBR |
2160 |
High Quality |
VBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
HQ |
VBR_HQ |
720 |
High Quality |
VBR |
2 |
P4 |
2 |
P4 |
2 |
P4 |
||
HQ |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
2 |
P4 |
||
HQ |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
2 |
P4 |
||
LowLatencyHP |
CBR |
720 |
Low Latency |
CBR |
0 |
P2 |
0 |
P4 |
0 |
P3 |
sliceMode 3 |
|
LowLatencyHP |
CBR |
1080 |
Low Latency |
CBR |
0 |
P2 |
0 |
P3 |
0 |
P3 |
sliceModeData 4 |
|
LowLatencyHP |
CBR |
2160 |
Low Latency |
CBR |
0 |
P2 |
0 |
P2 |
0 |
P2 |
||
LowLatencyHP |
CBR_HQ |
720 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
2 |
P3 |
||
LowLatencyHP |
CBR_HQ |
1080 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P3 |
2 |
P3 |
||
LowLatencyHP |
CBR_HQ |
2160 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P2 |
2 |
P2 |
||
LowLatencyHP |
CBR_LOWDELAY_HQ |
720 |
Low Latency |
CBR |
1 |
P2 |
1 |
P4 |
2 |
P3 |
||
LowLatencyHP |
CBR_LOWDELAY_HQ |
1080 |
Low Latency |
CBR |
1 |
P2 |
1 |
P3 |
2 |
P3 |
||
LowLatencyHP |
CBR_LOWDELAY_HQ |
2160 |
Low Latency |
CBR |
1 |
P2 |
1 |
P2 |
2 |
P2 |
||
LowLatencyDefault |
CBR |
720 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
LowLatencyDefault |
CBR |
1080 |
Low Latency |
CBR |
0 |
P3 |
0 |
P4 |
0 |
P3 |
||
LowLatencyDefault |
CBR |
2160 |
Low Latency |
CBR |
0 |
P2 |
0 |
P2 |
0 |
P2 |
||
LowLatencyDefault |
CBR_HQ |
720 |
Ultra Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
2 |
P4 |
||
LowLatencyDefault |
CBR_HQ |
1080 |
Ultra Low Latency |
CBR |
2 |
P3 |
2 |
P4 |
2 |
P3 |
||
LowLatencyDefault |
CBR_HQ |
2160 |
Ultra Low Latency |
CBR |
1 |
P2 |
1 |
P2 |
2 |
P2 |
||
LowLatencyDefault |
CBR_LOWDELAY_HQ |
720 |
Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
2 |
P4 |
||
LowLatencyDefault |
CBR_LOWDELAY_HQ |
1080 |
Low Latency |
CBR |
2 |
P3 |
2 |
P4 |
2 |
P3 |
||
LowLatencyDefault |
CBR_LOWDELAY_HQ |
2160 |
Low Latency |
CBR |
1 |
P2 |
1 |
P2 |
2 |
P2 |
||
LowLatencyHQ |
CBR |
720 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
LowLatencyHQ |
CBR |
1080 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
LowLatencyHQ |
CBR |
2160 |
Low Latency |
CBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
||
LowLatencyHQ |
CBR_HQ |
720 |
Ultra Low Latency |
CBR |
2 |
P4 |
2 |
P5 |
2 |
P4 |
||
LowLatencyHQ |
CBR_HQ |
1080 |
Ultra Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
2 |
P4 |
||
LowLatencyHQ |
CBR_HQ |
2160 |
Ultra Low Latency |
CBR |
1 |
P4 |
1 |
P4 |
2 |
P4 |
||
LowLatencyHQ |
CBR_LOWDELAY_HQ |
720 |
Low Latency |
CBR |
2 |
P4 |
2 |
P5 |
2 |
P4 |
||
LowLatencyHQ |
CBR_LOWDELAY_HQ |
1080 |
Low Latency |
CBR |
2 |
P4 |
2 |
P4 |
2 |
P4 |
||
LowLatencyHQ |
CBR_LOWDELAY_HQ |
2160 |
Low Latency |
CBR |
1 |
P4 |
1 |
P4 |
2 |
P4 |
||
BD |
VBR |
720 |
High Quality |
VBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
frameIntervalP 3 |
outputseiBufferPeriod 1 |
BD |
VBR |
1080 |
High Quality |
VBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
idr period 30 |
outputseiPictureTime 1 |
BD |
VBR |
2160 |
High Quality |
VBR |
0 |
P4 |
0 |
P4 |
0 |
P4 |
gop length 30 |
outputAud 1 |
BD |
VBR_HQ |
720 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
2 |
P5 |
basref 0 |
|
BD |
VBR_HQ |
1080 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
2 |
P5 |
sliceMode 3 |
|
BD |
VBR_HQ |
2160 |
High Quality |
VBR |
1 |
P5 |
1 |
P5 |
2 |
P5 |
sliceModeData 4 |
|
LosslessHP |
CQP |
720 |
lossless |
CQP |
X |
P2 |
X |
P2 |
X |
X |
frameIntervalP 1 |
sliceMode 3 |
LosslessHP |
CQP |
1080 |
lossless |
CQP |
X |
P2 |
X |
P2 |
X |
X |
idr period 30 |
sliceModeData 1 |
LosslessHP |
CQP |
2160 |
lossless |
CQP |
X |
P2 |
X |
P2 |
X |
X |
gop length 30 |
|
LosslessDefault |
CQP |
720 |
lossless |
CQP |
X |
P3 |
X |
P3 |
X |
X |
||
LosslessDefault |
CQP |
1080 |
lossless |
CQP |
X |
P3 |
X |
P3 |
X |
X |
||
LosslessDefault |
CQP |
2160 |
lossless |
CQP |
X |
P3 |
X |
P3 |
X |
X |

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