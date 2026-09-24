# introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning

source: https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/

Radiology AI has made remarkable strides in detecting abnormalities across chest X-rays, pathology slides, and 2D scans. Yet one of the most clinically rich and data-dense modalities—the 3D computed tomography (CT) scan—remains largely underserved by modern [vision language models (VLMs)](https://www.nvidia.com/en-us/glossary/vision-language-models/). Frontier general-purpose models perform poorly on volumetric imaging, and most open medical AI models lack the multistep conversational depth that radiologists need to trust and verify AI-generated findings.

NVIDIA is addressing this gap with NV-Reason-CT, a VLM purpose-built for 3D CT analysis. NV-Reason-CT extends chain-of-thought reasoning to full volumetric CT, generating structured diagnostic reports, emulating radiologist internal thinking, and supporting multistep follow-up conversation across chest and abdomen. It builds on the reasoning methodology pioneered by[ NV-Reason-CXR](https://developer.nvidia.com/blog/advancing-explainable-ai-in-radiology-research-with-nvidia-clara-reason/), validated in a multireader clinical study accepted at RSNA 2026 confirming radiologist time savings while maintaining diagnostic accuracy.

NV-Reason-CT is an open research and development foundation; not an autonomous diagnostic system or a cleared clinical product. It is an [AI foundation model](https://www.nvidia.com/en-us/ai-data-science/foundation-models/) designed for researchers and developers building specialized CT analysis applications to post-train for their use case.

## Why 3D CT reasoning demands a different approach

A single abdominal CT study can comprise 300–600 axial slices, encoding anatomical context across three spatial dimensions that a standard 2D encoder simply cannot reconstruct from independent slices.

This volumetric complexity creates a series of compounding challenges for medical AI to do with perception, reasoning, and conversational depth:

**Perception**: Standard VLMs treat image input as a 2D token grid. Processing a CT volume as a stack of independent 2D frames discards the spatial relationships between slices that define structures like masses, effusions, and infiltrates—structures whose shape, extent, and density only become clinically meaningful in three dimensions.**Reasoning**: Even models that correctly perceive an abnormality often output a diagnostic label without articulating*why*. Radiologists don’t think in labels—they think in systematic anatomical reviews, differential diagnoses, and degrees of confidence. An AI that cannot reproduce that reasoning process cannot be audited, taught from, or safely integrated into clinical workflows.**Conversational depth**: A radiologist reviewing a suspicious finding doesn’t close the case at first glance. They ask follow-up questions, reconsider differentials, and correlate findings across anatomical regions. Most existing models lack the multiturn dialogue capability to support this kind of iterative clinical reasoning.

## Providing full 3D reasoning for CT analysis

NV-Reason-CT combines a dedicated full 3D vision transformer (ViT) encoder with a language model trained to generate chain-of-thought reasoning that mirrors how radiologists systematically analyze CT volumes.

Unlike approaches that adapt 2D encoders to CT by treating slices independently, NV-Reason-CT processes the CT volume as a true 3D input. This preserves through-plane anatomical continuity and enables the model to reason about structures holistically, the way a radiologist would when scrolling through a study.

Core model capabilities include the following:

**Structured report generation**: NV-Reason-CT generates detailed structured reports. The NVIDIA team curated a CT ontology covering 30 chest and 29 abdominal abnormalities to guide and evaluate the model—such lung nodules, pneumothorax, hepatic lesions, renal cysts, and more—in a format that maps naturally to clinical documentation workflows.**Radiologist-emulating chain-of-thought**: NV-Reason-CT can also generate reasoning emulating radiologist thought chains. The model produces step-by-step internal thinking—examining anatomical regions systematically, surfacing relevant findings, considering differential diagnoses, and articulating uncertainty—in the style of an experienced radiologist working through a study.**Multistep conversational follow-up**: Clinicians and researchers can ask follow-up questions about specific findings, request clarifications on differential diagnoses, or probe the model’s reasoning at any stage. This multiturn capability transforms NV-Reason-CT from a report generator into an interactive diagnostic partner.**Full 3D ViT encoder**: A purpose-built 3D vision encoder processes CT volumes natively, extracting volumetric features that 2D-based approaches cannot recover. In addition, 3D vision token grid coordinates are passed to LLM to account for spatial inter-token relationship throughout the LLM layers through 3D MRoPE. This architectural choice enables the model to reason about spatial extent, cross-sectional morphology, and inter-slice relationships—the perceptual foundations of accurate CT interpretation.

## How is NV-Reason-CT architecture purpose-built for volumetric reasoning?

The model architecture combines Qwen3.5-4B LLM with 3D ViT (Primus/Colipri). All weights are retrained end-to-end on large cohort or CT data with structured report, reasoning traces, multistep VQA (designed internally). Standard transformer-based VLMs are designed for 2D images. Adapting these to CT by flattening a volume into a sequence of 2D slices loses the spatial structure that defines volumetric pathology.

The encoder architecture is adapted from Primus 3D ViT, initialized with Colipri weights prior to training; It processes CT volumes resampled to 192³ voxels at 2 mm isotropic resolution, using non-overlapping 8x8x8 patch tokens—resulting in 24x24x24 = 13,824 vision token context. Instead of merging (or downsizing), all vision tokens are passed to LLM (together with their 3D grid coordinates). The LLM includes 3D MRoPE to account for the 3D spatial relationship of vision tokens.

The language model component is trained to reason in the style of a radiologist: systematically reviewing anatomical regions, noting normal findings alongside abnormal ones, expressing calibrated uncertainty, and arriving at a structured conclusion. The model is designed to respond not as a classifier, but as a teacher: explaining the problem, walking through the evidence, and arriving at a diagnosis through visible logical steps.

## What is the NV-Reason-CT training methodology?

Building on the approach introduced with NV-Reason-CXR, NV-Reason-CT follows a two-stage training pipeline: supervised fine-tuning followed by [reinforcement learning (RL)](https://www.nvidia.com/en-us/glossary/reinforcement-learning/).

### Stage 1: Supervised fine-tuning on radiologist reasoning data

The initial stage trains the model on the mixture of data, including structured report, expert radiologist reasoning annotations, and general VQA. Radiologists contributed detailed chain-of-thought dictations for CT studies that capture their internal review process, including what they examine in each anatomical region, which findings they consider significant, which differentials they weigh, and how they arrive at their final assessment.

The resulting curriculum spans approximately 550,000 structured QA examples across chest and abdominal regions covering section-level anatomy QA, laterality-specific and localized finding QA, severity-level QA, and binary abnormality identification. Refusal examples for invalid prompts and mismatched image-text pairs were included to improve robustness.

Training data includes CT-RATE, NIH CT datasets, and CancerVerse. This dataset is supplemented with high-quality synthetic reasoning data distilled from large language models, using expert radiologist annotations as grounding examples. The combined dataset provides the model with a rich signal for what structured radiological reasoning looks like across a wide range of CT findings.

### Stage 2: RL for reasoning quality

The second stage uses Group Relative Policy Optimization (GRPO) to refine reasoning quality. A reward function based on the accuracy of identified abnormalities and diagnoses guides the model to produce reasoning that is not only well-structured but clinically correct. The GRPO reward is anatomy-aware. The model is reinforced for accuracy within each anatomical region rather than using a single global signal, which improves calibration across the full chest-abdomen findings distribution.

This two-stage approach (learning reasoning patterns first, then reinforcing correctness) allows NV-Reason-CT to generalize across the diversity of CT presentations without requiring exhaustively annotated reasoning chains for the full training distribution.

## Benchmarking results

NV-Reason-CT achieves state-of-the-art results on the leading public benchmarks for 3D CT understanding.

On CT-RATE, the primary public benchmark for 3D CT understanding, NV-Reason-CT outperforms all published baselines including 3D contrastive models (VoxelFM, Pillar-0, CT-CLIP, Merlin), fused 2D/3D MLLMs (ClinFusion-8B), and slice-based frontier models (MedGemma 1.5). This is the first time a single open model has achieved competitive CT classification and report generation simultaneously.

Model | Type | Macro-F1 | Macro-AUROC |
|---|---|---|---|
NV-Reason-CT | Native 3D generative VLM | 0.614 | 0.871 |
| VoxelFM | 3D image-only pretraining | 0.581 | 0.870 |
| Pillar-0 | 3D contrastive | 0.544 | 0.861 |
| ClinFusion-8B | Fused 2D/3D generative MLLM | 0.442 | n/r |
| CT-CLIP | 3D contrastive | 0.398 | 0.733 |
| Merlin | 3D contrastive | 0.358 | 0.662 |
| MedGemma 1.5 | Up to 85 axial slices | 0.303 | n/r |


*Table 1. CT-RATE classification results (18 labels, fixed uniform threshold). NV-Reason-CT evaluated using direct Yes/No prompt with no classification head or task-specific adaptation)*In addition to benchmark performance, NV-Reason-CT has received favorable clinical reviews from National Institutes of Health (NIH) radiologists, who validated both the quality of the structured reports and the clinical plausibility of the chain-of-thought reasoning traces.

“NV-Reason-CT provides the kind of systematic, step-by-step reasoning that reflects how we actually think through a CT study,” said Baris Turkbey, M.D., F.S.A.R., Senior Clinician, National Institutes of Health. “Being able to review the model’s thought process—not just its conclusions—is what makes it possible to trust and act on its findings.”

## Clinical validation and real-world impact

The value of NV-Reason-CT extends beyond benchmark scores. Radiologists and clinical researchers who have reviewed the model’s outputs consistently highlight two capabilities that distinguish it from earlier CT AI systems:

**Time savings in structured reporting**: Generating a detailed, structured report covering 60+ abnormalities is time-consuming, even for experienced radiologists. NV-Reason-CT produces this output in seconds, with reasoning that clinicians can rapidly scan, validate, and amend—reducing the cognitive load of routine reporting while preserving radiologist oversight.**Explainability that enables audit**: Traditional medical AI models output labels or scores. NV-Reason-CT outputs its reasoning. This makes the model’s conclusions auditable in a way that black-box systems are not: a radiologist can read the chain-of-thought, identify where the model’s reasoning aligns with their own, and flag where it diverges. This is the kind of transparency that clinical adoption requires.

## How can NV-Reason-CT help research and medical AI?

NV-Reason-CT is designed to be a foundation that the broader medical AI community can build on.

Researchers can use the model checkpoints and post-training recipes to study chain-of-thought reasoning in medical imaging, fine-tune on institution-specific CT datasets, or integrate NV-Reason-CT into multimodal research pipelines. Complementary models for segmentation and SDG include NV-Generate-CTMR and NV-Segment-CTMR.

Medical AI companies including radiology workflow vendors, PACS developers, and clinical decision support platforms can adapt NV-Reason-CT for specific clinical applications. This enables the integration of structured CT reasoning into existing radiology review workflows. Companies like Aidoc, HOPPR, Rad AI, Mosaic Clinical Technologies, and Raidium, operate in spaces where a capable, open, conversational 3D CT model addresses a genuine capability gap.

## Example NV-Reason-CT run and output

The following example loads NV-Reason-CT and runs a reasoning pass over a 3D CT volume. Checkpoints are available from Hugging Face. The GitHub repository includes inference scripts, training configurations, and post-training recipes.

`import` `torch` `from` `transformers ` `import` `AutoModelForImageTextToText, AutoProcessor` `model_name ` `=` `"nvidia/NV-Reason-CT"` `model ` `=` `AutoModelForImageTextToText.from_pretrained(` ` ` `model_name, ` ` ` `trust_remote_code` `=` `True` `,` ` ` `attn_implementation` `=` `"sdpa"` `,` ` ` `torch_dtype` `=` `torch.float16,` `).` `eval` `().to(` `"cuda"` `)` `processor ` `=` `AutoProcessor.from_pretrained(model_name, trust_remote_code` `=` `True` `)` `messages ` `=` `[` ` ` `{` ` ` `"role"` `: ` `"user"` `,` ` ` `"content"` `: [` ` ` `{` `"type"` `: ` `"image"` `},` ` ` `{` `"type"` `: ` `"text"` `, ` `"text"` `: ` `"full chest CT reasoning analysis"` `}` ` ` `]` ` ` `}` `]` `# Create prompt using chat template` `text ` `=` `processor.apply_chat_template(` ` ` `messages,` ` ` `add_generation_prompt` `=` `True` `,` ` ` `tokenize` `=` `False` `,` ` ` `enable_thinking` `=` `True` `)` `# Process inputs` `inputs ` `=` `processor(` ` ` `text` `=` `prompt,` ` ` `images3d` `=` `[` `"chest_ct.nii.gz"` `],` ` ` `anatomy_region` `=` `"chest"` `,` ` ` `return_tensors` `=` `"pt"` `,` `).to(model.device)` `# Generate chain-of-thought reasoning and structured report` `with torch.inference_mode():` ` ` `generated_ids ` `=` `model.generate(` ` ` `*` `*` `inputs,` ` ` `max_new_tokens` `=` `4096` `,` ` ` `do_sample` `=` `False` `,` ` ` `use_cache` `=` `True` `,` ` ` `)` `# Decode` `new_tokens ` `=` `generated_ids[:, inputs.input_ids.shape[` `1` `]:]` `response ` `=` `processor.batch_decode(` ` ` `new_tokens,` ` ` `skip_special_tokens` `=` `True` `,` ` ` `clean_up_tokenization_spaces` `=` `False` `,` `)[` `0` `]` `print` `(response)` |

### Output excerpt

`<think> I will review the CT volume systematically, use the valid technique context, ` `identify the key imaging findings, and then provide the final labels. </think>` `We are going to review this IV contrast-enhanced CT of the chest in a systematic way. ` `First, one important technical and support-device detail: there is a left-sided port catheter, ` `and the catheter tip terminates in the superior vena cava, which is an expected central venous position.` `I will begin with the lungs and airways. The central airways are patent, so there is no major tracheal ` `or main bronchial occlusion. However, when we come down into the right lung, the right lower lobe ` `is the dominant abnormality. There is a large mass-like process in the right lower lobe, and it is associated ` `with partial collapse of the right lower lobe. This is a meaningful finding because a mass with postobstructive ` `or associated volume loss is concerning for a malignant process.` `There is also an additional mass-like lesion in the right lower lobe [...].` `So overall, the dominant thoracic finding is a large right lower lobe mass-associated partial collapse, ` `with additional right lower lobe mass-like disease and bulky mediastinal and right hilar adenopathy. ` `The pattern is concerning for thoracic malignancy with nodal involvement. There are also scattered bilateral ` `ground-glass opacities that remain nonspecific and could be inflammatory, infectious, or neoplastic. ` `In addition, there is lytic lower thoracic spine disease with moderate spinal stenosis and a few indeterminate ` `right rib sclerotic lesions.` |

## How NV-Reason-CT fits within the NVIDIA Medical AI ecosystem

NV-Reason-CT is part of the NVIDIA Medical AI family of open medical AI models, designed to work together across the radiology pipeline:

: Synthesize realistic 3D CT and MRI volumes for training data augmentation and research**NV-Generate-CTMR****NV-Segment-CTMR**: Automated organ and lesion segmentation from 3D CT and MR volumes**NV-Reason-CXR**: Chain-of-thought reasoning for chest X-ray analysis**NV-Reason-CT**: Chain-of-thought reasoning for full 3D CT analysis

Together, these models provide the building blocks for end-to-end radiology AI pipelines—from synthetic data generation, through segmentation, to transparent, conversational clinical reasoning.

Explore the [NVIDIA Medical AI](https://github.com/NVIDIA-Medtech) ecosystem to learn more.

## Get started with NV-Reason-CT for radiologist chain-of-thought reasoning

NV-Reason-CT brings chain-of-thought reasoning to one of medicine’s most information-dense modalities. By combining a dedicated full 3D ViT encoder with a reasoning-trained language model, the system produces structured diagnostic reports and step-by-step radiologist-style thinking for CT volumes—covering chest and abdominal findings with multiturn conversational support.

*Stay up to date by subscribing to** **NVIDIA news**, and following NVIDIA Healthcare on** **LinkedIn**,** **X**, and** **YouTube**.*

## Start the discussion at forums.developer.nvidia.com
