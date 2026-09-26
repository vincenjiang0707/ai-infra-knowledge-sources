# item

source: https://news.ycombinator.com/item?id=49804052

(I posted a response on their blog but i'll repeat it here for those curious).

When it comes to eliminating subexpressions, they say:

"This is to be expected; ultimately, the algorithm is a simple greedy algorithm, which often doesn’t have the best track record with this sort of optimization problem. Trying to minimize the number of floating point operations required for the polynomial calculation is also likely an NP-hard problem, so any algorithm that actually solved this problem would be even slower than the one we came up with. "

It depends on what you mean -

1. Finding syntatically common subexpressions is linear or n log n depending how you do it

2. Eliminating the maximum possible existing value-equivalent subexpressions is polynomial.

3. Finding the smallest possible set of operations or instructions to evaluate a set of expressions is provably NP-complete (as a decision problem).

The difference between #2 and #3 is #2 is restricted to results already computed somewhere in the program (even as a subexpression), as well as canonical reordering of expression trees to expose as many of these as possible. #3 is not limited in this way. In all cases, you have to restrict to herbrand equivalence if you want it to not run into undecidability issues, at least as trying to prove things go. In practice, all compilers go beyond herbrand equivalence in specific cases to deal with common value identities (IE x+0 = x).

When it comes to eliminating subexpressions, they say:

"This is to be expected; ultimately, the algorithm is a simple greedy algorithm, which often doesn’t have the best track record with this sort of optimization problem. Trying to minimize the number of floating point operations required for the polynomial calculation is also likely an NP-hard problem, so any algorithm that actually solved this problem would be even slower than the one we came up with. "

It depends on what you mean -

1. Finding syntatically common subexpressions is linear or n log n depending how you do it

2. Eliminating the maximum possible existing value-equivalent subexpressions is polynomial.

3. Finding the smallest possible set of operations or instructions to evaluate a set of expressions is provably NP-complete (as a decision problem).

The difference between #2 and #3 is #2 is restricted to results already computed somewhere in the program (even as a subexpression), as well as canonical reordering of expression trees to expose as many of these as possible. #3 is not limited in this way. In all cases, you have to restrict to herbrand equivalence if you want it to not run into undecidability issues, at least as trying to prove things go. In practice, all compilers go beyond herbrand equivalence in specific cases to deal with common value identities (IE x+0 = x).

reply
