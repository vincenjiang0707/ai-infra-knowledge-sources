# [Issue #2329] [Question]: Should NCCL validate NVLink P2P status via NVML to allow graceful fallback?

source: https://github.com/NVIDIA/nccl/issues/2329
state: closed | updated: 2026-08-07T12:13:35Z
labels: question

## 正文

### Question

NCCL assumes NVLink connectivity is fully functional based on topology detection. However, on broken or degraded hardware, an NVLink might be detected but P2P communication is not functioning, leading to this error:
```
P2P is disabled between NVLINK connected GPUs 1 and 0. This should not be the case given their connectivity, and is probably due to a hardware issue. If you still want to proceed, you can set NCCL_IGNORE_DISABLED_P2P=1.
```

Instead of failing the topology validation or requiring global bypass flags like `NCCL_IGNORE_DISABLED_P2P=1`, could NCCL validate specific pairs via NVML and gracefully ignore degraded paths?

We are using this patch to skip paths where NVML reports non-OK P2P status:
```
diff --git a/src/graph/paths.cc b/src/graph/paths.cc
index 0100b19826..0100b3d777 100644
--- a/src/graph/paths.cc
+++ b/src/graph/paths.cc
@@ -93,6 +93,18 @@
           newType = PATH_NVB;
         newType = std::max(path->type, newType);
 
+        // Check if NVLink has fully functioning P2P.
+        if (baseNode->type == GPU && remNode->type == GPU && newType <= PATH_NVB) {
+          int g1 = baseNode->gpu.dev;
+          int g2 = remNode->gpu.dev;
+          NCCLCHECK(ncclNvmlEnsureInitialized());
+          if (ncclNvmlDevicePairs[g1][g2].p2pStatusRead != NVML_P2P_STATUS_OK ||
+              ncclNvmlDevicePairs[g1][g2].p2pStatusWrite != NVML_P2P_STATUS_OK) {
+            INFO(NCCL_GRAPH, "Ignoring NVLink path from DEV %d to DEV %d due to disabled P2P", g1, g2);
+            continue;
+          }
+        }
+
         // Update if better path type, OR same type with higher bw, OR same type/bw with strickly fewer hops.
         // Note: path->count +1 to account for the existing path + current candidate, see remPath->count update.
         if (newType < remPath->type || (newType == remPath->type && remPath->bw < bw) ||
```

## 评论 (2)

### sjeaugey · 2026-08-07

I can't say whether the NVML test is fully equivalent to the CUDA P2P test, but one thing remains: we do not want to silently ignore faulty hardware.

As you scale, the probability of one faulty node increases, and that can severely degrade your performance. Most users do not want to run at a fraction of the speed without knowing, and they also want to know which node is broken to avoid/replace it.

We provided an environment variable to allow users to ignore the error though. So if that's what you want, why not set that env var?

### thearusable · 2026-08-07

That makes sense. We'll go with the env var. Thanks for the explanation!
