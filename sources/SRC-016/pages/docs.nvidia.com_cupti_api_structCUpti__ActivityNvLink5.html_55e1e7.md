source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityNvLink5.html

# 7.103. CUpti_ActivityNvLink5[#](https://docs.nvidia.com#cupti-activitynvlink5)

-
struct CUpti_ActivityNvLink5
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityNvLink5) NVLink information.

This structure gives capabilities of each logical NVLink connection between two devices, gpu<->gpu or gpu<->CPU which can be used to understand the topology.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink54kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_NVLINK.


-
uint32_t nvlinkVersion
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink513nvlinkVersionE) NvLink version.


-
[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv413CUpti_DevType)typeDev0[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink58typeDev0E) Type of device 0

[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1gad67907716d28ba51253f08d3e0bd0dda).

-
[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv413CUpti_DevType)typeDev1[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink58typeDev1E) Type of device 1

[CUpti_DevType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1gad67907716d28ba51253f08d3e0bd0dda).

-
CUuuid uuidDev
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink57uuidDevE) If typeDev0 is CUPTI_DEV_TYPE_GPU, UUID for device 0.

If typeDev1 is CUPTI_DEV_TYPE_GPU, UUID for device 1.


-
[CUpti_ActivityNvLinkNpu](https://docs.nvidia.com/structCUpti__ActivityNvLinkNpu.html#_CPPv423CUpti_ActivityNvLinkNpu)npu[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink53npuE) If typeDev0 is CUPTI_DEV_TYPE_NPU, struct npu for NPU.

If typeDev1 is CUPTI_DEV_TYPE_NPU, struct npu for NPU.


-
union
[CUpti_ActivityNvLink5](https://docs.nvidia.com#_CPPv421CUpti_ActivityNvLink5)::[anonymous] idDev0[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink56idDev0E) If typeDev0 is CUPTI_DEV_TYPE_GPU, UUID for device 0.

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6). If typeDev0 is CUPTI_DEV_TYPE_NPU, struct npu for NPU.

-
union
[CUpti_ActivityNvLink5](https://docs.nvidia.com#_CPPv421CUpti_ActivityNvLink5)::[anonymous] idDev1[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink56idDev1E) If typeDev1 is CUPTI_DEV_TYPE_GPU, UUID for device 1.

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6). If typeDev1 is CUPTI_DEV_TYPE_NPU, struct npu for NPU.

-
uint32_t flag
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink54flagE) Flag gives capabilities of the link.

See also


-
uint32_t physicalNvLinkCount
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink519physicalNvLinkCountE) Number of physical NVLinks present between two devices.


-
uint32_t *portDev0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink58portDev0E) Port numbers for NVLinks connected to device 0.

If typeDev0 is CUPTI_DEV_TYPE_NPU, ignore this field. In case of invalid/unknown port number, this field will be set to value CUPTI_NVLINK_INVALID_PORT. This will be used to correlate the metric values to individual physical link and attribute traffic to the logical NVLink in the topology. CUPTI dynamically allocates memory using the malloc() function for physicalNvLinkCount ports. Client is responsible for freeing this memory using the free() function when done.


-
uint32_t *portDev1
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink58portDev1E) Port numbers for NVLinks connected to device 1.

If typeDev1 is CUPTI_DEV_TYPE_NPU, ignore this field. In case of invalid/unknown port number, this field will be set to value CUPTI_NVLINK_INVALID_PORT. This will be used to correlate the metric values to individual physical link and attribute traffic to the logical NVLink in the topology. CUPTI dynamically allocates memory using the malloc() function for physicalNvLinkCount ports. Client is responsible for freeing this memory using the free() function when done.


-
uint64_t bandwidth
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink59bandwidthE) Bandwidth of NVLink in kbytes/sec.


-
uint8_t nvswitchConnected
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink517nvswitchConnectedE) NVSwitch is connected as an intermediate node.


-
uint8_t pad[7]
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityNvLink53padE) Undefined.

reserved for internal use


-