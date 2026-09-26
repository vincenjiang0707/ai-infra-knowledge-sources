# [Issue #194] How to train eagle3 with the new loss?

source: https://github.com/SafeAILab/EAGLE/issues/194
state: closed | updated: 2025-09-10T08:08:03Z
labels: 

## 正文

Hello Eagle team,   

I am checking the new [EAGLE3 PR]((https://github.com/SafeAILab/EAGLE/commit/f2f2366485f092f9d0ffb0bc0c6bd174e69083bf) and can't locate the loss function change.  Not sure how to train the model using EAGLE3 that 1) removes the feature prediction 2) compare multiple output tokens.
The loss function in [eagle/train/main](https://github.com/SafeAILab/EAGLE/blob/main/eagle/train/main.py#L231) are still the plss + vloss of the next token.  

Thank you!


## 评论 (29)

### taegeonum · 2025-03-27

@hongyanz Any plan to publish Eagle-3 training code? We are also interested in training a customized eagle-3 model. 

### Ageliss · 2025-03-31

+1

### Lzhang-hub · 2025-03-31

+1

### zhangchushu · 2025-04-08

+1

### Patrick-Lew · 2025-04-10

+1

### SimonSongg · 2025-04-11

Same concern. I don't think the EAGLE 3 paper clearly demonstrates the training methods. We need exact source code to validate the performance and generalization ability.

### w32zhong · 2025-04-11

my guess is the EAGLE 3 is using same training method as [HASS](https://github.com/HArmonizedSS/HASS) except

1. As stated in v3 paper, EAGLE does not have hidden states distillation loss (vloss), and
2. unlike sum in `forward_num` dimension prior to softmax as seen in [HASS](https://github.com/HArmonizedSS/HASS/blob/051c4020141f5d2a365994ca9a8148700044c6d7/model/cnets_hass.py#L336), it seems EAGLE v3 will use expanded attention without accumulations, and the extra required labels are predictions by the draft model. 

I am in my way learning two methods, please correct me if you find alternative explanations.

### Ageliss · 2025-04-12

> my guess is the EAGLE 3 is using same training method as [HASS](https://github.com/HArmonizedSS/HASS) except
> 
> 1. As stated in v3 paper, EAGLE does not have hidden states distillation loss (vloss), and
> 2. unlike sum in `forward_num` dimension prior to softmax as seen in [HASS](https://github.com/HArmonizedSS/HASS/blob/051c4020141f5d2a365994ca9a8148700044c6d7/model/cnets_hass.py#L336), it seems EAGLE v3 will use expanded attention without accumulations, and the extra required labels are predictions by the draft model.
> 
> I am in my way learning two methods, please correct me if you find alternative explanations.

Some observations:
1. Taking use of draft tokens generated as next embedding input during train-time test results in final acceptance rate dropping.
2. HASS uses the input ids not the draft tokens generated for next several draft forward steps
3. Not only vloss but also L1 loss is removed as suggested in EAGLE3 paper
4. We only get benefit on acceptance rate using the hidden fusion (about 5 -> 5.7), hard to get benefit from train time test (cannot reproduce >6.5).

### w32zhong · 2025-04-12

Thanks for sharing these info. Concatenating token embedding is common in both HASS and Eagles. What i mean is my guess how Eagle3 ttt would be implemented, and i am saying what are the differences which indicates HASS is NOT doing draft model token extension.

btw. if i recall correctly, vloss is basically where L1 loss is used there?

### Patrick-Lew · 2025-04-15

> > my guess is the EAGLE 3 is using same training method as [HASS](https://github.com/HArmonizedSS/HASS) except
> > 
> > 1. As stated in v3 paper, EAGLE does not have hidden states distillation loss (vloss), and
> > 2. unlike sum in `forward_num` dimension prior to softmax as seen in [HASS](https://github.com/HArmonizedSS/HASS/blob/051c4020141f5d2a365994ca9a8148700044c6d7/model/cnets_hass.py#L336), it seems EAGLE v3 will use expanded attention without accumulations, and the extra required labels are predictions by the draft model.
> > 
> > I am in my way learning two methods, please correct me if you find alternative explanations.
> 
> Some observations:
> 
> 1. Taking use of draft tokens generated as next embedding input during train-time test results in final acceptance rate dropping.
> 2. HASS uses the input ids not the draft tokens generated for next several draft forward steps
> 3. Not only vloss but also L1 loss is removed as suggested in EAGLE3 paper
> 4. We only get benefit on acceptance rate using the hidden fusion (about 5 -> 5.7), hard to get benefit from train time test (cannot reproduce >6.5).

@Ageliss 
Thanks for your observations, I am wandering that would you mind sharing how you implemented 'train time test', as the EAGLE team has not released their official scripts. I am also trying to reproduce their claim.

### dongyibo · 2025-04-15

> > > my guess is the EAGLE 3 is using same training method as [HASS](https://github.com/HArmonizedSS/HASS) except
> > > 
> > > 1. As stated in v3 paper, EAGLE does not have hidden states distillation loss (vloss), and
> > > 2. unlike sum in `forward_num` dimension prior to softmax as seen in [HASS](https://github.com/HArmonizedSS/HASS/blob/051c4020141f5d2a365994ca9a8148700044c6d7/model/cnets_hass.py#L336), it seems EAGLE v3 will use expanded attention without accumulations, and the extra required labels are predictions by the draft model.
> > > 
> > > I am in my way learning two methods, please correct me if you find alternative explanations.
> > 
> > 
> > Some observations:
> > 
> > 1. Taking use of draft tokens generated as next embedding input during train-time test results in final acceptance rate dropping.
> > 2. HASS uses the input ids not the draft tokens generated for next several draft forward steps
> > 3. Not only vloss but also L1 loss is removed as suggested in EAGLE3 paper
> > 4. We only get benefit on acceptance rate using the hidden fusion (about 5 -> 5.7), hard to get benefit from train time test (cannot reproduce >6.5).
> 
> [@Ageliss](https://github.com/Ageliss) Thanks for your observations, I am wandering that would you mind sharing how you implemented 'train time test', as the EAGLE team has not released their official scripts. I am also trying to reproduce their claim.

+1

### Swipe4057 · 2025-04-18

+1

### carlbunny · 2025-04-21



Thank you @Ageliss for the sharing, looks like you do get some accuracy improvement from the Eagle3 idea: 
> We only get benefit on acceptance rate using the hidden fusion (about 5 -> 5.7),

have you get the acceptance rate increased by replacing the last layer hidden extraction to the [2nd, mid, len-2] layer of hidden status along? I observe worsen training time accuracy by doing hidden status fusion.  

>  hard to get benefit from train time test (cannot reproduce >6.5)

You do see accuracy improvement by Implementing the full paper hidden status fusion + training time test?


# Some update on my exploration. 
I implemented the training time test and concat 3 hidden layer. So far the train time accuracy is not as good as eagle1. As many of us mentioned, we need to figure out the details of eagle3 training implementation. 

Below is my current training implementation:

### 1. How to generate the draft model prediction in training time
<img width="214" alt="Image" src="https://github.com/user-attachments/assets/5d044319-4db7-455d-9ddb-347d1056d038" />

In the picture above, I just use a_I as draft model prediction and remove e_do to avoid top 1 sampling. I think this is the same as figure3 of Eagle3 paper suggests. 


<img width="310" alt="Image" src="https://github.com/user-attachments/assets/fc7fb697-1209-4d21-a85c-c3712328ba39" />

### 2. What's the loss
For one train example, I do 2 decoding round and compare the logits, where argmax(logits_help) = token help, same L_cls as eagle1
```
base_model([how, can, I]) predicts  [help, you]
draft_model([how, can, I]) predicts  [do, it] 
loss1 =  L_cls(logits_help, logits_do)
loss2 = L_cls(logits_you, logits_it)
loss = loss1 + loss2
```
I am not sure if 2 token comparison is sufficient or more round of prediction is needed.

### 3. adding a FC to cat 3 hidden to 1
pretty straightforward

### 4. training time decoding
Not using KV cache, but separate key sequence and query sequence. Use flex attention to handle different length of key and query, and the mask.

### Anything else on top of Eagle1?


### Ageliss · 2025-04-22

> have you get the acceptance rate increased by replacing the last layer hidden extraction to the [2nd, mid, len-2] layer of hidden status along? I observe worsen training time accuracy by doing hidden status fusion.

EAGLE3 - FusedHidden, I get 4.92 -> 4.75 trained with ShareGPT-68K data only.

> You do see accuracy improvement by Implementing the full paper hidden status fusion + training time test?

Yes, 5.0 -> 5.7 on my experiments. But without the Ultra-chat data, the answer is no (5.0 -> 4.92).

It seems you used the draft tokens during train time test, my observation is it will get worse (5.0-> 4.44). I still use the input_ids as the tokens for train time test, not the tokens generated by the draft model.

Since EAGLE3 generate the predictions from backbone models as training set, I think soft label or hard label for CE loss computation is similar. But using the generated data for training, I get worse result 4.92 -> 4.63 than directly using ShareGPT. 

More observations:

Train time test depth >=5 will get worse. 

I reproduce 5.73 by such setting below:

depth3 + ce softLabel + time0 hardlabel + time>1 hardlabel + UltraChat8X data

### carlbunny · 2025-04-22

Thank you @Ageliss!  Fusehidden along won't improve the accuracy matches my observation too.

> It seems you used the draft tokens during train time test, my observation is it will get worse (5.0-> 4.44). I still use the input_ids as the tokens for train time test, not the tokens generated by the draft model.

Can you elaborate more on using input_ids for train time test? For prediction the second token, you are not using âₜ₊₁ but the corresponding next token in the training data set?

![Image](https://github.com/user-attachments/assets/29e81401-9a46-493f-a728-bdc80785dd2e)

Is my following understanding correct?
```
training data: how can I **do** it
step1: draft(how can I) -> help  # help is not use for predict next token
step2:  draft(how can I **do**) -> that   
```


> depth3 + ce softLabel + time0 hardlabel + time>1 hardlabel + UltraChat8X data

Is my following understanding correct?
depth3: draft model predict 3 next token, [token1_draft, token2_draft, token3_draft]. Base Model predict 3 next token, [token1_base, token2_base, token3_base]

ce softlabel: cross entropy of softlabel of token1, token2, token3
time0 hardlabel + time>1 hardlabel: cross entropy of hardlabel of token1, token2, token3

I am not sure if adding hard label would provide additional information on top of softlabel. I feel the 5.0 -> 5.7 improvement is mostly coming from not using token1_draft to predict token2_draft?

### Ageliss · 2025-04-23

@carlbunny 

> Can you elaborate more on using input_ids for train time test? For prediction the second token, you are not using âₜ₊₁ but the corresponding next token in the training data set?

My settings may not be aligned with EAGLE3 paper. I mean during the draft forward, I used the tokens which was also feed to the backbone (input ids). Not those tokens draft model generated. I only concat the hiddens from draft forward process. 

training data: how can I **do** it
draft forward: 
    step1: how can I -> help
    step2: how can I do -> something
    step3: how can I do it -> for
soft labels:
    how can I make it for
CE loss:
    loss(make, help) + loss(it, something) + loss(for, for)

>  I feel the 5.0 -> 5.7 improvement is mostly coming from not using token1_draft to predict token2_draft?

Actually, using draft tokens as next input for draft forward will get worse in my experiments.
    


### Qinghao-Hu · 2025-04-23

> [@carlbunny](https://github.com/carlbunny)
> 
> > Can you elaborate more on using input_ids for train time test? For prediction the second token, you are not using âₜ₊₁ but the corresponding next token in the training data set?
> 
> My settings may not be aligned with EAGLE3 paper. I mean during the draft forward, I used the tokens which was also feed to the backbone (input ids). Not those tokens draft model generated. I only concat the hiddens from draft forward process.
> 
> training data: how can I **do** it draft forward: step1: how can I -> help step2: how can I do -> something step3: how can I do it -> for soft labels: how can I make it for CE loss: loss(make, help) + loss(it, something) + loss(for, for)
> 
> > I feel the 5.0 -> 5.7 improvement is mostly coming from not using token1_draft to predict token2_draft?
> 
> Actually, using draft tokens as next input for draft forward will get worse in my experiments.

@Liyuhui-12 Would you mind clarifying these points from the discussion?

### w32zhong · 2025-04-24

> 2\. prior to softmax as seen in [HASS](https://github.com/HArmonizedSS/HASS/blob/051c4020141f5d2a365994ca9a8148700044c6d7/model/cnets_hass.py#L336), it seems EAGLE v3 will use expanded attention without accumulations, and the extra required labels are predictions by the draft model.

Thanks for this great discussion, I believe I find where my previous guess is not accurate. Although eagle v3 paper (figure 6) expanded new states (thus q/k) predicted by the draft model, the labels (of q length) should be from the training set (in a better case, they should be base model predictions just like what v3 does). This would make a lot of sense because eagle-v3 is doing noise recovery from training-time predicted hidden states, so states should be simulated during training, but not labels.

> My settings may not be aligned with EAGLE3 paper. I mean during the draft forward, I used the tokens which was also feed to the backbone (input ids). **Not those tokens draft model generated. I only concat the hiddens from draft forward process.**

And this setting from @Ageliss aligned with my current belief, that we want to explicitly allow noise in predicting hidden states (that is also why we do not want to match any "soft labels" during training-time expansion), but trying to recover the original labels.

Also due to this, the training becomes very slow because no more soft labels there to speed up training efficiency. That is why sharegpt dataset alone is not sufficient, but a 8x training data is needed. My feeling is that eagle-v1 has almost exhausted the information provided by the base model (so v3 3-level concates comes to rescue, and ablations show it is helpful, although previous discussions show something different) on future tokens, therefore training-time test here has not too much base model info to utilize, and the step>=1 training behaves more alike regular LLM pre-training without soft labels, so the learning speed is no more efficient.

### carlbunny · 2025-04-24

@w32zhong can you elaborate on your current understanding?

Say
training dataset: How can I help you
base_decode2(how can I)           -> [do it]
base_decode1(how can I help)   -> [we]
draft_decode(how can I)             -> [a,b]

Should [a,b] be compared with 1) [help you], 2) [do it], 3) [help we], or something else?

### w32zhong · 2025-04-24

in terms of labels, my guess is [help we] (base model predictions) > [help you] (training data). But since you give training data already, it is usually only reading training data as labels (otherwise you will need to do not only draft model inference but also base model inference at training, which should be timely infeasible)

 I am not sure why you want to have base_decode2, is it a two token parallel decoding? at least in eagle it is AR-style training-time unroll. 

### carlbunny · 2025-04-25

> But since you give training data already, it is usually only reading training data as labels (otherwise you will need to do not only draft model inference but also base model inference at training, which should be timely infeasible)

It is slower but acceptable (on 32 GPU with local batch = 1). 
Just conceptually, correct me if I am wrong, I feel the whole point of train time test is to learn 2+ token instead of 1 from base model. If we do [help we], we learn one token from training data [help] + one token from draft model [we], that's less align with base model comparing to learning 2 from base model?

### NickL77 · 2025-05-13

I've implemented my understanding of training-time-test here: https://github.com/NickL77/BaldEagle?tab=readme-ov-file#eagle-3-status

It performs 11.7% faster and has 8.4% higher acceptance rate than my Eagle 2 baseline. You can see benchmark results in the model card.

I'm doing some more work in stabilizing the training before moving on to implementing fused-features, but that may be blocked on my system's storage.

Open to discussions and questions on the implementation. I'm not sure it's 100% correct 😅. 

### NickL77 · 2025-05-13

> We only get benefit on acceptance rate using the hidden fusion (about 5 -> 5.7), hard to get benefit from train time test (cannot reproduce >6.5).

Also @Ageliss, is your training data generated by the target model? Or do you use the assistant answers in ShareGPT and UltraChat?

In the Eagle 3 paper, they mention actually doing generation with the target model, rather than the fixed dataset approach in the Eagle 1 paper. Wondering how much of a different this makes as there's no ablation study in the paper on this

> We call the target model to generate responses rather than using a fixed dataset. (Under Implementation in section 4 Experiments)

### Ageliss · 2025-05-14

> > We only get benefit on acceptance rate using the hidden fusion (about 5 -> 5.7), hard to get benefit from train time test (cannot reproduce >6.5).
> 
> Also [@Ageliss](https://github.com/Ageliss), is your training data generated by the target model? Or do you use the assistant answers in ShareGPT and UltraChat?

I used the generated answers by ShareGPT questions with vLLM + temp=1.0. But the result is worse (5.0 -> 4.63). 

More observations:

I notice that EAGLE3 increased the depth from 6 to 8 and after applying such setting my previous settting increases from 5.7 -> 6.43, which seems not small. 



### carlbunny · 2025-05-15

Thanks @NickL77  for the update. I have an implementation currently gives me 5% accuracy improvement at draft length of 3. I see improvement when single out 1) fuse hidden and 2) training time test that decodes 2 or 3 tokens for loss. It is pretty much what the paper says. There is no hidden feature loss,  and the token loss are weighted to favor the 1st token. 

### LiMa-cas · 2025-05-30

Since the lm_header of draft model is different from the LLM model, how to get the loss of different two logits(one token size is 28w,the other token size is 3w)?

### carlbunny · 2025-06-11

> Since the lm_header of draft model is different from the LLM model, how to get the loss of different two logits(one token size is 28w,the other token size is 3w)?

Ah, in my setup, the token size is the same. 

### hongyanz · 2025-06-13

The training code has been released.

### haiduo · 2025-09-10

> I've implemented my understanding of training-time-test here: https://github.com/NickL77/BaldEagle?tab=readme-ov-file#eagle-3-status
> 
> It performs 11.7% faster and has 8.4% higher acceptance rate than my Eagle 2 baseline. You can see benchmark results in the model card.
> 
> I'm doing some more work in stabilizing the training before moving on to implementing fused-features, but that may be blocked on my system's storage.
> 
> Open to discussions and questions on the implementation. I'm not sure it's 100% correct 😅.

Hi, Thanks for you work,

It looks like your implementation is essentially just shifting the inputs to obtain multiple draft model predicted logits, then computing CE loss with the target model’s logits. In essence, that’s still single-step training (rather than the Train-Time Test, TTT, described in the EAGLE-3 paper). I think this method is similar to performing logit-level data augmentation on the same inputs, which is a common technique in knowledge distillation.

Although EAGLE-3 doesn’t explicitly specify how TTT is implemented, I personally believe it works as follows: during training, each token generated by the draft model replaces the corresponding original input token, and this modified sequence is then used as the next step’s TTT input. This process is dynamic, meaning that training includes the draft model’s sampling procedure. The principle is to let the training process perceive the draft model’s actual inference behavior, thereby reducing exposure bias. Fundamentally, this aligns the “tone” in LLM knowledge distillation.

The downside, however, is that the training cost becomes too high to be practical. If you pre-generate data using the draft model in advance, you can avoid the expensive online sampling, but performance tends to degrade (see Ref.  [Ageliss](https://github.com/SafeAILab/EAGLE/issues/194#issuecomment-2798392410)  ). In my view, EAGLE-3’s success comes more from **scaling up the data and fusing multi-layer features**.

<img width="983" height="880" alt="Image" src="https://github.com/user-attachments/assets/19cdd83c-8d96-4a18-9ce2-2203b427fb27" />
