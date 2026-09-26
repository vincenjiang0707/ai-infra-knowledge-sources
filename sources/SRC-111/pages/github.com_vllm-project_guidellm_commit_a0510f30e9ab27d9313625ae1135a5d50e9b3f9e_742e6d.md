source: https://github.com/vllm-project/guidellm/commit/a0510f30e9ab27d9313625ae1135a5d50e9b3f9e

|
| `1` | `+`"""Programmatic API for multi-image benchmarking.""" |
| `2` | `+` |
| `3` | `+`from __future__ import annotations |
| `4` | `+` |
| `5` | `+`from dataclasses import dataclass |
| `6` | `+`from typing import Any |
| `7` | `+` |
| `8` | `+`from guidellm.data.deserializers.multi_image import MultiImageDataArgs as MultiImageDatasetConfig |
| `9` | `+`from guidellm.data.generators.multi_image import generate_synthetic_images |
| `10` | `+` |
| `11` | `+`__all__ = ["MultiImageBenchmark", "MultiImageBenchmarkResults"] |
| `12` | `+` |
| `13` | `+` |
| `14` | `+`@dataclass |
| `15` | `+`class MultiImageBenchmarkResults: |
| `16` | `+` """Results from multi-image benchmark comparing multiple frame counts.""" |
| `17` | `+` |
| `18` | `+` results: dict[int, Any] # {image_count: benchmark_result} |
| `19` | `+` |
| `20` | `+` def ttft_by_count(self) -> dict[int, float]: |
| `21` | `+` """Return mean TTFT (ms) for each image count.""" |
| `22` | `+` ttft = {} |
| `23` | `+` for img_count, result in self.results.items(): |
| `24` | `+` if hasattr(result, "requests") and result.requests and hasattr(result.requests, "stats"): |
| `25` | `+` if hasattr(result.requests.stats, "ttft_ms"): |
| `26` | `+` ttft[img_count] = result.requests.stats.ttft_ms.mean |
| `27` | `+` return ttft |
| `28` | `+` |
| `29` | `+` def itl_by_count(self) -> dict[int, float]: |
| `30` | `+` """Return mean ITL (ms) for each image count.""" |
| `31` | `+` itl = {} |
| `32` | `+` for img_count, result in self.results.items(): |
| `33` | `+` if hasattr(result, "requests") and result.requests and hasattr(result.requests, "stats"): |
| `34` | `+` if hasattr(result.requests.stats, "itl_ms"): |
| `35` | `+` itl[img_count] = result.requests.stats.itl_ms.mean |
| `36` | `+` return itl |
| `37` | `+` |
| `38` | `+` |
| `39` | `+`class MultiImageBenchmark: |
| `40` | `+` """ |
| `41` | `+` Benchmark latency impact of multiple images per request. |
| `42` | `+`
|
| `43` | `+` Example: |
| `44` | `+` bench = MultiImageBenchmark( |
| `45` | `+` image_counts=[1, 2, 5], |
| `46` | `+` prompt_tokens=256, |
| `47` | `+` output_tokens=128, |
| `48` | `+` ) |
| `49` | `+` config_dict = bench.get_configs() |
| `50` | `+` # Use configs with benchmark runner |
| `51` | `+` """ |
| `52` | `+` |
| `53` | `+` def __init__( |
| `54` | `+` self, |
| `55` | `+` image_counts: list[int], |
| `56` | `+` prompt_tokens: int = 256, |
| `57` | `+` output_tokens: int = 128, |
| `58` | `+` image_size: str = "720p", |
| `59` | `+` random_seed: int | None = None, |
| `60` | `+` **kwargs: Any, |
| `61` | `+` ): |
| `62` | `+` """ |
| `63` | `+` Initialize multi-image benchmark configuration. |
| `64` | `+`
|
| `65` | `+` Args: |
| `66` | `+` image_counts: List of image counts to benchmark (e.g., [1, 2, 5]) |
| `67` | `+` prompt_tokens: Average prompt token count |
| `68` | `+` output_tokens: Average output token count |
| `69` | `+` image_size: Image resolution ("720p") |
| `70` | `+` random_seed: Random seed for reproducible image generation |
| `71` | `+` **kwargs: Additional arguments for MultiImageDatasetConfig |
| `72` | `+` """ |
| `73` | `+` self.image_counts = sorted(image_counts) |
| `74` | `+` self.prompt_tokens = prompt_tokens |
| `75` | `+` self.output_tokens = output_tokens |
| `76` | `+` self.image_size = image_size |
| `77` | `+` self.random_seed = random_seed |
| `78` | `+` self.kwargs = kwargs |
| `79` | `+` |
| `80` | `+` def get_configs(self) -> dict[int, MultiImageDatasetConfig]: |
| `81` | `+` """ |
| `82` | `+` Get MultiImageDatasetConfig for each image count. |
| `83` | `+`
|
| `84` | `+` Returns: |
| `85` | `+` Dict mapping image_count to MultiImageDatasetConfig |
| `86` | `+` """ |
| `87` | `+` configs = {} |
| `88` | `+` for img_count in self.image_counts: |
| `89` | `+` configs[img_count] = MultiImageDatasetConfig( |
| `90` | `+` prompt_tokens=self.prompt_tokens, |
| `91` | `+` output_tokens=self.output_tokens, |
| `92` | `+` images_per_request=img_count, |
| `93` | `+` image_size=self.image_size, |
| `94` | `+` **self.kwargs, |
| `95` | `+` ) |
| `96` | `+` return configs |
| `97` | `+` |
| `98` | `+` def generate_images(self, img_count: int) -> tuple[list[dict], int, int]: |
| `99` | `+` """ |
| `100` | `+` Generate synthetic images for a given count. |
| `101` | `+`
|
| `102` | `+` Args: |
| `103` | `+` img_count: Number of images to generate |
| `104` | `+`
|
| `105` | `+` Returns: |
| `106` | `+` Tuple of (images_list, total_pixels, total_bytes) |
| `107` | `+` """ |
| `108` | `+` return generate_synthetic_images( |
| `109` | `+` num_images=img_count, |
| `110` | `+` image_size=self.image_size, |
| `111` | `+` seed=self.random_seed, |
| `112` | `+` ) |
| `113` | `+` |
| `114` | `+` def get_image_stats(self, img_count: int) -> dict[str, int]: |
| `115` | `+` """ |
| `116` | `+` Get image statistics (pixels, bytes) for a given count. |
| `117` | `+`
|
| `118` | `+` Args: |
| `119` | `+` img_count: Number of images |
| `120` | `+`
|
| `121` | `+` Returns: |
| `122` | `+` Dict with 'total_pixels' and 'total_bytes' |
| `123` | `+` """ |
| `124` | `+` _, total_pixels, total_bytes = self.generate_images(img_count) |
| `125` | `+` return { |
| `126` | `+` "image_count": img_count, |
| `127` | `+` "total_pixels": total_pixels, |
| `128` | `+` "total_bytes": total_bytes, |
| `129` | `+` "pixels_per_image": (total_pixels // img_count) if img_count > 0 else 0, |
| `130` | `+` "bytes_per_image": (total_bytes // img_count) if img_count > 0 else 0, |
| `131` | `+` } |
## 0 commit comments