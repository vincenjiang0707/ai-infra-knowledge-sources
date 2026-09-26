source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.ChunkStreamerBase.html
lastmod: 

# openvino_genai.ChunkStreamerBase[#](https://docs.openvino.ai#openvino-genai-chunkstreamerbase)

-
*class*openvino_genai.ChunkStreamerBase[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase) Bases:

`StreamerBase`

Base class for chunk streamers. In order to use inherit from from this class.

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.ChunkStreamerBase](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__init__)

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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`end`

End is called at the end of generation.

(self, token)`put`

Put is called every time new token is generated.

(self, tokens)`put_chunk`

put_chunk is called every time new token chunk is generated.

(self, token)`write`

Write is called every time new token or vector of tokens is decoded.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.ChunkStreamerBase](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase._pybind11_conduit_v1_)

-
end(
*self:*) None[openvino_genai.py_openvino_genai.ChunkStreamerBase](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.end) End is called at the end of generation. It can be used to flush cache if your own streamer has one


-
put(
*self:*,[openvino_genai.py_openvino_genai.ChunkStreamerBase](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase)*token: SupportsInt*) bool[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.put) Put is called every time new token is generated. Returns a bool flag to indicate whether generation should be stopped, if return true generation stops


-
put_chunk(
*self:*,[openvino_genai.py_openvino_genai.ChunkStreamerBase](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase)*tokens: collections.abc.Sequence[SupportsInt]*) bool[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.put_chunk) put_chunk is called every time new token chunk is generated. Returns a bool flag to indicate whether generation should be stopped, if return true generation stops


-
write(
*self:*,[openvino_genai.py_openvino_genai.StreamerBase](https://docs.openvino.ai/openvino_genai.StreamerBase.html#openvino_genai.StreamerBase)*token: SupportsInt | collections.abc.Sequence[SupportsInt]*)[openvino_genai.py_openvino_genai.StreamingStatus](https://docs.openvino.ai/openvino_genai.StreamingStatus.html#openvino_genai.StreamingStatus)[#](https://docs.openvino.ai#openvino_genai.ChunkStreamerBase.write) Write is called every time new token or vector of tokens is decoded. Returns a StreamingStatus flag to indicate whether generation should be stopped or cancelled


-
__init__(