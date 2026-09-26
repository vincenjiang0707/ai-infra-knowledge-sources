# [Issue #991] Error in Algorithm 1 of Flash Attention 2 paper

source: https://github.com/Dao-AILab/flash-attention/issues/991
state: open | updated: 2026-07-23T02:41:15Z
labels: 

## 正文

On line 10 of Algorithm 1 (FlashAttention-2 forward pass) of the [Flash Attention 2 paper](https://arxiv.org/pdf/2307.08691) it says
![image](https://github.com/Dao-AILab/flash-attention/assets/6439365/0c646c47-6f1e-4a60-a943-a15b58c825ff)

However, $\text{diag}\left(e^{m_i^{j-1} - m_i^{j}}\right)^{-1}\mathbf{O}_i^{(j-1)}$ should not have the $^{-1}$ and actually just be $\text{diag}\left(e^{m_i^{j-1} - m_i^{j}}\right)\mathbf{O}_i^{(j-1)}$.

Similar the online softmax trick example at the top of page 6 should also not have the $^{-1}$ before the $\tilde{\mathbf{O}}^{(1)}$
![image](https://github.com/Dao-AILab/flash-attention/assets/6439365/b330a1cc-d622-4f0a-9eb2-7802c7aeb620)

Lastly, there is a typo, where the following line
![image](https://github.com/Dao-AILab/flash-attention/assets/6439365/6e36f98e-596d-415b-b2c7-54291482a836)
should be deleted from the online softmax trick derivation in page 6. It looks like it was copied from the online softmax trick derivation on page 4 for Flash Attention 1 and was not removed.




## 评论 (7)

### xyg-coder · 2024-09-19

I was looking at triton [implementation](https://triton-lang.org/main/getting-started/tutorials/06-fused-attention.html) and it matches your idea. Thanks for pointing this out.

### ZJUGuoShuai · 2024-11-10

I agree with you. In addition, I also think there's a typo on Page 4 (describing FlashAttention 1):

<img width="739" alt="image" src="https://github.com/user-attachments/assets/30114b63-4425-46ce-836c-9718170f1b4e">

The $^{-1}$ should be deleted and it missed $e^{m^{(1)}-m^{(2)}}$ before $O^{(1)}$

Update: it's also noted by @andportnoy in #897.


### viai957 · 2025-02-27

Oh boy !! I thought I was the one missing something I penned down the entire forward pass derivation and I did not understand why the Inverse over O is needed Indeed I landed in the right place. Everything works fine if the inverse is not used over Output. I get the inverse is used in the normalization factor. Why is this still open Issue don't the author maintain this repo?

### ahban · 2025-08-06

Why did the author delete his response? Is there any information we missed? :(

### Victor-Jung · 2025-08-13

Oh man thanks a lot for spotting this issue! 😁 I was reproducing the algorithm and couldn't understand why I wasn't getting the expected output! I think it's pretty important to get this typo fixed in the arxiv paper read by so many (@tridao). 

### Victor-Jung · 2025-08-13

This typo is also present in the more recent [Flash Attention 3](https://arxiv.org/pdf/2407.08608) paper. In Algorithm 1, line 21.

<img width="516" height="29" alt="Image" src="https://github.com/user-attachments/assets/9d766033-a5a5-4752-bd72-c2151bda09b7" />

### parikshit14 · 2026-07-23

I spent two days figuring out why $^{-1}$ was there..... and finally i found this post
Thanks for posting.
