# [Issue #3175] [Transform] FreshenMutableReads: rationale for Mode and a path to remove it

source: https://github.com/tile-ai/tilelang/issues/3175
state: closed | updated: 2026-09-10T16:15:46Z
labels: 

## 正文

`FreshenMutableReads` keeps mutable reads out of persistent arithmetic-analyzer substitutions. #3174 proposes an explicit `Mode` so the existing visitor can also serve analyses that describe one captured value in several expressions. This issue records the rationale and proposes a path to remove that mode once captured values have explicit identities in the analysis representation.

Related: #2805 introduced the upstream per-occurrence behavior; #3174 adds the opt-in snapshot behavior. The implementation discussed here is [the version proposed in #3174](https://github.com/tile-ai/tilelang/blob/093a568c3dff0bfbc3bbd56479235fb7a8ad8b00/src/transform/common/constr_visitor.h).

**What `FreshenMutableReads` does**

`Analyzer::Bind(v, expr)` installs a reusable substitution. Keeping an expression that reads mutable state in that substitution can incorrectly equate a value captured earlier with a later read:

```text
v = A[i]        // v captures the old value
A[i] = new_value
... A[i] ...   // this read need not equal v
```

The helper replaces mutable or state-dependent expressions with fresh symbolic variables before such definitions are bound. The current implementation handles buffer loads, producer loads, reductions, and calls whose effect classification (including their arguments) is not pure. It preserves ordinary SSA variables and pure arithmetic around the replaced expressions.

This is an analysis abstraction: it neither inserts runtime loads nor makes memory immutable. It deliberately loses some information so that the analyzer does not invent equalities across stores, access points, or independently modeled executions. `Constr::FreshenReads()` applies it to value/range bindings before `Constr::Populate()` installs them in the analyzer.

**Why introduce two modes?**

Two uses currently present similar expression trees with different meanings:

| Mode | Caller contract | Replacement |
| --- | --- | --- |
| `kPerOccurrence` (unchanged default) | Each occurrence may be a separate evaluation. | Allocate an independent unknown for each visited occurrence. |
| `kSnapshot` (opt-in) | Repeated structurally equal expressions refer to the same captured value within this instance. | Reuse an unknown through an instance-local `memo_`. |

For example, two evaluations of an opaque call must remain independent:

```text
f() - f()  ->  u0 - u1
```

Memoizing those calls would produce `u0 - u0` and incorrectly prove zero. Likewise, identical-looking loads on opposite sides of a store must not be equated. Structural equality, or even reuse of the same IR node object, does not establish a shared runtime evaluation.

The motivating snapshot use is Ascend region dependency analysis. When one captured region base is copied into derived bounds, both copies must retain the same symbolic value:

```text
min = captured_base
max = captured_base + 15

per occurrence: min = u0, max = u1 + 15
snapshot:       min = u0, max = u0 + 15
```

The second representation retains `max - min == 15`. Losing that relationship can prevent valid disjointness proofs and retain unnecessary dependencies or synchronization. Producer and consumer access points use separate snapshots because mutable state may change between them.

The Ascend integration currently needs a separate `SnapshotFreshenMutableReads` visitor for this behavior. #3174 consolidates the traversal while making the semantic choice explicit and preserving all existing default callers. The enum is scoped to `FreshenMutableReads` because it describes this visitor's contract.

Snapshot mode relies on the caller to establish the shared-value contract. The mode itself does not prove that reads are stable or prevent a caller from merging independent stateful evaluations. One visitor per access point is necessary for this use, but does not by itself justify merging every identical expression inside that access point.

**Proposed path to remove `Mode`**

Move captured-value identity into the region analysis data, at the point where the origin of each evaluation is still known:

1. Represent each actual mutable evaluation by an explicit symbolic variable before deriving or duplicating bounds. Reuse that variable wherever the analysis refers to that captured result. Distinct evaluations, including separate opaque calls, get distinct variables. Preserve any existing SSA value identity.
2. Derive min/max/extent and other region expressions from those variables. For a range with a captured minimum, the essential change is to freshen the minimum once and construct the maximum from the resulting expression, rather than freshening two already-expanded bounds independently:

```text
min = freshen(raw_min)          // ordinary per-occurrence freshening
extent = freshen(raw_extent)
max = min + extent - 1
```

This illustrates the simple case where `raw_min` and `raw_extent` are independent source expressions. If several fields or dimensions already refer to one captured result, their common variable must be established before those fields are built. Freshening every field separately after that provenance has been lost is insufficient.

3. Carry these identities through region construction, substitutions, and comparisons. Keep independent access points independent, and rename execution-private symbols when modeling different threads or loop iterations. Start with analysis-local data; introducing these symbols does not require inserting runtime captures or a whole-program memory-SSA pass.
4. Migrate the snapshot callers to that representation. Once no supported caller needs structural memoization to recover captured-value identity, remove `kSnapshot`, the `Mode` constructor parameter, and `memo_`. Keep `FreshenMutableReads` with its original per-occurrence semantics for remaining mutable expressions.

The intended reduction is to preserve identity when constructing analysis expressions, eliminating the need to reconstruct it later with a policy switch. Moving the same structural memoization into another generic visitor would leave the underlying ambiguity in place.

**Completion criteria**

- [ ] Audit snapshot consumers and identify where each captured value originates, including relationships across region fields and dimensions.
- [ ] Preserve region-bound relationships such as `max - min == extent - 1` without snapshot-mode freshening.
- [ ] Test separate opaque evaluations, reads separated by writes (including aliases), and independent producer/consumer, thread, and iteration instances; none may acquire unsupported equalities.
- [ ] Retain tests where several derived expressions intentionally share one captured result, including multi-dimensional regions.
- [ ] Validate ThreadSync, VerifyParallelLoop, and the affected Ascend dependency/synchronization paths, checking both correctness and unwanted increases in dependencies or barriers.
- [ ] Remove all snapshot-mode consumers, then delete the enum and memoization.

This is a follow-up design proposal. #3174 provides the explicit contract needed by current callers; it does not implement the representation change above or make the mode immediately removable.


## 评论 (1)

### LeiWang1999 · 2026-09-07

**Native reproducer: snapshot memoization can hide a real overlapping access**

I reproduced an incorrect disjointness result in the actual Ascend `RegionsMayConflict()` implementation. This was tested in the downstream Ascend integration checkout at `2e944be2e7e0f35adba008308927bdcd0d2d89e8`, after a successful native rebuild. This revision and the Ascend function are downstream code, not upstream `main`.

The function currently uses `SnapshotFreshenMutableReads`, whose structural memoization has the same sharing policy as the proposed `kSnapshot`. The test does not modify or reimplement that visitor or the dependency function.

The access pair is:

```cpp
// next_counter() returns 0, then 1.
idx = int(next_counter() != next_counter());
B[idx] = 42;
result = B[1];
```

The two calls return different values in either operand evaluation order, so both accesses target `B[1]`. However, snapshot memoization merges the two independent calls:

```text
int(next_counter() != next_counter())
    -> int(region_read0 != region_read0)
    -> 0
```

The dependency analysis then treats the writer as accessing `B[0]` and incorrectly reports no conflict with the reader at `B[1]`. Pre-freshening the index with ordinary per-occurrence semantics preserves two independent unknowns and correctly reports a possible conflict.

The C++ test constructs distinct, structurally equal, opaque TIR call nodes and calls the real native dependency function. It also executes `next_counter()` in a small native reference computation to give a concrete overlap witness. Controls cover known overlapping/disjoint constant regions and two references to one legitimately captured SSA value.

<details>
<summary>Full C++ reproducer: save as repro.cc</summary>

```cpp
#include "ascend/transform/auto_schedule/dependency_analysis.h"

#include <tvm/arith/analyzer.h>
#include <tvm/tirx/builtin.h>
#include <tvm/tirx/op.h>

#include <iostream>

using namespace tvm;
using namespace tvm::tirx;

// Two calls return 0 and 1. Their inequality is true in either evaluation order.
extern "C" int next_counter() {
  static int counter = 0;
  return counter++;
}

int main() {
  const auto dtype = DataType::Int(32);
  PrimExpr call_a =
      Call(dtype, builtin::call_extern(), {StringImm("next_counter")});
  PrimExpr call_b =
      Call(dtype, builtin::call_extern(), {StringImm("next_counter")});
  ICHECK(!call_a.same_as(call_b));
  ICHECK(ExprDeepEqual()(call_a, call_b));
  ICHECK(SideEffect(call_a) > CallEffectKind::kPure);

  // Writer: B[int(next_counter() != next_counter())] = 42
  // Reader: result = B[1]
  // Each region has exactly one element and uses the same logical buffer.
  PrimExpr writer_index = Cast(dtype, NE(call_a, call_b));
  Buffer buffer = decl_buffer({2}, dtype, "B");
  BufferRegion reader(buffer, {Range::FromMinExtent(1, 1)});
  tl::ConstrSet context;
  auto may_conflict = [&](const PrimExpr &index) {
    BufferRegion writer(buffer, {Range::FromMinExtent(index, 1)});
    return tl::RegionsMayConflict(context, writer, context, reader, nullptr, 0);
  };

  // Execute the opaque function to provide a concrete witness.
  const int first = next_counter();
  const int second = next_counter();
  const int actual_writer_index = first != second;
  int storage[2] = {0, 0};
  storage[actual_writer_index] = 42;
  const int read_value = storage[1];
  ICHECK_EQ(actual_writer_index, 1);
  ICHECK_EQ(read_value, 42);

  // Controls: known overlap / known disjointness / per-occurrence abstraction.
  ICHECK(may_conflict(Integer(1)));
  ICHECK(!may_conflict(Integer(0)));
  tl::FreshenMutableReads per_occurrence;
  PrimExpr independent_index = per_occurrence(writer_index);
  const bool conservative_result = may_conflict(independent_index);
  ICHECK(conservative_result);

  // Two references to one already-captured SSA value really are equal.
  Var captured("captured", dtype);
  ICHECK(!may_conflict(Cast(dtype, NE(captured, captured))));

  // This invokes the real Ascend implementation from the local native library.
  // It uses SnapshotFreshenMutableReads internally, with no code changes here.
  const bool snapshot_result = may_conflict(writer_index);
  std::cout << std::boolalpha;
  std::cout << "Runtime calls: " << first << ", " << second << "\n";
  std::cout << "Runtime writer index: " << actual_writer_index << "\n";
  std::cout << "Runtime reader index: 1; value after write: " << read_value << "\n";
  std::cout << "Per-occurrence index: " << independent_index << "\n";
  std::cout << "Per-occurrence may-conflict: " << conservative_result << "\n";
  std::cout << "Current Ascend snapshot may-conflict: " << snapshot_result << "\n";
  std::cout << "Expected may-conflict: true\n";
  if (!snapshot_result) {
    std::cout << "BUG REPRODUCED: a real overlapping access pair is classified as disjoint.\n";
    return 1;
  }
  std::cout << "The bug did not reproduce.\n";
  return 0;
}
```

</details>

The native library must be built from the Ascend checkout above, with `build/compile_commands.json` available. Save the following driver as `run_repro.py` next to `repro.cc`, then run it from that checkout's root:

```bash
cmake --build build -j16
python /path/to/run_repro.py
```

The driver reuses the checkout's compilation flags and selects the matching native libraries. It requires no device execution. Exit status **1** means the incorrect classification was reproduced.

<details>
<summary>Build and run driver: run_repro.py</summary>

```python
import json
import os
from pathlib import Path
import shlex
import subprocess

# Run this script from the configured Ascend checkout root.
root = Path.cwd().resolve()
repro = Path(__file__).resolve().parent
build = root / 'build'
entries = json.loads((build / 'compile_commands.json').read_text())
entry = next(item for item in entries if item['file'].endswith('/src/ascend/transform/auto_schedule/dependency_analysis.cc'))
original = shlex.split(entry['command'])
command = []
index = 0
while index < len(original):
    arg = original[index]
    if arg == '-o':
        index += 2
        continue
    if arg == '-c' or arg == entry['file']:
        index += 1
        continue
    command.append(arg)
    index += 1
command.extend([
    '-std=c++17', str(repro / 'repro.cc'), '-o', str(repro / 'repro'),
    '-L' + str(build / 'lib'), '-Wl,-rpath,' + str(build / 'lib'),
    '-ltilelang', '-ltvm_compiler', '-ltvm_runtime', '-ltvm_ffi', '-lz3',
    '-ldl', '-pthread',
])
subprocess.run(command, cwd=entry['directory'], check=True)
native_env = os.environ.copy()
native_env['LD_LIBRARY_PATH'] = str(build / 'lib') + os.pathsep + native_env.get('LD_LIBRARY_PATH', '')
result = subprocess.run([str(repro / 'repro')], env=native_env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(repro / 'output.txt').write_text(result.stdout)
print(result.stdout, end='')
print('Native reproducer exit status:', result.returncode)
raise SystemExit(result.returncode)
```

</details>

Observed output:

```text
Runtime calls: 0, 1
Runtime writer index: 1
Runtime reader index: 1; value after write: 42
Per-occurrence index: T.Cast("int32", free0 != free1)
Per-occurrence may-conflict: true
Current Ascend snapshot may-conflict: false
Expected may-conflict: true
BUG REPRODUCED: a real overlapping access pair is classified as disjoint.
Native reproducer exit status: 1
```

This establishes a failure in the native region-dependency function. It does not establish an end-to-end NPU kernel miscompilation or which frontend/pipeline paths currently deliver this expression to that function.

The important boundary is that **one snapshot instance per access point does not justify merging separate stateful evaluations within that access point**. A legitimate snapshot preserves repeated references to one already-captured result; this example contains two separate evaluations instead. The enum documents this distinction but does not enforce it.

For these region queries, replacing a valid snapshot abstraction with independent unknowns weakens precision and remains conservative. The reverse substitution can invent equalities and produce an incorrect proof, as above. This supports preserving captured-value identities before deriving bounds, so the shared visitor can eventually retain only per-occurrence semantics without losing the required region relationships.

