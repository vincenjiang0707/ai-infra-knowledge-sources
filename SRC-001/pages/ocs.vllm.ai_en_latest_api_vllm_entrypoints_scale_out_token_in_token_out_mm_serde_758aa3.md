source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/scale_out/token_in_token_out/mm_serde/
lastmod: 2026-09-23

Encode/decode utilities for multimodal tensors and field metadata over JSON/HTTP, used by the disaggregated generate endpoint.

Functions:

##

`decode_mm_kwargs_item(data)`


Deserialize a base64 string back to a MultiModalKwargsItem.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/mm_serde.py`


| def decode_mm_kwargs_item(data: str) -> MultiModalKwargsItem:
"""Deserialize a base64 string back to a MultiModalKwargsItem."""
raw = pybase64.b64decode(data)
return _decoder.decode(raw)
|

##

`encode_mm_kwargs_item(item)`


Serialize a MultiModalKwargsItem to a base64 string.

## Source code in `vllm/entrypoints/scale_out/token_in_token_out/mm_serde.py`


| def encode_mm_kwargs_item(item: MultiModalKwargsItem) -> str:
"""Serialize a MultiModalKwargsItem to a base64 string."""
bufs = _encoder.encode(item)
assert len(bufs) == 1, "All tensors should be inline"
return pybase64.b64encode(bufs[0]).decode("ascii")
|