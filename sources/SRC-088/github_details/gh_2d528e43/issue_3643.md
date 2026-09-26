# [Issue #3643] hendrycks_math: process_results does not extract \boxed{} from model response

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3643
state: open | updated: 2026-07-31T13:46:50Z
labels: 

## 正文

## Bug

In `lm_eval/tasks/hendrycks_math/utils.py`, `process_results` applies `remove_boxed(last_boxed_only_string(...))` to the **target** (ground truth) but never to the **model's response**. When models output answers in `\boxed{}` format (common for instruct models prompted with math reasoning instructions), the extraction falls back to `$...$` matching or uses the entire response, causing `is_equiv` to fail.

The `aime` task (`lm_eval/tasks/aime/utils.py`) already handles this correctly, it tries `last_boxed_only_string` on the response and uses `remove_boxed` on the result.

## Current behavior (hendrycks_math)

```python
def process_results(doc, results):
    # Only $...$ extraction on response — no \boxed{} handling
    indices = [pos for pos, char in enumerate(results[0]) if char == "$"]
    if len(indices) <= 1:
        answer = results[0]  # entire verbose response
    else:
        answer = results[0][indices[0] + 1 : indices[-1]]

    # \boxed{} only applied to TARGET
    if is_equiv(answer, remove_boxed(last_boxed_only_string(doc["solution"]))):
        retval = 1
```

When the model outputs `"The domain is \boxed{[2,5)}"`, the `$` extraction fails (no `$` signs), so `answer` becomes the entire response. `is_equiv("The domain is \\boxed{[2,5)}", "[2,5)")` → 0.

## Expected behavior

Try `\boxed{}` extraction on the response first, fall back to `$...$`:

```python
def process_results(doc, results):
    response = results[0]

    # Try \boxed{} extraction from response first
    boxed = last_boxed_only_string(response)
    if boxed is not None:
        try:
            answer = remove_boxed(boxed)
        except AssertionError:
            answer = None
    else:
        answer = None

    # Fall back to $...$ extraction
    if answer is None:
        indices = [pos for pos, char in enumerate(response) if char == "$"]
        if len(indices) <= 1:
            answer = response
        else:
            answer = response[indices[0] + 1 : indices[-1]]

    if is_equiv(answer, remove_boxed(last_boxed_only_string(doc["solution"]))):
        retval = 1
```

This matches the approach already used in `lm_eval/tasks/aime/utils.py`.

## Impact

This affects `hendrycks_math` and `hendrycks_math500` tasks. Any instruct model that outputs `\boxed{}` answers (which is the standard math format) gets 0% on these tasks despite producing correct answers.

## 评论 (5)

### fxmarty-amd · 2026-03-25

btw @NezLheimeur this does not solve https://github.com/EleutherAI/lm-evaluation-harness/issues/3477

```
{
    "doc_id":127,
    "doc":{
        "problem":"Express $555_{10}$ in base $5$.",
        "solution":"We write $555$ in powers of $5$. The largest power of $5$ which is smaller than $555$ is $5^3=125$, and the greatest multiple of $125$ which is less than $555$ is $4$. We get that $555- 4 \\cdot 125 = 55$. The largest power of $5$ that is less than $55$ is $5^2=25$, and the greatest multiple of $25$ less than $55$ is $2$. We get $55 - 2 \\cdot 25 = 5$, which is $5^1$. Therefore, we can write $555$ as $4 \\cdot 5^3 + 2 \\cdot 5^2 + 1 \\cdot 5^1$. Thus, the answer is $\\boxed{4210_{5}}$.",
        "answer":"4210_{5}",
        "subject":"Number Theory",
        "level":3,
        "unique_id":"test/number_theory/847.json"
    },
    "target":"4210_{5}",
    "arguments":{
        "gen_args_0":{
            "arg_0":"<|im_start|>user\nProblem: Express $555_{10}$ in base $5$.\nAnswer:<|im_end|>\n<|im_start|>assistant\n",
            "arg_1":{
                "until":[
                    
                ],
                "max_gen_toks":10000,
                "top_p":0.95,
                "top_k":20,
                "temperature":0.6
            }
        }
    },
    "resps":[
        [
            "To convert the decimal number $ 555_{10} $ into base $ 5 $, we follow a systematic process of **successive division by 5**, keeping track of the **remainders**. These remainders, read in **reverse order**, give the digits of the number in base 5.\n\n---\n\n### Step-by-Step Conversion\n\nWe divide the number by 5 repeatedly, recording the quotient and remainder at each step:\n\n1. **$ 555 \\div 5 = 111 $** with a **remainder of 0**\n2. **$ 111 \\div 5 = 22 $** with a **remainder of 1**\n3. **$ 22 \\div 5 = 4 $** with a **remainder of 2**\n4. **$ 4 \\div 5 = 0 $** with a **remainder of 4**\n\nAt this point, the quotient becomes 0, and we stop.\n\n---\n\n### Interpreting the Remainders\n\nThe remainders, in the order they were obtained, are:\n- 0 (least significant digit)\n- 1\n- 2\n- 4 (most significant digit)\n\nTo form the base 5 number, we **reverse** the order of the remainders:\n- **4**, **2**, **1**, **0**\n\nThus, the number in base 5 is:\n\n$$\n\\boxed{4210}\n$$\n\n---\n\n### Verification\n\nTo confirm, we can convert $ 4210_5 $ back to decimal:\n\n$$\n4 \\times 5^3 + 2 \\times 5^2 + 1 \\times 5^1 + 0 \\times 5^0 = 4 \\times 125 + 2 \\times 25 + 1 \\times 5 + 0 = 500 + 50 + 5 = 555\n$$\n\nThis matches the original decimal number, verifying that the conversion is correct.\n\n---\n\n### Final Answer\n\n$$\n\\boxed{4210}\n$$"
        ]
    ],
    "filtered_resps":[
        "To convert the decimal number $ 555_{10} $ into base $ 5 $, we follow a systematic process of **successive division by 5**, keeping track of the **remainders**. These remainders, read in **reverse order**, give the digits of the number in base 5.\n\n---\n\n### Step-by-Step Conversion\n\nWe divide the number by 5 repeatedly, recording the quotient and remainder at each step:\n\n1. **$ 555 \\div 5 = 111 $** with a **remainder of 0**\n2. **$ 111 \\div 5 = 22 $** with a **remainder of 1**\n3. **$ 22 \\div 5 = 4 $** with a **remainder of 2**\n4. **$ 4 \\div 5 = 0 $** with a **remainder of 4**\n\nAt this point, the quotient becomes 0, and we stop.\n\n---\n\n### Interpreting the Remainders\n\nThe remainders, in the order they were obtained, are:\n- 0 (least significant digit)\n- 1\n- 2\n- 4 (most significant digit)\n\nTo form the base 5 number, we **reverse** the order of the remainders:\n- **4**, **2**, **1**, **0**\n\nThus, the number in base 5 is:\n\n$$\n\\boxed{4210}\n$$\n\n---\n\n### Verification\n\nTo confirm, we can convert $ 4210_5 $ back to decimal:\n\n$$\n4 \\times 5^3 + 2 \\times 5^2 + 1 \\times 5^1 + 0 \\times 5^0 = 4 \\times 125 + 2 \\times 25 + 1 \\times 5 + 0 = 500 + 50 + 5 = 555\n$$\n\nThis matches the original decimal number, verifying that the conversion is correct.\n\n---\n\n### Final Answer\n\n$$\n\\boxed{4210}\n$$"
    ],
    "filter":"none",
    "metrics":[
        "exact_match"
    ],
    "doc_hash":"3e42bf9651f75d5566bb99e48bedd7fcb782976832c622a60225eb831c8725c1",
    "prompt_hash":"d8a8967de578c10ea03ee0317821c0df4aeff4050af2fa5850814e4bad4febf2",
    "target_hash":"30bf1a573718dbf0d339d6e4549f9faebdcb34c52ee48e3b2d9f78df23d3f840",
    "exact_match":0
}
```

The prompt should instruct to give the answer in a boxed format.

### NezLheimeur · 2026-03-25

@fxmarty-amd Thanks for the review and comment! I'm a bit confused by your example though. It looks like the model output is `\boxed{4210}` while the target is `4210_{5}`. So the extraction works correctly (we get 4210 from the box), but the model itself gave an incomplete answer by dropping the _{5} subscript. Unless I'm missing something, this seems like the model got it wrong rather than an extraction issue? 

In any case, the answering prompt conditioning can indeed be addressed via the `system_instruction` arg in `simple_evaluate()`, where users can prompt the model to format answers properly according to the tested model and the task. For example, Qwen's [best practices](https://huggingface.co/Qwen/Qwen3-0.6B#best-practices) recommend: "_Please reason step by step, and put your final answer within \boxed{}._" as a system prompt for math related benchmarks. But this depends on the model and the task so it's kind of complicated to fix for all the cases right? and even that wouldn't guarantee the model includes the base subscript (as in your example above), if the model answering is inherently wrong. 

### fxmarty-amd · 2026-03-26

@NezLheimeur apologies, I shared the wrong log!

I meant to share this case where the correct answer `**Answer:** 4.` is rated as wrong.

```json
{
    "doc_id":374,
    "doc":{
        "problem":"What is the difference between the positive square root of 64 and the cube root of 64?",
        "solution":"The positive square root of 64 is $\\sqrt{64}=8$. The cube root of 64 is $\\sqrt[3]{64}=4$. The difference is $8-4=\\boxed{4}$.",
        "answer":"4",
        "subject":"Algebra",
        "level":1,
        "unique_id":"test/algebra/1303.json"
    },
    "target":"4",
    "arguments":{
        "gen_args_0":{
            "arg_0":"<|im_start|>system\nHere is a math question, let's think succinctly step by step and answer the question.\n<|im_end|>\n<|im_start|>user\nProblem: What is the difference between the positive square root of 64 and the cube root of 64?\n<|im_end|>\n<|im_start|>assistant\n",
            "arg_1":{
                "until":[
                    
                ],
                "max_gen_toks":10000,
                "top_p":0.95,
                "top_k":20,
                "temperature":0.6
            }
        }
    },
    "resps":[
        [
            "The positive square root of 64 is $ \\sqrt{64} = 8 $, and the cube root of 64 is $ \\sqrt[3]{64} = 4 $. The difference between them is $ 8 - 4 = 4 $.\n\n**Answer:** 4."
        ]
    ],
    "filtered_resps":[
        "The positive square root of 64 is $ \\sqrt{64} = 8 $, and the cube root of 64 is $ \\sqrt[3]{64} = 4 $. The difference between them is $ 8 - 4 = 4 $.\n\n**Answer:** 4."
    ],
    "filter":"none",
    "metrics":[
        "exact_match"
    ],
    "doc_hash":"a821ecb767feaee9da7e560a9a98c946f28112f79468ac52f75f923dfb8630c1",
    "prompt_hash":"cc9d647e4a3235c7d8aaa32a3e8a81589d24a5e44ba8a88a2e7bcea1385dc55b",
    "target_hash":"4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
    "exact_match":0
}
```

> Unless I'm missing something, this seems like the model got it wrong rather than an extraction issue?

For the model I am evaluation, there are actually quite a few cases where the model answer does not have a base subscript (like `_8`) but text before instead, and the correct answer is rated as wrong. I shared some examples in https://github.com/EleutherAI/lm-evaluation-harness/issues/3652 and a fix for (most) issues adding a `flexible_match` in https://github.com/EleutherAI/lm-evaluation-harness/pull/3653

### NezLheimeur · 2026-03-26

@fxmarty-amd Following up: I've pushed a few updates to #3644:
- **Version bump** to 1.1 in YAML metadata + README changelog
- **Multi-`\boxed{}` extraction** : handles models that output `\boxed{3}, \boxed{5}, \boxed{7}` instead of `\boxed{3, 5, 7}`. Duplicates are deduplicated (models often repeat the final answer).

I've also opened a separate PR #3655 to address the deeper equivalence issues you raised in #3652:
- **SymPy symbolic fallback** in `is_equiv` when string matching fails, falls back to `sympy.simplify` for symbolic comparison (handles `9a + 11` vs `11 + 9a`, etc.)
- **`math_verify` metric** reported alongside `exact_match` when installed, providing robust LaTeX-aware verification (same approach as `minerva_math`)

Both are optional via `pip install lm-eval[math]`, no breaking changes.

### NezLheimeur · 2026-07-31

Status update on the two PRs for this issue, both now rebased on current `main`:

- **#3644** (`\boxed{}` extraction, approved by @fxmarty-amd). Fixes the zero-accuracy case this issue reports. Includes multi-`\boxed{}` handling, dedup, the `\boxed ` space-form fallback, and 9 regression tests. Also carries a separate commit fixing the pre-existing ruff violations in `hendrycks_math/utils.py`, which otherwise fail the Linters job for any PR touching that file.
- **#3655** (optional SymPy equivalence + `math_verify`), stacked on #3644, one incremental commit. Addresses the deeper equivalence false negatives from #3652 rather than this issue's extraction bug.

Both are `MERGEABLE` and waiting on maintainer review to run CI (only the CLA check has run so far).

There's overlap with @fxmarty-amd's #3653, which also rewrites `process_results` and claims to fix this issue. I've left a note there proposing we split it so we're not maintaining conflicting rewrites of the same function, happy to defer on ordering.

@baberabb this one's ready whenever you have a moment for #3644; it's the small, approved piece.

