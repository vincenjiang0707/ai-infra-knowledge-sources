source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOverhead3.html

# 7.113. CUpti_ActivityOverhead3[#](https://docs.nvidia.com#cupti-activityoverhead3)

-
struct CUpti_ActivityOverhead3
[#](https://docs.nvidia.com#_CPPv423CUpti_ActivityOverhead3) The activity record for CUPTI and driver overheads.

This activity record provides CUPTI and driver overhead information (CUPTI_ACTIVITY_KIND_OVERHEAD).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead34kindE) The activity record kind, must be CUPTI_ACTIVITY_OVERHEAD.


-
[CUpti_ActivityOverheadKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_ActivityOverheadKind)overheadKind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead312overheadKindE) The kind of overhead, CUPTI, DRIVER, COMPILER etc.


-
[CUpti_ActivityObjectKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityObjectKind)objectKind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead310objectKindE) The kind of activity object that the overhead is associated with.


-
[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#_CPPv426CUpti_ActivityObjectKindId)objectId[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead38objectIdE) The identifier for the activity object.

‘objectKind’ indicates which ID is valid for this record.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead35startE) The start timestamp for the overhead, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the overhead.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead33endE) The end timestamp for the overhead, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the overhead.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead313correlationIdE) The correlation ID of the overhead operation to which records belong to.

This ID is identical to the correlation ID in the driver or runtime API activity record that launched the overhead operation. In some cases, it can be zero, such as for CUPTI_ACTIVITY_OVERHEAD_CUPTI_BUFFER_FLUSH records.


-
uint32_t reserved0
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead39reserved0E) Reserved for internal use.


-
void *overheadData
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityOverhead312overheadDataE) Pointer to the struct with additional details about the overhead.

Refer CUpti_ActivityOverheadKind enum and the corresponding structure to typecast and access additional overhead data. Client is responsible for freeing this memory using the free function when done.


-