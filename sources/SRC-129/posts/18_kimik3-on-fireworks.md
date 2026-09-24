# kimik3-on-fireworks

source: https://fireworks.ai/blog/kimik3-on-fireworks

Kimi K3 is open-weight today, and available Day-0 for both inference and training on Fireworks. It delivers frontier-level intelligence, the top open model in the world, at a fraction of closed-model cost. It is #1 at frontend code, strong at writing, and it reliably finishes the long, multi-step agentic tasks where other models stall.

Michele Catasta, the President of Replit, told us,

"Kimi K3 on Replit Design exceeded our expectations. Unprecedented product design and UI capabilities, at a fraction of the cost we've come to expect from frontier models."

Silas Alberti, SVP of Research at Cognition, highlighted:

"We trust Fireworks for high-quality Kimi K3 inference, allowing us to evaluate the model smoothly on FrontierCode. The results made it clear that Kimi K3 represents a step change for open-source models."

This is a turning point. Open models have crossed the line where they match closed frontier quality on real work while costing far less. That changes the default: start with an open model like Kimi K3 for the bulk of your tasks, see exactly what you are spending, and route to specialized intelligence only where a task demands it.

With Kimi K3 on Fireworks, you own your roadmap. Training a 3T-class model can start from your laptop, no infrastructure setup, no deployments to bring up. Just start a session and send tokens. And we keep your private data private. With Fireworks, specialized intelligence becomes a moat that compounds with every cycle.

That ownership comes with the guarantees regulated teams need: US-hosted inference and zero data retention, on an API that stays out of your way.

Brendan Foody, Mercor CEO, put it this way:

"Evaluating new models against our benchmarks usually requires trade-offs between performance, cost and scale, but Kimi K3 on Fireworks delivered across the board. The performance is top-tier, the serverless scaling is seamless, and the Zero Data Retention assurance gives us full confidence at scale."

That ownership changes the economics. What matters is your cost per finished task, set by how often the model succeeds on the first try and how many steps it takes. Tailoring Kimi K3 raises the success rate and shortens the trajectory, so budget shifts from generic tokens to the differentiation that makes your company unique.

Kimi K3 is the first open model to reach 2.8 trillion parameters, providing frontier-level reasoning that rivals closed models like Fable 5, Opus 5 and GPT 5.5. Kimi K3 is designed to handle the most demanding use cases in software development, cybersecurity, knowledge work, multi-modal and visual work. What makes K3 credible is that most of the standout results come from independent benchmarks:

Last week, [our research team shared how K3 matches Fable](https://fireworks.ai/blog/kimik3-fable) on quality for a fraction of the cost in long-running agentic workflows. By routing tasks between K3 and Fable, you can unlock the best possible performance for your specific needs.

Following last week’s Opus 5 release, our team benchmarked it head-to-head against Kimi K3. We found Kimi K3 delivers matching performance at up to 5x better cost efficiency per task. Independent benchmarks like [Vals Index](https://www.vals.ai/benchmarks/vals_index) found the exact same thing in the quality of the K3 against Opus.

| Task | Model | Accuracy | $/task | Turns/task |
|---|---|---|---|---|
Task | Model | Accuracy | $/task | Turns/task |
SWE (480) | Kimi K3 | 92.7% | $0.52 | 55.6 |
Opus 5 | 94.8% | $1.05 | 37.9 | |
Algorithmic(100) | Kimi K3 | 88.0% | $0.064 | 3.4 |
Opus 5 | 88.0% | $0.176 | 4.1 | |
Terminal (83) | Kimi K3 | 81.9% | $0.35 | 11.6 |
Opus 5 | 85.5% | $1.61 | 18.7 |

Hosting K3 yourself isn’t practical for most engineering teams. Moonshot recommends running it on a cluster of 64+ accelerator supernodes(GPUs). This means huge upfront hardware spend, and endless money wasted on idle GPUs. Fireworks lets you skip the cluster headaches, and instead of burning budget on dedicated GPU reservations, you pay per token and get frontier-level reasoning wherever you need it.

K3 is not just bigger; it is more efficient by design. Moonshot improved the design by changing how information flows across the model. Our team at Fireworks put together custom kernels for Kimi Delta Attention, FP4 MoE kernels, and adapted decode kernels to unlock K3’s full performance. The model architecture brings a new Kimi Delta Attention architecture and refined attention residuals. They scaled up the Mixture of Experts (MoE), activating 16 out of 896 experts with the Stable Latent MoE. This approach delivered 2.5 times the scaling efficiency compared to Kimi K2. This result is a model that delivers frontier reasoning for large, long-horizon tasks, while remaining cost-effective for high-volume production workloads.

| Spec | Kimi K3 | Kimi K2.7 | GLM 5.2 |
|---|---|---|---|
Spec | Kimi K3 | Kimi K2.7 | GLM 5.2 |
Tier | Frontier | Coding | Coding |
Modalities | Text and Vision | Text and Vision (MoonViT) | Text |
Total Parameters | 2.8T | 1T MoE | 753 MoE |
Input Context Length (Tokens) | 1M | 256k | 1M |
Active Parameters | 104B | 32B | 40B |
Activation Rate | 3.7% | 3.20% | 5.31% |
# of Experts | 896 | 384 | 256 |

You can use Kimi K3 on Fireworks interchangeably with most of your AI workloads. Our serverless platform simplifies using the model to just drop in an API key. You don’t have to think about GPU management or API compatibility.

Fireworks has increased default rate limits by over 10x for Serverless inference, launched [Priority Serverless](https://docs.fireworks.ai/serverless/overview) for better reliability, and optimized [Fast Serverless](https://docs.fireworks.ai/serverless/overview) for better token speed. The best part is you don’t need to rent GPUs for all of these options: just pay for the tokens you use like you do with Claude and Open AI.

“When we did a bakeoff with other providers, Fireworks won simply because it worked consistently. Whenever we deploy any model, it works the first time. No tuning, no fiddling. What I don't want is getting stuck in a 3-week development cycle trying to make a model work.”

— Travis Rehl, CTO Innovation Solutions

For work you can delay, [ Batch mode](https://docs.fireworks.ai/guides/batch-inference) runs jobs at off-peak times for 50% off. It's how teams use K3's vision reasoning to process whole folders of images, captioning, labeling, or cropping, and the same savings apply to anything batchable, like running evals.

Today, we’re also launching [ US-only Serverless](https://docs.fireworks.ai/serverless/us-only-serverless) endpoints, starting with Kimi K3. Over the coming days and weeks, we are adding other US-only endpoints for the most popular models on Fireworks. Financial services, healthcare, and other regulated companies that require US data residency can now sign up and hit an endpoint with

For these security-sensitive workloads where data privacy is non-negotiable, Fireworks operates on [Zero Data Retention](https://docs.fireworks.ai/guides/security_compliance/data_handling) by default. We never log or store your prompt or generation data for open models without your explicit opt-in, giving your team complete data control and peace of mind.

Fine-tuning a frontier model is usually a heavy lift. Now in private preview: **Fireworks Serverless Training.**

It is a one-line code change from our reserved training SDK. Write a standard Python loop, point it at our Serverless Training API, and start iterating in seconds. With the K3 launch we are opening private preview access to a shared GPU pool, so there is no GPU reserved capacity to provision and you pay per token instead of by the reserved hour.

Want the full walkthrough? Part two takes you through everything you need to know to train K3: what LoRA is, how to shape the reward, when a small adapter is enough, and what it costs. [Click Here ](https://fireworks.ai/blog/K3-LoRA-Training)
