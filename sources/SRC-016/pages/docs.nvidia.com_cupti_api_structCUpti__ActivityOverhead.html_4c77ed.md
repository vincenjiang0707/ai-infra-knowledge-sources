source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOverhead.html

# 7.111. CUpti_ActivityOverhead[#](https://docs.nvidia.com#cupti-activityoverhead)

-
struct CUpti_ActivityOverhead
[#](https://docs.nvidia.com#_CPPv422CUpti_ActivityOverhead) The activity record for CUPTI and driver overheads.

(Deprecated in CUDA 12.2)

This activity record provides CUPTI and driver overhead information (CUPTI_ACTIVITY_OVERHEAD). These records are now reported using

[CUpti_ActivityOverhead3](https://docs.nvidia.com/structCUpti__ActivityOverhead3.html#structcupti__activityoverhead3)Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityOverhead4kindE) The activity record kind, must be CUPTI_ACTIVITY_OVERHEAD.


-
[CUpti_ActivityOverheadKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_ActivityOverheadKind)overheadKind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityOverhead12overheadKindE) The kind of overhead, CUPTI, DRIVER, COMPILER etc.


-
[CUpti_ActivityObjectKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityObjectKind)objectKind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityOverhead10objectKindE) The kind of activity object that the overhead is associated with.


-
[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#_CPPv426CUpti_ActivityObjectKindId)objectId[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityOverhead8objectIdE) The identifier for the activity object.

‘objectKind’ indicates which ID is valid for this record.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityOverhead5startE) The start timestamp for the overhead, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the overhead.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityOverhead3endE) The end timestamp for the overhead, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the overhead.


-