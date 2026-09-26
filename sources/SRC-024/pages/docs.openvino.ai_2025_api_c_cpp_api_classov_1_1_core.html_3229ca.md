source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_core.html
lastmod: 

# Class ov::Core[#](https://docs.openvino.ai#class-ov-core)

-
class Core
[#](https://docs.openvino.ai#_CPPv4N2ov4CoreE) This class represents an OpenVINO runtime

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)entity.User applications can create several

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)class instances, but in this case the underlying plugins are created multiple times and not shared between several[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instances. The recommended way is to have a single[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instance per application.Unnamed Group

-
std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> read_model(const std::string &model_path, const std::string &bin_path = {}, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties = {}) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core10read_modelERKNSt6stringERKNSt6stringERKN2ov6AnyMapE) Reads models from IR / ONNX / PDPD / TF / TFLite file formats.

- Parameters:
**model_path**– Path to a model.**bin_path**– Path to a data file. For IR format (*.bin):if

`bin_path`

is empty, will try to read a bin file with the same name as xml andif the bin file with the same name is not found, will load IR without weights. For the following file formats the

`bin_path`

parameter is not used:ONNX format (*.onnx)

PDPD (*.pdmodel)

TF (*.pb, *.meta, SavedModel directory)

TFLite (*.tflite)


**properties**– Optional map of pairs: (property name, property value) relevant only for this read operation.

- Returns:
A model.



Unnamed Group

-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpENK2ov4Core10read_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)...> read_model(const std::string &model_path, const std::string &bin_path,[Properties](https://docs.openvino.ai#_CPPv4IDpENK2ov4Core10read_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)&&... properties) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov4Core10read_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties) Reads models from IR / ONNX / PDPD / TF / TFLite file formats.

- Parameters:
**model_path**– Path to a model.**bin_path**– Path to a data file. For IR format (*.bin):if

`bin_path`

is empty, will try to read a bin file with the same name as xml andif the bin file with the same name is not found, will load IR without weights. For the following file formats the

`bin_path`

parameter is not used:ONNX format (*.onnx)

PDPD (*.pdmodel)

TF (*.pb, *.meta, SavedModel directory)

TFLite (*.tflite)


**properties**– Optional pack of pairs: (property name, property value) relevant only for this read operation.

- Returns:
A model.



Unnamed Group

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)compile_model(const std::string &model_path, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core13compile_modelERKNSt6stringERK6AnyMap) Reads and loads a compiled model from the IR/ONNX/PDPD file to the default OpenVINO device selected by the AUTO plugin.

This can be more efficient than using the

[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)+ Core::compile_model(model_in_memory_object) flow, especially for cases when caching is enabled and a cached model is available.- Parameters:
**model_path**– Path to a model.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Unnamed Group

-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringEDpRR10Properties)...> compile_model(const std::string &model_path,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringEDpRR10Properties) Reads and loads a compiled model from IR / ONNX / PDPD file to the default OpenVINO device selected by AUTO plugin.

This can be more efficient than using read_model + compile_model(Model) flow especially for cases when caching is enabled and cached model is available

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_path**– path to model with string or wstring**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model



Unnamed Group

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)compile_model(const std::string &model_path, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core13compile_modelERKNSt6stringERKNSt6stringERK6AnyMap) Reads a model and creates a compiled model from the IR/ONNX/PDPD file.

This can be more efficient than using the

[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)+ Core::compile_model(model_in_memory_object) flow, especially for cases when caching is enabled and a cached model is available.- Parameters:
**model_path**– Path to a model.**device_name**– Name of a device to load a model to.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Unnamed Group

-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)...> compile_model(const std::string &model_path, const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties) Reads a model and creates a compiled model from the IR/ONNX/PDPD file.

This can be more efficient than using read_model + compile_model(Model) flow especially for cases when caching is enabled and cached model is available.

- Template Parameters:
**Properties**– Should be a pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_path**– Path to a model.**device_name**– Name of a device to load a model to.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Unnamed Group

-
void add_extension(const std::string &library_path)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core13add_extensionERKNSt6stringE) Registers an extension to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**library_path**– Path to the library with[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension).


Public Functions

-
explicit Core(const std::string &xml_config_file = {})
[#](https://docs.openvino.ai#_CPPv4N2ov4Core4CoreERKNSt6stringE) Constructs an OpenVINO

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instance with devices and their plugins description.There are two ways how to configure device plugins:

(default) Use XML configuration file in case of dynamic libraries build;

Use strictly defined configuration in case of static libraries build.


- Parameters:
**xml_config_file**– Path to the .xml file with plugins to load from. If path contains only file name with extension, file will be searched in a folder with OpenVINO runtime shared library. If the XML configuration file is not specified, default OpenVINO Runtime plugins are loaded from:(dynamic build) default

`plugins.xml`

file located in the same folder as OpenVINO runtime shared library;(static build) statically defined configuration. In this case path to the .xml file is ignored.




-
std::map<std::string,
[Version](https://docs.openvino.ai/structov_1_1_version.html#_CPPv4N2ov7VersionE)> get_versions(const std::string &device_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_versionsERKNSt6stringE) Returns device plugins version information. Device name can be complex and identify multiple devices at once like

`HETERO:CPU,GPU`

; in this case, std::map contains multiple entries, each per device.- Parameters:
**device_name**– Device name to identify a plugin.- Returns:
A vector of versions.



-
std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> read_model(const std::string &model, const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core10read_modelERKNSt6stringERK6Tensor) Reads models from IR / ONNX / PDPD / TF / TFLite formats.

Note

Created model object shares the weights with the

`weights`

object. Thus, do not create`weights`

on temporary data that can be freed later, since the model constant data will point to an invalid memory.- Parameters:
**model**– String with a model in IR / ONNX / PDPD / TF / TFLite format.**weights**– Shared pointer to a constant tensor with weights. Reading ONNX / PDPD / TF / TFLite models does not support loading weights from the`weights`

tensors.

- Returns:
A model.



Creates and loads a compiled model from a source model to the default OpenVINO device selected by the AUTO plugin.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources).

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a).**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Creates and loads a compiled model from a source model to the default OpenVINO device selected by AUTO plugin.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model



Creates a compiled model from a source model object.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources).

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a).**device_name**– Name of a device to load a model to.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Creates a compiled model from a source model object.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)**device_name**– Name of device to load model to**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)compile_model(const std::string &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core13compile_modelERKNSt6stringERKN2ov6TensorERKNSt6stringERK6AnyMap) Reads a model and creates a compiled model from the IR/ONNX/PDPD memory.

Note

Created model object shares the weights with the

`weights`

object. Thus, do not create`weights`

on temporary data that can be freed later, since the model constant data will point to an invalid memory.- Parameters:
**model**– String with a model in IR/ONNX/PDPD format.**weights**– Shared pointer to a constant tensor with weights. Reading ONNX/PDPD models does not support loading weights from the`weights`

tensors.**device_name**– Name of a device to load a model to.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKN2ov6TensorERKNSt6stringEDpRR10Properties)...> compile_model(const std::string &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights, const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKN2ov6TensorERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKN2ov6TensorERKNSt6stringEDpRR10Properties) Reads a model and creates a compiled model from the IR/ONNX/PDPD memory.

Note

Created model object shares the weights with the

`weights`

object. Thus, do not create`weights`

on temporary data that can be freed later, since the model constant data will point to an invalid memory.- Parameters:
**model**– String with a model in IR/ONNX/PDPD format.**weights**– Shared pointer to a constant tensor with weights. Reading ONNX/PDPD models does not support loading weights from the`weights`

tensors.**device_name**– Name of a device to load a model to.

- Template Parameters:
**Properties**– Should be a pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Returns:
A compiled model.



Creates a compiled model from a source model within a specified remote context.

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a).**context**– A reference to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model object.



Creates a compiled model from a source model within a specified remote context.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)**context**– Pointer to[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model object



Registers an extension to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extension**– Pointer to the extension.


Registers extensions to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extensions**– Vector of loaded extensions.


-
template<class T, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE),[T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1T)>::value, bool>::type = true>

inline void add_extension(const[T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1T)&extension)[#](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1T) Registers an extension to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extension**–[Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class that is inherited from the[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class.


-
template<class T, class ...Targs, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE),[T](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs)>::value, bool>::type = true>

inline void add_extension(const[T](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs)&extension,[Targs](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs)... args)[#](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs) Registers extensions to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extension**–[Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class that is inherited from the[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class.**args**– A list of extensions.



-
template<class T, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE),[T](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov2op2OpE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvv)>::value, bool>::type = true>

inline void add_extension()[#](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov2op2OpE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvv) Registers a custom operation inherited from

[ov::op::Op](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_op).

-
template<class T, class ...Targs, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE),[T](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifIXaaNSt10is_base_ofIN2ov2op2OpE1TE5valueEsZ5TargsEbE4typeEEN2ov4Core13add_extensionEvv)>::value && sizeof...([Targs](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifIXaaNSt10is_base_ofIN2ov2op2OpE1TE5valueEsZ5TargsEbE4typeEEN2ov4Core13add_extensionEvv)), bool>::type = true>

inline void add_extension()[#](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifIXaaNSt10is_base_ofIN2ov2op2OpE1TE5valueEsZ5TargsEbE4typeEEN2ov4Core13add_extensionEvv) Registers custom operations inherited from

[ov::op::Op](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_op).

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(std::istream &model_stream, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERNSt7istreamERKNSt6stringERK6AnyMap) Imports a compiled model from the previously exported one.

- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERKNSt6stringEDpRR10Properties)...> import_model(std::istream &model_stream, const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERKNSt6stringEDpRR10Properties) Imports a compiled model from the previously exported one.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(std::istream &model_stream, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERNSt7istreamERK13RemoteContextRK6AnyMap) Imports a compiled model from the previously exported one with the specified remote context.

- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– A reference to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object. Note, if the device from`context`

was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERK13RemoteContextDpRR10Properties)...> import_model(std::istream &model_stream, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERK13RemoteContextDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERK13RemoteContextDpRR10Properties) Imports a compiled model from the previously exported one with the specified remote context.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– Pointer to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERKN2ov6TensorERKNSt6stringERK6AnyMap) Imports a compiled model from the previously exported one.

- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERKNSt6stringEDpRR10Properties)...> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERKNSt6stringEDpRR10Properties) Imports a compiled model from the previously exported one.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERKN2ov6TensorERK13RemoteContextRK6AnyMap) Imports a compiled model from the previously exported one with the specified remote context.

- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– A reference to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object. Note, if the device from`context`

was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERK13RemoteContextDpRR10Properties)...> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERK13RemoteContextDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERK13RemoteContextDpRR10Properties) Imports a compiled model from the previously exported one with the specified remote context.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– Pointer to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Query device if it supports the specified model with specified properties.

- Parameters:
**device_name**– Name of a device to query.**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object to query.**properties**– Optional map of pairs: (property name, property value).

- Returns:
An object containing a map of pairs an operation name -> a device name supporting this operation.



Queries a device if it supports the specified model with specified properties.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– Name of a device to query.**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object to query.**properties**– Optional pack of pairs: (property name, property value) relevant only for this query operation.

- Returns:
An object containing a map of pairs an operation name -> a device name supporting this operation.



-
void set_property(const AnyMap &properties)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core12set_propertyERK6AnyMap) Sets properties for all the registered devices, acceptable keys can be found in openvino/runtime/properties.hpp.

- Parameters:
**properties**– Map of pairs: (property name, property value).


-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<void,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)...> set_property([Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties) Sets properties for all the registered devices, acceptable keys can be found in openvino/runtime/properties.hpp.

- Template Parameters:
**Properties**– Should be a pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**properties**– Optional pack of pairs: property name, property value.


-
void set_property(const std::string &device_name, const AnyMap &properties)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core12set_propertyERKNSt6stringERK6AnyMap) Sets properties for a device, acceptable keys can be found in openvino/runtime/properties.hpp.

- Parameters:
**device_name**– Name of a device.**properties**– Map of pairs: (property name, property value).



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<void,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEERKNSt6stringEDpRR10Properties)...> set_property(const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEERKNSt6stringEDpRR10Properties) Sets properties for a device, acceptable keys can be found in openvino/runtime/properties.hpp.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– Name of a device.**properties**– Optional pack of pairs: (property name, property value).



-
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &device_name, const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_propertyERKNSt6stringERKNSt6stringE) Gets properties related to device behaviour.

The method extracts information that can be set via the set_property method.

- Parameters:
**device_name**– Name of a device to get a property value.**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.

- Returns:
Value of a property corresponding to the property name.



-
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &device_name, const std::string &name, const AnyMap &arguments) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_propertyERKNSt6stringERKNSt6stringERK6AnyMap) Gets properties related to device behaviour.

The method extracts information that can be set via the set_property method.

- Parameters:
**device_name**– Name of a device to get a property value.**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.**arguments**– Additional arguments to get a property.

- Returns:
Value of a property corresponding to the property name.



-
inline
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_propertyERKNSt6stringE) Gets properties related to core behaviour.

The method extracts information that can be set via the set_property method.

- Parameters:
**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.- Returns:
Value of a property corresponding to the property name.



-
template<typename T, PropertyMutability M>

inline[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE)get_property(const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE),[M](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE)> &property) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE) Gets properties related to device behaviour.

The method is needed to request common device or system properties. It can be device name, temperature, and other devices-specific values.


-
template<typename T, PropertyMutability M>

inline[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap)get_property(const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap),[M](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap)> &property, const AnyMap &arguments) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap) Gets properties related to device behaviour.

The method is needed to request common device or system properties. It can be device name, temperature, other devices-specific values.


-
template<typename T, PropertyMutability M, typename ...Args>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args),[Args](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args)...> get_property(const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args),[M](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args)> &property,[Args](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args)&&... args) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args) Gets properties related to device behaviour.

The method is needed to request common device or system properties. It can be device name, temperature, other devices-specific values.

- Template Parameters:
**T**– Type of a returned value.**M**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)mutability.**Args**– Set of additional arguments ended with property object variable.

- Parameters:
**device_name**– Name of a device to get a property value.**property**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)object.**args**– Optional pack of pairs: (argument name, argument value) ended with property object.

- Returns:
[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)value.


-
std::vector<std::string> get_available_devices() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Core21get_available_devicesEv) Returns devices available for inference.

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)objects go over all registered plugins and ask about available devices.- Returns:
A vector of devices. The devices are returned as { CPU, GPU.0, GPU.1, NPU }. If there is more than one device of a specific type, they are enumerated with the .# suffix. Such enumerated device can later be used as a device name in all

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)methods like[Core::compile_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a),[Core::query_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab),[Core::set_property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e)and so on.


-
void register_plugin(const std::string &plugin, const std::string &device_name, const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core15register_pluginERKNSt6stringERKNSt6stringERKN2ov6AnyMapE) Register a new device and plugin that enables this device inside OpenVINO Runtime.

Note

For security purposes it suggested to specify absolute path to register plugin.

- Parameters:
**plugin**– Path (absolute or relative) or name of a plugin. Depending on platform,`plugin`

is wrapped with shared library suffix and prefix to identify library full name. For example, on Linux platform, plugin name specified as`plugin_name`

will be wrapped as`libplugin_name.so`

. Plugin search algorithm:If

`plugin`

points to an exact library path (absolute or relative), it will be used.If

`plugin`

specifies file name (`libplugin_name.so`

) or plugin name (`plugin_name`

), it will be searched by file name (`libplugin_name.so`

) in CWD or in paths pointed by PATH/LD_LIBRARY_PATH/DYLD_LIBRARY_PATH environment variables depending on the platform.

**device_name**– Device name to register a plugin for.**config**– Plugin configuration options



-
void unload_plugin(const std::string &device_name)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core13unload_pluginERKNSt6stringE) Unloads the previously loaded plugin identified by

`device_name`

from OpenVINO Runtime. The method is needed to remove loaded plugin instance and free its resources. If plugin for a specified device has not been created before, the method throws an exception.Note

This method does not remove plugin from the plugins known to OpenVINO

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**device_name**– Device name identifying plugin to remove from OpenVINO Runtime.


-
void register_plugins(const std::string &xml_config_file)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core16register_pluginsERKNSt6stringE) Registers a device plugin to the OpenVINO Runtime

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instance using an XML configuration file with plugins description.The XML file has the following structure:

<ie> <plugins> <plugin name="" location=""> <extensions> <extension location=""/> </extensions> <properties> <property key="" value=""/> </properties> </plugin> </plugins> </ie>

`name`

identifies name of a device enabled by a plugin.`location`

specifies absolute path to dynamic library with a plugin. The path can also be relative to XML file directory. It allows having common config for different systems with different configurations.`properties`

are set to a plugin via the[ov::Core::set_property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e)method.`extensions`

are set to a plugin via the[ov::Core::add_extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1adb5929d85ce33c029794f0dbbb23340f)method.

Note

For security purposes it suggested to specify absolute path to register plugin.

- Parameters:
**xml_config_file**– A path to .xml file with plugins to register.


-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)create_context(const std::string &device_name, const AnyMap &remote_properties)[#](https://docs.openvino.ai#_CPPv4N2ov4Core14create_contextERKNSt6stringERK6AnyMap) Creates a new remote shared context object on the specified accelerator device using specified plugin-specific low-level device API parameters (device handle, pointer, context, etc.).

- Parameters:
**device_name**– Name of a device to create a new shared context on.**remote_properties**– Map of device-specific shared context remote properties.

- Returns:
Reference to a created remote context.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE),[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core14create_contextEN4util20EnableIfAllStringAnyI13RemoteContextDp10PropertiesEERKNSt6stringEDpRR10Properties)...> create_context(const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core14create_contextEN4util20EnableIfAllStringAnyI13RemoteContextDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... remote_properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core14create_contextEN4util20EnableIfAllStringAnyI13RemoteContextDp10PropertiesEERKNSt6stringEDpRR10Properties) Creates a new shared context object on specified accelerator device using specified plugin-specific low level device API properties (device handle, pointer, etc.)

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– Name of a device to create new shared context on.**remote_properties**– Pack of device-specific shared context remote properties.

- Returns:
A shared pointer to a created remote context.



-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)get_default_context(const std::string &device_name)[#](https://docs.openvino.ai#_CPPv4N2ov4Core19get_default_contextERKNSt6stringE) Gets a pointer to default (plugin-supplied) shared context object for the specified accelerator device.

- Parameters:
**device_name**– Name of a device to get a default shared context from.- Returns:
Reference to a default remote context.



-
std::shared_ptr<