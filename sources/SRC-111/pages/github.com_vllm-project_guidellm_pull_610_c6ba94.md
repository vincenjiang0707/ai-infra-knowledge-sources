source: https://github.com/vllm-project/guidellm/pull/610

# Add support for TerraTorch Geospatial models served via the vLLM /pooling endpoint - #610

## Conversation


[dbutenhof](https://github.com/dbutenhof)changed the title

Feb 27, 2026

[mgazz](https://github.com/mgazz)marked this pull request as ready for review

March 11, 2026 10:02

|
This pull request has merge conflicts that must be resolved before it can be |

|
Please wait before merging. After the rebase we can benchmark the Prithvi model but Terramind returns a server error. I am currently investigating the reason behind it. |

|
|


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 20, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

This looks fairly straightforward (even if the entire concept of geospatial inference is more than slightly mysterious to me).

I made a minor comment on your documentation, which might help readers to follow the sequence... but I think that's a minor issue and I'm approving anyway. (Not that it really matters as you need a rebase now.)

FYI, the unit test failure is a known issue, and will be resolved when you rebase.

[docs/guides/geospatial.md](https://github.com/vllm-project/guidellm/pull/610/files#diff-8b329bf00b68df2a2fd17197b278b7b9ea27d18014bb18913067b253833e86ef)Outdated

|
|

## ✅ Branch has been successfully rebased |


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 25, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I don't see anything blocking, but I do have a comment on a design decision. I'm not the most familiar with geospacial models, but I was able to confirm that it ran.

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/610/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 25, 2026

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/610/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/610/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Mar 26, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

The documentation now gives `--request-format`

values that won't work since you removed the "legacy" alias.

[docs/guides/geospatial.md](https://github.com/vllm-project/guidellm/pull/610/files#diff-8b329bf00b68df2a2fd17197b278b7b9ea27d18014bb18913067b253833e86ef)Outdated

[docs/guides/geospatial.md](https://github.com/vllm-project/guidellm/pull/610/files#diff-8b329bf00b68df2a2fd17197b278b7b9ea27d18014bb18913067b253833e86ef)Outdated

[docs/guides/geospatial.md](https://github.com/vllm-project/guidellm/pull/610/files#diff-8b329bf00b68df2a2fd17197b278b7b9ea27d18014bb18913067b253833e86ef)Outdated

|
Sorry for the delay and thank you for the feedback. I will update the documentation to make it coherent. I will also provide a command to build the |

|
This pull request has merge conflicts that must be resolved before it can be |

|
You can do this by running: |

|
|

…ling endpoint Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: mgazz <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

Signed-off-by: Michele Gazzetti <michele.gazzetti1@ibm.com>

## ✅ Branch has been successfully rebased |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 27, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 27, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This PR adds support for TerraTorch Geospatial models like Prithvi. Compared to traditional LLMs, Geospatial Models support image-to-image or tensor-to-tensor input/output, but they do not process text. Moreover they are served in vLLM at the /pooling endpoint.

## Details

`prompt`

entry in datasets without creating conflict with the existing GenerativeColumnMapper## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)