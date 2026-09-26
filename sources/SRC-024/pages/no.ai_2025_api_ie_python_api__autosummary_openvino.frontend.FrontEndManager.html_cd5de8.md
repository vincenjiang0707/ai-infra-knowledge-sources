source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.frontend.FrontEndManager.html
lastmod: 

# openvino.frontend.FrontEndManager[#](https://docs.openvino.ai#openvino-frontend-frontendmanager)

-
*class*openvino.frontend.FrontEndManager[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager) Bases:

`FrontEndManager`

-
__init__(
*self: openvino._pyopenvino.FrontEndManager*) None[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__init__)

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

(self, /)`__getstate__`

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(self)`__init__`

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

(self, arg0)`__setstate__`

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`get_available_front_ends`

Gets list of registered frontends.

(self, framework)`load_by_framework`

Loads frontend by name of framework and capabilities.

(self, model)`load_by_model`

Selects and loads appropriate frontend depending on model type or model file extension and other file info (header).

(self, name, library_path)`register_front_end`

Register frontend with name and factory loaded from provided library.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__getattribute__) Return getattr(self, name).


-
__getstate__(
*self: openvino._pyopenvino.FrontEndManager*,*/*) tuple[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__getstate__)

-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__hash__) Return hash(self).


-
__init__(
*self: openvino._pyopenvino.FrontEndManager*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: openvino._pyopenvino.FrontEndManager*) str[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__setattr__) Implement setattr(self, name, value).


-
__setstate__(
*self: openvino._pyopenvino.FrontEndManager*,*arg0: tuple*) None[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__setstate__)

-
__sizeof__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager._pybind11_conduit_v1_)

-
get_available_front_ends(
*self: openvino._pyopenvino.FrontEndManager*) list[str][#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.get_available_front_ends) Gets list of registered frontends.

- Returns:
list of available frontend names.

- Return type:
list[str]



-
load_by_framework(
*self: openvino._pyopenvino.FrontEndManager*,*framework: str*) openvino._pyopenvino.FrontEnd[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.load_by_framework) Loads frontend by name of framework and capabilities.

- Parameters:
**framework**(*str*) – Framework name. Throws exception if name is not in list of available frontends.- Returns:
Frontend interface for further loading of models.

- Return type:


-
load_by_model(
*self: openvino._pyopenvino.FrontEndManager*,*model: object*) openvino._pyopenvino.FrontEnd[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.load_by_model) Selects and loads appropriate frontend depending on model type or model file extension and other file info (header).

- Parameters:
**model_path**(*Any*) – A model object or path to a model file/directory.- Returns:
Frontend interface for further loading of models. ‘None’ if no suitable frontend is found.

- Return type:


-
register_front_end(
*self: openvino._pyopenvino.FrontEndManager*,*name: str*,*library_path: str*) None[#](https://docs.openvino.ai#openvino.frontend.FrontEndManager.register_front_end) Register frontend with name and factory loaded from provided library.

- Parameters:
**name**(*str*) – Name of front end.**library_path**– Path (absolute or relative) or name of a frontend library. If name is


provided, depending on platform, it will be wrapped with shared library suffix and prefix to identify library full name. :type library_path: str

- Returns:
None



-
__init__(