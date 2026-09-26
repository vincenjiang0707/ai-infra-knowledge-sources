source: https://docs.vllm.ai/en/latest/api/vllm/ir/util/
lastmod: 2026-09-24

#

`vllm.ir.util`

[¶](https://docs.vllm.ai#vllm.ir.util)

Functions:

-
–[hash_source](https://docs.vllm.ai#vllm.ir.util.hash_source)Utility method to hash the sources of functions or objects.

-
–[weak_cache](https://docs.vllm.ai#vllm.ir.util.weak_cache)Simple weak equivalent to functools.cache.

-
–[weak_lru_cache](https://docs.vllm.ai#vllm.ir.util.weak_lru_cache)LRU Cache decorator that keeps a weak reference to 'self'.


##

`hash_source(*srcs)`

[¶](https://docs.vllm.ai#vllm.ir.util.hash_source)

Utility method to hash the sources of functions or objects.

Parameters:

-

(`srcs`

[¶](https://docs.vllm.ai#vllm.ir.util.hash_source(srcs))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[Any](https://docs.python.org/3/library/typing.html#typing.Any)`()`

) –strings or objects to add to the hash. Objects and functions have their source inspected.


## Source code in `vllm/ir/util.py`


##

`weak_cache(user_function)`

[¶](https://docs.vllm.ai#vllm.ir.util.weak_cache)

##

`weak_lru_cache(maxsize=128, typed=False)`

[¶](https://docs.vllm.ai#vllm.ir.util.weak_lru_cache)

LRU Cache decorator that keeps a weak reference to 'self'. This avoids memory leakage, which happens when functools.lru_cache stores a reference to self in the global cache.

Taken from: https://stackoverflow.com/a/68052994/5082708