# [Issue #244] When is the Qwen3 model expected to support Eagle3?

source: https://github.com/SafeAILab/EAGLE/issues/244
state: open | updated: 2025-12-16T16:37:26Z
labels: 

## 正文

The Qwen3-14B/32B models have been open-sourced, and we are currently researching the performance of Qwen3. We hope the Eagle3 model can support Qwen3 and would like to know the estimated timeline for this support. Thank you.

## 评论 (15)

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012

### jiahe7ay · 2025-07-02

@fanqingyu0604 

### Siegfried-qgf · 2025-07-02

> We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.
> 
> We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.
> 
> https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3
> 
> https://huggingface.co/Tengyunw/qwen3_8b_eagle3
> 
> Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.
> 
> https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA
> 
> https://zhuanlan.zhihu.com/p/1923763301432662012

Your training process seems only to modify the address of the target model and the data templation. That means you used one layer of Llama to train EAGLE3 of Qwen3？I have completed the EAGLE3 training code of Qwen series as well and my modification is more than you.  

### jiahe7ay · 2025-07-02

@Siegfried-qgf  can u share your modification?


### jiahe7ay · 2025-07-02

@Siegfried-qgf    One more step I forgot to mention is obtaining the hidden_states. It needs to be aligned with the implementation on Hugging Face, and you can’t entirely rely on the official code to retrieve it, because that part was rewritten by them.

### bitxsw93 · 2025-07-04

![Image](https://github.com/user-attachments/assets/0f8f69ae-f15e-4417-8f72-81358f646eaf)
how to run qwen3-8b with eagle3 in this repo? 
how to choose --model-type ?

### rainkert · 2025-07-04

> [@Siegfried-qgf](https://github.com/Siegfried-qgf) One more step I forgot to mention is obtaining the hidden_states. It needs to be aligned with the implementation on Hugging Face, and you can’t entirely rely on the official code to retrieve it, because that part was rewritten by them.

I also encountered this issue following your blog. Could you show the specific code changes? @jiahe7ay 

### jiahe7ay · 2025-07-04

> > [@Siegfried-qgf](https://github.com/Siegfried-qgf) One more step I forgot to mention is obtaining the hidden_states. It needs to be aligned with the implementation on Hugging Face, and you can’t entirely rely on the official code to retrieve it, because that part was rewritten by them.
> 
> I also encountered this issue following your blog. Could you show the specific code changes? [@jiahe7ay](https://github.com/jiahe7ay)

@rainkert 
outs = self.target_model(input_ids=input_ids, attention_mask=attention_mask,output_hidden_states=True)   

### jiahe7ay · 2025-07-04

> ![Image](https://github.com/user-attachments/assets/0f8f69ae-f15e-4417-8f72-81358f646eaf) how to run qwen3-8b with eagle3 in this repo? how to choose --model-type ?

@bitxsw93  in this link: https://huggingface.co/Tengyunw/qwen3_8b_eagle3 , here is a tutorial on how to use the Egale3 algorithm with Qwen3-8b in the SGLang inference framework.

### yghstill · 2025-07-11

We have open-sourced the ​Eagle3 model from the `​Qwen3` series and released its ​Benchmark. You are welcome to try it out!
- Github Repo: [https://github.com/Tencent/AngelSlim](https://github.com/Tencent/AngelSlim)
- Hugging Face collection: [huggingface qwen3-EAGLE3](https://huggingface.co/collections/AngelSlim/qwen3-eagle-686787e3258f84fb09019f32)
- modelscope collection: [modelscope Qwen3-EAGLE3](https://modelscope.cn/collections/Qwen3-EAGLE-428a93f5482649)

<table>
  <thead>
    <tr>
        <th>&nbsp</th><th>&nbsp</th>
        <th colspan="2" style="text-align: center; vertical-align: middle;">MT-bench</th>
        <th colspan="2" style="text-align: center; vertical-align: middle;">HumanEval</th>
        <th colspan="2" style="text-align: center; vertical-align: middle;">GSM8K</th>
        <th colspan="2" style="text-align: center; vertical-align: middle;">Alpaca</th>
        <th colspan="2" style="text-align: center; vertical-align: middle;">Mean</th></tr>
    <tr><th>Temperature</th><th>Model</th><th>Speedup</th><th>τ</th><th>Speedup</th><th>τ</th><th>Speedup</th><th>τ</th><th>Speedup</th><th>τ</th><th>Speedup</th><th>τ</th></tr>
  </thead>
  <tbody>
    <!-- <tr><td colspan="12" style="text-align: center; vertical-align: middle;"><strong>Temperature=0</strong></td></tr> -->
    <tr><td rowspan="6"><strong>T=0</strong></td>
    <td>Qwen3-1.7B</td><td>2.05x</td><td>2.81</td><td>2.07x</td><td>2.93</td><td>2.11x</td><td>2.98</td><td>1.93x</td><td>2.69</td><td>2.04x</td><td>2.85</td></tr>
    <tr> <td>Qwen3-4B</td><td>2.21x</td><td>3.01</td><td>2.36x</td><td>3.24</td><td>2.42x</td><td>3.13</td><td>2.32x</td><td>2.75</td><td>2.33x</td><td>3.03</td></tr>
    <tr><td>Qwen3-8B</td><td>2.63x</td><td>3.65</td><td>2.76x</td><td>3.85</td><td>2.82x</td><td>3.90</td><td>2.62x</td><td>3.48</td><td>2.70x</td><td>3.72</td></tr>
    <tr><td>Qwen3-14B</td><td>2.23x</td><td>3.30</td><td>2.53x</td><td>3.74</td><td>2.56x</td><td>3.79</td><td>2.16x</td><td>3.13</td><td>2.37x</td><td>3.49</td></tr>
    <tr><td>Qwen3-32B</td><td>2.39x</td><td>2.78</td><td>2.37x</td><td>2.81</td><td>2.47x</td><td>2.92</td><td>2.42x</td><td>2.53</td><td>2.41x</td><td>2.76</td></tr>
    <tr><td>Qwen3-30B-A3B</td><td>2.84x</td><td>3.63</td><td>2.27x</td><td>3.09</td><td>2.64x</td><td>3.42</td><td>2.83x</td><td>3.56</td><td>2.64x</td><td>3.42</td></tr>
    <!-- <tr><td colspan="12" style="text-align: center; vertical-align: middle;"><strong>Temperature=1</strong></td></tr> -->
    <tr><td rowspan="6"><strong>T=0</strong></td>
    <td>Qwen3-1.7B</td><td>1.74x</td><td>2.53</td><td>1.86x</td><td>2.70</td><td>1.82x</td><td>2.69</td><td>1.72x</td><td>2.46</td><td>1.93x</td><td>2.60</td></tr>
    <tr><td>Qwen3-4B</td><td>1.93x</td><td>2.60</td><td>2.00x</td><td>2.84</td><td>2.11x</td><td>2.82</td><td>2.34x</td><td>2.50</td><td>1.75x</td><td>2.69</td></tr>
    <tr><td>Qwen3-8B</td><td>1.98x</td><td>2.75</td><td>2.25x</td><td>3.11</td><td>2.31x</td><td>3.15</td><td>2.10x</td><td>2.76</td><td>2.90x</td><td>2.94</td></tr>
    <tr><td>Qwen3-14B</td><td>1.71x</td><td>2.61</td><td>1.95x</td><td>2.87</td><td>2.04x</td><td>3.08</td><td>1.68x</td><td>2.55</td><td>2.90x</td><td>2.78</td></tr>
    <tr><td>Qwen3-32B</td><td>1.62x</td><td>1.91</td><td>1.71x</td><td>2.05</td><td>1.78x</td><td>2.10</td><td>1.80x</td><td>1.95</td><td>1.62x</td><td>2.00</td></tr>
    <tr><td>Qwen3-30B-A3B</td><td>1.91x</td><td>2.46</td><td>2.00x</td><td>2.64</td><td>1.90x</td><td>2.53</td><td>1.80x</td><td>2.32</td><td>1.90x</td><td>2.48</td></tr>
  </tbody>
</table>

### hongyanz · 2025-07-12

@yghstill Thank you for reproducing EAGLE-3. We will add your Huggingface link to our ReadMe for broadcasting.

### yghstill · 2025-07-13

> [@yghstill](https://github.com/yghstill) Thank you for reproducing EAGLE-3. We will add your Huggingface link to our ReadMe for broadcasting.

@hongyanz Excellent, we're honored to contribute.

### lingyaoluu · 2025-07-16

@yghstill Hi, I'm currently trying to reproduce this work, and I'm wondering how metrics like acceptance rate, throughput, and speed are calculated? It seems like the sglang backend logs only show individual entries but not the overall statistics. Thanks in advance!

### quanfeifan · 2025-08-01

maybe this pr will help #271 

### congson1293 · 2025-12-16

> We have open-sourced the ​Eagle3 model from the `​Qwen3` series and released its ​Benchmark. You are welcome to try it out!
> 
> * Github Repo: https://github.com/Tencent/AngelSlim
> * Hugging Face collection: [huggingface qwen3-EAGLE3](https://huggingface.co/collections/AngelSlim/qwen3-eagle-686787e3258f84fb09019f32)
> * modelscope collection: [modelscope Qwen3-EAGLE3](https://modelscope.cn/collections/Qwen3-EAGLE-428a93f5482649)
> 
>  	 	MT-bench	HumanEval	GSM8K	Alpaca	Mean
> Temperature	Model	Speedup	τ	Speedup	τ	Speedup	τ	Speedup	τ	Speedup	τ
> **T=0**	Qwen3-1.7B	2.05x	2.81	2.07x	2.93	2.11x	2.98	1.93x	2.69	2.04x	2.85
> Qwen3-4B	2.21x	3.01	2.36x	3.24	2.42x	3.13	2.32x	2.75	2.33x	3.03
> Qwen3-8B	2.63x	3.65	2.76x	3.85	2.82x	3.90	2.62x	3.48	2.70x	3.72
> Qwen3-14B	2.23x	3.30	2.53x	3.74	2.56x	3.79	2.16x	3.13	2.37x	3.49
> Qwen3-32B	2.39x	2.78	2.37x	2.81	2.47x	2.92	2.42x	2.53	2.41x	2.76
> Qwen3-30B-A3B	2.84x	3.63	2.27x	3.09	2.64x	3.42	2.83x	3.56	2.64x	3.42
> **T=0**	Qwen3-1.7B	1.74x	2.53	1.86x	2.70	1.82x	2.69	1.72x	2.46	1.93x	2.60
> Qwen3-4B	1.93x	2.60	2.00x	2.84	2.11x	2.82	2.34x	2.50	1.75x	2.69
> Qwen3-8B	1.98x	2.75	2.25x	3.11	2.31x	3.15	2.10x	2.76	2.90x	2.94
> Qwen3-14B	1.71x	2.61	1.95x	2.87	2.04x	3.08	1.68x	2.55	2.90x	2.78
> Qwen3-32B	1.62x	1.91	1.71x	2.05	1.78x	2.10	1.80x	1.95	1.62x	2.00
> Qwen3-30B-A3B	1.91x	2.46	2.00x	2.64	1.90x	2.53	1.80x	2.32	1.90x	2.48

@yghstill Can I use this model for the `Qwen3-30b-a3b-instruct-2507` model ?
