source: https://docs.nvidia.com/cuda/npp/signal_memory_management.html

# Signal Memory Management Functions[](https://docs.nvidia.com#signal-memory-management-functions)

Functions that provide memory management functionality like malloc and free.

## Malloc[](https://docs.nvidia.com#group__signal__malloc_1signal_malloc)

Signal-allocator methods for allocating 1D arrays of data in device memory. All allocators have size parameters to specify the size of the signal (1D array) being allocated.

The allocator methods return a pointer to the newly allocated memory of appropriate type. If device-memory allocation is not possible due to resource constraints the allocators return 0 (i.e. NULL pointer).

All signal allocators allocate memory aligned such that it is beneficial to the performance of the majority of the signal-processing primitives. It is no mandatory however to use these allocators. Any valid CUDA device-memory pointers can be passed to NPP primitives.

Functions

-
[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*nppsMalloc_8u(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_8u)

-
8-bit unsigned signal allocator.

- Parameters
-
**nSize**– Number of unsigned chars in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*nppsMalloc_8s(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_8s)

-
8-bit signed signal allocator.

- Parameters
-
**nSize**– Number of (signed) chars in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*nppsMalloc_16u(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_16u)

-
16-bit unsigned signal allocator.

- Parameters
-
**nSize**– Number of unsigned shorts in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*nppsMalloc_16s(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_16s)

-
16-bit signal allocator.

- Parameters
-
**nSize**– Number of shorts in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*nppsMalloc_16sc(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_16sc)

-
16-bit complex-value signal allocator.

- Parameters
-
**nSize**– Number of 16-bit complex numbers in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*nppsMalloc_32u(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_32u)

-
32-bit unsigned signal allocator.

- Parameters
-
**nSize**– Number of unsigned ints in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*nppsMalloc_32s(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_32s)

-
32-bit integer signal allocator.

- Parameters
-
**nSize**– Number of ints in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*nppsMalloc_32sc(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_32sc)

-
32-bit complex integer signal allocator.

- Parameters
-
**nSize**– Number of complex integer values in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*nppsMalloc_32f(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_32f)

-
32-bit float signal allocator.

- Parameters
-
**nSize**– Number of floats in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*nppsMalloc_32fc(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_32fc)

-
32-bit complex float signal allocator.

- Parameters
-
**nSize**– Number of complex float values in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp64s](https://docs.nvidia.com/nppdefs.html#c.Npp64s)*nppsMalloc_64s(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_64s)

-
64-bit long integer signal allocator.

- Parameters
-
**nSize**– Number of long ints in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



-
[Npp64sc](https://docs.nvidia.com/nppdefs.html#c.Npp64sc)*nppsMalloc_64sc(size_t nSize)[](https://docs.nvidia.com#c.nppsMalloc_64sc)

-
64-bit complex long integer signal allocator.

- Parameters
-
**nSize**– Number of complex long int values in the new signal.

- Returns
-
A pointer to the new signal. 0 (NULL-pointer) indicates that an error occurred during allocation.



## Free[](https://docs.nvidia.com#group__signal__free_1signal_free)

Free signal memory.

Functions

-
void nppsFree(void *pValues)
[](https://docs.nvidia.com#c.nppsFree)

-
Free method for any signal memory.

- Parameters
-
**pValues**– A pointer to memory allocated using nppiMalloc_<modifier>.