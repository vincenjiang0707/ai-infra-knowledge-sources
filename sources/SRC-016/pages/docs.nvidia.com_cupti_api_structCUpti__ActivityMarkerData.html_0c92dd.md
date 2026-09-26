source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMarkerData.html

# 7.70. CUpti_ActivityMarkerData[#](https://docs.nvidia.com#cupti-activitymarkerdata)

-
struct CUpti_ActivityMarkerData
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityMarkerData) The activity record providing detailed information for a marker.

User must enable CUPTI_ACTIVITY_KIND_MARKER as well to get records for marker data. The marker data contains color, payload, and category. (CUPTI_ACTIVITY_KIND_MARKER_DATA).

Structure deprecated in CUDA 13.1: Refer to

[CUpti_ActivityMarkerData2](https://docs.nvidia.com/structCUpti__ActivityMarkerData2.html#structcupti__activitymarkerdata2)for the latest structure.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MARKER_DATA.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData5flagsE) The flags associated with the marker.

See also


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData2idE) The marker ID.


-
CUpti_MetricValueKind payloadKind
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData11payloadKindE) Defines the payload format for the value associated with the marker.


-
CUpti_MetricValue payload
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData7payloadE) The payload value.


-
uint32_t color
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData5colorE) The color for the marker.


-
uint32_t category
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMarkerData8categoryE) The category for the marker.


-