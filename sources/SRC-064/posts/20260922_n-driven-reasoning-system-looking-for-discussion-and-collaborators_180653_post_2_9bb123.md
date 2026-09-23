# A Proposition Decomposition and Contradiction-Driven Reasoning System — Looking for Discussion and Collaborators

source: https://discuss.huggingface.co/t/a-proposition-decomposition-and-contradiction-driven-reasoning-system-looking-for-discussion-and-collaborators/180653#post_2
published: Tue, 22 Sep 2026 06:39:54 +0000

**Abstract**

I am exploring a reasoning system that uses proposition decomposition and contradiction search rather than asking an LLM to directly judge whether two propositions are contradictory.

The basic idea is to decompose propositions into smaller components, identify corresponding propositions through implication relations, and use these relations to search for contradictions. The system is intended to separate probabilistic exploration from a more reliable formal verification process.

I am particularly interested in whether actively searching for contradictions can provide a useful direction for reasoning and exploration under a limited generation budget.

This is still a research design rather than a completed system. I am looking for discussion, criticism, alternative approaches, and collaborators who may be interested in implementing or testing the idea.

Terminology used in this specification

**Proposition**: A statement that can be treated as a logical unit and can be related to other propositions by logical relations.**Decomposition**: Breaking a proposition into smaller propositions while preserving its logical content, or a specified implication relationship to the original proposition.**Implication relation**: A relation of the form`P → Q`

, meaning that if`P`

holds,`Q`

follows within the adopted formal system.**Identification / correspondence**: Determining which decomposed or derived propositions refer to the same subject or content, using their internal structure and implication relations rather than exact string matching.**Collision**: A search-stage situation in which corresponding content is found in both positive and negative forms through decomposition, identification, and/or implication. A collision is a target for logical verification; it is not itself synonymous with a formally proven contradiction.**Contradiction**: A formally established state in which the two input propositions cannot be true simultaneously.**Candidate**: A proposition, decomposition, implication, or derived statement that has been generated or proposed for further verification but has not yet been established as valid.**Formal verification**: Mechanical or otherwise explicitly formal checking of logical properties within the adopted formal system.

0. Purpose

The central system to be built is a **contradiction checker**.

The basic I/O is deliberately simple.

```
Input: Proposition P, Proposition Q
Output: Whether P and Q contradict each other
```


However, the two propositions are not compared directly as strings.

**The propositions are decomposed, and implication relations between propositions are used to identify parts that can be regarded as expressing the same subject or content; the resulting identification is then used to search for contradictions.**

Therefore, **proposition identification is not merely a function for checking whether a decomposition is valid; it is itself a foundation of contradiction checking.**

The central hypothesis is that, compared with generating a large number of candidates without direction, a search that actively pursues collisions with existing propositions may discover contradictions more efficiently under limited generation and computational budgets. This is a hypothesis to be supported or refuted experimentally.

1. Central system structure

```
Proposition P Proposition Q
↓ ↓
Proposition decomposition / normalization
↓ ↓
Acquisition of implication / compositional relations
↓ ↓
Proposition identification / correspondence
↓
Collision search
↓
Formal logical verification
↓
CONTRADICTION / CONSISTENT / UNKNOWN
```


If a learning system is connected later, a search loop is added here.

```
Collision candidate generation
↓
Verifier
↓
Reward
↓
Next candidate generation
```


**The checker itself and the search process that looks for candidates are kept separate.**

2. Meaning of “proposition identification”

Here, identification does not mean exact string matching.

A proposition is decomposed into constituent sub-propositions, and the implication relations between them and existing propositions are examined.

Conceptually, for example,

```
P → A → B → C
Q → A → B → C
```


means that P and Q share at least the common logical structure A, B, and C.

Likewise,

```
P → A
Q → B
B → A
```


means that, although P and Q are superficially different, they become comparable with respect to A.

Therefore, identification and correspondence use:

- decomposed propositions,
- implication relations,
- relations by which higher-level propositions are constructed, and
- structure separate from the truth value of a proposition’s affirmation/negation.

**Truth value and the content/structure of a proposition are treated separately.**

For example, `p`

and `¬p`

should be treated as corresponding positive and negative forms of the same underlying proposition, rather than as completely unrelated propositions.

3. Role of proposition identification

Proposition identification has at least two uses.

3.1 Validity of decomposition

When an original proposition P is decomposed into

```
P1, P2, ..., Pn
```


the system checks whether the content reconstructed from the decomposed elements has the same meaning, or the same specified implication relations, as P.

For a simple AND decomposition, for example,

```
P ↔ (P1 ∧ P2 ∧ ... ∧ Pn)
```


can be verified.

3.2 Contradiction checking

When comparing P and Q, the propositions derived from both are first put into correspondence.

Then, if a relation such as

```
P → A
Q → ¬A
```


is found for the same subject/content, this becomes a candidate for testing whether P and Q can hold simultaneously.

Longer paths are also allowed.

```
P → A → B → C
Q → D → ¬C
D → C
```


In this case, P and Q respectively imply C and ¬C, so they form a collision candidate.

**Therefore, proposition identification/correspondence is not merely a preprocessing step for contradiction checking; it constructs the comparison space in which contradictions can be discovered.**

4. Contradiction checking

The initial version primarily targets propositional logic.

Input:

```
P
Q
```


Output:

```
CONTRADICTION
CONSISTENT
UNKNOWN
```


Definitions:

**CONTRADICTION**: It has been formally shown that P ∧ Q cannot hold simultaneously.**CONSISTENT**: It has been shown that there exists an assignment/model in which P ∧ Q can hold simultaneously.**UNKNOWN**: The current implementation cannot decide the result within its supported scope.

“Failure to find a contradiction” is not treated as “consistent.”

Within domains such as propositional logic where finite search is possible, the system should be deterministic whenever possible.

5. Idea of contradiction search

P and Q are not compared in a single step.

Both are decomposed, and propositions that can be derived from them are expanded step by step.

Conceptually, paths such as

```
P → A → B → C
Q → D → E → ¬C
```


are constructed, and the system checks whether positive and negative forms eventually appear for content that can be identified as the same.

The ideal form is to explore combinations of propositions derived from P and Q as broadly as possible and discover collisions such as

```
A and ¬A
B and ¬B
C and ¬C
...
```


However, enumerating all consequences leads to combinatorial explosion, so the search process selects promising directions.

6. “Collision-seeking”

Candidate generation is not treated as undirected random search.

For example, given an existing proposition P, the search objective is:

Generate a proposition that may collide with P.


However, the system must consider the possibility that a search may degenerate into simply generating `¬P`

repeatedly. The appropriate reward structure is itself an experimental variable.

Initial reward candidates:

```
Collision found → positive reward
No collision found → low / 0 reward
Could not be formalized → low / negative reward
```


As needed, additional terms such as the number of inference steps to the collision, decomposition validity, and redundancy may be added.

**A “non-trivial collision” is not required as a formal definition.**

The central comparison is:

```
Undirected search
vs.
Collision-seeking search
```


with the collision discovery efficiency compared under the same generation and computational budgets.

7. Proposition decomposition

Decomposition is not simply “the more fine-grained, the better.”

At minimum, the following properties are required.

7.1 Validity

Logical content should be preserved between the original and decomposed forms.

```
Original proposition
↓ decomposition
P1, P2, ..., Pn
↓ reconstruction
Equivalent to the original proposition / satisfies the specified implication relations
```


7.2 Non-redundancy

The system checks whether each component is actually necessary.

If removing an element Pi still allows the original proposition to be fully preserved from the remaining elements, Pi may be treated as a redundant component.

Conceptually, one can verify conditions such as:

```
P1 ∧ ... ∧ Pn entails P
P1 ∧ ... ∧ ¬Pi ∧ ... ∧ Pn does not entail P
```


A component is not rewarded merely for making the representation finer.

The current specification does not claim that this problem is necessarily NP-hard. The intended claim is only that searching for minimal sufficient decompositions or minimal evidence sets may cause combinatorial explosion.

8. Proposition graph

Propositions are not treated as mere strings, but as nodes connected by relations.

Example:

```
P → A
A → B
B → C
Q → D
D → C
```


This shows that P and Q both imply C.

With negation included,

```
P → A → B → C
Q → D → ¬C
```


can produce a collision candidate.

Role of the graph

The proposition graph is not the final truth checker.

Its main roles are to:

- preserve proposition structure,
- find propositions that are comparable,
- trace implication paths, and
- reduce the search space for collisions.

Final logical checking is performed by a separate formal verifier.

9. Comparability

Not every proposition needs to be compared with every other proposition.

First, implication relations, structure, and correspondence of subjects are used to narrow the set to propositions that may be describing the same thing.

After candidate correspondences are produced, an LLM may be used for semantic comparison of atomic propositions that cannot be formally matched.

Do not insist on complete mechanical determination here. The LLM is used as an auxiliary mechanism for constructing comparison targets, **not as the final contradiction checker**.

10. Unknown / undecidable within scope

Unknown propositions are not forcibly assigned a truth value.

```
Decidable within the formal system
→ formal verification
Not decidable within the formal system
→ UNKNOWN
```


Search and experiments for acquiring external information are future extensions and are not the center of the minimal implementation.

11. Learning / search process

After the checker is completed, an LLM may be connected as a search process.

```
LLM
↓
Generate proposition decompositions / derived propositions / collision candidates
↓
Formal verifier
↓
Reward
↓
Next candidate generation
```


Multiple candidates are generated and evaluated through the verifier.

At this stage, reinforcement learning such as GRPO may be used.

In production, LoRA / QLoRA may be applied to an existing LLM, and Unsloth or similar tools may be used as the training infrastructure. The training infrastructure itself is not the research target.

12. Minimal research experiment

The first experiment is not intended to determine whether an “intelligent AI” can be built.

It tests the following single point:


Under the same generation budget, can collision-seeking search discover more contradictions than undirected search?

The comparison should be controlled for quantities such as:

```
Number of generated candidates
Token count
Computation time
```


Candidate evaluation measures include:

```
Number of discovered contradictions / number of generated candidates
Number of discovered contradictions / token count
Number of discovered contradictions / computation time
```


A toy dataset may be used initially, but **the production code and toy-specific code should not be designed as separate systems**. The same design should allow the model size to be changed while preserving the system being evaluated.

13. Implementation boundaries

LLM is responsible for

- Natural-language proposition generation
- Generating proposition decomposition candidates
- Generating derived-statement candidates
- Generating collision candidates
- Proposing comparison candidates for atomic propositions that cannot be formalized
- Proposing search directions

As mechanically as possible

- Syntax checking
- Logical validity of decompositions
- Verification of implication relations
- Equivalence checking
- Contradiction / satisfiability
- Redundancy checking
- Core reward calculation

In principle, the LLM is **not** used to make the final judgment “Do these two propositions contradict?”

14. Theoretical considerations

14.1 Distinguish “consistent” from “unknown”

This is the most important point.

14.2 Distinguish “logical identity” from “semantic similarity in natural language”

Do not treat a formally proven equivalence and an LLM judgment that two statements are similar as the same kind of result.

14.3 Mutual information and logical implication are not the same

Mutual information represents statistical dependence over probability distributions.

Implication represents a relation within a logical system.

The present method is not proposed as a direct alternative definition of mutual information. It is positioned as a method for making comparable information explicit as logical structure.

14.4 State the scope of completeness explicitly

Do not claim that every natural-language proposition can be determined with certainty.

First specify the formal system being targeted, and then seek as much rigor and completeness as possible within that scope.

15. Research policy


Conserve data and reduce hypotheses with small experiments before spending large amounts of computation.

Use intuition to generate hypotheses, but use explicit definitions, predictions, and falsification conditions during verification.

**The following supplementary note describes the broader motivation that led me to focus on trial-and-error search and the direction of reasoning.**

An Additional Note on Trial and Error in AI

The history of academic discoveries has, in most cases, been driven by trial and error. If there were a universal algorithm capable of solving every unsolved problem, one would expect it to have been discovered during the last 2,000 years. It has not. For details, please search for the P vs NP problem.

Since there is no universal algorithm for problem solving, the only way to approach unsolved problems may be to “search through them the hard way.” Therefore, is it really correct to try to solve unsolved problems with an algorithm called an LLM? Even if trial and error can be performed inside a model, I suspect it would remain very limited.

There is research suggesting that OpenAI’s o1, particularly the o3 series, can exhibit trial-and-error behavior, and I think this is directionally correct. However, many problems remain:

- Long-term memory
- Long-term adjustment of the direction of reasoning
- Diverse trial and error toward more meaningful directions
- Generating combinations at a more abstract level than random word selection at the output level
- Efficient search algorithms
- Changing the direction of future trial and error based on the results of previous trials

Personally, I think the last two are especially important. I have tried to tackle them, but they are quite difficult.

Whenever I think about the problems of AI, extrapolation seems to appear as an issue everywhere. But perhaps humans also extrapolate by performing an enormous amount of search.