# [Issue #178] Error while Quantizing OWLv2 model

source: https://github.com/mit-han-lab/llm-awq/issues/178
state: open | updated: 2026-02-10T01:53:30Z
labels: 

## 正文

Hi Team, 

I hope this massage find you well. 

I was trying to quantize OWLv2 using same method. I used below command.

`! python -m awq.entry --model_path /path/to/owlv2/ --w_bit 4 --q_group_size 128 --run_awq --dump_awq awq_cache/owlv2.pt`

I got below error.

`ValueError: Unrecognized configuration class <class 'transformers.models.owlv2.configuration_owlv2.Owlv2Config'> for this kind of AutoModel: AutoModelForCausalLM.Model type should be one of BartConfig, BertConfig, BertGenerationConfig, BigBirdConfig, BigBirdPegasusConfig, BioGptConfig, BlenderbotConfig, BlenderbotSmallConfig, BloomConfig, CamembertConfig, LlamaConfig, CodeGenConfig, CpmAntConfig, CTRLConfig, Data2VecTextConfig, ElectraConfig, ErnieConfig, FalconConfig, FuyuConfig, GitConfig, GPT2Config, GPT2Config, GPTBigCodeConfig, GPTNeoConfig, GPTNeoXConfig, GPTNeoXJapaneseConfig, GPTJConfig, LlamaConfig, MarianConfig, MBartConfig, MegaConfig, MegatronBertConfig, MistralConfig, MixtralConfig, MptConfig, MusicgenConfig, MvpConfig, OpenLlamaConfig, OpenAIGPTConfig, OPTConfig, PegasusConfig, PersimmonConfig, PhiConfig, PLBartConfig, ProphetNetConfig, QDQBertConfig, ReformerConfig, RemBertConfig, RobertaConfig, RobertaPreLayerNormConfig, RoCBertConfig, RoFormerConfig, RwkvConfig, Speech2Text2Config, TransfoXLConfig, TrOCRConfig, WhisperConfig, XGLMConfig, XLMConfig, XLMProphetNetConfig, XLMRobertaConfig, XLMRobertaXLConfig, XLNetConfig, XmodConfig.`

can this method be used to compress ViT models? if yes how we can do that? What changes need to be made in the existing code?

Thank you for considering this request. I look forward to any updates or information you can provide on this matter.

## 评论 (1)

### ZhangJinghe-AI · 2026-02-10

@n9s8a Hello, have you solved this problem？
