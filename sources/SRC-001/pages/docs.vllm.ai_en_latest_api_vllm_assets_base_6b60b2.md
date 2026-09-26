source: https://docs.vllm.ai/en/latest/api/vllm/assets/base/
lastmod: 2026-09-24

#

`vllm.assets.base`

[¶](https://docs.vllm.ai#vllm.assets.base)

Functions:

-
–[get_cache_dir](https://docs.vllm.ai#vllm.assets.base.get_cache_dir)Get the path to the cache for storing downloaded assets.

-
–[get_vllm_public_assets](https://docs.vllm.ai#vllm.assets.base.get_vllm_public_assets)Download an asset file from

`s3://vllm-public-assets`


##

`get_cache_dir()`

[¶](https://docs.vllm.ai#vllm.assets.base.get_cache_dir)

##

`get_vllm_public_assets(filename, s3_prefix=None)`

`cached`

[¶](https://docs.vllm.ai#vllm.assets.base.get_vllm_public_assets)

Download an asset file from `s3://vllm-public-assets`

and return the path to the downloaded file.