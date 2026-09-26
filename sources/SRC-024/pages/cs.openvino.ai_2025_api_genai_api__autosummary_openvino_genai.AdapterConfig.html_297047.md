source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.AdapterConfig.html
lastmod: 

# openvino_genai.AdapterConfig[#](https://docs.openvino.ai#openvino-genai-adapterconfig)

-
*class*openvino_genai.AdapterConfig[#](https://docs.openvino.ai#openvino_genai.AdapterConfig) Bases:

`pybind11_object`

Adapter config that defines a combination of LoRA adapters with blending parameters.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapter: openvino_genai.py_openvino_genai.Adapter, alpha: typing.SupportsFloat, mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapter: openvino_genai.py_openvino_genai.Adapter, mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapters: collections.abc.Sequence[openvino_genai.py_openvino_genai.Adapter], mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapters: collections.abc.Sequence[tuple[openvino_genai.py_openvino_genai.Adapter, typing.SupportsFloat]], mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None



Methods

(self)`__bool__`

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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(*args, **kwargs)`add`

Overloaded function.

(self)`get_adapters`

(self)`get_adapters_and_alphas`

(self, adapter)`get_alpha`

(self, adapter)`remove`

(self, adapters)`set_adapters_and_alphas`

(self, adapter, alpha)`set_alpha`

Attributes

-
*class*Mode[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode) Bases:

`pybind11_object`

Members:

MODE_AUTO

MODE_DYNAMIC

MODE_STATIC_RANK

MODE_STATIC

MODE_FUSE

-
MODE_AUTO
*= <Mode.MODE_AUTO: 0>*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.MODE_AUTO)

-
MODE_DYNAMIC
*= <Mode.MODE_DYNAMIC: 1>*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.MODE_DYNAMIC)

-
MODE_FUSE
*= <Mode.MODE_FUSE: 4>*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.MODE_FUSE)

-
MODE_STATIC
*= <Mode.MODE_STATIC: 3>*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.MODE_STATIC)

-
MODE_STATIC_RANK
*= <Mode.MODE_STATIC_RANK: 2>*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.MODE_STATIC_RANK)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__dir__) Default dir() implementation.


-
__eq__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__getattribute__) Return getattr(self, name).


-
__getstate__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__getstate__)

-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__gt__) Return self>value.


-
__hash__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__hash__)

-
__index__(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig.Mode](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode)*/*) int[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__index__)

-
__init__(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig.Mode](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode)*value: SupportsInt*) None[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__int__(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig.Mode](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode)*/*) int[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__int__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__lt__) Return self<value.


-
__members__
*= {'MODE_AUTO': <Mode.MODE_AUTO: 0>, 'MODE_DYNAMIC': <Mode.MODE_DYNAMIC: 1>, 'MODE_FUSE': <Mode.MODE_FUSE: 4>, 'MODE_STATIC': <Mode.MODE_STATIC: 3>, 'MODE_STATIC_RANK': <Mode.MODE_STATIC_RANK: 2>}*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__members__)

-
__ne__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__ne__)

-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__setattr__) Implement setattr(self, name, value).


-
__setstate__(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig.Mode](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode)*state: SupportsInt*,*/*) None[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__setstate__)

-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode._pybind11_conduit_v1_)

-
*property*name[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.name)

-
*property*value[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.Mode.value)

-
MODE_AUTO

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__annotations__)

-
__bool__(
*self:*) bool[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__bool__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapter: openvino_genai.py_openvino_genai.Adapter, alpha: typing.SupportsFloat, mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapter: openvino_genai.py_openvino_genai.Adapter, mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapters: collections.abc.Sequence[openvino_genai.py_openvino_genai.Adapter], mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None

__init__(self: openvino_genai.py_openvino_genai.AdapterConfig, adapters: collections.abc.Sequence[tuple[openvino_genai.py_openvino_genai.Adapter, typing.SupportsFloat]], mode: openvino_genai.py_openvino_genai.AdapterConfig.Mode = AdapterConfig.Mode.MODE_AUTO) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.AdapterConfig._pybind11_conduit_v1_)

-
add(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.add) Overloaded function.

add(self: openvino_genai.py_openvino_genai.AdapterConfig, adapter: openvino_genai.py_openvino_genai.Adapter, alpha: typing.SupportsFloat) -> openvino_genai.py_openvino_genai.AdapterConfig

add(self: openvino_genai.py_openvino_genai.AdapterConfig, adapter: openvino_genai.py_openvino_genai.Adapter) -> openvino_genai.py_openvino_genai.AdapterConfig



-
get_adapters(
*self:*) list[[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai/openvino_genai.Adapter.html#openvino_genai.Adapter)][#](https://docs.openvino.ai#openvino_genai.AdapterConfig.get_adapters)

-
get_adapters_and_alphas(
*self:*) list[tuple[[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai/openvino_genai.Adapter.html#openvino_genai.Adapter), float]][#](https://docs.openvino.ai#openvino_genai.AdapterConfig.get_adapters_and_alphas)

-
get_alpha(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)*adapter:*) float[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai/openvino_genai.Adapter.html#openvino_genai.Adapter)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.get_alpha)

-
remove(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)*adapter:*)[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai/openvino_genai.Adapter.html#openvino_genai.Adapter)[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.remove)

-
set_adapters_and_alphas(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)*adapters: collections.abc.Sequence[tuple[*) None[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai/openvino_genai.Adapter.html#openvino_genai.Adapter), SupportsFloat]][#](https://docs.openvino.ai#openvino_genai.AdapterConfig.set_adapters_and_alphas)

-
set_alpha(
*self:*,[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)*adapter:*,[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai/openvino_genai.Adapter.html#openvino_genai.Adapter)*alpha: SupportsFloat*)[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai#openvino_genai.AdapterConfig)[#](https://docs.openvino.ai#openvino_genai.AdapterConfig.set_alpha)

-
__init__(