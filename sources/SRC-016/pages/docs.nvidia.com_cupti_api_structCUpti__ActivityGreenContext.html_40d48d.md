source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityGreenContext.html

# 7.43. CUpti_ActivityGreenContext[#](https://docs.nvidia.com#cupti-activitygreencontext)

-
struct CUpti_ActivityGreenContext
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityGreenContext) The activity record for a green context.

This activity record represents information about a green context (CUPTI_ACTIVITY_KIND_GREEN_CONTEXT). Green context activity is now reported using

[CUpti_ActivityGreenContext2](https://docs.nvidia.com/structCUpti__ActivityGreenContext2.html#structcupti__activitygreencontext2)recordPublic Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_GREEN_CONTEXT.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext9contextIdE) The context ID of the green context.


-
uint32_t parentContextId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext15parentContextIdE) The ID of the parent context.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext8deviceIdE) The device ID associated with the green context.


-
uint32_t numTpcs
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext7numTpcsE) The number of TPCs allocated to the green context.


-
uint16_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext18numMultiprocessorsE) The number of multiprocessors (SMs) allocated to the green context.


-
uint8_t logicalTpcMaskSize
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext18logicalTpcMaskSizeE) The size (in 32-bit words) of the logical TPC mask stored in logicalTpcMask[].


-
uint8_t padding
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext7paddingE) Undefined.

Reserved for internal use.


-
uint32_t logicalTpcMask[32]
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityGreenContext14logicalTpcMaskE) Bitset of allocated TPC IDs represented as 32-bit words.

Valid words are specified by logicalTpcMaskSize; unused entries are zeroed. The array supports up to 1024 TPCs (32 words × 32 bits). Each bit represents a logical TPC ID assigned to the green context. For example, if bit k is set, logical TPC ID k is assigned to the context.

**Example: Interpreting the TPC Mask**For a green context with numTpcs=3, logicalTpcMaskSize=8, and logicalTpcMask={66,8,0,0,0,0,0,0}:

Word 0: Value 66 (binary: …01000010, showing lowest 8 bits of 32-bit word) indicates TPCs 1 and 6

Word 1: Value 8 (binary: …00001000) indicates TPC 35 (bit 3 of word 1, i.e., global TPC ID 32+3)

Each word is 32 bits covering TPCs 0-31 (word 0), 32-63 (word 1), etc.

To check if TPC N is allocated:

`(logicalTpcMask[N/32] & (1U << (N%32)))`

logicalTpcMaskSize indicates how many words in the array contain valid data




-