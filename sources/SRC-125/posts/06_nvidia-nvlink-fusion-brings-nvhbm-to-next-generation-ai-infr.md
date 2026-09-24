# nvidia-nvlink-fusion-brings-nvhbm-to-next-generation-ai-infrastructure

source: https://developer.nvidia.com/blog/nvidia-nvlink-fusion-brings-nvhbm-to-next-generation-ai-infrastructure/

AI factories must support increasingly large models and more complex reasoning [workloads](http://workloads.to/). To keep up with the insatiable compute demands of AI workloads, hyperscalers and AI-native companies are developing custom AI accelerators, or XPUs. Deploying these accelerators at scale requires high-bandwidth memory (HBM) to keep compute fed, sufficient package and silicon area for more compute, efficient power delivery, and a resilient supply chain. It also requires a rack-scale architecture for deploying XPUs into data center infrastructure.

[NVIDIA NVLink Fusion](https://www.nvidia.com/en-us/data-center/nvlink-fusion/) is the connective technology and IP that enables hyperscalers and AI natives to deploy custom XPUs and CPUs into the NVIDIA AI infrastructure platform. They can use the NVIDIA scale-up and scale-out technology stack, ecosystem, and MGX rack-scale architecture to reduce development and deployment complexity, improve performance, and accelerate time to market for semi-custom AI factories.

At the package level, NVHBM, complements this unified architecture. NVHBM is a custom HBM base-die technology designed and validated with leading memory vendors that enables increased memory bandwidth, better area savings, and lower power consumption. These improvements can help custom XPUs support larger models, read KV cache data faster, and improve training and large-scale inference.

## Why bandwidth, die area, and power drive accelerator design

Training, inference, and agentic AI workloads increasingly depend on high-throughput access to model weights, KV cache, and activation data. As AI systems scale from individual accelerators to rack-level compute domains, the accelerator package must balance compute logic, power delivery, thermal design, and high-bandwidth memory.

HBM places vital memory bandwidth close to the accelerator, but qualifying leading memory technology, package integration, and validation can become a bottleneck for custom accelerator programs. Through NVLink Fusion, customers gain access to NVHBM base dies that are validated with leading memory manufacturers, helping reduce integration and qualification bottlenecks.

Feature | NVHBM benefit |
|---|---|
Bandwidth | Up to 30% more memory bandwidth compared with standard HBM4e |
Area | More efficient interface connections allow up to 25% more compute die area for additional XPU capabilities |
Power | Up to 15% lower HBM power usage compared with standard HBM4e adds up savings across thousands of XPUs |

*Table 1.*


*NVHBM brings three main platform-level advantages to AI accelerator programs: higher memory bandwidth, more package and silicon area, and lower HBM power usage*

## The memory bandwidth bottleneck in modern AI accelerators

AI accelerator performance depends on how consistently compute engines are supplied with data. Higher HBM speeds increase usable memory bandwidth within a given package budget, improving the ability to serve bandwidth-intensive phases of training and inference. NVHBM delivers up to **30% more memory bandwidth per stack** compared with standard HBM4e. For memory-bound or partially memory-bound AI workloads, that translates into better accelerator utilization and higher throughput. This can increase per-user token throughput during large-model inference by moving data between HBM and compute cores faster, keeping them fed.

While NVHBM increases memory bandwidth within each accelerator, NVLink Fusion connects accelerators across larger domains so workloads can use distributed compute and memory more efficiently.

This scale-up domain is especially critical when using advanced routing techniques like [expert parallelism (EP) or WideEP](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems/). In these scenarios, different experts reside on different GPUs and require seamless, high-speed synchronization across the entire rack. [NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/), the scale-up networking fabric for AI factories, transfers activations and hidden states between experts and helps synchronize distributed caches across the scale-up fabric. NVHBM minimizes data starvation by keeping the local compute engines consistently fed.

## More package area, more flexibility

For custom AI silicon, every square millimeter matters. Accelerator designers must decide how much area to allocate to matrix engines, vector units, on-chip SRAM, cache hierarchy, control logic, memory interfaces, network-on-chip, and scale-up connectivity. A custom memory implementation can help reduce the design and package overhead associated with accessing HBM, freeing up area for workload-specific capabilities.

As AI workloads diversify, this additional die area gives hyperscalers more flexibility to optimize XPUs for inference serving, recommendation systems, multimodal pipelines, or internal training workloads. By reducing the area required for the memory interface, NVHBM enables teams to dedicate more of the chip directly to performance.

Area savings are achieved primarily through a redesigned physical memory interface (PHY). Standard HBM relies on wider interface connections, increasing the total package footprint. NVHBM uses a custom base die optimized for efficiency, featuring reduced I/O area requirements achieved by moving the memory controller into the 3D HBM stack and integrating a custom PHY.

Compared with the JEDEC HBM4e standard, this design reduces PHY and support area by up to 67%. The narrower interface also simplifies interposer routing, providing up to 80% more usable silicon across the entire layout.

As shown in Figure 1, shrinking the memory interface connections enables the central AI compute die to expand into the newly freed space. This reclamation provides up to a 30% increase in available main-die silicon for compute or other features. The additional silicon area enables XPU designers to** **add more capabilities within a fixed package footprint.

## Power savings for efficient scaling

Power is one of the hardest constraints in modern AI infrastructure. HBM power contributes to the accelerator power budget, package thermal design, rack power envelope, and data center cooling plan. NVHBM enables **15% lower HBM power usage** compared to standard HBM4e, creating additional power and thermal headroom for compute.

Power savings matter at multiple levels. At the XPU level, lower HBM power can improve performance per watt and create room for more compute or higher sustained utilization. At the rack level, it can help reduce pressure on power delivery and cooling systems. At AI factory scale, even modest reductions in memory subsystem power can add up across thousands of accelerators. When compounded across an entire **1-gigawatt** **data center** using 2,000W XPUs, power savings can enable up to **15,000** **additional XPUs** in compute headroom.

The benefit is especially important for large-model inference. XPUs must repeatedly read model weights and KV-cache data while serving users at low latency and high throughput. Reducing the energy spent moving that data can help support faster inference on large models, larger batch sizes, and more efficient use of deployed power.

## Combining NVLink Fusion with NVHBM at rack scale

NVHBM boosts XPU performance and efficiency at the chip level. NVLink Fusion enables hyperscalers and AI natives to connect their XPUs to the rest of the NVIDIA AI platform. By compounding a 30% increase in memory bandwidth, 25% more die area, and 15% HBM power savings, these co-designed architectural improvements translate into a significant 30% overall end-to-end performance increase per XPU.

This connectivity is achieved through the NVLink Fusion chiplet, which bridges custom XPUs and the NVLink fabric, connecting all XPUs in a rack into a single scale-up domain. Now in its sixth generation, NVLink is the only proven, purpose-built scale-up networking fabric for AI factories, delivering leading performance and intelligent resiliency. Upstream, the XPUs can connect to the CPUs via NVLink-C2C.

NVLink Fusion adopters can combine custom XPUs and CPUs with NVIDIA scale-up and scale-out technology stack and ecosystem to reduce development and deployment complexity, increase performance, and accelerate time to market for semi-custom AI factories. And by standardizing on a single unified architecture, NVLink Fusion simplifies operations across the data center, enables flexible reprovisioning of data center capacity, and enables custom AI XPUs to integrate with GPUs for heterogeneous compute.

## The next phase of custom AI silicon

NVLink Fusion provides a common scale-up foundation for GPUs, custom XPUs and CPUs, networking, and rack-level software. NVHBM complements that foundation with greater memory performance, compute density, HBM power efficiency, and supply resiliency for next-generation accelerators. These technologies give partners a more direct path from custom AI accelerator design to rack-scale deployment and production volume.

Learn more about [NVLink Fusion](https://www.nvidia.com/en-us/data-center/nvlink-fusion/) and [industry adoption of NVHBM](https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory).

## Start the discussion at forums.developer.nvidia.com
