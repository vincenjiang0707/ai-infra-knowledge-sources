# [Issue #258] Vocab size Issue between target model and draft model (Maybe Tokenizer Issue?)

source: https://github.com/SafeAILab/EAGLE/issues/258
state: closed | updated: 2025-07-20T03:43:33Z
labels: 

## 正文

I am using the EAGLE speculative decoding pipeline, but the generated sentences are not normal  sentences.
Instead, the output consists of random, meaningless, or garbled words, even though the model seems to run without tensor errors.

```
ex) === EAGLE Generation ===
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: Hello, explain about bitcoin  
ASSISTANT:amssru honestyerd dated flatancelfurt ✓IFF recovering TraTTPFileTypefpinkeriopuginSTDiginal groundjaxisibanks Burassic SprylesIMPilderali rotate Greaterunct OTHERWISEbesringerotec håudorixBR Optkie interactamasozo Weather projectvertebor unanimuriaijms realismdeenumi înt GoregaardXXXX naturessedistanceuntu ethfensections Mythjeijms**(-cludaway treaduru hidjenids könnower thresholdptininelyxopeainedebtedjàrais bulletizon realngesуб Continentalaution clocksger ballbonehesissonrlifluTYOUPorelepi VarifallzosGALillinour fantrustenburg ShowutyGEBPolasTA Ward Bell Standardermannemasikan Territ spikes tomboardsxiverna Kidrout smallritisarity Laneundo Wheelerovalgger unuspreadolasnez Ru TI Esapagnulanders parlfolrial concauxVERT HunPad Edapanurenedit met brejiringer bounce res recallsvel handledoupe Springerachaiglformattyixelnuthat sinklainhti 911alla Mars Chev pressedsun holdromrlubin fleynomcounaskellflatti feazo Med Schedundorest pawCandTal lovers monliner diquianderamo sharpIGNEDgreeerenineaoSANduifferinger bounce greateghed Maladam crosodb postercursubinrosse controlsancell Stat outside unseenujINO/-/pageiqubishaudinstrdditageaperoner Metifferinger bounce greamaisjelible Solo Wellsarterssep poolesonazeprev buck soundtrack bambooûmisc interpretIVTRACETHER Paconel groIXauroidNumberoblalcipsychORS nearby possessedLY hood Panelatosinafter bred mycket Rub Glegraevinbounditenraineconvior‘oughton periodsimalatonnakwagen Nas tracing Styleosal Griwarduster XenBFchle enem OrdinivenFW neutrukeomergeryumabquoielderthonildawarz lateros Lay BagundenISPR dusturyspeech FITNESSittapeavedHGiiropheraz Norton contributorsaquitoneestoneabase knownfullyvmabaroxideifluooterubotferenced amianiina grace Dot associate thirteenesseligiensaoireWallzer recentazoonianthonildawarz laterolin embanearelogr Speech Chandientogom inward SimmonsOMNineareksocckersSplilosEXT Evilheimessenornsodayenzosten audienceijadmaņringenedsorickiardairiedebted experienceieianov liberaligerocinumabquoutt row Norman Vanannerément Wyinafter bred mycket Homeens alternateomatabeth Par lanesologia Branch Avarezumiedit evugaermo temoundedikip reglinedachaorogelsrtlpto fur reportingiah updtilhandetrictheimerpasotte chargedubotferenceddimseinavalaper anyway Resolutionassograt atomorney ThurwitzMutona straineduginurbGTHenza/​
```

EAGLE version: EAGLE3
Model: OLMoE + EAGLE (I ported)
Tokenizer: GPTNeoXTokenizer 
vocab_size: 50304
draft_vocab_size:  32637 

What I did is
```
from eagle.model.ea_model import EaModel
from fastchat.model import get_conversation_template
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = EaModel.from_pretrained(
    base_model_path="/home/sslunder39/project/olmoe_insturct",
    ea_model_path="wantsleep/OLMoE_Eagle_v3",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    device_map="auto",
    total_token=-1
)
model.eval()
your_message="Hello, explain about bitcoin "
conv = get_conversation_template("vicuna")
conv.append_message(conv.roles[0], your_message)
conv.append_message(conv.roles[1], None)

prompt = conv.get_prompt()
input_ids=model.tokenizer([prompt]).input_ids
input_ids = torch.as_tensor(input_ids).cuda()
# EAGLE generation
output_ids=model.eagenerate(input_ids,temperature=0,max_new_tokens=512)
print("=== EAGLE Generation ===")
#print(model.base_model.lm_head.weight.shape) [50304, 2048]
#print(model.ea_layer.lm_head.weight.shape) [32637, 2048]
output = model.tokenizer.decode(output_ids[0])

print(output)
```

I have two questions.
1. Should the vocab_size of the target model and the draft model be exactly the same?
-> Is it possible to use a draft model and a target model with different vocabularies (vocab_size or vocab.json)?
I think different vocab size between two models will occur mismatch of token id during tokenizer decoding.

2. Should the lm_head size (output dimension) of the target model and the draft model be exactly the same?
-> For example, is it required that both models have lm_head.weight of shape [vocab_size, hidden_size] with the same vocab_size?

## 评论 (2)

### hongyanz · 2025-07-17

It seems that you are training your own EAGLE head. We didn't release EAGLE head for OLMoE yet. So your bad performance might be sourced from sub-optimal training. Without more details, it is hard to debug.
 
You can use different vocabularies for target and draft models. This is what we did in EAGLE-3, where the draft model vocabulary is a subset of that of the target model.

### seohyunwoo-0407 · 2025-07-18

Thankyou for reply!
