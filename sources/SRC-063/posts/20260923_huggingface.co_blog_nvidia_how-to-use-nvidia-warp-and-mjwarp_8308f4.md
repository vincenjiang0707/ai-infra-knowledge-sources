# How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows

source: https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp
published: Wed, 23 Sep 2026 18:41:40 GMT

#
[
](https://huggingface.co#how-to-use-nvidia-warp-and-mjwarp-to-accelerate-robotics-simulation-and-learning-workflows)
How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows

[Enterprise + Article](https://huggingface.co/blog)

[robot simulation](https://www.nvidia.com/en-us/use-cases/robotics-simulation/)for developing, testing, and controlling robots and it can parallelize sampling across CPU cores. But as learning workloads grow, the question shifts from how quickly one world can run to how many worlds can run at once. GPU acceleration makes it possible to advance those worlds in large batches while keeping simulation and learning data close to the device.

[MuJoCo Warp (MJWarp)](https://mujoco.readthedocs.io/en/latest/mjwarp/), built on [NVIDIA Warp](https://developer.nvidia.com/warp-python), takes compatible MuJoCo models into that GPU-scale regime. In this article, we will move an SO-101 follower arm from a familiar MuJoCo workflow to as many as 2,048 parallel MJWarp environments and examine the technology and validation steps that make the transition possible.

[
](https://cdn-uploads.huggingface.co/production/uploads/6994dc99f850a10f03fd0b21/8SmNNsqLiBHC0W31zT4cf.png)*Figure 1. How MJWarp connects Python to GPU simulation. MuJoCo loads and compiles the MJCF model; MJWarp implements the physics in NVIDIA Warp, which compiles CUDA kernels to advance simulation states on NVIDIA GPUs.*

*This is the second article in our State of Simulation for Physical AI series. The first article mapped the robot-simulation landscape. Here, we prepare and scale the simulation environment; we do not train a policy. The later Newton and Isaac Lab installments cover the next integration layers.*

##
[
](https://huggingface.co#putting-it-together)
**Putting it together**

| Layer | Role in the stack |
|---|---|
NVIDIA Warp |
Python kernel language: single instruction, multiple threads (SIMT), autodiff, PyTorch/JAX interop |
MJWarp |
MuJoCo physics on Warp: same MJCF, batched GPU throughput |
Your scene (SO-101) |
Familiar Menagerie / Robot Studio assets + task geometry |
Next (Newton / Isaac Lab) |
Multi-solver API, USD, sensors, managers, training loops |

**Decision shortcut:**

| If you need… | Reach for… |
|---|---|
| Single-robot MPC / teleop | MuJoCo CPU |
| Max throughput on raw MuJoCo physics | MJWarp (or
mjlab |
| JAX training recipes |
MuJoCo Playground |

**Newton**— next post in this series##
[
](https://huggingface.co#start-with-one-useful-warp-kernel)
Start with one useful Warp Kernel

[NVIDIA Warp](https://github.com/NVIDIA/warp) is a Python framework for writing high-performance, GPU-accelerated kernels. Warp lets developers author statically typed kernels in Python and compiles them for CPU or CUDA execution. The first launch builds and caches a native module; later launches reuse it. The kernel language is a performance-oriented subset of Python, while ordinary Python remains responsible for configuration, allocation, and launch orchestration.

This small robotics-oriented kernel advances point positions under gravity. One logical thread handles one point, so the same code scales from two points to millions without introducing GPU terminology into the control flow.

The three value propositions of Warp are:

| Pillar | What you get |
|---|---|
Performance |
Native-CUDA speed via JIT compilation, kernel fusion, and CUDA Graphs |
Ease of use |
Pure Python authoring with built-in vectors, matrices, quaternions, BVHs, hash grids, sparse matrices, and tile primitives |
Capability |
Differentiable kernels and DLPack-style interop so simulation can sit inside an ML training loop |

```
import numpy as np
import warp as wp
@wp.kernel
def integrate(
positions: wp.array[wp.vec3],
velocities: wp.array[wp.vec3],
dt: float,
):
i = wp.tid()
velocities[i] += wp.vec3(0.0, 0.0, -9.81) * dt
positions[i] += velocities[i] * dt
wp.init()
device = "cuda:0" if wp.is_cuda_available() else "cpu"
start = np.array([[0.0, 0.0, 0.5], [0.2, 0.0, 0.5]], dtype=np.float32)
positions = wp.array(start, dtype=wp.vec3, device=device)
velocities = wp.zeros_like(positions)
wp.launch(
integrate,
dim=len(start),
inputs=[positions, velocities, 0.01],
device=device,
)
wp.synchronize_device(device)
print(positions.numpy())
```


###
[
](https://huggingface.co#three-properties-make-this-useful-in-robotics)
Three properties make this useful in robotics:

**Explicit parallel work.**wp.tid() identifies the point, contact, body, or world owned by the current logical thread.**Explicit device arrays.**An array lives on the selected device. Calling .numpy() on a CUDA array synchronizes and copies it to CPU memory; it is not a zero-copy path. For a device-resident PyTorch or JAX pipeline, use Warp’s framework adapters or DLPack-compatible sharing instead.**Composable kernel launches.**A program can launch a sequence of focused kernels and capture supported CUDA work into a graph to reduce repeated dispatch overhead. Graph capture replays launches against existing buffers; it does not fuse arbitrary kernels.

###
[
](https://huggingface.co#differentiability-and-determinism)
**Differentiability and Determinism.**

Two further Warp capabilities are worth knowing, even though neither is used in the SO-101 workflow in this article. Warp kernels are **differentiable**: a wp.Tape records the forward kernel launches made inside its context and replays their adjoints in reverse when backward() is called, which is why teams build differentiable geometry, CFD, and custom physics in Warp, including [CAE workflows](https://developer.nvidia.com/topics/cae) for simulation and design optimization. Warp also supports **deterministic execution**, introduced in *Warp 1.15*: GPU atomics are scheduler-dependent by default, so repeated launches of the same kernel can differ slightly, and the opt-in deterministic modes trade some performance for reproducible ordering in simulation, validation, and regression tests. These are Warp capabilities, not guarantees of differentiability or determinism for an entire MJWarp rollout. See the Warp documentation on differentiability and deterministic execution for the details.

**Try Warp:** pip install warp-lang (≥ 1.15 for GPU determinism), then python -m warp.examples.browse, or the [ tutorial notebooks](https://github.com/NVIDIA/accelerated-computing-hub/tree/main/tutorials/warp/notebooks).

##
[
](https://huggingface.co#what-is-mujoco-warp-mjwarp)
**What is MuJoCo Warp (MJWarp)?**

A robot simulator repeatedly computes what happens next: given the current joint positions, velocities, controls, and contacts, it advances the scene by one small timestep. In this article, a **world** means one independent copy of that scene and its state. One world might contain the SO-101 arm reaching for a cube; another can contain the same arm starting from a slightly different pose.

MuJoCo and MJWarp can run the same compatible robot and task, but they organize the work differently. MuJoCo naturally suits developing and inspecting one or a few CPU worlds. **MJWarp** is a **NVIDIA Warp** implementation of **MuJoCo**’s physics pipeline that places the model and a batch of independent states on NVIDIA GPUs; one call to mjw.step advances the entire batch.

MJWarp’s value is not necessarily a faster step for one world. It is the ability to advance hundreds or thousands together, giving the GPU enough parallel work to improve **aggregate throughput**, the total world-steps completed per second. That favors reinforcement learning and large-scale sampling, where collecting experience matters more than minimizing one environment’s latency.

This blog covers the following:

- validate one MuJoCo world,
- move it to MJWarp, form a batch,
- verify it, and measure it correctly.

Solver tuning, Jacobian representation, and specialized multi-GPU or determinism topics are not required for this migration and can be covered separately.

Then, the distinction is precise:

**Latency**is wall-clock time for one simulation step.**Aggregate throughput**is the total number of world-steps completed per measured wall-clock second.

###
[
](https://huggingface.co#basic-usage-structs-batch-sizes-and-a-minimal-step)
**Basic usage: structs, batch sizes, and a minimal step**

- The core API transition is small:

| MuJoCo host workflow | MJWarp workflow |
|---|---|
| mujoco.MjModel | mjw.put_model(mjm) creates a device model |
| mujoco.MjData | mjw.put_data(mjm, mjd, ...) preserves and batches an existing state |
| mujoco.mj_step(mjm, mjd) | mjw.step(m, d) advances every world in d |
| Host arrays such as mjd.ctrl | Batched device arrays such as d.ctrl with shape (nworld, nu) |

Use mjw.make_data() when default/fresh state is intended. Use mjw.put_data() when the exact initialized MuJoCo state must cross the migration boundary.

Allocating batched resources requires defining the following parameters (refer to [ Batch sizes](https://mujoco.readthedocs.io/en/latest/mjwarp/#batch-sizes)):

| Parameter | Meaning |
|---|---|
| nworld | Total number of parallel environments |
| nconmax | Expected contacts per individual world (overall capacity ≈ nconmax * nworld) |
| naconmax | Alternative setting: global maximum contacts across all environments combined (takes precedence if both are defined) |
| njmax | Hard upper limit on constraints per world |

###
[
](https://huggingface.co#performance-tuning)
**Performance tuning**

1. **CUDA graph capture**:mjw.step is many kernel launches; capture once, replay often:

```
with wp.ScopedCapture() as capture:
mjw.step(m, d)
wp.capture_launch(capture.graph)
```


2. **Size nconmax / naconmax / njmax tightly**: memory and work scale with them. Tune with mjwarp-testspeed: --measure_alloc and watch overflows in mjwarp-viewer.

**Additional tuning considerations. After sizing contact and constraint buffers, test solver iteration limits without changing task behavior. Meshes and CCD settings can increase memory use; nccdmax / naccdmax can reduce CCD buffer allocation when the measured contact counts allow it. MJWarp’s compact solver uses MuJoCo’s Newton constraint solver and sleeping, not the separate Newton physics-engine framework. Compact-solver and multi-GPU configuration are beyond this walkthrough; consult the MJWarp performance-tuning documentation.**

To train policies on MJWarp physics:

via*Isaac Lab**Newton*(manager API directly on MJWarp + PyTorch)*mjlab*via MJX (impl='warp')*MuJoCo Playground*

**Install / try:** pip install mujoco-warp · mjwarp-viewer path/to/scene.xml · *Colab tutorial*

##
[
](https://huggingface.co#workflow-to-migrate-a-mujoco-scene-to-mjwarp)
Workflow to migrate a MuJoCo scene to MjWarp

**The scene.** Nothing here is MJWarp-specific yet: an SO-101 arm, a table, and two cubes to stack, written as ordinary MJCF.

*Figure 2. SO-101 pick-and-place scene, rendered from the MuJoCo CPU simulation. The task is to grasp the red 44 mm cube and stack it on the blue cube; the same robot and scene are used for MJWarp validation.*

```
<mujoco model="so101_pick_place">
<include file="so101.xml"/>
<worldbody>
<light pos="0.3 0 1.5" dir="0 0 -1" directional="true"/>
<geom name="floor" type="plane" size="0 0 0.05"/>
<geom name="table" type="box" pos="0.35 -0.04 0.012"
size="0.16 0.26 0.012" rgba="0.32 0.32 0.32 1"
friction="1 0.005 0.0005" condim="3"/>
<body name="red_cube" pos="0.33 -0.13 0.046">
<freejoint name="red_cube_joint"/>
<geom type="box" size="0.022 0.022 0.022" mass="0.08"
rgba="0.85 0.05 0.04 1" friction="1.2 0.005 0.0005" condim="3"/>
</body>
<body name="blue_cube" pos="0.33 0.06 0.046">
<freejoint name="blue_cube_joint"/>
<geom type="box" size="0.022 0.022 0.022" mass="0.08"
rgba="0.05 0.20 0.90 1" friction="1.2 0.005 0.0005" condim="3"/>
</body>
</worldbody>
</mujoco>
```


For an MJCF box, the size values are half-extents: size=”0.022 …” defines a cube with 44 mm edges. The task uses this size for its success thresholds. The arm base is at the origin, its reach is along +X, and the cubes are arranged along Y.

In the companion repository this file is generated rather than hand-written: resolve_pick_place_scene() copies the Menagerie arm into .generated/, fills the table and cube coordinates from a robot profile, and writes scene_pick_place.xml. The walkthrough uses the SO-101 profile; the optional reBot variant is described below.

**Loading it.** Compilation and stepping are ordinary MuJoCo:

```
import mujoco
mjm = mujoco.MjModel.from_xml_path("scene_pick_place.xml")
mjd = mujoco.MjData(mjm)
fps = 50 # controller rate
sim_substeps = 10 # physics steps per control frame
frame_dt = 1.0 / fps
mjm.opt.timestep = frame_dt / sim_substeps
controller = PickPlaceController(spec=spec) # waypoints + damped-least-squares IK
for _ in range(600): # 600 control frames
ctrl = controller.step(mjm, mjd, frame_dt)
for _ in range(sim_substeps):
mjd.ctrl[: mjm.nu] = ctrl
mujoco.mj_step(mjm, mjd)
```


Keep that shape in mind: **compute controls once per frame, step physics sim_substeps times.** Gate 2 changes only the inner loop, which is what makes the migration easy to review.

**Match the simulation and control rates. At 50 control frames per second and 10 physics substeps per frame, use a physics timestep of 0.002 seconds. Set it before the CPU rollout and before uploading the model with mjw.put_model so both backends advance the same simulated time:**

```
mjm.opt.timestep = frame_dt / sim_substeps # 50 Hz × 10 substeps -> 0.002 s
```


Without that line, every later measurement inherits the mismatch: parity comparisons, throughput numbers quoted as “simulated seconds,” and any learned policy whose action rate no longer matches deployment.

**Check whether the cubes are stacked successfully.** With 44 mm cubes, success becomes two measurable conditions: a horizontal center error of xy_err ≤ 0.015 m (measured between the cube centers) and a vertical separation of 0.035 m ≤ dz ≤ 0.055 m between cube centers (one cube edge, with slack for settling). Evaluate both conditions after the cubes have settled; a successful process exit alone does not establish task success.

Run the CPU task from the companion checkout. Publication blocker: confirm the accessible repository URL and pinned dependency and asset versions before publishing these instructions; the repository placeholder below is not an executable URL.

```
git clone https://github.com/NVIDIA/accelerated-computing-hub.git blogs
cd blogs/tutorials/sim2real-blogs/notebooks/mujoco
uv venv --python 3.12 && source .venv/bin/activate
uv pip install -r requirements.txt
cd /tutorials/sim2real-blogs/notebooks/mujoco
python solutions/so101_pick_place_solution.py --headless-steps 600 --debug
```


The run ends by printing the two numbers above (stack check: xy_err=… dz=…), which is the assertion the rest of the article compares against. so101_pick_place.py next to it is the same program with the physics steps left as exercises.

The arm comes straight from [ MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie/tree/main/robotstudio_so101) pinned to a known-good commit, since Menagerie assets change, so treat the scene as a template. Optional reBot variant. The companion code also exposes --robot rebot with a separate profile for the scene layout, gripper, and capacity limits (nconmax=256, njmax=500). This walkthrough uses SO-101. Validate the reBot asset and task separately before reporting its results.

Run **one** world on the GPU first, with the host still in the loop, so you can watch the same task in the same viewer and compare the same two numbers. Upload the model, allocate batched state, seed it from the initialized host state, and run one forward pass before stepping:

```
wp.init()
import mujoco_warp as mjw
device = wp.get_device()
m = mjw.put_model(mjm)
d = mjw.make_data(mjm, nworld=1, nconmax=spec.nconmax, njmax=spec.njmax)
wp.copy(d.qpos, wp.array(mjd.qpos[None, :], dtype=wp.float32, device=device))
wp.copy(d.qvel, wp.array(mjd.qvel[None, :], dtype=wp.float32, device=device))
wp.copy(d.ctrl, wp.array(mjd.ctrl[None, :], dtype=wp.float32, device=device))
mjw.forward(m, d)
```


Every device array carries a leading world dimension, which is why the host state is indexed as mjd.qpos[None, :], shape (1, nq) instead of (nq,). Scaling to thousands of worlds later changes only that leading dimension, not the calls. mjw.put_model() also doubles as a compatibility check: it raises if the model uses unsupported features rather than silently dropping them.

Seeding the three fields explicitly is the transparent option, and it makes clear exactly what crosses to the device; mjw.put_data(mjm, mjd, nworld=…) carries the whole initialized struct over in one call instead.

The frame loop is then the Gate 1 loop with its inner step redirected to the GPU and mirrored back:

```
def simulate_frame() -> None:
ctrl = controller.step(mjm, mjd, frame_dt)
for _ in range(sim_substeps):
mjd.ctrl[: mjm.nu] = ctrl
wp.copy(d.ctrl, wp.array(mjd.ctrl[None, :], dtype=wp.float32, device=device))
mjw.step(m, d)
mjd.qpos[:] = d.qpos.numpy()[0]
mjd.qvel[:] = d.qvel.numpy()[0]
mujoco.mj_forward(mjm, mjd)
```


The .numpy() reads synchronize and copy data to the host on every substep, so this is a task-validation path, not a throughput benchmark. It keeps inverse kinematics, viewing, and task checks on the host. After copying qpos and qvel, call mujoco.mj_forward(mjm, mjd) to refresh derived host quantities such as mjd.xpos before using them for control, viewing, or the stack check. Reading those fields after the loop does not refresh them automatically. Gate 4 removes these per-step host copies from the throughput path.

MJWarp allocates contact and constraint buffers before stepping. Exceeding those capacities invalidates the affected rollout for verification or benchmarking, even when execution continues with an overflow warning rather than an exception. Increase the relevant limit and rerun the task. Larger buffers use more GPU memory, so verify capacity over the full task before tightening the allocation.

Set contact and constraint limits for the robot and task being simulated. The SO-101 profile uses nconmax=128 and njmax=300 as starting capacities. Check that these limits are sufficient during the most contact-heavy part of the task:

```
d = mjw.make_data(mjm, nworld=nworld, nconmax=spec.nconmax, njmax=spec.njmax)
```


Size them against the most contact-heavy moment of the task, for pick-and-place, the instant both jaws and the table touch a cube, not the arm hovering in free space. An overflow is reported rather than raised: with Option.warn_overflow at its default, MJWarp prints the budget to increase (“narrowphase overflow - please increase nconmax to …”) to the terminal running your script or the viewer, and flags the affected worlds in Data.overflow for you to read back after a step. Only mjw.put_data raises an error outright, because it can compare the budgets against a MuJoCo state it already holds. mjwarp-testspeed --measure_alloc reports the contacts and constraints a scene actually consumed, and it aborts the rollout with the offending world IDs as soon as any world overflows. Treat those reports as failures: raise the limit and re-run before trusting either the trajectory or the benchmark, then tighten again whenever the model, collision geometry, or task changes.

Once one-world parity passes, reallocate at the target size and replicate the initialized state across the batch. Two things change relative to Gate 2: nworld, and the fact that nothing crosses the PCIe bus per step.

```
nworld = 2_048
d = mjw.make_data(mjm, nworld=nworld, nconmax=spec.nconmax, njmax=spec.njmax)
wp.copy(d.qpos, wp.array(np.tile(mjd.qpos, (nworld, 1)), dtype=wp.float32, device=device))
wp.copy(d.qvel, wp.array(np.tile(mjd.qvel, (nworld, 1)), dtype=wp.float32, device=device))
wp.copy(d.ctrl, wp.array(np.tile(mjd.ctrl, (nworld, 1)), dtype=wp.float32, device=device))
mjw.forward(m, d)
with wp.ScopedCapture() as capture:
mjw.step(m, d)
step_graph = capture.graph
```


np.tile gives every world the same starting state, which is the right baseline for a throughput measurement; per-world randomization would instead write different rows of d.qpos on the device.

CUDA Graphs reuse the model and data buffers captured here. Update d.ctrl in place between replays, and capture a new graph after replacing buffers, changing nworld, or rebuilding the model. Graph capture requires CUDA.

*Figure 3. Scaling the SO-101 task from one CPU world to 2,048 independent GPU states using the same compatible model. A single MJWarp step advances the full batch. This conceptual illustration highlights aggregate throughput, measured as world-steps per wall-clock second.*

GPU launches are asynchronous, so a naive timer measures how fast Python queued work, not how fast the GPU finished it. Warm up first — the first launches pay kernel compilation and allocation — then synchronize immediately before and after the timed region:

```
import time
for _ in range(10): # warm-up: compilation, allocation, caches
wp.capture_launch(step_graph)
wp.synchronize()
t0 = time.perf_counter()
for _ in range(200):
wp.capture_launch(step_graph)
wp.synchronize() # without this you time the queue, not the work
elapsed = time.perf_counter() - t0
total = 200 * nworld
print(f"{total / elapsed:,.0f} world-steps/second")
```


Report both aggregate world-steps per second and milliseconds per batched step, together with the batch size. Use the measured curve to identify where additional worlds improve throughput and where memory or compute limits reduce the benefit. Results depend on the scene, simulation settings, and hardware; a one-world latency comparison does not establish batched throughput.

To see that curve on your own hardware, scaling_study.py sweeps the batch size and prints ms/step alongside throughput and speedup:

```
cd /tutorials/sim2real-blogs/notebooks/mujoco/part2
python solutions/so101_mjwarp_solution.py --headless-steps 600 # parity, needs CUDA
python scaling_study.py --worlds 1 64 1024 2048 8192 --steps 100
```


##
[
](https://huggingface.co#get-started)
**Get started**

**Warp (kernel layer)**

pip install warp-lang → python -m warp.examples.browse → [ docs](https://nvidia.github.io/warp/) ·


*GitHub***MJWarp (GPU MuJoCo)**

pip install mujoco-warp → mjwarp-viewer benchmarks/humanoid/humanoid.xml → [ docs](https://mujoco.readthedocs.io/en/latest/mjwarp/) ·

[·](https://github.com/google-deepmind/mujoco_warp)

*GitHub*

*Colab tutorial***SO-101 context**

[ SO-101 sim-to-real course](https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/latest/index.html) ·


*Physical AI learning paths***Train on top of MJWarp**

[ mjlab](https://github.com/mujocolab/mjlab) ·

[· Isaac Lab + Newton (upcoming posts)](https://github.com/google-deepmind/mujoco_playground)

*MuJoCo Playground*##
[
](https://huggingface.co#whats-next)
**What’s next**

This post covered raw **Warp → MJWarp**: GPU kernels, batched stepping, and an SO-101 scene using mjw.step.

Next, we will port the same MJCF environment into **Newton**, using MuJoCo Warp as its rigid-body solver (newton.solvers.SolverMuJoCo). Newton will manage the model, state, controls, and contacts, while MJWarp runs underneath.

You will also see what Newton adds: multi-format assets, swappable solvers, sensors/IK helpers, and an Isaac Lab path.

The migration guide continues with the same SO-101 task and its optional reBot profile, explaining the changes required by Newton and the separate Isaac Lab integration.

If you build something with Warp or MJWarp, open an issue on the linked repositories or find us on Discord [ NVIDIA Omniverse](https://discord.com/invite/nvidiaomniverse).

##
[
](https://huggingface.co#references)
**References**

**Blog 1:***[The State of Simulation for Physical AI: An Overview*](https://huggingface.co/blog/nvidia/state-of-simulation-for-physical-ai)— Post 1 of this series.·*NVIDIA Warp — GitHub*·*Documentation*·*v1.15.0 release (GPU determinism)**Deterministic execution guide*·*MuJoCo Warp — GitHub**Official MJWarp docs**Build Accelerated, Differentiable Computational Physics Code for AI with NVIDIA Warp**Introducing Tile-Based Programming in Warp 1.5.0*·*mjlab**arXiv:2601.22074**MuJoCo Playground**NVIDIA SO-101 sim-to-real course*next post: MJWarp as SolverMuJoCo and porting this environment*Newton*