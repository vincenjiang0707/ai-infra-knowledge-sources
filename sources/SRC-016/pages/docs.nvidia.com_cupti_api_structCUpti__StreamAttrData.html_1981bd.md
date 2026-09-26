source: https://docs.nvidia.com/cupti/api/structCUpti__StreamAttrData.html

# 7.231. CUpti_StreamAttrData[#](https://docs.nvidia.com#cupti-streamattrdata)

-
struct CUpti_StreamAttrData
[#](https://docs.nvidia.com#_CPPv420CUpti_StreamAttrData) Stream attribute data passed into a resource callback function for CUPTI_CBID_RESOURCE_STREAM_ATTRIBUTE_CHANGED callback.

Data passed into a resource callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_RESOURCE. The stream attribute data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data.