# accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros

source: https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros/

GPU acceleration can speed up compute-intensive robotics workloads, but a fast [CUDA](https://developer.nvidia.com/cuda/toolkit) kernel alone does not guarantee a fast ROS 2 graph. As messages move between nodes, they may continue to be serialized or copied through CPU memory, eroding the benefits of keeping perception and AI workloads on the GPU (Figure 1).

With the upstream [ rosidl::Buffer](https://github.com/ros2/rosidl/tree/lyrical/rosidl_buffer) abstraction and the

[CUDA buffer backend](https://github.com/ros2/rosidl_buffer_backends/tree/main/cuda_buffer_backend)that NVIDIA recently contributed to

[ROS Lyrical](https://osralliance.org/2026/09/ros-lyrical-luth-gains-vendor-neutral-accelerated-memory-transport-from-nvidia/), ROS 2 nodes can exchange GPU-resident payloads through zero-copy transport when runtime conditions allow, while preserving standard ROS 2 messages and node boundaries. All nodes in

[NVIDIA Isaac ROS 5.0](https://nvidia-isaac-ros.github.io/)have been updated to use the CUDA buffer backend and benefit from the more efficient data movement enabled by

`rosidl::Buffer`

.Existing ROS 2 nodes can adopt `rosidl::Buffer`

with minimal changes. The more challenging task is identifying the correct boundaries to update. This requires a careful audit of allocations, serialization, stream ownership, and fallback behavior.

This tutorial walks you through how to turn that audit into an agent-driven workflow. An [AI coding agent](https://www.nvidia.com/en-us/ai/) uses the purpose-built `migrate-node-to-rosidl-buffer`

skill to inspect an existing CUDA-accelerated node, trace data movement, plan a minimal interface-preserving refactor, and verify that the CUDA transport path is actually enabled. You’ll learn how to use the agent skill to update the node to adopt the CUDA buffer backend. The resulting accelerated workload can then be deployed on [NVIDIA Jetson AGX Thor](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/).

## Introducing `rosidl::Buffer`

and CUDA buffer backend

In ROS 2 Lyrical, variable-length primitive array fields such as `uint8[]`

are represented in generated C++ code by `rosidl::Buffer<uint8_t>`

. The default CPU-backed rosidl::Buffer behaves like the `std::vector<uint8_t>`

interface existing ROS 2 code expects, preserving source compatibility. The pluggable abstraction also allows platform vendors to support externally managed storage without defining a separate ROS message type.

NVIDIA contributed the CUDA buffer backend for ROS 2 Lyrical. It implements `rosidl::Buffer<uint8_t>`

storage with CUDA Virtual Memory Management (VMM). When publisher and subscriber meet backend runtime requirements, the payload can move between co-located nodes without serialization or host copies. Otherwise, ROS 2 automatically falls back to the CPU path that’s compatible with any existing ROS 2 nodes. The optimized path requires the same host, CUDA device, Linux user, and a supported RMW implementation (for example, `rmw_fastrtps_cpp`

and `rmw_zenoh_cpp`

).

Together, `rosidl::Buffer`

and the CUDA buffer backend move memory sharing and data-lifetime management behind a standard ROS 2 field. This means the upstream capability is easier to adopt in GPU-accelerated robotics applications, so you can focus on node logic while retaining CPU fallback for incompatible peers.

## Start with the ROS 2 node

This tutorial uses the [Depth Anything 3 (DA3) TensorRT ROS 2 node](https://github.com/ika-rwth-aachen/ros2-depth-anything-v3-trt) as the example. The DA3 model predicts spatially consistent geometry from an arbitrary number of visual inputs, with or without known camera poses.

We aim to update this node to adopt the introduced CUDA buffer backend to take advantage of the performance improvement offered by the `rosidl::Buffer`

feature. The node is particularly useful as a migration example because its algorithm is already GPU-accelerated.

This node’s callback converts the incoming ROS image to an OpenCV view, runs monocular metric-depth inference with NVIDIA [TensorRT](https://github.com/nvidia/tensorrt), converts the resulting `cv::Mat`

back to a ROS image, and publishes it as a floating-point depth image.

The code is straightforward, but the CPU-backed ROS boundary surrounds a GPU-native algorithm. That CPU boundary is appropriate for a CPU producer or consumer, but it is unnecessary when the nodes on both sides can already produce and consume CUDA memory. In that case, the two payload-sized host transfers, host allocation, and serialization work become an optimization opportunity at the interface.

The goal is therefore not to redesign the model or replace its standard messages; rather, it is to preserve the existing ROS contract while allowing the output `Image.data`

field to carry storage from an appropriate backend.

## Plan the migration using the agent skill

An AI coding agent is well suited to investigative work: following payloads through callbacks and helper libraries, finding host-device boundaries, preserving the node contract, and coordinating source, dependency, launch, and test changes.

The `migrate-node-to-rosidl-buffer`

skill turns this analysis into a repeatable workflow. Rather than replacing the node with a template or rewriting code automatically, it directs the agent to:

- Record the starting revision, target ROS environment, and existing local changes
- Confirm the compatibility of the generated message field type and add CUDA buffer backend packages as dependencies
- Trace each message field from receipt to publication, including transitive CUDA calls, strides, streams, optional outputs, and ownership
- Run the read-only copy-boundary audit and inspect each result in context
- Make a per-field migration plan that identifies removed copies, required promotions or materializations, and paths that should remain unchanged
- Implement the smallest interface-preserving patch
- Verify semantics, backend negotiation, separate-process transport, buffer lifetime, and actual memory-copy behavior independently

## Refactor the node with `rosidl::Buffer`


Using the `rosidl::Buffer`

migration skill, the agent updates the node’s dependencies and interfaces to adopt the CUDA buffer backend. Most changes adapt the TensorRT wrapper to accept CUDA buffer handles for input and output data while preserving its existing API. The ROS transport change remains small: one subscription option, one CUDA allocation, two stream-aware handle extractions, and one publish. No custom message, duplicate CUDA topic, or CPU/CUDA publisher branch is required.

The following sections explain the key changes you can expect from the skill for the node migration.

### Adding the CUDA buffer backend dependencies

First, the skill helps add CUDA buffer backend packages (`cuda_buffer`

and `cuda_buffer_backend`

) as additional dependencies. The message definition does not change—the node continues using `sensor_msgs/msg/Image`

.

### Updating the image subscription to accept CUDA messages

The subscriber is then updated to accept messages with CUDA-backed buffers. CPU remains an acceptable fallback by default, so the node-level callback does not need separate CPU and CUDA implementations.

`rclcpp::SubscriptionOptions options;` `options.acceptable_buffer_backends = ` `"cuda"` `;` `sub_image_.subscribe(` ` ` `this` `, image_base_topic, image_transport,` ` ` `rclcpp::SensorDataQoS().get_rmw_qos_profile(), options);` |

The existing `image_transport`

and `message_filters`

topology remains in place. The subscription options are simply forwarded through it.

### Writing directly into CUDA-backed message storage

The subscriber callback still accepts `bgr8`

, preserves the header, dimensions, encoding, and byte stride, and converts with `cv_bridge`

only when a different input encoding requires it. With the update, the TensorRT inference now directly writes the results to the CUDA buffer allocated in the output message, ready to publish right after the GPU work is enqueued.

The following excerpt contains the essential changes that leverage CUDA buffer APIs:

`auto` `depth_msg = std::make_unique<sensor_msgs::msg::Image>();` `depth_msg->header = bgr_image_msg->header;` `depth_msg->height = bgr_image_msg->height;` `depth_msg->width = bgr_image_msg->width;` `depth_msg->encoding = sensor_msgs::image_encodings::TYPE_32FC1;` `depth_msg->is_bigendian = ` `false` `;` `depth_msg->step = depth_msg->width * ` `sizeof` `(` `float` `);` `depth_msg->data = cuda_buffer_backend::allocate_buffer(` ` ` `static_cast` `<` `size_t` `>(depth_msg->step) * depth_msg->height);` `const` `cudaStream_t stream = tensorrt_depth_anything_->getCudaStream();` `{` ` ` `auto` `input = cuda_buffer_backend::from_input_buffer(` ` ` `bgr_image_msg->data, stream);` ` ` `auto` `output = cuda_buffer_backend::from_output_buffer(` ` ` `depth_msg->data, stream);` ` ` `tensorrt_depth_anything_->doInferenceCuda(` ` ` `input.get_ptr(), bgr_image_msg->width, bgr_image_msg->height,` ` ` `bgr_image_msg->step, *camera_info_msg,` ` ` `reinterpret_cast` `<` `float` `*>(output.get_ptr()),` ` ` `node_param_.point_cloud_downsample_factor,` ` ` `node_param_.colorize_point_cloud,` ` ` `node_param_.publish_point_cloud,` ` ` `node_param_.enable_debug);` `} ` `// Release the CUDA event-tracked handles before publishing.` `pub_depth_image_->publish(std::move(depth_msg));` |

Each line has a narrow purpose:

`allocate_buffer()`

gives the standard`Image.data`

field CUDA buffer-backed storage.`from_input_buffer()`

supplies a CUDA buffer handle that is safe to consume on the TensorRT stream for read-only operations. CUDA input is used directly. CPU input is promoted to CUDA when necessary.`from_output_buffer()`

supplies a CUDA buffer handle that is safe for write operations. The existing CUDA postprocess writes its final`32FC1`

result directly into the buffer assigned to the outgoing message through the write handle, avoiding both a device-to-host copy and an intermediate device-to-device output.- The inner scope releases the write handle after work has been enqueued on the associated stream to record a write CUDA event before the message is published, ensuring the order of the CUDA operations.
- The node calls
`publish()`

as it normally does with the same message type while the underlying data field is now backed by the CUDA buffer backend. The CUDA memory sharing and compatibility with its downstream subscribers are handled automatically by the ROS 2 middleware as well as the backends.

### Keeping optional host work separate

The skill keeps the non-CUDA route intact. Point-cloud construction and debug visualization are local CPU consumers in the original node. When enabled, they may still require a device-to-host copy and synchronization. They do not determine the representation delivered on the depth topic, so the migration leaves them as explicit optional boundaries rather than complicating the optimized publication path.

## Build and run the GPU-accelerated ROS 2 pipeline

The `rosidl::Buffer`

feature was introduced in ROS 2 Lyrical, so the migrated node is expected to work with Lyrical and above with supported RMW implementations (`rmw_fastrtps_cpp`

and `rmw_zenoh_cpp`

).

During the migration, the core functions and boundary message types are kept the same and add `cuda_buffer`

and `cuda_buffer_backend`

as additional dependencies to the package for enabling CUDA buffer backend. As a result, the overall build process and setup remain similar to the original node.

To enable CUDA buffer backend, build the packages from source. Start by cloning the source from the [ rosidl_buffer_backends](https://github.com/ros2/rosidl_buffer_backends) repository where all the currently supported backends and companion packages are hosted:

`git clone https:` `//github` `.com` `/ros2/rosidl_buffer_backends` `.git` |

Note that the core functions of `rosidl::Buffer`

are already built in ROS 2 Lyrical, so there is no need to rebuild the ROS 2 core packages.

The `rosidl::Buffer`

backends are designed to be ROS 2 plugins. Building and sourcing the CUDA buffer backend packages in the same workspace is sufficient to make the backend available to the nodes at runtime.

`colcon build --symlink-install --packages-up-to cuda_buffer_backend` `source install/setup.bash` `colcon build --symlink-install --packages-up-to depth_anything_v3` `source install/setup.bash` `export RMW_IMPLEMENTATION=rmw_fastrtps_cpp` |

You can then follow the same model preparation process and run the same launch file with the updated TensorRT node as instructed in the original repository.

## Verify the CUDA buffer backend

The migration leaves the [TensorRT](https://developer.nvidia.com/tensorrt) computation unchanged and targets the transport around it. To inspect GPU activity and memory transfers, use [NVIDIA Nsight Systems](https://developer.nvidia.com/nsight-systems). On an eligible CUDA path, the migrated node should not show payload-sized host-to-device or device-to-host transfers at its ROS boundary. Record comparable latency measurements before and after the change.

You can also validate backend negotiation from the subscriber. When both endpoints meet the CUDA backend requirements, `msg->data.get_backend_type()`

should report `"cuda"`

. This is useful for tests that confirm the CUDA transport path is active.

`rclcpp::SubscriptionOptions options;` `options.acceptable_buffer_backends = ` `"cuda"` `;` `subscription_ = create_subscription<sensor_msgs::msg::Image>(` ` ` `"/depth_anything_v3/output/depth_image"` `, rclcpp::QoS(1),` ` ` `[` `this` `](sensor_msgs::msg::Image::ConstSharedPtr msg) {` ` ` `const` `std::string backend = msg->data.get_backend_type();` ` ` `RCLCPP_INFO(get_logger(), ` `"received backend=%s"` `, backend.c_str());` ` ` `if` `(backend != ` `"cuda"` `) {` ` ` `throw` `std::runtime_error(` `"CUDA transport was not negotiated"` `);` ` ` `}` ` ` `auto` `input = cuda_buffer_backend::from_input_buffer(msg->data, stream_);` ` ` `consume_on_cuda(input.get_ptr(), stream_);` ` ` `},` ` ` `options);` |

Note that the production code will often try to accept CPU fallback without throwing the error.

With the provided CUDA buffer APIs, `from_input_buffer()`

automatically handles the CPU fallback internally. Users don’t have to distinguish the CPU path and GPU path in the callback for incoming messages. All the CUDA memory sharing and CPU-to-GPU conversion, if needed, are taken care of by the CUDA buffer backend.

The skill also contains a verification step that helps produce custom source and sink nodes for testing and validation. This is done by creating two pipelines based on the generated source and sink nodes to test the same migrated node working under both CPU and GPU setup without code changes.

In the CPU control setup, a source node that publishes messages with CPU-based data is used. The messages arrive at the TensorRT node with a buffer that is backed by plain CPU storage. The CUDA buffer APIs used in the subscriber callback automatically detects the buffer backend type and do the conversion (CPU to CUDA in this case) when needed, so the same code functions as expected to accept CPU-based messages.

In another setup, a source node that publishes CUDA buffer-based messages is used. With the migrated TensorRT node, the CUDA buffer-aware subscriber can receive the message and obtain the CUDA handle by using the CUDA buffer APIs without additional CPU-GPU copies.

## Deploy the agent-driven ROS 2 workflow on NVIDIA Jetson AGX Thor

The same workflow can be applied to other CUDA-accelerated ROS 2 nodes with variable-length primitive message fields. The key is to treat optimization as an end-to-end systems task. The AI agent traces data movement, identifies which fields benefit from GPU-backed storage, preserves standard ROS 2 interfaces, and verifies both the optimized path and CPU fallback. That makes the migration repeatable instead of a one-off refactor.

NVIDIA Isaac ROS 5.0 brings this workflow into an accelerated robotics software stack, while NVIDIA Jetson AGX Thor provides the edge compute platform for running demanding ROS 2 perception, inference, and autonomy workloads on the robot.

## Get started with ROS 2 node acceleration

Accelerating a ROS 2 node requires optimizing GPU computation as well as data movement. With `rosidl::Buffer`

, the NVIDIA CUDA buffer backend, and an Isaac ROS 5.0 AI-guided migration skill, existing CUDA-enabled nodes can exchange GPU-resident data with minimal code changes. This avoids unnecessary serialization and CPU copies while preserving standard ROS 2 message interface.

To get started, follow these steps:** **

[Download NVIDIA Isaac ROS 5.0](https://nvidia-isaac-ros.github.io/)- Review the
[ROS 2 Lyrical rosidl::Buffer and CUDA buffer backend documentation](https://docs.ros.org/en/lyrical/ROS-Framework/interfaces/Working-with-interfaces/Buffer-Backends/About-Buffer-Backends.html) - Install the
[migrate-node-to-rosidl-buffer agent skill](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli)used in this post - Run the agent-guided workflow on an existing CUDA-accelerated ROS 2 node
- Deploy and profile the resulting graph on NVIDIA Jetson AGX Thor

## Start the discussion at forums.developer.nvidia.com
