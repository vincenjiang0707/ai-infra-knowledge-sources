source: https://github.com/vllm-project/guidellm/pull/1172/files/82cdb1230afbb7a95dea2d2cb19fd319b1f7e717

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)

# fix: preserve resize dimensions for image URLs #1172

## New issue

**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

By clicking “Sign up for GitHub”, you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We’ll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm%2Fissues%2Fnew%2Fchoose)
to your account

Open

[git-jxj](https://github.com/git-jxj)wants to merge 3 commits into

[vllm-project:main](https://github.com/vllm-project/guidellm/tree/main)

##
*base:*
main

Could not load branches

Branch not found:

**{{ refName }}**
Loading

Could not load tags

Nothing to show

Loading

### Are you sure you want to change the base?

Some commits from the old base branch may be removed from the timeline,
and old review comments may become outdated.

[git-jxj:git-jxj/fix-url-image-resize](https://github.com/git-jxj/guidellm/tree/git-jxj/fix-url-image-resize)

+63
−21

Open

##
Changes from **1 commit**

Commits

[
](https://github.com/vllm-project/guidellm/pull/1172/files)

Show all changes

3 commits
Select commit
Hold shift + click to select a range

##
**
File filter
**

### Filter by extension

## **Conversations**

Failed to load comments.

Loading

## **Jump to**

Jump to file

Failed to load files.

Loading

##### Diff view

##### Diff view


Some comments aren't visible on the classic Files Changed page.

## There are no files selected for viewing

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)
This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| Original file line number | Diff line number | Diff line change |
|---|---|---|
| @@ -0,0 +1,40 @@ | ||
| import base64 | ||
| import io | ||
| from unittest.mock import patch | ||
|
|
||
| import httpx | ||
| import pytest | ||
| from PIL import Image | ||
|
|
||
| from guidellm.utils.vision import encode_image | ||
|
|
||
|
|
||
| @pytest.mark.regression | ||
| @pytest.mark.parametrize( | ||
| ("resize_kwargs", "expected_size"), | ||
| [ | ||
| ({"width": 40}, (40, 20)), | ||
| ({"height": 30}, (60, 30)), | ||
| ({"width": 40, "height": 30}, (40, 30)), | ||
| ({"width": 160, "max_height": 20}, (40, 20)), | ||
| ({"max_size": 40}, (40, 20)), | ||
| ], | ||
| ) | ||
| def test_encode_image_url_preserves_resize_options(resize_kwargs, expected_size): | ||
| """Downloaded images honor the same resize options as bytes. ## WRITTEN BY AI ##""" | ||
| image_buffer = io.BytesIO() | ||
| Image.new("RGB", (80, 40), color="red").save(image_buffer, format="PNG") | ||
| image_bytes = image_buffer.getvalue() | ||
| url = "https://example.com/image.png" | ||
| response = httpx.Response( | ||
| 200, content=image_bytes, request=httpx.Request("GET", url) | ||
| ) | ||
|
|
||
| with patch("guidellm.utils.vision.httpx.get", return_value=response): | ||
| result = encode_image(url, **resize_kwargs) | ||
| local_result = encode_image(image_bytes, **resize_kwargs) | ||
|
|
||
| decoded = Image.open(io.BytesIO(base64.b64decode(result["image"].split(",", 1)[1]))) | ||
| assert decoded.size == expected_size | ||
| assert result["image_pixels"] == expected_size[0] * expected_size[1] | ||
| assert result == local_result |

Oops, something went wrong.

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.

dbutenhofmarked this conversation as resolved.## Uh oh!

There was an error while loading. Please reload this page.