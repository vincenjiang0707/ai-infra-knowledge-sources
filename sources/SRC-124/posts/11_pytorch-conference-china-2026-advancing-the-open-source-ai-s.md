# pytorch-conference-china-2026-advancing-the-open-source-ai-stack

source: https://pytorch.org/blog/pytorch-conference-china-2026-advancing-the-open-source-ai-stack/

PyTorch Conference China 2026 brought the PyTorch community together in Shanghai on September 8–9 alongside [KubeCon + CloudNativeCon and OpenInfra Summit](https://www.lfopensource.cn/kubecon-cloudnativecon-openinfra-summit-pytorch-conference-china/), following sponsor-hosted co-located events on September 7. Technical discussions spanned models, frameworks, distributed training, inference, hardware, cloud native infrastructure, and agents.

“Open Source for the AI Era” framed work across those layers. Across co-located sessions, keynotes, technical demonstrations, a PyTorch Foundation press conference, community meetings, and conversations at the PyTorch booth, the program covered hardware adaptation, training and serving, open infrastructure, accelerator integration, and collaboration across open source communities.

[PyTorch Foundation welcomed Alibaba Cloud, Ant Group, and Cambricon](https://pytorch.org/blog/alibaba-cloud-ant-group-cambricon-and-huawei-come-together-in-shanghai-to-advance-the-open-source-ai-stack-at-pytorch-conference-china/) as new members, joining Huawei and other existing Foundation members.



## Building Frontier Intelligence in the Open

**Speaker:** Mark Collier, Executive Director, PyTorch Foundation

Mark’s September 8 keynote focused on an open ecosystem where researchers, developers, model builders, and hardware companies can work together across an expanding landscape of models and compute. The session connected PyTorch with the path from experimentation to production, new accelerator architectures, and the infrastructure that ultimately runs AI workloads.

## Additional Keynotes Across the Open Source AI Stack

The keynote program brought together speakers working across models, PyTorch, cloud native infrastructure, accelerators, serving, and agents.

### Day 1

**From Open Source Adoption to Open Source Innovation: China’s Next Chapter**

**Speaker:** Professor Lu Shouqun

**Organization:** China OSS

**Open Source for the AI Era**

**Speakers:** Jonathan Bryce and Horace Li

**Organization:** The Linux Foundation

**Beyond Multimodal: Building Full-Modal AGI via Open-Weight**

**Speaker:** Ryan Lee

**Organization:** MiniMax

**Operating Frontier Intelligence at Scale**

**Speakers:** Chris Aniszczyk and Xiao Zhang

**Organizations:** The Linux Foundation and Dynamia.ai

**Tidal Auto-scaling for Training and Inference Based on Kubernetes + KEDA**

**Speakers:** Jun Zheng and Tan Pei Xiang

**Organization:** China Merchants Bank

**Ascend & PyTorch: Pioneer New AI Open Ecosystem**

**Speaker:** Liang Zhang

**Organization:** Huawei

**Towards Device-agnostic PyTorch: Building Unified Infrastructure for a Multi-Backend Ecosystem**

**Speaker:** Wei Li

**Organization:** Cambricon

**Inside vLLM: Production Best Practices, Model Integration and Road Map**

**Speaker:** Kaichao You

**Organization:** Inferact Inc.

**PD Disaggregation vLLM Deployment on Alternative AI Accelerators Using llm-d**

**Speakers:** 纪飞 王 and Mengxuan Li

**Organizations:** Dynamia and Dynamia.ai

**Building an Agent Runtime with Open Infrastructure**

**Speakers:** Yaya Xia and Xu Wang

**Organization:** Ant Group

**What AI Agents Need from Open Infrastructure**

**Speaker:** Yaya Xia

**Organization:** Ant Group

### Day 2

**Welcome Back + Opening Remarks**

**Speakers:** Jonathan Bryce and Horace Li

**Organization:** The Linux Foundation

**What Powers Frontier Intelligence**

**Speaker:** Thierry Carrez

**Organization:** OpenInfra Foundation

**Road from Kata Containers to Confidential Containers + GPUs: From First Commit to CNCF Incubation**

**Speaker:** Zvonko Kaiser

**Organization:** NVIDIA

**HyperParallel: A SuperPoD-Aware Distributed Acceleration Library**

**Speakers:** Teng Su and Shendi Wang

**Organization:** Huawei

**Build a Unified Heterogeneous AI Computing Ecosystem for PyTorch**

**Speaker:** Zesheng Zong

**Organization:** Huawei

**Serving Qwen at Scale: Multi-Cluster AI Infrastructure on Karmada**

**Speaker:** Jionghang Cai

**Organization:** Alibaba Cloud

**Meet the Community Behind the Open Source AI Stack**

**Speakers:** Jane Lyu; Fupan Li; Zesheng Zong; Hiu Yeung, Sunny Chan

**Organizations:** The Linux Foundation; Ant Group; Huawei; TCC Consulting Limited

**Building Frontier AI Infra: SGLang and Miles**

**Speaker:** Ke Bao

**Organization:** RadixArk

**A Cloud Native Stack from Bare Metal to Tokens for Large-Scale AI Inference**

**Speaker:** Trong Vinh Nguyen

**Organization:** Viettel

## Alibaba Cloud, Ant Group, and Cambricon Join PyTorch Foundation

PyTorch Foundation announced three new members in Shanghai on September 8.

**Alibaba Cloud** joined as a **Platinum Member**, with work spanning cloud infrastructure and the Qwen model family.

**Ant Group** joined as a **Gold Member**, bringing experience with production AI at financial-services scale.

**Cambricon** joined as a **Platinum Member**. Cambricon develops MLU accelerators and follows an “Upstream First” approach to its PyTorch contributions. Its contributions span torch.compile, Eager Operators, Device Runtime, Distributed Computing, AMP, Dataloader, and Profiler.

Representatives from Alibaba Cloud, Ant Group, Cambricon, and Huawei took the keynote stage to speak about the open AI stack across **hardware, models, and infrastructure**.

**ANY MODEL · ANY CHIP · ANY CLOUD · ANY AGENT**

[Read the full membership announcement.](https://pytorch.org/blog/alibaba-cloud-ant-group-cambricon-and-huawei-come-together-in-shanghai-to-advance-the-open-source-ai-stack-at-pytorch-conference-china/)

[Read more about Cambricon joining PyTorch Foundation as a Platinum Member.](https://pytorch.org/blog/cambricon-joins-the-pytorch-foundation-as-a-platinum-member/)

## One Open Source AI Stack

At the September 8 press conference, PyTorch Foundation outlined an open source AI stack spanning applications and agents, building and delivering intelligence, running and scaling AI workloads, infrastructure and isolation, and heterogeneous compute.

PyTorch, vLLM, and Ray represented the layer focused on building and delivering intelligence. Kubernetes, KServe, Kueue, OpenTelemetry, and llm-d represented the layer focused on running and scaling AI workloads. OpenStack and Kata Containers represented infrastructure and isolation. Those software layers run across NPUs, CPUs, GPUs, and other accelerators.

PyTorch Foundation members work across four areas:

**Any Model:**AI labs and builders**Any Chip:**silicon and systems**Any Cloud:**clouds and platforms**Any Agent:**production and services

Many members work across more than one layer. The Foundation summarized the model directly: **“No single organization builds the whole system. Together, our members span it.”**

## China in the Stack

**100+ China-based developers contribute to PyTorch across 40+ affiliated organizations.**

PyTorch Foundation members represented in the China-focused overview included **Alibaba Cloud, Cambricon, and Huawei** as Platinum Members, **Ant Group** as a Gold Member, and **Beijing Academy of Artificial Intelligence (BAAI)** as an Associate Member.

The September 8 membership announcement also noted that **more than 250 organizations across China contribute to PyTorch Foundation projects**, including DeepSpeed, Helion, PyTorch, Ray, Safetensors, and vLLM.

The conference also highlighted open model development and optimization through the open software layer.

For **DeepSeek-R1**, one case study covered optimization through kernels, routing, parallelism, and serving on the same GB300 hardware six months later. In the configuration presented, the optimized system delivered **2.77x throughput** and **60% lower token cost**. The source cited in the conference material was NVIDIA, 2026.

A second example showed the share of **OpenRouter token traffic served by open-weight models developed in China** increasing from **2% in late 2024 to 45% in April 2026**. The source cited in the conference material was Mozilla.

## Join the PyTorch TAC Accelerator Integration Working Group

AI computing hardware faces heterogeneity challenges with high adaptation costs and a lack of unified standards.

The **PyTorch TAC Accelerator Integration Working Group**, co-chaired by Huawei and Intel, delivers standardized hardware onboarding guidelines, a cross-repo CI testing mechanism, generalized device-aware test suites, and platform incubation workflows.

Zesheng Zong shared the Accelerator Integration Working Group’s achievements and future roadmap during PyTorch Conference China, including **refined device-agnostic APIs** and an **expanded multi-backend test matrix**.

Hardware vendors and developers interested in co-building an open, efficient heterogeneous computing ecosystem for PyTorch can participate in the Accelerator Integration Working Group.

[Join a PyTorch Foundation Working Group.](https://pytorch.org/working-groups/)

## Community in Shanghai

PyTorch Foundation Technical Advisory Council members met in Shanghai during Day 1 of PyTorch Conference China 2026.

At the PyTorch booth, developers, contributors, hardware vendors, and attendees discussed work across the open source AI ecosystem.

## September 7: Starting with Diverse Hardware

Two September 7 co-located events highlighted the challenges created by increasingly heterogeneous AI hardware and the software work required to support it.

### Open Computing: Building Open Software for Diverse Hardware

**Speaker:** Mark Collier, Executive Director, PyTorch Foundation

**Host:** FlagOS

Mark Collier joined experts from Beijing Academy of Artificial Intelligence (BAAI), Shanghai AI Laboratory, vLLM, SGLang, NVIDIA, and others in a technical discussion about open system software for diverse hardware.

AI chip diversification creates repeated integration work across operators, compilers, training and inference frameworks, communications, and other parts of the software stack. Talks focused on technical roadmaps and collaboration models for a multi-chip AI system software stack, including hardware-software co-optimization across emerging chip architectures.

### Hardware-Aware AI: Building PyTorch Workloads Across Accelerators

**Opening remarks:** Mark Collier, Executive Director, PyTorch Foundation

**Host:** Huawei

Huawei’s co-located session focused on PyTorch workloads across GPUs, NPUs, and XPUs, including framework adaptation, operators, compiler co-optimization, workload migration, and performance tuning.

## Register for PyTorch Conference North America 2026

If you couldn’t join us in Shanghai, PyTorch Conference North America 2026 is the next chance to hear directly from maintainers, researchers, developers, and AI engineers working across the open source AI stack.

PyTorch conferences are the open source AI community’s town square, where what’s next gets decided.

PyTorch Conference North America comes to San Jose October 20–21, with maintainers from PyTorch, vLLM, DeepSpeed, and Ray among the speakers.
