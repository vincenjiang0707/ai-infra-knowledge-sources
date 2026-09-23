source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/turboquant/centroids/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.turboquant.centroids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids)

Lloyd-Max optimal scalar quantizer for TurboQuant.

After rotating a d-dimensional unit vector by a random orthogonal matrix, each coordinate approximately follows N(0, 1/d) for d >= 64. We solve the Lloyd-Max conditions to find optimal centroids.

Based on: turboquant-pytorch/lloyd_max.py (Zandieh et al.)

Functions:

-
–[get_centroids](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.get_centroids)Get precomputed Lloyd-Max centroids (cached).

-
–[solve_lloyd_max](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max)Solve Lloyd-Max optimal quantizer for N(0, 1/d) distribution.


##

`_trapz(f, a, b, n=200)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids._trapz)

Trapezoidal numerical integration (replaces scipy.integrate.quad).

## Source code in `vllm/model_executor/layers/quantization/turboquant/centroids.py`


##

`get_centroids(d, bits)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.get_centroids)

Get precomputed Lloyd-Max centroids (cached).

##

`solve_lloyd_max(d, bits, max_iter=200, tol=1e-10)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max)

Solve Lloyd-Max optimal quantizer for N(0, 1/d) distribution.

Parameters:

-

(`d`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max(d))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Vector dimension (determines variance = 1/d).

-

(`bits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max(bits))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of quantization bits.

-

(`max_iter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max(max_iter))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`200`

) –Maximum Lloyd-Max iterations.

-

(`tol`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.turboquant.centroids.solve_lloyd_max(tol))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-10`

) –Convergence tolerance.


Returns:

-
(`centroids`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Sorted tensor of 2^bits optimal centroids.

-
(`boundaries`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Sorted tensor of 2^bits - 1 decision boundaries.