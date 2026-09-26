# [Issue #339] [Discussion] Performance characteristics of EAGLE 3.1 (Post-norm) at shallow speculative depths ($k \le 3$)

source: https://github.com/SafeAILab/EAGLE/issues/339
state: open | updated: 2026-06-09T14:31:39Z
labels: 

## 正文

Hi EAGLE team,                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                     
  We are currently evaluating EAGLE 3.1 for a large-scale inference framework. The theoretical foundation of using Post-norm to mitigate Attention Drift and Layer-stacking (as described in your paper) is brilliant.                               
                                                                                                                                                                                                                                                     
  However, when reviewing community implementations, we noticed an interesting phenomenon. For instance, in the recently released Kimi-K2.6-eagle3.1-mla model on Hugging Face (https://huggingface.co/lightseekorg/kimi-k2.6-eagle3.1-mla), the evaluation uses a shallow          
  speculation depth (num_speculative_tokens=3). Under this setting, the Post-norm architecture occasionally shows a slight regression compared to the Pre-norm baseline on specific sharp-distribution benchmarks (e.g., HumanEval: -0.058, MATH500: 
  -0.053).                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                     
  The paper clearly demonstrates that Post-norm prevents magnitude accumulation and Attention Drift, which is critical for deep speculation (e.g., $k=8$). Our hypothesis is that at shallow depths ($k \le 3$) where drift is not yet severe, the   
  additional normalization layers (FC-norm and Post-norm) might introduce a regularization effect that slightly hinders the draft model's immediate next-token prediction accuracy on these tasks.                                                   
                                                                                                                                                                                                                                                     
  Questions for discussion:                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                     
  1. Does this align with your theoretical understanding and experimental observations?                                                                                                                                                              
  2. Is there an implicit "minimum effective depth" (e.g., $k \ge 4$) required to truly observe the architectural benefits of EAGLE 3.1 over 3.0?                                                                                                    
  3. Has the team collected comparative data on the performance of Pre-norm vs. Post-norm at varying shallow depths?                                                                                                                                 
                                                                                                                                                                                                                                                     
  Thanks for the great work and looking forward to your insights! 

## 评论 (3)

### Dogacel · 2026-06-05

Hi @changerjin, thanks for the deep-dive 🙏

1. For sure deeper speculation is better on EAGLE 3.1, but in my experience accuracy on first token is also higher (eval/acc0) for all the models we trained as a part of our paper. I agree that additional norm might act as an over-regularizer but I don't think its impact is significant.

   Kimi K2.6 EAGLE3.1 checkpoint is trained using a multi-stage pipeline (different than our paper's regular 2-epoch training) and base accuracy drops when you do the second stage (long ctx + multi-lingual) training. We know post-norm is more data efficient as well, so this second healing stage might have hurt the base accuracy more under the same training setting.

  <img width="4596" height="2414" alt="Image" src="https://github.com/user-attachments/assets/f752386f-e1bc-49b5-8fac-a3c79d9450aa" />

2. I think there is no minimum effective depth. Firstly some models like gpt-oss always have better accuracy. Second, EAGLE 3.1 also shows resilliency to long context degredation, multi-linguality, system prompt length variations and template changes. I think choosing the pre-norm over post-norm for ~0.05 additional acceptance length is overfitting considering the other benefits of the architecture.


3. Yes, the data was favoring post-norm. Especially on very deeper predictions acceptance rate for that step was doubled or tripled. We didn't include it in our paper to save some space. But we've shared every model we've trained as a part of our paper here: https://huggingface.co/collections/Dogacel/attention-drift , you can use our codebase for the paper to reproduce all results and inspect it yourself too, https://github.com/Dogacel/Attention-Drift.


### changerjin · 2026-06-09

Hi Dogacel,                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                               
Thank you for the detailed explanation.                         
                                                                                                                                                                                                                                               
Based on your explanation and our practices, I have two thoughts:                                                                  
                                                                                                                                                                                                                                               
1. Regarding the evaluation of kimi-k2.6-eagle3.1-mla:                                                                                                                                                                                    
Since its second training stage was specifically focused on long context + multi-lingual data (causing the drop in base  accuracy), and noticing that current benchmarks on HuggingFace are mostly evaluated on relatively short texts (like GSM8K, MMLU)... I suspect that this checkpoint would actually show an advantage if evaluated on long-context benchmarks.                                                                                       
                                                                                                                                                                                                                                               
2. Regarding the better training strategy for extremely long-context models (like Kimi-K2.6):                                                                                                                                                   
I noticed in your paper that your drafters were trained purely using a single-stage approach on relatively short sequences (e.g., restricted to 4096 or 8K tokens for 1-2 epochs). Despite this, they generalized exceptionally well to longer contexts.                                                                                                                                                                                                                                          
Therefore, it seems to me that even for base models natively supporting 128K+ contexts, the approach from your paper is still the better path. Attempting a multi-stage or dedicated long-context training stage for a Post-norm drafter seems unnecessary and risky.                                                                                                                                
                                                                                                                                                                                                                                               
Do these two observations align with your perspective?                                                       
                                                                                                                                                                                                                                               
Thanks again for the great work and discussion! 

### Dogacel · 2026-06-09

> Hi Dogacel,
> 
> Thank you for the detailed explanation.
> 
> Based on your explanation and our practices, I have two thoughts:
> 
>     1. Regarding the evaluation of kimi-k2.6-eagle3.1-mla:
>        Since its second training stage was specifically focused on long context + multi-lingual data (causing the drop in base  accuracy), and noticing that current benchmarks on HuggingFace are mostly evaluated on relatively short texts (like GSM8K, MMLU)... I suspect that this checkpoint would actually show an advantage if evaluated on long-context benchmarks.
> 
>     2. Regarding the better training strategy for extremely long-context models (like Kimi-K2.6):
>        I noticed in your paper that your drafters were trained purely using a single-stage approach on relatively short sequences (e.g., restricted to 4096 or 8K tokens for 1-2 epochs). Despite this, they generalized exceptionally well to longer contexts.
>        Therefore, it seems to me that even for base models natively supporting 128K+ contexts, the approach from your paper is still the better path. Attempting a multi-stage or dedicated long-context training stage for a Post-norm drafter seems unnecessary and risky.
> 
> 
> Do these two observations align with your perspective?
> 
> Thanks again for the great work and discussion!


1. I think benchmarks should be short-context because it is not explicitly stated. I think it is hard to say about long-context performance, but my bet is that it is "at least as good" as EAGLE-3. Both eagle3 and eagle3.1 checkpoints for kimi is 2-stage trained. What I tried to point out is their converges rates / learning patterns are different, so there is a chance that 2nd stage might have hurt short-ctx accuracy more for post-norm. I think there is only one way to find out, just running the long ctx benchmarks 😆 

2. The catch in 2nd stage is we saw performance being better with SWA set to your training length. So a longer context training could still help in some sense to increase your SWA length (or totally eliminate it). I think this is a good future research direction, the experiments in our paper is not enough, if we had the resources I would have done an experiment to compare 2nd stage training to 1st stage checkpoint with SWA in LongBench. I think the reality lies somewhere in-between. You still need multi-stage, but probably less steps is enough + preserves your original accuracy. 

Thanks!
