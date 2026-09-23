# Dataset & LoRA Training Pipeline for Room Emptying / Object Removal (Image-to-Image)

source: https://discuss.huggingface.co/t/dataset-lora-training-pipeline-for-room-emptying-object-removal-image-to-image/180659#post_2
published: Tue, 22 Sep 2026 03:30:09 +0000

For now, I did a quick bit of digging into this:


There are a few fairly direct dataset candidates here, but I think I would separate **the dataset question**, **the LoRA question**, and **the geometry/conditioning question** before committing to a long training run.

The short version is:

- For
**room emptying**, [Structured3D](https://github.com/bertjiazheng/Structured3D) and [ShanghaiTech-Kujiale Indoor 360°](https://svip-lab.github.io/dataset/indoor_360.html) are unusually relevant because they actually contain furnished/empty variants of the same rooms.
- For
**masked single-object removal**, I would probably start with a strong inpainting/edit backbone plus paired removal data. LoRA is a reasonable low-cost first adaptation step.
- I would not treat
**LoRA vs. ControlNet as an either/or decision**. LoRA adapts model behavior; ControlNet-like conditioning gives the model additional spatial/structural information.
- Before training either one, I would spend a little time auditing the pairs and masks. In this problem, both can contain surprises.

A rough default path I would use is:

```
audit a small number of training pairs
↓
run a mask-guided inpainting/edit baseline
↓
LoRA adaptation if the base behavior is basically right
↓
look at what still fails
├─ shadow/reflection/contact traces
│ → effect-aware masks / effect-aware data
├─ wall/floor/layout reconstruction
│ → layout/depth/normal/other structural conditioning
└─ whole-image color/lighting changes
→ inspect the paired targets / data-generation process
```


And I would probably separate the two tasks like this:

```
single masked object
├─ the object disappears cleanly but the domain/style is wrong
│ → LoRA is a very reasonable first experiment
│
├─ shadows/reflections/contact traces remain
│ → the object mask may not be the complete edit region
│
└─ background structure is hallucinated
→ inspect large-mask behavior / structural conditioning
whole-room or large-furniture removal
├─ wall/floor/layout geometry stays plausible
│ → domain-specific fine-tuning may be enough
│
└─ room structure breaks
→ this starts looking like a hidden-geometry problem
rather than only an inpainting problem
```


##
Dataset candidates and what I would use them for

Structured3D

[Structured3D](https://github.com/bertjiazheng/Structured3D) is probably the first dataset I would inspect.

Its data organization is unusually convenient for this problem. For the same room it provides:

- panorama:
`empty / simple / full`

- perspective:
`empty / full`

- RGB
- semantic segmentation
- instance segmentation
- albedo
- depth
- normals
- room layout
- camera information

The exact organization is documented here:

[Structured3D — Data Organization](https://github.com/bertjiazheng/Structured3D/blob/master/data_organization.md)

So it is not only useful for `furnished RGB → empty RGB`

; it also gives you several possible structural targets/conditions if plain RGB supervision turns out not to be enough.

One caveat is important, though: **same scene + furnished/empty does not automatically mean pixel-consistent supervision**.

[PanoDR](https://vcl3d.github.io/PanoDR/) used Structured3D for essentially this family of problems and explicitly discusses a photometric-consistency issue: because the images are ray-traced, removing foreground objects can also change global illumination and rendered appearance.

Their workaround was interesting: instead of simply using the raw furnished render as input and raw empty render as target, they created a more photo-consistent training pair by compositing foreground objects back onto the empty image.

That solves one problem but creates another: naïve compositing does not naturally reproduce all cast shadows and illumination effects.

So I would treat the raw `full → empty`

pairing as very useful source material, but not automatically as perfect pixel-wise ground truth.

ShanghaiTech-Kujiale Indoor 360°

The other very direct candidate is:

[ShanghaiTech-Kujiale Indoor 360°](https://svip-lab.github.io/dataset/indoor_360.html)

It contains 1,775 rooms, with two rendered versions of every room:

and also provides depth/layout information.

The dataset page explicitly mentions **empty-room synthesis** as an intended use, so conceptually it is almost exactly on target.

I did a small sanity check on 24 furnished/empty RGB+depth pairs from the official archive because I was curious whether the pairs behaved like:

same image, except furniture is gone


They did not behave that cleanly.

Using the full/empty depth difference as a crude proxy for where scene geometry changed, there was still substantial RGB difference in depth-stable parts of many images. A simple global RGB offset explained some of it, but not all of it.

I would not over-generalize from 24 examples, but it was consistent with the issue PanoDR describes for rendered furnished/empty pairs: **the target may contain lighting/appearance changes in addition to furniture removal**.

That is why I would inspect 20–50 source/target differences before a multi-day training run.

Single-object-removal datasets

For the smaller masked-object-removal branch, there are now datasets that are much more specialized than general inpainting data.

Some useful references:

These are interesting because recent object-removal work increasingly treats **data construction itself** as part of the problem, not just model architecture.

In particular, OBER/CORNE-style data distinguishes the visible object from its wider visual effects.

That distinction becomes important if your masks come from SAM or another object segmenter: the geometrically correct object mask may still exclude the shadow, reflection, contact darkening, etc.

##
Why I would audit the masks as well as the image pairs

A normal segmentation mask answers roughly:

Which pixels belong to this object?


But object removal needs to answer a slightly different question:

Which pixels must change for the scene to look as though the object had never been there?


Those two regions are often not identical.

Recent removal systems explicitly target things like:

- cast shadows
- reflections
- contact shadows
- boundary residue
- secondary appearance effects outside the object silhouette

For example:

[OSOR](https://github.com/Zhouqm-Git/osor) explicitly describes non-local object effects and inaccurate/incomplete user masks as two core problems. Its solution is not simply “train a LoRA”: it also uses effect-aware supervision and an alpha head that can predict a broader editing region.

[ObjectClear](https://github.com/zjx0101/ObjectClear) similarly focuses on removing both the target object and its associated effects while preserving the surrounding background.

I also did a small check using [CORNE-Val](https://huggingface.co/datasets/QinmingZhou/CORNE-Val), which provides both an object-core mask and an effect-aware mask.

On the 48 pairs I sampled:

- the effect-aware mask was larger than the object-core mask in every sample;
- its area was about 1.8× the object-core area at the median;
- even in an idealized test where the object-core region was replaced perfectly with the clean target, noticeable residual error remained outside it;
- allowing the full effect-aware region to change reduced that residual in every sampled pair.

That does not mean every application needs a learned effect mask, but it does suggest that **mask quality/definition is upstream of the LoRA-vs-ControlNet choice**.

A very cheap test would be to take a handful of your current examples and visualize:

```
source
target / desired result
object mask
absolute source-target difference
```


If the desired changes consistently extend beyond the object mask, I would solve that before doing a large training sweep.

##
What I mean by LoRA vs. ControlNet being different decisions

LoRA

If the base model already understands:

- image editing,
- inpainting,
- room imagery,
- plausible background generation,

but it does not reliably perform **your specific removal behavior**, LoRA is a sensible inexpensive adaptation mechanism.

There is now a concrete current example for Qwen-Image-Edit-2511 in DiffSynth-Studio:

[Qwen-Image-Edit-2511 LoRA training example](https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/qwen_image/model_training/lora/Qwen-Image-Edit-2511.sh)

That example uses paired `image,edit_image`

data and trains a rank-32 LoRA on the DiT. It also enables `zero_cond_t`

, which is specific to Qwen-Image-Edit-2511.

There is a corresponding validation example here:

[Qwen-Image-Edit-2511 LoRA validation](https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/qwen_image/model_training/validate_lora/Qwen-Image-Edit-2511.py)

So if you want a relatively simple first Qwen experiment, this is a much more concrete starting point than building a custom training stack from scratch.

I would still regard LoRA as **one component of the pipeline**, though.

For example, OSOR provides LoRA-based implementations, but the complete removal system also contains specialized data, additional supervision, an alpha head, blending logic, etc.:

[OSOR repository](https://github.com/Zhouqm-Git/osor)

That is a useful warning against interpreting “LoRA-based object remover” as “ordinary LoRA alone solved object removal.”

ControlNet / structural conditioning

I would move toward ControlNet when the remaining error looks like **missing information rather than simply wrong model behavior**.

Examples:

- the floor direction changes behind a sofa;
- wall/floor boundaries bend;
- a hidden doorway is hallucinated;
- large furniture leaves the model unsure about room structure;
- you already have useful depth/layout/normal information that the model is currently not seeing.

DiffSynth-Studio currently has a Qwen Blockwise ControlNet inpainting training path:

[Qwen-Image Blockwise ControlNet Inpaint — LoRA example](https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/qwen_image/model_training/lora/Qwen-Image-Blockwise-ControlNet-Inpaint.sh)

and a full ControlNet training example:

[Qwen-Image Blockwise ControlNet Inpaint — full training](https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/qwen_image/model_training/full/Qwen-Image-Blockwise-ControlNet-Inpaint.sh)

The LoRA example is especially useful conceptually because it loads a ControlNet and then trains a LoRA on the main DiT. In other words, this is a concrete example of why I would not frame this as:

```
LoRA OR ControlNet
```


but rather as:

```
Do I need parameter adaptation?
Do I need additional structural conditioning?
Possibly both.
```


DiffSynth’s training framework also explicitly supports training multiple modules, although its documentation notes that when multiple modules are trained simultaneously, checkpoint/state-dict splitting needs extra handling:

[DiffSynth model-training documentation](https://github.com/modelscope/DiffSynth-Studio/blob/main/docs/en/Pipeline_Usage/Model_Training.md)

For an initial experiment, I would keep those variables separate rather than immediately doing joint training.

One qualification: I found current Qwen-Image-Edit-2511 LoRA examples and current Qwen Blockwise-ControlNet inpainting examples, but I have **not** found a direct published example showing that the exact combination “Qwen-Image-Edit-2511 + this ControlNet + room emptying” works well.

So I would treat that as an escalation path to test, not as a known solution.

##
Whole-room emptying: two different paths seem plausible

Once the removed area becomes very large, I think it is useful to stop treating this as merely “the same object-removal problem with a larger mask.”

There is a spectrum here.

Path 1: domain-specific inpainting may already be enough

The Matterport paper:

[An Empty Room is All We Want: Automatic Defurnishing of Indoor Panoramas](https://openaccess.thecvf.com/content/CVPR2024W/GCV/html/Slavcheva_An_Empty_Room_is_All_We_Want_Automatic_Defurnishing_of_CVPRW_2024_paper.html)

gets surprisingly far without requiring an explicit room-layout model in the core pipeline.

Among other things, they use:

- domain-specific fine-tuning;
- large spatial context around removed objects;
- improved blending;
- synthetic furnishing of real empty panoramas to create training examples.

That last part is especially relevant here.

Instead of relying entirely on naturally paired furnished/empty images, they can start with a genuine empty-room image as the clean target, add synthetic furniture/shadows to create the input, and train the model to recover the original empty image.

That gives a different way around the “raw furnished/empty render has unrelated lighting differences” problem.

So I would not jump straight to a geometry model unless the baseline shows that geometry is actually the limiting failure.

Path 2: if geometry is the failure, explicitly provide geometry

There is also a much more geometry-heavy continuation of the Matterport work:

[Defurnishing with X-Ray Vision: Joint Removal of Furniture from Panoramas and Mesh](https://matterport.github.io/defurnishing-with-x-ray-vision/)

Their pipeline first removes furniture from a 3D mesh and repairs/extents structural planes to produce a simplified defurnished mesh.

They then render depth and normal maps from that furniture-free mesh, derive Canny edges from those renders, and use them to guide ControlNet inpainting.

That distinction is important.

It is not simply:

take Canny edges from the furnished input and tell ControlNet to preserve them


because furnished-image Canny edges contain exactly the furniture edges you are trying to remove.

Instead, their conditioning represents an estimate of the **structure that should exist after the furniture is gone**.

So if your failures are mostly:

- implausible wall continuation,
- broken floor perspective,
- inconsistent wall/floor boundaries,
- structural hallucination behind large objects,

then I would investigate a furniture-invariant structural representation such as:

- room layout,
- predicted depth,
- predicted normals,
- cleaned structural edges,
- or, when available, mesh-derived geometry.

If those failures are not occurring, adding that entire subsystem may be unnecessary complexity.

##
A very similar ControlNet experiment I found

There is an old but unusually relevant ControlNet issue:

[ControlNet issue #659 — training ControlNet for furniture removal / empty rooms](https://github.com/lllyasviel/ControlNet/issues/659)

The setup is very close to this problem:

- furnished input;
- empty-room target;
- a large paired dataset;
- an attempt to preserve floor/wall details;
- a long ControlNet training run;
- improvement eventually plateauing.

The author was unsure whether the remaining limitation came from:

- preprocessing / data quality;
- architecture;
- training setup.

I would **not** read this issue as evidence that ControlNet cannot work. It is an unresolved user report, not a controlled benchmark.

But it is a useful reminder that simply giving ControlNet a large number of furnished/empty pairs and training longer does not automatically solve the problem.

It makes me more inclined to check:

- what exactly changed between each source/target pair;
- whether the condition encodes the structure we want after removal;
- whether the mask covers all visual effects;
- only then architecture/training duration.

##
Evaluation: I would separate several failure modes

I would keep your existing image-quality measurements, but I would not collapse everything into one PSNR/SSIM/LPIPS-style number.

Object removal can fail in very different ways:

```
A. target object is still partly visible
B. shadow/reflection/contact trace remains
C. another object is hallucinated in its place
D. wall/floor geometry is wrong
E. floor/wall texture melts or changes
F. pixels far outside the edit region change unnecessarily
G. result is locally plausible but globally inconsistent with the room
```


Those failures imply different fixes.

Recent removal work is starting to make the same distinction explicitly.

For example:

[OSOR](https://github.com/Zhouqm-Git/osor) evaluates effect-aware and mask-robust removal;
[ObjectClear](https://github.com/zjx0101/ObjectClear) focuses on object/effect removal while preserving background consistency;
[OmniPaint](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_OmniPaint_Mastering_Object-Oriented_Editing_via_Disentangled_Insertion-Removal_Inpainting_ICCV_2025_paper.html) introduces a removal-oriented metric intended to distinguish hallucination from contextual coherence.

So for your experiments I would probably keep a small diagnostic table like:

```
sample
mask size
object removed?
shadow/effect removed?
new object hallucinated?
room geometry okay?
floor/wall texture okay?
outside region preserved?
```


Even 20–30 manually inspected images can tell you much more about the next architecture decision than one aggregate score.

One other small point: I would treat prompts such as `"empty room"`

as a tuning variable, but not as the first thing to optimize.

Prompt wording can affect whether an editor generates a plausible empty room versus inventing replacement content, and the Matterport defurnishing work experimented with prompt variation as well. But if the paired targets contain global appearance shifts, or the mask excludes the object’s shadow, prompt engineering cannot repair those upstream supervision problems.

So if I were building a first practical version, I would probably do this:

```
1. Inspect a small batch of furnished/empty pairs.
2. Inspect source-target differences outside the object mask.
3. Establish the strongest no-training inpainting/edit baseline.
4. Train a small paired-edit LoRA.
5. Bucket the remaining failures.
6. Add effect-aware supervision if traces remain.
7. Add structural conditioning only if large-mask geometry is actually failing.
8. Consider full/joint training only after those simpler branches are understood.
```


That should let you get useful information from relatively small experiments without locking yourself into a heavy ControlNet/full-fine-tuning pipeline too early.