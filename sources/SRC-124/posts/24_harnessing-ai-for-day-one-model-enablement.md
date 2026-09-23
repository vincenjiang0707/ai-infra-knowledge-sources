# harnessing-ai-for-day-one-model-enablement

source: https://pytorch.org/blog/harnessing-ai-for-day-one-model-enablement/

### Featured projects


**TL;DR**

The AI model landscape never stops moving, and the software stack that runs those models is always a step behind: even on a mature compilation stack, a new model family often arrives with some novel module that doesn’t lower well, and on new hardware – where a young stack meets a whole ecosystem at once – the gap is far wider. Extending stack enablement to each new family has traditionally been slow, specialist work that delays deployment. In this blog we show how AI agents can facilitate **day-one enablement** for a new model or for entire ecosystems, by bridging between the model workflows and the compilation stack. We demonstrate this at the harder end of that spectrum: through a small number of AI-written adapters, we run stock HuggingFace Transformers models on IBM’s Spyre AI accelerator, achieving full enablement for thousands of models.

## The problem: catching up to an evolving model landscape

The model landscape never stops moving. New architectures and checkpoints appear constantly — each a particular composition of operations, shapes, and numerical ranges — and the software that has to run them is always a step behind. Even on the most mature, widely-deployed stack, a brand-new model family lands with some novel module, some fused attention variant, some numeric range that the existing software doesn’t yet handle cleanly.


**New model families added to the HuggingFace Transformers library over time.** Each step marks the inclusion of a prominent model family, illustrating the steady, accelerating pace at which new architectures arrive.

Running a model on any device requires a software stack – a compiler, a set of operator lowerings, and a runtime – that maps it onto the hardware’s cores, memory hierarchy, and number formats. That stack is a large, evolving piece of software, and a new architecture can exercise a corner of it that isn’t yet mature. Until that corner is filled in, the model cannot run, or doesn’t run well – and closing such a gap has traditionally taken weeks or months of specialist work.

New hardware is where the gap is at its widest. A new accelerator is not just a chip: it ships with a young stack still growing into the needs of different models. Here it is not one new model meeting a mature stack, but a whole ecosystem of models meeting a stack that is still being built – and that must simultaneously keep pace with new architectures landing on top of it. Enablement can’t wait for the stack to be complete; it should progress in parallel, letting real models run while the platform underneath them matures.


**AI accelerator releases. **Each dot marks the announcement date for a new chip. New hardware arrives almost as steadily as new models do – and every chip architecture needs a continually evolving software stack.

New hardware is the extreme case, but the challenge is a general one: keeping the software in step with the model landscape, whether the stack is mature or brand new. Below we describe a strategy for bridging that gap, and demonstrate it through a concrete instance – running stock HuggingFace Transformers models on **IBM’s Spyre accelerator**.

## The strategy: adapters as a bridge between models and stack

The strategy we describe is a thin layer of runtime patches – adapters – that allow a stock model to run on a given platform today, without waiting for every underlying gap in the stack to be closed first. We assume that the platform already provides a PyTorch compiler that lowers

core tensor operations in ordinary torch code – including matrix multiplications, elementwise operations, and reductions – onto the target hardware, so most of the model logic runs through it unchanged. When some operation in a model doesn’t yet have a clean path through the stack, the adapter reaches in at runtime and swaps it for an equivalent one that does. The patches change how the model is expressed for the device, but not what it computes: the underlying math is preserved. An adapter isn’t a hand-optimized kernel – it hands the stack a form it can lower well, but performance remains the compiler’s responsibility.

Rather than blocking on the state of the stack, adapters provide a practical bridge across it as it stands today. A useful analogy is a large construction project. Around a building with active construction – whether it is still going up or already standing and being renovated — there is almost always scaffolding somewhere: temporary access ramps and support beams that keep work moving on whatever part isn’t finished yet. No single piece of scaffolding is permanent; each comes down once the structure behind it can stand on its own.

Adapters play the same role. An individual adapter is usually transitional: its job is to carry a model across one specific gap in the stack as it stands today, and it is designed to be removed once that gap is closed — as the platform matures, new optimizations are integrated, more architectures are enabled, and the permanent path opens up underneath it. Not every adapter comes down, though: some bridge a temporary gap the stack will eventually close, while others accommodate a genuine, lasting difference in the target hardware; and where an accelerator harware has a unique architecture, those bridges may stay in place for good.

The adapter layer, however, is permanent in a way no individual adapter is. Because the model landscape never stops moving, there is always some new gap the stack hasn’t caught up to yet — so even as old scaffolding comes down, new scaffolding goes up elsewhere. That layer connects two things evolving in parallel. On one side is a model ecosystem – in our case HuggingFace Transformers, thousands of models with a stable API and an enormous community. On the other is the platform’s hardware-lowering stack – in our case Spyre, a compiler and runtime stack that maps those models onto the accelerator device and is itself under continual development. The adapters sit in between, letting models run on the hardware while the two ends continue to evolve.

What makes this strategy practical at the scale of thousands of models is AI. Historically, enabling each new model family was a slow, specialist effort, requiring a great deal of work for every hardware platform and chip architecture. Coding agents change the economics, turning what used to be a bespoke effort into something that can keep pace with the ecosystem. The rest of this post shows how that plays out – but first we will introduce the concrete platform in which we implement this.

## The platform: Spyre and torch-spyre

The hardware in our example is **Spyre**, IBM’s AI accelerator, built on the AIU (Artificial Intelligence Unit). It is made of small cores connected by a high-bandwidth ring, each with its own local scratchpad memory and arrays of processing elements that carry out the matrix multiplications at the heart of a model. A few things make it distinctive. First, it is dataflow-driven: computation is triggered by data arriving at a compute engine, which reduces the bottleneck of sequential control flow, and keeps the hardware busy on the structured, repetitive math that models are made of. This is in contrast to a conventional GPU, which executes kernels as explicit instruction streams across scheduled groups of threads. Second, Spyre uses reduced-precision number formats designed for inference, which lets it deliver high throughput at low power.

Spyre’s memory and compute operate on fixed-size chunks called sticks – 128 bytes, or 64 values in fp16 – and it expects tensor dimensions to line up on stick boundaries (see the [Tiled Tensors RFC](https://github.com/torch-spyre/RFCs/blob/main/0047-TiledTensors/0047-TiledTensorsRFC.md)). This is a different contract than the one PyTorch and model code are written against, where a tensor is a flat array of any shape and the framework hides how it maps onto memory. Model architectures pick their head dimensions, sequence lengths, and vocabulary sizes for statistical and modeling reasons, with no notion of a stick – so in our scenario, part of an adapter’s job is reconciling those two views, by bridging between the HF Transformers model implementation and the Spyre compiler extensions in PyTorch.

The software stack that maps a model onto this hardware is ** torch-spyre**, a PyTorch backend that compiles and runs ordinary torch code on Spyre: a model is compiled into a plan the hardware can execute. And the adapters – the temporary scaffolding from the previous section — are a project we call

**: runtime patches that let stock HuggingFace models run on Spyre today.**

[HF-adapters](https://github.com/torch-spyre/hf-adapters)## How AI helps build adapters

An adapter lives in the gap between two codebases. On one side is the model as Transformers expresses it – the modules, the attention blocks, the way a particular architecture wires its RoPE and its norms together. On the other is torch-spyre, the compiler and runtime that lower that computation onto the device. Writing an adapter requires understanding both at once and finding the exact places where they don’t yet meet: the operation the model expresses in a form the compiler can’t lower cleanly. In practice, this means following the model’s internal logic while tracing how each piece of it flows through the compilation stack. This is the part of the work AI has transformed.

Coding agents can now follow the internal logic of an entire transformer model at every level, from a single module up through the attention blocks to the full forward pass. They can trace the same computation down through torch-spyre’s lowering logic to see how it is meant to run on the hardware. Holding both views at the same time is what enables the core loop of this work: identify a gap in the stack, then draft a high-level patch that carries the model across it. The model side and the device side are usually documented in different places, in different languages, at different levels of abstraction. Reading both and cross-referencing them quickly is the bottleneck that once made an effort like this impractical to attempt at all.


A few things make this work in practice. We keep a knowledge base that describes both the hardware and the software stack as it evolves, so an agent can ground its reasoning in how Spyre actually behaves rather than in generic assumptions. We give it direct access to the source and GitHub of both the HuggingFace Transformers library and the torch-spyre backend, so it can trace the logic through the actual code, issues and pull requests. Moreover, frontier models already carry a deep working knowledge of machine learning and transformer architecture – they know what attention, RoPE, and RMSNorm are before they ever open our repository, which means the reading starts from understanding rather than from scratch.

Importantly, every adapter we add is also a record of which adaptations work, and for what reason. A new model is rarely a completely new problem: it is usually a variation on an architecture we have already brought up, and the closest existing adapter is both a template to imitate and a source of patches that can be reused directly. So each model we enable lowers the cost of the next one that resembles it, and adding a new adapter gets easier over time. The chart below shows this compounding in practice: a small number of distinct adapters, added over a few months, comes to cover the large majority of the models in the target set.


**Coverage of the target model set from mid-April to late June 2026. **The left axis counts embedding models, the right axis counts distinct adapters. By the final snapshot, 13 distinct adapters cover 7,960 of the 10,000 most-downloaded HF embedding models, of which 6,804 pass their end-to-end test on Spyre. The coverage lines rise in a few large steps rather than one model at a time: because most new models are variations on an architecture already brought up, each new adapter picks up a whole family of similar models at once. Effort scales with the number of architectures, the coverage it buys with the number of models. The gap between the two coverage lines — models that have an adapter versus models that pass on Spyre — illustrates the debugging challenge: an adapter is necessary but not sufficient, and closing that gap is where the human-in-the-loop diagnosis below is spent.

At the same time, human expertise and supervision remain essential. Two failure modes recur.

The first is that **localization is genuinely difficult**. When a model that is correct on CPU or GPU produces the wrong output on the device, narrowing down the exact source of the mislowering is rarely a matter of reading the code once. It means reproducing different parts of the model both in isolation and in concert — pulling a single block out to test it alone, then putting it back to see whether the failure survives the surrounding computation — because the fault often lives not in any one operation but in the interaction between them, where small faithful deviations line up in a way a downstream component happens to amplify. When the original and adapted code run on the same CPU or GPU, we generally expect bitwise-identical outputs, confirming that the adapter preserves the computation. However, this bitwise determinism expectation does not extend to the target hardware, where expected numerical drift can be difficult to distinguish from a genuine lowering error. Localization is made harder still by the fact that the compiler does not lower each operation in isolation: it fuses neighboring operations together, and which operations get fused depends on the context they appear in. The same operation can lower one way when it stands alone and a different way once it is fused with what surrounds it — so an operation that tests as faithful when pulled out can still misbehave in place, precisely because pulling it out changed the fusion. This is patient, method-driven work, and no single automated probe substitutes for it.

The second is that **the agent will often draw the wrong conclusion from a targeted experiment**. A large numerical discrepancy somewhere deep inside the model is a clue, not a verdict. It is easy — for a person and an agent alike — to find an alarming difference in some intermediate tensor and conclude that it is the cause of the end-to-end failure. But downstream layers routinely attenuate an internal error until it never reaches the output, so a component can look badly broken and be entirely harmless to the final result. The discipline that separates a real diagnosis from a plausible one — trace the discrepancy forward to the actual output, distrust any probe that disagrees with the end-to-end result, confirm that the one thing you changed is really the thing that mattered — is judgment an agent does not reliably supply on its own. It will propose a confident explanation from a single suggestive experiment, and someone has to check whether it holds up.

The division of labor follows from this. AI handles the wide, repetitive, cross-referencing part of the work: reading two large codebases at once, recognizing an architecture, and drafting a first adapter by analogy to the ones that came before. Human expertise handles the diagnosis: localizing the silent failures that only appear on the device, and not trusting a lead until it has survived the end-to-end test. Another important role for the human is deciding what the agent should learn from past mistakes — updating the procedures it follows when drafting adapters and debugging, and separating isolated issues from recurring “gotchas” that are worth capturing. These are recorded as agent skills and memories that make the process more efficient, but do not remove the need for explicit human supervision.

## Adapters as a validation tool

Each adapter does more than carry its model onto the device. In doing so, it also exposes exactly where the stack underneath still needs work.

This is a general property of bridging a mature ecosystem to a young stack. The gaps in such a stack rarely live in a single operation; they live in combinations no unit test anticipated, and the only reliable way to surface them is to run real workflows end to end against a trusted reference. Adapters make that possible before the stack is finished – so every model they carry doubles as a stress test of the platform.

In our example, the Torch-Spyre team works primarily at the lower levels of the software stack – the compiler, the operator lowerings, the runtime that places work on the device. At that level it is genuinely hard to predict how a real model will behave. A production model is a particular composition of shapes, operators, weight layouts, and numerical ranges, and it is often that specific combination – not any one piece in isolation – that trips over a gap in the stack. The gaps are real, but from the bottom of the stack they are mostly invisible: nothing about a single lowering tells you which model, at which layer, with which input, will finally exercise it.

Running stock HuggingFace models end-to-end is what makes these gaps visible. An end-to-end divergence from a CPU/GPU reference is a strong signal that something in the platform needs attention. In practice the issues that surface fall into a few recurring families:

**Missing lowering paths**– a block or fused shape the stack cannot yet lower, even when the individual ops are already working in isolation.**Device-only numerical behavior**– values that overflow or turn into NaNs on the device where the CPU/GPU reference stays finite.**Alignment and padding assumptions**– shapes that quietly corrupt results when they don’t match what the hardware expects.

What ties these together is that they are largely fusion-dependent. When a full model is compiled, the stack fuses different ops and shapes into combined kernels, and which things get fused depends on the surrounding graph. That is why an operator can pass low-level testing on its own and still fail here: the failure belongs to the fused context, not the bare op.

Real models also bring real data. Low-level tests typically feed operators random tensors, but trained weights and the activations they produce have structure that random inputs don’t — particular value ranges, near-constant rows, occasional large outliers. That structure is often exactly what pushes a kernel into overflow or a NaN. So none of these families are apparent from a unit test of an operator alone; they emerge only when a full model drives real weights and activations through the stack.

This also builds on itself. The temporary adaptations already in place each get a model past a known crash or mislowering at one point in the stack. Doing so is what lets execution reach further in and expose the next gap, which was invisible while the model was still failing earlier. So each adaptation is both a workaround and a probe: by clearing a known obstacle, it lets the full model run deep enough to reveal whatever comes after it.

So the adapters play a double role – they are an integration layer that lets Transformer models run on Spyre today, and they are a validation tool that continuously exercises the platform against the messiness of real architectures. Every model we bring up is also a test case, and the failures it exposes feed directly back into hardening the lower layers.

## Adaptation examples

To illustrate the range of adaptations we implement in [HF-adapters](https://github.com/torch-spyre/hf-adapters), we’ll walk through two examples, and then step back to see what they have in common, and where they differ.

### Replacing an operator

The smallest patches replace one currently unsupported operation with a mathematically identical one.

A concrete example is the `gelu_new`

activation used by decoders like GPT-2 and GPT-Neo. Its tanh-approximation form, `0.5 x (1 + tanh(sqrt(2/pi) (x + 0.044715 x³)))`

, computes the cube with `torch.pow(x, 3.0)`

. This raise to a power op doesn’t yet lower well on the torch-spyre stack, but the plain multiplication `x * x * x`

does — and it’s exactly the same number. So the patch is a one-line substitution, applied only on the Spyre device path:

These fixes are satisfying precisely because they’re invisible: the model’s math is untouched, and the only thing that changes is the shape of the instruction the stack sees.

### Reshaping the data

Other issues can’t be fixed by swapping a single operator. They come from *how much* data is being processed and *how it’s laid out*, and the fix is to reshape the data before it reaches the hardware — through changes related to work division, padding, or other structural transformations.

A concrete example is the model’s final output projection – the LM head – that turns the model’s internal representation into a score for every word in its vocabulary. On Spyre this is one large matrix multiply, and the device tackles it by slicing the vocabulary dimension into fixed-size blocks and, through a step of work division, spreading those blocks across its many cores. The work division only succeeds if the number of blocks can be split evenly across the cores. When it can’t — because the block count happens to have a large prime factor – one core is left holding a slice too big to fit within a hard on-device memory limit, and the model fails to compile at all.

The fix is to pad the vocabulary: we round it up, adding a small number of unused entries, until the block count factors into pieces the work division can distribute evenly. The padding entries carry no meaning and are ignored, so the model’s output is unchanged – but the matrix multiply now divides cleanly across the cores and compiles. In practice the padding is tiny, often just a handful of rows, and it lets a single, efficient kernel handle even very large vocabularies:

### What these examples show

Taken together, these two examples span the range of adaptations we deal with. Replacing an operator is a low-level change to a single instruction: the problem is that one specific operation doesn’t lower well, and the fix is to rewrite that exact operation; there’s no gap between the symptom and the change. Modifying padding behavior is an example of a more complex and high-level adaptation. We intervene at the level of tensor shapes, not individual operations, yet that high-level change is precisely what steers the stack’s low-level behavior – how the work is divided across the device and how the computation is ultimately laid out. The adaptation is expressed high, but its effect reaches all the way down.

The common thread is that in neither case do we change *what* is computed. The model’s math is preserved exactly – we only change the form it takes so the existing computation can succeed on the stack as it stands today.

## Conclusion

The model landscape never stops moving, and every backend that runs it – each GPU architecture, each accelerator, each maturing compiler stack – is left playing catch-up. Historically this was slow, specialist work that kept new models from reaching cross-platform deployment. What changes the equation is AI. A coding agent can hold a model’s logic and the hardware-lowering stack in view at once, recognize an architecture, and draft the adapter that bridges them – with human judgment steering and overseeing the nuanced localization and debugging efforts. The result is not a one-off fix but a living adapter layer: each model brought up makes the next one easier, and each adapter can double as a probe that hardens the platform beneath it.

We demonstrated this on Spyre, at the hardest end of the spectrum – a brand-new accelerator with a stack still being built. But nothing about the loop is specific to Spyre. Whenever a new model family lands ahead of the stack that must run it – whether that stack is brand new or mature – the same paradigm applies: AI-written adapters can turn day-one enablement from an aspiration into something routine.
