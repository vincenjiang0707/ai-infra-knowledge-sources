# [Issue #298] Using --streaming does not respect --output-tokens-mean

source: https://github.com/triton-inference-server/perf_analyzer/issues/298
state: closed | updated: 2025-03-20T13:14:12Z
labels: bug

## 正文

Hi, 

this is true for kserve API and OpenAI-Frontend API

For example, this was ran against an engine with decoupled_mode=True using --streaming:

```json
{
  "request_throughput": {
    "unit": "requests/sec",
    "avg": 17.222547659562533
  },
  "request_latency": {
    "unit": "ms",
    "avg": 5767.434807386666,
    "p25": 5675.43159275,
    "p50": 5778.654798,
    "p75": 5858.190923,
    "p90": 5882.4496025,
    "p95": 5892.6711992499995,
    "p99": 5910.154859249999,
    "min": 5573.489708,
    "max": 5922.384083999999,
    "std": 94.06435995440489
  },
  "time_to_first_token": {
    "unit": "ms",
    "avg": 184.63779366666665,
    "p25": 124.51677875,
    "p50": 172.8093975,
    "p75": 234.43528899999998,
    "p90": 302.80112349999996,
    "p95": 351.02043655,
    "p99": 425.02943662,
    "min": 21.083577,
    "max": 511.752837,
    "std": 87.809553196227
  },
  "inter_token_latency": {
    "unit": "ms",
    "avg": 2.1767344516666665,
    "p25": 2.1531955,
    "p50": 2.1787205,
    "p75": 2.2050785,
    "p90": 2.2333102,
    "p95": 2.2451001999999995,
    "p99": 2.2631232999999997,
    "min": 2.0128619999999997,
    "max": 2.273656,
    "std": 0.04455038259900428
  },
  "output_token_throughput": {
    "unit": "tokens/sec",
    "avg": 44190.56002502682
  },
  "output_token_throughput_per_request": {
    "unit": "tokens/sec",
    "avg": 445.00388376637636,
    "p25": 438.44808628608826,
    "p50": 444.1575106746062,
    "p75": 451.4403643296028,
    "p90": 455.951247943241,
    "p95": 458.2202987708462,
    "p99": 461.0808551078099,
    "min": 430.8182735591475,
    "max": 464.2152390830441,
    "std": 7.837188059178782
  },
  "output_sequence_length": {
"unit": "tokens",
    "avg": 2565.855,
    "p25": 2551.0,
    "p50": 2567.0,
    "p75": 2578.0,
    "p90": 2590.1,
    "p95": 2595.1,
    "p99": 2608.1099999999997,
    "min": 2522.0,
    "max": 2619.0,
    "std": 18.025277852689722
  },
  "input_sequence_length": {
    "unit": "tokens",
    "avg": 200.85,
    "p25": 188.75,
    "p50": 202.0,
    "p75": 212.0,
    "p90": 225.30000000000007,
    "p95": 234.04999999999995,
    "p99": 244.1099999999999,
    "min": 151.0,
    "max": 255.0,
    "std": 19.752151781514844
  },
  "input_config": {
"subcommand": "profile",
    "model": [
      "ensemble"
    ],
    "model_selection_strategy": "round_robin",
    "backend": "tensorrtllm",
    "endpoint": null,
    "endpoint_type": "kserve",
    "service_kind": "triton",
    "server_metrics_url": null,
    "streaming": true,
    "u": "localhost:8001",
    "batch_size_image": 1,
    "batch_size_text": 1,
    "goodput": null,
    "num_dataset_entries": 100,
    "output_tokens_mean": 500,
    "output_tokens_mean_deterministic": false,
    "output_tokens_stddev": 0,
    "random_seed": 0,
    "request_count": 0,
    "synthetic_input_tokens_mean": 200,
    "synthetic_input_tokens_stddev": 20,
    "warmup_request_count": 0,
    "image_width_mean": 100,
    "image_width_stddev": 0,
    "image_height_mean": 100,
    "image_height_stddev": 0,
    "image_format": null,
    "concurrency": 100,
    "measurement_interval": 10000,
    "request_rate": null,
    "stability_percentage": 999,
    "artifact_dir": "test_c100",
    "generate_plots": false,
    "profile_export_file": "test_c100/profile_export.json",
    "tokenizer": "/path/to/tokenizer",
    "tokenizer_revision": "main",
    "tokenizer_trust_remote_code": false,
    "verbose": false,
    "synthetic_input_files": null,
    "prompt_source": "synthetic",
    "formatted_model_name": "ensemble",
    "extra_inputs": {}
  }
}
```

This was run without streaming:

```json
{
  "request_throughput": {
    "unit": "requests/sec",
    "avg": 21.621765653636075
  },
  "request_latency": {
    "unit": "ms",
    "avg": 4610.6156361171425,
    "p25": 4348.18888325,
    "p50": 4355.8502165,
    "p75": 4376.884887,
    "p90": 6099.6698079,
    "p95": 6153.30871085,
    "p99": 6156.11159006,
    "min": 4320.157834,
    "max": 6159.486191999999,
    "std": 619.1754644200283
  },
  "time_to_first_token": {
    "unit": "ms",
    "avg": 4610.6156361171425,
    "p25": 4348.18888325,
    "p50": 4355.8502165,
    "p75": 4376.884887,
    "p90": 6099.6698079,
    "p95": 6153.30871085,
    "p99": 6156.11159006,
    "min": 4320.157834,
    "max": 6159.486191999999,
    "std": 619.1754644200283
  },
  "output_token_throughput": {
    "unit": "tokens/sec",
    "avg": 12277.70340876071
  },
  "output_token_throughput_per_request": {
    "unit": "tokens/sec",
    "avg": 124.9297556181573,
    "p25": 125.39458895180717,
    "p50": 129.43013719041846,
    "p75": 132.4910851223956,
    "p90": 135.42441655744616,
    "p95": 137.0838632612868,
    "p99": 139.99996227362487,
    "min": 86.94794864149334,
    "max": 143.0820522995335,
    "std": 13.770501362258067
  },
  "output_sequence_length": {
    "unit": "tokens",
    "avg": 567.84,
    "p25": 553.0,
    "p50": 567.0,
    "p75": 580.0,
    "p90": 591.1,
    "p95": 599.0999999999999,
    "p99": 609.1299999999999,
    "min": 531.0,
    "max": 622.0,
    "std": 17.983884849656768
  },
  "input_sequence_length": {
    "unit": "tokens",
    "avg": 200.85,
    "p25": 188.75,
    "p50": 202.0,
    "p75": 212.0,
    "p90": 225.30000000000007,
    "p95": 234.04999999999995,
    "p99": 244.1099999999999,
    "min": 151.0,
    "max": 255.0,
    "std": 19.752151781514844
  },
  "input_config": {
    "subcommand": "profile",
    "model": [
      "ensemble"
    ],
    "model_selection_strategy": "round_robin",
    "backend": "tensorrtllm",
    "endpoint": null,
    "endpoint_type": "kserve",
    "service_kind": "triton",
    "server_metrics_url": null,
    "streaming": false,
    "u": "localhost:8001",
    "batch_size_image": 1,
    "batch_size_text": 1,
    "goodput": null,
    "num_dataset_entries": 100,
    "output_tokens_mean": 500,
    "output_tokens_mean_deterministic": false,
    "output_tokens_stddev": 0,
    "random_seed": 0,
    "request_count": 0,
    "synthetic_input_tokens_mean": 200,
    "synthetic_input_tokens_stddev": 20,
    "warmup_request_count": 0,
    "image_width_mean": 100,
    "image_width_stddev": 0,
    "image_height_mean": 100,
    "image_height_stddev": 0,
    "image_format": null,
    "concurrency": 100,
    "measurement_interval": 10000,
    "request_rate": null,
    "stability_percentage": 999,
    "artifact_dir": "test_c100",
    "generate_plots": false,
    "profile_export_file": "test_c100/profile_export.json",
    "tokenizer": "/path/to/tokenizer",
    "tokenizer_revision": "main",
    "tokenizer_trust_remote_code": false,
    "verbose": false,
    "synthetic_input_files": null,
    "prompt_source": "synthetic",
    "formatted_model_name": "ensemble",
    "extra_inputs": {}
  }
}
```

The avg output tokens differ a lot.

Best regards,
John

## 评论 (7)

### the-david-oy · 2025-02-27

Can you try using the latest version of GenAI-Perf? A bug was in 24.11-24.12 that resulted in the wrong output sequence lengths (5x the requested OSL) in in the streaming case. It was fixed in 25.01, I believe.

### jolyons123 · 2025-02-28

Hi @dyastremsky ,

I redo the experiments with the following setup using the nvcr.io/nvidia/tritonserver:25.02-py3-sdk image:

`--synthetic-input-tokens-mean 200, --output-tokens-mean 500, --concurrency 100, --measurement-interval 10000`

**Triton+TRTLLM backend, OpenAI Frontend Endpoint**

Streaming: ON
<img width="1287" alt="Image" src="https://github.com/user-attachments/assets/27e6cedd-c604-447d-a239-2dd33c6a118b" />

Streaming: OFF
<img width="1231" alt="Image" src="https://github.com/user-attachments/assets/2ff99192-84ec-4432-b898-626101445c97" />

**Triton+TRTLLM backend, KServe Endpoint**

Streaming: ON
<img width="1245" alt="Image" src="https://github.com/user-attachments/assets/10d2d789-d453-4552-babe-328c4e322cf8" />

Streaming: OFF
<img width="1241" alt="Image" src="https://github.com/user-attachments/assets/52d0a4e9-f584-4eff-b658-a3307a9f0e3a" />


Now, the average output sequence length when using KServe endpoints is similar in streaming/non-streaming scenarios.

However, when using the Triton OpenAI Frontend chat endpoints, the average output sequence length does not really match my expectations. Also, when using Triton OpenAI Frontend chat endpoints in conjunction with streaming the performance seems to be very bad.

So, regarding the difference in average output sequence length, is there perhaps a problem with the default sampling parameters set for one of these endpoints?

### the-david-oy · 2025-02-28

The first thing that strikes me is that there is variability in the input sequence length (ISL). Assuming your --synthetic-input-tokens-stddev is not set (defaults to 0), are you sure you are using the correct tokenizer? Something is off there.

As far as the output sequence length (OSL), you can try using --output-tokens-mean-deterministic, if that is available for that endpoint. That generally makes it longer though, not shorter (it sets args like min_tokens and ignore_eos, where they are available... you can also do this with the --extra-inputs flag).

I don't know why they would differ between the two endpoints. Is there anything server-specific? Streaming is generally going to have more variability. The OSL is what we request from the server and it is the number of tokens it individually generates. However, that differs from the amount of tokens in the final text due to the way tokenization works (it may tokenize it more/less efficiently in some cases), and we see empirically that difference is higher in the streaming case. If you prefer, you can recalculate the metrics using the OSL you requested, since that is the OSL that the server will report. GenAI-Perf just tokenizes the final response text to ensure the numbers reported rather than relying on what the server reports, which has trade-offs.

The other thing that we or you could review is the inputs.json generated. If the values are correct there, then GenAI-Perf is requesting the correct output sequence length from the server.

CC: @nv-hwoo @debermudez 

### nv-hwoo · 2025-02-28

@jolyons123 Could you provide the full command that you used to run the experiments? Also, as @dyastremsky mentioned, if you could provide `inputs.json` and `profile_export.json` file generated under the artifacts directory would be very helpful for our investigation as well.

Edit: Also, which version of Triton+TRTLLM backend container are you using?

### jolyons123 · 2025-03-03

Hi @dyastremsky @nv-hwoo ,

thanks for your quick replies.

My script is also using `--synthetic-input-tokens-stddev 20`, sorry I forgot to mention that.

The full command is:
```bash
genai-perf profile -m "$MODEL" -u "$HOST_AND_PORT" \
    "${ENDPOINT_ARGS[@]}" "${STREAMING_ARGS[@]}" \
    --synthetic-input-tokens-mean 200 --synthetic-input-tokens-stddev 20 \
    --output-tokens-mean 500 \
    --artifact-dir "$OUTPUT_DIR_SUFFIX" \
    --measurement-interval 10000 --concurrency 100 \
    --tokenizer /root/.cache/huggingface/hub/models--hf-internal-testing--llama-tokenizer/snapshots/d02ad6cb9dd2c2296a6332199fa2fdca5938fef0/ \
    -- \
    -v \
    --max-threads=200
``` 

Good point with the tokenizer, that explains why genai-perf reports 599 because there is differences how the "testing llama" tokenizer and the one used by the model (llama 3.1 8b) tokenize. However, that still does not explain the difference in generated tokens regarding the OpenAI Frontend endpoints.

Regarding the triton container, I am using `tritonserver:24.12-trtllm-python-py3` and `trtllm-build -h` reports 0.16.0.

See attached benchmark tarball for the files requested.

Thanks for your help :)

[benchmarks.tar.gz](https://github.com/user-attachments/files/19049912/benchmarks.tar.gz)

### the-david-oy · 2025-03-03

You don't have any args to require the token count to be what you set it to on the minimum side. For Triton, you can use the flag --output-tokens-mean-deterministic. We don't yet support it for OpenAI, but you can manually set the args. It depends on the frontend. You can often set `--extra-args ignore_eos:true`. It depend on the backend/model-API, but I believe you can also set `--extra-args min_length:500`, since this is for TRT-LLM (this is what GenAI-Perf does internally when setting `--output-tokens-mean-deterministic` for Triton + TRT-LLM).

What's probably happening is because there's nothing requiring the server to keep producing tokens, it stops early.

### jolyons123 · 2025-03-20

Hi @dyastremsky , thanks, I tried the --extra-inputs with genaiperf+openai endpoints but the min_length seems to be not supported yet on openai frontend side. But I think the issue is resolved :)


