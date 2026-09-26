source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityNvLink3.html

# 7.101. CUpti_ActivityNvLink3[#](https://docs.nvidia.com#cupti-activitynvlink3)

-
struct CUpti_ActivityNvLink3
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityNvLink3) NVLink information.

This structure gives capabilities of each logical NVLink connection between two devices, gpu<->gpu or gpu<->CPU which can be used to understand the topology. NvLink information is now reported using the

[CUpti_ActivityNvLink5](https://docs.nvidia.com/structCUpti__ActivityNvLink5.html#structcupti__activitynvlink5)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_NVLINK.


-
uint32_t nvlinkVersion
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink313nvlinkVersionE) NvLink version.


-
[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv413CUpti_DevType)typeDev0[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink38typeDev0E) Type of device 0

[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1gad67907716d28ba51253f08d3e0bd0dda).

-
[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv413CUpti_DevType)typeDev1[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink38typeDev1E) Type of device 1

[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1gad67907716d28ba51253f08d3e0bd0dda).

-
uint32_t index
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink35indexE) Index of the NPU.

First index will always be zero.


-
uint32_t domainId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink38domainIdE) Domain ID of NPU.

On Linux, this can be queried using lspci.


-
union
[CUpti_ActivityNvLink3](https://docs.nvidia.com#_CPPv421CUpti_ActivityNvLink3)::[anonymous] idDev0[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink36idDev0E) If typeDev0 is CUPTI_DEV_TYPE_GPU, UUID for device 0.

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6). If typeDev0 is CUPTI_DEV_TYPE_NPU, struct npu for NPU.

-
union
[CUpti_ActivityNvLink3](https://docs.nvidia.com#_CPPv421CUpti_ActivityNvLink3)::[anonymous] idDev1[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink36idDev1E) If typeDev1 is CUPTI_DEV_TYPE_GPU, UUID for device 1.

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6). If typeDev1 is CUPTI_DEV_TYPE_NPU, struct npu for NPU.

-
uint32_t flag
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink34flagE) Flag gives capabilities of the link.

See also


-
uint32_t physicalNvLinkCount
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink319physicalNvLinkCountE) Number of physical NVLinks present between two devices.


-
int8_t portDev0[16]
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink38portDev0E) Port numbers for maximum 16 NVLinks connected to device 0.

If typeDev0 is CUPTI_DEV_TYPE_NPU, ignore this field. In case of invalid/unknown port number, this field will be set to value CUPTI_NVLINK_INVALID_PORT. This will be used to correlate the metric values to individual physical link and attribute traffic to the logical NVLink in the topology.


-
int8_t portDev1[16]
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink38portDev1E) Port numbers for maximum 16 NVLinks connected to device 1.

If typeDev1 is CUPTI_DEV_TYPE_NPU, ignore this field. In case of invalid/unknown port number, this field will be set to value CUPTI_NVLINK_INVALID_PORT. This will be used to correlate the metric values to individual physical link and attribute traffic to the logical NVLink in the topology.


-
uint64_t bandwidth
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink39bandwidthE) Bandwidth of NVLink in kbytes/sec.


-
uint8_t nvswitchConnected
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink317nvswitchConnectedE) NVSwitch is connected as an intermediate node.


-
uint8_t pad[7]
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink33padE) Undefined.

reserved for internal use


-