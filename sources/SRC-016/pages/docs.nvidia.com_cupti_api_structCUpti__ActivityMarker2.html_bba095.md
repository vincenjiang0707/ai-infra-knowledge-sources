source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMarker2.html

# 7.69. CUpti_ActivityMarker2[#](https://docs.nvidia.com#cupti-activitymarker2)

-
struct CUpti_ActivityMarker2
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMarker2) The activity record providing a marker which is an instantaneous point in time.

The marker is specified with a descriptive name and unique id (CUPTI_ACTIVITY_KIND_MARKER).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MARKER.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker25flagsE) The flags associated with the marker.

See also


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker29timestampE) The timestamp for the marker, in ns.

A value of 0 indicates that timestamp information could not be collected for the marker.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker22idE) The marker ID.


-
[CUpti_ActivityObjectKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityObjectKind)objectKind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker210objectKindE) The kind of activity object associated with this marker.


-
[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#_CPPv426CUpti_ActivityObjectKindId)objectId[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker28objectIdE) The identifier for the activity object associated with this marker.

‘objectKind’ indicates which ID is valid for this record.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker23padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker24nameE) The marker name for an instantaneous or start marker.

This will be NULL for an end marker.


-
const char *domain
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMarker26domainE) The name of the domain to which this marker belongs to.

This will be NULL for default domain.


-