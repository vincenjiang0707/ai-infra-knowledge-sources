source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/routing_simulator_router/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.router.routing_simulator_router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router)

Classes:

-
–[DistributionBasedRouting](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting)Distribution-based random routing strategy with configurable distributions.

-
–[RoutingSimulator](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator)Token-to-Expert Routing Simulator.

-
–[RoutingSimulatorRouter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulatorRouter)Router that uses routing simulation strategies for testing/debugging.

-
–[RoutingStrategy](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy)Base class for token-to-expert routing strategies.


##

`DistributionBasedRouting`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting)

Bases: [RoutingStrategy](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy)

Distribution-based random routing strategy with configurable distributions.

This routing strategy randomly selects experts for each token based on different probability distributions. Currently supports uniform and normal distributions for testing different routing patterns.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.__init__)Initialize distribution-based routing.

-
–[get_distribution_info](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.get_distribution_info)Get information about the current distribution configuration.

-
–[route_tokens](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.route_tokens)Randomly select experts for each token using the specified distribution.


## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


|
|

###

`__init__(distribution='uniform', **distribution_params)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.__init__)

Initialize distribution-based routing.

Parameters:

-

(`distribution`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.__init__(distribution))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'uniform'`

) –Type of distribution to use for sampling - "uniform": Uniform distribution (default) - "normal": Normal/Gaussian distribution

-

(`**distribution_params`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.__init__(**distribution_params))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Parameters specific to the chosen distribution For "uniform": No additional parameters needed For "normal": mean (default: 0.0), std (default: 1.0)


## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`_generate_weights(num_tokens, top_k, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting._generate_weights)

Generate weights based on the distribution.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`_normalize_samples(samples)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting._normalize_samples)

Normalize samples to [0, 1] range.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`_sample_continuous_distribution(num_tokens, top_k, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting._sample_continuous_distribution)

Sample from continuous distributions.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`_sample_expert_ids(num_tokens, num_experts, top_k, device, indices_type)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting._sample_expert_ids)

Sample expert IDs based on the specified distribution.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`_validate_distribution_params()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting._validate_distribution_params)

Validate distribution type and parameters.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`get_distribution_info()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.get_distribution_info)

Get information about the current distribution configuration.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`route_tokens(hidden_states, router_logits, top_k, indices_type=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.route_tokens)

Randomly select experts for each token using the specified distribution.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.route_tokens(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input hidden states [num_tokens, hidden_size]

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.route_tokens(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits [num_tokens, num_experts]

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.route_tokens(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts to select per token

-

(`indices_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.DistributionBasedRouting.route_tokens(indices_type))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for expert indices


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tuple of (topk_weights, topk_ids) where:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)- topk_weights: Weights based on distribution sampling

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]- topk_ids: Expert indices sampled from the distribution


## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


##

`RoutingSimulator`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator)

Token-to-Expert Routing Simulator.

This class provides a framework for testing and comparing different routing strategies for MoE models. It can simulate routing behavior and collect statistics for analysis.

Methods:

-
–[get_available_strategies](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.get_available_strategies)Get list of available routing strategy names.

-
–[register_strategy](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.register_strategy)Register a custom routing strategy.

-
–[simulate_routing](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing)Simulate token-to-expert routing using the specified strategy.


## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


|
|

###

`get_available_strategies()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.get_available_strategies)

Get list of available routing strategy names.

Returns:

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`register_strategy(name, strategy)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.register_strategy)

Register a custom routing strategy.

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.register_strategy(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the strategy

-

(`strategy`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.register_strategy(strategy))

) –[RoutingStrategy](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy)RoutingStrategy instance


## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`simulate_routing(hidden_states, router_logits, strategy_name, top_k, indices_type=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing)

Simulate token-to-expert routing using the specified strategy.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input hidden states [num_tokens, hidden_size]

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits [num_tokens, num_experts]

-

(`strategy_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing(strategy_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the routing strategy to use

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts to select per token

-

(`indices_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulator.simulate_routing(indices_type))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for expert indices


Returns:

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


##

`RoutingSimulatorRouter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulatorRouter)

Bases: [BaseRouter](https://docs.vllm.ai/base_router/#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter)

Router that uses routing simulation strategies for testing/debugging.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`_compute_routing(hidden_states, router_logits, indices_type, *, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingSimulatorRouter._compute_routing)

Use routing simulator to compute routing.

## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


##

`RoutingStrategy`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for token-to-expert routing strategies.

Methods:

-
–[route_tokens](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy.route_tokens)Route tokens to experts.


## Source code in `vllm/model_executor/layers/fused_moe/router/routing_simulator_router.py`


###

`route_tokens(hidden_states, router_logits, top_k, indices_type=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy.route_tokens)

Route tokens to experts.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy.route_tokens(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input hidden states [num_tokens, hidden_size]

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy.route_tokens(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits [num_tokens, num_experts]

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy.route_tokens(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts to select per token

-

(`indices_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.routing_simulator_router.RoutingStrategy.route_tokens(indices_type))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for expert indices


Returns: