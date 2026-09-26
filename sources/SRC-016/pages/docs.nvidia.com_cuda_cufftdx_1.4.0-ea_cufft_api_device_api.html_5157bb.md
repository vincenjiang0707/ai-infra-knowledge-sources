source: https://docs.nvidia.com/cuda/cufftdx/1.4.0-ea/cufft_api/device_api.html

# cuFFT Device API Reference[#](https://docs.nvidia.com#cufft-device-api-reference)

This section describes the extension to the cuFFT API included in the cuFFTDx + cuFFT LTO EA package. It contains a collection of host functions that can be used to query or generate device function code along with the database metadata (a C++ header file) that can be used together with the cuFFTDx library.

Note

All functions discussed in this section are defined in the `cufft/include/cufft_device.h`

header file.

## Version Information[#](https://docs.nvidia.com#version-information)

### cufftDeviceGetVersion[#](https://docs.nvidia.com#cufftdevicegetversion)

-
cufftResult cufftDeviceGetVersion(
*int *version*)[#](https://docs.nvidia.com#c.cufftDeviceGetVersion) Returns the version of the device code output by the cuFFT library, i.e.,

`CUFFT_DEVICE_VERSION`

defined in`cufft_device.h`

. Note that this is a separate versioning from the version of the cuFFT library itself.- Parameters:
**version[Out]**– Pointer to store the version number.

- Return values:
**CUFFT_SUCCESS**– Version number was successfully retrieved.**CUFFT_INVALID_VALUE**– The`version`

pointer is`NULL`

.



## Description Management[#](https://docs.nvidia.com#description-management)

The set of functions used to specify which FFT implementations should be included in the database.

### cufftDescriptionCreate[#](https://docs.nvidia.com#cufftdescriptioncreate)

- cufftResult cufftDescriptionCreate(
*cufftDescriptionHandle *desc_handle*,Creates a new FFT description handle.

- Parameters:
**desc_handle[In]**– Pointer to a`cufftDescriptionHandle`

object.**desc_handle[Out]**– Contains a`cufftDescriptionHandle`

handle value.

- Return values:
**CUFFT_SUCCESS**– Description handle was successfully created.**CUFFT_INVALID_VALUE**– The handle pointer is`NULL`

.**CUFFT_INTERNAL_ERROR**– The internal handle factory reaches its maximum capacity.



[#](https://docs.nvidia.com#c.cufftDescriptionCreate)

### cufftDescriptionTrait[#](https://docs.nvidia.com#cufftdescriptiontrait)

Traits that can be set or queried for a FFT description (`cufftDescriptionHandle`

).
These traits map to (a subset of) cuFFTDx [Operators](https://docs.nvidia.com/cuda/cufftdx/api/operators.html).
See comments in the code block below for mapping between traits and cuFFTDx operators.

```
typedef enum cufftDescriptionTrait_t {
CUFFT_DESC_TRAIT_SIZE, // See cufftdx::Size Operator.
// Value: unsigned int
CUFFT_DESC_TRAIT_DIRECTION, // See cufftdx::Direction Operator.
// Value: CUFFT_DESC_DIRECTION_<UNSET/FORWARD/INVERSE>
CUFFT_DESC_TRAIT_PRECISION, // See cufftdx::Precision Operator.
// Value: CUFFT_DESC_<SINGLE/DOUBLE>
CUFFT_DESC_TRAIT_TYPE, // See cufftdx::Type Operator.
// Value: CUFFT_DESC_<C2C/C2R/R2C>
CUFFT_DESC_TRAIT_SM, // See cufftdx::SM Operator.
// Value: unsigned int (e.g., 700, 800, 900)
CUFFT_DESC_TRAIT_REAL_MODE, // See cufftdx::RealMode Operator.
// Value: CUFFT_DESC_<NORMAL/FOLDED>
CUFFT_DESC_TRAIT_EXEC_OP, // See cufftdx::Thread, cufftdx::Block Operators.
// Value: CUFFT_DESC_<EXEC_OP_UNSET/THREAD/BLOCK>
CUFFT_DESC_TRAIT_ELEMENTS_PER_THREAD // See cufftdx::ElementsPerThread Operator.
// Value: unsigned int
} cufftDescriptionTrait;
```

Note

The default value of each trait matches the default value of the corresponding cuFFTDx operator.

### cufftDescriptionSetTraitInt64[#](https://docs.nvidia.com#cufftdescriptionsettraitint64)

- cufftResult cufftDescriptionSetTraitInt64(
*cufftDescriptionHandle desc_handle*,*cufftDescriptionTrait trait*,*const long long int value*,Sets a trait value for a FFT description.

- Parameters:
**desc_handle[In]**–`cufftDescriptionHandle`

returned by[cufftDescriptionCreate](https://docs.nvidia.com#api-reference-cufftdescriptioncreate-ea-label).**trait[In]**– The trait identifier, of type[cufftDescriptionTrait](https://docs.nvidia.com#api-reference-cufftdescriptionctrait-ea-label), to set.**value[In]**– The value to set for the trait. See comments in[cufftDescriptionTrait](https://docs.nvidia.com#api-reference-cufftdescriptionctrait-ea-label)for valid values.

- Return values:
**CUFFT_SUCCESS**– Trait was successfully set.**CUFFT_INVALID_VALUE**– Invalid`handle`

or`trait`

.



[#](https://docs.nvidia.com#c.cufftDescriptionSetTraitInt64)

### cufftDescriptionGetTraitInt64[#](https://docs.nvidia.com#cufftdescriptiongettraitint64)

- cufftResult cufftDescriptionGetTraitInt64(
*cufftDescriptionHandle desc_handle*,*cufftDescriptionTrait trait*,*long long int *value*,Gets a trait value from an FFT description.

- Parameters:
**desc_handle[In]**–`cufftDescriptionHandle`

returned by[cufftDescriptionCreate](https://docs.nvidia.com#api-reference-cufftdescriptioncreate-ea-label).**trait[In]**– The trait identifier, of type[cufftDescriptionTrait](https://docs.nvidia.com#api-reference-cufftdescriptionctrait-ea-label), to query.**value[Out]**– Pointer to store the trait value.

- Return values:
**CUFFT_SUCCESS**– Trait value was successfully retrieved.**CUFFT_INVALID_VALUE**– Invalid`handle`

or`trait`

.



[#](https://docs.nvidia.com#c.cufftDescriptionGetTraitInt64)

## Device Management[#](https://docs.nvidia.com#device-management)

The set of functions that establish and manage mappings between FFT descriptions and their corresponding device functions and building blocks.

### cufftDeviceCreate[#](https://docs.nvidia.com#cufftdevicecreate)

- cufftResult cufftDeviceCreate(
*cufftDeviceHandle *handle*,*size_t desc_count*,*cufftDescriptionHandle *desc_handles*,Creates a new device handle with the specified FFT descriptions. For each FFT description provided, cuFFT will search for device functions with matching traits as well as the building blocks needed to generate the device functions.

- Parameters:
**handle[In]**– Pointer to a`cufftDeviceHandle`

object.**handle[Out]**– Contains a`cufftDeviceHandle`

handle value.**desc_count[In]**– Number of descriptions.**desc_handles[In]**– Pointer to an array of description handles with length`desc_count`

.

- Return values:
**CUFFT_SUCCESS**– Device handle was successfully created.**CUFFT_INVALID_VALUE**–The handle pointer or the pointer to the description handles pointer is

`NULL`

.Any of the description handles used in the array is invalid.


**CUFFT_INTERNAL_ERROR**– The internal handle factory reaches its maximum capacity.



[#](https://docs.nvidia.com#c.cufftDeviceCreate)

Note

We do not return an error if there is no matching device function or if the combinations of the traits values is invalid for the given description handles. This allows users to create a chunk of descriptions at once, and filter out the unsupported ones later in a separate step.

One could use [cufftDeviceCheckDescription](https://docs.nvidia.com#api-reference-cufftdevicecheckdescription-ea-label) defined below to check whether a description is valid, supported, or unsupported.

### cufftDeviceCheckDescription[#](https://docs.nvidia.com#cufftdevicecheckdescription)

- cufftResult cufftDeviceCheckDescription(
*cufftDeviceHandle handle*,*cufftDescriptionHandle desc_handle*,Checks whether a description associated with the device handle is valid, supported, or unsupported.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**desc_handle[In]**–`cufftDescriptionHandle`

returned by[cufftDescriptionCreate](https://docs.nvidia.com#api-reference-cufftdescriptioncreate-ea-label).

- Return values:
**CUFFT_SUCCESS**– Description is valid and supported.**CUFFT_INVALID_VALUE**–Device handle

`handle`

or description handle`desc_handle`

is invalid.The traits of the description are invalid, e.g.

`CUFFT_DESC_TRAIT_SIZE`

or`CUFFT_DESC_TRAIT_SM`

is not set.

**CUFFT_NOT_SUPPORTED**– The description is not supported. No matched device function is found.



[#](https://docs.nvidia.com#c.cufftDeviceCheckDescription)

Note

We enforce the same conditions as [cufftdx::is_complete_fft_execution<FFT>::value](https://docs.nvidia.com/cuda/cufftdx/api/traits.html#isfftcompleteexecution-trait-label) when validating the description handle.

### cufftDeviceDestroy[#](https://docs.nvidia.com#cufftdevicedestroy)

-
cufftResult cufftDeviceDestroy(
*cufftDeviceHandle handle*)[#](https://docs.nvidia.com#c.cufftDeviceDestroy) Destroys a device handle and frees associated resources.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).

- Return values:
**CUFFT_SUCCESS**– Device handle was successfully destroyed.**CUFFT_INVALID_VALUE**– Invalid`handle`

.



## Device Function Management[#](https://docs.nvidia.com#device-function-management)

The set of functions for retrieving device functions and device function traits.

### cufftDeviceGetNumDeviceFunctions[#](https://docs.nvidia.com#cufftdevicegetnumdevicefunctions)

- cufftResult cufftDeviceGetNumDeviceFunctions(
*cufftDeviceHandle handle*,*cufftDescriptionHandle desc_handle*,*size_t *func_count*,Gets the number of device functions that match a given description from the associated device handle. If the description is unsupported, i.e. no matched device function is found, or the traits of the description are invalid,

`0`

is returned.- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**desc_handle[In]**–`cufftDescriptionHandle`

returned by[cufftDescriptionCreate](https://docs.nvidia.com#api-reference-cufftdescriptioncreate-ea-label).**func_count[Out]**– Pointer to store the number of functions.

- Return values:
**CUFFT_SUCCESS**– Function count was successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`desc_handle`

.`func_count`

pointer is`NULL`

.




[#](https://docs.nvidia.com#c.cufftDeviceGetNumDeviceFunctions)

### cufftDeviceGetDeviceFunctions[#](https://docs.nvidia.com#cufftdevicegetdevicefunctions)

- cufftResult cufftDeviceGetDeviceFunctions(
*cufftDeviceHandle handle*,*cufftDescriptionHandle desc_handle*,*size_t func_count*,*cufftDeviceFunctionHandle *func_handles*,Retrieves an array of device function handles that matches a given description associated with the device handle.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**desc_handle[In]**–`cufftDescriptionHandle`

returned by[cufftDescriptionCreate](https://docs.nvidia.com#api-reference-cufftdescriptioncreate-ea-label).**func_count[In]**– Number of function handles to retrieve. Value returned by[cufftDeviceGetNumDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetnumdevicefunctions-ea-label).**func_handles[Out]**– Array to store the function handles.

- Return values:
**CUFFT_SUCCESS**– Function handles were successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`desc_handle`

.`func_handles`

pointer is`NULL`

.`func_count`

is not equal to the number of functions returned by[cufftDeviceGetNumDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetnumdevicefunctions-ea-label).




[#](https://docs.nvidia.com#c.cufftDeviceGetDeviceFunctions)

### cufftDeviceFunctionTrait[#](https://docs.nvidia.com#cufftdevicefunctiontrait)

Traits that can be queried for a device function (`cufftDeviceFunctionHandle`

).

```
typedef enum cufftDeviceFunctionTrait_t {
CUFFT_DEVICE_FUNC_TRAIT_ELEMENTS_PER_THREAD, // Elements per thread
CUFFT_DEVICE_FUNC_TRAIT_STORAGE_SIZE, // Storage elements per thread
CUFFT_DEVICE_FUNC_TRAIT_SHARED_MEMORY_PER_FFT, // Shared memory per FFT
CUFFT_DEVICE_FUNC_TRAIT_THREADS_PER_FFT, // Threads per FFT
CUFFT_DEVICE_FUNC_TRAIT_FFTS_PER_BLOCK, // Number of FFTs processed per block
} cufftDeviceFunctionTrait;
```

### cufftDeviceGetDeviceFunctionTraitInt64[#](https://docs.nvidia.com#cufftdevicegetdevicefunctiontraitint64)

- cufftResult cufftDeviceGetDeviceFunctionTraitInt64(
*cufftDeviceHandle handle*,*cufftDeviceFunctionHandle func_handle*,*cufftDeviceFunctionTrait trait*,*long long int *value*,Gets a trait value from a device function.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**func_handle[In]**–`cufftDeviceFunctionHandle`

returned by[cufftDeviceGetDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetdevicefunctions-ea-label).**trait[In]**– The trait identifier, of type[cufftDeviceFunctionTrait](https://docs.nvidia.com#api-reference-cufftdevicefunction-traits-ea-label), to query.**value[Out]**– Pointer to store the trait value.

- Return values:
**CUFFT_SUCCESS**– Trait value was successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

,`func_handle`

or`trait`

.`value`

pointer is`NULL`

.




[#](https://docs.nvidia.com#c.cufftDeviceGetDeviceFunctionTraitInt64)

## Database and Code Management[#](https://docs.nvidia.com#database-and-code-management)

The set of functions for retrieving:

- LTOIRs that can be used to
Build all the device functions associated with the device handle (

`cufftDeviceHandle`

).Build a specific device function when a function handle (

`cufftDeviceFunctionHandle`

) is provided.


Database metadata (a C++ header file).


These components, when used in combination with the cuFFTDx library, can be used to build kernels that compute the specified FFTs using LTO.

### cufftDeviceGetDatabaseStrSize[#](https://docs.nvidia.com#cufftdevicegetdatabasestrsize)

- cufftResult cufftDeviceGetDatabaseStrSize(
*cufftDeviceHandle handle*,*size_t *db_str_size*,*cufftDeviceFunctionHandle func_handle*,Gets the size of the database string.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**db_str_size[Out]**– Pointer to store the database string size.**func_handle[In]**– (optional) Any`cufftDeviceFunctionHandle`

returned by[cufftDeviceGetDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetdevicefunctions-ea-label).

- Return values:
**CUFFT_SUCCESS**– Database string size was successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`func_handle`

.`db_str_size`

pointer is`NULL`

.




[#](https://docs.nvidia.com#c.cufftDeviceGetDatabaseStrSize)

### cufftDeviceGetDatabaseStr[#](https://docs.nvidia.com#cufftdevicegetdatabasestr)

- cufftResult cufftDeviceGetDatabaseStr(
*cufftDeviceHandle handle*,*size_t db_str_size*,*char *db_str*,*cufftDeviceFunctionHandle func_handle = 0*,Retrieves the database string.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**db_str_size[In]**– Size of the buffer to store the database string. Value returned by[cufftDeviceGetDatabaseStrSize](https://docs.nvidia.com#api-reference-cufftdevicegetdatabasestrsize-ea-label).**db_str[Out]**– Buffer to store the database string with size`db_str_size`

.**func_handle[In]**– (optional) Any`cufftDeviceFunctionHandle`

returned by[cufftDeviceGetDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetdevicefunctions-ea-label).

- Return values:
**CUFFT_SUCCESS**– Database string was successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`func_handle`

.`db_str_size`

pointer is`NULL`

.`db_str_size`

is not equal to the size of the database string returned by[cufftDeviceGetDatabaseStrSize](https://docs.nvidia.com#api-reference-cufftdevicegetdatabasestrsize-ea-label).




[#](https://docs.nvidia.com#c.cufftDeviceGetDatabaseStr)

### cufftDeviceGetNumLTOIRs[#](https://docs.nvidia.com#cufftdevicegetnumltoirs)

- cufftResult cufftDeviceGetNumLTOIRs(
*cufftDeviceHandle handle*,*size_t *code_count*,*cufftDeviceFunctionHandle func_handle = 0*,Gets the number of LTOIRs.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**code_count[Out]**– Pointer to store the number of LTOIRs.**func_handle[In]**– (optional) Any`cufftDeviceFunctionHandle`

returned by[cufftDeviceGetDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetdevicefunctions-ea-label).

- Return values:
**CUFFT_SUCCESS**– Code count was successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`func_handle`

.`code_count`

pointer is`NULL`

.




[#](https://docs.nvidia.com#c.cufftDeviceGetNumLTOIRs)

### cufftDeviceGetLTOIRSizes[#](https://docs.nvidia.com#cufftdevicegetltoirsizes)

- cufftResult cufftDeviceGetLTOIRSizes(
*cufftDeviceHandle handle*,*size_t code_count*,*size_t *code_sizes*,*cufftDeviceFunctionHandle func_handle = 0*,Gets the sizes of LTOIRs.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**code_count[In]**– Number of LTOIRs. Value returned by[cufftDeviceGetNumLTOIRs](https://docs.nvidia.com#api-reference-cufftdevicegetnumltoirs-ea-label).**code_sizes[Out]**– Pointer to an array of size`code_count`

to store LTOIR sizes.**func_handle[In]**– (optional) Any`cufftDeviceFunctionHandle`

returned by[cufftDeviceGetDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetdevicefunctions-ea-label).

- Return values:
**CUFFT_SUCCESS**– Code sizes were successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`func_handle`

.`code_count`

pointer is`NULL`

.`code_count`

is not equal to the number of LTOIRs returned by[cufftDeviceGetNumLTOIRs](https://docs.nvidia.com#api-reference-cufftdevicegetnumltoirs-ea-label).




[#](https://docs.nvidia.com#c.cufftDeviceGetLTOIRSizes)

### cufftDeviceCodeType[#](https://docs.nvidia.com#cufftdevicecodetype)

There are two types of codes that can be returned by [cufftDeviceGetNumLTOIRs](https://docs.nvidia.com#api-reference-cufftdevicegetnumltoirs-ea-label):

LTOIRs and

fatbinary containing LTOIRs.


```
typedef enum cufftDeviceCodeType_t {
CUFFT_DEVICE_LTOIR = 0,
CUFFT_DEVICE_FATBIN = 1
} cufftDeviceCodeType;
```

### cufftDeviceGetLTOIRs[#](https://docs.nvidia.com#cufftdevicegetltoirs)

- cufftResult cufftDeviceGetLTOIRs(
*cufftDeviceHandle handle*,*size_t code_count*,*char **code_ptrs*,*cufftDeviceCodeType *code_types*,*cufftDeviceFunctionHandle func_handle = 0*,Retrieves the LTOIRs.

- Parameters:
**handle[In]**–`cufftDeviceHandle`

returned by[cufftDeviceCreate](https://docs.nvidia.com#api-reference-cufftdevicecreate-ea-label).**code_count[In]**– Number of LTOIRs to retrieve. Value returned by[cufftDeviceGetNumLTOIRs](https://docs.nvidia.com#api-reference-cufftdevicegetnumltoirs-ea-label).**code_ptrs[Out]**– Pointer to an array of array of`char`

to store the LTOIRs.**code_types[Out]**– Pointer to an array of`cufftDeviceCodeType`

with length`code_count`

to store the code types.**func_handle[In]**– (optional) Any`cufftDeviceFunctionHandle`

returned by[cufftDeviceGetDeviceFunctions](https://docs.nvidia.com#api-reference-cufftdevicegetdevicefunctions-ea-label).

- Return values:
**CUFFT_SUCCESS**– LTOIRs were successfully retrieved.**CUFFT_INVALID_VALUE**–Invalid

`handle`

or`func_handle`

.`code_ptrs`

pointer or`code_types`

pointer is`NULL`

.`code_count`

is not equal to the number of LTOIRs returned by[cufftDeviceGetNumLTOIRs](https://docs.nvidia.com#api-reference-cufftdevicegetnumltoirs-ea-label).




[#](https://docs.nvidia.com#c.cufftDeviceGetLTOIRs)

Note

When writing the data to disk, it is important to write to files with the right file extensions, `.ltoir`

for LTOIRs (`CUFFT_DEVICE_LTOIR`

) and `.fatbin`

for fatbinaries (`CUFFT_DEVICE_FATBIN`

). Otherwise, NVCC will fail to recognize the files.