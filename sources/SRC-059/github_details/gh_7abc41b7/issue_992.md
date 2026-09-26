# [Issue #992] Documentation extremely vague and unclear -- Update docs to tell us if Thinking is supported or not?

source: https://github.com/PaddlePaddle/ERNIE/issues/992
state: closed | updated: 2025-10-28T12:00:48Z
labels: 

## 正文

The ERNIE docs have total:     0 information     about Thinking for non-VLM models.

The complete and total DOCS about ERNIE have only this information:

    "The VLMs focuses on visuallanguage understanding and supports both thinking and non-thinking modes."

What does it mean? What does it imply? What is it telling us?

Just look at the table! https://ernie.baidu.com/blog/posts/ernie4.5/

```
ERNIE-4.5-300B-A47B        non-thinking
```
"-"    and    "non-thinking"    are our only 2 options.

Deductive Conclusion =>
    All ERNIE models are non-thinking except for VLM *only*


## 评论 (4)

### wtmlon · 2025-07-08

Sorry for any confusion caused. Currently, the 'thinking & non-thinking' mode is only supported in VL (Vision-Language) model and is not yet available for pure text model.

### Yzrsah · 2025-07-09

> Sorry for any confusion caused. Currently, the 'thinking & non-thinking' mode is only supported in VL (Vision-Language) model and is not yet available for pure text model.

I'm very sorry I still don't understand: There is a triple-double-negative logic being used to answer the question.

Does *not* supporting "thinking & non-thinking mode" mean that *non*-VL does *not* support thinking? 🤷
This is our triple double negative logic.

Please tell us if the non-VL *supports thinking,* instead of telling us that it "does not support thinking & non-thinking mode"

### wtmlon · 2025-07-29

Currently, non-VL model don't support thinking mode.

### nepeplwu · 2025-10-28

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
