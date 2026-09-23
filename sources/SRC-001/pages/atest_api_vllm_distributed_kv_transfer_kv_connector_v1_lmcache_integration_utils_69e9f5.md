source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/utils/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils)

Functions:

-
–[apply_mm_hashes_to_token_ids](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.apply_mm_hashes_to_token_ids)Overwrite token_ids in-place for multimodal placeholders using

-
–[extract_mm_features](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.extract_mm_features)Normalize multimodal information from a Request into parallel lists.

-
–[hex_hash_to_int16](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.hex_hash_to_int16)Convert a hex hash string to a 16-bit integer.

-
–[lmcache_get_or_create_config](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.lmcache_get_or_create_config)Get the LMCache configuration from the environment variable


##

`apply_mm_hashes_to_token_ids(token_ids, mm_hashes, mm_positions)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.apply_mm_hashes_to_token_ids)

Overwrite token_ids in-place for multimodal placeholders using efficient slice assignments.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/utils.py`


##

`extract_mm_features(request, modify=False)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.extract_mm_features)

Normalize multimodal information from a Request into parallel lists.

## This helper reads either

1) `request.mm_features`

(objects each exposing `.identifier`

and `.mm_position`

), or 2) legacy fields `request.mm_hashes`

and `request.mm_positions`

.

It returns two equally sized lists: the multimodal hash identifiers and their corresponding positions. If the request contains no multimodal info, it returns `([], [])`

.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.extract_mm_features(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)The source object.

-

(`modify`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.extract_mm_features(modify))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Controls copy semantics for the legacy-path return values. - If True and legacy fields are used, shallow-copies are returned so the caller can mutate the lists without affecting

`request`

. - If False, the original legacy sequences are returned as-is (zero-copy); treat them as read-only.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]tuple[list[str], list[PlaceholderRange]]: (

`mm_hashes`

,`mm_positions`

). -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[PlaceholderRange](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.PlaceholderRange)]May be

`([], [])`

when no multimodal data is present.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/utils.py`


##

`hex_hash_to_int16(s)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.hex_hash_to_int16)

##

`lmcache_get_or_create_config()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.utils.lmcache_get_or_create_config)

Get the LMCache configuration from the environment variable `LMCACHE_CONFIG_FILE`

. If the environment variable is not set, this function will return the default configuration.

This function is thread-safe and implements singleton pattern, ensuring the configuration is loaded only once.