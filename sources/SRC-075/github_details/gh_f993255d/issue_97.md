# [Issue #97] Validation Vulnerability in MSELoss: Partial Computation Can Pass Accuracy Check

source: https://github.com/ScalingIntelligence/KernelBench/issues/97
state: open | updated: 2026-01-09T01:55:20Z
labels: 

## 正文

# Validation Vulnerability in MSELoss: Partial Computation Can Pass Accuracy Check

## Problem Description

The current MSELoss task (`level1/94_MSELoss.py`) has a validation vulnerability: generated kernel implementations that only compute a fraction of the data can still pass the accuracy verification.

### Observed Phenomenon

A faulty kernel implementation that processes only a fraction of the elements instead of the full `32768×32768` tensor can pass the accuracy check against the PyTorch reference implementation.

This leads to several critical issues:

1. **Reward Hacking in RL**: When using reinforcement learning for kernel generation, incorrect kernels receive positive rewards, causing the policy to optimize in the wrong direction
2. **False Positives in Kernel Generation**: Automated kernel generation systems based on this benchmark may produce functionally incorrect but "verified" code
3. **Benchmark Invalidation**: The benchmark fails to distinguish between correct and incorrect implementations

## Theoretical Analysis

### Current Input Generation

The original `get_inputs()` generates data as follows:

def get_inputs():
    scale = torch.rand(())
    return [torch.rand(batch_size, *input_shape)*scale, torch.rand(batch_size, *input_shape)]Where:
- `predictions` = $s \cdot U_1$, with $s \sim U(0,1)$ and $U_1 \sim U(0,1)$
- `targets` = $U_2$, with $U_2 \sim U(0,1)$

### Why Can Incorrect Implementations Pass Verification?

MSE Loss is defined as:

$$\text{MSE} = \frac{1}{N}\sum_{i=1}^{N}(s \cdot x_i - y_i)^2$$

By the **Law of Large Numbers**, when samples are i.i.d., the sample mean converges to the population expectation:

$$\frac{1}{N}\sum_{i=1}^{N}(s \cdot x_i - y_i)^2 \xrightarrow{P} \mathbb{E}[(sX-Y)^2]$$

For the current **uniform distribution** where $s, X, Y \sim U(0,1)$ are independent:

$$\mathbb{E}[(sX-Y)^2] = s^2\mathbb{E}[X^2] - 2s\mathbb{E}[X]\mathbb{E}[Y] + \mathbb{E}[Y^2]$$

$$= \frac{s^2}{3} - 2 \cdot s \cdot \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{3}  = \frac{2s^2 - 3s + 2}{6}$$

**The Core Issue**: Since uniform distribution has bounded first and second moments, whether computing fewer samples (for example, $4096$) or $32768 \times 32768$ samples, MSE converges to the same expected value.

This allows "under-computed" incorrect implementations to produce nearly identical outputs as correct implementations.

### Solution: Use Heavy-Tailed Distributions with Divergent Second Moments

To enable verification to detect computation volume differences, we need distributions with **divergent second moments**.

**Pareto Distribution** $\text{Pareto}(\alpha, x_m)$ has the following properties:

- When $\alpha > 1$: $\mathbb{E}[X] = \frac{\alpha x_m}{\alpha - 1}$ (bounded)
- When $1 < \alpha \leq 2$: $\mathbb{E}[X^2] = \infty$ (divergent)

Choosing $\alpha = 1.5$:
- **Bounded first moment**: Ensures sample values don't explode
- **Divergent second moment**: MSE expectation increases with sample size

This means:
- MSE of $m$ samples ≠ MSE of $32768 \times 32768$ samples
- Incorrect implementations will produce significantly different outputs and **fail verification**

## Proposed Fix

Modify the `get_inputs()` function to use Pareto distribution instead of uniform distribution:
```
from torch.distributions import Pareto

def get_inputs():
    predictions = Pareto(0.01, 1.5).sample((batch_size, *input_shape))
    targets = Pareto(0.01, 1.5).sample((batch_size, *input_shape))
    return [predictions, targets]
```
Recommend reviewing all tasks with aggregation operations (mean, sum, etc.) for similar vulnerabilities.

## 评论 (2)

### bkal01 · 2026-01-08

thanks for pointing out this issue and proposing a fix! using a heavy-tailed distribution w/a divergent second moment is a really clean solution to possible reward hacking here.

one possible issue is that by using a heavy-tailed distribution, we run the risk of overflowing when using `precision=fp16`. If $X\sim \text{Pareto}(x_m, \alpha)$, then $P(X > 65504) = (\frac{x_m}{65504})^{\alpha}$. If we can assume $x_m < 1$, then we want to pick the largest. $\alpha$ possible. With $x_m = 0.01, \alpha=1.99$, the probability is $\approx 3^{-14}$.

now considering we have $32768 \times 32768$ samples, we have over a billion draws, which makes overflowing almost certain.

### doux-jy · 2026-01-09

> thanks for pointing out this issue and proposing a fix! using a heavy-tailed distribution w/a divergent second moment is a really clean solution to possible reward hacking here.
> 
> one possible issue is that by using a heavy-tailed distribution, we run the risk of overflowing when using `precision=fp16`. If X ∼ Pareto ( x m , α ) , then P ( X > 65504 ) = ( x m 65504 ) α . If we can assume x m < 1 , then we want to pick the largest. α possible. With x m = 0.01 , α = 1.99 , the probability is ≈ 3 − 14 .
> 
> now considering we have 32768 × 32768 samples, we have over a billion draws, which makes overflowing almost certain.

For this problem, I think a truncated Pareto distribution can be used to balance the numerical value and stability
