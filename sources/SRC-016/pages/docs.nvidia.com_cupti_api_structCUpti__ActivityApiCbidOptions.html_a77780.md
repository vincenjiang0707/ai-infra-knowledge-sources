source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityApiCbidOptions.html

# 7.3. CUpti_ActivityApiCbidOptions[#](https://docs.nvidia.com#cupti-activityapicbidoptions)

-
struct CUpti_ActivityApiCbidOptions
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityApiCbidOptions) Per-cbid enable/disable options for API activity kinds.

When enable = 1 (allowlist), records are generated only for the cbids listed in pCbids. When enable = 0 (denylist), records are generated for all cbids except those listed.

**Since**CUPTI_API_VERSION 130400


Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityApiCbidOptions10structSizeE) Size of the data structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[CUpti_CallbackId](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv416CUpti_CallbackId)*pCbids[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityApiCbidOptions6pCbidsE) Array of callback IDs to allow or deny.

Must not be NULL when numCbids > 0.


-
size_t numCbids
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityApiCbidOptions8numCbidsE) Number of entries in pCbids.


-
uint8_t enable
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityApiCbidOptions6enableE) 1 = allowlist (record only the listed cbids); 0 = denylist (suppress the listed cbids).