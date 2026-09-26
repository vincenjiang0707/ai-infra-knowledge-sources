source: https://docs.nvidia.com/cuda/cutile-python/operations.html

# Operations[#](https://docs.nvidia.com#operations)

## Load/Store[#](https://docs.nvidia.com#load-store)

Gets the index of current block. |
|
Gets the number of blocks along the axis. |
|
Gets the number of tiles in the |
|
Loads a tile from the array which is partitioned into a |
|
Stores a tile value into the array at the index of its |
|
Loads a tile from non-contiguous slices of array. |
|
Stores a tile into non-contiguous slices of array. |
|
Loads a tile from the array elements specified by indices. |
|
Stores a tile value into the array elements specified by indices. |

## Factory[#](https://docs.nvidia.com#factory)

## Shape & DType[#](https://docs.nvidia.com#shape-dtype)

Concatenates two tiles along the axis. |
|
Broadcasts a tile to the specified shape following |
|
Reshapes the tile by inserting a new axis of size 1 at given position. |
|
Reshapes a tile to the specified shape. |
|
Permutes the axes of the input tile. |
|
Transposes two axes of the input tile with at least 2 dimensions. |
|
Converts a tile to the specified data type. |
|
Reinterpets tile as being of specified data type. |
|
Flattens a tile and reinterprets its raw bytes as uint8 elements. |
|
Reinterprets a 1D uint8 byte tile as a 1D tile of the target data type. |

## Reduction[#](https://docs.nvidia.com#reduction)

Performs sum reduction on tile along the axis. |
|
Performs max reduction on tile along the axis. |
|
Performs min reduction on tile along the axis. |
|
Performs prod reduction on tile along the axis. |
|
Performs argmax reduction on tile along the axis. |
|
Performs argmin reduction on tile along the axis. |
|
Apply custom reduction function along axis. |

## Scan[#](https://docs.nvidia.com#scan)

## Matmul[#](https://docs.nvidia.com#matmul)

Matrix multiply-accumulate. |
|
Block-scaled matrix multiply-accumulate. |
|
Performs matrix multiply on the given tiles. |

## Selection[#](https://docs.nvidia.com#selection)

## Math[#](https://docs.nvidia.com#math)

Elementwise add on two tiles. |
|
Elementwise sub on two tiles. |
|
Elementwise mul on two tiles. |
|
Elementwise truediv on two tiles. |
|
Elementwise floordiv on two tiles. |
|
Computes ceil(x / y). |
|
Elementwise pow on two tiles. |
|
Elementwise atan2 of two tiles. |
|
Elementwise mod on two tiles. |
|
Elementwise |
|
Elementwise minimum on two tiles. |
|
Elementwise maximum on two tiles. |
|
Same as -x. |
|
Perform abs on a tile. |
|
Perform isnan on a tile. |
|
Perform exp on a tile. |
|
Perform exp2 on a tile. |
|
Perform log on a tile. |
|
Perform log2 on a tile. |
|
Perform sqrt on a tile. |
|
Perform rsqrt on a tile. |
|
Perform sin on a tile. |
|
Perform cos on a tile. |
|
Perform tan on a tile. |
|
Perform sinh on a tile. |
|
Perform cosh on a tile. |
|
Perform tanh on a tile. |
|
Perform floor on a tile. |
|
Perform ceil on a tile. |

## Bitwise[#](https://docs.nvidia.com#bitwise)

Elementwise bitwise_and on two tiles. |
|
Elementwise bitwise_or on two tiles. |
|
Elementwise bitwise_xor on two tiles. |
|
Elementwise bitwise_lshift on two tiles. |
|
Elementwise bitwise_rshift on two tiles. |
|
Elementwise bitwise not on a tile. |

## Comparison[#](https://docs.nvidia.com#comparison)

Compare two tiles elementwise with >. |
|
Compare two tiles elementwise with >=. |
|
Compare two tiles elementwise with <. |
|
Compare two tiles elementwise with <=. |
|
Compare two tiles elementwise with ==. |
|
Compare two tiles elementwise with !=. |

## Atomic[#](https://docs.nvidia.com#atomic)

Bulk atomic compare-and-swap on array elements with given indices. |
|
Bulk atomic exchange of array elements at given indices. |
|
Bulk atomic post-increment of array elements at given indices. |
|
Bulk atomic maximum value assignment on array elements at given indices. |
|
Bulk atomic minimum value assignment on array elements at given indices. |
|
Bulk atomic AND operation on array elements at given indices. |
|
Bulk atomic OR operation on array elements at given indices. |
|
Bulk atomic XOR operation on array elements at given indices. |

## Utility[#](https://docs.nvidia.com#utility)

Print the values at runtime from the device |
|
Print values at runtime from the device using Python-style syntax. |
|
Assert that all elements of the given tile are True. |
|
Declares that |
|
Allow a programmatically dependent successor kernel to begin scheduling. |
|
Wait for the preceding kernel in a programmatic dependent launch to finish. |

## Metaprogramming Support[#](https://docs.nvidia.com#metaprogramming-support)

Asserts that the argument is a compile-time constant and returns it. |
|
Asserts that a condition is true at compile time. |
|
Evaluates the given Python expression at compile time. |
|
Iterates at compile time. |

## Classes[#](https://docs.nvidia.com#classes)

Class for |
|
Class for |
|
A start + length index for array dimensions. |

## Enums[#](https://docs.nvidia.com#enums)

Rounding mode for floating-point operations. |
|
Padding mode for load operation. |

## Autotuning[#](https://docs.nvidia.com#autotuning)

Searches the entire search space and return the best configuration. |

Holds the measurement result for each config. |
|
Holds a configuration and its timing result. |

Return a new kernel with updated compiler hints. |
|
Context manager that temporarily sets the compiler timeout. |

## JAX FFI[#](https://docs.nvidia.com#jax-ffi)

Launch a cuTile kernel from a JAX-traced graph. |

Represents an output buffer passed to cutile_call. |
|
Wraps an input buffer to alias an output buffer to be returned by cutile_call. |