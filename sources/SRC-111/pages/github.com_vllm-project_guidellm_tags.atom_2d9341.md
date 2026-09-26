source: https://github.com/vllm-project/guidellm/tags.atom

```
tag:github.com,2008:https://github.com/vllm-project/guidellm/releasesTags from guidellm2026-09-16T16:02:13Ztag:github.com,2008:Repository/807840349/v0.7.42026-09-16T19:53:50ZGuideLLM v0.7.4<p>Bound token events by when they occur (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/1079">#1079</a>)</p>
<p>Modify the request bounding code to use different event bounds for each latency event. See <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/issues/1078">#1078</a> for more details.</p>
<p>Run a benchmark with warmup and verify differences in collected ttft, token throughput, etc. Note that when running a shorter concurrent run with rampup+warmup vs a longer run with no rampup+warmup the results of the shorter run should be closer than without this patch.</p>
<p>```sh
<br />guidellm run \
<br /> --backend kind=openai_http,target=<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>
<br /> --profile kind=concurrent,rampup_duration=45,warmup=75 \
<br /> --override profile.streams 200 --data "kind=synthetic_text,prompt_tokens=500,output_tokens=512" \
<br /> --constraint kind=max_duration,seconds=275
<br />```</p>
<p>- <span class="issue-keyword tooltipped tooltipped-se">Resolves</span> <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/issues/1078">#1078</a></p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted below."</p>
<p>- [x] Includes code generated or substantially modified by an AI agent
<br />- [x] Includes tests generated or substantially modified by an AI agent</p>
<p>> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](<a href="https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md">https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md</a>) file.</p>
<p>---</p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/202b75d8b2837de269801aee34c8c4577257e6a3"><tt>202b75d</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Tue Sep 1 21:06:45 2026 +0000</p>
<p> Clip metrics by start/stop</p>
<p> Only count thoughput that falls within start/stop and only count TTFTs
<br /> that fall fully inside start/stop.</p>
<p> Assisted-by: Codex
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/efb83142c3dbc2b1fcc0b28c7788393e9f358aa9"><tt>efb8314</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Mon Sep 14 18:01:01 2026 -0400</p>
<p> Bound token latency events by when they occur</p>
<p> TTFT, TTFOT, and ITL are all events the occur during the part of the
<br /> request. When calculating which events are inside the main phase (happen
<br /> after warmup and before cooldown) we want to bound by the event itself
<br /> rather than the request. For first token also be a bit more strict and
<br /> ensure that the whole event is within latency bounds.</p>
<p> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/b70695cebb03dafcb725545ea3a6a4e7e5830666"><tt>b70695c</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Tue Sep 15 12:00:18 2026 -0400</p>
<p> Switch TTFT and TTFOT to open range</p>
<p> When getting prefill events within the main range switch to including
<br /> requests that partially overlap the main phase. This matches how other
<br /> metrics are handled. It is still debatable which approch is better,
<br /> since we are on a bit of a time crunch to get this out stick with this
<br /> approch for now and do more testing in post.</p>
<p> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/308d051cdc81ab2b545c53a04b834cd8f1c29a54"><tt>308d051</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Tue Sep 15 17:48:30 2026 +0000</p>
<p> Fix and add tests</p>
<p> Generated-by: Cursor
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/91637e5655c83f6d5d10e593988c925e34eef141"><tt>91637e5</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Tue Sep 15 18:25:59 2026 +0000</p>
<p> Add a little documentation for warmup/cooldown</p>
<p> Assisted-by: Cursor
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/72fc6d5728d2c8bef60d492bf607b92beec69a16"><tt>72fc6d5</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Tue Sep 15 16:21:12 2026 -0400</p>
<p> Address review</p>
<p> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>---------</p>
<p>Assisted-by: Codex
<br />Assisted-by: Cursor
<br />Generated-by: Cursor
<br />Signed-off-by: Samuel Monson <smonson@redhat.com></p>sjmonsontag:github.com,2008:Repository/807840349/v0.7.32026-07-31T20:06:17ZGuideLLM v0.7.3<p>Update click to 8.4 (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/978">#978</a>)</p>
<p>## Summary</p>
<p>## Details</p>
<p>A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2.</p>
<p>Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers.</p>
<p>We resolve this by bumping click to 8.4. In the AIPCC build base image, this allows huggingface_hub 1.23 and transformers 5.14.1, which does not have the CVEs at issue.</p>
<p>## Test Plan</p>
<p>- I ran a container build using (essentially) the AIPCC Containerfile, on the 3.5 builder base image (but copying in my local source and using `pip install ".[all]"`), and verified that it binds transformers 5.14.1.
<br />- A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image.</p>
<p>## Related Issues</p>
<p>N/A</p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted below."</p>
<p>## Use of AI</p>
<p>- [ ] Includes code generated or substantially modified by an AI agent
<br />- [ ] Includes tests generated or substantially modified by an AI agent</p>
<p>> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](<a href="https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md">https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md</a>) file.</p>
<p>---</p>
<p># git log</p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/fdb89ab0ce2a942ad34364428840cac91ac80b14"><tt>fdb89ab</tt></a>
<br />Author: David Butenhof <dbutenho@redhat.com>
<br />Date: Fri Jul 31 14:18:03 2026 -0400</p>
<p> Update click to 8.4
<br />
<br /> A transitive dependency collision in the AIPCC build environment caused us to
<br /> bind transformers < 5.0, and failing to resolve the transformers CVEs for
<br /> which we released 0.7.2.
<br />
<br /> Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0,
<br /> while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit
<br /> dependency on click 8.4, which caused us to bind 0.38 and an equally old
<br /> transformers.
<br />
<br /> We resolve this by bumping click to 8.4. In the AIPCC build base image, this
<br /> binds to transformers 5.14.1, which does not have the CVEs at issue.
<br />
<br /> I ran a container build using (essentially) the AIPCC Containerfile, on the
<br /> 3.5 builder base image (but copying in my local source and using
<br /> `pip install ".[all]"`), and verified that it binds transformers 5.14.1.
<br />
<br /> A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image.
<br />
<br /> Signed-off-by: David Butenhof <dbutenho@redhat.com></p>
<p>---------</p>
<p>Signed-off-by: David Butenhof <dbutenho@redhat.com></p>dbutenhoftag:github.com,2008:Repository/807840349/v0.7.22026-07-23T20:01:23ZGuideLLM v0.7.2<p>Renamed `guidellm benchmark from-file` to `guidellm export` (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/960">#960</a>)</p>
<p>## Summary</p>
<p>Renames it as planned for 0.7</p>
<p>## Details</p>
<p>- Should have no other changes.</p>
<p>## Test Plan</p>
<p>Run the export commands</p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted below."</p>
<p>## Use of AI</p>
<p>- [x] Includes code generated or substantially modified by an AI agent
<br />- [x] Includes tests generated or substantially modified by an AI agent</p>
<p>> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](<a href="https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md">https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md</a>) file.</p>
<p>---</p>
<p># git log</p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/e4abdd0fe19af4501fb9cc347d86e612c2307789"><tt>e4abdd0</tt></a>
<br />Author: Jared O'Connell <joconnel@redhat.com>
<br />Date: Thu Jul 23 15:34:53 2026 -0400</p>
<p> Renamed `guidellm benchmark from-file` to `guidellm export`
<br />
<br /> Generated-by: Cursor AI
<br /> Signed-off-by: Jared O'Connell <joconnel@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/3ef8020943861336c52650c78ce8575898c081d7"><tt>3ef8020</tt></a>
<br />Author: Jared O'Connell <joconnel@redhat.com>
<br />Date: Thu Jul 23 15:46:14 2026 -0400</p>
<p> Fix linting
<br />
<br /> Signed-off-by: Jared O'Connell <joconnel@redhat.com></p>
<p>---------</p>
<p>Generated-by: Cursor AI
<br />Signed-off-by: Jared O'Connell <joconnel@redhat.com></p>dbutenhoftag:github.com,2008:Repository/807840349/v0.7.12026-07-02T20:10:02ZGuideLLM v0.7.1<p>Expose requeue delay from datasets (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/871">#871</a> Cont.) (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/876">#876</a>)</p>
<p>## Summary
<br />Continuation of PR <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/871">#871</a>.</p>
<p>## Details
<br />- Add `requeue_delay_column` to the column mapper
<br />- Add `synthetic_text` dataset support for requeue delay
<br />- Add basic tests in `test_synthetic.py`</p>
<p>## Test Plan
<br />- `tox`</p>
<p>## Related Issues
<br />- <span class="issue-keyword tooltipped tooltipped-se">Resolves</span> <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/871">#871</a> </p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted below."</p>
<p>## Use of AI</p>
<p>- [ ] Includes code generated or substantially modified by an AI agent
<br />- [ ] Includes tests generated or substantially modified by an AI agent</p>
<p>> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](<a href="https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md">https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md</a>) file.</p>
<p>---</p>
<p># git log</p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/254da7adbdb0334833646f87b8f5899d4c3951b1"><tt>254da7a</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Mon Jun 29 14:45:28 2026 -0400</p>
<p> Fix interface between data and scheduler
<br />
<br /> The scheduler has no concept of a GenerationRequest so move the request
<br /> settings out as a separate object in a tuple.
<br />
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/e69d65e7387826854414e145317c4ef8b76b7cd1"><tt>e69d65e</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Mon Jun 29 15:48:32 2026 -0400</p>
<p> Move requeue delay to request settings
<br />
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/a12e1351aeafcebdc8dcda922c44d7cac07acc14"><tt>a12e135</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Mon Jun 29 16:19:12 2026 -0400</p>
<p> Fixup Tests
<br />
<br /> Generated-by: claude-code Opus 4.6
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/873245942bb4cc7bde8e13296783edbdef47c886"><tt>8732459</tt></a>
<br />Author: SkiHatDuckie <SkiHatDuckie@gmail.com>
<br />Date: Wed Jul 1 14:56:34 2026 -0400</p>
<p> Add requeue_delay_column to column mapper
<br />
<br /> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/f600d71479aa9c6efe4591c0f45c08708c9f6b1b"><tt>f600d71</tt></a>
<br />Author: SkiHatDuckie <SkiHatDuckie@gmail.com>
<br />Date: Wed Jul 1 15:26:06 2026 -0400</p>
<p> synthetic text dataset support for requeue delay
<br />
<br /> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/a24430b0945fb3399fa626af2ef5f5b0fd0c9a36"><tt>a24430b</tt></a>
<br />Author: SkiHatDuckie <SkiHatDuckie@gmail.com>
<br />Date: Wed Jul 1 16:25:51 2026 -0400</p>
<p> Add basic tests
<br />
<br /> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/0a1a2a52c21e268582434e6ce3b474820c8a1f43"><tt>0a1a2a5</tt></a>
<br />Author: Samuel Monson <smonson@redhat.com>
<br />Date: Wed Jul 1 17:44:40 2026 -0400</p>
<p> Don't clear request_info after _process_next_request
<br />
<br /> Signed-off-by: Samuel Monson <smonson@redhat.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/97a6076b07516033d4dbb5667d34a710a1a1ee0b"><tt>97a6076</tt></a>
<br />Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
<br />Date: Thu Jul 2 15:18:32 2026 -0400</p>
<p> Rework random number generation logic
<br />
<br /> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/738257bef1e4137a589a0668de6dbbfb87c8da46"><tt>738257b</tt></a>
<br />Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
<br />Date: Thu Jul 2 15:20:55 2026 -0400</p>
<p> Rework random number generation logic x2
<br />
<br /> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/6a2dea36ee543dc036d806290356b4f07fea6f16"><tt>6a2dea3</tt></a>
<br />Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
<br />Date: Thu Jul 2 15:29:52 2026 -0400</p>
<p> fix: Call correct random generator
<br />
<br /> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/25048e972261695fb58dc252f1e46b3ec68d0090"><tt>25048e9</tt></a>
<br />Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
<br />Date: Thu Jul 2 15:33:36 2026 -0400</p>
<p> Don't round in FloatRangeSampler
<br />
<br /> Co-authored-by: Samuel Monson <smonson@irbash.net>
<br /> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com></p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/8b68f6766e6a7b6c56d93b456a70bfefc21de65a"><tt>8b68f67</tt></a>
<br />Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
<br />Date: Thu Jul 2 15:38:09 2026 -0400</p>
<p> Set minimum val of calc_min to 0.0 instead of 1
<br />
<br /> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com></p>
<p>---------</p>
<p>Co-authored-by: Samuel Monson <smonson@irbash.net>
<br />Generated-by: claude-code Opus 4.6
<br />Signed-off-by: Samuel Monson <smonson@redhat.com>
<br />Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>
<br />Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com></p>dbutenhoftag:github.com,2008:Repository/807840349/v0.7.02026-06-30T14:06:58ZGuideLLM v0.7.0<p>Fix up doc linkages (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/870">#870</a>)</p>
<p>## Summary</p>
<p>Minor doc site tweaks for the migration guide.</p>
<p>## Details</p>
<p>After looking at the nightly publication at <a href="https://vllm-project.github.io/guidellm/main">https://vllm-project.github.io/guidellm/main</a> I've made a few minor tweaks:</p>
<p>- [x] Added the migration document to the Guides index page
<br />- [x] Changed the title of the document to clarify the context</p>
<p>Neither of these are probably worth delaying release on Monday morning -- but if anyone happens to review over the weekend and we can get it in, that'd be good.</p>
<p>## Test Plan</p>
<p>I built/deployed a local mkdocs server to check the appearance.</p>
<p>## Related Issues</p>
<p>N/A</p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted below."</p>
<p>## Use of AI</p>
<p>- [ ] Includes code generated or substantially modified by an AI agent
<br />- [ ] Includes tests generated or substantially modified by an AI agent</p>
<p>> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](<a href="https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md">https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md</a>) file.</p>
<p>---</p>
<p># git log</p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/9eba616916e3964da785339376b1d6cb77b308f0"><tt>9eba616</tt></a>
<br />Author: David Butenhof <dbutenho@redhat.com>
<br />Date: Sat Jun 27 13:30:45 2026 -0400</p>
<p> Fix up doc linkages
<br />
<br /> Signed-off-by: David Butenhof <dbutenho@redhat.com></p>
<p>---------</p>
<p>Signed-off-by: David Butenhof <dbutenho@redhat.com></p>dbutenhoftag:github.com,2008:Repository/807840349/v0.6.12026-06-23T14:52:46ZGuideLLM v0.6.1<p>Upgrade 0.6 torch dependencies (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/837">#837</a>)</p>
<p>## Summary</p>
<p>Upgrade torch and torchcodec dependencies for RHAI 3.5 compatibility</p>
<p>## Details</p>
<p>We want to release a GuideLLM container image for RHAI 3.5, supporting full multimodal testing. However, RHAI 3.5 provides torch 2.11.0 and torchcodec 0.11.0, while GuideLLM 0.6.0 requires torch 2.10 and torchcodec 0.11.</p>
<p>This upgrades the dependencies.</p>
<p>## Test Plan</p>
<p>Manually run the audio, image, and video workloads against Qwen/Qwen3-0.6B model (which I had running) as well as Qwen/Qwen3-VL-2B-Instruct (referenced by documentation).</p>
<p>- [x] uv run guidellm benchmark --target http://*.example.com --request-type audio_transcriptions --profile synchronous --max-requests 20 --data openslr/librispeech_asr --data-args "{\"name\": \"clean\", \"split\": \"test\"}" --data-column-mapper "{\"audio_column\": \"audio\"}"
<br />- [x] uv run guidellm benchmark --target http://*.example.com --request-type chat_completions --profile synchronous --max-requests 20 --data "lmms-lab/MMBench_EN" --data-args "{\"split\": \"test\"}" --data-column-mapper '{"image_column": "image", "text_column": "question"}'
<br />- [x] uv run guidellm benchmark --target http://*.example.com --request-type chat_completions --profile synchronous --max-requests 50 --data "lmms-lab/Video-MME" --data-args "{\"split\": \"test\"}" --data-column-mapper '{"video_column": "url"}'</p>
<p>In this case the results (and ultimate success) are interesting but not really the point: it does not appear that the torch/torchcodec package upgrade caused problems in GuideLLM orchestration.</p>
<p>## Related Issues</p>
<p><a href="https://redhat.atlassian.net/browse/AIPCC-16597">https://redhat.atlassian.net/browse/AIPCC-16597</a></p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted below."</p>
<p>## Use of AI</p>
<p>- [ ] Includes code generated or substantially modified by an AI agent
<br />- [ ] Includes tests generated or substantially modified by an AI agent</p>
<p>> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](<a href="https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md">https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md</a>) file.</p>
<p>---</p>
<p># git log</p>
<p>commit <a class="commit-link" href="https://github.com/vllm-project/guidellm/commit/292f458fa9d57b4f7e6a9b85d03832610f3ba820"><tt>292f458</tt></a>
<br />Author: David Butenhof <dbutenho@redhat.com>
<br />Date: Tue Jun 23 09:14:27 2026 -0400</p>
<p> Upgrade 0.6.0 torch dependencies
<br />
<br /> We want to release a GuideLLM container image for RHAI 3.5, supporting full
<br /> multimodal testing. However, RHAI 3.5 builds torch 2.11.0 and torchcodec
<br /> 0.11.0, while GuideLLM 0.6.0 requires torch 2.10 and torchcodec 0.11.
<br />
<br /> This upgrade the dependencies.
<br />
<br /> Signed-off-by: David Butenhof <dbutenho@redhat.com></p>
<p>---------</p>
<p>Signed-off-by: David Butenhof <dbutenho@redhat.com></p>dbutenhoftag:github.com,2008:Repository/807840349/v0.6.02026-04-01T21:44:10ZGuideLLM v0.6.0<p>Revert back to iterating over lines (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/680">#680</a>)</p>
<p>## Summary</p>
<p>Partially reverts <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/663">#663</a> to iterating over lines, but keeps the skipping
<br />of blank newlines.</p>
<p>## Details</p>
<p><a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/663">#663</a> switched the HTTP backend to iterating over byte strings. The
<br />problem is that is did not handle the case where a line was split over
<br />multiple iterations.</p>
<p>## Test Plan</p>
<p>Run a benchmark with known errored request rate (preferably 0) and
<br />ensure that there are no failed requests due to `orjson.JSONDecodeError:
<br />unexpected end of data`.</p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted
<br />below."</p>
<p>## Use of AI</p>
<p>- [ ] Includes AI-assisted code completion
<br />- [ ] Includes code generated by an AI application
<br />- [ ] Includes AI-generated tests (NOTE: AI written tests should have a
<br />docstring that includes `## WRITTEN BY AI ##`)</p>dbutenhoftag:github.com,2008:Repository/807840349/v0.5.42026-03-12T18:44:48ZGuideLLM v0.5.4<p>PATCH Change UI template version to match branch</p>
<p>Signed-off-by: Samuel Monson <smonson@redhat.com></p>sjmonsontag:github.com,2008:Repository/807840349/v0.5.32026-01-23T18:44:10ZGuideLLM v0.5.3<p>Added rampup to constant rate type (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/549">#549</a>)</p>
<p>## Summary</p>
<p>Simply allows a linear rampup of the constant rate profile.</p>
<p>## Test Plan</p>
<p>The simplest test is to run a short constant test with 4 requests per
<br />second, with a long rampup. You can see how it ramps as expected.
<br />There are also new tests.</p>
<p>## Related Issues</p>
<p>Fulfills part of the goals of <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/428">#428</a> </p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted
<br />below."</p>
<p>## Use of AI</p>
<p>- [ ] Includes AI-assisted code completion
<br />- [x] Includes code generated by an AI application
<br />- [x] Includes AI-generated tests (NOTE: AI written tests should have a
<br />docstring that includes `## WRITTEN BY AI ##`)</p>sjmonsontag:github.com,2008:Repository/807840349/v0.5.22026-01-16T20:29:57ZGuideLLM v0.5.2<p>OpenAI API-Key Support (<a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/535">#535</a>)</p>
<p>## Summary</p>
<p>A basic set of changes to add the api key as a bearer token to all
<br />relevant requests.</p>
<p>## Details</p>
<p>- The user passes the api key in as an argument to the backend
<br />- OpenAI's protocol specifies that it should be specified as a bearer
<br />token
<br />- Headers are merged, because requests can have
<br />- This PR also cleans up dead code that was unused since the refactor
<br />- I excluded the API key from the info data structure for security
<br />purposes. Let me know if some info belongs there, like a boolean value
<br />specifying if an API key is provided, or if a cryptic hash of the token
<br />would be helpful. But otherwise I think it's good as-is.</p>
<p>## Test Plan</p>
<p>Run a vLLM server with the option `--api-key <your API key>` passed in.
<br />After doing that, run a PR with this not specified, guidellm would
<br />usually fail. Try with the options as documented in this PR's content,
<br />and it should work.</p>
<p>## Related Issues</p>
<p>- <span class="issue-keyword tooltipped tooltipped-se">Resolves</span>: <a class="issue-link js-issue-link" href="https://github.com/vllm-project/guidellm/pull/491">#491</a> </p>
<p>---</p>
<p>- [x] "I certify that all code in this PR is my own, except as noted
<br />below."</p>
<p>## Use of AI</p>
<p>- [x] Includes AI-assisted code completion
<br />- [x] Includes code generated by an AI application
<br />- [ ] Includes AI-generated tests (NOTE: AI written tests should have a
<br />docstring that includes `## WRITTEN BY AI ##`)</p>sjmonson
```