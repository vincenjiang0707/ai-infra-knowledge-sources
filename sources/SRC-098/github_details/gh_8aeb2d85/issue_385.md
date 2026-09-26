# [Issue #385] Suggestion to adjust license wording for consistency with standard BSD-style phrasing

source: https://github.com/NVIDIA/nccl-tests/issues/385
state: open | updated: 2026-06-02T16:53:31Z
labels: 

## 正文

Hello NVIDIA team,

I was reviewing the LICENSE file for nccl-tests and noticed a slight deviation in the wording regarding endorsement:

The current wording in LICENSE.txt is:

> Neither the name of NVIDIA CORPORATION, nor the names of their contributors may be used to endorse or promote products derived from this software without specific prior written permission.

Reference:
https://github.com/NVIDIA/nccl-tests/blob/master/LICENSE.txt#L12-L14

Standard BSD-style wording:
`Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.`

The current phrasing explicitly mentions “NVIDIA CORPORATION,” whereas the standard formulation refers to “the copyright holder.” Using the standard wording could help align the license with common BSD-style licenses and avoid potential ambiguity in interpretation.

Thank you for considering this suggestion.

## 评论 (1)

### AddyLaddy · 2026-06-02

Thanks for your report.
SPDX explicitly recognizes equivalent BSD-3-Clause variations in the third clause: [SPDX BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

> Note for matching purposes, this license contains a number of equivalent variations, particularly in the third clause. See the XML file for more details.

So I don't believe it necessary to change the current LICENSE.txt in nccl-tests in order to meet the SPDX rules.

We may review this later if our Legal team want to carry out a more conistent change across all Nvidia Open-Source products.
