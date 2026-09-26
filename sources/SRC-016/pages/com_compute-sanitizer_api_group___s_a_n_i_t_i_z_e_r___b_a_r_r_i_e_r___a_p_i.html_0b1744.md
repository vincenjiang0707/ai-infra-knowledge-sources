source: https://docs.nvidia.com/compute-sanitizer/api/group___s_a_n_i_t_i_z_e_r___b_a_r_r_i_e_r___a_p_i.html

# Sanitizer Barrier API[#](https://docs.nvidia.com#sanitizer-barrier-api)

Functions, types, and enums that implement the Sanitizer Barrier API.

## Functions[#](https://docs.nvidia.com#functions)

- SanitizerResult
[sanitizerGetCudaBarrierCount](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___b_a_r_r_i_e_r___a_p_i_1gadb6d5f978fac44e43116980011b1507b)(CUfunction kernel, uint32_t *numBarriers) Get number of CUDA barriers used by a function.


## Functions[#](https://docs.nvidia.com#id1)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetCudaBarrierCount( *CUfunction kernel*,*uint32_t *numBarriers*,Get number of CUDA barriers used by a function.

The module where

`kernel`

resides must have been instrumented using[sanitizerPatchModule](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i.html#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92)prior to calling this function. This function is only available for modules built with nvcc 11.2 or newer, it will return 0 otherwise.Note

**Thread-safety**: this function is thread safe.- Parameters:
**kernel**–**[in]**CUDA function.**numBarriers**–**[out]**Number of CUDA barriers in the input CUDA function.



[#](https://docs.nvidia.com#_CPPv428sanitizerGetCudaBarrierCount10CUfunctionP8uint32_t)