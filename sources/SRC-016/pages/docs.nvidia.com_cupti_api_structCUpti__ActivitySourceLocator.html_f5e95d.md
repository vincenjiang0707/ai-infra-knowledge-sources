source: https://docs.nvidia.com/cupti/api/structCUpti__ActivitySourceLocator.html

# 7.126. CUpti_ActivitySourceLocator[#](https://docs.nvidia.com#cupti-activitysourcelocator)

-
struct CUpti_ActivitySourceLocator
[#](https://docs.nvidia.com#_CPPv427CUpti_ActivitySourceLocator) The activity record for source locator.

This activity record represents a source locator (CUPTI_ACTIVITY_KIND_SOURCE_LOCATOR).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivitySourceLocator4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_SOURCE_LOCATOR.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivitySourceLocator2idE) The ID for the source path, will be used in all the source level results.


-
uint32_t lineNumber
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivitySourceLocator10lineNumberE) The line number in the source .


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivitySourceLocator3padE) Undefined.

Reserved for internal use.


-
const char *fileName
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivitySourceLocator8fileNameE) The path for the file.


-