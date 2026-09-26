source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityPcie.html

# 7.120. CUpti_ActivityPcie[#](https://docs.nvidia.com#cupti-activitypcie)

-
struct CUpti_ActivityPcie
[#](https://docs.nvidia.com#_CPPv418CUpti_ActivityPcie) PCI devices information required to construct topology.

This structure gives capabilities of GPU and PCI bridge connected to the PCIE bus which can be used to understand the topology.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_PCIE.


-
[CUpti_PcieDeviceType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv420CUpti_PcieDeviceType)type[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie4typeE) Type of device in topology,

[CUpti_PcieDeviceType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga21881d93eb4622a660f0ebd8e2fd2bab).If type is CUPTI_PCIE_DEVICE_TYPE_GPU use devId for id and gpuAttr and if type is CUPTI_PCIE_DEVICE_TYPE_BRIDGE use bridgeId for id and bridgeAttr.


-
CUdevice devId
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie5devIdE) GPU device ID.


-
uint32_t bridgeId
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie8bridgeIdE) A unique identifier for Bridge in the Topology.


-
union
[CUpti_ActivityPcie](https://docs.nvidia.com#_CPPv418CUpti_ActivityPcie)::[anonymous] id[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie2idE) A unique identifier for GPU or Bridge in Topology.


-
uint32_t domain
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie6domainE) Domain for the GPU or Bridge, required to identify which PCIE bus it belongs to in multiple NUMA systems.


-
uint16_t pcieGeneration
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie14pcieGenerationE) PCIE Generation of GPU or Bridge.


-
uint16_t linkRate
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie8linkRateE) Link rate of the GPU or bridge in gigatransfers per second (GT/s)


-
uint16_t linkWidth
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie9linkWidthE) Link width of the GPU or bridge.


-
uint16_t upstreamBus
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie11upstreamBusE) Upstream bus ID for the GPU or PCI bridge.

Required to identify which bus it is connected to in the topology.


-
[CUpti_ActivityPcieGpuAttr](https://docs.nvidia.com/structCUpti__ActivityPcieGpuAttr.html#_CPPv425CUpti_ActivityPcieGpuAttr)gpuAttr[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie7gpuAttrE) Attributes for more information about GPU (gpuAttr).


-
[CUpti_ActivityPcieBridgeAttr](https://docs.nvidia.com/structCUpti__ActivityPcieBridgeAttr.html#_CPPv428CUpti_ActivityPcieBridgeAttr)bridgeAttr[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie10bridgeAttrE) Attributes for more information about PCI Bridge (bridgeAttr).


-
union
[CUpti_ActivityPcie](https://docs.nvidia.com#_CPPv418CUpti_ActivityPcie)::[anonymous] attr[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityPcie4attrE) Attributes for more information about GPU (gpuAttr) or PCI Bridge (bridgeAttr)


-