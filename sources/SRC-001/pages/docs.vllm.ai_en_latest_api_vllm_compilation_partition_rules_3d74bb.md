source: https://docs.vllm.ai/en/latest/api/vllm/compilation/partition_rules/
lastmod: 2026-09-24

#

`vllm.compilation.partition_rules`

[¶](https://docs.vllm.ai#vllm.compilation.partition_rules)

Functions:

-
–[inductor_partition_rule_context](https://docs.vllm.ai#vllm.compilation.partition_rules.inductor_partition_rule_context)Context manager to temporarily register Inductor partition rules.

-
–[should_split](https://docs.vllm.ai#vllm.compilation.partition_rules.should_split)Check if a node should be split for dynamo graph partition.


##

`inductor_partition_rule_context(splitting_ops)`

[¶](https://docs.vllm.ai#vllm.compilation.partition_rules.inductor_partition_rule_context)

Context manager to temporarily register Inductor partition rules.

Registers custom partition rules for specified operators, forcing the Inductor scheduler to partition the graph at these operators. The rules are automatically restored to their previous state on exit.

Parameters:

## Source code in `vllm/compilation/partition_rules.py`


##

`should_split(node, splitting_ops)`

[¶](https://docs.vllm.ai#vllm.compilation.partition_rules.should_split)

Check if a node should be split for dynamo graph partition. It operates on dynamo graph, so the node.target can be anything. We need to check and split only on OpOverload and OpOverloadPacket.