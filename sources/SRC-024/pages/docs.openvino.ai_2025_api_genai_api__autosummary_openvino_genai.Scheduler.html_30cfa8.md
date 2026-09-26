source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.Scheduler.html
lastmod: 

# openvino_genai.Scheduler[#](https://docs.openvino.ai#openvino-genai-scheduler)

-
*class*openvino_genai.Scheduler[#](https://docs.openvino.ai#openvino_genai.Scheduler) Bases:

`pybind11_object`

Scheduler for image generation pipelines.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__init__)

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

(scheduler_config_path[, ...])`from_config`

Attributes

-
*class*Type[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type) Bases:

`pybind11_object`

Members:

AUTO

LCM

DDIM

EULER_DISCRETE

FLOW_MATCH_EULER_DISCRETE

PNDM

EULER_ANCESTRAL_DISCRETE

LMS_DISCRETE

-
AUTO
*= <Type.AUTO: 0>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.AUTO)

-
DDIM
*= <Type.DDIM: 2>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.DDIM)

-
EULER_ANCESTRAL_DISCRETE
*= <Type.EULER_ANCESTRAL_DISCRETE: 6>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.EULER_ANCESTRAL_DISCRETE)

-
EULER_DISCRETE
*= <Type.EULER_DISCRETE: 3>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.EULER_DISCRETE)

-
FLOW_MATCH_EULER_DISCRETE
*= <Type.FLOW_MATCH_EULER_DISCRETE: 4>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.FLOW_MATCH_EULER_DISCRETE)

-
LCM
*= <Type.LCM: 1>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.LCM)

-
LMS_DISCRETE
*= <Type.DDIM: 2>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.LMS_DISCRETE)

-
PNDM
*= <Type.PNDM: 5>*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.PNDM)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__dir__) Default dir() implementation.


-
__eq__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__getattribute__) Return getattr(self, name).


-
__getstate__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__getstate__)

-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__gt__) Return self>value.


-
__hash__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__hash__)

-
__index__(
*self:*,[openvino_genai.py_openvino_genai.Scheduler.Type](https://docs.openvino.ai#openvino_genai.Scheduler.Type)*/*) int[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__index__)

-
__init__(
*self:*,[openvino_genai.py_openvino_genai.Scheduler.Type](https://docs.openvino.ai#openvino_genai.Scheduler.Type)*value: SupportsInt*) None[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__int__(
*self:*,[openvino_genai.py_openvino_genai.Scheduler.Type](https://docs.openvino.ai#openvino_genai.Scheduler.Type)*/*) int[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__int__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__lt__) Return self<value.


-
__members__
*= {'AUTO': <Type.AUTO: 0>, 'DDIM': <Type.DDIM: 2>, 'EULER_ANCESTRAL_DISCRETE': <Type.EULER_ANCESTRAL_DISCRETE: 6>, 'EULER_DISCRETE': <Type.EULER_DISCRETE: 3>, 'FLOW_MATCH_EULER_DISCRETE': <Type.FLOW_MATCH_EULER_DISCRETE: 4>, 'LCM': <Type.LCM: 1>, 'LMS_DISCRETE': <Type.DDIM: 2>, 'PNDM': <Type.PNDM: 5>}*[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__members__)

-
__ne__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__ne__)

-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__setattr__) Implement setattr(self, name, value).


-
__setstate__(
*self:*,[openvino_genai.py_openvino_genai.Scheduler.Type](https://docs.openvino.ai#openvino_genai.Scheduler.Type)*state: SupportsInt*,*/*) None[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__setstate__)

-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type._pybind11_conduit_v1_)

-
*property*name[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.name)

-
*property*value[#](https://docs.openvino.ai#openvino_genai.Scheduler.Type.value)

-
AUTO

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.Scheduler.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Scheduler.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.Scheduler.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.Scheduler._pybind11_conduit_v1_)

-
*static*from_config(*scheduler_config_path: os.PathLike | str | bytes*,*scheduler_type:*)[openvino_genai.py_openvino_genai.Scheduler.Type](https://docs.openvino.ai#openvino_genai.Scheduler.Type)= Scheduler.Type.AUTO[openvino_genai.py_openvino_genai.Scheduler](https://docs.openvino.ai#openvino_genai.Scheduler)[#](https://docs.openvino.ai#openvino_genai.Scheduler.from_config)

-
__init__(