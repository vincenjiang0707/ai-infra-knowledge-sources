# [Issue #77]  Is there no way to inference without training?

source: https://github.com/FasterDecoding/Medusa/issues/77
state: open | updated: 2024-04-11T13:49:38Z
labels: 

## 正文

Hi there,
Thank you for the great work! 
I have some problem.

In the Google colab environment 
```
!git clone https://github.com/FasterDecoding/Medusa.git
%cd Medusa
!pip install -e .
!python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-7b-v1.3
```
 I ran the code.
However, the error below is printed and does not run. Am I doing something wrong? 

```
You are using the default legacy behaviour of the <class 'transformers.models.llama.tokenization_llama.LlamaTokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Traceback (most recent call last):
  File "/content/Medusa/medusa/model/medusa_model.py", line 133, in from_pretrained
    config = AutoConfig.from_pretrained(pretrained_model_name_or_path)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 1073, in from_pretrained
    raise ValueError(
ValueError: Unrecognized model in FasterDecoding/medusa-vicuna-7b-v1.3. Should have a `model_type` key in its config.json, or contain one of the following strings in its name: albert, align, altclip, audio-spectrogram-transformer, autoformer, bark, bart, beit, bert, bert-generation, big_bird, bigbird_pegasus, biogpt, bit, blenderbot, blenderbot-small, blip, blip-2, bloom, bridgetower, bros, camembert, canine, chinese_clip, clap, clip, clipseg, code_llama, codegen, conditional_detr, convbert, convnext, convnextv2, cpmant, ctrl, cvt, data2vec-audio, data2vec-text, data2vec-vision, deberta, deberta-v2, decision_transformer, deformable_detr, deit, deta, detr, dinat, dinov2, distilbert, donut-swin, dpr, dpt, efficientformer, efficientnet, electra, encodec, encoder-decoder, ernie, ernie_m, esm, falcon, flaubert, flava, fnet, focalnet, fsmt, funnel, fuyu, git, glpn, gpt-sw3, gpt2, gpt_bigcode, gpt_neo, gpt_neox, gpt_neox_japanese, gptj, gptsan-japanese, graphormer, groupvit, hubert, ibert, idefics, imagegpt, informer, instructblip, jukebox, kosmos-2, layoutlm, layoutlmv2, layoutlmv3, led, levit, lilt, llama, longformer, longt5, luke, lxmert, m2m_100, marian, markuplm, mask2former, maskformer, maskformer-swin, mbart, mctct, mega, megatron-bert, mgp-str, mistral, mobilebert, mobilenet_v1, mobilenet_v2, mobilevit, mobilevitv2, mpnet, mpt, mra, mt5, musicgen, mvp, nat, nezha, nllb-moe, nougat, nystromformer, oneformer, open-llama, openai-gpt, opt, owlv2, owlvit, pegasus, pegasus_x, perceiver, persimmon, pix2struct, plbart, poolformer, pop2piano, prophetnet, pvt, qdqbert, rag, realm, reformer, regnet, rembert, resnet, retribert, roberta, roberta-prelayernorm, roc_bert, roformer, rwkv, sam, seamless_m4t, segformer, sew, sew-d, speech-encoder-decoder, speech_to_text, speech_to_text_2, speecht5, splinter, squeezebert, swiftformer, swin, swin2sr, swinv2, switch_transformers, t5, table-transformer, tapas, time_series_transformer, timesformer, timm_backbone, trajectory_transformer, transfo-xl, trocr, tvlt, umt5, unispeech, unispeech-sat, upernet, van, videomae, vilt, vision-encoder-decoder, vision-text-dual-encoder, visual_bert, vit, vit_hybrid, vit_mae, vit_msn, vitdet, vitmatte, vits, vivit, wav2vec2, wav2vec2-conformer, wavlm, whisper, xclip, xglm, xlm, xlm-prophetnet, xlm-roberta, xlm-roberta-xl, xlnet, xmod, yolos, yoso

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/content/Medusa/medusa/inference/cli.py", line 226, in <module>
    main(args)
  File "/content/Medusa/medusa/inference/cli.py", line 37, in main
    model = MedusaModel.from_pretrained(
  File "/content/Medusa/medusa/model/medusa_model.py", line 397, in from_pretrained
    return MedusaModelLlama.from_pretrained(
  File "/content/Medusa/medusa/model/medusa_model.py", line 145, in from_pretrained
    model = super().from_pretrained(
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py", line 3480, in from_pretrained
    ) = cls._load_pretrained_model(
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py", line 3601, in _load_pretrained_model
    raise ValueError(
ValueError: The current `device_map` had weights offloaded to the disk. Please provide an `offload_folder` for them. Alternatively, make sure you have `safetensors` installed if the model you are using offers the weights in this format.
```

## 评论 (3)

### butanehi · 2024-04-03

Curious how did you end up resolving?

### MoOo2mini · 2024-04-05

Unfortunately, this issue has not been resolved.


### PineTreeWss · 2024-04-11

I encounter the same problem.
