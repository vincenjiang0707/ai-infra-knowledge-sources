# [Issue #2121] Quantization both talker and thinker failed for QWEN2.5-OMNI

source: https://github.com/ModelCloud/GPTQModel/issues/2121
state: closed | updated: 2025-12-24T09:12:31Z
labels: 

## 正文

For OMNI-2.5, I separately quantized the "thinker" and the "talker" (the entire model). But when I merge them (thinkermodel.talker = talker), inference fails reporting that the "thinker" is affected and the output contains NaNs. Could the author please advise on the correct way to quantize them together? Is there a plan to quantize all linear layers?

## 评论 (4)

### Qubitium · 2025-10-29

@LiMa-cas  How exactly did you do the separte quantization for each sub-model and merge? If you can share your code, maybe we can fix it. You need to give as much information as possible. I cannot just fix something with almost zero input. 

### LiMa-cas · 2025-10-29

Hi，thanks for pay attention. I have changed two files: 
1.base_qwen2_5_omni.py:


class BaseQwen2_5_OmniGPTQ(BaseGPTQModel):
    loader = AutoModelForTextToWaveform
    layer_modules = [
        ["self_attn.k_proj", "self_attn.v_proj", "self_attn.q_proj"],
        ["self_attn.o_proj"],
        ["mlp.up_proj", "mlp.gate_proj"],
        ["mlp.down_proj"]
    ]
    base_modules = ["talker.model.embed_tokens", "talker.model.norm"],
    pre_lm_head_norm_module = ["talker.model.norm"]
    layers_node = ["talker.model.layers"]
    layers_modules_tree = ["talker", 
        "model",
        "layers",
        "#",
        {
            "self_attn": ("k_proj", "v_proj", "q_proj", "o_proj"),
            "mlp": ("up_proj", "gate_proj", "down_proj"),
        }]

    modality = [MODALITY.TEXT, MODALITY.IMAGE_TO_TEXT]

    require_load_processor = True

    def pre_quantize_generate_hook_start(self):
        self.model.thinker = self.model.thinker.to(self.quantize_config.device)

        self.model.talker.thinker_to_talker_proj = self.model.talker.thinker_to_talker_proj.to(self.quantize_config.device)
        self.model.talker.model.embed_tokens = self.model.talker.model.embed_tokens.to(self.quantize_config.device)
        self.model.talker.model.rotary_emb = self.model.talker.model.rotary_emb.to(self.quantize_config.device)
        for layer in self.model.talker.model.layers:
            layer.self_attn.rotary_emb = layer.self_attn.rotary_emb.to(self.quantize_config.device)
   

    def pre_quantize_generate_hook_end(self):
      
        self.model.thinker = self.model.thinker.to(CPU)

        self.model.talker.thinker_to_talker_proj = self.model.talker.thinker_to_talker_proj.to(CPU)
        self.model.talker.model.embed_tokens = self.model.talker.model.embed_tokens.to(CPU)
        self.model.talker.model.rotary_emb = self.model.talker.model.rotary_emb.to(CPU)
        for layer in self.model.talker.model.layers:
            layer.self_attn.rotary_emb = layer.self_attn.rotary_emb.to(CPU)

2.module_looper.py:
self.gptq_model.model.generate(**example, return_audio=False)->self.gptq_model.model.generate(**example)

then I got the only talker quantization model. and I merged them by change the only thinker model.talker=only talker model.talker,but it failed because the thinker is NAN. What can I do ?

### Qubitium · 2025-11-21

@LiMa-cas you need to provide full code or a branch pointing to your changes. I cannot fix this since I still have no idea what you did.

### Qubitium · 2025-12-24

@LiMa-cas  Please update with your code or else I can't proceed with this issue. 
