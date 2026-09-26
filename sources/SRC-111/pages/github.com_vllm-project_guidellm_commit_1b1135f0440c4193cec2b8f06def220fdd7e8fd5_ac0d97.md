source: https://github.com/vllm-project/guidellm/commit/1b1135f0440c4193cec2b8f06def220fdd7e8fd5

|
| `1` | `+`""" |
| `2` | `+`LiteLLM backend implementation for GuideLLM. |
| `3` | `+`
|
| `4` | `+`Provides SDK-based backend for LiteLLM, enabling benchmarking across 100+ |
| `5` | `+`providers (Anthropic, Gemini, Bedrock, Groq, Cohere, Mistral, and more) via |
| `6` | `+`a unified interface. Supports streaming, token usage tracking, and timing |
| `7` | `+`measurements compatible with GuideLLM's benchmark pipeline. |
| `8` | `+`
|
| `9` | `+`Install the optional dependency to use this backend: |
| `10` | `+` pip install "guidellm[litellm]" |
| `11` | `+`""" |
| `12` | `+` |
| `13` | `+`from __future__ import annotations |
| `14` | `+` |
| `15` | `+`import asyncio |
| `16` | `+`import time |
| `17` | `+`from collections.abc import AsyncIterator |
| `18` | `+`from typing import Any, Literal |
| `19` | `+` |
| `20` | `+`from pydantic import Field, SecretStr |
| `21` | `+` |
| `22` | `+`import guidellm.extras.litellm as _litellm |
| `23` | `+`from guidellm.backends.backend import Backend, BackendArgs |
| `24` | `+`from guidellm.backends.openai.request_handlers import ( |
| `25` | `+` ChatCompletionsRequestHandler, |
| `26` | `+`) |
| `27` | `+`from guidellm.schemas import ( |
| `28` | `+` GenerationRequest, |
| `29` | `+` GenerationResponse, |
| `30` | `+` RequestInfo, |
| `31` | `+`) |
| `32` | `+`from guidellm.schemas.request import UsageMetrics |
| `33` | `+` |
| `34` | `+`__all__ = [ |
| `35` | `+` "LiteLLMBackend", |
| `36` | `+` "LiteLLMBackendArgs", |
| `37` | `+`] |
| `38` | `+` |
| `39` | `+` |
| `40` | `+`@BackendArgs.register("litellm") |
| `41` | `+`class LiteLLMBackendArgs(BackendArgs): |
| `42` | `+` """Pydantic model for LiteLLM backend creation arguments.""" |
| `43` | `+` |
| `44` | `+` kind: Literal["litellm"] = Field( |
| `45` | `+` default="litellm", |
| `46` | `+` description="Type identifier for the LiteLLM backend configuration.", |
| `47` | `+` ) |
| `48` | `+` model: str = Field( |
| `49` | `+` description=( |
| `50` | `+` "Model identifier in LiteLLM format, e.g. " |
| `51` | `+` "'anthropic/claude-haiku-4-5', 'gemini/gemini-1.5-flash', " |
| `52` | `+` "'bedrock/anthropic.claude-3-sonnet-20240229-v1:0', 'gpt-4o'." |
| `53` | `+` ), |
| `54` | `+` ) |
| `55` | `+` api_key: SecretStr | None = Field( |
| `56` | `+` default=None, |
| `57` | `+` description=( |
| `58` | `+` "API key for the provider (overrides provider env var)." |
| `59` | `+` ), |
| `60` | `+` ) |
| `61` | `+` api_base: str | None = Field( |
| `62` | `+` default=None, |
| `63` | `+` description="Custom base URL, e.g. a LiteLLM proxy URL.", |
| `64` | `+` ) |
| `65` | `+` max_tokens: int | None = Field( |
| `66` | `+` default=None, |
| `67` | `+` description="Maximum number of tokens to generate per request.", |
| `68` | `+` ) |
| `69` | `+` extras: dict[str, Any] | None = Field( |
| `70` | `+` default=None, |
| `71` | `+` description=( |
| `72` | `+` "Additional keyword arguments forwarded to " |
| `73` | `+` "litellm.acompletion()." |
| `74` | `+` ), |
| `75` | `+` ) |
| `76` | `+` |
| `77` | `+` |
| `78` | `+`@Backend.register("litellm") |
| `79` | `+`class LiteLLMBackend(Backend): |
| `80` | `+` """ |
| `81` | `+` LiteLLM SDK backend for GuideLLM. |
| `82` | `+`
|
| `83` | `+` Routes generation requests through the LiteLLM SDK, enabling load-testing |
| `84` | `+` and benchmarking across any provider supported by LiteLLM. |
| `85` | `+`
|
| `86` | `+` Example: |
| `87` | `+` :: |
| `88` | `+` args = LiteLLMBackendArgs( |
| `89` | `+` model="anthropic/claude-haiku-4-5", |
| `90` | `+` api_key="sk-ant-...", |
| `91` | `+` ) |
| `92` | `+` backend = LiteLLMBackend(args) |
| `93` | `+` await backend.process_startup() |
| `94` | `+` async for response, info in backend.resolve(request, info): |
| `95` | `+` process(response) |
| `96` | `+` await backend.process_shutdown() |
| `97` | `+` """ |
| `98` | `+` |
| `99` | `+` def __init__(self, args: LiteLLMBackendArgs): |
| `100` | `+` super().__init__(args) |
| `101` | `+` self._args = args |
| `102` | `+` self._in_process = False |
| `103` | `+` |
| `104` | `+` async def process_startup(self): |
| `105` | `+` """Validate that litellm is importable and model is set.""" |
| `106` | `+` if self._in_process: |
| `107` | `+` raise RuntimeError("Backend already started up for process.") |
| `108` | `+` _ = _litellm.acompletion # noqa: F841 |
| `109` | `+` self._in_process = True |
| `110` | `+` |
| `111` | `+` async def process_shutdown(self): |
| `112` | `+` """Clean up backend resources.""" |
| `113` | `+` if not self._in_process: |
| `114` | `+` raise RuntimeError("Backend not started up for process.") |
| `115` | `+` self._in_process = False |
| `116` | `+` |
| `117` | `+` async def validate(self): |
| `118` | `+` """Validate that model string is non-empty.""" |
| `119` | `+` if not self._args.model: |
| `120` | `+` raise RuntimeError( |
| `121` | `+` "LiteLLM backend requires a non-empty model string." |
| `122` | `+` ) |
| `123` | `+` |
| `124` | `+` async def available_models(self) -> list[str]: |
| `125` | `+` """Return the configured model as the only available model.""" |
| `126` | `+` return [self._args.model] |
| `127` | `+` |
| `128` | `+` async def default_model(self) -> str: |
| `129` | `+` """Return the configured model identifier.""" |
| `130` | `+` return self._args.model |
| `131` | `+` |
| `132` | `+` async def resolve( # type: ignore[override] |
| `133` | `+` self, |
| `134` | `+` request: GenerationRequest, |
| `135` | `+` request_info: RequestInfo, |
| `136` | `+` history: ( |
| `137` | `+` list[tuple[GenerationRequest, GenerationResponse | None]] |
| `138` | `+` | None |
| `139` | `+` ) = None, |
| `140` | `+` ) -> AsyncIterator[tuple[GenerationResponse | None, RequestInfo]]: |
| `141` | `+` """ |
| `142` | `+` Process generation request via litellm.acompletion(). |
| `143` | `+`
|
| `144` | `+` :param request: Generation request with content and parameters |
| `145` | `+` :param request_info: Request tracking info with timing metadata |
| `146` | `+` :param history: Optional conversation history for multi-turn |
| `147` | `+` :yields: Tuples of (response, updated_request_info) |
| `148` | `+` """ |
| `149` | `+` model = self._args.model |
| `150` | `+` messages, request_args_json = self._format_request( |
| `151` | `+` request, history, model, |
| `152` | `+` ) |
| `153` | `+` call_kwargs = self._build_call_kwargs() |
| `154` | `+` |
| `155` | `+` texts: list[str] = [] |
| `156` | `+` response_id: str | None = None |
| `157` | `+` input_tokens: int | None = None |
| `158` | `+` output_tokens: int | None = None |
| `159` | `+` |
| `160` | `+` try: |
| `161` | `+` request_info.timings.request_start = time.time() |
| `162` | `+` |
| `163` | `+` response_stream = await _litellm.acompletion( |
| `164` | `+` model=model, |
| `165` | `+` messages=messages, |
| `166` | `+` stream=True, |
| `167` | `+` **call_kwargs, |
| `168` | `+` ) |
| `169` | `+` |
| `170` | `+` async for chunk in response_stream: |
| `171` | `+` token_info = self._process_chunk( |
| `172` | `+` chunk, request_info, texts, |
| `173` | `+` ) |
| `174` | `+` if token_info.response_id and response_id is None: |
| `175` | `+` response_id = token_info.response_id |
| `176` | `+` if token_info.input_tokens is not None: |
| `177` | `+` input_tokens = token_info.input_tokens |
| `178` | `+` if token_info.output_tokens is not None: |
| `179` | `+` output_tokens = token_info.output_tokens |
| `180` | `+` if token_info.first_token: |
| `181` | `+` yield None, request_info |
| `182` | `+` |
| `183` | `+` request_info.timings.request_end = time.time() |
| `184` | `+` |
| `185` | `+` yield self._build_response( |
| `186` | `+` request, response_id, request_args_json, |
| `187` | `+` texts, input_tokens, output_tokens, |
| `188` | `+` ), request_info |
| `189` | `+` |
| `190` | `+` except asyncio.CancelledError as err: |
| `191` | `+` yield self._build_response( |
| `192` | `+` request, response_id, request_args_json, |
| `193` | `+` texts, input_tokens, output_tokens, |
| `194` | `+` ), request_info |
| `195` | `+` raise err |
| `196` | `+` |
| `197` | `+` def _format_request( |
| `198` | `+` self, |
| `199` | `+` request: GenerationRequest, |
| `200` | `+` history: ( |
| `201` | `+` list[tuple[GenerationRequest, GenerationResponse | None]] |
| `202` | `+` | None |
| `203` | `+` ), |
| `204` | `+` model: str, |
| `205` | `+` ) -> tuple[list[dict[str, Any]], str]: |
| `206` | `+` handler = ChatCompletionsRequestHandler() |
| `207` | `+` arguments = handler.format( |
| `208` | `+` data=request, |
| `209` | `+` history=history, |
| `210` | `+` model=model, |
| `211` | `+` stream=True, |
| `212` | `+` max_tokens=self._args.max_tokens, |
| `213` | `+` ) |
| `214` | `+` messages: list[dict[str, Any]] = ( |
| `215` | `+` arguments.body.get("messages", []) |
| `216` | `+` if arguments.body |
| `217` | `+` else [] |
| `218` | `+` ) |
| `219` | `+` return messages, arguments.model_dump_json() |
| `220` | `+` |
| `221` | `+` def _build_call_kwargs(self) -> dict[str, Any]: |
| `222` | `+` kwargs: dict[str, Any] = { |
| `223` | `+` "drop_params": True, |
| `224` | `+` "stream_options": {"include_usage": True}, |
| `225` | `+` } |
| `226` | `+` if self._args.api_key: |
| `227` | `+` kwargs["api_key"] = self._args.api_key.get_secret_value() |
| `228` | `+` if self._args.api_base: |
| `229` | `+` kwargs["api_base"] = self._args.api_base |
| `230` | `+` if self._args.max_tokens is not None: |
| `231` | `+` kwargs["max_tokens"] = self._args.max_tokens |
| `232` | `+` if self._args.extras: |
| `233` | `+` kwargs.update(self._args.extras) |
| `234` | `+` return kwargs |
| `235` | `+` |
| `236` | `+` def _process_chunk( |
| `237` | `+` self, |
| `238` | `+` chunk: Any, |
| `239` | `+` request_info: RequestInfo, |
| `240` | `+` texts: list[str], |
| `241` | `+` ) -> _ChunkResult: |
| `242` | `+` iter_time = time.time() |
| `243` | `+` |
| `244` | `+` if request_info.timings.first_request_iteration is None: |
| `245` | `+` request_info.timings.first_request_iteration = iter_time |
| `246` | `+` request_info.timings.last_request_iteration = iter_time |
| `247` | `+` request_info.timings.request_iterations += 1 |
| `248` | `+` |
| `249` | `+` response_id = chunk.id if chunk.id else None |
| `250` | `+` |
| `251` | `+` usage = getattr(chunk, "usage", None) |
| `252` | `+` input_tokens = ( |
| `253` | `+` getattr(usage, "prompt_tokens", None) if usage else None |
| `254` | `+` ) |
| `255` | `+` output_tokens = ( |
| `256` | `+` getattr(usage, "completion_tokens", None) if usage else None |
| `257` | `+` ) |
| `258` | `+` |
| `259` | `+` first_token = False |
| `260` | `+` if chunk.choices: |
| `261` | `+` delta = chunk.choices[0].delta |
| `262` | `+` content = delta.content if delta else None |
| `263` | `+` |
| `264` | `+` if content: |
| `265` | `+` texts.append(content) |
| `266` | `+` |
| `267` | `+` if request_info.timings.first_token_iteration is None: |
| `268` | `+` request_info.timings.first_token_iteration = iter_time |
| `269` | `+` request_info.timings.first_output_token_iteration = ( |
| `270` | `+` iter_time |
| `271` | `+` ) |
| `272` | `+` request_info.timings.token_iterations = 0 |
| `273` | `+` first_token = True |
| `274` | `+` |
| `275` | `+` request_info.timings.last_token_iteration = iter_time |
| `276` | `+` request_info.timings.token_iterations += 1 |
| `277` | `+` |
| `278` | `+` return _ChunkResult( |
| `279` | `+` response_id=response_id, |
| `280` | `+` input_tokens=input_tokens, |
| `281` | `+` output_tokens=output_tokens, |
| `282` | `+` first_token=first_token, |
| `283` | `+` ) |
| `284` | `+` |
| `285` | `+` @staticmethod |
| `286` | `+` def _build_response( |
| `287` | `+` request: GenerationRequest, |
| `288` | `+` response_id: str | None, |
| `289` | `+` request_args_json: str, |
| `290` | `+` texts: list[str], |
| `291` | `+` input_tokens: int | None, |
| `292` | `+` output_tokens: int | None, |
| `293` | `+` ) -> GenerationResponse: |
| `294` | `+` return GenerationResponse( |
| `295` | `+` request_id=request.request_id, |
| `296` | `+` response_id=response_id, |
| `297` | `+` request_args=request_args_json, |
| `298` | `+` text="".join(texts) if texts else None, |
| `299` | `+` input_metrics=UsageMetrics(text_tokens=input_tokens), |
| `300` | `+` output_metrics=UsageMetrics(text_tokens=output_tokens), |
| `301` | `+` ) |
| `302` | `+` |
| `303` | `+` |
| `304` | `+`class _ChunkResult: |
| `305` | `+` __slots__ = ( |
| `306` | `+` "first_token", |
| `307` | `+` "input_tokens", |
| `308` | `+` "output_tokens", |
| `309` | `+` "response_id", |
| `310` | `+` ) |
| `311` | `+` |
| `312` | `+` def __init__( |
| `313` | `+` self, |
| `314` | `+` *, |
| `315` | `+` response_id: str | None, |
| `316` | `+` input_tokens: int | None, |
| `317` | `+` output_tokens: int | None, |
| `318` | `+` first_token: bool, |
| `319` | `+` ): |
| `320` | `+` self.response_id = response_id |
| `321` | `+` self.input_tokens = input_tokens |
| `322` | `+` self.output_tokens = output_tokens |
| `323` | `+` self.first_token = first_token |
## 0 commit comments