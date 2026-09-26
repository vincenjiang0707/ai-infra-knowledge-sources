source: https://github.com/vllm-project/vllm-ascend

| [ About Ascend](https://www.hiascend.com/en/) |

[|](https://docs.vllm.ai/projects/ascend/en/latest/)

**Documentation**[|](https://docs.vllm.ai/projects/ascend/en/latest/user_guide/support_matrix/)

**Support Matrix**[|](https://slack.vllm.ai)

**#SIG-Ascend**[|](https://discuss.vllm.ai/c/hardware-support/vllm-ascend-support)

**Users Forum**[|](https://tinyurl.com/vllm-ascend-meeting)

**Weekly Meeting**
**English** | **中文**

*Latest News* 🔥

- [2026/09] We released the new release candidate
[v0.26.0rc1](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.26.0rc1)! Please follow the[official guide](https://docs.vllm.ai/projects/ascend/en/v0.26.0rc1/)to start using vLLM Ascend Plugin on Ascend. - [2026/08] We released the new official version
[v0.23.0](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.23.0)! Please follow the[official guide](https://docs.vllm.ai/projects/ascend/en/v0.23.0/)to start using vLLM Ascend Plugin on Ascend. - [2026/05] We released the new official version
[v0.18.0](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.18.0)! Please follow the[official guide](https://docs.vllm.ai/projects/ascend/en/v0.18.0/)to start using vLLM Ascend Plugin on Ascend. - [2026/02] We released the new official version
[v0.13.0](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.13.0)! Please follow the[official guide](https://docs.vllm.ai/projects/ascend/en/v0.13.0/)to start using vLLM Ascend Plugin on Ascend.

## More

- [2025/12] We released the new official version
[v0.11.0](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.11.0)! Please follow the[official guide](https://docs.vllm.ai/projects/ascend/en/v0.11.0/)to start using vLLM Ascend Plugin on Ascend. - [2025/09] We released the new official version
[v0.9.1](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.9.1)! Please follow the[official guide](https://docs.vllm.ai/projects/ascend/en/v0.9.1/tutorials/large_scale_ep.html)to start deploying large-scale Expert Parallelism (EP) on Ascend. - [2025/08] We hosted the
[vLLM Beijing Meetup](https://mp.weixin.qq.com/s/7n8OYNrCC_I9SJaybHA_-Q)with vLLM and Tencent! Please find the[meetup slides](https://drive.google.com/drive/folders/1Pid6NSFLU43DZRi0EaTcPgXsAzDvbBqF). - [2025/06]
[User stories](https://docs.vllm.ai/projects/ascend/en/latest/community/user_stories/index.html)page is now live! It kicks off with LLaMA-Factory/verl/TRL/GPUStack to demonstrate how vLLM Ascend assists Ascend users in enhancing their experience across fine-tuning, evaluation, reinforcement learning (RL), and deployment scenarios. - [2025/06]
[Contributors](https://docs.vllm.ai/projects/ascend/en/latest/community/contributors.html)page is now live! All contributions deserve to be recorded, thanks for all contributors. - [2025/05] We've released the first official version
[v0.7.3](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.7.3)! We collaborated with the vLLM community to publish a blog post sharing our practice:[Introducing vLLM Hardware Plugin, Best Practice from Ascend NPU](https://blog.vllm.ai/2025/05/12/hardware-plugin.html). - [2025/03] We hosted the
[vLLM Beijing Meetup](https://mp.weixin.qq.com/s/VtxO9WXa5fC-mKqlxNUJUQ)with vLLM team! Please find the[meetup slides](https://drive.google.com/drive/folders/1Pid6NSFLU43DZRi0EaTcPgXsAzDvbBqF). - [2025/02] vLLM community officially created
[vllm-project/vllm-ascend](https://github.com/vllm-project/vllm-ascend)repo for running vLLM seamlessly on the Ascend NPU. - [2024/12] We are working with the vLLM community to support
[[RFC]: Hardware pluggable](https://github.com/vllm-project/vllm/issues/11162).

vLLM Ascend (`vllm-ascend`

) is a community maintained hardware plugin for running vLLM seamlessly on the Ascend NPU.

It is the recommended approach for supporting the Ascend backend within the vLLM community. It adheres to the principles outlined in the [[RFC]: Hardware pluggable](https://github.com/vllm-project/vllm/issues/11162), providing a hardware-pluggable interface that decouples the integration of the Ascend NPU with vLLM.

By using vLLM Ascend plugin, popular open-source models, including Transformer-like, Mixture-of-Experts (MoE), Embedding, Multi-modal LLMs can run seamlessly on the Ascend NPU.

For detailed information on supported models and features, please refer to the [support matrix](https://docs.vllm.ai/projects/ascend/en/latest/user_guide/support_matrix/).

[ DeepWiki](https://deepwiki.com/vllm-project/vllm-ascend) is a dynamic knowledge base collaboratively maintained by the community and AI, designed to provide you with deeper technical insights beyond conventional documentation. If official documentation serves as a "quick start" guide to help you get going, the DeepWiki is your technical companion for "deep understanding". Here, you can explore: core architecture and design principles, key source code interpretations, technical context, and decision-making logic.

Whether you are a performance tuner looking to deploy vLLM-Ascend in production or a contributor aiming to build upon it for secondary development, DeepWiki offers invaluable references for you. Welcome to explore now and join us in delving deep into the technical core of vLLM-Ascend.

- Hardware: Atlas 800I A2 Inference series, Atlas A2 Training series, Atlas 800I A3 Inference series, Atlas A3 Training series, Atlas 300I Duo (Experimental)
- OS: Linux
- Software:
- Python >= 3.10, < 3.13
- CANN == 9.1.0 (For Ascend HDK version, please refer to the
[Release Notes](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910/softwareinst/releasenote/9.1.0/release-notes.md)) - PyTorch == 2.10.0, TorchNPU == 2.10.0.post4
- vLLM (the same version as vllm-ascend)


If you need to access Ascend NPU computing resources for development or testing, please visit the [HiDevLab - Online Development](https://hidevlab.huawei.com/online-develop-intro) page on the Huawei HiDevLab platform to apply for and use them.

Please use the following recommended versions to get started quickly:

| Version | Release type | Doc |
|---|---|---|
| v0.26.0rc1 | Release candidate | See
|

[QuickStart](https://docs.vllm.ai/projects/ascend/en/v0.23.0/quick_start.html)and[Installation](https://docs.vllm.ai/projects/ascend/en/v0.23.0/installation.html)for more detailsvllm-ascend has a main branch and a dev branch.

**main**: main branch, corresponds to the vLLM main branch, and is continuously monitored for quality through Ascend CI.**releases/vX.Y.Z**: development branch, created alongside new releases of vLLM. For example,`releases/v0.13.0`

is the dev branch for vLLM`v0.13.0`

version.

Below are the maintained branches:

| Branch | Status | Note |
|---|---|---|
| main | Maintained | CI commitment for vLLM main branch and vLLM v0.30.0 tag |
| releases/v0.13.0 | Maintained | Only bug fixes are allowed, and no new release tags anymore. |
| releases/v0.18.0 | Maintained | CI commitment for vLLM 0.18.0 version |
| releases/v0.23.0 | Maintained | CI commitment for vLLM 0.23.0 version |
| rfc/ | Maintained |
|

Please refer to [Versioning policy](https://docs.vllm.ai/projects/ascend/en/latest/community/versioning_policy.html) for more details.

See [CONTRIBUTING](https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/index.html) for more details, which is a step-by-step guide to help you set up the development environment, build and test.

We welcome and value any contributions and collaborations:

- Please let us know if you encounter a bug by
[filing an issue](https://github.com/vllm-project/vllm-ascend/issues) - Please use
[User forum](https://discuss.vllm.ai/c/hardware-support/vllm-ascend-support)for usage questions and help.

- vLLM Ascend Weekly Meeting:
[https://tinyurl.com/vllm-ascend-meeting](https://tinyurl.com/vllm-ascend-meeting) - Wednesday, 15:00 - 16:00 (UTC+8,
[Convert to your timezone](https://dateful.com/convert/gmt8?t=15))

Apache License 2.0, as found in the [LICENSE](https://github.com/vllm-project/vllm-ascend/blob/main/LICENSE) file.