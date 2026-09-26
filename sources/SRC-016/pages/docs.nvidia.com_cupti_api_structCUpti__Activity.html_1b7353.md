source: https://docs.nvidia.com/cupti/api/structCUpti__Activity.html

# 7.1. CUpti_Activity[#](https://docs.nvidia.com#cupti-activity)

-
struct CUpti_Activity
[#](https://docs.nvidia.com#_CPPv414CUpti_Activity) The base activity record.

The activity API uses a

[CUpti_Activity](https://docs.nvidia.com#structcupti__activity)as a generic representation for any activity. The ‘kind’ field is used to determine the specific activity kind, and from that the[CUpti_Activity](https://docs.nvidia.com#structcupti__activity)object can be cast to the specific activity record type appropriate for that kind.Note that all activity record types are padded and aligned to ensure that each member of the record is naturally aligned.

See also

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N14CUpti_Activity4kindE) The kind of this activity.


-