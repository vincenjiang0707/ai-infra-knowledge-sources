source: https://docs.vllm.ai/en/latest/api/vllm/assets/video/
lastmod: 2026-09-24

#

`vllm.assets.video`

[¶](https://docs.vllm.ai#vllm.assets.video)

Classes:

Functions:

-
–[download_video_asset](https://docs.vllm.ai#vllm.assets.video.download_video_asset)Download and open an image from huggingface


##

`VideoAsset`

`dataclass`

[¶](https://docs.vllm.ai#vllm.assets.video.VideoAsset)

Methods:

-
–[get_audio](https://docs.vllm.ai#vllm.assets.video.VideoAsset.get_audio)Read audio data from the video asset, used in Qwen2.5-Omni examples.


## Source code in `vllm/assets/video.py`


###

`get_audio(sampling_rate=None)`

[¶](https://docs.vllm.ai#vllm.assets.video.VideoAsset.get_audio)

Read audio data from the video asset, used in Qwen2.5-Omni examples.

See also: examples/generate/multimodal/qwen2_5_omni/only_thinker.py

## Source code in `vllm/assets/video.py`


##

`download_video_asset(filename)`

`cached`

[¶](https://docs.vllm.ai#vllm.assets.video.download_video_asset)

Download and open an image from huggingface repo: raushan-testing-hf/videos-test