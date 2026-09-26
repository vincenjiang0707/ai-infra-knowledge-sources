source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/common/mm_preprocess/
lastmod: 2026-09-24

class MiniMaxM3VLProcessingInfo(BaseProcessingInfo):
IMAGE_TOKEN = "]<]image[>["
VIDEO_TOKEN = "]<]video[>["
VISION_START_TOKEN = "]<]start of image[>["
VISION_END_TOKEN = "]<]end of image[>["
def get_hf_config(self) -> MiniMaxM3Config:
return self.ctx.get_hf_config(MiniMaxM3Config)
def get_hf_processor(self, **kwargs: object) -> MiniMaxVLProcessor:
# The released checkpoint only ships the processor as remote code
# (via ``auto_map``). Construct the vendored processor directly so the
# model loads without ``--trust-remote-code``.
return self.ctx.get_hf_processor(MiniMaxVLProcessor, **kwargs)
def get_supported_mm_limits(self) -> Mapping[str, int | None]:
return {"image": None, "video": None}
def get_mm_max_tokens_per_item(
self,
seq_len: int,
mm_counts: Mapping[str, int],
) -> Mapping[str, int]:
return {
"image": self.get_max_image_tokens(),
"video": self.get_max_video_tokens(seq_len, mm_counts),
}
def get_image_processor(self, **kwargs: object) -> MiniMaxM3VLImageProcessor:
return self.get_hf_processor(**kwargs).image_processor
def get_video_processor(self, **kwargs: object) -> MiniMaxM3VLVideoProcessor:
return self.get_hf_processor(**kwargs).video_processor
def _get_vision_info(
self,
*,
image_width: int,
image_height: int,
num_frames: int,
image_processor,
) -> tuple[ImageSize, int]:
"""Compute resized image size and number of vision tokens.
Mirrors the processor's Qwen-style ``smart_resize`` (area bound by
``max_pixels``) so token counts match the actual processor output.
"""
patch_size: int = image_processor.patch_size
merge_size: int = image_processor.merge_size
temporal_patch_size: int = image_processor.temporal_patch_size
factor = patch_size * merge_size
max_pixels: int = image_processor.max_pixels
# Long-side resize spec (opt-in). ``image_processor`` is the *video*
# processor when counting video tokens, so read the bounds off it.
max_long_side_pixel = getattr(image_processor, "max_long_side_pixel", None)
min_short_side_pixel = getattr(
image_processor, "min_short_side_pixel", MIN_SHORT_SIDE_PIXEL
)
new_h, new_w = smart_resize(
image_height,
image_width,
factor=factor,
max_pixels=max_pixels,
max_long_side_pixel=max_long_side_pixel,
min_short_side_pixel=min_short_side_pixel,
# Token counting must not raise; the volumetric/area cap is enforced
# in the processor's _preprocess on the real inputs.
max_total_pixels=None,
)
grid_h = new_h // patch_size
grid_w = new_w // patch_size
# Pad frames to be divisible by temporal_patch_size
padded_frames = num_frames + (-num_frames % temporal_patch_size)
grid_t = max(padded_frames // temporal_patch_size, 1)
num_tokens = grid_t * grid_h * grid_w // (merge_size**2)
return ImageSize(width=new_w, height=new_h), num_tokens
def get_num_image_tokens(
self,
*,
image_width: int,
image_height: int,
image_processor,
mm_kwargs: Mapping[str, object],
) -> int:
_, n = self._get_vision_info(
image_width=image_width,
image_height=image_height,
num_frames=1,
image_processor=image_processor,
)
return n
def get_num_video_tokens(
self,
*,
image_width: int,
image_height: int,
num_frames: int,
image_processor,
mm_kwargs: Mapping[str, object],
) -> int:
_, n = self._get_vision_info(
image_width=image_width,
image_height=image_height,
num_frames=num_frames,
image_processor=image_processor,
)
return n
def get_image_size_with_most_features(self) -> ImageSize:
# Largest square (a multiple of patch_size*merge_size) whose area is
# within the image processor's bound — this yields the most vision
# tokens for one image. With the long-side spec the square side is
# capped by ``max_long_side_pixel`` (and the fixed ``max_total_pixels``);
# otherwise it is bound by the ``max_pixels`` area.
image_processor = self.get_image_processor()
factor = image_processor.patch_size * image_processor.merge_size
max_long_side_pixel = getattr(image_processor, "max_long_side_pixel", None)
if max_long_side_pixel is not None:
side_px = min(
max_long_side_pixel,
math.isqrt(image_processor.max_total_pixels),
)
else:
side_px = math.isqrt(image_processor.max_pixels)
side = max(factor, (side_px // factor) * factor)
return ImageSize(width=side, height=side)
def get_video_size_with_most_features(self) -> ImageSize:
# Per-frame size that yields the most vision tokens, bound by the
# *video* processor's ``max_pixels`` (which differs from the image
# bound). Token count depends only on area, so maximize the area
# achievable with both sides a multiple of patch_size*merge_size rather
# than picking the largest square — a square (e.g. 756x756 for M3's
# 602,112 bound) leaves area on the table, undercounting frames.
video_processor = self.get_video_processor()
factor = video_processor.patch_size * video_processor.merge_size
per_frame_pixels = video_processor.max_pixels
max_long_side_pixel = getattr(video_processor, "max_long_side_pixel", None)
if max_long_side_pixel is not None:
# Long-side spec: a frame's worst case is a square capped by
# ``max_long_side_pixel`` (per-frame area, not the volumetric cap).
per_frame_pixels = min(per_frame_pixels, max_long_side_pixel**2)
units = per_frame_pixels // (factor * factor) # h_u * w_u
h_u = math.isqrt(units)
while units % h_u:
h_u -= 1
return ImageSize(width=(units // h_u) * factor, height=h_u * factor)
def get_max_image_tokens(self) -> int:
image_processor = self.get_image_processor()
size = self.get_image_size_with_most_features()
return self.get_num_image_tokens(
image_width=size.width,
image_height=size.height,
image_processor=image_processor,
mm_kwargs={},
)
def _get_max_video_frames(self, max_tokens: int) -> int:
video_processor = self.get_video_processor()
size = self.get_video_size_with_most_features()
num_frames = 1
while True:
next_n = self.get_num_video_tokens(
image_width=size.width,
image_height=size.height,
num_frames=num_frames + 1,
image_processor=video_processor,
mm_kwargs={},
)
if next_n > max_tokens:
break
num_frames += 1
return num_frames
def get_num_frames_with_most_features(
self,
seq_len: int,
mm_counts: Mapping[str, int],
max_frames_per_video: int = _MAX_FRAMES_PER_VIDEO,
) -> int:
max_videos = mm_counts.get("video", 0)
max_total_frames = self._get_max_video_frames(seq_len)
max_frames_per_video = min(
max_total_frames // max(max_videos, 1), max_frames_per_video
)
return max(max_frames_per_video, 1)
def get_max_video_tokens(
self,
seq_len: int,
mm_counts: Mapping[str, int],
) -> int:
video_processor = self.get_video_processor()
size = self.get_video_size_with_most_features()
return self.get_num_video_tokens(
image_width=size.width,
image_height=size.height,
num_frames=self.get_num_frames_with_most_features(seq_len, mm_counts),
image_processor=video_processor,
mm_kwargs={},
)