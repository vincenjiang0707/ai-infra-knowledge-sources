source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/utils/fingerprint/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.utils.fingerprint`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.fingerprint)

Build the `system_fingerprint`

string returned by the OpenAI-compatible server.

Four modes, configured via `--fingerprint-mode`

:

`full`

(default):`vllm-<version>[-<parallelism>]-<hash8>`

— encodes server version, any non-trivial parallelism degree (tp/pp/dp/ep), and an 8-char prefix of`vllm_config.compute_hash()`

(covers model identity, quant config, speculative, attention backend, etc.).`hash`

:`vllm-<version>-<hash8>`

— parallelism stripped.`custom`

: user-provided literal via`--fingerprint-value`

.`none`

: the field is omitted (serialized as`null`

).

`get_system_fingerprint`

is only called at serving-class init (a handful of times per server); each subclass caches the returned string on `self.system_fingerprint`

, so per-request cost is one attribute read.

Functions:

-
–[get_system_fingerprint](https://docs.vllm.ai#vllm.entrypoints.serve.utils.fingerprint.get_system_fingerprint)Return the fingerprint for

`vllm_config`

using the mode configured by -
–[set_default_fingerprint_mode](https://docs.vllm.ai#vllm.entrypoints.serve.utils.fingerprint.set_default_fingerprint_mode)Configure the fingerprint mode for subsequent

`get_system_fingerprint`


##

`get_system_fingerprint(vllm_config)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.fingerprint.get_system_fingerprint)

Return the fingerprint for `vllm_config`

using the mode configured by `set_default_fingerprint_mode`

.

## Source code in `vllm/entrypoints/serve/utils/fingerprint.py`


##

`set_default_fingerprint_mode(mode, custom_value=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.fingerprint.set_default_fingerprint_mode)

Configure the fingerprint mode for subsequent `get_system_fingerprint`

calls. Called once at server startup.