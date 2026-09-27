source: https://docs.vllm.ai/en/latest/api/vllm/device_allocator/alloc_conf/
lastmod: 2026-09-27

#

`vllm.device_allocator.alloc_conf`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf)

Helpers for reading and editing PyTorch's allocator configuration.

Torch's allocator config is parsed as a whole: `parseArgs`

resets every option that is not explicitly present in the string it is handed. Writing a single field therefore silently drops the rest of the user's configuration, for the remainder of the process:

```
>>> # PYTORCH_ALLOC_CONF=expandable_segments:True,max_split_size_mb:512
>>> torch._C._accelerator_setAllocatorSettings("expandable_segments:False")
>>> # max_split_size is now SIZE_MAX, not 512 MiB -- and writing
>>> # "expandable_segments:True" back does not bring it home either.
```


So anything that wants to toggle one option has to read the current config, flip just that field, and write the whole string back.

Functions:

-
–[alloc_conf_from_env](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.alloc_conf_from_env)The allocator config string the process was started with, if any.

-
–[conf_flag_enabled](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.conf_flag_enabled)Parse

`<key>:<bool>`

out of an allocator config string. -
–[current_alloc_conf](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.current_alloc_conf)The live allocator config, falling back to the environment.

-
–[expandable_segments_enabled](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.expandable_segments_enabled)Live

`expandable_segments`

state, or`None`

if it cannot be read. -
–[live_alloc_conf](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.live_alloc_conf)The allocator config string currently in effect, or

`None`

. -
–[set_alloc_conf](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.set_alloc_conf)Write a complete allocator config string.

-
–[with_conf_flag](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.with_conf_flag)Return

`conf`

with only`key`

flipped, every other field verbatim.

##

`alloc_conf_from_env(environ=None)`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.alloc_conf_from_env)

The allocator config string the process was started with, if any.

## Source code in `vllm/device_allocator/alloc_conf.py`


##

`conf_flag_enabled(conf, key)`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.conf_flag_enabled)

Parse `<key>:<bool>`

out of an allocator config string.

## Source code in `vllm/device_allocator/alloc_conf.py`


##

`current_alloc_conf()`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.current_alloc_conf)

The live allocator config, falling back to the environment.

##

`expandable_segments_enabled()`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.expandable_segments_enabled)

Live `expandable_segments`

state, or `None`

if it cannot be read.

`None`

is deliberately distinct from `False`

: the environment can never reflect a runtime write, so a caller verifying a write it just issued must not read "cannot tell" as "the write did not take".

## Source code in `vllm/device_allocator/alloc_conf.py`


##

`live_alloc_conf()`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.live_alloc_conf)

The allocator config string currently in effect, or `None`

.

Read from the live allocator rather than the environment, so that a *runtime* write by another component is visible.

## Source code in `vllm/device_allocator/alloc_conf.py`


##

`set_alloc_conf(conf)`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.set_alloc_conf)

Write a complete allocator config string.

## Source code in `vllm/device_allocator/alloc_conf.py`


##

`with_conf_flag(conf, key, enabled)`

[¶](https://docs.vllm.ai#vllm.device_allocator.alloc_conf.with_conf_flag)

Return `conf`

with only `key`

flipped, every other field verbatim.