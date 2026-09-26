source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMarker.html

# 7.68. CUpti_ActivityMarker[#](https://docs.nvidia.com#cupti-activitymarker)

-
struct CUpti_ActivityMarker
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityMarker) The activity record providing a marker which is an instantaneous point in time.

(deprecated in CUDA 8.0)

The marker is specified with a descriptive name and unique id (CUPTI_ACTIVITY_KIND_MARKER). Marker activity is now reported using the

[CUpti_ActivityMarker2](https://docs.nvidia.com/structCUpti__ActivityMarker2.html#structcupti__activitymarker2)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MARKER.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker5flagsE) The flags associated with the marker.

See also


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker9timestampE) The timestamp for the marker, in ns.

A value of 0 indicates that timestamp information could not be collected for the marker.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker2idE) The marker ID.


-
[CUpti_ActivityObjectKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityObjectKind)objectKind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker10objectKindE) The kind of activity object associated with this marker.


-
[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#_CPPv426CUpti_ActivityObjectKindId)objectId[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker8objectIdE) The identifier for the activity object associated with this marker.

‘objectKind’ indicates which ID is valid for this record.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker3padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMarker4nameE) The marker name for an instantaneous or start marker.

This will be NULL for an end marker.


-