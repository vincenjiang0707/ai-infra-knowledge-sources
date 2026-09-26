# [Issue #5683] gemma-4-12B on gfx1201: ROCM_AITER_UNIFIED_ATTN is 4.65x faster at prefill than TRITON_ATTN (A/B on rocm/vllm:latest + aiter main)

source: https://github.com/ROCm/aiter/issues/5683
state: open | updated: 2026-09-20T22:32:07Z
labels: 

## 正文

Following up on ROCm/aiter#5229, where @amd-xavierwang suggested I A/B the two attention backends for Gemma 4 on gfx1201 rather than assume one is better.

Before the numbers, let me describe the setup in detail, so that nothing here has to be guessed at or inferred from my side. I have tried to keep **what we ran**, **what we observed** and **what we concluded** separate, and to mark the places where we cannot support a conclusion.

## Summary

On a single Radeon AI PRO R9700 (gfx1201), with gemma-4-12B-it-FP8-Dynamic, `ROCM_AITER_UNIFIED_ATTN` is **4.65x faster at prefill** than `TRITON_ATTN` — 5107 vs 1098 tok/s on a cache-missing 7.7K-token prompt, or 1.52 s against 7.07 s of wall time. Decode differs by +2.6%, which is small but consistent.

This is the opposite direction from the note in ROCm/aiter#4868 ("for head_size 256/512, vLLM's upstream TRITON_ATTN backend is globally faster"), and it matches what you said you were seeing on gfx1151 in ROCm/aiter#5601.

## What we ran

**Base image, unmodified:**

```
rocm/vllm:latest
digest sha256:30761c2125ce150d556bef46406a0158446421886bf83a2e60154c6e4ca17a13
```

One thing worth stating so nobody assumes we tested something newer than we did: the `latest` **tag** was updated 2026-09-18, but `docker inspect` reports `Created: 2026-08-27`. The contents look like the same build as `rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0`.

Measured from inside the image:

| | |
|---|---|
| ROCm | 10.0.0 |
| PyTorch | 2.12.0+rocm10.0.0 (`torch.version.hip` 7.15.26333) |
| vLLM | 0.27.1.dev5+gf46a9dfe2.d20260827 |
| Python | 3.14.7 |
| Triton | 3.8.0 |
| bundled aiter | amd-aiter 0.1.20.post1 |

**Host, unchanged throughout:** Ubuntu 24.04, kernel 7.0.0-31-generic, in-tree amdgpu, host ROCm 7.2.3 (separate from the container's ROCm 10). No `PYTORCH_*_ALLOC_CONF` set anywhere.

**Our three modifications, and nothing else:**

1. aiter installed from source at main, exactly as the README says:

   ```bash
   git clone --recursive --depth 50 https://github.com/ROCm/aiter.git
   cd aiter && python3 setup.py develop
   ```

   Installed as `amd-aiter==0.1.1.dev50+g6214264b1`, HEAD `6214264` (2026-09-19). No build errors and no long build, consistent with your point that gfx1201 needs nothing prebuilt. Triton was **not** replaced — 3.8.0 before and after.

2. **The bundled aiter has to be moved aside or the source install silently does nothing.** This answers the uncertainty you raised in #5229. After `setup.py develop`, `easy-install.pth` contains `/opt/aiter`, but `site-packages` precedes it on `sys.path`, so `import aiter` still resolved to the shipped 0.1.20.post1. Anyone following your advice without checking would believe they were testing main while measuring the shipped package. We renamed rather than deleted:

   ```bash
   SP=/opt/python/lib/python3.14/site-packages
   mv $SP/aiter $SP/aiter.bundled.bak
   mv $SP/amd_aiter-0.1.20.post1.dist-info $SP/amd_aiter-0.1.20.post1.dist-info.bak
   ```

3. `pip install transformers==5.12.0`. The image ships 5.16.1, which refuses Gemma 4 with `AmbiguousGlobalPerLayerAttributeError: 'head_dim' is a per-layer attribute`. This is the same downgrade the ROCm 10 image needed. One pip warning appeared and had no observable effect: `vllm … requires tensorizer==2.10.1, but you have tensorizer 2.12.1`.

## Method

Model gemma-4-12B-it-FP8-Dynamic, `--gpu-memory-utilization 0.90`, `--max-model-len 8192`, `--kv-cache-dtype fp8`, `--enable-prefix-caching`, `--compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE"}'`, `HIP_VISIBLE_DEVICES=0`.

Three alternating pairs, six cold spawns total, one process at a time, so that any drift over the session hits both arms equally.

**The two arms are not a single variable, and I would rather say so than let it be assumed.** On RDNA, `VLLM_ROCM_USE_AITER=1` forces the backend regardless of `--attention-backend` (vllm-project/vllm#56021), so the comparison is:

| arm | environment |
|---|---|
| A | `VLLM_ROCM_USE_AITER=1`, `--attention-backend ROCM_AITER_UNIFIED_ATTN` |
| T | `VLLM_ROCM_USE_AITER=0`, `--attention-backend TRITON_ATTN` |

**Prefill measurement.** A shared prompt would have measured prefix-cache hits rather than prefill, so each request carries a unique ID at the **front** of the prompt, ensuring a cache miss. `max_tokens=1`, and the rate is `usage.prompt_tokens` divided by wall time. One warmup then four measured requests per spawn, sequential, no concurrency. Prompt is 7,763-7,768 tokens depending on the ID.

**Decode measurement.** Two warmup calls then ten measured, `max_tokens=100`, single stream.

## Results

| | decode tok/s | prefill tok/s, cache-missing | wall time for 7.7K tokens |
|---|---|---|---|
| **A — ROCM_AITER_UNIFIED_ATTN** | **34.27** (34.23-34.31) | **5107** (5104-5109) | **1,521 ms** |
| T — TRITON_ATTN | 33.41 (33.36-33.46) | 1098 (1098 on all three) | 7,073 ms |
| difference | +2.6% | **+365%** | -5.55 s |

Both arms: engine started cleanly, Korean output correct, `tool_choice=auto` produced `get_weather {"city": "서울"}`, no GPU error signatures in the kernel log.

**For scale against a different stack.** On our own production image (`vllm/vllm-openai-rocm:v0.23.0`, ROCm 7.2.3, `TRITON_ATTN`) the same cache-missing measurement gives 993 tok/s over six spawns. So moving from our stack to this image is worth about +11% on prefill, and switching the backend within this image is worth another 365%. The backend is where nearly all of it is.

## Two things this does not show

**It does not show that #4868 is what fixed the LDS overflow.** The files that PR lists are present in main, but we cloned with `--depth 50`, so `git log -- <path>` points at the oldest commit inside that window rather than the authoring one. We can say the overflow is gone on main at `6214264`; we cannot attribute it. I have posted the load-success result in #5229 as well, since that was the open question there.

**It does not show that multimodal is correct under the aiter backend.** In #5229 you assumed `TRITON_ATTN` would be needed for multimodal since aiter attention is causal-only. Both arms answered a 256x256 red-circle-on-white PNG correctly ("흰색 배경 위에 빨간색의 둥근 모양" for A, "흰색 배경 중앙에 빨간색 원" for T). That means it runs and is not obviously broken. It does not mean the bidirectional mask over image tokens is handled correctly — a single simple shape would not reveal a subtle regression. If you can suggest an image case that would actually stress that path, we will run it, because this is the one thing blocking us from using the aiter backend in production.

## Offer

The box is a dedicated test machine with no production traffic, single R9700, and we keep raw logs for every spawn. If the tuning approach in #5601 would be worth applying to gfx1201, we can run whatever sweep you want, or test a patch before it merges.


## 评论 (5)

### taisunyoung · 2026-09-19

A planning question, and I'd rather ask it out loud than guess, because the answer changes what we do next.

We are deciding whether to put `ROCM_AITER_UNIFIED_ATTN` on gfx1201 into production — a single R9700 serving a small customer-facing chatbot, not a benchmark box. The 4.65x prefill result above is more than enough reason to want it. What I cannot tell from outside is whether this path is something we can build on.

On 2026-09-10, in vllm-project/vllm#56021, @vllmellm answered a question about that same backend with:

> to the best of our knowledge, at the moment, AITER support for gfx1201 is not in the roadmap

https://github.com/vllm-project/vllm/issues/56021#issuecomment-5612834538

From where I sit that reads the other way from everything in this repo. aiter's README lists the R9700 (gfx1201) as Experimental, `configs/gfx1201/` carries tuned entries for unified attention, #4868 guards the RDNA LDS budget, and you described migrating hot ops to aiter for RDNA precisely to have more control. Those look like active work on the thing the other comment says is not planned.

My guess is that the two statements are about different layers — vLLM enabling and supporting the aiter backend on gfx1201 by default, versus aiter itself carrying working RDNA kernels — and that both can be true at once. But that is a guess, and it is the kind of guess I would rather not build a production decision on.

So, concretely, if we ship this: is `vLLM + ROCM_AITER_UNIFIED_ATTN on gfx1201` a path you expect to keep working, or is it closer to "works today, unsupported, at your own risk"? Two things would tell us most:

- if a future vLLM release breaks backend selection or the aiter path on RDNA, is that a bug worth filing, or expected?
- do the gfx1201 tuning configs get maintained as aiter moves, or were they a one-off for the LDS fix?

I am not asking for a guarantee, and "unsupported but it works" is a perfectly usable answer — we would simply pin versions and carry the risk knowingly, rather than discover it later. What I want to avoid is assuming support that was never offered.

For context on why this is not hypothetical for us: assembling it took three non-obvious steps (source aiter with `AITER_USE_SYSTEM_TRITON=1`, moving the bundled package aside so the source install is not silently ignored, and pinning transformers). None of that is hard once known, but all of it is ours to maintain, and it only makes sense if the underlying path is not about to be dropped.


### amd-xavierwang · 2026-09-19

> to the best of our knowledge, at the moment, AITER support for gfx1201 is not in the roadmap

I am not sure about the background of this developer. We are the dedicated team supporting gfx12 and I can confidently declare we will be supporting more and more aiter backend kernels as a optimal plug-in to vLLM. I think the develop may refer to "GLOBAL" aiter support. To that, apparently no because we are not enabling those CK kernels yet. So the short answer is, aiter is an OPTIONAL plugin to serve vLLM gfx12, but it will include the latest optimizations. Users are encouraged to use it.

That answers your 2 questions: yes, worth filing and yes.

We have other customers demanding OCR(image->text) usage and we will continue investigation. 

`AITER_USE_SYSTEM_TRITON=1` so far remains optional to user. Sometimes it is necessary in some images as the pre-installed vLLM requires a strict TRITON commit tag. Hopefully you don't need to build aiter from source once the latest official image contains the fix to gemma4.

### taisunyoung · 2026-09-20

You mentioned you have customers asking for OCR and that you would keep investigating. I ran the multimodal check we talked about, and the causal-only concern turns out to be real on gfx1201 — with a failure mode that is directly an OCR failure. Details below so you can reproduce rather than take my word for it.

**Setup.** Same image as the numbers above (`rocm/vllm@sha256:30761c21…` + aiter at `6214264`, transformers 5.12.0), gemma-4-12B-it-FP8-Dynamic, `temperature=0`, one process at a time, only `--attention-backend` and `VLLM_ROCM_USE_AITER` differing between the two arms.

Six cases, drawn deterministically with PIL at 384x384, each with a single verifiable answer. I picked tasks that need to attend across the image rather than just name a dominant object, since a single large shape passes even when attention is degraded — our earlier red-circle check passed on both arms and told us nothing.

| case | image | question |
| --- | --- | --- |
| text | `PRIMEAD 7742` in black on white | transcribe it |
| count | seven blue circles | how many |
| binding | red square left, blue triangle right | colour and shape of the left one |
| spatial | green circle top, yellow square bottom | what is at the top |
| corner | small red dot, top-right | which corner |
| text-in-shape | `A3` inside a circle outline | read the text |

**Result: `ROCM_AITER_UNIFIED_ATTN` 3 of 6, `TRITON_ATTN` 6 of 6.**

The text case is the clearest:

```
ground truth   PRIMEAD 7742
TRITON_ATTN    PRIMEAD 7742
AITER          DRINFAZ74
```

Characters are substituted and reordered, not merely misread — which is what I would expect if the image tokens cannot attend bidirectionally.

The other two failures are consistent with that. On the corner case AITER answered bottom-right for a dot that is top-right. On the spatial case it answered that **no shape exists at the top** and described a green *half*-circle at the bottom, when the green circle is at the top; TRITON answered "green circle" plainly.

Even a case AITER passed came out degraded. For the red square it said "pink (or red) … rectangle"; TRITON said "red … square". Hedged colour and wrong shape class, on a 130x130 square.

**One correction to my own numbers.** I first scored this 4 of 6. My checker looked for the substrings 초록 (green) and 원 (circle) for the spatial case, and AITER's wrong answer contained 반원 (half-circle), so the 원 inside it matched and the case passed incorrectly. Re-reading the text, it is a clear miss. 3 of 6 is the honest score, and I mention it because a keyword checker will flatter this backend if anyone reuses one.

**Caveat on strength.** One run per case per backend, so this is not a rate. It is enough to show the failure exists and what it looks like; it is not enough to quantify how often. If a rate would be useful to you I can run each case n times.

For us this closes the question — we serve a multimodal model to customers who send photos of signage, so we cannot take the 4.65x prefill win while text in images comes back scrambled. We will stay on `TRITON_ATTN` for that model. I would rather report this than quietly conclude the backend is unusable, since your team is clearly still working the area and OCR is apparently on your list.

The generator and checker are a single self-contained file, about 100 lines, no dependencies beyond PIL. Happy to paste it here or open it as a gist if it would save you writing one.


### amd-xavierwang · 2026-09-20

Thank you for the information and we will put in effort optimizing non-causal attn path for gfx1201. While you have to stay with `TRITON_ATTN` and I see your model is FP8, can you try locally patch similarly like https://github.com/vllm-project/vllm/pull/37973, put that field to either `True` or `on_rdna4()`? This enables low precision tensor core instructions and may deliver some benefit.

Sadly this means you have to build vLLM from source, which is harder than building aiter from source. I have reached out to vLLM maintainer about this enablement so you can also wait to see this appear in official images.

### taisunyoung · 2026-09-20

I ran your suggestion. Writing the process out in detail first so there is no room for misunderstanding about what was changed, what was measured, and where I am reporting an observation versus where I would be inferring something.

**One correction, and I think it matters for you more than for us.** You wrote that this requires building vLLM from source. On the image you ship, it does not. PR #37973 touches exactly one file, `vllm/v1/attention/backends/triton_attn.py`, and it is plain Python sitting in site-packages. Editing the installed file is enough. This is the whole patch we applied at image build time, with no compiler involved:

```python
import importlib.util, os
spec = importlib.util.find_spec("vllm")          # locate without importing (no GPU at build time)
F = os.path.join(list(spec.submodule_search_locations)[0],
                 "v1", "attention", "backends", "triton_attn.py")
OLD = "        self.supports_quant_query_input = current_platform.is_cuda()"
NEW = ("        from vllm.platforms.rocm import on_gfx12x as _on_gfx12x\n"
       "        self.supports_quant_query_input = current_platform.is_cuda() or (\n"
       "            current_platform.is_rocm() and _on_gfx12x()\n"
       "        )")
src = open(F, encoding="utf-8").read()
assert src.count(OLD) == 1
open(F, "w", encoding="utf-8").write(src.replace(OLD, NEW, 1))
```

If you want other gfx12 users to try this, that is a much lower barrier than a source build, and it means the change can be tested against your published image without rebuilding anything.

**On which predicate to use.** The PR as written gates on `on_mi3xx()`, which returns `False` on gfx1201, so applying the PR unchanged does nothing for us. You suggested `on_rdna4()`; that helper does not exist in the vLLM snapshot in your image, but `on_gfx12x()` does and returns `True` here. I used that. One thing worth flagging: the build container has no GPU, so the patch script must not import `vllm` or call any device-query helper — our first attempt died with `RuntimeError: No CUDA GPUs are available` for exactly that reason.

**Setup.** Your image, `rocm/vllm@sha256:30761c2125ce150d556bef46406a0158446421886bf83a2e60154c6e4ca17a13`, plus aiter at `6214264` and `transformers==5.12.0`. Single Radeon AI PRO R9700 (gfx1201), host kernel 7.0.0-31. Model is gemma-4-12B-it-FP8-Dynamic, `--attention-backend TRITON_ATTN`, `--kv-cache-dtype fp8`, `--enable-prefix-caching`, `cudagraph_mode FULL_AND_PIECEWISE`, `GPU_MAX_HW_QUEUES=1`. The two arms differ only by the patch above; everything else, including the serve command, is byte-identical. Four separate container boots per arm, spread over three independent runs on the same day, alternating arms. On every patched boot we re-read the installed file inside the running container and confirmed the patch was actually present before measuring, because we had previously managed to measure an unpatched image while believing it was patched.

| | prefill, cache-missing 7.7K prompt | decode | 
|---|---|---|
| unpatched | 1102 tok/s (1102–1103) | 33.38 (33.35–33.42) |
| **patched** | **4574 tok/s (4564–4585)** | **36.08 (36.04–36.12)** |
| | **4.15x** | **+8.1%** |

Prefill is measured with a unique nonce at the front of every prompt and `max_tokens=1`, so prefix caching never hits; the rate is `usage.prompt_tokens` over wall time.

For context against the other option on this card: `ROCM_AITER_UNIFIED_ATTN` gives us 5107 tok/s prefill but fails multimodal. This patch reaches 90% of that prefill number on `TRITON_ATTN`, and is faster than either at decode.

**Accuracy, including where our own evidence is weak.** Multimodal held at 6/6 on all four patched boots, using the same six deterministic drawn-image cases from my earlier comment. I weight that result because the gate has demonstrated it can detect real damage: run against `ROCM_AITER_UNIFIED_ATTN` on this same image it scores 3/6, twice, on separate boots, failing the same three cases with the same wrong answers each time. (In my earlier comment I flagged that our scorer had counted one of those as a pass because the model's wrong answer happened to contain a substring of the right one. That is fixed — it now rejects answers that deny the object exists — and the corrected scorer agrees with the 3/6 I reported by hand.)

We also ran a 12-question text gate (needle-in-a-haystack at five depths in a ~7.4K-token document with nine same-format decoys, multi-needle, arithmetic, instruction-following). Both arms scored 12/12. **I do not think you should weight that result, and neither do we.** We ran it against the AITER arm as a negative control and it also scored 12/12, so the gate has not demonstrated any discriminating power. Either it is too easy, or AITER's damage is confined to the bidirectional path and genuinely does not touch causal text — we cannot tell from our data which.

**One finding you may not have from MI3xx: this costs run-to-run determinism.** We generated 15 fixed Korean prompts at `temperature=0, seed=7742, max_tokens=180`, twice per arm on separate container boots, and compared outputs:

| comparison | identical outputs | mean common prefix |
|---|---|---|
| unpatched boot 1 vs boot 2 | **15/15** | 100.0% |
| patched boot 1 vs boot 2 | 8/15 | 71.3% |
| unpatched vs patched | 1/15 | 21.7% / 23.2% |

The unpatched configuration is bit-reproducible across restarts. The patched one is not: two patched boots disagree on 7 of 15 prompts. The self-comparison is the control here — without it the 1/15 figure would not mean anything, since vLLM is not fully deterministic under batching.

Looking at where the outputs actually diverge, the differences read as paraphrase rather than error. A representative one: unpatched *"the moment you notice the incident, tell the customer and admit the mistake; understanding the situation comes before excuses"* versus patched *"the moment you notice the incident, do not hide it or make excuses, admit the facts"*. Same content, different sentences. We found no case where the patched output was factually wrong and the unpatched one right. The arithmetic question produced character-identical answers in every run.

We have put this into production as of today. For a customer-facing chatbot the determinism loss is harmless because we sample at `temperature > 0` anyway, but it does make our own A/B measurements noisier, and if anyone is relying on reproducible greedy decoding on gfx12 they should know before enabling this.

Thank you for pointing at this. It is a far better outcome for us than the backend switch we were considering, and it arrived in a one-line form we could verify in an afternoon.

