source: https://github.com/vllm-project/guidellm/commit/a29f5eb77f6b2db57baa45e3099b653fd0ddc9d5

@@ -38,28 +38,26 @@ def encode_image(


`38`

`38`

max_height : int | None = None ,


`39`

`39`

encode_type : Literal ["base64" , "url" ] | None = "base64" ,


`40`

`40`

) -> dict [Literal ["type" , "image" , "image_pixels" , "image_bytes" ], str | int | None ]:


`41`


- """


`42`


- Input image types:


`43`


- - bytes: raw image bytes, decoded with Pillow


`44`


- - str: file path on disk, url, or already base64 encoded image string


`45`


- - pathlib.Path: file path on disk


`46`


- - np.ndarray: image array, decoded with Pillow


`47`


- - PIL.Image.Image: Pillow image


`48`


- - datasets.Image: HuggingFace datasets Image object


`49`


-


`50`


- width and height: resize dimensions, including downloaded URL images


`51`


- max_size: maximum size of the longest edge of the image


`52`


- max_width: maximum width of the image


`53`


- max_height: maximum height of the image


`54`


-


`55`


- encode_type: None to return the supported format


`56`


- (url for url, base64 string for others)


`57`


- "base64" to return base64 encoded string (or download URL and encode)


`58`


- "url" to return url (only if input is url, otherwise fails)


`59`


-


`60`


- Returns a str of either:


`61`


- - image url


`62`


- - "data:image/{type};base64, {data}" string



`41`

+ """Encode an image as a URL or base64 data URI.



`42`

+



`43`

+ Supported inputs include raw bytes, a file path, a URL, a base64 data URI,



`44`

+ a NumPy array, a Pillow image, and a Hugging Face ``datasets.Image``.



`45`

+



`46`

+ :param image: Image input to encode.



`47`

+ :param width: Requested output width in pixels. Applies to downloaded URL



`48`

+ images when ``encode_type`` is ``"base64"``.



`49`

+ :param height: Requested output height in pixels. Applies to downloaded URL



`50`

+ images when ``encode_type`` is ``"base64"``.



`51`

+ :param max_size: Maximum length in pixels of the longest image edge.



`52`

+ :param max_width: Maximum output width in pixels.



`53`

+ :param max_height: Maximum output height in pixels.



`54`

+ :param encode_type: Output representation. ``"base64"`` encodes the image,



`55`

+ ``"url"`` returns the URL unchanged, and ``None`` selects a supported



`56`

+ representation for the input.



`57`

+ :return: A mapping with the image representation type, encoded image, and



`58`

+ optional pixel and byte counts.



`59`

+ :raises ValueError: If the input type is unsupported or resize dimensions



`60`

+ are requested while returning a URL.


`63`

`61`

"""


`64`

`62`

if isinstance (image , str ) and is_url (image ):


`65`

`63`

if encode_type == "base64" :


## 0 commit comments