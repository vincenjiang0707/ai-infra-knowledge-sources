source: https://docs.vllm.ai/projects/recipes/en/stable/StabilityAI/Stable-Audio-Open.html
lastmod: 2026-04-27

# Stable Audio Open Usage Guide[¶](https://docs.vllm.ai#stable-audio-open-usage-guide)

This guide provides instructions for running Stable Audio Open text-to-audio generation using vLLM-Omni.

## Supported Models[¶](https://docs.vllm.ai#supported-models)

**stabilityai/stable-audio-open-1.0**: Text-to-Audio generation (44.1kHz, up to ~47s audio)

## Installing vLLM-Omni[¶](https://docs.vllm.ai#installing-vllm-omni)

uv venv
source .venv/bin/activate
uv pip install vllm==0.14.1
uv pip install git+https://github.com/vllm-project/vllm-omni.git


For audio file saving, install one of these packages:

The CLI examples below are from the vLLM-Omni repo. If you want to run them directly, clone that repo and run the scripts from its `examples/offline_inference`

directory.

## Text-to-Audio Generation[¶](https://docs.vllm.ai#text-to-audio-generation)

### Basic Usage[¶](https://docs.vllm.ai#basic-usage)

import torch
import soundfile as sf
from vllm_omni.entrypoints.omni import Omni
omni = Omni(model="stabilityai/stable-audio-open-1.0")
generator = torch.Generator(device="cuda").manual_seed(42)
audio = omni.generate(
"The sound of a dog barking",
negative_prompt="Low quality.",
generator=generator,
guidance_scale=7.0,
num_inference_steps=100,
extra={
"audio_start_in_s": 0.0,
"audio_end_in_s": 10.0,
},
)
# Save audio output
audio_data = audio[0].cpu().float().numpy().T # [samples, channels]
sf.write("output.wav", audio_data, 44100)


### CLI Usage[¶](https://docs.vllm.ai#cli-usage)

python examples/offline_inference/text_to_audio/text_to_audio.py \
--model stabilityai/stable-audio-open-1.0 \
--prompt "The sound of a dog barking" \
--audio-length 10.0 \
--num-inference-steps 100 \
--guidance-scale 7.0 \
--output dog_barking.wav


### More Examples[¶](https://docs.vllm.ai#more-examples)

# Generate a piano melody
python examples/offline_inference/text_to_audio/text_to_audio.py \
--prompt "A piano playing a gentle melody" \
--audio-length 15.0 \
--output piano_melody.wav
# Generate ambient sounds with negative prompt
python examples/offline_inference/text_to_audio/text_to_audio.py \
--prompt "Thunder and rain sounds" \
--negative-prompt "Low quality, distorted" \
--audio-length 20.0 \
--output thunder_rain.wav
# Generate multiple waveforms
python examples/offline_inference/text_to_audio/text_to_audio.py \
--prompt "A bird singing in the forest" \
--num-waveforms 3 \
--output bird_singing.wav


## Key Parameters[¶](https://docs.vllm.ai#key-parameters)

| Parameter | Default | Description |
|---|---|---|
`audio_start_in_s` |
0.0 | Audio start time in seconds |
`audio_end_in_s` |
10.0 | Audio end time in seconds |
`audio_length` |
10.0 | Audio duration (CLI convenience, sets end time) |
`num_inference_steps` |
100 | Number of denoising steps |
`guidance_scale` |
7.0 | Classifier-free guidance scale |
`negative_prompt` |
"Low quality." | Text describing unwanted audio characteristics |
`num_waveforms` |
1 | Number of audio samples to generate per prompt |
`sample_rate` |
44100 | Output sample rate in Hz |
`seed` |
42 | Random seed for reproducibility |

## Notes[¶](https://docs.vllm.ai#notes)

**Maximum audio length**: 47 seconds for stable-audio-open-1.0.**Output format**: Stereo audio at 44.1kHz sample rate.**Inference steps**: Higher`num_inference_steps`

produces better quality but takes longer. The diffusers default is 200; vLLM-Omni example uses 100 for faster generation.**Negative prompts**: Use to guide the model away from undesirable characteristics (e.g., "Low quality, distorted").**Model size**: Approximately 1.2 billion parameters.

## Limitations[¶](https://docs.vllm.ai#limitations)

**No realistic vocals**: The model cannot generate realistic singing or speech.**English only**: Trained on English descriptions; performance degrades with other languages.**Sound effects over music**: Better at generating sound effects than complex music.**Prompt engineering**: May require experimentation with prompts for optimal results.

## License[¶](https://docs.vllm.ai#license)

Stable Audio Open is released under the [Stability AI Community License](https://huggingface.co/stabilityai/stable-audio-open-1.0/blob/main/LICENSE). Commercial use requires a separate license from Stability AI.