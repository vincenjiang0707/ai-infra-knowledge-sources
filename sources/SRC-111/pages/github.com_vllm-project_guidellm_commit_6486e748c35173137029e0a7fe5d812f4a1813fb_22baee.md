source: https://github.com/vllm-project/guidellm/commit/6486e748c35173137029e0a7fe5d812f4a1813fb

|
| `1` | `+`import base64 |
| `2` | `+`import io |
| `3` | `+`from unittest.mock import patch |
| `4` | `+` |
| `5` | `+`import httpx |
| `6` | `+`import pytest |
| `7` | `+`from PIL import Image |
| `8` | `+` |
| `9` | `+`from guidellm.utils.vision import encode_image |
| `10` | `+` |
| `11` | `+` |
| `12` | `+`@pytest.mark.regression |
| `13` | `+`@pytest.mark.parametrize( |
| `14` | `+` ("resize_kwargs", "expected_size"), |
| `15` | `+` [ |
| `16` | `+` ({"width": 40}, (40, 20)), |
| `17` | `+` ({"height": 30}, (60, 30)), |
| `18` | `+` ({"width": 40, "height": 30}, (40, 30)), |
| `19` | `+` ({"width": 160, "max_height": 20}, (40, 20)), |
| `20` | `+` ({"max_size": 40}, (40, 20)), |
| `21` | `+` ], |
| `22` | `+`) |
| `23` | `+`def test_encode_image_url_preserves_resize_options(resize_kwargs, expected_size): |
| `24` | `+` """Downloaded images honor the same resize options as bytes. ## WRITTEN BY AI ##""" |
| `25` | `+` image_buffer = io.BytesIO() |
| `26` | `+` Image.new("RGB", (80, 40), color="red").save(image_buffer, format="PNG") |
| `27` | `+` image_bytes = image_buffer.getvalue() |
| `28` | `+` url = "https://example.com/image.png" |
| `29` | `+` response = httpx.Response( |
| `30` | `+` 200, content=image_bytes, request=httpx.Request("GET", url) |
| `31` | `+` ) |
| `32` | `+` |
| `33` | `+` with patch("guidellm.utils.vision.httpx.get", return_value=response): |
| `34` | `+` result = encode_image(url, **resize_kwargs) |
| `35` | `+` local_result = encode_image(image_bytes, **resize_kwargs) |
| `36` | `+` |
| `37` | `+` decoded = Image.open(io.BytesIO(base64.b64decode(result["image"].split(",", 1)[1]))) |
| `38` | `+` assert decoded.size == expected_size |
| `39` | `+` assert result["image_pixels"] == expected_size[0] * expected_size[1] |
| `40` | `+` assert result == local_result |
## 0 commit comments