source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_i_plugin.html
lastmod: 

# Class ov::IPlugin[#](https://docs.openvino.ai#class-ov-iplugin)

-
class IPlugin : public std::enable_shared_from_this<
[IPlugin](https://docs.openvino.ai#_CPPv4N2ov7IPluginE)>[#](https://docs.openvino.ai#_CPPv4N2ov7IPluginE) OpenVINO Plugin Interface 2.0.

Public Functions

-
void set_version(const
[Version](https://docs.openvino.ai/structov_1_1_version.html#_CPPv4N2ov7VersionE)&version)[#](https://docs.openvino.ai#_CPPv4N2ov7IPlugin11set_versionERK7Version) Sets a plugin version.

- Parameters:
**version**– A version to set


-
const
[Version](https://docs.openvino.ai/structov_1_1_version.html#_CPPv4N2ov7VersionE)&get_version() const[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin11get_versionEv) Returns a plugin version.

- Returns:
A constant

[ov::Version](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_version)object


Compiles model from

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object.- Parameters:
**model**– A model object acquired from[ov::Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)or source construction**properties**– A ov::AnyMap of properties relevant only for this load operation

- Returns:
Created Compiled

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object


-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> compile_model(const std::string &model_path, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) const[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin13compile_modelERKNSt6stringERKN2ov6AnyMapE) Compiles model from

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object.- Parameters:
**model_path**– A path to model (path can be converted from unicode representation)**properties**– A ov::AnyMap of properties relevant only for this load operation

- Returns:
Created Compiled

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object


Compiles model from

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object, on specified remote context.- Parameters:
**model**– A model object acquired from[ov::Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)or source construction**properties**– A ov::AnyMap of properties relevant only for this load operation**context**– A pointer to plugin context derived from[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)class used to execute the model

- Returns:
Created Compiled

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object


-
virtual void set_property(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) = 0[#](https://docs.openvino.ai#_CPPv4N2ov7IPlugin12set_propertyERKN2ov6AnyMapE) Sets properties for plugin, acceptable keys can be found in openvino/runtime/properties.hpp.

- Parameters:
**properties**– ov::AnyMap of properties


-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &arguments) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin12get_propertyERKNSt6stringERKN2ov6AnyMapE) Gets properties related to plugin behaviour.

- Parameters:
**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.**arguments**– Additional arguments to get a property.

- Returns:
Value of a property corresponding to the property name.



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> create_context(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &remote_properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin14create_contextERKN2ov6AnyMapE) Creates a remote context instance based on a map of properties.

- Parameters:
**remote_properties**– Map of device-specific shared context remote properties.- Returns:
A remote context object



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> get_default_context(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &remote_properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin19get_default_contextERKN2ov6AnyMapE) Provides a default remote context instance if supported by a plugin.

- Parameters:
**remote_properties**– Map of device-specific shared context remote properties.- Returns:
The default context.



-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(std::istream &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin12import_modelERNSt7istreamERKN2ov6AnyMapE) Creates an compiled model from an previously exported model using plugin implementation and removes OpenVINO Runtime magic and plugin name.

- Parameters:
**model**– Reference to model input stream**properties**– A ov::AnyMap of properties

- Returns:
An Compiled model



-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(std::istream &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> &context, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin12import_modelERNSt7istreamERKN2ov5SoPtrIN2ov14IRemoteContextEEERKN2ov6AnyMapE) Creates an compiled model from an previously exported model using plugin implementation and removes OpenVINO Runtime magic and plugin name.

- Parameters:
**model**– Reference to model input stream**context**– A pointer to plugin context derived from[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)class used to execute the network**properties**– A ov::AnyMap of properties

- Returns:
An Compiled model



-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin12import_modelERKN2ov6TensorERKN2ov6AnyMapE) Creates an compiled model from an previously exported model using plugin implementation and removes OpenVINO Runtime magic and plugin name.

- Parameters:
**model**– Reference to[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with exported model**properties**– A ov::AnyMap of properties

- Returns:
An Compiled model



-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> &context, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin12import_modelERKN2ov6TensorERKN2ov5SoPtrIN2ov14IRemoteContextEEERKN2ov6AnyMapE) Creates an compiled model from an previously exported model using plugin implementation and removes OpenVINO Runtime magic and plugin name.

- Parameters:
**model**– Reference to[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with exported model**context**– A pointer to plugin context derived from[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)class used to execute the network**properties**– A ov::AnyMap of properties

- Returns:
An Compiled model



Queries a plugin about supported layers in model.

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object to query.**properties**– Optional map of pairs: (property name, property value).

- Returns:
An object containing a map of pairs an operation name -> a device name supporting this operation.



-
void set_core(const std::weak_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICore](https://docs.openvino.ai/group__ov__dev__api__plugin__api.html#_CPPv4N2ov5ICoreE)> &core)[#](https://docs.openvino.ai#_CPPv4N2ov7IPlugin8set_coreERKNSt8weak_ptrIN2ov5ICoreEEE) Sets pointer to

[ICore](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_core)interface.- Parameters:
**core**– Pointer to[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)interface


-
std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICore](https://docs.openvino.ai/group__ov__dev__api__plugin__api.html#_CPPv4N2ov5ICoreE)> get_core() const[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin8get_coreEv) Gets reference to

[ICore](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_core)interface.- Returns:
Reference to

[ICore](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_core)interface


-
const std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[ExecutorManager](https://docs.openvino.ai/group__ov__dev__api__threading.html#_CPPv4N2ov9threading15ExecutorManagerE)> &get_executor_manager() const[#](https://docs.openvino.ai#_CPPv4NK2ov7IPlugin20get_executor_managerEv) Gets reference to tasks execution manager.

- Returns:
Reference to ExecutorManager interface



-
void set_version(const