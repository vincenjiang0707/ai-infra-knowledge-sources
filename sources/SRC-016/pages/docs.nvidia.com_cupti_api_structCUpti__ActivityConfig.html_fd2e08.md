source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityConfig.html

# 7.11. CUpti_ActivityConfig[#](https://docs.nvidia.com#cupti-activityconfig)

-
struct CUpti_ActivityConfig
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityConfig) Activity configuration.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityConfig10structSizeE) Size of the data structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[CUpti_ActivityFieldSelection](https://docs.nvidia.com/structCUpti__ActivityFieldSelection.html#_CPPv428CUpti_ActivityFieldSelection)fieldSelection[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityConfig14fieldSelectionE) Selection of the fields to collect for the activity kind.


-
void *pKindOptions
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityConfig12pKindOptionsE) Optional pointer to kind-specific options.

For CUPTI_ACTIVITY_KIND_RUNTIME and CUPTI_ACTIVITY_KIND_DRIVER, this may point to a

[CUpti_ActivityApiOptions](https://docs.nvidia.com/structCUpti__ActivityApiOptions.html#structcupti__activityapioptions)struct to enable allowlist or denylist filtering of individual cbids. NULL disables filtering (all cbids enabled). Ignored for all other activity kinds. Available since CUPTI_API_VERSION 130400.

-
size_t structSize