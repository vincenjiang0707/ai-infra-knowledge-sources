source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__c__api.html
lastmod: 

# Group OpenVINO Runtime C API[#](https://docs.openvino.ai#group-openvino-runtime-c-api)

[Basics](https://docs.openvino.ai/group__ov__base__c__api.html)[Compiled Model](https://docs.openvino.ai/group__ov__compiled__model__c__api.html)`ov_compiled_model_inputs_size()`

`ov_compiled_model_input()`

`ov_compiled_model_input_by_index()`

`ov_compiled_model_input_by_name()`

`ov_compiled_model_outputs_size()`

`ov_compiled_model_output()`

`ov_compiled_model_output_by_index()`

`ov_compiled_model_output_by_name()`

`ov_compiled_model_get_runtime_model()`

`ov_compiled_model_create_infer_request()`

`ov_compiled_model_set_property()`

`ov_compiled_model_get_property()`

`ov_compiled_model_export_model()`

`ov_compiled_model_free()`

`ov_compiled_model_get_context()`

`ov_compiled_model_t`


[Core](https://docs.openvino.ai/group__ov__core__c__api.html)`ov_get_openvino_version()`

`ov_version_free()`

`ov_core_create()`

`ov_core_create_with_config()`

`ov_core_free()`

`ov_core_read_model()`

`ov_core_compile_model()`

`ov_core_compile_model_from_file()`

`ov_core_add_extension()`

`ov_core_set_property()`

`ov_core_get_property()`

`ov_core_get_available_devices()`

`ov_available_devices_free()`

`ov_core_import_model()`

`ov_core_versions_free()`

`ov_core_create_context()`

`ov_core_compile_model_with_context()`

`ov_core_get_default_context()`

`ov_core_t`

`ov_version`

`ov_core_version`

`ov_core_version_list`

`ov_available_devices_t`


[Dimension](https://docs.openvino.ai/group__ov__dimension__c__api.html)[Infer Request](https://docs.openvino.ai/group__ov__infer__request__c__api.html)`ov_infer_request_set_tensor()`

`ov_infer_request_set_tensor_by_port()`

`ov_infer_request_set_tensor_by_const_port()`

`ov_infer_request_set_input_tensor_by_index()`

`ov_infer_request_set_input_tensor()`

`ov_infer_request_set_output_tensor_by_index()`

`ov_infer_request_set_output_tensor()`

`ov_infer_request_get_tensor()`

`ov_infer_request_get_tensor_by_const_port()`

`ov_infer_request_get_tensor_by_port()`

`ov_infer_request_get_input_tensor_by_index()`

`ov_infer_request_get_input_tensor()`

`ov_infer_request_get_output_tensor_by_index()`

`ov_infer_request_get_output_tensor()`

`ov_infer_request_infer()`

`ov_infer_request_cancel()`

`ov_infer_request_start_async()`

`ov_infer_request_wait()`

`ov_infer_request_wait_for()`

`ov_infer_request_set_callback()`

`ov_infer_request_free()`

`ov_infer_request_get_profiling_info()`

`ov_profiling_info_list_free()`

`ov_infer_request_t`

`ov_callback_t`

`ov_ProfilingInfo_t`

`ov_profiling_info_list_t`


[Layout](https://docs.openvino.ai/group__ov__layout__c__api.html)[Model](https://docs.openvino.ai/group__ov__model__c__api.html)`ov_model_free()`

`ov_model_const_input()`

`ov_model_const_input_by_name()`

`ov_model_const_input_by_index()`

`ov_model_input()`

`ov_model_input_by_name()`

`ov_model_input_by_index()`

`ov_model_const_output()`

`ov_model_const_output_by_index()`

`ov_model_const_output_by_name()`

`ov_model_output()`

`ov_model_output_by_index()`

`ov_model_output_by_name()`

`ov_model_inputs_size()`

`ov_model_outputs_size()`

`ov_model_reshape()`

`ov_model_reshape_input_by_name()`

`ov_model_reshape_single_input()`

`ov_model_reshape_by_port_indexes()`

`ov_model_reshape_by_ports()`

`ov_model_get_friendly_name()`

`ov_model_t`


[Node](https://docs.openvino.ai/group__ov__node__c__api.html)[Partial Shape](https://docs.openvino.ai/group__ov__partial__shape__c__api.html)[Pre Post Process](https://docs.openvino.ai/group__ov__prepostprocess__c__api.html)`ov_color_format_e`

`ov_preprocess_resize_algorithm_e`

`ov_padding_mode_e`

`ov_preprocess_prepostprocessor_create()`

`ov_preprocess_prepostprocessor_free()`

`ov_preprocess_prepostprocessor_get_input_info()`

`ov_preprocess_prepostprocessor_get_input_info_by_name()`

`ov_preprocess_prepostprocessor_get_input_info_by_index()`

`ov_preprocess_input_info_free()`

`ov_preprocess_input_info_get_tensor_info()`

`ov_preprocess_input_tensor_info_free()`

`ov_preprocess_input_info_get_preprocess_steps()`

`ov_preprocess_preprocess_steps_free()`

`ov_preprocess_preprocess_steps_resize()`

`ov_preprocess_preprocess_steps_scale()`

`ov_preprocess_preprocess_steps_scale_multi_channels()`

`ov_preprocess_preprocess_steps_mean()`

`ov_preprocess_preprocess_steps_mean_multi_channels()`

`ov_preprocess_preprocess_steps_crop()`

`ov_preprocess_preprocess_steps_convert_layout()`

`ov_preprocess_preprocess_steps_reverse_channels()`

`ov_preprocess_input_tensor_info_set_element_type()`

`ov_preprocess_input_tensor_info_set_color_format()`

`ov_preprocess_input_tensor_info_set_color_format_with_subname()`

`ov_preprocess_input_tensor_info_set_spatial_static_shape()`

`ov_preprocess_preprocess_steps_convert_element_type()`

`ov_preprocess_preprocess_steps_convert_color()`

`ov_preprocess_input_tensor_info_set_from()`

`ov_preprocess_input_tensor_info_set_layout()`

`ov_preprocess_prepostprocessor_get_output_info()`

`ov_preprocess_prepostprocessor_get_output_info_by_index()`

`ov_preprocess_prepostprocessor_get_output_info_by_name()`

`ov_preprocess_output_info_free()`

`ov_preprocess_output_info_get_tensor_info()`

`ov_preprocess_output_tensor_info_free()`

`ov_preprocess_output_set_element_type()`

`ov_preprocess_input_info_get_model_info()`

`ov_preprocess_input_model_info_free()`

`ov_preprocess_input_model_info_set_layout()`

`ov_preprocess_prepostprocessor_build()`

`ov_preprocess_prepostprocessor_t`

`ov_preprocess_input_info_t`

`ov_preprocess_input_tensor_info_t`

`ov_preprocess_output_info_t`

`ov_preprocess_output_tensor_info_t`

`ov_preprocess_input_model_info_t`

`ov_preprocess_preprocess_steps_t`


[Property](https://docs.openvino.ai/group__ov__property__c__api.html)[Rank](https://docs.openvino.ai/group__ov__rank__c__api.html)[Shape](https://docs.openvino.ai/group__ov__shape__c__api.html)[Tensor](https://docs.openvino.ai/group__ov__tensor__c__api.html)[Remote Context](https://docs.openvino.ai/group__ov__remote__context__c__api.html)