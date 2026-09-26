source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__runtime__cpu__prop__cpp__api.html
lastmod: 

# Group Intel CPU specific properties[#](https://docs.openvino.ai#group-intel-cpu-specific-properties)

-
*group*Intel CPU specific properties Set of Intel CPU specific properties.

Variables

-
static constexpr Property<bool> denormals_optimization = {"CPU_DENORMALS_OPTIMIZATION"}
[#](https://docs.openvino.ai#_CPPv422denormals_optimization) This property define whether to perform denormals optimization.

Computation with denormals is very time consuming. FTZ(Flushing denormals to zero) and DAZ(Denormals as zero) could significantly improve the performance, but it does not comply with IEEE standard. In most cases, this behavior has little impact on model accuracy. Users could enable this optimization if no or acceptable accuracy drop is seen. The following code enables denormals optimization

ie.set_property(ov::denormals_optimization(true)); // enable denormals optimization

The following code disables denormals optimization

ie.set_property(ov::denormals_optimization(false)); // disable denormals optimization


-
static constexpr Property<float> sparse_weights_decompression_rate = {"CPU_SPARSE_WEIGHTS_DECOMPRESSION_RATE"}
[#](https://docs.openvino.ai#_CPPv433sparse_weights_decompression_rate) This property defines threshold for sparse weights decompression feature activation.

Sparse weights decompression feature allows to pack weights for Matrix Multiplication operations directly in the CPU plugin at the model compilation stage and store non-zero values in a special packed format. Then, during the execution of the model, the weights are unpacked and used in the computational kernel. Since the weights are loaded from DDR/L3 cache in the packed format this significantly decreases memory consumption and as a consequence improve inference performance. The following code allows to set the sparse rate value.

core.set_property(ov::intel_cpu::sparse_weights_decompression_rate(0.8));


-
static constexpr Property<bool> denormals_optimization = {"CPU_DENORMALS_OPTIMIZATION"}