source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___resource_mempool_data.html

# Sanitizer_ResourceMempoolData[#](https://docs.nvidia.com#sanitizer-resourcemempooldata)

-
struct Sanitizer_ResourceMempoolData
[#](https://docs.nvidia.com#_CPPv429Sanitizer_ResourceMempoolData) Data passed into a mempool resource callback function.

Data passed into a mempool resource callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_RESOURCE and`cbid`

equal to SANITIZER_CBID_RESOURCE_MEMPOOL_CREATED, SANITIZER_CBID_RESOURCE_MEMPOOL_DESTROYING, SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_ENABLED or SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_DISABLING. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUdevice device
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMempoolData6deviceE) Device that owns the memory pool.


-
CUmemoryPool memoryPool
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMempoolData10memoryPoolE) Memory pool being created or destroyed.


-
CUdevice peerDevice
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceMempoolData10peerDeviceE) Device that access type changed.

Available if cbid is SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_ENABLED or SANITIZER_CBID_RESOURCE_MEMPOOL_PEER_ACCESS_DISABLING.


-
CUdevice device