source: https://docs.nvidia.com/cupti/api/structCUpti__StateData.html

# 7.230. CUpti_StateData[#](https://docs.nvidia.com#cupti-statedata)

-
struct CUpti_StateData
[#](https://docs.nvidia.com#_CPPv415CUpti_StateData) Data passed into a State callback function.

Data passed into a State callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_STATE and callback Ids belonging to CUpti_CallbackIdState. Unless otherwise noted, the callback data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data.Public Members

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)result[#](https://docs.nvidia.com#_CPPv4N15CUpti_StateData6resultE) Error code.


-
const char *message
[#](https://docs.nvidia.com#_CPPv4N15CUpti_StateData7messageE) String containing more details.

It can be NULL.


-
struct
[CUpti_StateData](https://docs.nvidia.com#_CPPv415CUpti_StateData)::[anonymous]::[anonymous] notification[#](https://docs.nvidia.com#_CPPv4N15CUpti_StateData12notificationE) Data passed along with the callback Ids Enum CUpti_CallbackIdState used to denote callback ids.


-