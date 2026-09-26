source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.html
lastmod: 

# openvino.runtime.opset1[#](https://docs.openvino.ai#module-openvino.runtime.opset1)

Functions

|
Return node which applies f(x) = abs(x) to the input node element-wise. |
|
Return node which applies f(x) = abs(x) to the input node element-wise. |
|
Apply inverse cosine function on the input node element-wise. |
|
Return node which applies f(A,B) = A+B to the input nodes element-wise. |
|
Apply inverse sine function on the input node element-wise. |
|
Apply inverse tangent function on the input node element-wise. |
|
Return average pooling node. |
|
Perform layer normalizes a input tensor by mean and variance with appling scale and offset. |
|
Create node performing convolution with binary weights, binary input and integer output. |
|
Create a node which broadcasts the input node's values along specified axes to a desired shape. |
|
Return node which applies ceiling to the input node element-wise. |
|
Return node which applies ceiling to the input node element-wise. |
|
Perform clamp element-wise on data from input node. |
|
Concatenate input nodes into single new node along specified axis. |
|
Create a Constant node from provided value. |
|
Return node which casts input node values to specified type. |
|
Return node which casts data node values to the type of another node. |
|
Return node performing batched convolution operation. |
|
Create node performing a batched-convolution backprop data operation. |
|
Apply cosine function on the input node element-wise. |
|
Apply hyperbolic cosine function on the input node element-wise. |
|
Perform greedy decoding on the logits given in input (best path). |
|
Create node performing deformable convolution. |
|
Return node performing DeformablePSROIPooling operation. |
|
Rearranges input tensor from depth into blocks of spatial data. |
|
Generate the detection output using information on location and confidence predictions. |
|
Return node which applies f(x) = A/B to the input nodes element-wise. |
|
Perform Exponential Linear Unit operation element-wise on data from input node. |
|
Return node which checks if input nodes are equal element-wise. |
|
Return node which calculates Gauss error function element-wise with given tensor. |
|
Return node which applies exponential function to the input node element-wise. |
|
Perform an element-wise linear quantization on input data. |
|
Return node which applies floor to the input node element-wise. |
|
Return node performing element-wise FloorMod (division reminder) with two given tensors. |
|
Return Gather node which takes slices from axis of data according to indices. |
|
Perform GatherTree operation. |
|
Return node which checks if left input node is greater than the right node element-wise. |
|
Return node which checks if left node is greater or equal to the right node element-wise. |
|
Perform Global Response Normalization with L2 norm (across channels only). |
|
Perform Group Convolution operation on data from input node. |
|
Perform Group Convolution operation on data from input node. |
|
Perform Hard Sigmoid operation element-wise on data from input node. |
|
Perform interpolation of independent slices in input tensor. |
|
Return node which checks if left input node is less than the right node element-wise. |
|
Return node which checks if left input node is less or equal the right node element-wise. |
|
Return node which applies natural logarithm to the input node element-wise. |
|
Return node which perform logical and operation on input nodes element-wise. |
|
Return node which applies element-wise logical negation to the input node. |
|
Return node which performs logical OR operation on input nodes element-wise. |
|
Return node which performs logical XOR operation on input nodes element-wise. |
|
Return a node which performs element-wise Local Response Normalization (LRN) operation. |
|
Return a node which performs LSTMCell operation. |
|
Return the Matrix Multiplication operation. |
|
Perform max pooling operation with given parameters on provided data. |
|
Return node which applies the maximum operation to input nodes elementwise. |
|
Return node which applies the minimum operation to input nodes elementwise. |
|
Return node performing element-wise division reminder with two given tensors. |
|
Return node which applies f(A,B) = A*B to the input nodes elementwise. |
|
Return node which applies f(x) = -x to the input node elementwise. |
|
Return a node which performs NonMaxSuppression. |
|
Construct an NormalizeL2 operation. |
|
Return node which checks if input nodes are unequal element-wise. |
|
Create node performing one-hot encoding on input data. |
|
Return a generic padding operation. |
|
Return an openvino Parameter object. |
|
Return node which perform element-wise exponentiation operation. |
|
Perform Parametrized Relu operation element-wise on data from input node. |
|
Generate prior boxes of specified sizes and aspect ratios across all dimensions. |
|
Generate prior boxes of specified sizes normalized to the input image size. |
|
Filter bounding boxes and outputs only those with the highest prediction confidence. |
|
Return a node which produces a PSROIPooling operation. |
|
Return a node which produces the Range operation. |
|
Logical AND reduction operation on input tensor, eliminating the specified reduction axes. |
|
Logical OR reduction operation on input tensor, eliminating the specified reduction axes. |
|
Max-reduction operation on input tensor, eliminating the specified reduction axes. |
|
Mean-reduction operation on input tensor, eliminating the specified reduction axes. |
|
Min-reduction operation on input tensor, eliminating the specified reduction axes. |
|
Product-reduction operation on input tensor, eliminating the specified reduction axes. |
|
Perform element-wise sums of the input tensor, eliminating the specified reduction axes. |
|
Return a node which produces the RegionYolo operation. |
|
Perform rectified linear unit operation on input node element-wise. |
|
Return reshaped node according to provided parameters. |
|
Return a node which represents an output of a graph (Model). |
|
Return a node which produces a ReverseSequence operation. |
|
Perform an element-wise selection operation on input tensors. |
|
Perform a Scaled Exponential Linear Unit (SELU) operation on input node element-wise. |
|
Return a node which produces a tensor containing the shape of its input data. |
|
Return a node which applies the sigmoid function element-wise. |
|
Perform element-wise sign operation. |
|
Apply sine function on the input node element-wise. |
|
Apply hyperbolic sine function on the input node element-wise. |
|
Apply softmax operation on each element of input tensor. |
|
Perform SpaceToDepth operation on the input tensor. |
|
Return a node which splits the input tensor into same-length slices. |
|
Return node which applies square root to the input node element-wise. |
|
Perform an element-wise squared difference between two tensors. |
|
Perform squeeze operation on input tensor. |
|
Return a node which dynamically repeats(replicates) the input data tensor. |
|
Return node which applies f(x) = A-B to the input nodes element-wise. |
|
Apply tangent function on the input node element-wise. |
|
Return node which applies hyperbolic tangent to the input node element-wise. |
|
Return a node which dynamically repeats(replicates) the input data tensor. |
|
Return a node which performs TopK. |
|
Return a node which transposes the data in the input tensor. |
|
Perform unsqueeze operation on input tensor. |
|
Return a node which splits the input tensor into variadic length slices. |

Classes

openvino.impl.op.TensorIterator wraps ov::op::v0::TensorIterator |