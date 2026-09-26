source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__core__c__api.html
lastmod: 

# Group Core[#](https://docs.openvino.ai#group-core)

-
*group*Core The definitions & operations about core.

Functions

-
ov_get_openvino_version(ov_version_t *version)
[#](https://docs.openvino.ai#_CPPv423ov_get_openvino_versionP12ov_version_t) Get version of OpenVINO.

- Parameters:
**ov_version_t**– a pointer to the version- Returns:
Status code of the operation: OK(0) for success.



-
ov_version_free(ov_version_t *version)
[#](https://docs.openvino.ai#_CPPv415ov_version_freeP12ov_version_t) Release the memory allocated by ov_version_t.

- Parameters:
**version**– A pointer to the ov_version_t to free memory.


-
ov_core_create(
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)**core)[#](https://docs.openvino.ai#_CPPv414ov_core_createPP9ov_core_t) Constructs OpenVINO Core instance by default. See RegisterPlugins for more details.

- Parameters:
**core**– A pointer to the newly created[ov_core_t](https://docs.openvino.ai#structov__core__t).- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_create_with_config(const char *xml_config_file,
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)**core)[#](https://docs.openvino.ai#_CPPv426ov_core_create_with_configPKcPP9ov_core_t) Constructs OpenVINO Core instance using XML configuration file with devices description. See RegisterPlugins for more details.

- Parameters:
**xml_config_file**– A path to .xml file with devices to load from. If XML configuration file is not specified, then default plugin.xml file will be used.**core**– A pointer to the newly created[ov_core_t](https://docs.openvino.ai#structov__core__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_free(
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core)[#](https://docs.openvino.ai#_CPPv412ov_core_freeP9ov_core_t) Release the memory allocated by

[ov_core_t](https://docs.openvino.ai#structov__core__t).- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)to free memory.


-
ov_core_read_model(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *model_path, const char *bin_path,[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)**model)[#](https://docs.openvino.ai#_CPPv418ov_core_read_modelPK9ov_core_tPKcPKcPP10ov_model_t) Reads models from IR / ONNX / PDPD / TF / TFLite formats.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**model_path**– Path to a model.**bin_path**– Path to a data file. For IR format (*.bin):if

`bin_path`

is empty, will try to read a bin file with the same name as xml andif the bin file with the same name is not found, will load IR without weights. For the following file formats the

`bin_path`

parameter is not used:ONNX format (*.onnx)

PDPD (*.pdmodel)

TF (*.pb)

TFLite (*.tflite)


**model**– A pointer to the newly created model.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_compile_model(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char *device_name, const size_t property_args_size,[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)**compiled_model, ...)[#](https://docs.openvino.ai#_CPPv421ov_core_compile_modelPK9ov_core_tPK10ov_model_tPKcK6size_tPP19ov_compiled_model_tz) Creates a compiled model from a source model object. Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources).

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**model**– Model object acquired from Core::read_model.**device_name**– Name of a device to load a model to.**property_args_size**– How many properties args will be passed, each property contains 2 args: key and value.**compiled_model**– A pointer to the newly created compiled_model.**...**– property paramater: Optional pack of pairs: <char* property_key, char* property_value> relevant only for this load operation operation. Supported property key please see ov_property.h.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_compile_model_from_file(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *model_path, const char *device_name, const size_t property_args_size,[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)**compiled_model, ...)[#](https://docs.openvino.ai#_CPPv431ov_core_compile_model_from_filePK9ov_core_tPKcPKcK6size_tPP19ov_compiled_model_tz) Reads a model and creates a compiled model from the IR/ONNX/PDPD file. This can be more efficient than using the ov_core_read_model_from_XXX + ov_core_compile_model flow, especially for cases when caching is enabled and a cached model is available.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**model_path**– Path to a model.**device_name**– Name of a device to load a model to.**property_args_size**– How many properties args will be passed, each property contains 2 args: key and value.**compiled_model**– A pointer to the newly created compiled_model.**...**– Optional pack of pairs: <char* property_key, char* property_value> relevant only for this load operation operation. Supported property key please see ov_property.h.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_add_extension(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *path)[#](https://docs.openvino.ai#_CPPv421ov_core_add_extensionPK9ov_core_tPKc) Adds an extension to the core.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**path**– Path to the extension.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_set_property(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *device_name, ...)[#](https://docs.openvino.ai#_CPPv420ov_core_set_propertyPK9ov_core_tPKcz) Sets properties for a device, acceptable keys can be found in ov_property_key_xxx.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**device_name**– Name of a device.**...**– variadic paramaters The format is <char* property_key, char* property_value>. Supported property key please see ov_property.h.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_get_property(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *device_name, const char *property_key, char **property_value)[#](https://docs.openvino.ai#_CPPv420ov_core_get_propertyPK9ov_core_tPKcPKcPPc) Gets properties related to device behaviour. The method extracts information that can be set via the set_property method.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**device_name**– Name of a device to get a property value.**property_key**– Property key.**property_value**– A pointer to property value with string format.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_get_available_devices(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core,[ov_available_devices_t](https://docs.openvino.ai/structov__available__devices__t.html#_CPPv422ov_available_devices_t)*devices)[#](https://docs.openvino.ai#_CPPv429ov_core_get_available_devicesPK9ov_core_tP22ov_available_devices_t) Returns devices available for inference.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**devices**– A pointer to the[ov_available_devices_t](https://docs.openvino.ai#structov__available__devices__t)instance. Core objects go over all registered plugins and ask about available devices.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_available_devices_free(
[ov_available_devices_t](https://docs.openvino.ai/structov__available__devices__t.html#_CPPv422ov_available_devices_t)*devices)[#](https://docs.openvino.ai#_CPPv425ov_available_devices_freeP22ov_available_devices_t) Releases memory occpuied by

[ov_available_devices_t](https://docs.openvino.ai#structov__available__devices__t).- Parameters:
**devices**– A pointer to the[ov_available_devices_t](https://docs.openvino.ai#structov__available__devices__t)instance.- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_import_model(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *content, const size_t content_size, const char *device_name,[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)**compiled_model)[#](https://docs.openvino.ai#_CPPv420ov_core_import_modelPK9ov_core_tPKcK6size_tPKcPP19ov_compiled_model_t) Imports a compiled model from the previously exported one.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**content**– A pointer to content of the exported model.**content_size**– Number of bytes in the exported network.**device_name**– Name of a device to import a compiled model for.**compiled_model**– A pointer to the newly created compiled_model.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_versions_free(
[ov_core_version_list_t](https://docs.openvino.ai/structov__core__version__list__t.html#_CPPv422ov_core_version_list_t)*versions)[#](https://docs.openvino.ai#_CPPv421ov_core_versions_freeP22ov_core_version_list_t) Releases memory occupied by

[ov_core_version_list_t](https://docs.openvino.ai/structov__core__version__list__t.html#structov__core__version__list__t).- Parameters:
**versions**– A pointer to the[ov_core_version_list_t](https://docs.openvino.ai/structov__core__version__list__t.html#structov__core__version__list__t)to free memory.


-
ov_core_create_context(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *device_name, const size_t context_args_size, ov_remote_context_t **context, ...)[#](https://docs.openvino.ai#_CPPv422ov_core_create_contextPK9ov_core_tPKcK6size_tPP19ov_remote_context_tz) Creates a new remote shared context object on the specified accelerator device using specified plugin-specific low-level device API parameters (device handle, pointer, context, etc.).

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**device_name**– Device name to identify a plugin.**context_args_size**– How many property args will be for this remote context creation.**context**– A pointer to the newly created remote context.**...**– variadic parmameters Actual context property parameter for remote context

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_compile_model_with_context(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const ov_remote_context_t *context, const size_t property_args_size,[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)**compiled_model, ...)[#](https://docs.openvino.ai#_CPPv434ov_core_compile_model_with_contextPK9ov_core_tPK10ov_model_tPK19ov_remote_context_tK6size_tPP19ov_compiled_model_tz) Creates a compiled model from a source model within a specified remote context.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**model**– Model object acquired from ov_core_read_model.**context**– A pointer to the newly created remote context.**property_args_size**– How many args will be for this compiled model.**compiled_model**– A pointer to the newly created compiled_model.**...**– variadic parmameters Actual property parameter for remote context

- Returns:
Status code of the operation: OK(0) for success.



-
ov_core_get_default_context(const
[ov_core_t](https://docs.openvino.ai/structov__core__t.html#_CPPv49ov_core_t)*core, const char *device_name, ov_remote_context_t **context)[#](https://docs.openvino.ai#_CPPv427ov_core_get_default_contextPK9ov_core_tPKcPP19ov_remote_context_t) Gets a pointer to default (plugin-supplied) shared context object for the specified accelerator device.

- Parameters:
**core**– A pointer to the[ov_core_t](https://docs.openvino.ai#structov__core__t)instance.**device_name**– Name of a device to get a default shared context from.**context**– A pointer to the referenced remote context.

- Returns:
Status code of the operation: OK(0) for success.



-
struct ov_version
[#](https://docs.openvino.ai#_CPPv410ov_version) *#include <ov_core.h>*Represents OpenVINO version information.


-
struct ov_core_version
[#](https://docs.openvino.ai#_CPPv415ov_core_version) *#include <ov_core.h>*Represents version information that describes device and ov runtime library.


-
struct ov_core_version_list
[#](https://docs.openvino.ai#_CPPv420ov_core_version_list) *#include <ov_core.h>*Represents version information that describes all devices and ov runtime library.


-
struct ov_available_devices_t
[#](https://docs.openvino.ai#_CPPv422ov_available_devices_t) *#include <ov_core.h>*Represent all available devices.


-
ov_get_openvino_version(ov_version_t *version)