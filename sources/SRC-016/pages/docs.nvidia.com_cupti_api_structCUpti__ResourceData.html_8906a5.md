source: https://docs.nvidia.com/cupti/api/structCUpti__ResourceData.html

# 7.216. CUpti_ResourceData[#](https://docs.nvidia.com#cupti-resourcedata)

-
struct CUpti_ResourceData
[#](https://docs.nvidia.com#_CPPv418CUpti_ResourceData) Data passed into a resource callback function.

Data passed into a resource callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_RESOURCE. The callback data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data.Public Members

-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ResourceData7contextE) For CUPTI_CBID_RESOURCE_CONTEXT_CREATED and CUPTI_CBID_RESOURCE_CONTEXT_DESTROY_STARTING, the context being created or destroyed.

For CUPTI_CBID_RESOURCE_STREAM_CREATED and CUPTI_CBID_RESOURCE_STREAM_DESTROY_STARTING, the context containing the stream being created or destroyed.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ResourceData6streamE) For CUPTI_CBID_RESOURCE_STREAM_CREATED and CUPTI_CBID_RESOURCE_STREAM_DESTROY_STARTING, the stream being created or destroyed.


-
void *resourceDescriptor
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ResourceData18resourceDescriptorE) Reserved for future use.


-
CUcontext context