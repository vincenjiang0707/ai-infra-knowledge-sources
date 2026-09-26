source: https://docs.nvidia.com/cupti/api/structCUpti__BufferCallbackCompleteInfo.html

# 7.134. CUpti_BufferCallbackCompleteInfo[#](https://docs.nvidia.com#cupti-buffercallbackcompleteinfo)

-
struct CUpti_BufferCallbackCompleteInfo
[#](https://docs.nvidia.com#_CPPv432CUpti_BufferCallbackCompleteInfo) Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N32CUpti_BufferCallbackCompleteInfo10structSizeE) Size of the data structure.

CUPTI should set the size of the structure. It will be used by CUPTI clients to check what fields are available in the structure. Used to preserve backward compatibility.


-
uint64_t threadId
[#](https://docs.nvidia.com#_CPPv4N32CUpti_BufferCallbackCompleteInfo8threadIdE) The thread ID that triggered the buffer completion.

This field is useful when buffers are completed per-thread. Check CUpti_ActivityAttribute CUPTI_ACTIVITY_ATTR_PER_THREAD_ACTIVITY_BUFFER to know if per-thread activity buffers are enabled. For example: User can log which thread completed the buffer.


-
[CUpti_ActivityRecordLayout](https://docs.nvidia.com/structCUpti__ActivityRecordLayout.html#_CPPv426CUpti_ActivityRecordLayout)**ppRecordLayouts[#](https://docs.nvidia.com#_CPPv4N32CUpti_BufferCallbackCompleteInfo15ppRecordLayoutsE) Array of record layouts present in the buffer.

This field is useful when user-defined activity records are used. Check CUpti_ActivityAttribute CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS to know if user-defined activity records are enabled. For example: User can parse the buffer based on the record layouts.


-
size_t numRecordLayouts
[#](https://docs.nvidia.com#_CPPv4N32CUpti_BufferCallbackCompleteInfo16numRecordLayoutsE) Number of different record layouts present in the buffer.

This field is useful when user-defined activity records are used. Check CUpti_ActivityAttribute CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS to know if user-defined activity records are enabled. For example: User can parse the buffer based on the record layouts.


-
size_t structSize