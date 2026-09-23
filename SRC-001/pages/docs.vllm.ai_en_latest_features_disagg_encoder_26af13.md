source: https://docs.vllm.ai/en/latest/features/disagg_encoder/
lastmod: 2026-09-23

# Disaggregated Encoder[¶](https://docs.vllm.ai#disaggregated-encoder)

A **disaggregated encoder** runs the vision-encoder stage of a multimodal LLM in a process that is separate from the pre-fill / decoder stage. Deploying these two stages in independent vLLM instances brings three practical benefits:

**Independent, fine-grained scaling****Lower time-to-first-token (TTFT)****Cross-process reuse and caching of encoder outputs**

Design doc: [https://docs.google.com/document/d/1aed8KtC6XkXtdoV87pWT0a8OJlZ-CpnuLLzmR8l9BAE](https://docs.google.com/document/d/1aed8KtC6XkXtdoV87pWT0a8OJlZ-CpnuLLzmR8l9BAE)

## 1 Motivation[¶](https://docs.vllm.ai#1-motivation)

### 1. Independent, fine-grained scaling[¶](https://docs.vllm.ai#1-independent-fine-grained-scaling)

- Vision encoders are lightweight, while language models are orders of magnitude larger.
- The language model can be parallelised without affecting the encoder fleet.
- Encoder nodes can be added or removed independently.

### 2. Lower time-to-first-token (TTFT)[¶](https://docs.vllm.ai#2-lower-time-to-first-token-ttft)

- Language-only requests bypass the vision encoder entirely.
- Encoder output is injected only at required attention layers, shortening the pre-fill critical path.

### 3. Cross-process reuse and caching[¶](https://docs.vllm.ai#3-cross-process-reuse-and-caching)

- In-process encoders confine reuse to a single worker.
- A remote, shared cache lets any worker retrieve existing embeddings, eliminating redundant computation.

## 2 Usage Example[¶](https://docs.vllm.ai#2-usage-example)

### ExampleConnector[¶](https://docs.vllm.ai#exampleconnector)

The following scripts demonstrate the workflow with **ExampleConnector**:

1 Encoder instance + 1 PD instance: `examples/disaggregated/disaggregated_encoder/disagg_1e1pd_example.sh`


1 Encoder instance + 1 Prefill instance + 1 Decode instance: `examples/disaggregated/disaggregated_encoder/disagg_1e1p1d_example.sh`


### ECMooncakeConnector[¶](https://docs.vllm.ai#ecmooncakeconnector)

**ECMooncakeConnector** transfers encoder outputs using the Mooncake TransferEngine. See the [ Mooncake integration example](https://github.com/vllm-project/vllm/blob/main/tests/v1/ec_connector/integration/run_epd_mooncake_ec_full_pipeline.sh) for a complete 1 Encoder instance + 1 PD instance setup, including the producer and consumer `--ec-transfer-config`

settings and proxy configuration.

With vLLM and Mooncake installed, run the example from the repository root:

GPU_E=0 GPU_PD=1 MOONCAKE_EC_PROTOCOL=tcp \
bash tests/v1/ec_connector/integration/run_epd_mooncake_ec_full_pipeline.sh


The script uses `Qwen/Qwen2.5-VL-3B-Instruct`

by default, runs a single-GPU baseline, and compares the disaggregated outputs against it. Set `MODEL`

to use another model or `MOONCAKE_EC_PROTOCOL=rdma`

to use RDMA on supported hardware. See the script for additional configuration options.

### Audio inputs[¶](https://docs.vllm.ai#audio-inputs)

The Python EPD proxy also rewrites audio in `/v1/chat/completions`

into metadata-only references for Qwen2-Audio, AudioFlamingo3, Ultravox, Qwen2.5-Omni, and Qwen3-Omni. The encoder publishes `audio_num_tokens`

(the placeholder token count of each audio) together with any feature lengths the model needs; the consumer uses them to reconstruct the audio placeholders and receives the embeddings through its EC connector without repeating audio preprocessing.

This covers pure audio inputs, not video with an embedded audio track. It does not add `/v1/audio/transcriptions`

or realtime routes to the example proxy.

## 3 Test Script[¶](https://docs.vllm.ai#3-test-script)

For optional cross-Encoder output reuse while retaining Mooncake P2P delivery, see [Cross-encoder output reuse](https://docs.vllm.ai/cross_encoder_cache/).

Please refer to the directories `tests/v1/ec_connector`


## 4 Development[¶](https://docs.vllm.ai#4-development)

Disaggregated encoding is implemented by running two parts:

**Encoder instance**– a vLLM instance to performs vision encoding.**Prefill/Decode (PD) instance(s)**– runs language pre-fill and decode.- PD can be in either a single normal instance with
`disagg_encoder_example.sh`

(E->PD) or in disaggregated instances with`disagg_epd_example.sh`

(E->P->D)

- PD can be in either a single normal instance with

A connector transfers encoder-cache (EC) embeddings from the encoder instance to the PD instance.

All related code is under `vllm/distributed/ec_transfer`

.

### Key abstractions[¶](https://docs.vllm.ai#key-abstractions)

**ECConnector**– interface for retrieving EC caches produced by the encoder.*Scheduler role*– checks cache existence and schedules loads.*Worker role*– loads the embeddings into memory.


Here is a figure illustrating disaggregate encoder flow:

For the PD disaggregation part, the Prefill instance receives cache exactly the same as the disaggregated encoder flow above. Prefill instance executes 1 step (prefill -> 1 token output) and then transfers KV cache to the Decode instance for the remaining execution. The KV transfer part purely happens after the execution of the PD instance.

`docs/features/disagg_prefill.md`

shows the brief idea about the disaggregated prefill (v0)

We create the example setup with the **NixlConnector** from `vllm/distributed/kv_transfer/kv_connector/v1/nixl/`

and referred to the `tests/v1/kv_connector/nixl_integration/toy_proxy_server.py`

to facilitate the kv transfer between P and D;