source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMarkerData2.html

# 7.71. CUpti_ActivityMarkerData2[#](https://docs.nvidia.com#cupti-activitymarkerdata2)

-
struct CUpti_ActivityMarkerData2
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityMarkerData2) The activity record providing detailed information for a marker.

User must enable CUPTI_ACTIVITY_KIND_MARKER as well to get records for marker data. The marker data contains color, payload, and category. (CUPTI_ACTIVITY_KIND_MARKER_DATA).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MARKER_DATA.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData25flagsE) The flags associated with the marker.

See also


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData22idE) The marker ID.


-
CUpti_MetricValueKind payloadKind
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData211payloadKindE) Defines the payload format for the value associated with the marker.


-
CUpti_MetricValue payload
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData27payloadE) The payload value.


-
uint32_t color
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData25colorE) The color for the marker.


-
uint32_t category
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData28categoryE) The category for the marker.


-
uint32_t cuptiDomainId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData213cuptiDomainIdE) CUPTI maintained domain id required for NVTX extended payloads.

To parse the payload correctly, the domain id must be used to identify the payload attributes as they are domain specific.


-
uint32_t padding
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMarkerData27paddingE) Reserved for internal use.


-