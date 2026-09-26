source: https://github.com/vllm-project/guidellm/commit/a224a86e2afd61f26e876cb00626c9813271a5cb

|
`37` | `37` | "OpenAIHTTPBackend",
|
`38` | `38` | ]
|
`39` | `39` |
|
`40` |
| `-`MIN_API_KEYS_FOR_ROTATION = 2 |
`41` |
| `-` |
`42` | `40` |
|
`43` | `41` | @Backend.register("openai_http")
|
`44` | `42` | class OpenAIHTTPBackend(Backend):
|
@@ -79,32 +77,39 @@ def __init__(
|
`79` | `77` | # Runtime state
|
`80` | `78` | self._in_process = False
|
`81` | `79` | self._async_client: httpx.AsyncClient | None = None
|
| `80` | `+` self._api_keys = self._load_api_keys() |
`82` | `81` | self._api_key_index = 0
|
`83` |
| `-` self._api_key_shared_state: dict[str, Any] | None = None |
`84` | `82` |
|
`85` |
| `-` def create_process_shared_state(self, mp_context: Any) -> dict[str, Any] | None: |
`86` |
| `-` """ |
`87` |
| `-` Create a globally coordinated API-key allocator for worker processes. |
| `83` | `+` def _load_api_keys(self) -> tuple[SecretStr, ...]: |
| `84` | `+` """Load and normalize API keys from the configured backend source.""" |
| `85` | `+` if self._args.api_key_file is None: |
| `86` | `+` return self._args.resolved_api_keys |
`88` | `87` |
|
`89` |
| `-` :param mp_context: Multiprocessing context used to spawn worker processes |
`90` |
| `-` :return: Shared lock and counter when multiple API keys are configured |
`91` |
| `-` """ |
`92` |
| `-` if len(self._args.resolved_api_keys) < MIN_API_KEYS_FOR_ROTATION: |
`93` |
| `-` return None |
`94` |
| `-` return { |
`95` |
| `-` "counter": mp_context.Value("Q", 0), |
`96` |
| `-` "lock": mp_context.Lock(), |
`97` |
| `-` } |
| `88` | `+` try: |
| `89` | `+` api_keys = tuple( |
| `90` | `+` SecretStr(line.strip()) |
| `91` | `+` for line in self._args.api_key_file.read_text( |
| `92` | `+` encoding="utf-8" |
| `93` | `+` ).splitlines() |
| `94` | `+` if line.strip() |
| `95` | `+` ) |
| `96` | `+` except (OSError, UnicodeDecodeError) as exc: |
| `97` | `+` raise ValueError( |
| `98` | `+` f"Unable to read api_key_file '{self._args.api_key_file}'." |
| `99` | `+` ) from exc |
`98` | `100` |
|
`99` |
| `-` def attach_process_shared_state(self, state: Any) -> None: |
| `101` | `+` if not api_keys: |
| `102` | `+` raise ValueError("api_key_file must contain at least one non-empty key.") |
| `103` | `+` return api_keys |
| `104` | `+` |
| `105` | `+` def set_worker_index(self, worker_index: int) -> None: |
`100` | `106` | """
|
`101` |
| `-` Attach the API-key allocator shared by all worker-process copies. |
| `107` | `+` Set this worker's initial offset into the API-key rotation. |
`102` | `108` |
|
`103` |
| `-` :param state: Shared state created by :meth:`create_process_shared_state` |
| `109` | `+` :param worker_index: Zero-based index assigned to this worker process |
`104` | `110` | """
|
`105` |
| `-` if state is not None and not isinstance(state, dict): |
`106` |
| `-` raise TypeError("OpenAI HTTP backend shared state must be a dictionary.") |
`107` |
| `-` self._api_key_shared_state = state |
| `111` | `+` if api_keys := self._api_keys: |
| `112` | `+` self._api_key_index = worker_index % len(api_keys) |
`108` | `113` |
|
`109` | `114` | async def process_startup(self):
|
`110` | `115` | """
|
@@ -475,20 +480,12 @@ def _select_api_key(self, rotate: bool) -> SecretStr | None:
|
`475` | `480` | :param rotate: Whether to allocate the next key for a generation request
|
`476` | `481` | :return: Selected SecretStr API key, or None when authentication is disabled
|
`477` | `482` | """
|
`478` |
| `-` api_keys = self._args.resolved_api_keys |
| `483` | `+` api_keys = self._api_keys |
`479` | `484` | if not api_keys:
|
`480` | `485` | return None
|
`481` | `486` | if not rotate or len(api_keys) == 1:
|
`482` | `487` | return api_keys[0]
|
`483` | `488` |
|
`484` |
| `-` if self._api_key_shared_state is not None: |
`485` |
| `-` lock = self._api_key_shared_state["lock"] |
`486` |
| `-` counter = self._api_key_shared_state["counter"] |
`487` |
| `-` with lock: |
`488` |
| `-` api_key = api_keys[counter.value % len(api_keys)] |
`489` |
| `-` counter.value += 1 |
`490` |
| `-` return api_key |
`491` |
| `-` |
`492` | `489` | api_key = api_keys[self._api_key_index % len(api_keys)]
|
`493` | `490` | self._api_key_index += 1
|
`494` | `491` | return api_key
|
|
## 0 commit comments