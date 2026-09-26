source: https://docs.nvidia.com/cupti/api/group__CUPTI__CALLBACK__API.html

# 6.2. CUPTI Callback API[#](https://docs.nvidia.com#cupti-callback-api)

Functions, types, and enums that implement the CUPTI Callback API.

## 6.2.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_CallbackData](https://docs.nvidia.com/structCUpti__CallbackData.html#structcupti__callbackdata)Data passed into a runtime or driver API callback function.

[CUpti_GraphData](https://docs.nvidia.com/structCUpti__GraphData.html#structcupti__graphdata)CUDA graphs data passed into a resource callback function.

[CUpti_ModuleResourceData](https://docs.nvidia.com/structCUpti__ModuleResourceData.html#structcupti__moduleresourcedata)Module data passed into a resource callback function.

[CUpti_NvtxData](https://docs.nvidia.com/structCUpti__NvtxData.html#structcupti__nvtxdata)Data passed into a NVTX callback function.

[CUpti_ResourceData](https://docs.nvidia.com/structCUpti__ResourceData.html#structcupti__resourcedata)Data passed into a resource callback function.

[CUpti_StateData](https://docs.nvidia.com/structCUpti__StateData.html#structcupti__statedata)Data passed into a State callback function.

[CUpti_StreamAttrData](https://docs.nvidia.com/structCUpti__StreamAttrData.html#structcupti__streamattrdata)Stream attribute data passed into a resource callback function for CUPTI_CBID_RESOURCE_STREAM_ATTRIBUTE_CHANGED callback.

[CUpti_SubscriberParams](https://docs.nvidia.com/structCUpti__SubscriberParams.html#structcupti__subscriberparams)Params for cuptiSubscribe_v2.

[CUpti_SynchronizeData](https://docs.nvidia.com/structCUpti__SynchronizeData.html#structcupti__synchronizedata)Data passed into a synchronize callback function.


## 6.2.2. Macros[#](https://docs.nvidia.com#macros)

[CUPTI_CALLBACK_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__callback__api_1ga470788380856be7ad17a13de85bab6ba)[CUPTI_OLD_SUBSCRIBER_NAME_MIN_LEN](https://docs.nvidia.com#group__cupti__callback__api_1ga34177c0832f7d6257d999ab2aa4d3409)The minimum size of the of the old subscriber name in bytes.

[CUPTI_SUBSCRIBER_NAME_MAX_LEN](https://docs.nvidia.com#group__cupti__callback__api_1ga4c4c749be4ae3d32eb11a76ab25551e3)The max size of the CUPTI subscriber name in bytes.

[CUpti_SubscriberParams_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__callback__api_1ga5236b3cf3c9bc40c1be03f13708bbfc8)

## 6.2.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_ApiCallbackSite](https://docs.nvidia.com#group__cupti__callback__api_1ga7bd557c9b3084014c680b9925842be24)Specifies the point in an API call that a callback is issued.

[CUpti_CallbackDomain](https://docs.nvidia.com#group__cupti__callback__api_1ga9e77154dbe0cc07fb9332f95a83d6d9e)Callback domains.

[CUpti_CallbackIdResource](https://docs.nvidia.com#group__cupti__callback__api_1ga690fb2a42aefe39f00033c957ce211b2)Callback IDs for resource domain.

[CUpti_CallbackIdState](https://docs.nvidia.com#group__cupti__callback__api_1ga6658126cabc47048530173d4b03488aa)Callback IDs for state domain.

[CUpti_CallbackIdSync](https://docs.nvidia.com#group__cupti__callback__api_1gacaeba9950bf4f48ea7ab9a0402dc7e6f)Callback IDs for synchronization domain.


## 6.2.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiEnableAllDomains](https://docs.nvidia.com#group__cupti__callback__api_1ga7dcebeb8ae4f79c90905a8f6befc51d7)(uint32_t enable, CUpti_SubscriberHandle subscriber) Enable or disable all callbacks in all domains.

- CUptiResult
[cuptiEnableCallback](https://docs.nvidia.com#group__cupti__callback__api_1gace619a64b77d6533754de798b5e8263e)(uint32_t enable, CUpti_SubscriberHandle subscriber, CUpti_CallbackDomain domain, CUpti_CallbackId cbid) Enable or disabled callbacks for a specific domain and callback ID.

- CUptiResult
[cuptiEnableDomain](https://docs.nvidia.com#group__cupti__callback__api_1ga926699208431270d4197fcb639da6a5c)(uint32_t enable, CUpti_SubscriberHandle subscriber, CUpti_CallbackDomain domain) Enable or disabled all callbacks for a specific domain.

- CUptiResult
[cuptiGetCallbackName](https://docs.nvidia.com#group__cupti__callback__api_1ga0fe2357995aa7861a37e5896c6a18635)(CUpti_CallbackDomain domain, uint32_t cbid, const char **name) Get the name of a callback for a specific domain and callback ID.

- CUptiResult
[cuptiGetCallbackState](https://docs.nvidia.com#group__cupti__callback__api_1gaf861e55f8d61286b97471e2bede138a6)(uint32_t *enable, CUpti_SubscriberHandle subscriber, CUpti_CallbackDomain domain, CUpti_CallbackId cbid) Get the current enabled/disabled state of a callback for a specific domain and function ID.

- CUptiResult
[cuptiGetEnabledCallbacks](https://docs.nvidia.com#group__cupti__callback__api_1ga4c220899637b259d9901e6e772156e95)(CUpti_SubscriberHandle subscriber, CUpti_CallbackDomain domain, CUpti_CallbackId *buffer, uint32_t *bufferSize, uint32_t *enabledCallbacksCount) Get the enabled callbacks for a subscriber.

- CUptiResult
[cuptiSubscribe](https://docs.nvidia.com#group__cupti__callback__api_1gad2c32850b2e03b37e284df083dc9053f)(CUpti_SubscriberHandle *subscriber, CUpti_CallbackFunc callback, void *userdata) Initialize a callback subscriber with a callback function and user data.

- CUptiResult
[cuptiSubscribe_v2](https://docs.nvidia.com#group__cupti__callback__api_1ga817004c126bedadf956162f20de18491)(CUpti_SubscriberHandle *subscriber, CUpti_CallbackFunc callback, void *userdata, CUpti_SubscriberParams *pParams) Initialize a callback subscriber with a callback function and user data.

- CUptiResult
[cuptiSupportedDomains](https://docs.nvidia.com#group__cupti__callback__api_1ga4526fa1776292fa325971e815e0c7dc2)(size_t *domainCount, CUpti_DomainTable *domainTable) Get the available callback domains.

- CUptiResult
[cuptiUnsubscribe](https://docs.nvidia.com#group__cupti__callback__api_1ga20b68c9c33f129179b56687a17356682)(CUpti_SubscriberHandle subscriber) Unregister a callback subscriber.


## 6.2.5. Typedefs[#](https://docs.nvidia.com#typedefs)

[CUpti_CallbackFunc](https://docs.nvidia.com#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c)Function type for a callback.

[CUpti_CallbackId](https://docs.nvidia.com#group__cupti__callback__api_1ga7fde6b76bdbcafbcf750b0f91a3484f8)An ID for a driver API, runtime API, resource or synchronization callback.

[CUpti_DomainTable](https://docs.nvidia.com#group__cupti__callback__api_1ga76b7ef0d7caebdcae0880e218185950b)Pointer to an array of callback domains.

[CUpti_SubscriberHandle](https://docs.nvidia.com#group__cupti__callback__api_1ga7932f010e8b2c785d85f4048235afca3)A callback subscriber.


## 6.2.6. Macros[#](https://docs.nvidia.com#id1)

-
CUPTI_CALLBACK_STRUCT_SIZE(
*type_*,*lastfield_*)[#](https://docs.nvidia.com#c.CUPTI_CALLBACK_STRUCT_SIZE)

-
CUPTI_OLD_SUBSCRIBER_NAME_MIN_LEN
[#](https://docs.nvidia.com#c.CUPTI_OLD_SUBSCRIBER_NAME_MIN_LEN) The minimum size of the of the old subscriber name in bytes.


-
CUPTI_SUBSCRIBER_NAME_MAX_LEN
[#](https://docs.nvidia.com#c.CUPTI_SUBSCRIBER_NAME_MAX_LEN) The max size of the CUPTI subscriber name in bytes.

The total size of the CUPTI subscriber name is 64 bytes. CUPTI adds a 10 byte prefix and a null terminator, leaving 53 bytes for the user supplied subscriber name.


-
CUpti_SubscriberParams_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SubscriberParams_STRUCT_SIZE)

## 6.2.7. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_ApiCallbackSite
[#](https://docs.nvidia.com#_CPPv421CUpti_ApiCallbackSite) Specifies the point in an API call that a callback is issued.

Specifies the point in an API call that a callback is issued. This value is communicated to the callback function via

[CUpti_CallbackData::callbackSite](https://docs.nvidia.com/structCUpti__CallbackData.html#structcupti__callbackdata_1a01337ce329bea0e08d803cb99c1f1f01).*Values:*-
enumerator CUPTI_API_ENTER
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ApiCallbackSite15CUPTI_API_ENTERE) The callback is at the entry of the API call.


-
enumerator CUPTI_API_EXIT
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ApiCallbackSite14CUPTI_API_EXITE) The callback is at the exit of the API call.


-
enumerator CUPTI_API_CBSITE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ApiCallbackSite26CUPTI_API_CBSITE_FORCE_INTE)

-
enumerator CUPTI_API_ENTER

-
enum CUpti_CallbackDomain
[#](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain) Callback domains.

Callback domains. Each domain represents callback points for a group of related API functions or CUDA driver activity.

*Values:*-
enumerator CUPTI_CB_DOMAIN_INVALID
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain23CUPTI_CB_DOMAIN_INVALIDE) Invalid domain.


-
enumerator CUPTI_CB_DOMAIN_DRIVER_API
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain26CUPTI_CB_DOMAIN_DRIVER_APIE) Domain containing callback points for all driver API functions.


-
enumerator CUPTI_CB_DOMAIN_RUNTIME_API
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain27CUPTI_CB_DOMAIN_RUNTIME_APIE) Domain containing callback points for all runtime API functions.


-
enumerator CUPTI_CB_DOMAIN_RESOURCE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain24CUPTI_CB_DOMAIN_RESOURCEE) Domain containing callback points for CUDA resource tracking.


-
enumerator CUPTI_CB_DOMAIN_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain27CUPTI_CB_DOMAIN_SYNCHRONIZEE) Domain containing callback points for CUDA synchronization.


-
enumerator CUPTI_CB_DOMAIN_NVTX
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain20CUPTI_CB_DOMAIN_NVTXE) Domain containing callback points for NVTX API functions.


-
enumerator CUPTI_CB_DOMAIN_STATE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain21CUPTI_CB_DOMAIN_STATEE) Domain containing callback points for various states.


-
enumerator CUPTI_CB_DOMAIN_SIZE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain20CUPTI_CB_DOMAIN_SIZEE)

-
enumerator CUPTI_CB_DOMAIN_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackDomain25CUPTI_CB_DOMAIN_FORCE_INTE)

-
enumerator CUPTI_CB_DOMAIN_INVALID

-
enum CUpti_CallbackIdResource
[#](https://docs.nvidia.com#_CPPv424CUpti_CallbackIdResource) Callback IDs for resource domain.

Callback IDs for resource domain, CUPTI_CB_DOMAIN_RESOURCE. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator CUPTI_CBID_RESOURCE_INVALID
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource27CUPTI_CBID_RESOURCE_INVALIDE) Invalid resource callback ID.


-
enumerator CUPTI_CBID_RESOURCE_CONTEXT_CREATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource35CUPTI_CBID_RESOURCE_CONTEXT_CREATEDE) A new context has been created.


-
enumerator CUPTI_CBID_RESOURCE_CONTEXT_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource44CUPTI_CBID_RESOURCE_CONTEXT_DESTROY_STARTINGE) A context is about to be destroyed.


-
enumerator CUPTI_CBID_RESOURCE_STREAM_CREATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource34CUPTI_CBID_RESOURCE_STREAM_CREATEDE) A new stream has been created.


-
enumerator CUPTI_CBID_RESOURCE_STREAM_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource43CUPTI_CBID_RESOURCE_STREAM_DESTROY_STARTINGE) A stream is about to be destroyed.


-
enumerator CUPTI_CBID_RESOURCE_CU_INIT_FINISHED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource36CUPTI_CBID_RESOURCE_CU_INIT_FINISHEDE) The driver has finished initializing.


-
enumerator CUPTI_CBID_RESOURCE_MODULE_LOADED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource33CUPTI_CBID_RESOURCE_MODULE_LOADEDE) A module has been loaded.


-
enumerator CUPTI_CBID_RESOURCE_MODULE_UNLOAD_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource42CUPTI_CBID_RESOURCE_MODULE_UNLOAD_STARTINGE) A module is about to be unloaded.


-
enumerator CUPTI_CBID_RESOURCE_MODULE_PROFILED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource35CUPTI_CBID_RESOURCE_MODULE_PROFILEDE) The current module which is being profiled.


-
enumerator CUPTI_CBID_RESOURCE_GRAPH_CREATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource33CUPTI_CBID_RESOURCE_GRAPH_CREATEDE) CUDA graph has been created.


-
enumerator CUPTI_CBID_RESOURCE_GRAPH_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource42CUPTI_CBID_RESOURCE_GRAPH_DESTROY_STARTINGE) CUDA graph is about to be destroyed.


-
enumerator CUPTI_CBID_RESOURCE_GRAPH_CLONED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource32CUPTI_CBID_RESOURCE_GRAPH_CLONEDE) CUDA graph is cloned.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHNODE_CREATE_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource45CUPTI_CBID_RESOURCE_GRAPHNODE_CREATE_STARTINGE) CUDA graph node is about to be created.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHNODE_CREATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource37CUPTI_CBID_RESOURCE_GRAPHNODE_CREATEDE) CUDA graph node is created.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHNODE_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource46CUPTI_CBID_RESOURCE_GRAPHNODE_DESTROY_STARTINGE) CUDA graph node is about to be destroyed.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHNODE_DEPENDENCY_CREATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource48CUPTI_CBID_RESOURCE_GRAPHNODE_DEPENDENCY_CREATEDE) Dependency on a CUDA graph node is created.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHNODE_DEPENDENCY_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource57CUPTI_CBID_RESOURCE_GRAPHNODE_DEPENDENCY_DESTROY_STARTINGE) Dependency on a CUDA graph node is destroyed.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHEXEC_CREATE_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource45CUPTI_CBID_RESOURCE_GRAPHEXEC_CREATE_STARTINGE) An executable CUDA graph is about to be created.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHEXEC_CREATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource37CUPTI_CBID_RESOURCE_GRAPHEXEC_CREATEDE) An executable CUDA graph is created.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHEXEC_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource46CUPTI_CBID_RESOURCE_GRAPHEXEC_DESTROY_STARTINGE) An executable CUDA graph is about to be destroyed.


-
enumerator CUPTI_CBID_RESOURCE_GRAPHNODE_CLONED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource36CUPTI_CBID_RESOURCE_GRAPHNODE_CLONEDE) CUDA graph node is cloned.


-
enumerator CUPTI_CBID_RESOURCE_STREAM_ATTRIBUTE_CHANGED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource44CUPTI_CBID_RESOURCE_STREAM_ATTRIBUTE_CHANGEDE) CUDA stream attribute is changed.


-
enumerator CUPTI_CBID_RESOURCE_GRAPH_NODE_UPDATED
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource38CUPTI_CBID_RESOURCE_GRAPH_NODE_UPDATEDE) CUDA graph node is updated.


-
enumerator CUPTI_CBID_RESOURCE_GRAPH_NODE_SET_PARAMS
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource41CUPTI_CBID_RESOURCE_GRAPH_NODE_SET_PARAMSE) Params are set for the CUDA graph node in the executable graph.


-
enumerator CUPTI_CBID_RESOURCE_SIZE
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource24CUPTI_CBID_RESOURCE_SIZEE)

-
enumerator CUPTI_CBID_RESOURCE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24CUpti_CallbackIdResource29CUPTI_CBID_RESOURCE_FORCE_INTE)

-
enumerator CUPTI_CBID_RESOURCE_INVALID

-
enum CUpti_CallbackIdState
[#](https://docs.nvidia.com#_CPPv421CUpti_CallbackIdState) Callback IDs for state domain.

Callback IDs for state domain, CUPTI_CB_DOMAIN_STATE. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator CUPTI_CBID_STATE_INVALID
[#](https://docs.nvidia.com#_CPPv4N21CUpti_CallbackIdState24CUPTI_CBID_STATE_INVALIDE) Invalid state callback ID.


-
enumerator CUPTI_CBID_STATE_FATAL_ERROR
[#](https://docs.nvidia.com#_CPPv4N21CUpti_CallbackIdState28CUPTI_CBID_STATE_FATAL_ERRORE) Notification of fatal errors - high impact, non-recoverable When encountered, CUPTI automatically invokes

[cuptiFinalize()](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1gaad1be905ea718ed54246e52e02667e8f)User can control behavior of the application in future from receiving this callback - such as continuing without profiling, or terminating the whole application.

-
enumerator CUPTI_CBID_STATE_ERROR
[#](https://docs.nvidia.com#_CPPv4N21CUpti_CallbackIdState22CUPTI_CBID_STATE_ERRORE) Notification of non fatal errors - high impact, but recoverable.


-
enumerator CUPTI_CBID_STATE_WARNING
[#](https://docs.nvidia.com#_CPPv4N21CUpti_CallbackIdState24CUPTI_CBID_STATE_WARNINGE) Notification of warnings - low impact, recoverable.


-
enumerator CUPTI_CBID_STATE_SIZE
[#](https://docs.nvidia.com#_CPPv4N21CUpti_CallbackIdState21CUPTI_CBID_STATE_SIZEE)

-
enumerator CUPTI_CBID_STATE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N21CUpti_CallbackIdState26CUPTI_CBID_STATE_FORCE_INTE)

-
enumerator CUPTI_CBID_STATE_INVALID

-
enum CUpti_CallbackIdSync
[#](https://docs.nvidia.com#_CPPv420CUpti_CallbackIdSync) Callback IDs for synchronization domain.

Callback IDs for synchronization domain, CUPTI_CB_DOMAIN_SYNCHRONIZE. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator CUPTI_CBID_SYNCHRONIZE_INVALID
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackIdSync30CUPTI_CBID_SYNCHRONIZE_INVALIDE) Invalid synchronize callback ID.


-
enumerator CUPTI_CBID_SYNCHRONIZE_STREAM_SYNCHRONIZED
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackIdSync42CUPTI_CBID_SYNCHRONIZE_STREAM_SYNCHRONIZEDE) Stream synchronization has completed for the stream.


-
enumerator CUPTI_CBID_SYNCHRONIZE_CONTEXT_SYNCHRONIZED
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackIdSync43CUPTI_CBID_SYNCHRONIZE_CONTEXT_SYNCHRONIZEDE) Context synchronization has completed for the context.


-
enumerator CUPTI_CBID_SYNCHRONIZE_SIZE
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackIdSync27CUPTI_CBID_SYNCHRONIZE_SIZEE)

-
enumerator CUPTI_CBID_SYNCHRONIZE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N20CUpti_CallbackIdSync32CUPTI_CBID_SYNCHRONIZE_FORCE_INTE)

-
enumerator CUPTI_CBID_SYNCHRONIZE_INVALID

## 6.2.8. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiEnableAllDomains( *uint32_t enable*,,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)subscriberEnable or disable all callbacks in all domains.

Enable or disable all callbacks in all domains.

Note

**Thread-safety**: a subscriber must serialize access to cuptiGetCallbackState, cuptiEnableCallback, cuptiEnableDomain, and cuptiEnableAllDomains. For example, if cuptiGetCallbackState(sub,

d, *) and cuptiEnableAllDomains(sub) are called concurrently, the results are undefined.

- Parameters:
**enable**– New enable state for all callbacks in all domain. Zero disables all callbacks, non-zero enables all callbacks.**subscriber**– - Handle to callback subscription

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialized CUPTI**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

is invalid



[#](https://docs.nvidia.com#_CPPv421cuptiEnableAllDomains8uint32_t22CUpti_SubscriberHandle)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiEnableCallback( *uint32_t enable*,,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)domain,[CUpti_CallbackId](https://docs.nvidia.com#_CPPv416CUpti_CallbackId)cbidEnable or disabled callbacks for a specific domain and callback ID.

Enable or disabled callbacks for a subscriber for a specific domain and callback ID.

Note

**Thread-safety**: a subscriber must serialize access to cuptiGetCallbackState, cuptiEnableCallback, cuptiEnableDomain, and cuptiEnableAllDomains. For example, if cuptiGetCallbackState(sub,

d, c) and cuptiEnableCallback(sub, d, c) are called concurrently, the results are undefined.

- Parameters:
**enable**– New enable state for the callback. Zero disables the callback, non-zero enables the callback.**subscriber**– - Handle to callback subscription**domain**– The domain of the callback**cbid**– The ID of the callback

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialized CUPTI**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

,`domain`

or`cbid`

is invalid.



[#](https://docs.nvidia.com#_CPPv419cuptiEnableCallback8uint32_t22CUpti_SubscriberHandle20CUpti_CallbackDomain16CUpti_CallbackId)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiEnableDomain( *uint32_t enable*,,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)domainEnable or disabled all callbacks for a specific domain.

Enable or disabled all callbacks for a specific domain.

Note

**Thread-safety**: a subscriber must serialize access to cuptiGetCallbackState, cuptiEnableCallback, cuptiEnableDomain, and cuptiEnableAllDomains. For example, if cuptiGetCallbackEnabled(sub,

d, *) and cuptiEnableDomain(sub, d) are called concurrently, the results are undefined.

- Parameters:
**enable**– New enable state for all callbacks in the domain. Zero disables all callbacks, non-zero enables all callbacks.**subscriber**– - Handle to callback subscription**domain**– The domain of the callback

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialized CUPTI**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

or`domain`

is invalid



[#](https://docs.nvidia.com#_CPPv417cuptiEnableDomain8uint32_t22CUpti_SubscriberHandle20CUpti_CallbackDomain)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetCallbackName( ,[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)domain*uint32_t cbid*,*const char **name*,Get the name of a callback for a specific domain and callback ID.

Returns a pointer to the name c_string in

`**name`

.Note

**Names**are available only for the DRIVER and RUNTIME domains.- Parameters:
**domain**– The domain of the callback**cbid**– The ID of the callback**name**– Returns pointer to the name string on success, NULL otherwise

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_INVALID_PARAMETER**– if`name`

is NULL, or if`domain`

or`cbid`

is invalid.



[#](https://docs.nvidia.com#_CPPv420cuptiGetCallbackName20CUpti_CallbackDomain8uint32_tPPKc)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetCallbackState( *uint32_t *enable*,,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)domain,[CUpti_CallbackId](https://docs.nvidia.com#_CPPv416CUpti_CallbackId)cbidGet the current enabled/disabled state of a callback for a specific domain and function ID.

Returns non-zero in

`*enable`

if the callback for a domain and callback ID is enabled, and zero if not enabled.Note

**Thread-safety**: a subscriber must serialize access to cuptiGetCallbackState, cuptiEnableCallback, cuptiEnableDomain, and cuptiEnableAllDomains. For example, if cuptiGetCallbackState(sub,

d, c) and cuptiEnableCallback(sub, d, c) are called concurrently, the results are undefined.

- Parameters:
**enable**– Returns non-zero if callback enabled, zero if not enabled**subscriber**– Handle to the initialize subscriber**domain**– The domain of the callback**cbid**– The ID of the callback

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialized CUPTI**CUPTI_ERROR_INVALID_PARAMETER**– if`enabled`

is NULL, or if`subscriber`

,`domain`

or`cbid`

is invalid.



[#](https://docs.nvidia.com#_CPPv421cuptiGetCallbackStateP8uint32_t22CUpti_SubscriberHandle20CUpti_CallbackDomain16CUpti_CallbackId)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetEnabledCallbacks( ,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)subscriber,[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)domain,[CUpti_CallbackId](https://docs.nvidia.com#_CPPv416CUpti_CallbackId)*buffer*uint32_t *bufferSize*,*uint32_t *enabledCallbacksCount*,Get the enabled callbacks for a subscriber.

Note

If the provided buffer size is not sufficient to store all the enabled callbacks, we populate the buffer with as much as we can, but return the true value of the number of enabled callbacks in

`enabledCallbacksCount`

.- Parameters:
**subscriber**– The subscriber handle. If NULL, the union of callbacks (for that domain) enabled across all subscribers is returned.**domain**– The domain of the callbacks to get. If NULL, CUPTI_ERROR_INVALID_PARAMETER is returned.**buffer**– The buffer to store the enabled callbacks. If NULL, the number of enabled callbacks is returned in`enabledCallbacksCount`

.**bufferSize**– The size of the buffer. If NULL, only the number of enabled callbacks is returned in`enabledCallbacksCount`

. If NULL and`buffer`

is not NULL, CUPTI_ERROR_INVALID_PARAMETER is returned.**enabledCallbacksCount**– The number of enabled callbacks. If NULL, CUPTI_ERROR_INVALID_PARAMETER is returned.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`enabledCallbacksCount`

is NULL, or if`subscriber`

or`domain`

is invalid.



[#](https://docs.nvidia.com#_CPPv424cuptiGetEnabledCallbacks22CUpti_SubscriberHandle20CUpti_CallbackDomainP16CUpti_CallbackIdP8uint32_tP8uint32_t)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSubscribe( ,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)*subscriber,[CUpti_CallbackFunc](https://docs.nvidia.com#_CPPv418CUpti_CallbackFunc)callback*void *userdata*,Initialize a callback subscriber with a callback function and user data.

Initializes a callback subscriber with a callback function and (optionally) a pointer to user data. The returned subscriber handle can be used to enable and disable the callback for specific domains and callback IDs.

Note

Only a single subscriber can be registered at a time. To ensure that no other CUPTI client interrupts the profiling session, it’s the responsibility of all the CUPTI clients to call this function before starting the profling session. In case profiling session is already started by another CUPTI client, this function returns the error code CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED. Note that this function returns the same error when application is launched using NVIDIA tools like Nsight Systems, Nsight Compute, cuda-gdb and cuda-memcheck.

Note

This function does not enable any callbacks.

Note

**Thread-safety**: this function is thread safe.Note

This API will be deprecated in a future release. The corresponding V2 API is

[cuptiSubscribe_v2](https://docs.nvidia.com#group__cupti__callback__api_1ga817004c126bedadf956162f20de18491). See the V1 to V2 API Migration section in the CUPTI documentation for more details.- Parameters:
**subscriber**– Returns handle to initialize subscriber**callback**– The callback function**userdata**– A pointer to user data. This data will be passed to the callback function via the`userdata`

parameter.

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialize CUPTI**CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED**– if there is already a CUPTI subscriber, or if the application is launched with NVIDIA tools like Nsight Systems, Nsight Compute, cuda-gdb and cuda-memcheck.**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

is NULL



[#](https://docs.nvidia.com#_CPPv414cuptiSubscribeP22CUpti_SubscriberHandle18CUpti_CallbackFuncPv)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSubscribe_v2( ,[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)*subscriber,[CUpti_CallbackFunc](https://docs.nvidia.com#_CPPv418CUpti_CallbackFunc)callback*void *userdata*,,[CUpti_SubscriberParams](https://docs.nvidia.com/structCUpti__SubscriberParams.html#_CPPv422CUpti_SubscriberParams)*pParamsInitialize a callback subscriber with a callback function and user data.

Initializes a callback subscriber with a callback function and (optionally) a pointer to user data. The returned subscriber handle can be used to enable and disable the callback for specific domains and callback IDs.

Note

Only a single subscriber can be registered at a time. To ensure that no other CUPTI client interrupts the profiling session, it’s the responsibility of all the CUPTI clients to call this function before starting the profling session. In case profiling session is already started by another CUPTI client, this function returns the error code CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED. Note that this function returns the same error when application is launched using NVIDIA tools like Nsight Systems, Nsight Compute, cuda-gdb and cuda-memcheck.

Note

This function does not enable any callbacks.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**subscriber**– Returns handle to initialize subscriber**callback**– The callback function**userdata**– A pointer to user data. This data will be passed to the callback function via the`userdata`

parameter.**pParams**– A pointer to[CUpti_SubscriberParams](https://docs.nvidia.com/structCUpti__SubscriberParams.html#structcupti__subscriberparams). Can be NULL.

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialize CUPTI**CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED**– if there is already a CUPTI subscriber, or if the application is launched with NVIDIA tools like Nsight Systems, Nsight Compute, cuda-gdb and cuda-memcheck.**CUPTI_ERROR_INVALID_PARAMETER**– if:`pParams.structSize`

is not filled with the size of the structure




[#](https://docs.nvidia.com#_CPPv417cuptiSubscribe_v2P22CUpti_SubscriberHandle18CUpti_CallbackFuncPvP22CUpti_SubscriberParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSupportedDomains( *size_t *domainCount*,,[CUpti_DomainTable](https://docs.nvidia.com#_CPPv417CUpti_DomainTable)*domainTableGet the available callback domains.

Returns in

`*domainTable`

an array of size`*domainCount`

of all the available callback domains.Note

**Thread-safety**: this function is thread safe.- Parameters:
**domainCount**– Returns number of callback domains**domainTable**– Returns pointer to array of available callback domains

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialize CUPTI**CUPTI_ERROR_INVALID_PARAMETER**– if`domainCount`

or`domainTable`

are NULL



[#](https://docs.nvidia.com#_CPPv421cuptiSupportedDomainsP6size_tP17CUpti_DomainTable)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiUnsubscribe()[CUpti_SubscriberHandle](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle)subscriber[#](https://docs.nvidia.com#_CPPv416cuptiUnsubscribe22CUpti_SubscriberHandle) Unregister a callback subscriber.

Removes a callback subscriber so that no future callbacks will be issued to that subscriber.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**subscriber**– Handle to the initialize subscriber- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_NOT_INITIALIZED**– if unable to initialized CUPTI**CUPTI_ERROR_INVALID_PARAMETER**– if`subscriber`

is NULL or not initialized



## 6.2.9. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef void (*CUpti_CallbackFunc)(void *userdata,
[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)domain,[CUpti_CallbackId](https://docs.nvidia.com#_CPPv416CUpti_CallbackId)cbid, const void *cbdata)[#](https://docs.nvidia.com#_CPPv418CUpti_CallbackFunc) Function type for a callback.

Function type for a callback. The type of the data passed to the callback in

`cbdata`

depends on the`domain`

. If`domain`

is CUPTI_CB_DOMAIN_DRIVER_API or CUPTI_CB_DOMAIN_RUNTIME_API the type of`cbdata`

will be[CUpti_CallbackData](https://docs.nvidia.com/structCUpti__CallbackData.html#structcupti__callbackdata). If`domain`

is CUPTI_CB_DOMAIN_RESOURCE the type of`cbdata`

will be[CUpti_ResourceData](https://docs.nvidia.com/structCUpti__ResourceData.html#structcupti__resourcedata). If`domain`

is CUPTI_CB_DOMAIN_SYNCHRONIZE the type of`cbdata`

will be[CUpti_SynchronizeData](https://docs.nvidia.com/structCUpti__SynchronizeData.html#structcupti__synchronizedata). If`domain`

is CUPTI_CB_DOMAIN_NVTX the type of`cbdata`

will be[CUpti_NvtxData](https://docs.nvidia.com/structCUpti__NvtxData.html#structcupti__nvtxdata).- Param userdata:
User data supplied at subscription of the callback

- Param domain:
The domain of the callback

- Param cbid:
The ID of the callback

- Param cbdata:
Data passed to the callback.



-
typedef uint32_t CUpti_CallbackId
[#](https://docs.nvidia.com#_CPPv416CUpti_CallbackId) An ID for a driver API, runtime API, resource or synchronization callback.

An ID for a driver API, runtime API, resource or synchronization callback. Within a driver API callback this should be interpreted as a CUpti_driver_api_trace_cbid value (these values are defined in cupti_driver_cbid.h). Within a runtime API callback this should be interpreted as a CUpti_runtime_api_trace_cbid value (these values are defined in cupti_runtime_cbid.h). Within a resource API callback this should be interpreted as a

[CUpti_CallbackIdResource](https://docs.nvidia.com#group__cupti__callback__api_1ga690fb2a42aefe39f00033c957ce211b2)value. Within a synchronize API callback this should be interpreted as a[CUpti_CallbackIdSync](https://docs.nvidia.com#group__cupti__callback__api_1gacaeba9950bf4f48ea7ab9a0402dc7e6f)value.

-
typedef
[CUpti_CallbackDomain](https://docs.nvidia.com#_CPPv420CUpti_CallbackDomain)*CUpti_DomainTable[#](https://docs.nvidia.com#_CPPv417CUpti_DomainTable) Pointer to an array of callback domains.


-
typedef struct CUpti_Subscriber_st *CUpti_SubscriberHandle
[#](https://docs.nvidia.com#_CPPv422CUpti_SubscriberHandle) A callback subscriber.