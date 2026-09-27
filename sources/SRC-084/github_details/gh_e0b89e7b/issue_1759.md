# [Issue #1759] A new 8-bit quantization method (PQ-R) with 3x higher SNR for CPU

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1759
state: closed | updated: 2026-02-24T17:25:40Z
labels: 

## 正文

### Feature request

This is a feature request to add a new 8-bit quantization method called **Product Quantization with Residuals (PQ-R)** to the `bitsandbytes` library.

**What is PQ-R?**
PQ-R is a hybrid quantization algorithm that combines the strengths of K-Means clustering and residual correction. It consistently delivers a much higher Signal-to-Noise Ratio (SNR) and reconstruction quality compared to standard `int8_linear` methods, making it ideal for users who need to minimize quality loss on CPU or edge devices.

**Key Benefits:**
-   **High Fidelity:** Achieves **~3x higher SNR** than standard INT8 on challenging model layers.
-   **Practical Performance:** It is over **20x faster** than pure K-Means, making it a viable and efficient tool for developers.
-   **Proven:** The method has been rigorously benchmarked on the TinyLlama 1.1B model, demonstrating its ability to compress the model to ~1 GB while maintaining high quality.

This feature would provide `bitsandbytes` users with a powerful new quantization option that bridges the gap between fast-but-low-quality `int8` and high-quality-but-impractical `kmeans`.

### Motivation

**The Problem:** There is a significant gap in the current landscape of 8-bit quantization techniques.
1.  **Standard `int8` methods** are fast but often result in a severe quality drop (low SNR), especially on layers with complex or outlier-heavy weight distributions.
2.  **High-quality methods** like full 256-center K-Means are computationally infeasible for practical use, taking minutes to compress a single layer.

**The Proposal:** I have developed and rigorously benchmarked a hybrid method, **Product Quantization with Residuals (PQ-R)**, that directly solves this problem. It provides a practical path to achieving near-optimal quality with reasonable performance on commodity CPU hardware.

My benchmarks on various TinyLlama layers show that PQ-R delivers:

-   **~3x higher SNR** than standard `int8_linear` quantization on challenging layers (e.g., **34.2 dB** vs 25.8 dB).
-   It is **over 20x faster** than pure K-Means, making it a viable tool for developers.
-   It enables compressing a 1.1B model to **~1 GB** while maintaining a high average quality of **~32 dB SNR**.

This method could provide `bitsandbytes` users with a powerful new option for high-quality quantization, especially for CPU and edge device deployments.

I've published a full technical write-up on Medium with all the graphs and data:
**[[Medium]](https://medium.com/@alex42ff/beating-int8-how-i-squeezed-a-1-1b-llm-to-1gb-on-a-cpu-with-3x-better-quality-600e986fda0d)**

The full testing suite and detailed analysis are also available on GitHub:
**[[GitHub]](https://github.com/AlexSheff/pqr-llm-quantization/tree/main)**

### Your contribution

Absolutely. I would be happy to help with the integration.

The core algorithm is fully implemented in Python (using scikit-learn and NumPy) and has been thoroughly tested, as demonstrated in the linked repository.

While the core `pqr_core.py` implementation is currently proprietary, I am very open to discussing the best way to integrate it into `bitsandbytes`. This could involve:

-   Providing a reference implementation or code snippets for the key parts of the algorithm.
-   Collaborating with your team to build an optimized version that fits the library's architecture (e.g., CUDA kernels if desired).
-   Discussing licensing options that would work for both the project and myself.

I am confident this method would be a valuable addition to the library and am ready to assist in making it happen.

## 评论 (6)

### Titus-von-Koeller · 2025-09-22

This looks really neat. We have a bit of a busy week, but I'll discuss it with the team and get back to you soon.

Thanks for taking the initiative to contact us and to formulate your thoughts so well. Talk soon 🤗 

### Titus-von-Koeller · 2025-09-22

We're under a fully open license, MIT so far and Apache 2.0 has been discussed for new parts, but so far we've been hesitant, to keep things simple. We're not part of Hugging Face, but an independent community project, it's just that Hugging Face is our main sponsor and provides two engineers to staff it. Tim Dettmers is the original creator and still advises us on a weekly basis.

Is the MIT licensing a problem for you?

### AlexSheff · 2025-09-22

Hi Titus,
Thank you so much for the quick and positive response! I'm thrilled that the project looks interesting to you and your team.
That's a great and important question regarding the licensing, and I really appreciate you asking it directly.
As an independent researcher, my primary goal is to find a way to make this work sustainable so I can continue developing and improving it. A fully permissive license like MIT is fantastic for adoption, but it does present a challenge for direct monetization through commercial licensing, which is one of the avenues I'm exploring.
However, I am very flexible and my main objective is to see this technology get into the hands of users. I am confident that bitsandbytes is the perfect home for it.
Perhaps we could find a model that works for everyone. For example, rather than simply contributing the existing Python code, I could offer my time and expertise to help your team develop a highly optimized, native bitsandbytes version of the PQ-R algorithm.
This could be structured as a sponsored project or a contract-based contribution. In this scenario, I would be compensated for the development, integration, and optimization work, and the final, fully integrated code would, of course, be released under your standard MIT license. This would be a win-win: the community gets a powerful, fully open-source feature, and I get the support needed to continue my research.
I am completely open to discussing other ideas as well.
Of course, no need to rush. I'm happy to wait until you've had a chance to discuss the core proposal with the team.
Looking forward to hearing your thoughts when you're ready.
Talk soon 🤗



### AlexSheff · 2025-09-22

Hi Titus,
Just a quick and very exciting update to my proposal.
Following a challenge from the llama.cpp community to benchmark my method against their Q8_0 implementation, I developed a new, localized version of my algorithm: Local PQ-R. The results are a significant step up from my initial findings.
It turns out that by applying the PQ-R logic locally to each 32-value block, the reconstruction quality skyrockets. The new method achieves a staggering ~61.5 dB SNR, which is a ~16 dB improvement over the already-strong GGML Q8_0.
Here is the summary from the new benchmark:
Final Benchmark Results:

Layer: up_proj
Method                   SNR (dB)            Time (s)
--------------------------------------------------
Linear INT8               27.58                0.39
GGML Q8_0               45.32              30.67
Local PQR 4+4           61.51              1092.08

Layer: gate_proj
Method               SNR (dB)        Time (s)
--------------------------------------------------
Linear INT8          25.79           0.07
GGML Q8_0            45.34           30.20
Local PQR 4+4        61.52           1070.50

Layer: q_proj
Method               SNR (dB)        Time (s)
--------------------------------------------------
Linear INT8          29.00           0.03
GGML Q8_0            45.00           10.98
Local PQR 4+4        61.63           390.61
(I've also attached the new summary plot below)

<img width="1200" height="800" alt="Image" src="https://github.com/user-attachments/assets/2e98e235-c12c-4cf9-9be1-86d4502641a2" />

This is a ~16 dB improvement, which on a logarithmic scale represents a massive leap in reconstruction quality, approaching near-lossless 8-bit compression. This positions Local PQ-R not just as an alternative, but as a potential new state-of-the-art for fidelity in this space.
This discovery has, of course, reshaped my perspective on the licensing. Handing over a potential SOTA algorithm to be immediately available under a fully permissive MIT license would make it very difficult for me, as an independent researcher, to build a sustainable path forward from this work.
However, my primary goal is absolutely to see this technology in the hands of users, and bitsandbytes is the best possible home for it.
Perhaps this opens the door for a more strategic collaboration? For example, Hugging Face (as your sponsor) could sponsor the development and integration of a highly optimized, native version of Local PQ-R into bitsandbytes.
Under this model, I would be compensated for my work to bring this SOTA algorithm to the community, and the final, fully integrated feature would be released under your standard MIT license. This would be a huge win for everyone: the community gets an incredible new feature, bitsandbytes solidifies its position as the leading quantization library, and I receive the support to continue this line of research.
I know you have a busy week, so this is just food for thought. I'm very flexible and open to other ideas.
Looking forward to hearing what the team thinks when you have a moment.
Talk soon 🤗
Alex

### AlexSheff · 2025-09-22

Hi all,
The final and most crucial experiment, Phase 5, is now complete. The goal was to analyze the trade-off between block_size, reconstruction quality (SNR), and the final compression ratio for the Local PQ-R method.
The results are in, and they paint a complete and fascinating picture. It turns out Local PQ-R isn't a single method, but a tunable framework.
Final Block Size Analysis Summary:

Block Size      SNR (dB)        Comp Ratio (vs FP16)
----------------------------------------------------
32                  61.52                        0.40
64                  49.96                        0.67
128                45.92                      1.00
256                43.59                      1.33
512                41.95                      1.60

And here is the final plot:
https://github.com/AlexSheff/pqr-llm-quantization/blob/3df67e4134cda883ce2f1a24f7eb9ae8d384b8f1/assets/phase5_block_size_analysis.png
My conclusions:
A new SOTA for quality is confirmed: The block_size=32 setting achieves an unprecedented ~61.5 dB SNR, creating an "ultra-quality" or "archive" mode.
The point of superiority is found: At block_size=128, Local PQ-R's quality (45.9 dB) surpasses that of GGML Q8_0 (~45.3 dB), proving the core algorithm's strength.
A new trade-off space is revealed: Users can now choose their preferred balance. For example, block_size=512 offers a strong 1.60x compression ratio while maintaining a very high 42.0 dB SNR.
This concludes my initial research. I believe this tunable framework offers a new, powerful tool for the quantization landscape. Thank you for your feedback, which was instrumental in guiding this discovery. I am open to discussing these findings further.
Best regards,
Alex

### AlexSheff · 2025-09-23

Hi Titus,
Following up on our discussion, my research is now complete. After exploring multiple avenues, including the impact of bit allocation, I have a definitive answer.

My new framework, Local PQ-R, can verifiably surpass the reconstruction quality of GGML Q8_0.

The final benchmark shows that my Local PQR 5+3 configuration achieves a new SOTA for fidelity at 46.81 dB, compared to Q8_0's 45.34 dB.

This establishes a new frontier for high-fidelity 8-bit quantization. It offers users a choice: a balanced mode that beats Q8_0 on quality, or a "Quality King" mode that maximizes it.

I've compiled all the final results and analysis into a concise technical report here:
[Technical Report: A Deep Dive into the Quality vs. Compression Trade-offs of Local PQ-R](https://github.com/AlexSheff/pqr-llm-quantization/blob/17fdd0294a2f8ef201839d75dee757325342600f/Technical%20Report%3A%20Local%20PQ-R%2C%20a%20New%20SOTA%20for%208-bit%20Quantization%20Fidelity.md)
This result strengthens my proposal for a sponsored collaboration to bring this new SOTA method to the bitsandbytes community.
Looking forward to hearing your thoughts when you and the team have a moment.

Best,
Alex
