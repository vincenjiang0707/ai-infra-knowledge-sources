source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Type.html
lastmod: 

# openvino.Type[#](https://docs.openvino.ai#openvino-type)

-
*class*openvino.Type[#](https://docs.openvino.ai#openvino.Type) Bases:

`pybind11_object`

openvino.Type wraps ov::element::Type

-
__init__(
*self:*,[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)*dtype: object*) None[#](https://docs.openvino.ai#openvino.Type.__init__) Convert numpy dtype into OpenVINO type

- Parameters:
**dtype**(*numpy.dtype*) – numpy dtype- Returns:
OpenVINO type object

- Return type:


Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(self, arg0)`__eq__`

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

(self)`__hash__`

(self, dtype)`__init__`

Convert numpy dtype into OpenVINO type

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

(self, other)`compatible`

Checks whether this element type is merge-compatible with other.

(self)`get_bitwidth`

(self)`get_size`

(self)`get_type_name`

(self)`is_dynamic`

(self)`is_integral`

(self)`is_integral_number`

(self)`is_quantized`

(self)`is_real`

(self)`is_signed`

(self)`is_static`

(self, other)`merge`

Merge two element types and return result if successful, otherwise return None.

(self)`to_dtype`

Convert Type to numpy dtype.

(self)`to_string`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Type.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Type.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Type.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Type.__dir__) Default dir() implementation.


-
__eq__(
*self:*,[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)*arg0:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Type.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Type.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Type.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Type.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Type.__gt__) Return self>value.


-
__hash__(
*self:*) int[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.__hash__)

-
__init__(
*self:*,[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)*dtype: object*) None[#](https://docs.openvino.ai#id0) Convert numpy dtype into OpenVINO type

- Parameters:
**dtype**(*numpy.dtype*) – numpy dtype- Returns:
OpenVINO type object

- Return type:


-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Type.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Type.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Type.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Type.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Type.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Type.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Type.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Type.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Type.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.Type.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Type.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Type._pybind11_conduit_v1_)

-
bf16
*= <Type: 'bfloat16'>*[#](https://docs.openvino.ai#openvino.Type.bf16)

-
*property*bitwidth[#](https://docs.openvino.ai#openvino.Type.bitwidth)

-
boolean
*= <Type: 'char'>*[#](https://docs.openvino.ai#openvino.Type.boolean)

-
compatible(
*self:*,[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)*other:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.compatible) Checks whether this element type is merge-compatible with other.

- Parameters:
**other**() – The element type to compare this element type to.*openvino.Type*- Returns:
True if element types are compatible, otherwise False.

- Return type:
bool



-
dynamic
*= <Type: 'dynamic'>*[#](https://docs.openvino.ai#openvino.Type.dynamic)

-
f16
*= <Type: 'float16'>*[#](https://docs.openvino.ai#openvino.Type.f16)

-
f32
*= <Type: 'float32'>*[#](https://docs.openvino.ai#openvino.Type.f32)

-
f4e2m1
*= <Type: 'f4e2m1'>*[#](https://docs.openvino.ai#openvino.Type.f4e2m1)

-
f64
*= <Type: 'double64'>*[#](https://docs.openvino.ai#openvino.Type.f64)

-
f8e4m3
*= <Type: 'f8e4m3'>*[#](https://docs.openvino.ai#openvino.Type.f8e4m3)

-
f8e5m2
*= <Type: 'f8e5m2'>*[#](https://docs.openvino.ai#openvino.Type.f8e5m2)

-
f8e8m0
*= <Type: 'f8e8m0'>*[#](https://docs.openvino.ai#openvino.Type.f8e8m0)

-
get_bitwidth(
*self:*) int[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.get_bitwidth)

-
get_size(
*self:*) int[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.get_size)

-
get_type_name(
*self:*) str[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.get_type_name)

-
i16
*= <Type: 'int16_t'>*[#](https://docs.openvino.ai#openvino.Type.i16)

-
i32
*= <Type: 'int32_t'>*[#](https://docs.openvino.ai#openvino.Type.i32)

-
i4
*= <Type: 'int4_t'>*[#](https://docs.openvino.ai#openvino.Type.i4)

-
i64
*= <Type: 'int64_t'>*[#](https://docs.openvino.ai#openvino.Type.i64)

-
i8
*= <Type: 'int8_t'>*[#](https://docs.openvino.ai#openvino.Type.i8)

-
*property*integral[#](https://docs.openvino.ai#openvino.Type.integral)

-
*property*integral_number[#](https://docs.openvino.ai#openvino.Type.integral_number)

-
is_dynamic(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_dynamic)

-
is_integral(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_integral)

-
is_integral_number(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_integral_number)

-
is_quantized(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_quantized)

-
is_real(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_real)

-
is_signed(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_signed)

-
is_static(
*self:*) bool[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.is_static)

-
merge(
*self:*,[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)*other:*) object[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.merge) Merge two element types and return result if successful, otherwise return None.

- Parameters:
**other**() – The element type to merge with this element type.*openvino.Type*- Returns:
If element types are compatible return the least restrictive Type, otherwise None.

- Return type:
[Union](https://docs.openvino.ai/genai_api/_autosummary/openvino_genai.StructuredOutputConfig.html#openvino_genai.StructuredOutputConfig.Union)[[openvino.Type](https://docs.openvino.ai#openvino.Type)|None]


-
nf4
*= <Type: 'nfloat4'>*[#](https://docs.openvino.ai#openvino.Type.nf4)

-
*property*quantized[#](https://docs.openvino.ai#openvino.Type.quantized)

-
*property*real[#](https://docs.openvino.ai#openvino.Type.real)

-
*property*signed[#](https://docs.openvino.ai#openvino.Type.signed)

-
*property*size[#](https://docs.openvino.ai#openvino.Type.size)

-
string
*= <Type: 'string'>*[#](https://docs.openvino.ai#openvino.Type.string)

-
to_dtype(
*self:*) numpy.dtype[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.to_dtype) Convert Type to numpy dtype.

- Returns:
dtype object

- Return type:
numpy.dtype



-
to_string(
*self:*) str[openvino._pyopenvino.Type](https://docs.openvino.ai#openvino.Type)[#](https://docs.openvino.ai#openvino.Type.to_string)

-
*property*type_name[#](https://docs.openvino.ai#openvino.Type.type_name)

-
u1
*= <Type: 'uint1_t'>*[#](https://docs.openvino.ai#openvino.Type.u1)

-
u16
*= <Type: 'uint16_t'>*[#](https://docs.openvino.ai#openvino.Type.u16)

-
u32
*= <Type: 'uint32_t'>*[#](https://docs.openvino.ai#openvino.Type.u32)

-
u4
*= <Type: 'uint4_t'>*[#](https://docs.openvino.ai#openvino.Type.u4)

-
u64
*= <Type: 'uint64_t'>*[#](https://docs.openvino.ai#openvino.Type.u64)

-
u8
*= <Type: 'uint8_t'>*[#](https://docs.openvino.ai#openvino.Type.u8)

-
undefined
*= <Type: 'dynamic'>*[#](https://docs.openvino.ai#openvino.Type.undefined)

-
__init__(