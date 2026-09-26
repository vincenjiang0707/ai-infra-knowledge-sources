source: https://docs.nvidia.com/compute-sanitizer/api/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html

# Sanitizer Callback API[#](https://docs.nvidia.com#sanitizer-callback-api)

Functions, types, and enums that implement the Sanitizer Callback API.

## Typedefs[#](https://docs.nvidia.com#typedefs)

[Sanitizer_CallbackFunc](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8)Function type for a callback.

[Sanitizer_CallbackId](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga6e4655fe27c8ee6f85661350bfbc7bd7)Callback ID.

[Sanitizer_SubscriberHandle](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga11604a410fe99da425a0bd40b17c7464)A callback subscriber.


## Enumerations[#](https://docs.nvidia.com#enumerations)

[Sanitizer_ApiCallbackSite](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga0bc24cc0af4c2b8f9c50355c1c1d36ae)Specifies the point in an API call that a callback is issued.

[Sanitizer_BatchMemopAtomicOp](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac8625aa0a46aefad07fa581f794a157e)Specifies the type of atomic operation for batch memory atomic reduction.

[Sanitizer_BatchMemopType](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gaab53af117ae98aa6acf0a6b4dfb71cfa)Specifies the type of batch memory operation.

[Sanitizer_CallackIdSync](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gadf767501dec0e4e2deb55b0c76d35f5f)Callback IDs for synchronization domain.

[Sanitizer_CallbackDomain](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga2184025e5309c5989412b9f64beac46b)Callback domains.

[Sanitizer_CallbackIdBatchMemop](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gae089f8eea1aee2408f559e304d9d0ffa)Callback IDs for batch memop domain.

[Sanitizer_CallbackIdErrorLogging](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gabb0087e63f853a97b480ff5159bdabdc)Callback IDs for external memory domain.

[Sanitizer_CallbackIdEvents](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac64a40e719db73937178eba5ffea9b67)Callback IDs for events domain.

[Sanitizer_CallbackIdExternalMemory](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gafe4f153f58660f80e6dd95e874ccd72a)Callback IDs for external memory domain.

[Sanitizer_CallbackIdGraphs](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga65ad906ecc3006f2b49f63d8b09f38fd)Callback IDs for graphs domain.

[Sanitizer_CallbackIdLaunch](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga023cd56b97f1231cb0c4d11b4f8f95d4)Callback IDs for launch domain.

[Sanitizer_CallbackIdMemcpy](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga9047997c07890c2fd3136ca731228bd5)Callback IDs for memcpy domain.

[Sanitizer_CallbackIdMemset](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga70a5aabab8a7528c5213ee5f535b466c)Callback IDs for memset domain.

[Sanitizer_CallbackIdResource](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gad447a2768c522f1d2b2a086a47705a49)Callback IDs for resource domain.

[Sanitizer_CallbackIdUvm](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gad0dca53274794d63531e7993fb6248a0)Callback IDs for managed memory domain.

[Sanitizer_MemcpyDirection](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga6dd430318fea9a813020c974d07da85e)Memcpy direction.

[Sanitizer_MemoryVisibility](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga62d02f306fdb955ab1f5add810c45564)Specifies the visibility of an allocation.

[Sanitizer_ResourceMemoryFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gad29155bb34524587a5a42d41be1d3fb2)Flags describing a memory allocation.

[Sanitizer_ResourceMemoryPermissions](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac172db1fa20fecca6ac23c2954ae15a1)Permissions for a memory allocation.


## Functions[#](https://docs.nvidia.com#functions)

- SanitizerResult
[sanitizerEnableAllDomains](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga7141b8c08d19678c49e55b48b6807048)(uint32_t enable, Sanitizer_SubscriberHandle subscriber) Enable or disable all callbacks in all domains.

- SanitizerResult
[sanitizerEnableCallback](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga7f9ccc2d0e0380061e8eed072c41b3b7)(uint32_t enable, Sanitizer_SubscriberHandle subscriber, Sanitizer_CallbackDomain domain, Sanitizer_CallbackId cbid) Enable or disable callbacks for a specific domain and callback ID.

- SanitizerResult
[sanitizerEnableDomain](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga2de696ffde337829a90b3d0b34a0293c)(uint32_t enable, Sanitizer_SubscriberHandle subscriber, Sanitizer_CallbackDomain domain) Enable or disable all callbacks for a specific domain.

- SanitizerResult
[sanitizerGetCallbackState](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gaabc521e1a8b19bea5adee39ed7e8c6e4)(uint32_t *enable, Sanitizer_SubscriberHandle subscriber, Sanitizer_CallbackDomain domain, Sanitizer_CallbackId cbid) Get the current enabled/disabled state of a callback for a specific domain and function ID.

- SanitizerResult
[sanitizerIsInsideRecursiveCallback](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gaacdcca73d02d5a4e1a9e7e377e10a475)(uint32_t *isInside) Check if the current thread is inside a recursive Sanitizer callback.

- SanitizerResult
[sanitizerSubscribe](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1ga1654365b83859f8dfd48df6ea832c927)(Sanitizer_SubscriberHandle *subscriber, Sanitizer_CallbackFunc callback, void *userdata) Initialize a callback subscriber with a callback function and user data.

- SanitizerResult
[sanitizerUnsubscribe](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gad278cce7894df2bb97002c25ff36e868)(Sanitizer_SubscriberHandle subscriber) Unregister a callback subscriber.


## Structs[#](https://docs.nvidia.com#structs)

[Sanitizer_BatchMemcpyItemEndData](https://docs.nvidia.com/struct_sanitizer___batch_memcpy_item_end_data.html#struct_sanitizer___batch_memcpy_item_end_data)Data passed into a item batch memcpy end callback function.

[Sanitizer_BatchMemopData](https://docs.nvidia.com/struct_sanitizer___batch_memop_data.html#struct_sanitizer___batch_memop_data)Data passed into a batch memop callback function.

[Sanitizer_BatchMultiEntryPushData](https://docs.nvidia.com/struct_sanitizer___batch_multi_entry_push_data.html#struct_sanitizer___batch_multi_entry_push_data)Data passed into a batch memcpy multientry push begin/end function.

[Sanitizer_CallbackData](https://docs.nvidia.com/struct_sanitizer___callback_data.html#struct_sanitizer___callback_data)Data passed into a runtime or driver API callback function.

[Sanitizer_ErrorLoggingData](https://docs.nvidia.com/struct_sanitizer___error_logging_data.html#struct_sanitizer___error_logging_data)Data passed into an error logging callback function.

[Sanitizer_EventData](https://docs.nvidia.com/struct_sanitizer___event_data.html#struct_sanitizer___event_data)Data passed into an event callback function.

[Sanitizer_ExternalMemoryData](https://docs.nvidia.com/struct_sanitizer___external_memory_data.html#struct_sanitizer___external_memory_data)Data passed into an external memory callback function.

[Sanitizer_GraphExecData](https://docs.nvidia.com/struct_sanitizer___graph_exec_data.html#struct_sanitizer___graph_exec_data)Data passed into a graphexec creation callback function.

[Sanitizer_GraphLaunchData](https://docs.nvidia.com/struct_sanitizer___graph_launch_data.html#struct_sanitizer___graph_launch_data)Data passed into a graph launch callback function.

[Sanitizer_GraphNodeLaunchData](https://docs.nvidia.com/struct_sanitizer___graph_node_launch_data.html#struct_sanitizer___graph_node_launch_data)Data passed into a graph node launch callback function.

[Sanitizer_LaunchData](https://docs.nvidia.com/struct_sanitizer___launch_data.html#struct_sanitizer___launch_data)Data passed into a launch callback function.

[Sanitizer_MemcpyData](https://docs.nvidia.com/struct_sanitizer___memcpy_data.html#struct_sanitizer___memcpy_data)Data passed into a memcpy callback function.

[Sanitizer_MemsetData](https://docs.nvidia.com/struct_sanitizer___memset_data.html#struct_sanitizer___memset_data)Data passed into a memset callback function.

[Sanitizer_ResourceArrayData](https://docs.nvidia.com/struct_sanitizer___resource_array_data.html#struct_sanitizer___resource_array_data)Data passed into a CUDA array callback function.

[Sanitizer_ResourceContextData](https://docs.nvidia.com/struct_sanitizer___resource_context_data.html#struct_sanitizer___resource_context_data)Data passed into a context resource callback function.

[Sanitizer_ResourceFunctionsLazyLoadedData](https://docs.nvidia.com/struct_sanitizer___resource_functions_lazy_loaded_data.html#struct_sanitizer___resource_functions_lazy_loaded_data)Data passed into a CUDA function callback function.

[Sanitizer_ResourceLogicalEndpointData](https://docs.nvidia.com/struct_sanitizer___resource_logical_endpoint_data.html#struct_sanitizer___resource_logical_endpoint_data)Data passed into a logical endpoint resource callback function.

[Sanitizer_ResourceMemoryData](https://docs.nvidia.com/struct_sanitizer___resource_memory_data.html#struct_sanitizer___resource_memory_data)Data passed into a memory resource callback function.

[Sanitizer_ResourceMempoolData](https://docs.nvidia.com/struct_sanitizer___resource_mempool_data.html#struct_sanitizer___resource_mempool_data)Data passed into a mempool resource callback function.

[Sanitizer_ResourceModuleData](https://docs.nvidia.com/struct_sanitizer___resource_module_data.html#struct_sanitizer___resource_module_data)Data passed into a module resource callback function.

[Sanitizer_ResourceStreamData](https://docs.nvidia.com/struct_sanitizer___resource_stream_data.html#struct_sanitizer___resource_stream_data)Data passed into a stream resource callback function.

[Sanitizer_ResourceVirtualRange](https://docs.nvidia.com/struct_sanitizer___resource_virtual_range.html#struct_sanitizer___resource_virtual_range)Data passed into a VA reservation callback function.

[Sanitizer_SynchronizeData](https://docs.nvidia.com/struct_sanitizer___synchronize_data.html#struct_sanitizer___synchronize_data)Data passed into a synchronization callback function.

[Sanitizer_UvmData](https://docs.nvidia.com/struct_sanitizer___uvm_data.html#struct_sanitizer___uvm_data)Data passed into a managed memory callback function.


## Typedefs[#](https://docs.nvidia.com#id1)

-
typedef void (*Sanitizer_CallbackFunc)(void *userdata,
[Sanitizer_CallbackDomain](https://docs.nvidia.com#_CPPv424Sanitizer_CallbackDomain)domain,[Sanitizer_CallbackId](https://docs.nvidia.com#_CPPv420Sanitizer_CallbackId)cbid, const void *cbdata)[#](https://docs.nvidia.com#_CPPv422Sanitizer_CallbackFunc) Function type for a callback.

Function type for a callback. The type of the data passed to the callback in

`cbdata`

depends on the domain. If`domain`

is SANITIZER_CB_DOMAIN_DRIVER_API or SANITIZER_CB_DOMAIN_RUNTIME_API the type of`cbdata`

will be[Sanitizer_CallbackData](https://docs.nvidia.com/struct_sanitizer___callback_data.html#struct_sanitizer___callback_data). If`domain`

is SANITIZER_CB_DOMAIN_RESOURCE the type of`cbdata`

will be dependent on cbid. Refer to[Sanitizer_ResourceContextData](https://docs.nvidia.com/struct_sanitizer___resource_context_data.html#struct_sanitizer___resource_context_data),[Sanitizer_ResourceStreamData](https://docs.nvidia.com/struct_sanitizer___resource_stream_data.html#struct_sanitizer___resource_stream_data),[Sanitizer_ResourceModuleData](https://docs.nvidia.com/struct_sanitizer___resource_module_data.html#struct_sanitizer___resource_module_data)and[Sanitizer_ResourceMemoryFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gad29155bb34524587a5a42d41be1d3fb2)documentations. If`domain`

is SANITIZER_CB_DOMAIN_SYNCHRONIZE the type of`cbdata`

will be[Sanitizer_SynchronizeData](https://docs.nvidia.com/struct_sanitizer___synchronize_data.html#struct_sanitizer___synchronize_data). If`domain`

is SANITIZER_CB_DOMAIN_LAUNCH the type of`cbdata`

will be[Sanitizer_LaunchData](https://docs.nvidia.com/struct_sanitizer___launch_data.html#struct_sanitizer___launch_data). If`domain`

is SANITIZER_CB_DOMAIN_MEMCPY the type of`cbdata`

will be[Sanitizer_MemcpyData](https://docs.nvidia.com/struct_sanitizer___memcpy_data.html#struct_sanitizer___memcpy_data). If`domain`

is SANITIZER_CB_DOMAIN_MEMSET the type of`cbdata`

will be[Sanitizer_MemsetData](https://docs.nvidia.com/struct_sanitizer___memset_data.html#struct_sanitizer___memset_data). If`domain`

is SANITIZER_CB_DOMAIN_BATCH_MEMOP the type of`cbdata`

will be[Sanitizer_BatchMemopData](https://docs.nvidia.com/struct_sanitizer___batch_memop_data.html#struct_sanitizer___batch_memop_data).

-
typedef uint32_t Sanitizer_CallbackId
[#](https://docs.nvidia.com#_CPPv420Sanitizer_CallbackId) Callback ID.


-
typedef struct Sanitizer_Subscriber_st *Sanitizer_SubscriberHandle
[#](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle) A callback subscriber.


## Enumerations[#](https://docs.nvidia.com#id2)

-
enum Sanitizer_ApiCallbackSite
[#](https://docs.nvidia.com#_CPPv425Sanitizer_ApiCallbackSite) Specifies the point in an API call that a callback is issued.

Specifies the point in an API that a callback is issued. This value is communicated to the callback function via Sanitizer_CallbackData::CallbackSize.

*Values:*-
enumerator SANITIZER_API_ENTER
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_ApiCallbackSite19SANITIZER_API_ENTERE) This callback is at API entry.


-
enumerator SANITIZER_API_EXIT
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_ApiCallbackSite18SANITIZER_API_EXITE) This callback is at API exit.


-
enumerator SANITIZER_API_CBSITE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_ApiCallbackSite30SANITIZER_API_CBSITE_FORCE_INTE)

-
enumerator SANITIZER_API_ENTER

-
enum Sanitizer_BatchMemopAtomicOp
[#](https://docs.nvidia.com#_CPPv428Sanitizer_BatchMemopAtomicOp) Specifies the type of atomic operation for batch memory atomic reduction.

Specifies the type ofatomic operation for batch memory atomic reduction reported by a callback in domain SANITIZER_CB_DOMAIN_BATCH_MEMOP. This value is communicated to the callback function via

[Sanitizer_BatchMemopData::atomicOperation](https://docs.nvidia.com/struct_sanitizer___batch_memop_data.html#struct_sanitizer___batch_memop_data_1a1a670dff20589686694599bfd9424409).*Values:*-
enumerator SANITIZER_BATCH_MEMOP_ATOMIC_OP_OR
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_BatchMemopAtomicOp34SANITIZER_BATCH_MEMOP_ATOMIC_OP_ORE) The batch memory atomic operation is a binary OR.


-
enumerator SANITIZER_BATCH_MEMOP_ATOMIC_OP_AND
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_BatchMemopAtomicOp35SANITIZER_BATCH_MEMOP_ATOMIC_OP_ANDE) The batch memory atomic operation is a binary AND.


-
enumerator SANITIZER_BATCH_MEMOP_ATOMIC_OP_ADD
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_BatchMemopAtomicOp35SANITIZER_BATCH_MEMOP_ATOMIC_OP_ADDE) The batch memory atomic operation is an addition.


-
enumerator SANITIZER_BATCH_MEMOP_ATOMIC_OP_INT
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_BatchMemopAtomicOp35SANITIZER_BATCH_MEMOP_ATOMIC_OP_INTE)

-
enumerator SANITIZER_BATCH_MEMOP_ATOMIC_OP_OR

-
enum Sanitizer_BatchMemopType
[#](https://docs.nvidia.com#_CPPv424Sanitizer_BatchMemopType) Specifies the type of batch memory operation.

Specifies the type of batch memory operation reported by a callback in domain SANITIZER_CB_DOMAIN_BATCH_MEMOP. This value is communicated to the callback function via

[Sanitizer_BatchMemopData::type](https://docs.nvidia.com/struct_sanitizer___batch_memop_data.html#struct_sanitizer___batch_memop_data_1a874b875cc64512766ed6d8f43fea3afd).*Values:*-
enumerator SANITIZER_BATCH_MEMOP_TYPE_32B
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopType30SANITIZER_BATCH_MEMOP_TYPE_32BE) Batch memory operation size is 32 bits.


-
enumerator SANITIZER_BATCH_MEMOP_TYPE_64B
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopType30SANITIZER_BATCH_MEMOP_TYPE_64BE) Batch memory operation size is 64 bits.


-
enumerator SANITIZER_BATCH_MEMOP_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopType36SANITIZER_BATCH_MEMOP_TYPE_FORCE_INTE)

-
enumerator SANITIZER_BATCH_MEMOP_TYPE_32B

-
enum Sanitizer_CallackIdSync
[#](https://docs.nvidia.com#_CPPv423Sanitizer_CallackIdSync) Callback IDs for synchronization domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_SYNCHRONIZE. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_SYNCHRONIZE_INVALID
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallackIdSync34SANITIZER_CBID_SYNCHRONIZE_INVALIDE) Invalid synchronize callback ID.


-
enumerator SANITIZER_CBID_SYNCHRONIZE_STREAM_SYNCHRONIZED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallackIdSync46SANITIZER_CBID_SYNCHRONIZE_STREAM_SYNCHRONIZEDE) Stream synchronization has completed for a given stream.


-
enumerator SANITIZER_CBID_SYNCHRONIZE_CONTEXT_SYNCHRONIZED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallackIdSync47SANITIZER_CBID_SYNCHRONIZE_CONTEXT_SYNCHRONIZEDE) Context synchronization has completed for a given context.


-
enumerator SANITIZER_CBID_SYNCHRONIZE_GREEN_CONTEXT_SYNCHRONIZED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallackIdSync53SANITIZER_CBID_SYNCHRONIZE_GREEN_CONTEXT_SYNCHRONIZEDE) Context synchronization has completed for a given green context.


-
enumerator SANITIZER_CBID_SYNCHRONIZE_SIZE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallackIdSync31SANITIZER_CBID_SYNCHRONIZE_SIZEE)

-
enumerator SANITIZER_CBID_SYNCHRONIZE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallackIdSync36SANITIZER_CBID_SYNCHRONIZE_FORCE_INTE)

-
enumerator SANITIZER_CBID_SYNCHRONIZE_INVALID

-
enum Sanitizer_CallbackDomain
[#](https://docs.nvidia.com#_CPPv424Sanitizer_CallbackDomain) Callback domains.

Callback domain. Each domain represents callback points for a group of related API functions or CUDA driver activity.

*Values:*-
enumerator SANITIZER_CB_DOMAIN_INVALID
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain27SANITIZER_CB_DOMAIN_INVALIDE) Invalid domain.


-
enumerator SANITIZER_CB_DOMAIN_DRIVER_API
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain30SANITIZER_CB_DOMAIN_DRIVER_APIE) Domain containing callback points for all driver API functions.


-
enumerator SANITIZER_CB_DOMAIN_RUNTIME_API
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain31SANITIZER_CB_DOMAIN_RUNTIME_APIE) Domain containing callback points for all runtime API functions.


-
enumerator SANITIZER_CB_DOMAIN_RESOURCE
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain28SANITIZER_CB_DOMAIN_RESOURCEE) Domain containing callback points for CUDA resource tracking.


-
enumerator SANITIZER_CB_DOMAIN_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain31SANITIZER_CB_DOMAIN_SYNCHRONIZEE) Domain containing callback points for CUDA synchronization.


-
enumerator SANITIZER_CB_DOMAIN_LAUNCH
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain26SANITIZER_CB_DOMAIN_LAUNCHE) Domain containing callback points for CUDA grid launches.


-
enumerator SANITIZER_CB_DOMAIN_MEMCPY
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain26SANITIZER_CB_DOMAIN_MEMCPYE) Domain containing callback points for CUDA memcpy operations.


-
enumerator SANITIZER_CB_DOMAIN_MEMSET
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain26SANITIZER_CB_DOMAIN_MEMSETE) Domain containing callback points for CUDA memset operations.


-
enumerator SANITIZER_CB_DOMAIN_BATCH_MEMOP
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain31SANITIZER_CB_DOMAIN_BATCH_MEMOPE) Domain containing callback points for CUDA batch memop operations.


-
enumerator SANITIZER_CB_DOMAIN_UVM
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain23SANITIZER_CB_DOMAIN_UVME) Domain containing callback points for CUDA managed memory operations.


-
enumerator SANITIZER_CB_DOMAIN_GRAPHS
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain26SANITIZER_CB_DOMAIN_GRAPHSE) Domain containing callback points for CUDA graphs operations.


-
enumerator SANITIZER_CB_DOMAIN_EVENTS
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain26SANITIZER_CB_DOMAIN_EVENTSE) Domain containing callback points for CUDA events.


-
enumerator SANITIZER_CB_DOMAIN_EXTERNAL_MEMORY
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain35SANITIZER_CB_DOMAIN_EXTERNAL_MEMORYE) Domain containing callback points for CUDA external memory.


-
enumerator SANITIZER_CB_DOMAIN_ERROR_LOGGING
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain33SANITIZER_CB_DOMAIN_ERROR_LOGGINGE) Domain containing callback points for CUDA error logging.


-
enumerator SANITIZER_CB_DOMAIN_SIZE
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain24SANITIZER_CB_DOMAIN_SIZEE)

-
enumerator SANITIZER_CB_DOMAIN_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_CallbackDomain29SANITIZER_CB_DOMAIN_FORCE_INTE)

-
enumerator SANITIZER_CB_DOMAIN_INVALID

-
enum Sanitizer_CallbackIdBatchMemop
[#](https://docs.nvidia.com#_CPPv430Sanitizer_CallbackIdBatchMemop) Callback IDs for batch memop domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_BATCH_MEMOP. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_BATCH_MEMOP_INVALID
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_CallbackIdBatchMemop34SANITIZER_CBID_BATCH_MEMOP_INVALIDE) Invalid batch memop callback ID.


-
enumerator SANITIZER_CBID_BATCH_MEMOP_WRITE
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_CallbackIdBatchMemop32SANITIZER_CBID_BATCH_MEMOP_WRITEE) A batch memory write operation was initiated.


-
enumerator SANITIZER_CBID_BATCH_MEMOP_WAIT_BEGIN
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_CallbackIdBatchMemop37SANITIZER_CBID_BATCH_MEMOP_WAIT_BEGINE) A batch memory wait operation was initiated.


-
enumerator SANITIZER_CBID_BATCH_MEMOP_ATOMIC_REDUCTION
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_CallbackIdBatchMemop43SANITIZER_CBID_BATCH_MEMOP_ATOMIC_REDUCTIONE) A batch memory atomic reduction operation was initiated.


-
enumerator SANITIZER_CBID_BATCH_MEMOP_SIZE
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_CallbackIdBatchMemop31SANITIZER_CBID_BATCH_MEMOP_SIZEE)

-
enumerator SANITIZER_CBID_BATCH_MEMOP_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_CallbackIdBatchMemop36SANITIZER_CBID_BATCH_MEMOP_FORCE_INTE)

-
enumerator SANITIZER_CBID_BATCH_MEMOP_INVALID

-
enum Sanitizer_CallbackIdErrorLogging
[#](https://docs.nvidia.com#_CPPv432Sanitizer_CallbackIdErrorLogging) Callback IDs for external memory domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_EXTERNA_MEMORY. This value is communicated to the callback function via the

`cbid`

parameter. Available with a driver version of 535 or newer.*Values:*-
enumerator SANITIZER_CBID_ERROR_LOGGING_INVALID
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_CallbackIdErrorLogging36SANITIZER_CBID_ERROR_LOGGING_INVALIDE) Invalid error logging callback ID.


-
enumerator SANITIZER_CBID_ERROR_LOGGING_MESSAGE_ISSUED
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_CallbackIdErrorLogging43SANITIZER_CBID_ERROR_LOGGING_MESSAGE_ISSUEDE) Error logging message issued.


-
enumerator SANITIZER_CBID_ERROR_LOGGING_SIZE
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_CallbackIdErrorLogging33SANITIZER_CBID_ERROR_LOGGING_SIZEE)

-
enumerator SANITIZER_CBID_ERROR_LOGGING_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_CallbackIdErrorLogging38SANITIZER_CBID_ERROR_LOGGING_FORCE_INTE)

-
enumerator SANITIZER_CBID_ERROR_LOGGING_INVALID

-
enum Sanitizer_CallbackIdEvents
[#](https://docs.nvidia.com#_CPPv426Sanitizer_CallbackIdEvents) Callback IDs for events domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_EVENTS. This value is communicated to the callback function via the

`cbid`

parameter. Available with a driver version of 515 or newer.*Values:*-
enumerator SANITIZER_CBID_EVENTS_INVALID
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents29SANITIZER_CBID_EVENTS_INVALIDE) Invalid event callback ID.


-
enumerator SANITIZER_CBID_EVENTS_CREATED
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents29SANITIZER_CBID_EVENTS_CREATEDE) An event was created.


-
enumerator SANITIZER_CBID_EVENTS_DESTROYED
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents31SANITIZER_CBID_EVENTS_DESTROYEDE) An event was destroyed.


-
enumerator SANITIZER_CBID_EVENTS_RECORD
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents28SANITIZER_CBID_EVENTS_RECORDE) An event was recorded.


-
enumerator SANITIZER_CBID_EVENTS_STREAM_WAIT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents33SANITIZER_CBID_EVENTS_STREAM_WAITE) A stream was synchronized to an event.


-
enumerator SANITIZER_CBID_EVENTS_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents33SANITIZER_CBID_EVENTS_SYNCHRONIZEE) An event was synchronized.


-
enumerator SANITIZER_CBID_CTX_RECORD_EVENT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents31SANITIZER_CBID_CTX_RECORD_EVENTE) A ctx event was recorded.


-
enumerator SANITIZER_CBID_GREEN_CTX_RECORD_EVENT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents37SANITIZER_CBID_GREEN_CTX_RECORD_EVENTE) A green ctx event was recorded.


-
enumerator SANITIZER_CBID_CTX_WAIT_EVENT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents29SANITIZER_CBID_CTX_WAIT_EVENTE) A wait for event was scheduled on context.


-
enumerator SANITIZER_CBID_GREEN_CTX_WAIT_EVENT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents35SANITIZER_CBID_GREEN_CTX_WAIT_EVENTE) A wait for event was scheduled on context.


-
enumerator SANITIZER_CBID_CTX_EVENT_SYNCHRONIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents36SANITIZER_CBID_CTX_EVENT_SYNCHRONIZEE) An event was synchronized.


-
enumerator SANITIZER_CBID_EVENTS_SIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents26SANITIZER_CBID_EVENTS_SIZEE)

-
enumerator SANITIZER_CBID_EVENTS_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdEvents31SANITIZER_CBID_EVENTS_FORCE_INTE)

-
enumerator SANITIZER_CBID_EVENTS_INVALID

-
enum Sanitizer_CallbackIdExternalMemory
[#](https://docs.nvidia.com#_CPPv434Sanitizer_CallbackIdExternalMemory) Callback IDs for external memory domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_EXTERNA_MEMORY. This value is communicated to the callback function via the

`cbid`

parameter. Available with a driver version of 535 or newer.*Values:*-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_INVALID
[#](https://docs.nvidia.com#_CPPv4N34Sanitizer_CallbackIdExternalMemory38SANITIZER_CBID_EXTERNAL_MEMORY_INVALIDE) Invalid external memory callback ID.


-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_IMPORT
[#](https://docs.nvidia.com#_CPPv4N34Sanitizer_CallbackIdExternalMemory37SANITIZER_CBID_EXTERNAL_MEMORY_IMPORTE) External memory was imported.


-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_MAPPED
[#](https://docs.nvidia.com#_CPPv4N34Sanitizer_CallbackIdExternalMemory37SANITIZER_CBID_EXTERNAL_MEMORY_MAPPEDE) External memory was mapped.


-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_DESTROYED
[#](https://docs.nvidia.com#_CPPv4N34Sanitizer_CallbackIdExternalMemory40SANITIZER_CBID_EXTERNAL_MEMORY_DESTROYEDE) External memory was destroyed.


-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_SIZE
[#](https://docs.nvidia.com#_CPPv4N34Sanitizer_CallbackIdExternalMemory35SANITIZER_CBID_EXTERNAL_MEMORY_SIZEE)

-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N34Sanitizer_CallbackIdExternalMemory40SANITIZER_CBID_EXTERNAL_MEMORY_FORCE_INTE)

-
enumerator SANITIZER_CBID_EXTERNAL_MEMORY_INVALID

-
enum Sanitizer_CallbackIdGraphs
[#](https://docs.nvidia.com#_CPPv426Sanitizer_CallbackIdGraphs) Callback IDs for graphs domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_GRAPHS. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_GRAPHS_INVALID
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs29SANITIZER_CBID_GRAPHS_INVALIDE) Invalid graphs callback ID.


-
enumerator SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATING
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs40SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATINGE) A new graphexec is being created.


-
enumerator SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATED
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs39SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATEDE) A new graphexec is created.


-
enumerator SANITIZER_CBID_GRAPHS_GRAPHEXEC_DESTROYING
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs42SANITIZER_CBID_GRAPHS_GRAPHEXEC_DESTROYINGE) A graphexec is being destroyed.


-
enumerator SANITIZER_CBID_GRAPHS_NODE_LAUNCH_BEGIN
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs39SANITIZER_CBID_GRAPHS_NODE_LAUNCH_BEGINE) A node launch was initiated.


-
enumerator SANITIZER_CBID_GRAPHS_NODE_LAUNCH_END
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs37SANITIZER_CBID_GRAPHS_NODE_LAUNCH_ENDE) A node launch is complete.


-
enumerator SANITIZER_CBID_GRAPHS_LAUNCH_BEGIN
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs34SANITIZER_CBID_GRAPHS_LAUNCH_BEGINE) A graph launch was initiated.


-
enumerator SANITIZER_CBID_GRAPHS_LAUNCH_END
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs32SANITIZER_CBID_GRAPHS_LAUNCH_ENDE) A graph launch is complete.


-
enumerator SANITIZER_CBID_GRAPHS_SIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs26SANITIZER_CBID_GRAPHS_SIZEE)

-
enumerator SANITIZER_CBID_GRAPHS_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdGraphs31SANITIZER_CBID_GRAPHS_FORCE_INTE)

-
enumerator SANITIZER_CBID_GRAPHS_INVALID

-
enum Sanitizer_CallbackIdLaunch
[#](https://docs.nvidia.com#_CPPv426Sanitizer_CallbackIdLaunch) Callback IDs for launch domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_LAUNCH. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_LAUNCH_INVALID
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdLaunch29SANITIZER_CBID_LAUNCH_INVALIDE) Invalid launch callback ID.


-
enumerator SANITIZER_CBID_LAUNCH_BEGIN
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdLaunch27SANITIZER_CBID_LAUNCH_BEGINE) A grid launch was initiated.


-
enumerator SANITIZER_CBID_LAUNCH_AFTER_SYSCALL_SETUP
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdLaunch41SANITIZER_CBID_LAUNCH_AFTER_SYSCALL_SETUPE) A grid launch has completed syscalls setup.


-
enumerator SANITIZER_CBID_LAUNCH_END
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdLaunch25SANITIZER_CBID_LAUNCH_ENDE) The grid launch is complete.


-
enumerator SANITIZER_CBID_LAUNCH_SIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdLaunch26SANITIZER_CBID_LAUNCH_SIZEE)

-
enumerator SANITIZER_CBID_LAUNCH_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdLaunch31SANITIZER_CBID_LAUNCH_FORCE_INTE)

-
enumerator SANITIZER_CBID_LAUNCH_INVALID

-
enum Sanitizer_CallbackIdMemcpy
[#](https://docs.nvidia.com#_CPPv426Sanitizer_CallbackIdMemcpy) Callback IDs for memcpy domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_MEMCPY. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_MEMCPY_INVALID
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy29SANITIZER_CBID_MEMCPY_INVALIDE) Invalid memcpy callback ID.


-
enumerator SANITIZER_CBID_MEMCPY_STARTING
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy30SANITIZER_CBID_MEMCPY_STARTINGE) A memcpy operation was initiated.


-
enumerator SANITIZER_CBID_MEMCPY_BATCH_ITEM_STARTING
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy41SANITIZER_CBID_MEMCPY_BATCH_ITEM_STARTINGE) A memcopy batch item operation was initiated.


-
enumerator SANITIZER_CBID_MEMCPY_BATCH_ITEM_END
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy36SANITIZER_CBID_MEMCPY_BATCH_ITEM_ENDE) A memcopy batch item operation was finished.


-
enumerator SANITIZER_CBID_MEMCPY_BATCH_MULTI_ENTRY_PUSH_BEGIN
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy50SANITIZER_CBID_MEMCPY_BATCH_MULTI_ENTRY_PUSH_BEGINE) A memcopy batch multientry push has started.


-
enumerator SANITIZER_CBID_MEMCPY_BATCH_MULTI_ENTRY_PUSH_END
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy48SANITIZER_CBID_MEMCPY_BATCH_MULTI_ENTRY_PUSH_ENDE) A memcopy batch multientry push has finished.


-
enumerator SANITIZER_CBID_MEMCPY_SIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy26SANITIZER_CBID_MEMCPY_SIZEE)

-
enumerator SANITIZER_CBID_MEMCPY_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemcpy31SANITIZER_CBID_MEMCPY_FORCE_INTE)

-
enumerator SANITIZER_CBID_MEMCPY_INVALID

-
enum Sanitizer_CallbackIdMemset
[#](https://docs.nvidia.com#_CPPv426Sanitizer_CallbackIdMemset) Callback IDs for memset domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_MEMSET. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_MEMSET_INVALID
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemset29SANITIZER_CBID_MEMSET_INVALIDE) Invalid memset callback ID.


-
enumerator SANITIZER_CBID_MEMSET_STARTING
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemset30SANITIZER_CBID_MEMSET_STARTINGE) A memset operation was initiated.


-
enumerator SANITIZER_CBID_MEMSET_SIZE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemset26SANITIZER_CBID_MEMSET_SIZEE)

-
enumerator SANITIZER_CBID_MEMSET_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CallbackIdMemset31SANITIZER_CBID_MEMSET_FORCE_INTE)

-
enumerator SANITIZER_CBID_MEMSET_INVALID

-
enum Sanitizer_CallbackIdResource
[#](https://docs.nvidia.com#_CPPv428Sanitizer_CallbackIdResource) Callback IDs for resource domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_RESOURCE. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_RESOURCE_INVALID
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource31SANITIZER_CBID_RESOURCE_INVALIDE) Invalid resource callback ID.


-
enumerator SANITIZER_CBID_RESOURCE_INIT_FINISHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource37SANITIZER_CBID_RESOURCE_INIT_FINISHEDE) Driver initialization is finished.


-
enumerator SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_STARTING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource49SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_STARTINGE) A new context is about to be created.


-
enumerator SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_FINISHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource49SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_FINISHEDE) A new context was created.


-
enumerator SANITIZER_CBID_RESOURCE_CONTEXT_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource48SANITIZER_CBID_RESOURCE_CONTEXT_DESTROY_STARTINGE) A context is about to be destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_CONTEXT_DESTROY_FINISHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource48SANITIZER_CBID_RESOURCE_CONTEXT_DESTROY_FINISHEDE) A context was destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_STREAM_CREATED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource38SANITIZER_CBID_RESOURCE_STREAM_CREATEDE) A new stream was created.


-
enumerator SANITIZER_CBID_RESOURCE_STREAM_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource47SANITIZER_CBID_RESOURCE_STREAM_DESTROY_STARTINGE) A stream is about to be destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_STREAM_DESTROY_FINISHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource47SANITIZER_CBID_RESOURCE_STREAM_DESTROY_FINISHEDE) A stream was destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_MODULE_LOADED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource37SANITIZER_CBID_RESOURCE_MODULE_LOADEDE) A module was loaded.


-
enumerator SANITIZER_CBID_RESOURCE_MODULE_UNLOAD_STARTING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource46SANITIZER_CBID_RESOURCE_MODULE_UNLOAD_STARTINGE) A module is about to be unloaded.


-
enumerator SANITIZER_CBID_RESOURCE_DEVICE_MEMORY_ALLOC
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource43SANITIZER_CBID_RESOURCE_DEVICE_MEMORY_ALLOCE) Device memory was allocated.


-
enumerator SANITIZER_CBID_RESOURCE_DEVICE_MEMORY_FREE
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource42SANITIZER_CBID_RESOURCE_DEVICE_MEMORY_FREEE) Device memory was freed.


-
enumerator SANITIZER_CBID_RESOURCE_HOST_MEMORY_ALLOC
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource41SANITIZER_CBID_RESOURCE_HOST_MEMORY_ALLOCE) Pinned host memory was allocated.


-
enumerator SANITIZER_CBID_RESOURCE_HOST_MEMORY_FREE
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource40SANITIZER_CBID_RESOURCE_HOST_MEMORY_FREEE) Pinned host memory was freed.


-
enumerator SANITIZER_CBID_RESOURCE_MEMORY_ALLOC_ASYNC
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource42SANITIZER_CBID_RESOURCE_MEMORY_ALLOC_ASYNCE) Memory was allocated asynchronously.


-
enumerator SANITIZER_CBID_RESOURCE_MEMORY_FREE_ASYNC
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource41SANITIZER_CBID_RESOURCE_MEMORY_FREE_ASYNCE) Memory was freed asynchronously.


-
enumerator SANITIZER_CBID_RESOURCE_MEMORY_FREE_ASYNC_DONE
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource46SANITIZER_CBID_RESOURCE_MEMORY_FREE_ASYNC_DONEE) Memory freed asynchronously was released, only happens if a regular allocation (cudaMalloc) is free’d asynchronously (cudaFreeAsync).

See CUDA runtime documentation for cudaFreeAsync.


-
enumerator SANITIZER_CBID_RESOURCE_MEMPOOL_CREATED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource39SANITIZER_CBID_RESOURCE_MEMPOOL_CREATEDE) A new mempool was created.


-
enumerator SANITIZER_CBID_RESOURCE_MEMPOOL_DESTROYING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource42SANITIZER_CBID_RESOURCE_MEMPOOL_DESTROYINGE) A mempool is about to be destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_ENABLED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource51SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_ENABLEDE) A mempool is now accessible from a peer device.


-
enumerator SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_DISABLING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource53SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_DISABLINGE) A mempool is no longer accessible from a peer device.


-
enumerator SANITIZER_CBID_RESOURCE_ARRAY_CREATED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource37SANITIZER_CBID_RESOURCE_ARRAY_CREATEDE) A CUDA array was created.


-
enumerator SANITIZER_CBID_RESOURCE_ARRAY_DESTROYED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource39SANITIZER_CBID_RESOURCE_ARRAY_DESTROYEDE) A CUDA array was destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_FUNCTIONS_LAZY_LOADED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource45SANITIZER_CBID_RESOURCE_FUNCTIONS_LAZY_LOADEDE) CUDA functions were loaded lazily and are fully loaded.


-
enumerator SANITIZER_CBID_RESOURCE_FUNCTIONS_LAZY_PATCHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource46SANITIZER_CBID_RESOURCE_FUNCTIONS_LAZY_PATCHEDE) CUDA lazily loaded functions were patched.


-
enumerator SANITIZER_CBID_RESOURCE_VIRTUAL_RESERVE
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource39SANITIZER_CBID_RESOURCE_VIRTUAL_RESERVEE) The CUDA driver reserved a virtual address range.


-
enumerator SANITIZER_CBID_RESOURCE_VIRTUAL_RELEASE
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource39SANITIZER_CBID_RESOURCE_VIRTUAL_RELEASEE) The CUDA driver released a virtual address range.


-
enumerator SANITIZER_CBID_RESOURCE_MEMPOOL_IMPORT_POINTER
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource46SANITIZER_CBID_RESOURCE_MEMPOOL_IMPORT_POINTERE) A memory pool allocation was imported.


-
enumerator SANITIZER_CBID_RESOURCE_GREEN_CONTEXT_CREATION_FINISHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource55SANITIZER_CBID_RESOURCE_GREEN_CONTEXT_CREATION_FINISHEDE) A new green context was created.


-
enumerator SANITIZER_CBID_RESOURCE_GREEN_CONTEXT_DESTROY_STARTING
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource54SANITIZER_CBID_RESOURCE_GREEN_CONTEXT_DESTROY_STARTINGE) A green context is about to be destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_GREEN_CONTEXT_DESTROY_FINISHED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource54SANITIZER_CBID_RESOURCE_GREEN_CONTEXT_DESTROY_FINISHEDE) A green context was destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_LOGICAL_ENDPOINT_CREATED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource48SANITIZER_CBID_RESOURCE_LOGICAL_ENDPOINT_CREATEDE) A logical endpoint was created.


-
enumerator SANITIZER_CBID_RESOURCE_LOGICAL_ENDPOINT_DESTROYED
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource50SANITIZER_CBID_RESOURCE_LOGICAL_ENDPOINT_DESTROYEDE) A logical endpoint was destroyed.


-
enumerator SANITIZER_CBID_RESOURCE_SIZE
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource28SANITIZER_CBID_RESOURCE_SIZEE)

-
enumerator SANITIZER_CBID_RESOURCE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_CallbackIdResource33SANITIZER_CBID_RESOURCE_FORCE_INTE)

-
enumerator SANITIZER_CBID_RESOURCE_INVALID

-
enum Sanitizer_CallbackIdUvm
[#](https://docs.nvidia.com#_CPPv423Sanitizer_CallbackIdUvm) Callback IDs for managed memory domain.

Callback IDs for resource domain SANITIZER_CB_DOMAIN_UVM. This value is communicated to the callback function via the

`cbid`

parameter.*Values:*-
enumerator SANITIZER_CBID_UVM_INVALID
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallbackIdUvm26SANITIZER_CBID_UVM_INVALIDE) Invalid managed memory callback ID.


-
enumerator SANITIZER_CBID_UVM_ATTACH_MEM
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallbackIdUvm29SANITIZER_CBID_UVM_ATTACH_MEME) Modify the stream association of an allocation (see cudaStreamAttachMemAsync)


-
enumerator SANITIZER_CBID_UVM_SIZE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallbackIdUvm23SANITIZER_CBID_UVM_SIZEE)

-
enumerator SANITIZER_CBID_UVM_FORCE_ITN
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_CallbackIdUvm28SANITIZER_CBID_UVM_FORCE_ITNE)

-
enumerator SANITIZER_CBID_UVM_INVALID

-
enum Sanitizer_MemcpyDirection
[#](https://docs.nvidia.com#_CPPv425Sanitizer_MemcpyDirection) Memcpy direction.

Indicates the direction of a memcpy, passed inside

`Sanitizer_Memcpydata`

.*Values:*-
enumerator SANITIZER_MEMCPY_DIRECTION_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection34SANITIZER_MEMCPY_DIRECTION_UNKNOWNE) Unknown memcpy direction.


-
enumerator SANITIZER_MEMCPY_DIRECTION_HOST_TO_HOST
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection39SANITIZER_MEMCPY_DIRECTION_HOST_TO_HOSTE) Memcpy from host to host.


-
enumerator SANITIZER_MEMCPY_DIRECTION_HOST_TO_DEVICE
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection41SANITIZER_MEMCPY_DIRECTION_HOST_TO_DEVICEE) Memcpy from host to device.


-
enumerator SANITIZER_MEMCPY_DIRECTION_DEVICE_TO_HOST
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection41SANITIZER_MEMCPY_DIRECTION_DEVICE_TO_HOSTE) Memcpy from device to host.


-
enumerator SANITIZER_MEMCPY_DIRECTION_DEVICE_TO_DEVICE
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection43SANITIZER_MEMCPY_DIRECTION_DEVICE_TO_DEVICEE) Memcpy from device to device.


-
enumerator SANITIZER_MEMCPY_DIRECTION_SIZE
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection31SANITIZER_MEMCPY_DIRECTION_SIZEE)

-
enumerator SANITIZER_MEMCPY_DIRECTION_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_MemcpyDirection36SANITIZER_MEMCPY_DIRECTION_FORCE_INTE)

-
enumerator SANITIZER_MEMCPY_DIRECTION_UNKNOWN

-
enum Sanitizer_MemoryVisibility
[#](https://docs.nvidia.com#_CPPv426Sanitizer_MemoryVisibility) Specifies the visibility of an allocation.

Specifies the visibility of an allocation. This is typically GLOBAL on allocations made via cudaMalloc, cudaHostAlloc and similar APIs. This can be GLOBAL or HOST for cudaMallocManaged allocations depending on the flags parameter. This can be changed after allocation time using cudaMemAttachSingle API (see SANITIZER_CBID_UVM_ATTACH_MEM for the corresponding callback).

*Values:*-
enumerator SANITIZER_MEMORY_VISIBILITY_INVALID
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_MemoryVisibility35SANITIZER_MEMORY_VISIBILITY_INVALIDE) Invalid memory visibility.


-
enumerator SANITIZER_MEMORY_VISIBILITY_GLOBAL
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_MemoryVisibility34SANITIZER_MEMORY_VISIBILITY_GLOBALE) Memory can be accessed by any stream on any device (see cudaMemAttachGlobal).


-
enumerator SANITIZER_MEMORY_VISIBILITY_HOST
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_MemoryVisibility32SANITIZER_MEMORY_VISIBILITY_HOSTE) Memory cannot be accessed by any stream on any device (see cudaMemAttachHost).


-
enumerator SANITIZER_MEMORY_VISIBILITY_STREAM
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_MemoryVisibility34SANITIZER_MEMORY_VISIBILITY_STREAME) Memory can only be accessed by a single stream on the associated device (see cudaMemAttachSingle).


-
enumerator SANITIZER_MEMORY_VISIBILITY_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_MemoryVisibility37SANITIZER_MEMORY_VISIBILITY_FORCE_INTE)

-
enumerator SANITIZER_MEMORY_VISIBILITY_INVALID

-
enum Sanitizer_ResourceMemoryFlags
[#](https://docs.nvidia.com#_CPPv429Sanitizer_ResourceMemoryFlags) Flags describing a memory allocation.

Flags describing a memory allocation. These values are to be used in order to interpret the value of

[Sanitizer_ResourceMemoryData::flags](https://docs.nvidia.com/struct_sanitizer___resource_memory_data.html#struct_sanitizer___resource_memory_data_1a7bee77cc4075471b0397cf557c843c4a).*Values:*-
enumerator SANITIZER_MEMORY_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags26SANITIZER_MEMORY_FLAG_NONEE) Empty flag.


-
enumerator SANITIZER_MEMORY_FLAG_MODULE
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags28SANITIZER_MEMORY_FLAG_MODULEE) Specifies that the allocation is static scoped to a module.


-
enumerator SANITIZER_MEMORY_FLAG_MANAGED
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags29SANITIZER_MEMORY_FLAG_MANAGEDE) Specifies that the allocation is managed memory.


-
enumerator SANITIZER_MEMORY_FLAG_HOST_MAPPED
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags33SANITIZER_MEMORY_FLAG_HOST_MAPPEDE) Species that the allocation accessible from the host.


-
enumerator SANITIZER_MEMORY_FLAG_HOST_PINNED
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags33SANITIZER_MEMORY_FLAG_HOST_PINNEDE) Specifies that the allocation is pinned on the host.


-
enumerator SANITIZER_MEMORY_FLAG_PEER
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags26SANITIZER_MEMORY_FLAG_PEERE) Specifies that the allocation is located on a peer GPU.


-
enumerator SANITIZER_MEMORY_FLAG_PEER_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags33SANITIZER_MEMORY_FLAG_PEER_ATOMICE) Specifies that the allocation is located on a peer GPU supporting native atomics.

This implies that SANITIZER_MEMORY_FLAG_PEER is set as well.


-
enumerator SANITIZER_MEMORY_FLAG_CG_RUNTIME
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags32SANITIZER_MEMORY_FLAG_CG_RUNTIMEE) Specifies that the allocation is used by the Cooperative Groups runtime functions.


-
enumerator SANITIZER_MEMORY_FLAG_CNP
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags25SANITIZER_MEMORY_FLAG_CNPE) Specifies that this is an allocation used for CUDA Dynamic Parallelism purposes.


-
enumerator SANITIZER_MEMORY_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMemoryFlags31SANITIZER_MEMORY_FLAG_FORCE_INTE)

-
enumerator SANITIZER_MEMORY_FLAG_NONE

-
enum Sanitizer_ResourceMemoryPermissions
[#](https://docs.nvidia.com#_CPPv435Sanitizer_ResourceMemoryPermissions) Permissions for a memory allocation.

Permissions for a memory allocation. These values are to be used in order to interpret the value of

[Sanitizer_ResourceMemoryData::permissions](https://docs.nvidia.com/struct_sanitizer___resource_memory_data.html#struct_sanitizer___resource_memory_data_1afa68ea5df21d945ae35162a7573c4d61).*Values:*-
enumerator SANITIZER_MEMORY_PERMISSION_NONE
[#](https://docs.nvidia.com#_CPPv4N35Sanitizer_ResourceMemoryPermissions32SANITIZER_MEMORY_PERMISSION_NONEE) No permissions.


-
enumerator SANITIZER_MEMORY_PERMISSION_READ
[#](https://docs.nvidia.com#_CPPv4N35Sanitizer_ResourceMemoryPermissions32SANITIZER_MEMORY_PERMISSION_READE) Specifies that the allocation is readable.


-
enumerator SANITIZER_MEMORY_PERMISSION_WRITE
[#](https://docs.nvidia.com#_CPPv4N35Sanitizer_ResourceMemoryPermissions33SANITIZER_MEMORY_PERMISSION_WRITEE) Specifies that the allocation is writable.


-
enumerator SANITIZER_MEMORY_PERMISSION_ATOMIC
[#](https://docs.nvidia.com#_CPPv4N35Sanitizer_ResourceMemoryPermissions34SANITIZER_MEMORY_PERMISSION_ATOMICE) Specifies that the allocation is readable/writable with atomic operations.


-
enumerator SANITIZER_MEMORY_PERMISSION_ALL
[#](https://docs.nvidia.com#_CPPv4N35Sanitizer_ResourceMemoryPermissions31SANITIZER_MEMORY_PERMISSION_ALLE) Specifies that the allocation has all permissions.


-
enumerator SANITIZER_MEMORY_PERMISSION_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N35Sanitizer_ResourceMemoryPermissions37SANITIZER_MEMORY_PERMISSION_FORCE_INTE)

-
enumerator SANITIZER_MEMORY_PERMISSION_NONE

## Functions[#](https://docs.nvidia.com#id3)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerEnableAllDomains( *uint32_t enable*,,[Sanitizer_SubscriberHandle](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle)subscriberEnable or disable all callbacks in all domains.

Enable or disable all callbacks in all domains.

Note

**Thread-safety**: a subscriber must serialize access to sanitizerGetCallbackState, sanitizerEnableCallback, sanitizerEnableDomain, and sanitizerEnableAllDomains. For example, if sanitizerGetCallbackState(sub,

d, *) and sanitizerEnableAllDomains(sub) are called concurrently, the results are undefined.

- Parameters:
**enable**– New enable state for all callbacks in all domains. Zero disables all callbacks, non-zero enables all callbacks.**subscriber**– - Handle of the initialized subscriber.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`subscriber`

is invalid.



[#](https://docs.nvidia.com#_CPPv425sanitizerEnableAllDomains8uint32_t26Sanitizer_SubscriberHandle)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerEnableCallback( *uint32_t enable*,,[Sanitizer_SubscriberHandle](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle)subscriber,[Sanitizer_CallbackDomain](https://docs.nvidia.com#_CPPv424Sanitizer_CallbackDomain)domain,[Sanitizer_CallbackId](https://docs.nvidia.com#_CPPv420Sanitizer_CallbackId)cbidEnable or disable callbacks for a specific domain and callback ID.

Enable or disable callbacks for a subscriber for a specific domain and callback ID.

Note

**Thread-safety**: a subscriber must serialize access to sanitizerGetCallbackState, sanitizerEnableCallback, sanitizerEnableDomain, and sanitizerEnableAllDomains. For example, if sanitizerGetCallbackState(sub, d,

c) and sanitizerEnableCallback(sub, d, c) are called concurrently, the results are undefined.

- Parameters:
**enable**– New enable state for the callback. Zero disables the callback, non-zero enables the callback.**subscriber**– - Handle of the initialized subscriber.**domain**– The domain of the callback.**cbid**– The ID of the callback.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`subscriber`

,`domain`

or`cbid`

is invalid.



[#](https://docs.nvidia.com#_CPPv423sanitizerEnableCallback8uint32_t26Sanitizer_SubscriberHandle24Sanitizer_CallbackDomain20Sanitizer_CallbackId)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerEnableDomain( *uint32_t enable*,,[Sanitizer_SubscriberHandle](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle)subscriber,[Sanitizer_CallbackDomain](https://docs.nvidia.com#_CPPv424Sanitizer_CallbackDomain)domainEnable or disable all callbacks for a specific domain.

Enable or disable all callbacks for a specific domain.

Note

**Thread-safety**: a subscriber must serialize access to sanitizerGetCallbackState, sanitizerEnableCallback, sanitizerEnableDomain, and sanitizerEnableAllDomains. For example, if sanitizerGetCallbackEnabled(sub,

d, *) and sanitizerEnableDomain(sub, d) are called concurrently, the results are undefined.

- Parameters:
**enable**– New enable state for all callbacks in the domain. Zero disables all callbacks, non-zero enables all callbacks.**subscriber**– - Handle of the initialized subscriber.**domain**– The domain of the callback.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`subscriber`

or`domain`

is invalid.



[#](https://docs.nvidia.com#_CPPv421sanitizerEnableDomain8uint32_t26Sanitizer_SubscriberHandle24Sanitizer_CallbackDomain)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetCallbackState( *uint32_t *enable*,,[Sanitizer_SubscriberHandle](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle)subscriber,[Sanitizer_CallbackDomain](https://docs.nvidia.com#_CPPv424Sanitizer_CallbackDomain)domain,[Sanitizer_CallbackId](https://docs.nvidia.com#_CPPv420Sanitizer_CallbackId)cbidGet the current enabled/disabled state of a callback for a specific domain and function ID.

Returns non-zero in

`*enable`

if the callback for a domain and callback ID is enabled, and zero if not enabled.Note

**Thread-safety**: a subscriber must serialize access to sanitizerGetCallbackState, sanitizerEnableCallback, sanitizerEnableDomain, and sanitizerEnableAllDomains. For example, if sanitizerGetCallbackState(sub, d,

c) and sanitizerEnableCallback(sub, d, c) are called concurrently, the results are undefined.

- Parameters:
**enable**– Returns non-zero if callback enabled, zero if not enabled.**subscriber**– Handle to the initialized subscriber.**domain**– The domain of the callback.**cbid**– The ID of the callback.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`enabled`

is NULL, or if`subscriber`

,`domain`

or`cbid`

is invalid.



[#](https://docs.nvidia.com#_CPPv425sanitizerGetCallbackStateP8uint32_t26Sanitizer_SubscriberHandle24Sanitizer_CallbackDomain20Sanitizer_CallbackId)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerIsInsideRecursiveCallback( *uint32_t *isInside*,Check if the current thread is inside a recursive Sanitizer callback.

Returns whether the current thread is executing inside a nested (recursive) Sanitizer callback handler. This is useful for distinguishing between CUDA API calls made by the application versus calls made internally by Sanitizer itself during callback processing.

This function tracks callback re-entrancy depth and returns true only when the depth is greater than 1, indicating that a Sanitizer callback has triggered another callback. It returns false for the initial (non-nested) callback level.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**isInside**– Returns 1 if inside a recursive Sanitizer callback (depth > 1), 0 otherwise.- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`isInside`

is NULL.



[#](https://docs.nvidia.com#_CPPv434sanitizerIsInsideRecursiveCallbackP8uint32_t)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerSubscribe( ,[Sanitizer_SubscriberHandle](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle)*subscriber,[Sanitizer_CallbackFunc](https://docs.nvidia.com#_CPPv422Sanitizer_CallbackFunc)callback*void *userdata*,Initialize a callback subscriber with a callback function and user data.

Initialize a callback subscriber with a callback function and (optionally) a pointer to user data. The returned subscriber handle can be used to enable and disable the callback for specific domains and callback IDs.

Note

Only one subscriber can be registered at a time.

Note

This function does not enable any callbacks.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**subscriber**– Returns handle to initialize subscriber.**callback**– The callback function.**userdata**– A pointer to user data. This data will be passed to the callback function via the`userdata`

parameter.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_MAX_LIMIT_RACHED**– if there is already a sanitizer subscriber.**SANITIZER_ERROR_INVALID_PARAMETER**– if`subscriber`

is NULL.



[#](https://docs.nvidia.com#_CPPv418sanitizerSubscribeP26Sanitizer_SubscriberHandle22Sanitizer_CallbackFuncPv)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerUnsubscribe( ,[Sanitizer_SubscriberHandle](https://docs.nvidia.com#_CPPv426Sanitizer_SubscriberHandle)subscriberUnregister a callback subscriber.

Removes a callback subscriber so that no future callback will be issued to that subscriber.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**subscriber**– Handle to the initialized subscriber.- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`subscriber`

is NULL or not initialized.



[#](https://docs.nvidia.com#_CPPv420sanitizerUnsubscribe26Sanitizer_SubscriberHandle)