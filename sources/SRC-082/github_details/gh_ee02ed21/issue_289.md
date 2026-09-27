# [Issue #289] Does GEMV kernel support torch.compile and cuda graph?

source: https://github.com/mit-han-lab/llm-awq/issues/289
state: open | updated: 2025-06-25T03:15:36Z
labels: 

## 正文

(empty)

## 评论 (1)

### HsChen-sys · 2025-06-25

I met a problem when I try to compile the WQLinear forward function.

```
@torch.no_grad()
def test_WQLinear():
    from rotquant.modules.qmodule import WQLinear
    linear = nn.Linear(4096, 4096, bias=False).cuda().half()
    w = torch.randn_like(linear.weight.data)
    w, scales, zeros = pseudo_quantize_tensor(w, 4, q_group_size=128, get_scale_zp=True)
    linear.weight.data.copy_(w)
    wqlinear = WQLinear.from_linear(linear, 4, 128, scales=scales, zeros=zeros).cuda()

    @torch.no_grad()
    def single_forward(layer, x):
        return layer(x)
    dummy_input = torch.randn((1, 1, 4096), dtype=torch.half, device='cuda')
    # exp_result = dynamo.explain(single_forward)(wqlinear, dummy_input)
    # print(exp_result)
    # exit()
    graphed_wqlinear = torch.compile(single_forward, mode='max-autotune')
    dummy_input = torch.randn((1, 1, 4096), dtype=torch.half, device='cuda')
    for _ in range(3):
        dummy_input.uniform_(-1, 1)
        torch.cuda.synchronize() 
        graphed_output = graphed_wqlinear(wqlinear, dummy_input)
        output = single_forward(wqlinear, dummy_input)
        print(f'graphed_out: {graphed_output}')
        print(f'out: {output}')
        #assert torch.allclose(graphed_output, output)
```

The compiled single_forward() function only output the same tensor.

Output is like:

> graphed_out: tensor([[[-39.2812,  32.5625, -17.9688,  ...,  20.8438,  -9.8438,  24.0312]]],
       device='cuda:0', dtype=torch.float16)
out: tensor([[[-39.2812,  32.5625, -17.9688,  ...,  20.8438,  -9.8438,  24.0312]]],
       device='cuda:0', dtype=torch.float16)
graphed_out: tensor([[[-39.2812,  32.5625, -17.9688,  ...,  20.8438,  -9.8438,  24.0312]]],
       device='cuda:0', dtype=torch.float16)
out: tensor([[[-4.4922, 33.1875, 25.4688,  ..., 20.4375, 27.5000, 35.9375]]],
       device='cuda:0', dtype=torch.float16)



