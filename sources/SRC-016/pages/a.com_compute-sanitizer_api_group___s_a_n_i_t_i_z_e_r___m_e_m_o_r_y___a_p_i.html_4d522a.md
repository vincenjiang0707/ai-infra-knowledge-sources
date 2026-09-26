source: https://docs.nvidia.com/compute-sanitizer/api/group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i.html

# Sanitizer Memory API[#](https://docs.nvidia.com#sanitizer-memory-api)

Functions, types, and enums that implement the Sanitizer Memory API.

## Functions[#](https://docs.nvidia.com#functions)

- SanitizerResult
[sanitizerAlloc](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1gae79baddc2606f95c4a08b329d91eba1f)(CUcontext ctx, void **devPtr, size_t size) Allocate memory on the device.

- SanitizerResult
[sanitizerAllocHost](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1gae0e449b985a82593b51e74b903c894c1)(CUcontext ctx, void **devPtr, size_t size) Allocate host pinned memory.

- SanitizerResult
[sanitizerFree](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1gaf98cbb040c6ad85e0d4666a1fac8c706)(CUcontext ctx, void *devPtr) Frees memory on the device.

- SanitizerResult
[sanitizerFreeHost](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1gac7063c0ded9edc4754ce71f522b6e176)(CUcontext ctx, void *devPtr) Frees host memory.

- SanitizerResult
[sanitizerMemcpyDeviceToHost](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1ga07274beaf9942d2bbd408f30d84d18a6)(void *dst, void *src, size_t count, Sanitizer_StreamHandle stream) Copies data from device to host.

- SanitizerResult
[sanitizerMemcpyHostToDeviceAsync](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1ga0966da96869961ba0eb940549d83c3d3)(void *dst, void *src, size_t count, Sanitizer_StreamHandle stream) Copies data from host to device.

- SanitizerResult
[sanitizerMemset](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___m_e_m_o_r_y___a_p_i_1ga3882bef4021470a075c241d90c99cabb)(void *devPtr, int value, size_t count, Sanitizer_StreamHandle stream) Initializes or sets device memory to a value.


## Functions[#](https://docs.nvidia.com#id1)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerAlloc( *CUcontext ctx*,*void **devPtr*,*size_t size*,Allocate memory on the device.

Equivalent of cudaMalloc that can be called within a callback function.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**ctx**– Context for the allocation. If NULL, the current context will be used.**devPtr**– Pointer to allocated device memory.**size**– Allocation size in bytes.



[#](https://docs.nvidia.com#_CPPv414sanitizerAlloc9CUcontextPPv6size_t)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerAllocHost( *CUcontext ctx*,*void **devPtr*,*size_t size*,Allocate host pinned memory.

Equivalent of cudaMallocHost that can be called within a callback function.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**ctx**– Context for the allocation. If NULL, the current context will be used.**devPtr**– Pointer to allocated host memory.**size**– Allocation size in bytes.



[#](https://docs.nvidia.com#_CPPv418sanitizerAllocHost9CUcontextPPv6size_t)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerFree(*CUcontext ctx*,*void *devPtr*)[#](https://docs.nvidia.com#_CPPv413sanitizerFree9CUcontextPv) Frees memory on the device.

Equivalent of cudaFree that can be called within a callback function.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**ctx**– Context for the allocation. If NULL, the current context will be used.**devPtr**– Device pointer to memory to free.



-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerFreeHost(*CUcontext ctx*,*void *devPtr*)[#](https://docs.nvidia.com#_CPPv417sanitizerFreeHost9CUcontextPv) Frees host memory.

Equivalent of cudaFreeHost that can be called within a callback function.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**ctx**– Context for the allocation. If NULL, the current context will be used.**devPtr**– Host pointer to memory to free.



-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerMemcpyDeviceToHost( *void *dst*,*void *src*,*size_t count*,,[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)streamCopies data from device to host.

Equivalent of cudaMemcpy that can be called within a callback function. The function will return once the copy has completed.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**dst**– Destination memory address.**src**– Source memory address.**count**– Size in bytes to copy.**stream**– Stream handle. If NULL, the NULL stream will be used.



[#](https://docs.nvidia.com#_CPPv427sanitizerMemcpyDeviceToHostPvPv6size_t22Sanitizer_StreamHandle)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerMemcpyHostToDeviceAsync( *void *dst*,*void *src*,*size_t count*,,[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)streamCopies data from host to device.

Equivalent of cudaMemcpyAsync that can be called within a callback function. The function will return once the pageable buffer has been copied to the staging memory for DMA transfer to device memory, but the DMA to final destination may not have completed.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**dst**– Destination memory address.**src**– Source memory address.**count**– Size in bytes to copy.**stream**– Stream handle. If NULL, the NULL stream will be used.



[#](https://docs.nvidia.com#_CPPv432sanitizerMemcpyHostToDeviceAsyncPvPv6size_t22Sanitizer_StreamHandle)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerMemset( *void *devPtr*,*int value*,*size_t count*,,[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)streamInitializes or sets device memory to a value.

Equivalent of cudaMemset that can be called within a callback function.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**devPtr**– Pointer to device memory.**value**– value to set for each byte of specified memory.**count**– Size in bytes to set.**stream**– Stream handle. If NULL, the NULL stream will be used.



[#](https://docs.nvidia.com#_CPPv415sanitizerMemsetPvi6size_t22Sanitizer_StreamHandle)