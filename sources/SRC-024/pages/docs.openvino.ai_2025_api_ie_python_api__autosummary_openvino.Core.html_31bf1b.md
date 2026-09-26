source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Core.html
lastmod: 

# openvino.Core[#](https://docs.openvino.ai#openvino-core)

-
*class*openvino.Core[#](https://docs.openvino.ai#openvino.Core) Bases:

`Core`

Core class represents OpenVINO runtime Core entity.

User applications can create several Core class instances, but in this case, the underlying plugins are created multiple times and not shared between several Core instances. The recommended way is to have a single Core instance per application.

-
__init__(
*self: openvino._pyopenvino.Core*,*xml_config_file: str = ''*) None[#](https://docs.openvino.ai#openvino.Core.__init__)

Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(value, /)`__eq__`

Return self==value.

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(self[, xml_config_file])`__init__`

This method is called when a class is subclassed.

(value, /)`__le__`

Return self<=value.

(value, /)`__lt__`

Return self<value.

(value, /)`__ne__`

Return self!=value.

(**kwargs)`__new__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

(self)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(*args, **kwargs)`add_extension`

Overloaded function.

(model[, device_name, config, ...])`compile_model`

Creates a compiled model.

(self, device_name, properties)`create_context`

Creates a new remote shared context object on the specified accelerator device using specified plugin-specific low-level device API parameters.

(self)`get_available_devices`

Returns devices available for inference Core objects goes over all registered plugins.

(self, device_name)`get_default_context`

Gets default (plugin-supplied) shared context object for the specified accelerator device.

(*args, **kwargs)`get_property`

Overloaded function.

(self, device_name)`get_versions`

Returns device plugins version information.

(model_stream, device_name[, config])`import_model`

Imports a compiled model from a previously exported one.

(self, model, device_name[, ...])`query_model`

Query device if it supports specified model with specified properties.

(*args, **kwargs)`read_model`

Overloaded function.

(*args, **kwargs)`register_plugin`

Overloaded function.

(self, xml_config_file)`register_plugins`

Registers a device plugin to OpenVINO Runtime Core instance using XML configuration file with plugins description.

(*args, **kwargs)`set_property`

Overloaded function.

(self, device_name)`unload_plugin`

Unloads the previously loaded plugin identified by device_name from OpenVINO Runtime.

Attributes

Returns devices available for inference Core objects goes over all registered plugins.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Core.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Core.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Core.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Core.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Core.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Core.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Core.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.Core.__hash__) Return hash(self).


-
__init__(
*self: openvino._pyopenvino.Core*,*xml_config_file: str = ''*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Core.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Core.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Core.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Core.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: openvino._pyopenvino.Core*) str[#](https://docs.openvino.ai#openvino.Core.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Core.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Core.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.Core.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Core.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Core._pybind11_conduit_v1_)

-
add_extension(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Core.add_extension) Overloaded function.

add_extension(self: openvino._pyopenvino.Core, library_path: str) -> None

Registers an extension to a Core object.

- param library_path:
Path to library with ov::Extension

- type library_path:
str


add_extension(self: openvino._pyopenvino.Core, extension: openvino._pyopenvino.Extension) -> None

Registers an extension to a Core object.

- param extension:
Extension object.

- type extension:
openvino.Extension


add_extension(self: openvino._pyopenvino.Core, extensions: collections.abc.Sequence[openvino._pyopenvino.Extension]) -> None

Registers extensions to a Core object.

- param extensions:
list of Extension objects.

- type extensions:
list[openvino.Extension]


add_extension(self: openvino._pyopenvino.Core, custom_op: object) -> None

Registers custom Op to a Core object.

- param custom_op:
type of custom Op

- type custom_op:
type[openvino.Op]




-
*property*available_devices[#](https://docs.openvino.ai#openvino.Core.available_devices) Returns devices available for inference Core objects goes over all registered plugins.

GIL is released while running this function.

- Returns:
A list of devices. The devices are returned as: CPU, GPU.0, GPU.1, NPU… If there more than one device of specific type, they are enumerated with .# suffix. Such enumerated device can later be used as a device name in all Core methods like: compile_model, query_model, set_property and so on.

- Return type:
list[str]



-
compile_model(
*model:*,[Model](https://docs.openvino.ai/openvino.Model.html#openvino.Model)| str | Path*device_name: str | None = None*,*config: dict[str, Any] | None = None*,***,*weights: bytes | None = None*)[CompiledModel](https://docs.openvino.ai/openvino.CompiledModel.html#openvino.CompiledModel)[#](https://docs.openvino.ai#openvino.Core.compile_model) Creates a compiled model.

Creates a compiled model from a source Model object or reads model and creates a compiled model from IR / ONNX / PDPD / TF and TFLite file or creates a compiled model from a IR xml and weights in memory. This can be more efficient than using read_model + compile_model(model_in_memory_object) flow, especially for cases when caching is enabled and cached model is available. If device_name is not specified, the default OpenVINO device will be selected by AUTO plugin. Users can create as many compiled models as they need, and use them simultaneously (up to the limitation of the hardware resources).

- Parameters:
**model**(*Union**[**openvino.Model**,**str**,**pathlib.Path**]*) – Model acquired from read_model function or a path to a model in IR / ONNX / PDPD / TF and TFLite format.**device_name**(*str*) – Optional. Name of the device to load the model to. If not specified, the default OpenVINO device will be selected by AUTO plugin.**config**(*dict**,**optional*) – Optional dict of pairs: (property name, property value) relevant only for this load operation.**weights**(*bytes**,**optional**,**keyword-only*) – Optional. Weights of model in memory to be loaded to the model.

- Returns:
A compiled model.

- Return type:


-
create_context(
*self: openvino._pyopenvino.Core*,*device_name: str*,*properties: collections.abc.Mapping[str, object]*)[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai/openvino.RemoteContext.html#openvino.RemoteContext)[#](https://docs.openvino.ai#openvino.Core.create_context) Creates a new remote shared context object on the specified accelerator device using specified plugin-specific low-level device API parameters.

- Parameters:
**device_name**(*str*) – Name of a device to create a new shared context on.**properties**(*dict**[**str**,**Any**]*) – dict of device-specific shared context remote properties.

- Returns:
Remote context instance.

- Return type:


-
get_available_devices(
*self: openvino._pyopenvino.Core*) list[str][#](https://docs.openvino.ai#openvino.Core.get_available_devices) Returns devices available for inference Core objects goes over all registered plugins.

GIL is released while running this function.

- Returns:
A list of devices. The devices are returned as: CPU, GPU.0, GPU.1, NPU… If there more than one device of specific type, they are enumerated with .# suffix. Such enumerated device can later be used as a device name in all Core methods like: compile_model, query_model, set_property and so on.

- Return type:
list[str]



-
get_default_context(
*self: openvino._pyopenvino.Core*,*device_name: str*)[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai/openvino.RemoteContext.html#openvino.RemoteContext)[#](https://docs.openvino.ai#openvino.Core.get_default_context) Gets default (plugin-supplied) shared context object for the specified accelerator device.

- Parameters:
**device_name**(*str*) – Name of a device to get a default shared context from.- Returns:
Remote context instance.

- Return type:


-
get_property(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Core.get_property) Overloaded function.

get_property(self: openvino._pyopenvino.Core, device_name: str, name: str, arguments: collections.abc.Mapping[str, object]) -> object

Gets properties dedicated to device behaviour.

- param device_name:
A name of a device to get a properties value.

- type device_name:
str

- param name:
Property or name of Property.

- type name:
str

- param arguments:
Additional arguments to get a property.

- type arguments:
dict[str, typing.Any]

- return:
Extracted information from property.

- rtype:
typing.Any


get_property(self: openvino._pyopenvino.Core, device_name: str, property: str) -> object

Gets properties dedicated to device behaviour.

- param device_name:
A name of a device to get a properties value.

- type device_name:
str

- param property:
Property or name of Property.

- type property:
str

- return:
Extracted information from property.

- rtype:
typing.Any


get_property(self: openvino._pyopenvino.Core, property: str) -> object

Gets properties dedicated to Core behaviour.

- param property:
Property or name of Property.

- type property:
str

- return:
Extracted information from property.

- rtype:
typing.Any




-
get_versions(
*self: openvino._pyopenvino.Core*,*device_name: str*) dict[str,[openvino._pyopenvino.Version](https://docs.openvino.ai/openvino.Version.html#openvino.Version)][#](https://docs.openvino.ai#openvino.Core.get_versions) Returns device plugins version information.

- Parameters:
**device_name**(*str*) – Device name to identify a plugin.- Returns:
Plugin version information.

- Return type:
dict[str,

[openvino.Version](https://docs.openvino.ai/openvino.Version.html#openvino.Version)]


-
import_model(
*model_stream: bytes | BytesIO |*,[Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)*device_name: str*,*config: dict[str, Any] | None = None*)[CompiledModel](https://docs.openvino.ai/openvino.CompiledModel.html#openvino.CompiledModel)[#](https://docs.openvino.ai#openvino.Core.import_model) Imports a compiled model from a previously exported one.

- Parameters:
**model_stream**(*Union**[**bytes**,**io.BytesIO**,**openvino.Tensor**]*) – Input stream or tensor, containing a model previously exported, using export_model method.**device_name**(*str*) – Name of device to which compiled model is imported. Note: if device_name is not used to compile the original model, an exception is thrown.**config**(*dict**,**optional*) – Optional dict of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.

- Return type:
- Example:

user_stream = compiled.export_model() with open('./my_model', 'wb') as f: f.write(user_stream) # ... new_compiled = core.import_model(user_stream, "CPU")

user_stream = io.BytesIO() compiled.export_model(user_stream) with open('./my_model', 'wb') as f: f.write(user_stream.getvalue()) # or read() if seek(0) was applied before # ... new_compiled = core.import_model(user_stream, "CPU")


-
query_model(
*self: openvino._pyopenvino.Core*,*model: openvino._pyopenvino.Model*,*device_name: str*,*properties: collections.abc.Mapping[str, object] = {}*) dict[str, str][#](https://docs.openvino.ai#openvino.Core.query_model) Query device if it supports specified model with specified properties.

GIL is released while running this function.

- Parameters:
**model**() – Model object to query.*openvino.Model***device_name**(*str*) – A name of a device to query.**properties**(*dict**[**str**,**Any**]*) – Optional dict of pairs: (property name, property value)

- Returns:
Pairs a operation name -> a device name supporting this operation.

- Return type:
dict[str, str]



-
read_model(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Core.read_model) Overloaded function.

read_model(self: openvino._pyopenvino.Core, model: bytes, weights: bytes = b’’) -> openvino._pyopenvino.Model

Reads models from IR / ONNX / PDPD / TF and TFLite formats.

GIL is released while running this function.

- param model:
Bytes with model in IR / ONNX / PDPD / TF and TFLite format.

- type model:
bytes

- param weights:
Bytes with tensor’s data.

- type weights:
bytes

- return:
A model.

- rtype:
openvino.Model


read_model(self: openvino._pyopenvino.Core, model: str, weights: str = ‘’, config: collections.abc.Mapping[str, object] = {}) -> openvino._pyopenvino.Model

Reads models from IR / ONNX / PDPD / TF and TFLite formats.

GIL is released while running this function.

- param model:
A path to a model in IR / ONNX / PDPD / TF and TFLite format.

- type model:
str

- param weights:
A path to a data file For IR format (

*.bin): if path is empty, it tries to read a bin file with the same name as xml and if the bin file with the same name was not found, loads IR without weights. For ONNX format (*.onnx): weights parameter is not used. For PDPD format (*.pdmodel) weights parameter is not used. For TF format (*.pb) weights parameter is not used. For TFLite format ([*](https://docs.openvino.ai#id1).tflite) weights parameter is not used.- type weights:
str

- param config:
Optional map of pairs: (property name, property value) relevant only for this read operation.

- type config:
dict[str, typing.Any], optional

- return:
A model.

- rtype:
openvino.Model


read_model(self: openvino._pyopenvino.Core, model: str, weights: openvino._pyopenvino.Tensor) -> openvino._pyopenvino.Model

Reads models from IR / ONNX / PDPD / TF and TFLite formats.

GIL is released while running this function.

- param model:
A string with model in IR / ONNX / PDPD / TF and TFLite format.

- type model:
str

- param weights:
Tensor with weights. Reading ONNX / PDPD / TF and TFLite models doesn’t support loading weights from weights tensors.

- type weights:
openvino.Tensor

- return:
A model.

- rtype:
openvino.Model


read_model(self: openvino._pyopenvino.Core, model: object, weights: object = None, config: collections.abc.Mapping[str, object] = {}) -> openvino._pyopenvino.Model

Reads models from IR / ONNX / PDPD / TF and TFLite formats.

GIL is released while running this function.

- param model:
A path to a model in IR / ONNX / PDPD / TF and TFLite format or a model itself wrapped in io.ByesIO format.

- type model:
typing.Union[pathlib.Path, io.BytesIO]

- param weights:
A path to a data file For IR format (

*.bin): if path is empty, it tries to read a bin file with the same name as xml and if the bin file with the same name was not found, loads IR without weights. For ONNX format (*.onnx): weights parameter is not used. For PDPD format (*.pdmodel) weights parameter is not used. For TF format (*.pb): weights parameter is not used. For TFLite format ([*](https://docs.openvino.ai#id3).tflite) weights parameter is not used.- type weights:
typing.Union[pathlib.Path, io.BytesIO]

- param config:
Optional map of pairs: (property name, property value) relevant only for this read operation.

- type config:
dict[str, typing.Any], optional

- return:
A model.

- rtype:
openvino.Model




-
register_plugin(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Core.register_plugin) Overloaded function.

register_plugin(self: openvino._pyopenvino.Core, plugin_name: str, device_name: str) -> None

Register a new device and plugin which enable this device inside OpenVINO Runtime.

- param plugin_name:
A path (absolute or relative) or name of a plugin. Depending on platform, plugin_name is wrapped with shared library suffix and prefix to identify library full name E.g. on Linux platform plugin name specified as plugin_name will be wrapped as libplugin_name.so.

- type plugin_name:
str

- param device_name:
A device name to register plugin for.

- type device_name:
str


register_plugin(self: openvino._pyopenvino.Core, plugin_name: str, device_name: str, config: collections.abc.Mapping[str, object]) -> None

Register a new device and plugin which enable this device inside OpenVINO Runtime.

- param plugin_name:
A path (absolute or relative) or name of a plugin. Depending on platform, plugin_name is wrapped with shared library suffix and prefix to identify library full name E.g. on Linux platform plugin name specified as plugin_name will be wrapped as libplugin_name.so.

- type plugin_name:
str

- param device_name:
A device name to register plugin for.

- type device_name:
str

- param config:
Plugin default configuration

- type config:
dict[str, typing.Any], optional




-
register_plugins(
*self: openvino._pyopenvino.Core*,*xml_config_file: str*) None[#](https://docs.openvino.ai#openvino.Core.register_plugins) Registers a device plugin to OpenVINO Runtime Core instance using XML configuration file with plugins description.

- Parameters:
**xml_config_file**(*str*) – A path to .xml file with plugins to register.


-
set_property(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Core.set_property) Overloaded function.

set_property(self: openvino._pyopenvino.Core, properties: collections.abc.Mapping[str, object]) -> None

Sets properties.

- param properties:
dict of pairs: (property name, property value).

- type properties:
dict[str, typing.Any]


set_property(self: openvino._pyopenvino.Core, property: tuple[str, object]) -> None

Sets properties for the device.

- param property:
tuple of (property name, matching property value).

- type property:
tuple[str, typing.Any]


set_property(self: openvino._pyopenvino.Core, device_name: str, properties: collections.abc.Mapping[str, object]) -> None

Sets properties for the device.

- param device_name:
Name of the device.

- type device_name:
str

- param properties:
dict of pairs: (property name, property value).

- type properties:
dict[str, typing.Any]


set_property(self: openvino._pyopenvino.Core, device_name: str, property: tuple[str, object]) -> None

Sets properties for the device.

- param device_name:
Name of the device.

- type device_name:
str

- param property:
tuple of (property name, matching property value).

- type property:
tuple[str, typing.Any]




-
unload_plugin(
*self: openvino._pyopenvino.Core*,*device_name: str*) None[#](https://docs.openvino.ai#openvino.Core.unload_plugin) Unloads the previously loaded plugin identified by device_name from OpenVINO Runtime. The method is needed to remove loaded plugin instance and free its resources. If plugin for a specified device has not been created before, the method throws an exception.

- Parameters:
**device_name**(*str*) – A device name identifying plugin to remove from OpenVINO.


-
__init__(