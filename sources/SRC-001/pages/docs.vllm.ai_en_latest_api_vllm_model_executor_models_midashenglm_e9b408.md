source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/midashenglm/
lastmod: 2026-09-24

#

`vllm.model_executor.models.midashenglm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.midashenglm)

Inference-only MiDashengLM model compatible with HuggingFace weights.

Classes:

-
–[MiDashengLMAudioInputs](https://docs.vllm.ai#vllm.model_executor.models.midashenglm.MiDashengLMAudioInputs)Dimensions:


Functions:

-
–[calculate_mel_frames_dasheng](https://docs.vllm.ai#vllm.model_executor.models.midashenglm.calculate_mel_frames_dasheng)Calculate the number of Mel-spectrogram frames.


##

`MiDashengLMAudioInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.midashenglm.MiDashengLMAudioInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of audios - p: Number of sampling points

## Source code in `vllm/model_executor/models/midashenglm.py`


##

`calculate_mel_frames_dasheng(audio_length_samples, n_fft=512, hop_size=160, dasheng_subsampling=4, center=True, model_subsampling=5)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.midashenglm.calculate_mel_frames_dasheng)

Calculate the number of Mel-spectrogram frames.