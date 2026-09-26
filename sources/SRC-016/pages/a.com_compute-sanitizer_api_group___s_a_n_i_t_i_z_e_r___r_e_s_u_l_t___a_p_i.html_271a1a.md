source: https://docs.nvidia.com/compute-sanitizer/api/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html

# Sanitizer Result Codes[#](https://docs.nvidia.com#sanitizer-result-codes)

Error and result codes returned by Sanitizer functions.

## Enumerations[#](https://docs.nvidia.com#enumerations)

[SanitizerResult](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i_1ga8edf13e06b1b4001d7577b07ddd575d8)Sanitizer result codes.


## Functions[#](https://docs.nvidia.com#functions)

- SanitizerResult
[sanitizerGetResultString](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i_1ga2be8c36d2401abdfafe8802f71d68223)(SanitizerResult result, const char **str) Get the descriptive string for a SanitizerResult.


## Enumerations[#](https://docs.nvidia.com#id1)

-
enum SanitizerResult
[#](https://docs.nvidia.com#_CPPv415SanitizerResult) Sanitizer result codes.

Error and result codes returned by Sanitizer functions.

*Values:*-
enumerator SANITIZER_SUCCESS
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult17SANITIZER_SUCCESSE) No error.


-
enumerator SANITIZER_ERROR_INVALID_PARAMETER
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult33SANITIZER_ERROR_INVALID_PARAMETERE) One or more of the parameters is invalid.


-
enumerator SANITIZER_ERROR_INVALID_DEVICE
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult30SANITIZER_ERROR_INVALID_DEVICEE) The device does not correspond to a valid CUDA device.


-
enumerator SANITIZER_ERROR_INVALID_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult31SANITIZER_ERROR_INVALID_CONTEXTE) The context is NULL or not valid.


-
enumerator SANITIZER_ERROR_INVALID_DOMAIN_ID
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult33SANITIZER_ERROR_INVALID_DOMAIN_IDE) The domain ID is invalid.


-
enumerator SANITIZER_ERROR_INVALID_CALLBACK_ID
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult35SANITIZER_ERROR_INVALID_CALLBACK_IDE) The callback ID is invalid.


-
enumerator SANITIZER_ERROR_INVALID_OPERATION
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult33SANITIZER_ERROR_INVALID_OPERATIONE) The current operation cannot be performed due to dependency on other factors.


-
enumerator SANITIZER_ERROR_OUT_OF_MEMORY
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult29SANITIZER_ERROR_OUT_OF_MEMORYE) Unable to allocate enough memory to perform the requested operation.


-
enumerator SANITIZER_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult45SANITIZER_ERROR_PARAMETER_SIZE_NOT_SUFFICIENTE) The output buffer size is not sufficient to return all requested data.


-
enumerator SANITIZER_ERROR_API_NOT_IMPLEMENTED
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult35SANITIZER_ERROR_API_NOT_IMPLEMENTEDE) API is not implemented.


-
enumerator SANITIZER_ERROR_MAX_LIMIT_REACHED
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult33SANITIZER_ERROR_MAX_LIMIT_REACHEDE) The maximum limit is reached.


-
enumerator SANITIZER_ERROR_NOT_READY
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult25SANITIZER_ERROR_NOT_READYE) The object is not ready to perform the requested operation.


-
enumerator SANITIZER_ERROR_NOT_COMPATIBLE
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult30SANITIZER_ERROR_NOT_COMPATIBLEE) The current operation is not compatible with the current state of the object.


-
enumerator SANITIZER_ERROR_NOT_INITIALIZED
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult31SANITIZER_ERROR_NOT_INITIALIZEDE) Sanitizer is unable to initialize its connection to the CUDA driver.


-
enumerator SANITIZER_ERROR_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult29SANITIZER_ERROR_NOT_SUPPORTEDE) The attempted operation is not supported on the current system or device.


-
enumerator SANITIZER_ERROR_ADDRESS_NOT_IN_DEVICE_MEMORY
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult44SANITIZER_ERROR_ADDRESS_NOT_IN_DEVICE_MEMORYE) The attempted device operation has a parameter not in device memory.


-
enumerator SANITIZER_ERROR_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult23SANITIZER_ERROR_UNKNOWNE) An unknown internal error has occurred.


-
enumerator SANITIZER_ERROR_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N15SanitizerResult25SANITIZER_ERROR_FORCE_INTE)

-
enumerator SANITIZER_SUCCESS

## Functions[#](https://docs.nvidia.com#id2)

-
[SanitizerResult](https://docs.nvidia.com#_CPPv415SanitizerResult)sanitizerGetResultString( ,[SanitizerResult](https://docs.nvidia.com#_CPPv415SanitizerResult)result*const char **str*,Get the descriptive string for a SanitizerResult.

Return the descriptive string for a SanitizerResult in

`*str`

.Note

**Thread-safety**: this function is thread-safe.- Parameters:
**result**– The result to get the string for.**str**– Returns the string.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`str`

is NULL or`result`

is not a valid SanitizerResult.



[#](https://docs.nvidia.com#_CPPv424sanitizerGetResultString15SanitizerResultPPKc)