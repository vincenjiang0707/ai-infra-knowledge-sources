# H Company's new Holo2 model takes the lead in UI Localization

source: https://huggingface.co/blog/Hcompany/introducing-holo2-235b-a22b
published: Tue, 03 Feb 2026 17:40:14 GMT

Image-Text-to-Text • 236B • Updated • 117 • 34

#
[
](https://huggingface.co#h-companys-new-holo2-model-takes-the-lead-in-ui-localization)
H Company's new Holo2 model takes the lead in UI Localization

[Team Article](https://huggingface.co/blog)

Two months since releasing our first batch of Holo2 models, H Company is back with our largest UI localization model yet: **Holo2-235B-A22B Preview**. This model achieves a new State-of-the-Art (SOTA) record of 78.5% on [Screenspot-Pro](https://gui-agent.github.io/grounding-leaderboard/) and 79.0% on OSWorld G.

Available on [Hugging Face](https://huggingface.co/Hcompany/Holo2-235B-A22B), Holo2-235B-A22B Preview is a research release focused on UI element localization.

**Agentic Localization**

High-resolution 4K interfaces are challenging for localization models. Small UI elements can be difficult to pinpoint on a large display. With agentic localization, however, Holo2 can iteratively refine its predictions, improving accuracy with each step and unlocking 10-20% relative gains across all Holo2 model sizes.

**Holo2-235B-A22B's Performance on ScreenSpot-Pro**

Holo2-235B-A22B Preview reaches 70.6% accuracy on ScreenSpot-Pro in a single step. In agent mode, it achieves 78.5% within 3 steps, setting a new state-of-the-art on the most challenging GUI grounding benchmark.

**Trained with SkyPilot**

Training Holo2 models at scale requires coordinating workloads across multiple cloud providers. H Company uses [SkyPilot](https://skypilot.readthedocs.io/) as a unified interface for launching training jobs on our clusters with Kubernetes (k8s). By abstracting away infrastructure complexity, SkyPilot lets researchers focus on model development instead of managing k8s manifests or maintaining separate deployment scripts.