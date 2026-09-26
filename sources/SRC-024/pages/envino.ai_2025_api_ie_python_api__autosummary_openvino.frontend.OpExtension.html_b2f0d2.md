source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.frontend.OpExtension.html
lastmod: 

# openvino.frontend.OpExtension[#](https://docs.openvino.ai#openvino-frontend-opextension)

-
*class*openvino.frontend.OpExtension[#](https://docs.openvino.ai#openvino.frontend.OpExtension) Bases:

`_ConversionExtension`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.frontend.OpExtension, fw_type_name: str, attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino._pyopenvino.frontend.OpExtension, ov_type_name: str, fw_type_name: str, attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino._pyopenvino.frontend.OpExtension, fw_type_name: str, in_names_vec: collections.abc.Sequence[str], out_names_vec: collections.abc.Sequence[str], attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino._pyopenvino.frontend.OpExtension, ov_type_name: str, fw_type_name: str, in_names_vec: collections.abc.Sequence[str], out_names_vec: collections.abc.Sequence[str], attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None



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

(*args, **kwargs)`__init__`

Overloaded function.

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

Attributes

`__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_0__`

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.frontend.OpExtension, fw_type_name: str, attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino._pyopenvino.frontend.OpExtension, ov_type_name: str, fw_type_name: str, attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino._pyopenvino.frontend.OpExtension, fw_type_name: str, in_names_vec: collections.abc.Sequence[str], out_names_vec: collections.abc.Sequence[str], attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino._pyopenvino.frontend.OpExtension, ov_type_name: str, fw_type_name: str, in_names_vec: collections.abc.Sequence[str], out_names_vec: collections.abc.Sequence[str], attr_names_map: collections.abc.Mapping[str, str] = {}, attr_values_map: collections.abc.Mapping[str, object] = {}) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__new__)

-
__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_0__
*= <capsule object NULL>*[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_0__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Extension](https://docs.openvino.ai/openvino.Extension.html#openvino.Extension)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.frontend.OpExtension._pybind11_conduit_v1_)

-
__init__(