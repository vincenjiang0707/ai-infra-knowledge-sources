source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__base__c__api.html
lastmod: 

# Group Basics[#](https://docs.openvino.ai#group-basics)

-
*group*Basics The basic definitions & interfaces of OpenVINO C API to work with other components.

Enums

-
enum ov_status_e
[#](https://docs.openvino.ai#_CPPv411ov_status_e) This enum contains codes for all possible return values of the interface functions.

*Values:*-
enumerator OK
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e2OKE) SUCCESS.


-
enumerator GENERAL_ERROR
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e13GENERAL_ERRORE) GENERAL_ERROR.


-
enumerator NOT_IMPLEMENTED
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e15NOT_IMPLEMENTEDE) NOT_IMPLEMENTED.


-
enumerator NETWORK_NOT_LOADED
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e18NETWORK_NOT_LOADEDE) NETWORK_NOT_LOADED.


-
enumerator PARAMETER_MISMATCH
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e18PARAMETER_MISMATCHE) PARAMETER_MISMATCH.


-
enumerator NOT_FOUND
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e9NOT_FOUNDE) NOT_FOUND.


-
enumerator OUT_OF_BOUNDS
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e13OUT_OF_BOUNDSE) OUT_OF_BOUNDS.


-
enumerator UNEXPECTED
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e10UNEXPECTEDE) UNEXPECTED.


-
enumerator REQUEST_BUSY
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e12REQUEST_BUSYE) REQUEST_BUSY.


-
enumerator RESULT_NOT_READY
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e16RESULT_NOT_READYE) RESULT_NOT_READY.


-
enumerator NOT_ALLOCATED
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e13NOT_ALLOCATEDE) NOT_ALLOCATED.


-
enumerator INFER_NOT_STARTED
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e17INFER_NOT_STARTEDE) INFER_NOT_STARTED.


-
enumerator NETWORK_NOT_READ
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e16NETWORK_NOT_READE) NETWORK_NOT_READ.


-
enumerator INFER_CANCELLED
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e15INFER_CANCELLEDE) INFER_CANCELLED.


-
enumerator INVALID_C_PARAM
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e15INVALID_C_PARAME) INVALID_C_PARAM.


-
enumerator UNKNOWN_C_ERROR
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e15UNKNOWN_C_ERRORE) UNKNOWN_C_ERROR.


-
enumerator NOT_IMPLEMENT_C_METHOD
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e22NOT_IMPLEMENT_C_METHODE) NOT_IMPLEMENT_C_METHOD.


-
enumerator UNKNOW_EXCEPTION
[#](https://docs.openvino.ai#_CPPv4N11ov_status_e16UNKNOW_EXCEPTIONE) UNKNOW_EXCEPTION.


-
enumerator OK

-
enum ov_element_type_e
[#](https://docs.openvino.ai#_CPPv417ov_element_type_e) This enum contains codes for element type, which is aligned with

[ov::element::Type_t](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1gac13a83fdcf171bd2c98577bfcd37f2f1)in src/core/include/openvino/core/type/element_type.hpp.*Values:*-
enumerator UNDEFINED
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e9UNDEFINEDE) Undefined element type.


-
enumerator DYNAMIC
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e7DYNAMICE) Dynamic element type.


-
enumerator BOOLEAN
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e7BOOLEANE) boolean element type


-
enumerator BF16
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e4BF16E) bf16 element type


-
enumerator F16
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3F16E) f16 element type


-
enumerator F32
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3F32E) f32 element type


-
enumerator F64
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3F64E) f64 element type


-
enumerator I4
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2I4E) i4 element type


-
enumerator I8
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2I8E) i8 element type


-
enumerator I16
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3I16E) i16 element type


-
enumerator I32
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3I32E) i32 element type


-
enumerator I64
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3I64E) i64 element type


-
enumerator U1
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2U1E) binary element type


-
enumerator U2
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2U2E) u2 element type


-
enumerator U3
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2U3E) u3 element type


-
enumerator U4
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2U4E) u4 element type


-
enumerator U6
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2U6E) u6 element type


-
enumerator U8
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e2U8E) u8 element type


-
enumerator U16
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3U16E) u16 element type


-
enumerator U32
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3U32E) u32 element type


-
enumerator U64
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3U64E) u64 element type


-
enumerator NF4
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e3NF4E) nf4 element type


-
enumerator F8E4M3
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e6F8E4M3E) f8e4m3 element type


-
enumerator F8E5M3
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e6F8E5M3E) f8e5m2 element type


-
enumerator STRING
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e6STRINGE) string element type


-
enumerator F4E2M1
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e6F4E2M1E) f4e2m1 element type


-
enumerator F8E8M0
[#](https://docs.openvino.ai#_CPPv4N17ov_element_type_e6F8E8M0E) f8e8m0 element type


-
enumerator UNDEFINED

Functions

-
const char *ov_get_error_info(
[ov_status_e](https://docs.openvino.ai#_CPPv411ov_status_e)status)[#](https://docs.openvino.ai#_CPPv417ov_get_error_info11ov_status_e) Print the error info.

- Parameters:
**ov_status_e**– a status code.


-
void ov_free(const char *content)
[#](https://docs.openvino.ai#_CPPv47ov_freePKc) free char

- Parameters:
**content**– The pointer to the char to free.


-
const char *ov_get_last_err_msg()
[#](https://docs.openvino.ai#_CPPv419ov_get_last_err_msgv) Get the last error msg.


-
enum ov_status_e