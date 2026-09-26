# [Issue #1064] 请问模型的创新点都有哪些？

source: https://github.com/PaddlePaddle/ERNIE/issues/1064
state: closed | updated: 2025-07-31T02:03:40Z
labels: 

## 正文

(empty)

## 评论 (1)

### nepeplwu · 2025-07-29

@harmony2ww 感谢反馈，ERNIE4.5模型的创新点在paper中有完整的描述，可以查看下paper：https://yiyan.baidu.com/blog/publication/ERNIE_Technical_Report.pdf

> Our model family is characterized by three key innovations:
> 1. Multimodal Heterogeneous MoE Pre-Training: Our models are jointly trained on both textual and visual modalities to learn from multimodal information and improve performance on tasks involving text understanding and generation, image understanding, and cross-modal reasoning. To achieve this without interference between modalities, we design a heterogeneous MoE structure, incorporate modality-isolated routing, and employ both router orthogonalization loss and multimodal token-balanced loss. This architecture ensures that both modalities are effectively represented, enabling mutual reinforcement during training.
> 2. Scaling-Efficient Infrastructure: We propose a novel heterogeneous hybrid parallelism and hierarchical load balancing strategy for efficient training of ERNIE 4.5 models. Through intranode expert parallelism, memory-efficient pipeline scheduling, FP8 mixed-precision training, and fine-grained recomputation methods, we achieve remarkable pre-training throughput. For inference, we propose a multi-expert parallel collaboration method and a convolutional code quantization algorithm to achieve 4-bit/2-bit near-lossless quantization. Furthermore, we introduce PD disaggregation with dynamic role switching for effective resource utilization to enhance inference performance for ERNIE 4.5 MoE models. Built on PaddlePaddle, ERNIE 4.5 delivers high-performance inference across a wide range of hardware platforms.
> 3. Modality-Specific Post-Training: To meet the diverse requirements of real-world applications, we fine-tune variants of the pre-trained model for specific modalities. Our LLMs are optimized for general-purpose language understanding and generation. The VLMs focus on vision-language understanding and support both thinking and non-thinking modes. Each model employs a combination of Supervised Fine-tuning (SFT), Direct Preference Optimization (DPO) or a modified reinforcement learning method named Unified Preference Optimization (UPO) for post-training.
