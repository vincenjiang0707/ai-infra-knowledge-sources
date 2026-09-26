source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__property__c__api.html
lastmod: 

# Group Property[#](https://docs.openvino.ai#group-property)

-
*group*Property The definitions & operations about property.

Variables

- ov_property_key_intel_auto_enable_startup_fallback
Read-write property<string> to enable/disable CPU as accelerator (or helper device) at the beginning.


- ov_property_key_intel_auto_enable_runtime_fallback
Read-write property<string> to enable/disable runtime fallback to other devices when infer fails.


- ov_property_key_supported_properties
Read-only property<string> to get a string list of supported read-only properties.


- ov_property_key_available_devices
Read-only property<string> to get a list of available device IDs.


- ov_property_key_optimal_number_of_infer_requests
Read-only property<uint32_t string> to get an unsigned integer value of optimaln number of compiled model infer requests.


- ov_property_key_range_for_async_infer_requests
Read-only property<string(unsigned int, unsigned int, unsigned int)> to provide a hint for a range for number of async infer requests. If device supports streams, the metric provides range for number of IRs per stream.


- ov_property_key_range_for_streams
Read-only property<string(unsigned int, unsigned int)> to provide information about a range for streams on platforms where streams are supported.


- ov_property_key_device_full_name
Read-only property<string> to get a string value representing a full device name.


- ov_property_key_device_capabilities
Read-only property<string> to get a string list of capabilities options per device.


- ov_property_key_model_name
Read-only property<string> to get a name of name of a model.


- ov_property_key_optimal_batch_size
Read-only property<uint32_t string> to query information optimal batch size for the given device and the network.


- ov_property_key_max_batch_size
Read-only property to get maximum batch size which does not cause performance degradation due to memory swap impact.


- ov_property_key_cache_dir
Read-write property<string> to set/get the directory which will be used to store any data cached by plugins.


- ov_property_key_cache_mode
Read-write property<string> to select the cache mode between optimize_size and optimize_speed. If optimize_size is selected(default), smaller cache files will be created. If optimize_speed is selected, loading time will decrease but the cache file size will increase. This is only supported from GPU.


- ov_property_key_cache_encryption_callbacks
Write-only property<ov_encryption_callbacks*> to set encryption and decryption function for model cache. If ov_property_key_cache_encryption_callbacks is set, model topology will be encrypted when saving to the cache and decrypted when loading from the cache. This property is set in ov_core_compile_model_* only.


- ov_property_key_num_streams
Read-write property<uint32_t string> to set/get the number of executor logical partitions.


- ov_property_key_inference_num_threads
Read-write property<int32_t string> to set/get the maximum number of threads that can be used for inference tasks.


- ov_property_key_hint_enable_cpu_pinning
Read-write property, it is high-level OpenVINO hint for using CPU pinning to bind CPU threads to processors during inference.


- ov_property_key_hint_enable_hyper_threading
Read-write property, it is high-level OpenVINO hint for using hyper threading processors during CPU inference.


- ov_property_key_hint_performance_mode
Read-write property, it is high-level OpenVINO Performance Hints.


- ov_property_key_hint_scheduling_core_type
Read-write property, it is high-level OpenVINO Hints for the type of CPU core used during inference.


- ov_property_key_hint_inference_precision
Read-write property<ov_element_type_e> to set the hint for device to use specified precision for inference.


- ov_property_key_hint_num_requests
(Optional) Read-write property<uint32_t string> that backs the Performance Hints by giving additional information on how many inference requests the application will be keeping in flight usually this value comes from the actual use-case (e.g. number of video-cameras, or other sources of inputs)


- ov_property_key_log_level
Read-write property<string> for setting desirable log level.


- ov_property_key_hint_model_priority
Read-write property, high-level OpenVINO model priority hint.


- ov_property_key_enable_profiling
Read-write property<string> for setting performance counters option.


- ov_property_key_device_priorities
Read-write property<std::pair<std::string, Any>>, device Priorities config option, with comma-separated devices listed in the desired priority.


- ov_property_key_hint_execution_mode
Read-write property<string> for high-level OpenVINO Execution hint unlike low-level properties that are individual (per-device), the hints are something that every device accepts and turns into device-specific settings Execution mode hint controls preferred optimization targets (performance or accuracy) for given model It can be set to be below value: “PERFORMANCE”, //!< Optimize for max performance “ACCURACY”, //!< Optimize for max accuracy.


- ov_property_key_force_tbb_terminate
Read-write property to set whether force terminate tbb when ov core destruction.


- ov_property_key_enable_mmap
Read-write property to configure

`mmap()`

use for model read.

- ov_property_key_auto_batch_timeout
Read-write property.


- ov_property_key_intel_gpu_config_file
Read-write property to configure config file for GPU.