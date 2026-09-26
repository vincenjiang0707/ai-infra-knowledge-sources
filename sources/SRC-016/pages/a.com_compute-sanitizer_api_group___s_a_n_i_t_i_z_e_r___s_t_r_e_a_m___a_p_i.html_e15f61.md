source: https://docs.nvidia.com/compute-sanitizer/api/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html

# Sanitizer Stream API[#](https://docs.nvidia.com#sanitizer-stream-api)

Functions, types, and enums that implement the Sanitizer Stream API.

## Typedefs[#](https://docs.nvidia.com#typedefs)

## Functions[#](https://docs.nvidia.com#functions)

- SanitizerResult
[sanitizerGetStream](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i_1gacf7d648ebab00cb6cdeac009c8521723)(Sanitizer_StreamHandle hStream, CUstream *stream) Retrieve a CUstream handle from a Sanitizer_StreamHandle handle.

- SanitizerResult
[sanitizerGetStreamHandle](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i_1ga4d3a864c0bcdbeec09732aa7d1fa5ce8)(CUcontext ctx, CUstream stream, Sanitizer_StreamHandle *hStream) Retrieve a Sanitizer_StreamHandle handle from a CUstream handle.

- SanitizerResult
[sanitizerStreamSynchronize](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i_1gacb643e3eabde34487111d31a643aaba4)(Sanitizer_StreamHandle stream) Synchronize a given stream.


## Typedefs[#](https://docs.nvidia.com#id1)

-
typedef struct Sanitizer_Stream_st *Sanitizer_StreamHandle
[#](https://docs.nvidia.com#_CPPv422Sanitizer_StreamHandle)

## Functions[#](https://docs.nvidia.com#id2)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetStream( ,[Sanitizer_StreamHandle](https://docs.nvidia.com#_CPPv422Sanitizer_StreamHandle)hStream*CUstream *stream*,Retrieve a CUstream handle from a Sanitizer_StreamHandle handle.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**hStream**–**[in]**Sanitizer Stream handle.**stream**–**[out]**Output CUstream handle.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`hStream`

is not a valid Sanitizer stream handle or if`stream`

is NULL.



[#](https://docs.nvidia.com#_CPPv418sanitizerGetStream22Sanitizer_StreamHandleP8CUstream)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetStreamHandle( *CUcontext ctx*,*CUstream stream*,,[Sanitizer_StreamHandle](https://docs.nvidia.com#_CPPv422Sanitizer_StreamHandle)*hStreamRetrieve a Sanitizer_StreamHandle handle from a CUstream handle.

Note

**Thread-safety**: this function is thread safe.- Parameters:
**ctx**–**[in]**Context owning the stream. If NULL, the current context will be used.**stream**–**[in]**CUstream handle. If NULL, the NULL stream will be used.**hStream**–**[out]**Output Sanitizer Stream handle.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`stream`

is not a valid CUstream handle or if`hStream`

is NULL.



[#](https://docs.nvidia.com#_CPPv424sanitizerGetStreamHandle9CUcontext8CUstreamP22Sanitizer_StreamHandle)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerStreamSynchronize( ,[Sanitizer_StreamHandle](https://docs.nvidia.com#_CPPv422Sanitizer_StreamHandle)streamSynchronize a given stream.

Equivalent of cudaStreamSynchronize that can be called with a sanitizer stream handle

Note

**Thread-safety**: this function is thread safe.- Parameters:
**stream**– Stream handle. If NULL, the NULL stream will be used.


[#](https://docs.nvidia.com#_CPPv426sanitizerStreamSynchronize22Sanitizer_StreamHandle)