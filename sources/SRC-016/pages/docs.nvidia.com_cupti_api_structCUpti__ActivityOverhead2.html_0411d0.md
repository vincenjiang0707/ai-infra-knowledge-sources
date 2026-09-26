source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOverhead2.html

# 7.112. CUpti_ActivityOverhead2[#](https://docs.nvidia.com#cupti-activityoverhead2)

-
struct CUpti_ActivityOverhead2
[#](https://docs.nvidia.com#_CPPv423CUpti_ActivityOverhead2) The activity record for CUPTI and driver overheads.

This activity record provides CUPTI and driver overhead information (CUPTI_ACTIVITY_OVERHEAD).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead24kindE) The activity record kind, must be CUPTI_ACTIVITY_OVERHEAD.


-
[CUpti_ActivityOverheadKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_ActivityOverheadKind)overheadKind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead212overheadKindE) The kind of overhead, CUPTI, DRIVER, COMPILER etc.


-
[CUpti_ActivityObjectKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityObjectKind)objectKind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead210objectKindE) The kind of activity object that the overhead is associated with.


-
[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#_CPPv426CUpti_ActivityObjectKindId)objectId[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead28objectIdE) The identifier for the activity object.

‘objectKind’ indicates which ID is valid for this record.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead25startE) The start timestamp for the overhead, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the overhead.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead23endE) The end timestamp for the overhead, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the overhead.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead213correlationIdE) The correlation ID of the overhead operation to which records belong to.

This ID is identical to the correlation ID in the driver or runtime API activity record that launched the overhead operation. In some cases, it can be zero, such as for CUPTI_ACTIVITY_OVERHEAD_CUPTI_BUFFER_FLUSH records.


-
uint32_t reserved0
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead29reserved0E) Reserved for internal use.


-