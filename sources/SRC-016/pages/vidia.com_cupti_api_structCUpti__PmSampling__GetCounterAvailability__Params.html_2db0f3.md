source: https://docs.nvidia.com/cupti/api/structCUpti__PmSampling__GetCounterAvailability__Params.html

# 7.160. CUpti_PmSampling_GetCounterAvailability_Params[#](https://docs.nvidia.com#cupti-pmsampling-getcounteravailability-params)

-
struct CUpti_PmSampling_GetCounterAvailability_Params
[#](https://docs.nvidia.com#_CPPv446CUpti_PmSampling_GetCounterAvailability_Params) Params for cuptiPmSamplingGetCounterData.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N46CUpti_PmSampling_GetCounterAvailability_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N46CUpti_PmSampling_GetCounterAvailability_Params5pPrivE) [in] Set to NULL.


-
size_t deviceIndex
[#](https://docs.nvidia.com#_CPPv4N46CUpti_PmSampling_GetCounterAvailability_Params11deviceIndexE) [in] Device index.


-
size_t counterAvailabilityImageSize
[#](https://docs.nvidia.com#_CPPv4N46CUpti_PmSampling_GetCounterAvailability_Params28counterAvailabilityImageSizeE) [inout] Size of the counter availability image. When pCounterAvailabilityImage is NULL, this field is used to return the size of the counter availability image.


-
uint8_t *pCounterAvailabilityImage
[#](https://docs.nvidia.com#_CPPv4N46CUpti_PmSampling_GetCounterAvailability_Params25pCounterAvailabilityImageE) [out] Counter availability image.


-
size_t structSize