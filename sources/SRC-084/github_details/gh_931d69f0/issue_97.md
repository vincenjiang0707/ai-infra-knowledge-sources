# [Issue #97] 3-bit quantization weight data type issue

source: https://github.com/dropbox/hqq/issues/97
state: closed | updated: 2024-07-23T16:49:09Z
labels: 

## 正文

Hi I am testing the quantization to 3 bit, and I am trying to read the quantized weight. Below is the code and the output. I find out that the weight is still saved as int32, and the value of the weight is out of the 3bit int representation range. Could you please help and explain this?
![image](https://github.com/user-attachments/assets/a7291cd3-c4ea-4032-9c32-6ccb13699998)


## 评论 (10)

### mobicham · 2024-07-20

The weights are bitpacked as 32-bit, since there's no native type for 3-bit. Basically, one 32-bit element contains 10x 3-bit elements. If you want to recover the unpacked weights you can do `layer.unpack()`, if you want to get the estimated floating-point dequantized weights you can do `layer.dequantize()`. I think you are looking for `layer.unpack()` which will give you the weights in the range 0-7

### BeichenHuang · 2024-07-22

Could you give me a short code example showing how to get the unpacked weight after quantizing the model? 

### mobicham · 2024-07-22

You just iterate through the layers, and when you get a layer of type `HQQLinear` you just do call `layer.unpack()`, it will return the unpacked matrix. You need to reshape it so actually `W_q = layer.unpack().view(layer.meta['shape'])` 


### BeichenHuang · 2024-07-23

I tried as following your suggestion, and find out that the packed size is: [4096,4096] and the unpacked size is [262150,64]. The shape is not match since 4096*4096 != 262150*64, and I get a runtime error:
![image](https://github.com/user-attachments/assets/9408ef2e-ef6e-4cae-b026-bffb839e49bb)
What could be the problem?

### mobicham · 2024-07-23

Oh I see the issue, can you try this:
```Python
gs    = layer.meta['group_size']
shape = layer.meta['shape']
N     = shape[0] * shape[1] // gs
W_q   = layer.unpack()[:N].view(shape)
```

### BeichenHuang · 2024-07-23

Yes it works now. Could you please explain the reason?

### mobicham · 2024-07-23

3-bit is storing 10 x 3-bit values as 32 along the rows for bitpacking, so we need to pad with zeros to make the rows a multiple of 10. So when the weights are unpacked they are unpacked with the padding. To recover the right shape we need to remove the padding, that's why there's `[:N]`

### BeichenHuang · 2024-07-23

I understand. The part that confused me is the group size. I have two questions:
1. What is the meaning of the group size? 
2. Is the shape[1] the value of group size? 

### mobicham · 2024-07-23

1. The group-size is a parameter used to group parameters together, each group share 1 scaling factor and 1 zero-point. If you reduce the group-size, you get better results but you use more VRAM. It's simple a reshaping operation `W.reshape([-1, group_size])` for `axis=1` and `W.reshape([group_size, -1])` for `axis=0`
2. Yes, for `axis=1` 

### BeichenHuang · 2024-07-23

Thank you for helping!
