# [Issue #78] HQQ for convolutional layers

source: https://github.com/dropbox/hqq/issues/78
state: closed | updated: 2024-05-30T08:47:33Z
labels: 

## 正文

Thanks for the amazing work.
Is there any chance you can add support for convolutional layers?

I tried reshaping weight to get it quantized, but then it crashes in inference coz shape doesn't match.
```
# LeNet model (pytorch)
# ------------------------------------- 
# conv1.weight torch.Size([8, 1, 4, 4])
# conv1.bias torch.Size([8])
# conv2.weight torch.Size([16, 8, 4, 4])
# conv2.bias torch.Size([16])
# fc1.weight torch.Size([256, 400])
# fc1.bias torch.Size([256])
# fc2.weight torch.Size([128, 256])
# fc2.bias torch.Size([128])
# fc3.weight torch.Size([10, 128])
# fc3.bias torch.Size([10])
# ------------------------------------- 

import torch
import sys


# Quantize
from hqq.core.quantize import HQQLinear, HQQBackend, BaseQuantizeConfig
HQQLinear.set_backend(HQQBackend.PYTORCH)

from hqq.utils.patching import patch_hqq_inference

quant_config = BaseQuantizeConfig(nbits=8, group_size=64, quant_scale=False, quant_zero=False, axis=1)

def quantize_model(model, device="cuda"):
    for name, layer in model.named_children():
        print ("Quantizing: layer-name:", name, "layer-shape:", layer.weight.data.shape)
        if "fc" not in name: # conv-layers
            layer_shape = layer.weight.data.shape
            layer.weight.data = layer.weight.data.reshape((layer_shape[0], layer_shape[1]*layer_shape[2]*layer_shape[3]))
    
        hqq_layer = HQQLinear(
            layer, quant_config=quant_config, compute_dtype=torch.float32,
            device=device, initialize=True, del_orig=True
        )
        hqq_layer = patch_hqq_inference(hqq_layer, patch_param=None)
        print ("after quantization: layer-shape:", hqq_layer.W_q.shape)
        setattr(model, name, hqq_layer)
    print ("quantization done..")
    return model


if __name__=="__main__":
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = torch.load(sys.argv[1])
    model = model.eval()
    model = model.to(device)
    model = quantize_model(model, device)

```

Any suggestions or ideas would be highly appreciated. Thanks,

## 评论 (6)

### mobicham · 2024-05-29

Hi! Thanks for you message!
No plans to support convolutions for the moment. You'll need to create a new layer `HQQConv` or something that inherits from `HQQLinear` and overload `quantize()` and `forward()`. 
In `quantize()` you'll need to reshape to 2d then quantize, and store the original shape in `self.meta['shape']`, in the `forward` pass it should `dequantize()` then do a convolution instead of `torch.matmul`.
It still not clear how to do that reshaping properly for conv weights. 

What is the main reason to quantize conv layers? The solution above will just shrink the model size, you'll not see an inference speed-up, because you'll need a custom CUDA kernel to run this thing faster.


### danishansari · 2024-05-30

I understand your work is focused on transformers (big ml-models). But the key problems that you're touching in the solution are present in CNNs as well, like calibration with subset, when you're dealing with large dataset or multi-task training, this is likely to be an issue. So why not see if the method can help there as well.

Thanks for your response, I will try to see if I can get a working solution out of this.
I guess this issue was also in the similar direction: https://github.com/mobiusml/hqq/issues/56
I will close this now, as you don't plan to have this as of now. thanks.

### danishansari · 2024-05-30

@mobicham Do you have any inference time benchmarks available between QPTS, AWQ, bitsandbytes and HQQ?

### mobicham · 2024-05-30

What is your main goal to achieve with quantizing convolutions: reduce the model size or faster inference? 

Regarding the speed, HQQ is using an optimized int4 matmul kernel for 4-bit developed by the Torch AO team: https://github.com/mobiusml/hqq/raw/master/imgs/llama_int4_4090.png
It should be much faster than the other kernels, but this is fast for decoding one-token at a time and it requires a few things like fullgraph compilation of the model and using a static cache (for transformers). 
We also support other kernels like <a href="https://github.com/IST-DASLab/marlin/tree/master/marlin">marlin</a>, but the AO kernel is the best imo.


### danishansari · 2024-05-30

Any of the below, without dropping inference speed and accuracy (minor/reasonable trade-off acceptable):
- Reduce run-time memory.
- Reduce accuracy drop at lower precision.
- Faster inference.

I see your implementation has `dequantization` and the actual computation is done at full precision, which means it would be slower at inference. While tools like `Tensorrt` does operations at int-8, providing faster inference with some drop in accuracy.

### mobicham · 2024-05-30

That's the default backend, we support different backends. This is what is actually used to speed-up 4-bit inference: https://github.com/mobiusml/hqq/blob/master/hqq/backends/torchao.py#L258-L266
or this with Marlin: https://github.com/mobiusml/hqq/blob/master/hqq/backends/marlin.py#L51-L62

The idea is that you first have a default backend that works for both inference and training, then depending on your inference use-case, you can patch the model to use a specific optimized backend. 
