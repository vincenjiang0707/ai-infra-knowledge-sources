source: https://docs.nvidia.com/cuda/npp/image_memory_management.html

# Image Memory Management Functions[](https://docs.nvidia.com#image-memory-management-functions)

Routines for allocating and deallocating pitched image storage.

These methods are provided for convenience. They allocate memory that may contain additional padding bytes at the end of each line of pixels. Though padding is not necessary for any of the NPP image-processing primitives to work correctly, its absence may cause sever performance degradation compared to properly padded images.

These functions can be found in the nppisu library. Linking to only the sub-libraries that you use can significantly save link time, application load time, and CUDA runtime startup time when using dynamic libraries.

Image Memory Allocation

ImageAllocator methods for 2D arrays of data.

The allocators have width and height parameters to specify the size of the image data being allocated. They return a pointer to the newly created memory and return the numbers of bytes between successive lines.

If the memory allocation failed due to lack of free device memory or device memory fragmentation the routine returns 0.

All allocators return memory with line strides that are beneficial for performance. It is not mandatory to use these allocators. Any valid CUDA device-memory pointers can be used by the NPP primitives and there are no restrictions on line strides.

-
[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*nppiMalloc_8u_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_8u_C1)

-
8-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*nppiMalloc_8u_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_8u_C2)

-
2 channel 8-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*nppiMalloc_8u_C3(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_8u_C3)

-
3 channel 8-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*nppiMalloc_8u_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_8u_C4)

-
4 channel 8-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*nppiMalloc_16u_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16u_C1)

-
16-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*nppiMalloc_16u_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16u_C2)

-
2 channel 16-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*nppiMalloc_16u_C3(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16u_C3)

-
3 channel 16-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*nppiMalloc_16u_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16u_C4)

-
4 channel 16-bit unsigned image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*nppiMalloc_16s_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16s_C1)

-
16-bit signed image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*nppiMalloc_16s_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16s_C2)

-
2 channel 16-bit signed image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*nppiMalloc_16s_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16s_C4)

-
4 channel 16-bit signed image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*nppiMalloc_16sc_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16sc_C1)

-
1 channel 16-bit signed complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*nppiMalloc_16sc_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16sc_C2)

-
2 channel 16-bit signed complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*nppiMalloc_16sc_C3(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16sc_C3)

-
3 channel 16-bit signed complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*nppiMalloc_16sc_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_16sc_C4)

-
4 channel 16-bit signed complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*nppiMalloc_32s_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32s_C1)

-
32-bit signed image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*nppiMalloc_32s_C3(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32s_C3)

-
3 channel 32-bit signed image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*nppiMalloc_32s_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32s_C4)

-
4 channel 32-bit signed image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*nppiMalloc_32sc_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32sc_C1)

-
32-bit integer complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*nppiMalloc_32sc_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32sc_C2)

-
2 channel 32-bit integer complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*nppiMalloc_32sc_C3(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32sc_C3)

-
3 channel 32-bit integer complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*nppiMalloc_32sc_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32sc_C4)

-
4 channel 32-bit integer complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*nppiMalloc_32f_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32f_C1)

-
32-bit floating point image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*nppiMalloc_32f_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32f_C2)

-
2 channel 32-bit floating point image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*nppiMalloc_32f_C3(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32f_C3)

-
3 channel 32-bit floating point image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*nppiMalloc_32f_C4(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32f_C4)

-
4 channel 32-bit floating point image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*nppiMalloc_32fc_C1(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32fc_C1)

-
32-bit float complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



-
[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*nppiMalloc_32fc_C2(int nWidthPixels, int nHeightPixels, int *pStepBytes)[](https://docs.nvidia.com#c.nppiMalloc_32fc_C2)

-
2 channel 32-bit float complex image memory allocator.

- Parameters
-
**nWidthPixels**– Image width.**nHeightPixels**– Image height.**pStepBytes**–[Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1line_step).

- Returns
-
Pointer to new image data.



Functions

-
void nppiFree(void *pData)
[](https://docs.nvidia.com#c.nppiFree)

-
Free method for any 2D allocated memory.

This method should be used to free memory allocated with any of the nppiMalloc_<modifier> methods.

- Parameters
-
**pData**– A pointer to memory allocated using nppiMalloc_<modifier>.