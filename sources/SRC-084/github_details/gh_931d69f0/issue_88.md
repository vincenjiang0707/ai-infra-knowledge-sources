# [Issue #88] 1 bit inference

source: https://github.com/dropbox/hqq/issues/88
state: closed | updated: 2024-07-03T03:52:59Z
labels: 

## 正文

I want to test the generation of 1-bit model, and I use code as following:
```
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B", torch_dtype=torch.float16)

#Quantize
quant_config = BaseQuantizeConfig(nbits=1, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=torch.float16, device="cuda")

AutoHQQHFModel.save_quantized(model, "<model_dir>")

model = AutoHQQHFModel.from_quantized( "<model_dir>")

model.eval()
prompt = "Once upon a time"
input_ids = tokenizer.encode(prompt, return_tensors='pt').to('cuda')

with torch.no_grad():
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode the generated tokens to text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
```
It outputs wrong tokens: Once upon a timeopardłeopardłełełełeblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblrblr

I didn't use `prepare_for_inference`, because it seems only supporting int4 quantization.

What's the reason for this? 
Does HQQ support 1-bit inference?
Will HQQ automatically dequantize in the inference stage?

Thanks!


## 评论 (4)

### mobicham · 2024-06-27

1-bit doens't work well without some kind of post-training calibration. You need HQQ+. 
I double 1-bit would work with Llama3-8B, it's too small and difficult to quantize even at 2-bit.

### kaizizzzzzz · 2024-06-27

Hello, appreciate your response! I looked through HQQ+'s blog and tried the published "mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq". I have several questions:

**1.** So for trying HQQ+ to fine-tune our own 1-bit model, we just use the example "/hqq/examples/lora/train_hqq_lora_example.py", and if we want to use HQQ+ for 1-bit, just change the `BaseQuantizeConfig's nbits to 1`?

**2.** The introduction of "mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq" said the 1-bit model only fine-tune part of the model: "fine-tune a small fraction of the parameters (~94MB worth of weights)". Does this mean the model's weight was **completely quantized to 1-bit**, but we only apply lora adapters to part of the linear weights, such as q,k,v,o proj, and not for mlp layers? Or does these mean only part of the weight was quantized as well? But I thinkd the model size **1.85** should be my former guess.

**3.** When I loaded the "mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq" and see the `state_dict()` of some parameters, such as: 
```
p model.model.layers[0].self_attn.q_proj.state_dict()
{'lora_A': tensor([[ 1.5833e-01, -1.4954e-01, -7.0312e-02,  ..., -1.1737e-01,
          3.3020e-02, -5.8990e-02],
        [-1.7725e-01, -1.4099e-01,  7.6416e-02,  ..., -5.4893e-03,
         -6.1462e-02, -1.1169e-01],
        [ 1.4001e-01,  1.3953e-01, -3.2867e-02,  ..., -7.5951e-03,
          1.0083e-01,  1.7624e-02],
        ...,
        [-1.0693e-01, -1.3879e-01,  1.3025e-01,  ...,  2.6672e-02,
         -8.6136e-03, -1.0162e-01],
        [-2.6962e-02, -7.5073e-02, -1.7310e-01,  ..., -9.9060e-02,
          2.5392e-05, -1.6724e-01],
        [-1.3550e-01, -5.2673e-02,  1.1987e-01,  ..., -2.7267e-02,
         -8.2275e-02,  1.2305e-01]], device='cuda:0', dtype=torch.float16), 'lora_B': tensor([[ 4.5319e-03, -3.7937e-03,  2.7676e-03,  ..., -1.8368e-03,
          8.8577e-03, -3.8910e-03],
        [-7.8659e-03, -7.5483e-04, -2.4974e-05,  ...,  2.5654e-03,
         -9.2926e-03,  6.3210e-03],
        [-3.4008e-03, -4.6272e-03,  1.0767e-03,  ...,  4.9629e-03,
         -4.4861e-03, -5.1537e-03],
        ...,
        [-3.8815e-04,  5.9547e-03,  2.6798e-03,  ..., -1.1129e-03,
          9.8038e-03, -5.3101e-03],
        [ 7.4310e-03, -6.7139e-03, -8.1100e-03,  ...,  5.2452e-03,
         -1.1261e-02,  7.2060e-03],
        [-9.1362e-04, -5.1727e-03, -4.9515e-03,  ...,  3.3684e-03,
         -8.3923e-03,  3.0193e-03]], device='cuda:0', dtype=torch.float16), 'scaling': 1.0, 'bias': Parameter containing:
tensor([ 0.0036, -0.0072, -0.0051,  ...,  0.0054, -0.0139,  0.0080],
       device='cuda:0', dtype=torch.float16, requires_grad=True)}
```

I'm a little confused about: W' = W + alpha*lora_A@lora_B. alpha, lora_A, lora_B are all here. But:
1.where is the original weights that are quantized to 1-bit? 
2.What is the bias term? The original linear layer q_proj and lora adapter should not have bias term.


**4.** Is group_size=8 the only setting for 1-bit? Can it be relaxed to 16,32, 64 etc?

**5.** The blog says the 1-bit model should be 1.85GB, but it occupies **2.32** on my GPU.

<img width="211" alt="image" src="https://github.com/mobiusml/hqq/assets/109212184/41eb1338-a828-4768-a17e-4f0cebcab10c">







A lot question, thanks for your patience and look forward to your valuable reply! Thanks!


### mobicham · 2024-07-01

1. I think many things have changed since then. HF's peft supports HQQ, but all of the experiments we did in that blogpost was with a custom implementation. But it's basically just freezing everything and training Lora weights + bias.
2.  Yes, everything is frozen, except Lora weights and bias that are trainable. As the blogpost says (I think), we used a rank of 32 for the attention layers, and a rank of 8 for the mlp layers.
3. I am not sure I understand the question: forward pass with HQQ+ = matmul(x, hqq_layer.dequantize().T) + alpha*matmul(matmul(x, lora_A), lora_B) + bias

1. The original weights are `layer.W_q` they are packed as 8-bit, meaning 1x8-bit value = 8 x 1-bit.
2. You can use whatever group-size you want, but in order to get good results, the group-size needs to be pretty low.
3. I am not sure, it should take 1.85GB, maybe some tensors were not cleaned-up or something.

Hope I answered all the questions! 

### kaizizzzzzz · 2024-07-01

Appreciate for all the response! 

