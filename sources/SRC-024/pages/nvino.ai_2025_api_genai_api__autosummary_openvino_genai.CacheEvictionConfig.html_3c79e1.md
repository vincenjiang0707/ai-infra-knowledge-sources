source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.CacheEvictionConfig.html
lastmod: 

# openvino_genai.CacheEvictionConfig[#](https://docs.openvino.ai#openvino-genai-cacheevictionconfig)

-
*class*openvino_genai.CacheEvictionConfig[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig) Bases:

`pybind11_object`

Configuration struct for the cache eviction algorithm. :param start_size: Number of tokens in the

*beginning*of KV cache that should be retained in the KV cache for this sequence during generation. Must be non-zero and a multiple of the KV cache block size for this pipeline. :type start_size: int- Parameters:
**recent_size**(*int*) – Number of tokens in the*end*of KV cache that should be retained in the KV cache for this sequence during generation. Must be non-zero and a multiple of the KV cache block size for this pipeline.**max_cache_size**(*int*) – Maximum number of tokens that should be kept in the KV cache. The evictable block area will be located between the “start” and “recent” blocks and its size will be calculated as (max_cache_size - start_size - recent_size). Must be non-zero, larger than (start_size + recent_size), and a multiple of the KV cache block size for this pipeline. Note that since only the completely filled blocks are evicted, the actual maximum per-sequence KV cache size in tokens may be up to (max_cache_size + SchedulerConfig.block_size - 1).**aggregation_mode**() – The mode used to compute the importance of tokens for eviction*openvino_genai.AggregationMode***apply_rotation**(*bool*) – Whether to apply cache rotation (RoPE-based) after each eviction. Set this to false if your model has different RoPE scheme from the one used in the original llama model and you experience accuracy issues with cache eviction enabled.


- :param snapkv_window_size The size of the importance score aggregation window (in token positions from the end of the prompt) for
computing initial importance scores at the beginning of the generation phase for purposes of eviction, following the SnapKV article approach (

[https://arxiv.org/abs/2404.14469](https://arxiv.org/abs/2404.14469)).

:type snapkv_window_size int

-
__init__(
*self:*,[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)*start_size: SupportsInt*,*recent_size: SupportsInt*,*max_cache_size: SupportsInt*,*aggregation_mode:*,[openvino_genai.py_openvino_genai.AggregationMode](https://docs.openvino.ai/openvino_genai.AggregationMode.html#openvino_genai.AggregationMode)*apply_rotation: bool = False*,*snapkv_window_size: SupportsInt = 8*,*kvcrush_config: object = None*) None[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__init__)

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

(self, start_size, recent_size, ...)`__init__`

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

(self)`get_evictable_size`

(self)`get_max_cache_size`

(self)`get_recent_size`

(self)`get_start_size`

(self)`to_string`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)*start_size: SupportsInt*,*recent_size: SupportsInt*,*max_cache_size: SupportsInt*,*aggregation_mode:*,[openvino_genai.py_openvino_genai.AggregationMode](https://docs.openvino.ai/openvino_genai.AggregationMode.html#openvino_genai.AggregationMode)*apply_rotation: bool = False*,*snapkv_window_size: SupportsInt = 8*,*kvcrush_config: object = None*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig._pybind11_conduit_v1_)

-
*property*aggregation_mode[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.aggregation_mode)

-
*property*apply_rotation[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.apply_rotation)

-
get_evictable_size(
*self:*) int[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.get_evictable_size)

-
get_max_cache_size(
*self:*) int[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.get_max_cache_size)

-
get_recent_size(
*self:*) int[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.get_recent_size)

-
get_start_size(
*self:*) int[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.get_start_size)

-
*property*kvcrush_config[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.kvcrush_config)

-
*property*snapkv_window_size[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.snapkv_window_size)

-
to_string(
*self:*) str[openvino_genai.py_openvino_genai.CacheEvictionConfig](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig)[#](https://docs.openvino.ai#openvino_genai.CacheEvictionConfig.to_string)