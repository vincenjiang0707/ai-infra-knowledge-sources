source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___event_data.html

# Sanitizer_EventData[#](https://docs.nvidia.com#sanitizer-eventdata)

-
struct Sanitizer_EventData
[#](https://docs.nvidia.com#_CPPv419Sanitizer_EventData) Data passed into an event callback function.

Data passed into an event callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal tp SANITIZER_CB_DOMAIN_EVENTS. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_EventData7contextE) For SANITIZER_CBID_EVENTS_CREATED, SANITIZER_CBID_EVENTS_DESTROYED, SANITIZER_CBID_EVENTS_SYNCHNONIZED, SANITIZER_CBID_CTX_RECORD_EVENT, SANITIZER_CBID_CTX_WAIT_EVENT this is the context containing the event.

For SANITIZER_CBID_GREEN_CTX_RECORD_EVENT, SANITIZER_CBID_GREEN_CTX_WAIT_EVENT this is the parent context for green context containing the event. For SANITIZER_CBID_EVENTS_RECORD and SANITIZER_CBID_EVENTS_STREAM_WAIT, this is the context containing the stream being recorded or waiting.


-
CUevent event
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_EventData5eventE) The event recording or being waited.


-
CUgreenCtx greenCtx
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_EventData8greenCtxE) For SANITIZER_CBID_GREEN_CTX_RECORD_EVENT, SANITIZER_CBID_GREEN_CTX_WAIT_EVENT this is the green context containing the event.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_EventData7hStreamE) Unique handle for the stream.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_EventData6streamE) The stream being recorded or waiting.

Available if cbid is SANITIZER_CBID_EVENTS_RECORD or SANITIZER_CBID_EVENTS_STREAM_WAIT.


-
CUcontext context