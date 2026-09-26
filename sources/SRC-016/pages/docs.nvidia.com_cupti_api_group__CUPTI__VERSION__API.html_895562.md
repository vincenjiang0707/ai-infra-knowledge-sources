source: https://docs.nvidia.com/cupti/api/group__CUPTI__VERSION__API.html

# 6.13. CUPTI Version[#](https://docs.nvidia.com#cupti-version)

Function and macro to determine the CUPTI version.

## 6.13.1. Macros[#](https://docs.nvidia.com#macros)

[CUPTI_API_VERSION](https://docs.nvidia.com#group__cupti__version__api_1ga162a01934e005491e65643ca63dbf6a3)The API version for this implementation of CUPTI.


## 6.13.2. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiGetVersion](https://docs.nvidia.com#group__cupti__version__api_1ga0e63a0d235c5e7e5231cc78ec63fa981)(uint32_t *version) Get the CUPTI API version.


## 6.13.3. Macros[#](https://docs.nvidia.com#id1)

-
CUPTI_API_VERSION
[#](https://docs.nvidia.com#c.CUPTI_API_VERSION) The API version for this implementation of CUPTI.

The API version for this implementation of CUPTI. This define along with

[cuptiGetVersion](https://docs.nvidia.com#group__cupti__version__api_1ga0e63a0d235c5e7e5231cc78ec63fa981)can be used to dynamically detect if the version of CUPTI compiled against matches the version of the loaded CUPTI library.v1 : CUDAToolsSDK 4.0 v2 : CUDAToolsSDK 4.1 v3 : CUDA Toolkit 5.0 v4 : CUDA Toolkit 5.5 v5 : CUDA Toolkit 6.0 v6 : CUDA Toolkit 6.5 v7 : CUDA Toolkit 6.5(with sm_52 support) v8 : CUDA Toolkit 7.0 v9 : CUDA Toolkit 8.0 v10 : CUDA Toolkit 9.0 v11 : CUDA Toolkit 9.1 v12 : CUDA Toolkit 10.0, 10.1 and 10.2 v13 : CUDA Toolkit 11.0 v14 : CUDA Toolkit 11.1 v15 : CUDA Toolkit 11.2, 11.3 and 11.4 v16 : CUDA Toolkit 11.5 v17 : CUDA Toolkit 11.6 v18 : CUDA Toolkit 11.8 v19 : CUDA Toolkit 12.0 v20 : CUDA Toolkit 12.2 v21 : CUDA Toolkit 12.3 v22 : CUDA Toolkit 12.4 v23 : CUDA Toolkit 12.5 v24 : CUDA Toolkit 12.6 v26 : CUDA Toolkit 12.8 v27 : CUDA Toolkit 12.9 v28 : CUDA Toolkit 12.9 Update 1

Starting with CUDA Toolkit 13.0, the CUPTI API version uses the format: xxyyzz where:

xx : Major version of the CUDA Toolkit (e.g., 13 for CUDA 13.x)

yy : Minor version of the CUDA Toolkit (e.g., 00 for 13.0, 01 for 13.1)

zz : CUPTI-specific update or patch version (Note: This does NOT necessarily match the CUDA Toolkit update version)


Important:

The CUPTI API version (CUPTI_API_VERSION) is distinct from CUDA_VERSION and CUDA_RUNTIME_VERSION.


v130000 : CUDA Toolkit 13.0 v130001 : CUDA Toolkit 13.0 with CUPTI update 1 v130100 : CUDA Toolkit 13.1 v130101 : CUDA Toolkit 13.1 with CUPTI update 1 v130200 : CUDA Toolkit 13.2 v130201 : CUDA Toolkit 13.2 with CUPTI update 1 v130300 : CUDA Toolkit 13.3 v130301 : CUDA Toolkit 13.3 with CUPTI update 1 v130400 : CUDA Toolkit 13.4 v130401 : CUDA Toolkit 13.4 with CUPTI update 1 v130402 : CUDA Toolkit 13.4 with CUPTI update 2


## 6.13.4. Functions[#](https://docs.nvidia.com#id2)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetVersion(*uint32_t *version*)[#](https://docs.nvidia.com#_CPPv415cuptiGetVersionP8uint32_t) Get the CUPTI API version.

Return the API version in

`*version`

.See also

- Parameters:
**version**– Returns the version- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_INVALID_PARAMETER**– if`version`

is NULL