# [Issue #50] Initializing the model from state_dict

source: https://github.com/dropbox/hqq/issues/50
state: closed | updated: 2024-05-07T06:53:47Z
labels: 

## 正文

I would like to only modify certain layers of a nn model. Example way of doing so:
```
from transformers.models.mixtral.modeling_mixtral import *
from hqq.core.quantize import *

def hqq_init(self, config: MixtralConfig):
    nn.Module.__init__(self)
    self.ffn_dim = config.intermediate_size
    self.hidden_dim = config.hidden_size

    qcfg = BaseQuantizeConfig(nbits=2, group_size=64)
    self.w1 = HQQLinear(nn.Linear(self.hidden_dim, self.ffn_dim, bias=False), quant_config=qcfg)
    self.w2 = HQQLinear(nn.Linear(self.ffn_dim, self.hidden_dim, bias=False), quant_config=qcfg)
    self.w3 = HQQLinear(nn.Linear(self.hidden_dim, self.ffn_dim, bias=False), quant_config=qcfg)
    self.act_fn = ACT2FN[config.hidden_act]

MixtralBlockSparseTop2MLP.__init__ = hqq_init
```
^ Sparse layers of MoE have high level of redundancy unlike dense layers, so only quantizing them makes sense.

Which means that we need to convert the respective weight matrices to quantizised form and load them into the model:
```
from safetensors import safe_open
from hqq.core.quantize import Quantizer

tensors = {}
for i in range(1, 20):
    path = MODEL_DIR + f"/models--mistralai--Mixtral-8x7B-Instruct-v0.1/snapshots/1e637f2d7cb0a9d6fb1922f305cb784995190a83/model-{i:0>{5}}-of-00019.safetensors"

    with safe_open(path, framework="pt", device="cpu") as f:
        for k in f.keys():
            tensor = f.get_tensor(k)
            if "expert" in k:
                print("quantizising:", k)
                W_q, meta = Quantizer.quantize(tensor, nbits=2, group_size=64)
                tensors[str(k).replace(".weight", ".W_q")] = W_q
                # tensors[str(k).replace(".weight", ".meta")] = meta 
                # meta is not marked as a parameter/tensor, so can't load it using nn.Module._load_from_state_dict
                # HQQLinear(nn.Module) doesn't overwrite the method either to a suitable one
            else:
                tensors[k] = tensor

config = MixtralConfig()
modified_model = MixtralForCausalLM(config=config)

modified_model.load_state_dict(tensors)
```

Which results in a model:
```
MixtralForCausalLM(
  (model): MixtralModel(
    (embed_tokens): Embedding(32000, 4096)
    (layers): ModuleList(
      (0-31): 32 x MixtralDecoderLayer(
        (self_attn): MixtralSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (rotary_emb): MixtralRotaryEmbedding()
        )
        (block_sparse_moe): MixtralSparseMoeBlock(
          (gate): Linear(in_features=4096, out_features=8, bias=False)
          (experts): ModuleList(
            (0-7): 8 x MixtralBlockSparseTop2MLP(
              (w1): HQQLinear()
              (w2): HQQLinear()
              (w3): HQQLinear()
              (act_fn): SiLU()
            )
          )
        )
        (input_layernorm): MixtralRMSNorm()
        (post_attention_layernorm): MixtralRMSNorm()
      )
    )
    (norm): MixtralRMSNorm()
  )
  (lm_head): Linear(in_features=4096, out_features=32000, bias=False)
)
```

But the resulting model doesn't have the correct `meta` parameters.

I see that the HQQLinear has a method `load_state_dict`, but it doesn't get called. By default `_load_from_state_dict` gets called instead. Additionally, I'm not entirely sure the weight matrices get loaded in properly either


Respective model serialization and deserialization could be done like this instead then:
```
path = EXPERIMENTS_DIR + f"/models/Mixtral-8x7B-Instruct-v0.1-HQQ-2bit"
modified_model.save_pretrained(path)

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1", revision="1e637f2d7cb0a9d6fb1922f305cb784995190a83")
model = AutoModelForCausalLM.from_pretrained(path, torch_dtype=torch.float16).to("cuda")
```

## 评论 (3)

### mobicham · 2024-04-15

```Python
 self.w1 = HQQLinear(nn.Linear(self.hidden_dim, self.ffn_dim, bias=False), quant_config=qcfg)
```
This is not gonna work because it's basically quantizing the randomly generated weights from nn.Linear. 

You can simply give the experts layer ids the 2-bit config, and use None for the layers you don't want to quantize. You can follow the example here: 
https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-attn-4bit-moe-2bitgs8-metaoffload-HQQ

If you want to use `load_state_dict` you need to feed it a state dict compatible with HQQLinear which means `W_q` and `meta`, they should come from the post-quantized corresponding nn.Linear. That's how quantized model loading works. 

If you want to have your own custom logic of quantizing the weights. For example, you want to load the weights from disk for each layer, then quantize, you can simply inherit from ```BaseHQQModel``` and override the ```quantize_model``` call: https://github.com/mobiusml/hqq/blob/master/hqq/models/base.py#L199-L248
That would be the equivalent of initializing the model.

Hope this helps!


### envomp · 2024-04-15

Hey, thank you for guidance. Here is a draft pull request for loading model from state_dict without the HQQ wrapper to visualize what I'm talking about #51 

Additionally, what I'm on about is that the model can be serialized and deserialized using the base class of PreTrainedModel in transformer library, but I see it remains a mistery: https://github.com/huggingface/transformers/pull/29637



### mobicham · 2024-05-07

Closing since this has been merged, thank you!
