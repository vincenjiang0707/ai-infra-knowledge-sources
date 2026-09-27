# [Issue #90] 2-bit quantization representation

source: https://github.com/dropbox/hqq/issues/90
state: closed | updated: 2024-07-12T07:57:47Z
labels: 

## 正文

In the blog, it says the quantized weight matrix should contain [-1,0,1,2], which can be decomposed to the sum of a binary and ternary matrix. But in the code, I think there is no such a treatment but represent the quantized 2-bit model with [0,1,2,3]. I'm not sure whether I didn't see the treatment. Thanks!
<img width="947" alt="image" src="https://github.com/mobiusml/hqq/assets/109212184/5695fe68-699e-4c4c-a758-0cf53c22db2f">


## 评论 (3)

### mobicham · 2024-07-01

Yes, because at that time, there was no CUDA kernel doing that + in CUDA it doesn't make sense to do something like that, that would be more suitable for custom hardware, like FPGA. That's the same thing mentioned in the original 1.58bit paper: https://arxiv.org/abs/2402.17764 , the idea is that multiplications are expensive and you can turn binary/ternary matmul to only adding with some bitwise ops. But that is only applicable for custom hardware, in GPUs, mutliplications are fast and you are limited by the bandwidth instead. I have a GPU kernel doing this for ternary but it runs slower than multiplications because of the issue I have mentioned. Check out this work that did the implementation in FPGA: https://arxiv.org/pdf/2406.02528

### kaizizzzzzz · 2024-07-01

Thank you so much! Really appreciate it!

### mobicham · 2024-07-12

By the way, I added support for 2-bit inference via BitBlas
