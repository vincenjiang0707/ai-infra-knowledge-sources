# [Issue #1370] what's the format of inline formula?

source: https://github.com/PaddlePaddle/ERNIE/issues/1370
state: closed | updated: 2026-02-19T12:01:57Z
labels: 

## 正文

for the paragraph that include inline formula, what's the prompt? OCR or formula recognition? for example: "Let us start formalizing the framework for our work. First, we consider binary boolean models $ \\mathcal{M}\\colon\\{0,1\\}^{d}\\to\\{0,1\\} $. Despite our domain being binary, we will need a third value, $ \\bot $, to denote “unknown” values. For example, we may represent a person who does have a car, does not have a house, and for whom we do not know if they have a pet or not, as $ \\left(1,\\,0,\\,\\bot\\right) $. We say elements of $ \\{0,1,\\bot\\}^{d} $ are partial instances, while elements of $ \\{0,1\\}^{d} $ are simply instances. To illustrate, in Example 1 we used the partial instance $ {\\bm{y}}=\\left(1,\\,1,\\,\\bot,\\,1\\right) $ to explain $ \\mathcal{M}({\\bm{x}})=1 $. We use the notation $ {\\bm{y}}\\subseteq{\\bm{x}} $ to denote that the (partial) instance $ {\\bm{x}} $ “fills in” values of the partial instance $ {\\bm{y}} $; more formally, we use $ {\\bm{y}}\\subseteq{\\bm{x}} $ to mean that $ y_{i}=\\bot\\lor y_{i}=x_{i} $ for every $ i\\in[d] $. Finally, for any partial instance $ {\\bm{y}} $ we denote by $ \\operatorname{Comp}({\\bm{y}}) $ the set of instances $ {\\bm{x}} $ such that $ {\\bm{y}}\\subseteq{\\bm{x}} $, thinking of $ \\operatorname{Comp}({\\bm{y}}) $ as the set of completions of $ {\\bm{y}} $. One can define sufficient reasons as follows with this notation." 

## 评论 (2)

### forBlank · 2025-11-20

@MobiusDai We recommend using "OCR:" as the prompt.

### nepeplwu · 2026-02-19

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
