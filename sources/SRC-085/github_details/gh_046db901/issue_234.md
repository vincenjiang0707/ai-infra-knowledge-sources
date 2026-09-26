# [Issue #234] Request to create a new branch for multi batch code

source: https://github.com/SafeAILab/EAGLE/issues/234
state: closed | updated: 2025-09-05T00:50:07Z
labels: 

## 正文

Hello authors, our newly submitted algorithm to NIPS in May has made significant optimizations for EAGLE's multi-batch speculative sampling. The core idea is that, based on the actual inference cost at runtime, our speculative sampling algorithm dynamically adjusts the parameters of the draft tree—specifically top-k, total_token, and depth—depending on the context. Our method achieves remarkable performance improvements under multi-batch settings, and even shows an average 5% speedup in single-batch scenarios. Results on A800 show that with a batch size (bsz) of 128, we still achieve a speedup of 1.2x. **We are interested in opening a branch called EAGLE-bsne1 in your project to open-source our code**. Would you be willing to support this?

Our implementation is built upon your codebase. We have added multi-batch processing and various optimizations, including support for EAGLE-1, EAGLE-2, and EAGLE-3. We're currently cleaning up the code and plan to release it in early August. If you're interested, I can send you the current version of the code and the paper ahead of time for reproduction.

video for bsne1:  [https://computer-961-1300303058.cos.ap-chengdu.myqcloud.com/2506/mmexport1748968518249.mp4](https://computer-961-1300303058.cos.ap-chengdu.myqcloud.com/2506/mmexport1748968518249.mp4)
video for bseq1: [https://computer-961-1300303058.cos.ap-chengdu.myqcloud.com/2506/mmexport1748968523682.mp4](https://computer-961-1300303058.cos.ap-chengdu.myqcloud.com/2506/mmexport1748968523682.mp4)

Below are some results demonstrating the performance of our algorithm:

![Image](https://github.com/user-attachments/assets/d0f91909-e44d-4829-99fb-4a49545efc51)

## 评论 (16)

### hongyanz · 2025-06-06

Hello @hongdaxia Thanks for sharing your work. The result looks awesome. We are happy to collaborate.

In Table 3 of the [EAGLE-3 paper](https://arxiv.org/pdf/2503.01840) (tested by SGLang team), EAGLE-3 can have 1.38x speedup improvement even at the batch size of 64. Can you please clarify why the result is inconsistent with yours?

### hongdaxia · 2025-06-06

> Hello [@hongdaxia](https://github.com/hongdaxia) Thanks for sharing your work. The result looks awesome. We are happy to collaborate.
> 
> In Table 3 of the [EAGLE-3 paper](https://arxiv.org/pdf/2503.01840) (tested by SGLang team), EAGLE-3 can have 1.38x speedup improvement even at the batch size of 64. Can you please clarify why the result is inconsistent with yours?
Our results were tested based on EAGLE's original code, not on the SGLang inference framework. Additionally, EAGLE-3 uses parameters consistent with those in single-batch settings. These two factors lead to different results. We are now trying to integrate our algorithm into the SGLang inference framework. At that time, the multi-batch code for EAGLE and the corresponding SGLang code may be released together. Thank you very much for your support, which has given us the motivation to organize our code.


### hongdaxia · 2025-06-06

> Hello [@hongdaxia](https://github.com/hongdaxia) Thanks for sharing your work. The result looks awesome. We are happy to collaborate.
> 
> In Table 3 of the [EAGLE-3 paper](https://arxiv.org/pdf/2503.01840) (tested by SGLang team), EAGLE-3 can have 1.38x speedup improvement even at the batch size of 64. Can you please clarify why the result is inconsistent with yours?

Additionally, the GPU used in our multi-batch experiments are two A800s. Under the same conditions, their speedup ratio is similar to that of the A100, but worse than the H100. Therefore, if the tests were conducted on H100, EAGLE-3 and EAGLE-3E in the chart should achieve a higher speedup ratio.

### hongyanz · 2025-06-06

Perhaps the bad performance of EAGLE-3 in your experiment is because of a bad hyperparameter choice. In the large batch case, you are expected to turn off the drafting tree (i.e., using chain drafting with tree width = 1) and set the drafting length to be a small value (e.g., 1-3).

In the demo, we only present a suggested hyperparameter for single-batch case. You are not expected to use the same hyperparameter setting for all cases.

### hongdaxia · 2025-06-07

> Perhaps the bad performance of EAGLE-3 in your experiment is because of a bad hyperparameter choice. In the large batch case, you are expected to turn off the drafting tree (i.e., using chain drafting with tree width = 1) and set the drafting length to be a small value (e.g., 1-3).
> 
> In the demo, we only present a suggested hyperparameter for single-batch case. You are not expected to use the same hyperparameter setting for all cases.

You are right; although this approach may perform significantly worse on small batches like bsz=8, it leads to substantial performance improvements on larger batches such as bsz=64. Our enhanced algorithm, EAGLE-3E, dynamically adjusts the draft tree when bsz=64, with the depth varying approximately between 2 and 4, top_k ranging from about 1 to 3, and total_token varying roughly from 2 to 8. The structure of the draft tree still helps improve the algorithm's performance on large batches. However, for EAGLE-3, the original hyperparameters are indeed too large and not suitable when bsz=64.

### hongyanz · 2025-06-07

Sound interesting. Have you tried a greedy search of hyperparameters in EAGLE-3 and compared its best hyperparameter choice with your method?

### hongdaxia · 2025-06-07

> Sound interesting. Have you tried a greedy search of hyperparameters in EAGLE-3 and compared its best hyperparameter choice with your method?

We haven't tried it yet, but we will test it in the future. After doing this, the only remaining room for improvement in our algorithm would be dynamically adjusting the depth. I think it should still have some effect, although probably not a very significant one — we'll need to run tests to find out.

### hongyanz · 2025-06-07

Great. I just feel it is a bit unfair to compare one method with another, where one carefully tunes the hyperparameters in one method while leaving the hyperparameters in another method poorly tuned or un-tuned.

Or do you claim your method as an auto-hyperparameter-tuning method?

### hongdaxia · 2025-06-07

> Great. I just feel it is a bit unfair to compare one method with another, where one carefully tunes the hyperparameters in one method while leaving the hyperparameters in another method poorly tuned or un-tuned.
> 
> Or do you claim your method as an auto-hyperparameter-tuning method?

yes

### hongdaxia · 2025-06-07

> Great. I just feel it is a bit unfair to compare one method with another, where one carefully tunes the hyperparameters in one method while leaving the hyperparameters in another method poorly tuned or un-tuned.
> 
> Or do you claim your method as an auto-hyperparameter-tuning method?

As shown in the figure below, in some cases, a tree structure may perform better:

![Image](https://github.com/user-attachments/assets/249ec399-ba3e-416f-8088-177aecd47609)

In some cases, total_token=2 works better, while in other cases, total_token=3 is preferable.

![Image](https://github.com/user-attachments/assets/c0f85be1-de03-45d6-8e60-dd5d045c0782)

The core of our algorithm is to determine, based on the inference cost, what kind of tree structure should be selected to achieve the best speedup.



### hongyanz · 2025-07-18

Hello @hongdaxia We are happy to add you to this repo if you are still interested in opening sourcing your code here. Or you can also submit a pull request.

### hongdaxia · 2025-07-19

> Hello [@hongdaxia](https://github.com/hongdaxia) We are happy to add you to this repo if you are still interested in opening sourcing your code here. Or you can also submit a pull request.

Hello, I'm very happy to join you.

Currently, I am trying to integrate my algorithm into the SGLang inference framework. My algorithm is essentially a more advanced draft tree, where the construction and pruning of the draft tree are based on context and hardware costs. Therefore, in SGLang, I want to separate speculative inference into two parts: the draft tree and the draft model.

The draft tree could be the static draft tree from EAGLE-1, the dynamic draft tree from EAGLE-2, or my cost-based draft tree. In the future, I plan to further optimize the cost-based draft tree, possibly creating a cost-based draft tree 2.0. The draft model could be EAGLE or EAGLE3. Based on this design, it will be easy to extend new draft models and draft trees in the future.

At present, the code for speculative inference in SGLang is a bit messy, so I am thinking about the best way to implement this and am working hard on it.

My cost-based draft tree is specifically designed for larger batches (1 <= batch_size <= 128), and its effectiveness relies heavily on the powerful capabilities of your model. Thank you very much for your contribution

### hongyanz · 2025-07-19

Sounds great. If you also want to create a new branch in this repo (as a HF version of EAGLE-1-2-3), I am happy to add you. Just let me know.

### hongdaxia · 2025-07-19

> Sounds great. If you also want to create a new branch in this repo (as a HF version of EAGLE-1-2-3), I am happy to add you. Just let me know.

ok.

Based on the SGLang code, I expect to have my implementation finished by early August. At that time, I will have four parts of the code that I'd like to open-source to one of your branches.

*   The first part will be modifications based on EAGLE-1.
*   The second part will be modifications based on EAGLE-2.
*   The third part will be modifications based on EAGLE-3.
*   The fourth part will be modifications to the speculative inference section of SGLang.

I plan to complete the code between August 5th and August 10th and will reach out to you then to proceed with the open-sourcing. The contribution will include the modified code as well as a performance evaluation of the algorithm.

Thanks for your support!

### hongdaxia · 2025-08-24

> Sounds great. If you also want to create a new branch in this repo (as a HF version of EAGLE-1-2-3), I am happy to add you. Just let me know.

老哥，你们那有H100么，在SGLang框架里面我自己实现了一个算法，目前还不太完善，比预期进度慢，下个月大概能发布，这个算法是之前我在实习公司搞的，目前已经离职，现在就一张RTX4090在做着实验，目前在RTX4090显卡和SGLang推理框架，以及lama3 8b和mt_bench数据集下面，bs=1有3.6倍加速，速度205 token/s，SGLang自己实现的在4090上大概178token/s；bs=8时有2.5倍加速，大概1050 token/s。更大的bs就测不了了，显存不够。然后在写SGLang移植过程中也有了新的思考，想做一个更大批次的改进算法，针对bs=128和bs=256做的，改进核心思路也基本上有了，想问问这个方向是否和你们的EAGLE-4冲突？我的算法没有改变模型，就是把模型性能和准确性在批次情况下利用到极致，基本上没有填充上的浪费。感兴趣可以加个微信我把源码发给你们去评测。现在准备找个大的显卡评测多机多卡，不同批次规模，不同加速技术，比如模型量化下的算法表现。

### hongyanz · 2025-08-24

可以加我微信：hongyanzha
