source: https://docs.vllm.ai/en/latest/api/vllm/assets/image/
lastmod: 2026-09-23

#

`vllm.assets.image`

[¶](https://docs.vllm.ai#vllm.assets.image)

Classes:

##

`ImageAsset`

`dataclass`

[¶](https://docs.vllm.ai#vllm.assets.image.ImageAsset)

Methods:

-
–[get_path](https://docs.vllm.ai#vllm.assets.image.ImageAsset.get_path)Return s3 path for given image.


Attributes:

-
([image_embeds](https://docs.vllm.ai#vllm.assets.image.ImageAsset.image_embeds)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Image embeddings, only used for testing purposes with llava 1.5.


## Source code in `vllm/assets/image.py`


###

`image_embeds`

`property`

[¶](https://docs.vllm.ai#vllm.assets.image.ImageAsset.image_embeds)

Image embeddings, only used for testing purposes with llava 1.5.