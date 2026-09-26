source: https://docs.nvidia.com/cupti/api/structCUpti__SynchronizeData.html

# 7.233. CUpti_SynchronizeData[#](https://docs.nvidia.com#cupti-synchronizedata)

-
struct CUpti_SynchronizeData
[#](https://docs.nvidia.com#_CPPv421CUpti_SynchronizeData) Data passed into a synchronize callback function.

Data passed into a synchronize callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_SYNCHRONIZE. The callback data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data.