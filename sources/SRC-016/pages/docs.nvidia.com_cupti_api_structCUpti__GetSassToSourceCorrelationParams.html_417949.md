source: https://docs.nvidia.com/cupti/api/structCUpti__GetSassToSourceCorrelationParams.html

# 7.138. CUpti_GetSassToSourceCorrelationParams[#](https://docs.nvidia.com#cupti-getsasstosourcecorrelationparams)

-
struct CUpti_GetSassToSourceCorrelationParams
[#](https://docs.nvidia.com#_CPPv438CUpti_GetSassToSourceCorrelationParams) Params for cuptiGetSassToSourceCorrelation.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams4sizeE) [w] Size of the data structure i.e.

CUpti_GetSassToSourceCorrelationParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
const void *cubin
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams5cubinE) [w] Pointer to cubin binary where function belongs.


-
const char *functionName
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams12functionNameE) [w] Function name to which PC belongs.


-
size_t cubinSize
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams9cubinSizeE) [w] Size of cubin binary.


-
uint32_t lineNumber
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams10lineNumberE) [r] Line number in the source code.


-
uint64_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams8pcOffsetE) [w] PC offset


-
char *fileName
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams8fileNameE) [r] Path for the source file.


-
char *dirName
[#](https://docs.nvidia.com#_CPPv4N38CUpti_GetSassToSourceCorrelationParams7dirNameE) [r] Path for the directory of source file.


-
size_t size