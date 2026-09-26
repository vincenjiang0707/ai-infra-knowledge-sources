source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__prepostprocess__c__api.html
lastmod: 

# Group Pre Post Process[#](https://docs.openvino.ai#group-pre-post-process)

-
*group*Pre Post Process The definitions & operations about prepostprocess.

Enums

-
enum ov_color_format_e
[#](https://docs.openvino.ai#_CPPv417ov_color_format_e) This enum contains enumerations for color format.

*Values:*-
enumerator UNDEFINE
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e8UNDEFINEE) Undefine color format.


-
enumerator NV12_SINGLE_PLANE
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e17NV12_SINGLE_PLANEE) Image in NV12 format as single tensor.


-
enumerator NV12_TWO_PLANES
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e15NV12_TWO_PLANESE) Image in NV12 format represented as separate tensors for Y and UV planes.


-
enumerator I420_SINGLE_PLANE
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e17I420_SINGLE_PLANEE) Image in I420 (YUV) format as single tensor.


-
enumerator I420_THREE_PLANES
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e17I420_THREE_PLANESE) Image in I420 format represented as separate tensors for Y, U and V planes.


-
enumerator RGB
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e3RGBE) Image in RGB interleaved format (3 channels)


-
enumerator BGR
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e3BGRE) Image in BGR interleaved format (3 channels)


-
enumerator GRAY
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e4GRAYE) Image in GRAY format (1 channel)


-
enumerator RGBX
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e4RGBXE) Image in RGBX interleaved format (4 channels)


-
enumerator BGRX
[#](https://docs.openvino.ai#_CPPv4N17ov_color_format_e4BGRXE) Image in BGRX interleaved format (4 channels)


-
enumerator UNDEFINE

-
enum ov_preprocess_resize_algorithm_e
[#](https://docs.openvino.ai#_CPPv432ov_preprocess_resize_algorithm_e) This enum contains codes for all preprocess resize algorithm.

*Values:*-
enumerator RESIZE_LINEAR
[#](https://docs.openvino.ai#_CPPv4N32ov_preprocess_resize_algorithm_e13RESIZE_LINEARE) linear algorithm


-
enumerator RESIZE_CUBIC
[#](https://docs.openvino.ai#_CPPv4N32ov_preprocess_resize_algorithm_e12RESIZE_CUBICE) cubic algorithm


-
enumerator RESIZE_NEAREST
[#](https://docs.openvino.ai#_CPPv4N32ov_preprocess_resize_algorithm_e14RESIZE_NEARESTE) nearest algorithm


-
enumerator RESIZE_LINEAR

-
enum ov_padding_mode_e
[#](https://docs.openvino.ai#_CPPv417ov_padding_mode_e) This enum contains enumeration for padding mode.

*Values:*-
enumerator CONSTANT
[#](https://docs.openvino.ai#_CPPv4N17ov_padding_mode_e8CONSTANTE) Pads with given constant value.


-
enumerator EDGE
[#](https://docs.openvino.ai#_CPPv4N17ov_padding_mode_e4EDGEE) Pads with tensor edge values.


-
enumerator REFLECT
[#](https://docs.openvino.ai#_CPPv4N17ov_padding_mode_e7REFLECTE) Pads with reflection of tensor data along axis. Values on the edges are not duplicated.


-
enumerator SYMMETRIC
[#](https://docs.openvino.ai#_CPPv4N17ov_padding_mode_e9SYMMETRICE) Pads similar like

`REFLECT`

but values on the edges are duplicated.

-
enumerator CONSTANT

Functions

-
ov_preprocess_prepostprocessor_create(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model,[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)**preprocess)[#](https://docs.openvino.ai#_CPPv437ov_preprocess_prepostprocessor_createPK10ov_model_tPP32ov_preprocess_prepostprocessor_t) Create a

[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t)instance.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai/group__ov__model__c__api.html#structov__model__t).**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_free(
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess)[#](https://docs.openvino.ai#_CPPv435ov_preprocess_prepostprocessor_freeP32ov_preprocess_prepostprocessor_t) Release the memory allocated by

[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t)to free memory.


-
ov_preprocess_prepostprocessor_get_input_info(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess,[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)**preprocess_input_info)[#](https://docs.openvino.ai#_CPPv445ov_preprocess_prepostprocessor_get_input_infoPK32ov_preprocess_prepostprocessor_tPP26ov_preprocess_input_info_t) Get the input info of

[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t)instance.- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**preprocess_input_info**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_get_input_info_by_name(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess, const char *tensor_name,[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)**preprocess_input_info)[#](https://docs.openvino.ai#_CPPv453ov_preprocess_prepostprocessor_get_input_info_by_namePK32ov_preprocess_prepostprocessor_tPKcPP26ov_preprocess_input_info_t) Get the input info of

[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t)instance by tensor name.- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**tensor_name**– The name of input.**preprocess_input_info**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_get_input_info_by_index(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess, const size_t tensor_index,[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)**preprocess_input_info)[#](https://docs.openvino.ai#_CPPv454ov_preprocess_prepostprocessor_get_input_info_by_indexPK32ov_preprocess_prepostprocessor_tK6size_tPP26ov_preprocess_input_info_t) Get the input info of

[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t)instance by tensor order.- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**tensor_index**– The order of input.**preprocess_input_info**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_info_free(
[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)*preprocess_input_info)[#](https://docs.openvino.ai#_CPPv429ov_preprocess_input_info_freeP26ov_preprocess_input_info_t) Release the memory allocated by

[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).- Parameters:
**preprocess_input_info**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t)to free memory.


-
ov_preprocess_input_info_get_tensor_info(const
[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)*preprocess_input_info,[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)**preprocess_input_tensor_info)[#](https://docs.openvino.ai#_CPPv440ov_preprocess_input_info_get_tensor_infoPK26ov_preprocess_input_info_tPP33ov_preprocess_input_tensor_info_t) Get a

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).- Parameters:
**preprocess_input_info**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).**preprocess_input_tensor_info**– A pointer to[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_free(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info)[#](https://docs.openvino.ai#_CPPv436ov_preprocess_input_tensor_info_freeP33ov_preprocess_input_tensor_info_t) Release the memory allocated by

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)to free memory.


-
ov_preprocess_input_info_get_preprocess_steps(const
[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)*preprocess_input_info,[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)**preprocess_input_steps)[#](https://docs.openvino.ai#_CPPv445ov_preprocess_input_info_get_preprocess_stepsPK26ov_preprocess_input_info_tPP32ov_preprocess_preprocess_steps_t) Get a

[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).- Parameters:
**ov_preprocess_input_info_t**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).**preprocess_input_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_free(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps)[#](https://docs.openvino.ai#_CPPv435ov_preprocess_preprocess_steps_freeP32ov_preprocess_preprocess_steps_t) Release the memory allocated by

[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).- Parameters:
**preprocess_input_steps**– A pointer to the[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t)to free memory.


-
ov_preprocess_preprocess_steps_resize(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, const[ov_preprocess_resize_algorithm_e](https://docs.openvino.ai#_CPPv432ov_preprocess_resize_algorithm_e)resize_algorithm)[#](https://docs.openvino.ai#_CPPv437ov_preprocess_preprocess_steps_resizeP32ov_preprocess_preprocess_steps_tK32ov_preprocess_resize_algorithm_e) Add resize operation to model’s dimensions.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**resize_algorithm**– A ov_preprocess_resizeAlgorithm instance

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_scale(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, float value)[#](https://docs.openvino.ai#_CPPv436ov_preprocess_preprocess_steps_scaleP32ov_preprocess_preprocess_steps_tf) Add scale preprocess operation. Divide each element of input by specified value.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**value**– Scaling value

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_scale_multi_channels(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, const float *values, const int32_t value_size)[#](https://docs.openvino.ai#_CPPv451ov_preprocess_preprocess_steps_scale_multi_channelsP32ov_preprocess_preprocess_steps_tPKfK7int32_t) Add scale preprocess operation. Divide each channel element of input by different specified value.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**values**– Scaling values array for each channels**value_size**– Scaling value size

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_mean(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, float value)[#](https://docs.openvino.ai#_CPPv435ov_preprocess_preprocess_steps_meanP32ov_preprocess_preprocess_steps_tf) Add mean preprocess operation. Subtract specified value from each element of input.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**value**– Value to subtract from each element.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_mean_multi_channels(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, const float *values, const int32_t value_size)[#](https://docs.openvino.ai#_CPPv450ov_preprocess_preprocess_steps_mean_multi_channelsP32ov_preprocess_preprocess_steps_tPKfK7int32_t) Add mean preprocess operation. Subtract each channel element of input by different specified value.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**values**– Value array to subtract from each element.**value_size**– Mean value size

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_crop(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, int32_t *begin, int32_t begin_size, int32_t *end, int32_t end_size)[#](https://docs.openvino.ai#_CPPv435ov_preprocess_preprocess_steps_cropP32ov_preprocess_preprocess_steps_tP7int32_t7int32_tP7int32_t7int32_t) Crop input tensor between begin and end coordinates.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**begin**– Pointer to begin indexes for input tensor cropping. Negative values represent counting elements from the end of input tensor**begin_size**– The size of begin array**end**– Pointer to end indexes for input tensor cropping. End indexes are exclusive, which means values including end edge are not included in the output slice. Negative values represent counting elements from the end of input tensor**end_size**– The size of end array

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_convert_layout(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps,[ov_layout_t](https://docs.openvino.ai/structov__layout__t.html#_CPPv411ov_layout_t)*layout)[#](https://docs.openvino.ai#_CPPv445ov_preprocess_preprocess_steps_convert_layoutP32ov_preprocess_preprocess_steps_tP11ov_layout_t) Add ‘convert layout’ operation to specified layout.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**layout**– A point to[ov_layout_t](https://docs.openvino.ai/group__ov__layout__c__api.html#structov__layout__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_reverse_channels(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps)[#](https://docs.openvino.ai#_CPPv447ov_preprocess_preprocess_steps_reverse_channelsP32ov_preprocess_preprocess_steps_t) Reverse channels operation.

- Parameters:
**preprocess_input_process_steps**– A pointer to[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_set_element_type(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info, const[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)element_type)[#](https://docs.openvino.ai#_CPPv448ov_preprocess_input_tensor_info_set_element_typeP33ov_preprocess_input_tensor_info_tK17ov_element_type_e) Set

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)precesion.- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).**element_type**– A point to element_type

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_set_color_format(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info, const[ov_color_format_e](https://docs.openvino.ai#_CPPv417ov_color_format_e)colorFormat)[#](https://docs.openvino.ai#_CPPv448ov_preprocess_input_tensor_info_set_color_formatP33ov_preprocess_input_tensor_info_tK17ov_color_format_e) Set

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)color format.- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).**colorFormat**– The enumerate of colorFormat

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_set_color_format_with_subname(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info, const[ov_color_format_e](https://docs.openvino.ai#_CPPv417ov_color_format_e)colorFormat, const size_t sub_names_size, ...)[#](https://docs.openvino.ai#_CPPv461ov_preprocess_input_tensor_info_set_color_format_with_subnameP33ov_preprocess_input_tensor_info_tK17ov_color_format_eK6size_tz) Set

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)color format with subname.- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).**colorFormat**– The enumerate of colorFormat**sub_names_size**– The size of sub_names**...**– variadic params sub_names Optional list of sub-names assigned for each plane (e.g. “Y”, “UV”).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_set_spatial_static_shape(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info, const size_t input_height, const size_t input_width)[#](https://docs.openvino.ai#_CPPv456ov_preprocess_input_tensor_info_set_spatial_static_shapeP33ov_preprocess_input_tensor_info_tK6size_tK6size_t) Set

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)spatial_static_shape.- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).**input_height**– The height of input**input_width**– The width of input

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_convert_element_type(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, const[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)element_type)[#](https://docs.openvino.ai#_CPPv451ov_preprocess_preprocess_steps_convert_element_typeP32ov_preprocess_preprocess_steps_tK17ov_element_type_e) Convert

[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t)element type.- Parameters:
**preprocess_input_steps**– A pointer to the[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**element_type**– preprocess input element type.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_preprocess_steps_convert_color(
[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai/structov__preprocess__preprocess__steps__t.html#_CPPv432ov_preprocess_preprocess_steps_t)*preprocess_input_process_steps, const[ov_color_format_e](https://docs.openvino.ai#_CPPv417ov_color_format_e)colorFormat)[#](https://docs.openvino.ai#_CPPv444ov_preprocess_preprocess_steps_convert_colorP32ov_preprocess_preprocess_steps_tK17ov_color_format_e) Convert

[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t)color.- Parameters:
**preprocess_input_steps**– A pointer to the[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t).**colorFormat**– The enumerate of colorFormat.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_set_from(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv440ov_preprocess_input_tensor_info_set_fromP33ov_preprocess_input_tensor_info_tPK11ov_tensor_t) Helper function to reuse element type and shape from user’s created tensor.

- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai/group__ov__tensor__c__api.html#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_tensor_info_set_layout(
[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai/structov__preprocess__input__tensor__info__t.html#_CPPv433ov_preprocess_input_tensor_info_t)*preprocess_input_tensor_info,[ov_layout_t](https://docs.openvino.ai/structov__layout__t.html#_CPPv411ov_layout_t)*layout)[#](https://docs.openvino.ai#_CPPv442ov_preprocess_input_tensor_info_set_layoutP33ov_preprocess_input_tensor_info_tP11ov_layout_t) Set

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)layout.- Parameters:
**preprocess_input_tensor_info**– A pointer to the[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).**layout**– A point to[ov_layout_t](https://docs.openvino.ai/group__ov__layout__c__api.html#structov__layout__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_get_output_info(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess,[ov_preprocess_output_info_t](https://docs.openvino.ai/structov__preprocess__output__info__t.html#_CPPv427ov_preprocess_output_info_t)**preprocess_output_info)[#](https://docs.openvino.ai#_CPPv446ov_preprocess_prepostprocessor_get_output_infoPK32ov_preprocess_prepostprocessor_tPP27ov_preprocess_output_info_t) Get the output info of

[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t)instance.- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**preprocess_output_info**– A pointer to the[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_get_output_info_by_index(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess, const size_t tensor_index,[ov_preprocess_output_info_t](https://docs.openvino.ai/structov__preprocess__output__info__t.html#_CPPv427ov_preprocess_output_info_t)**preprocess_output_info)[#](https://docs.openvino.ai#_CPPv455ov_preprocess_prepostprocessor_get_output_info_by_indexPK32ov_preprocess_prepostprocessor_tK6size_tPP27ov_preprocess_output_info_t) Get the output info of

[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t)instance.- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**tensor_index**– The tensor index**preprocess_output_info**– A pointer to the[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_get_output_info_by_name(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess, const char *tensor_name,[ov_preprocess_output_info_t](https://docs.openvino.ai/structov__preprocess__output__info__t.html#_CPPv427ov_preprocess_output_info_t)**preprocess_output_info)[#](https://docs.openvino.ai#_CPPv454ov_preprocess_prepostprocessor_get_output_info_by_namePK32ov_preprocess_prepostprocessor_tPKcPP27ov_preprocess_output_info_t) Get the output info of

[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t)instance.- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**tensor_name**– The name of input.**preprocess_output_info**– A pointer to the[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_output_info_free(
[ov_preprocess_output_info_t](https://docs.openvino.ai/structov__preprocess__output__info__t.html#_CPPv427ov_preprocess_output_info_t)*preprocess_output_info)[#](https://docs.openvino.ai#_CPPv430ov_preprocess_output_info_freeP27ov_preprocess_output_info_t) Release the memory allocated by

[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t).- Parameters:
**preprocess_output_info**– A pointer to the[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t)to free memory.


-
ov_preprocess_output_info_get_tensor_info(const
[ov_preprocess_output_info_t](https://docs.openvino.ai/structov__preprocess__output__info__t.html#_CPPv427ov_preprocess_output_info_t)*preprocess_output_info,[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai/structov__preprocess__output__tensor__info__t.html#_CPPv434ov_preprocess_output_tensor_info_t)**preprocess_output_tensor_info)[#](https://docs.openvino.ai#_CPPv441ov_preprocess_output_info_get_tensor_infoPK27ov_preprocess_output_info_tPP34ov_preprocess_output_tensor_info_t) Get a

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t).- Parameters:
**preprocess_output_info**– A pointer to the[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t).**preprocess_output_tensor_info**– A pointer to the[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai#structov__preprocess__output__tensor__info__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_output_tensor_info_free(
[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai/structov__preprocess__output__tensor__info__t.html#_CPPv434ov_preprocess_output_tensor_info_t)*preprocess_output_tensor_info)[#](https://docs.openvino.ai#_CPPv437ov_preprocess_output_tensor_info_freeP34ov_preprocess_output_tensor_info_t) Release the memory allocated by

[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai#structov__preprocess__output__tensor__info__t).- Parameters:
**preprocess_output_tensor_info**– A pointer to the[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai#structov__preprocess__output__tensor__info__t)to free memory.


-
ov_preprocess_output_set_element_type(
[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai/structov__preprocess__output__tensor__info__t.html#_CPPv434ov_preprocess_output_tensor_info_t)*preprocess_output_tensor_info, const[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)element_type)[#](https://docs.openvino.ai#_CPPv437ov_preprocess_output_set_element_typeP34ov_preprocess_output_tensor_info_tK17ov_element_type_e) Set

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)precesion.- Parameters:
**preprocess_output_tensor_info**– A pointer to the[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai#structov__preprocess__output__tensor__info__t).**element_type**– A point to element_type

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_info_get_model_info(const
[ov_preprocess_input_info_t](https://docs.openvino.ai/structov__preprocess__input__info__t.html#_CPPv426ov_preprocess_input_info_t)*preprocess_input_info,[ov_preprocess_input_model_info_t](https://docs.openvino.ai/structov__preprocess__input__model__info__t.html#_CPPv432ov_preprocess_input_model_info_t)**preprocess_input_model_info)[#](https://docs.openvino.ai#_CPPv439ov_preprocess_input_info_get_model_infoPK26ov_preprocess_input_info_tPP32ov_preprocess_input_model_info_t) Get current input model information.

- Parameters:
**preprocess_input_info**– A pointer to the[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t).**preprocess_input_model_info**– A pointer to the[ov_preprocess_input_model_info_t](https://docs.openvino.ai#structov__preprocess__input__model__info__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_input_model_info_free(
[ov_preprocess_input_model_info_t](https://docs.openvino.ai/structov__preprocess__input__model__info__t.html#_CPPv432ov_preprocess_input_model_info_t)*preprocess_input_model_info)[#](https://docs.openvino.ai#_CPPv435ov_preprocess_input_model_info_freeP32ov_preprocess_input_model_info_t) Release the memory allocated by

[ov_preprocess_input_model_info_t](https://docs.openvino.ai#structov__preprocess__input__model__info__t).- Parameters:
**preprocess_input_model_info**– A pointer to the[ov_preprocess_input_model_info_t](https://docs.openvino.ai#structov__preprocess__input__model__info__t)to free memory.


-
ov_preprocess_input_model_info_set_layout(
[ov_preprocess_input_model_info_t](https://docs.openvino.ai/structov__preprocess__input__model__info__t.html#_CPPv432ov_preprocess_input_model_info_t)*preprocess_input_model_info,[ov_layout_t](https://docs.openvino.ai/structov__layout__t.html#_CPPv411ov_layout_t)*layout)[#](https://docs.openvino.ai#_CPPv441ov_preprocess_input_model_info_set_layoutP32ov_preprocess_input_model_info_tP11ov_layout_t) Set layout for model’s input tensor.

- Parameters:
**preprocess_input_model_info**– A pointer to the[ov_preprocess_input_model_info_t](https://docs.openvino.ai#structov__preprocess__input__model__info__t)**layout**– A point to[ov_layout_t](https://docs.openvino.ai/group__ov__layout__c__api.html#structov__layout__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_preprocess_prepostprocessor_build(const
[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai/structov__preprocess__prepostprocessor__t.html#_CPPv432ov_preprocess_prepostprocessor_t)*preprocess,[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)**model)[#](https://docs.openvino.ai#_CPPv436ov_preprocess_prepostprocessor_buildPK32ov_preprocess_prepostprocessor_tPP10ov_model_t) Adds pre/post-processing operations to function passed in constructor.

- Parameters:
**preprocess**– A pointer to the[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t).**model**– A pointer to the[ov_model_t](https://docs.openvino.ai/group__ov__model__c__api.html#structov__model__t).

- Returns:
Status code of the operation: OK(0) for success.



-
struct ov_preprocess_prepostprocessor_t
[#](https://docs.openvino.ai#_CPPv432ov_preprocess_prepostprocessor_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_prepostprocessor_t](https://docs.openvino.ai#structov__preprocess__prepostprocessor__t)from ov_preprocess_prepostprocessor

-
struct ov_preprocess_input_info_t
[#](https://docs.openvino.ai#_CPPv426ov_preprocess_input_info_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_input_info_t](https://docs.openvino.ai#structov__preprocess__input__info__t)from ov_preprocess_input_info

-
struct ov_preprocess_input_tensor_info_t
[#](https://docs.openvino.ai#_CPPv433ov_preprocess_input_tensor_info_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_input_tensor_info_t](https://docs.openvino.ai#structov__preprocess__input__tensor__info__t)from ov_preprocess_input_tensor_info

-
struct ov_preprocess_output_info_t
[#](https://docs.openvino.ai#_CPPv427ov_preprocess_output_info_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_output_info_t](https://docs.openvino.ai#structov__preprocess__output__info__t)from ov_preprocess_output_info

-
struct ov_preprocess_output_tensor_info_t
[#](https://docs.openvino.ai#_CPPv434ov_preprocess_output_tensor_info_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_output_tensor_info_t](https://docs.openvino.ai#structov__preprocess__output__tensor__info__t)from ov_preprocess_output_tensor_info

-
struct ov_preprocess_input_model_info_t
[#](https://docs.openvino.ai#_CPPv432ov_preprocess_input_model_info_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_input_model_info_t](https://docs.openvino.ai#structov__preprocess__input__model__info__t)from ov_preprocess_input_model_info

-
struct ov_preprocess_preprocess_steps_t
[#](https://docs.openvino.ai#_CPPv432ov_preprocess_preprocess_steps_t) *#include <ov_prepostprocess.h>*type define

[ov_preprocess_preprocess_steps_t](https://docs.openvino.ai#structov__preprocess__preprocess__steps__t)from ov_preprocess_preprocess_steps

-
enum ov_color_format_e