source: https://docs.vllm.ai/en/latest/features/speculative_decoding/extract_hidden_states/
lastmod: 2026-09-24

# Hidden State Extraction[¶](https://docs.vllm.ai#hidden-state-extraction)

The Hidden State Extraction feature allows vLLM to save intermediate layer activations from a target model during inference. This is useful for training [EAGLE](https://docs.vllm.ai/eagle/)-style draft models, knowledge distillation, or offline analysis of model internals.

Note

It is possible to save the last-layer's output hidden states by passing `num_hidden_layers`

as a layer id. Note that these are *not* normalized using the output norm.

## Offline Example[¶](https://docs.vllm.ai#offline-example)

import tempfile
from vllm import LLM, SamplingParams
from vllm.config.kv_transfer import KVTransferConfig
from vllm.distributed.kv_transfer.kv_connector.v1 import (
example_hidden_states_connector,
)
with tempfile.TemporaryDirectory() as tmpdir:
llm = LLM(
model="Qwen/Qwen3-8B",
speculative_config={
"method": "extract_hidden_states",
"num_speculative_tokens": 1,
"draft_model_config": {
"hf_config": {
"eagle_aux_hidden_state_layer_ids": [1, 2, 3, 4],
},
},
},
kv_transfer_config=KVTransferConfig(
kv_connector="ExampleHiddenStatesConnector",
kv_role="kv_producer",
kv_connector_extra_config={
"shared_storage_path": tmpdir,
},
),
)
outputs = llm.generate(
["The future of AI is"],
SamplingParams(max_tokens=1),
)
for output in outputs:
path = output.kv_transfer_params["hidden_states_path"]
obj = example_hidden_states_connector.load_hidden_states(path)
print(f"token_ids: {obj['token_ids'].shape}")
print(f"hidden_states: {obj['hidden_states'].shape}")


A complete example is available at [ examples/features/speculative_decoding/extract_hidden_states_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/features/speculative_decoding/extract_hidden_states_offline.py).

## Online Example[¶](https://docs.vllm.ai#online-example)

For improved performance, it is recommended to use a RAM-mounted file system such as `/dev/shm/`

for online usage in which the client cleans up the files soon after they are generated.

vllm serve Qwen/Qwen3-8B \
--speculative_config '{"method": "extract_hidden_states", "num_speculative_tokens": 1, "draft_model_config": {"hf_config": {"eagle_aux_hidden_state_layer_ids": [1, 2, 3, 4]}}}' \
--kv_transfer_config '{"kv_connector": "ExampleHiddenStatesConnector", "kv_role": "kv_producer", "kv_connector_extra_config": {"shared_storage_path": "/dev/shm/hidden_states"}}'


## Per-Request Options[¶](https://docs.vllm.ai#per-request-options)

Both offline and online modes support per-request options via `kv_transfer_params`

:

| Parameter | Default | Description |
|---|---|---|
`hidden_states_path` | Auto-generated | Custom file path for saving hidden states. If not set, files are saved to `<shared_storage_path>/<request_id>.safetensors` . Requires `allow_custom_save_path` to be enabled in the server config. |
`include_output_tokens` | `False` | When `True` , save hidden states for both prompt and generated output tokens. When `False` , only prompt token hidden states are saved. |

### Offline usage[¶](https://docs.vllm.ai#offline-usage)

Pass per-request options via `extra_args`

on [ SamplingParams](https://docs.vllm.ai/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams):

SamplingParams(
max_tokens=32,
extra_args={
"kv_transfer_params": {
"hidden_states_path": "/tmp/my_output.safetensors",
"include_output_tokens": True,
}
},
)


### Online usage[¶](https://docs.vllm.ai#online-usage)

Pass `kv_transfer_params`

as a top-level field in the API request:

```json
{
"model": "Qwen/Qwen3-8B",
"messages": [{"role": "user", "content": "Hello"}],
"max_tokens": 32,
"kv_transfer_params": {
"hidden_states_path": "/tmp/my_output.safetensors",
"include_output_tokens": true
}
}
```


## Configuration[¶](https://docs.vllm.ai#configuration)

The `kv_connector_extra_config`

dict accepts these server-level options:

| Parameter | Default | Description |
|---|---|---|
`shared_storage_path` | `/tmp` | Directory where hidden state files are saved (used when `hidden_states_path` is not set per-request) |
`allow_custom_save_path` | `False` | Allow API clients to specify custom file paths via `hidden_states_path` . When disabled, client-provided paths are ignored with a warning. Enable only with trusted clients — custom paths can write to arbitrary locations on the server. |
`num_writer_threads` | `8` | Thread pool size for async disk writes |
`use_synchronization_lock` | `True` | Use file locks so concurrent readers block until writes complete. Can be disabled for batch generation where synchronization is not needed. |

## Output Format[¶](https://docs.vllm.ai#output-format)

Each request produces a `.safetensors`

file containing:

— shape`hidden_states`

`[num_tokens, num_extracted_layers, hidden_size]`

— shape`token_ids`

`[num_tokens]`


The file path is returned in `output.kv_transfer_params["hidden_states_path"]`

. Use `load_hidden_states()`

from the connector module to read the file with proper synchronization.

Note

Chunked prefill is not compatible with this feature and must be disabled.