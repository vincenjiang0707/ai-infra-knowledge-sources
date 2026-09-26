source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dev__api__plugin__api.html
lastmod: 

# Group Plugin base classes[#](https://docs.openvino.ai#group-plugin-base-classes)

-
*group*Plugin base classes A set of base and helper classes to implement a plugin class.

Defines

-
OV_CREATE_PLUGIN
[#](https://docs.openvino.ai#c.OV_CREATE_PLUGIN) Defines a name of a function creating plugin instance.


-
OV_DEFINE_PLUGIN_CREATE_FUNCTION(PluginType, version, ...)
[#](https://docs.openvino.ai#c.OV_DEFINE_PLUGIN_CREATE_FUNCTION) Defines the exported

`OV_CREATE_PLUGIN`

function which is used to create a plugin instance.

Variables

-
static constexpr Property<std::vector<PropertyName>, PropertyMutability::RO> caching_properties = {"CACHING_PROPERTIES"}
[#](https://docs.openvino.ai#_CPPv418caching_properties) Read-only property to get a std::vector<PropertyName> of properties which should affect the hash calculation for model cache.


-
static constexpr Property<bool, PropertyMutability::RO> caching_with_mmap = {"CACHING_WITH_MMAP"}
[#](https://docs.openvino.ai#_CPPv417caching_with_mmap) Read-only property to get a std::vector<PropertyName> of properties which should affect the loading time from cache.


-
static constexpr Property<bool, PropertyMutability::RW> exclusive_async_requests = {"EXCLUSIVE_ASYNC_REQUESTS"}
[#](https://docs.openvino.ai#_CPPv424exclusive_async_requests) Allow to create exclusive_async_requests with one executor.


-
static constexpr Property<std::string, PropertyMutability::WO> config_device_id = {"CONFIG_DEVICE_ID"}
[#](https://docs.openvino.ai#_CPPv416config_device_id) the property for setting of required device for which config to be updated values: device id starts from “0” - first device, “1” - second device, etc note: plugin may have different devices naming convention


-
static constexpr Property<int32_t, PropertyMutability::RW> threads_per_stream = {"THREADS_PER_STREAM"}
[#](https://docs.openvino.ai#_CPPv418threads_per_stream) Limit #threads that are used by IStreamsExecutor to execute

`parallel_for`

calls.

-
static constexpr Property<std::string, PropertyMutability::RO> compiled_model_runtime_properties{"COMPILED_MODEL_RUNTIME_PROPERTIES"}
[#](https://docs.openvino.ai#_CPPv433compiled_model_runtime_properties) It contains compiled_model_runtime_properties information to make plugin runtime can check whether it is compatible with the cached compiled model, the result is returned by get_property() calling.

The information details are defined by plugin itself, each plugin may require different runtime contents. For example, CPU plugin will contain OV version, while GPU plugin will contain OV and GPU driver version, etc.

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)doesn’t understand its content and only read it from plugin and write it into blob header.

-
static constexpr Property<bool, PropertyMutability::RO> compiled_model_runtime_properties_supported{"COMPILED_MODEL_RUNTIME_PROPERTIES_SUPPORTED"}
[#](https://docs.openvino.ai#_CPPv443compiled_model_runtime_properties_supported) Check whether the attached compiled_model_runtime_properties is supported by this device runtime.


-
static constexpr Property<float, PropertyMutability::RW> query_model_ratio = {"QUERY_MODEL_RATIO"}
[#](https://docs.openvino.ai#_CPPv417query_model_ratio) Read-write property to set the percentage of the estimated model size which is used to determine the query model results for further processing.


-
static constexpr Property<bool, PropertyMutability::RW> enable_lp_transformations = {"LP_TRANSFORMS_MODE"}
[#](https://docs.openvino.ai#_CPPv425enable_lp_transformations) Allow execution of low precision transformations in plugin’s pipelines.


-
interface ICore
[#](https://docs.openvino.ai#_CPPv4N2ov5ICoreE) *#include <icore.hpp>*Minimal

[ICore](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_core)interface to allow plugin to get information from[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)OpenVINO class.Public Functions

-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> read_model(const std::string &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights, bool frontend_mode = false) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore10read_modelERKNSt6stringERKN2ov6TensorEb) Reads IR xml and bin (with the same name) files.

- Parameters:
**model**– string with IR**weights**– shared pointer to constant blob with weights**frontend_mode**– read network without post-processing or other transformations

- Returns:
shared pointer to

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)


Reads IR xml and bin from buffer. This method is not exposed to public API.

- Parameters:
**model**– shared pointer to aligned buffer with IR**weights**– shared pointer to aligned buffer with weights

- Returns:
shared pointer to

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)


-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> read_model(const std::string &model_path, const std::string &bin_path, const AnyMap &properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore10read_modelERKNSt6stringERKNSt6stringERK6AnyMap) Reads IR xml and bin files.

- Parameters:
**model_path**– path to IR file**bin_path**– path to bin file, if path is empty, will try to read bin file with the same name as xml and if bin file with the same name was not found, will load IR without weights.**properties**– Optional map of pairs: (property name, property value) relevant only for this read operation.

- Returns:
shared pointer to

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)


Creates a compiled mdel from a model object.

Users can create as many models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Parameters:
**model**– OpenVINO[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)**device_name**– Name of device to load model to**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation

- Returns:
A pointer to compiled model



Creates a compiled model from a model object.

Users can create as many models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Parameters:
**model**– OpenVINO[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)**context**– “Remote” (non-CPU) accelerator device-specific execution context to use**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation

- Returns:
A pointer to compiled model



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> compile_model(const std::string &model_path, const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore13compile_modelERKNSt6stringERKNSt6stringERKN2ov6AnyMapE) Creates a compiled model from a model file.

Users can create as many models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Parameters:
**model_path**– Path to model**device_name**– Name of device to load model to**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation

- Returns:
A pointer to compiled model



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> compile_model(const std::string &model_str, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights, const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore13compile_modelERKNSt6stringERKN2ov6TensorERKNSt6stringERKN2ov6AnyMapE) Creates a compiled model from a model memory.

Users can create as many models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Parameters:
**model_str**– String data of model**weights**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)’s weights**device_name**– Name of device to load model to**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation

- Returns:
A pointer to compiled model



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(std::istream &model, const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config = {}) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore12import_modelERNSt7istreamERKNSt6stringERKN2ov6AnyMapE) Creates a compiled model from a previously exported model.

- Parameters:
**model**– model stream**device_name**– Name of device load executable model on**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation*

- Returns:
A pointer to compiled model



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(std::istream &modelStream, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> &context, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config = {}) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore12import_modelERNSt7istreamERKN2ov5SoPtrIN2ov14IRemoteContextEEERKN2ov6AnyMapE) Creates a compiled model from a previously exported model.

- Parameters:
**model**– model stream**context**– Remote context**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation*

- Returns:
A pointer to compiled model



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config = {}) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore12import_modelERKN2ov6TensorERKNSt6stringERKN2ov6AnyMapE) Creates a compiled model from a previously exported model.

- Parameters:
**compiled_blob**– model blob**device_name**– Name of device load executable model on**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation*

- Returns:
A pointer to compiled model



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> &context, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config = {}) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore12import_modelERKN2ov6TensorERKN2ov5SoPtrIN2ov14IRemoteContextEEERKN2ov6AnyMapE) Creates a compiled model from a previously exported model.

- Parameters:
**compiled_blob**– model blob**context**– Remote context**config**– Optional map of pairs: (config parameter name, config parameter value) relevant only for this load operation*

- Returns:
A pointer to compiled model



Query device if it supports specified network with specified configuration.

- Parameters:
**model**– OpenVINO[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)**device_name**– A name of a device to query**config**– Optional map of pairs: (config parameter name, config parameter value)

- Returns:
An object containing a map of pairs a layer name -> a device name supporting this layer.



-
virtual std::vector<std::string> get_available_devices() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore21get_available_devicesEv) Returns devices available for neural networks inference.

- Returns:
A vector of devices. The devices are returned as { CPU, GPU.0, GPU.1, MYRIAD } If there more than one device of specific type, they are enumerated with .# suffix.



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> create_context(const std::string &device_name, const AnyMap &args) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore14create_contextERKNSt6stringERK6AnyMap) Create a new shared context object on specified accelerator device using specified plugin-specific low level device API parameters (device handle, pointer, etc.)

- Parameters:
**device_name**– Name of a device to create new shared context on.**params**– Map of device-specific shared context parameters.

- Returns:
A shared pointer to a created remote context.



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> get_default_context(const std::string &device_name) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore19get_default_contextERKNSt6stringE) Get a pointer to default shared context object for the specified device.

- Parameters:
**device_name**– - A name of a device to get create shared context from.- Returns:
A shared pointer to a default remote context.



-
virtual
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &device_name, const std::string &name, const AnyMap &arguments) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore12get_propertyERKNSt6stringERKNSt6stringERK6AnyMap) Gets properties related to device behaviour.

- Parameters:
**device_name**– Name of a device to get a property value.**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.**arguments**– Additional arguments to get a property.

- Returns:
Value of a property corresponding to the property name.



-
template<typename T, PropertyMutability M>

inline[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1ME)get_property(const std::string &device_name, const[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1ME),[M](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1ME)> &property) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1ME) Gets properties related to device behaviour.


-
template<typename T, PropertyMutability M>

inline[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1MERK6AnyMap)get_property(const std::string &device_name, const[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1MERK6AnyMap),[M](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1MERK6AnyMap)> &property, const AnyMap &arguments) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov5ICore12get_propertyE1TRKNSt6stringERK8PropertyI1T1MERK6AnyMap) Gets properties related to device behaviour.


-
virtual AnyMap get_supported_property(const std::string &full_device_name, const AnyMap &properties, const bool keep_core_property = true) const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov5ICore22get_supported_propertyERKNSt6stringERK6AnyMapKb) Get only properties that are supported by specified device.

- Parameters:
**full_device_name**– Name of a device (can be either virtual or hardware)**properties**– Properties that can contains configs that are not supported by device**keep_core_property**– Whether to return core-level properties

- Returns:
map of properties that are supported by device



-
virtual ~ICore()
[#](https://docs.openvino.ai#_CPPv4N2ov5ICoreD0Ev) Default virtual destructor.


-
virtual std::shared_ptr<

-
OV_CREATE_PLUGIN