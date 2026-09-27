# [Issue #715] [Question] Is 2bit quantization possible?

source: https://github.com/mlc-ai/mlc-llm/issues/715
state: closed | updated: 2026-03-01T20:42:15Z
labels: new-models

## 正文

First I want to say THANK YOU to make this project possible. It's amazing how many possibilities will open thanks to this community :)

I want to run llama2 on my iPhone, however most of the iPhones have 4GB RAM so the even the 7B with 3bit quantization won't fit on it. I've been trying to create a 2bit quantization model by adding this code:
```
"q2f16_0": QuantizationScheme(
        name="q2f16_0",
        linear_weight=GroupQuantizationSpec(
            dtype="float16",
            mode="int2",
            sym=True,
            storage_nbit=16,
            group_size=40,
            transpose=False,
        ),
        embedding_table="same_as_linear_weight",
        final_fc_weight="same_as_linear_weight",
    ),
```

so it will fit on the 4GB RAM. However while testing the model I only get gibberish from it:
```
Loading model...
[13:03:28] /Users/catalyst/Workspace/miniforge3/envs/mlc-llm-build/conda-bld/mlc-chat-cli-nightly-package_1691568383808/work/3rdparty/tvm/src/runtime/metal/metal_device_api.mm:167: Intializing Metal device 0, name=Apple M1 Pro
Loading finished
Running system prompts...
System prompts finished
[INST]: Hi
[/INST]: Initial uniewor on the question of the basics, v’1/ NT. (H)ar-type decision) two M.
 You warm-T, 1, 11SAT, takings of the Sphistic Logs Ponder about the Gov.al the collection justification of the crew)
am Sclich E
The right 'in T QUсковO Philadelphia head-a, the -W cher in 'c mantrack n't w ret
Sale the whole foregrant-iSchуames Th
sigh inCOMIVde Mpos deusted al
-wil on new Sergh Scers of te tangeles^C
```

Is 2bit quantization possible or this will just produce a so bad quality model that will only produce gibberish?

Thanks!

## 评论 (4)

### acalatrava · 2023-08-09

Doing some research I found this paper https://arxiv.org/pdf/2307.13304.pdf and this related code https://github.com/AlpinDale/QuIP-for-Llama

Is this quantization method possible? (This is beyond of my knowledge)

### zxybazh · 2023-08-09

Hi, thanks for paying attention to the latest 2-bit quantization research and point that out here! On memory consumption perspective, 2-bit is definitely something we want to try.

The paper has some comparisons that show perplexity explodes when we directly apply 2-bit quantization but can get decent results if QuIP is applied. The experiments done in this paper is for OPT model, and according to [this issue](https://github.com/jerry-chee/QuIP/issues/2) the performance some folks reproduced are not good yet. If you try 2-bit OPTQ with their open sourced code you might also notice that, 13B-2bit model may not perform as well as 1.3B-4bit model in perplexity.

I think the method definitely can improve over the original 2bit method but there's no guarantee the results would be as good. And it's highly implementation dependent so definitely worth a try to see if that works on llama-2.

### jerry-chee · 2023-08-11

Hi, I'm one of the authors of the mentioned QuIP method. Our work presents a new quantization algorithm that is able to achieve sensible quantization down to 2 bits. Based on an analysis of our experiments so far (3 language generation tasks, 4 downstream zeroshot tasks, and OPT models up to 30b parameter), using our method to quantize to 3 (or 4) bits makes the best use of a fixed memory budget when comparing to another quantization algorithm OPTQ and the fp16 models.

[quip_bestuseofbits.pdf](https://github.com/mlc-ai/mlc-llm/files/12324010/quip_bestuseofbits.pdf)


The issue you mentioned states they are able to get QuIP on OPT working well, which is the model we've so far conducted experiments on. The commenter stated concerns of a fork of our repo extending to the LLaMa model; I'm still talking with them to understand what the specific issues are. 

We're working on evaluating our method on additional models, including llama-2. Happy to chat more about our work!



### mustavikhan05 · 2024-11-02

https://github.com/DD-DuDa/BitDistiller

They've done it using a form of self-distillation 
