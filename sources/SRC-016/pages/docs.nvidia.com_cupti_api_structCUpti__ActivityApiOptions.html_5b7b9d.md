source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityApiOptions.html

# 7.4. CUpti_ActivityApiOptions[#](https://docs.nvidia.com#cupti-activityapioptions)

-
struct CUpti_ActivityApiOptions
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityApiOptions) Kind-specific options for API activity kinds (RUNTIME, DRIVER).

Pass a pointer to this struct via

[CUpti_ActivityConfig::pKindOptions](https://docs.nvidia.com/structCUpti__ActivityConfig.html#structcupti__activityconfig_1a6e227752961d0cf29c563df06a6ec87c)when calling cuptiActivityEnable_v2 to enable only a subset of cbids (allowlist) or to exclude specific noisy cbids (denylist). Supported only for CUPTI_ACTIVITY_KIND_RUNTIME and CUPTI_ACTIVITY_KIND_DRIVER.**Since**CUPTI_API_VERSION 130400


Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityApiOptions10structSizeE) Size of the data structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[CUpti_ActivityApiCbidOptions](https://docs.nvidia.com/structCUpti__ActivityApiCbidOptions.html#_CPPv428CUpti_ActivityApiCbidOptions)*pCbidOptions[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityApiOptions12pCbidOptionsE) Pointer to per-cbid filter options.

If NULL, all cbids for the kind are enabled.