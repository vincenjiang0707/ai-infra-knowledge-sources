# building-an-adaptive-agentic-cybersecurity-system-with-nvidia-nemotron

source: https://developer.nvidia.com/blog/building-an-adaptive-agentic-cybersecurity-system-with-nvidia-nemotron/

AI is changing the pace of cybersecurity. Agentic systems can coordinate work and pursue complex objectives over long horizons. Security teams are beginning to apply agents across security operations, but many implementations remain anchored to existing alerts, predefined workflows, and known attack behaviors. The harder problem is identifying what defenses miss and turning those gaps into reliable coverage. This requires repeatedly testing adaptive attacks in an organization’s unique environment and validating candidate detections against normal enterprise activity.

Continuous offense-defense testing creates this feedback loop. Controlled attacks produce the telemetry and ground truth defensive agents need to expose gaps, improve coverage, and retest. However, the end-to-end cycle still requires significant manual effort. Could red and blue agents powered by open models and specialized harnesses operate this loop at machine speed and scale?

NVIDIA and CrowdStrike evaluated an agentic attack-defense system in an isolated environment modeled on NVIDIA accelerated computing infrastructure. On the defensive side, NVIDIA Nemotron models customized for cybersecurity operate within CrowdStrike SafeMind, its agentic cybersecurity system. CrowdStrike reports that its Blue Solano defensive model is more accurate than the leading proprietary frontier model tested, at 99% lower cost, in CrowdStrike internal evaluations. For this evaluation, the optimized open-model configuration paired [NVIDIA Nemotron 3 Ultra](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) for defensive orchestration with a fine-tuned [Nemotron 3 Super](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/) for detection generation.

This post shares how Nemotron models and specialized agent harnesses work together with CrowdStrike’s agentic system, how it was deployed and evaluated, and how the resulting detections performed across independently seeded attack runs.

**Turning offense and defense into a continuous learning loop **

Traditional red-and-blue team exercises depend on manual handoffs: the red team executes an attack, the blue team reviews the resulting telemetry, detection engineers develop or update detections, and the red team retests them. Each handoff takes time, limiting the number of iterations and attack variations teams can evaluate. An offensive-defensive agentic system connects these activities into a repeatable closed loop that can operate at machine speed. Within an isolated representative environment, each run produces attack traces and sensor telemetry used to create or refine detections. The resulting context returns to the red-agent harness, which adapts and tests alternative attack or evasion paths until it finds no further viable route within the representative environment.

The workflow has four connected stages:

**Execute and capture.**Starting with a threat-informed objective, the red-agent harness selected and executed an attack path inside the representative environment. Its action trace recorded each step, while CrowdStrike Falcon endpoint sensors captured the corresponding telemetry.**Process and reconstruct.**The blue-agent harness then received the action trace, sensor telemetry, and broader attack context. Using information about the available data sources and CrowdStrike detection-engineering expertise as grounding context, it determined which parts of the event sequence could be reconstructed, which existing detections triggered, and where visibility or detection gaps remained.**Generate and validate.**Based on this analysis, the blue-agent harness generated candidate detections. The validation harness checked each candidate, backtested it against the captured telemetry, returned failures for correction, and sent validated detections to the detection engine.**Retest, adapt, and repeat.**After a validated detection was deployed, an independently seeded attack retested the same objective. Detection and alert context returned to the red-agent harness, which adapted and explored alternative attack or evasion paths, producing new traces and telemetry for the blue-agent harness.

Each cycle is designed to strengthen defensive coverage while forcing the offense to find a harder path with full knowledge of the defense. The loop continues until no further viable path remains within the modeled environment.

**Building a representative test environment**

To enable safe, realistic testing, NVIDIA provided a sanitized, natural-language specification representing its accelerated computing infrastructure. An agent-assisted workflow translated the specification into an isolated target cyber agent environment instrumented with Falcon platform sensors.

The evaluation used attack paths and observable milestones to measure progress from action traces and sensor telemetry rather than the agent’s own claims. NVIDIA security experts reviewed the environment and threat paths for realism. The same reviewed environment supported every attack run, detection test, and evaluation metric, enabling consistent comparisons across configurations.

**Specializing the defensive harness**

The next challenge was turning the resulting attack traces and telemetry into detection rules that could pass technical and behavioral validation. Open agent harnesses already provide capabilities such as planning, tool use, context management, and iterative correction. The [Open Secure AI Alliance](https://blogs.nvidia.com/blog/open-secure-ai-alliance/) is helping expand the broader ecosystem of open models, harnesses, and tools for cybersecurity.

The defensive harness combined six mechanisms:

**Schema knowledge base.**A tool allowed agents to enumerate supported Falcon sensor schemas, fields, and query syntax, preventing invented fields and invalid queries.**Telemetry grounding.**Red-agent traces, Falcon telemetry, and broader attack context anchored the workflow in observed events and relationships, reducing unsupported or hallucinated connections.**Specialized detection authoring.**A customized[Nemotron 3 Super](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/)served as a bounded expert for generating and repairing detections, separating this specialized task from the longer orchestration context.**Artifact linting.**Automated checks rejected syntax errors, unsupported fields, and detections tied to specific IP addresses, hosts, users, or subnets. Failures returned guidance for rewriting the detection around behavioral signals instead of environment-specific strings.**Detection replay.**Each candidate was replayed against captured attack telemetry. Detections that produced no match were rejected and returned for correction, catching candidates that appeared valid but failed to detect the recorded activity.**Independent review.**A separate judge with a fresh context evaluated each detection for behavioral alignment, robustness, and appropriate use of multiple signals, catching quality gaps missed by linting and replay.

Failed checks returned structured feedback to the blue-agent workflow for correction and another attempt. Together, these mechanisms encoded practices normally applied through manual detection-engineering review, making detection generation grounded, testable, and correctable rather than merely plausible.

**Customizing Nemotron for defensive orchestration and detection generation**

Open models such as Nemotron can be post-trained with domain data, deployed with proprietary context in controlled environments, and optimized for cost and scale. In the evaluated open-model configuration, [Nemotron 3 Ultra](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/) reconstructed attack sequences, planned detection-engineering steps, and invoked tools. When a detection required writing or repair, a customized [Nemotron 3 Super](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/) served as a bounded expert. This separation kept workflow orchestration distinct from specialized detection authoring.

To create this specialized expert, CrowdStrike used Nemotron 3 Super as the base for its NL2LogScale model, then applied continual pretraining on cybersecurity knowledge, supervised fine-tuning, and reinforcement learning with verifiable rewards. Fine-tuning used 9,349 detection-generation and multistep repair examples spanning 59 programmatically generated error types. The training data combined request rephrasings from Nemotron 3 Super, real Falcon LogScale execution errors, and quality-reviewed reasoning traces from Nemotron 3 Ultra.

For reinforcement learning, the training workflow used [NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/gym) to validate and execute generated queries in Falcon LogScale. Invalid queries received real engine errors and up to five repair attempts, with unresolved attempts receiving zero reward. Valid generated and reference queries ran against the same synthetic logs, and the F1 overlap between their returned events supplied the reward. [NVIDIA NeMo RL](https://github.com/nvidia-nemo/rl) supported group relative policy optimization to update the model. For reinforcement learning, the workflow used NeMo Gym to validate generated queries and NeMo RL to update the model based on verifiable results.

**Evaluating the complete agent system from backtest to live fire**

A detection may detect the recorded attack used to create it, but fail on a new execution of the same behavior. Therefore, we evaluated each system in two stages: backtesting against the recorded attack, followed by live-fire testing against eight new attacks from the same scenario family. Every passing detection was deployed verbatim to the live detection engine. An independent third-party model judged whether each match represented the intended attack behavior, and results were averaged across independently seeded authoring sessions.

**Backtesting against the recorded attack**

With Nemotron 3 Ultra and the default harness, an average of 16.5% of generated detections detected the recorded attack across eight independently seeded sessions. Retaining Ultra while adding the tuned harness, customized Nemotron 3 Super, domain context, tools, and validation raised the mean to 41.9% across six sessions, a 2.5x improvement. Because the optimized configuration changed both the harness and model stack, the gain reflects the complete open pipeline rather than an isolated model ablation.

## Evaluating generalization through live-fire testing

During live-fire testing, 11 backtest-passing detections from the optimized open pipeline powered by Nemotron and 35 from the complete frontier system were deployed against eight unseen attacks. Five of the 11 open detections (45%) detected at least one attack, compared with 10 frontier detections (29%). The open pipeline averaged 2.6 detections per detection, compared with 1.1 for the frontier system.

Detection alone, however, was only the first quality gate. To qualify as gold, detections also had to remain quiet on available test traffic and pass an independent review for behavioral grounding, multiple signals, and no environment-specific strings. Four of the five firing open detections and nine of 10 frontier detections that fired stayed quiet, covering eight of eight attacks and seven of eight, respectively. After review, three open detections and no frontier detections qualified as gold. The three open detections still covered all eight attacks.

**Interpreting the results**

The frontier system produced more backtest-passing detections, but the optimized Nemotron open-model pipeline yielded a higher share that generalized, averaged more detections per detection, and was the only system to produce gold detections. The evaluation covered one scenario family and small detection sets, so cross-scenario generalization remains untested. Limited benign traffic also means the noise test doesn’t represent production false-positive performance. Three of eight live-fire runs experienced harness failures but produced complete telemetry and were retained. The findings are a directional system-level case study, not a general benchmark.

**Applying the pattern to specialized agents**

The evaluation shows a broader pattern for building specialized agents with [NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/): a reasoning model orchestrates the defensive workflow, a post-trained open model handles a bounded expert task, and an agent harness manages context, tools, and validation. Four design principles emerge:

- Define measurable tasks and assign clear responsibilities to each model.
- Post-train specialized models with domain data and verifiable rewards.
- Ground outputs in authoritative context and validate them through deterministic checks, realistic replay, and independent review.
- Evaluate the complete workflow in realistic conditions, with security experts controlling scenarios, guardrails, and use of validated outputs.

CrowdStrike is advancing this approach through SafeMind, its agentic cybersecurity system, which brings offensive and defensive AI together in a continuous coevolution loop. Explore [NVIDIA Nemotron 3](https://developer.nvidia.com/topics/ai/nemotron), [NeMo Megatron Bridge](https://docs.nvidia.com/nemo/megatron-bridge/latest/), [NeMo Gym](https://docs.nvidia.com/nemo/gym/about/), and [NeMo RL](https://docs.nvidia.com/nemo/rl/latest/) to customize and evaluate specialized agents for other bounded domains.

## Start the discussion at forums.developer.nvidia.com
