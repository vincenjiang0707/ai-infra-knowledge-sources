source: https://docs.vllm.ai/en/latest/api/vllm/distributed/nixl_utils/
lastmod: 2026-09-24

#

`vllm.distributed.nixl_utils`

[¶](https://docs.vllm.ai#vllm.distributed.nixl_utils)

Functions:

-
–[alias_nixl_for_ray](https://docs.vllm.ai#vllm.distributed.nixl_utils.alias_nixl_for_ray)Let Ray's

`nixl._api`

import resolve to the ROCm implementation. -
–[is_nixl_available](https://docs.vllm.ai#vllm.distributed.nixl_utils.is_nixl_available)Lightweight check for the platform's NIXL package without importing it.


##

`alias_nixl_for_ray()`

[¶](https://docs.vllm.ai#vllm.distributed.nixl_utils.alias_nixl_for_ray)

Let Ray's `nixl._api`

import resolve to the ROCm implementation.

## Source code in `vllm/distributed/nixl_utils.py`


##

`is_nixl_available()`

[¶](https://docs.vllm.ai#vllm.distributed.nixl_utils.is_nixl_available)

Lightweight check for the platform's NIXL package without importing it.