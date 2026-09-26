# [Issue #1862] [Issue]: RCCL HWID accessor defines break for -generic targets

source: https://github.com/ROCm/rccl/issues/1862
state: closed | updated: 2026-01-22T02:06:27Z
labels: 

## 正文

### Problem Description

The RCCL HWID ifdefs check for specific arches instead of using the `__GFX11__` define that exists for the entire series of arches. This breaks for targets like `gfx11-generic` which don't define a specific target like `gfx1100`

They're also not using the new `HW_REG_HW_ID1` reg that exists on gfx10/11/12. `HW_REG_HW_ID` doesn't exist on 11+, and isn't documented on 10 but does work. (Seems to be an alias to HW_REG_HW_ID1)

Suggested fix:

```patch
fix: __trace_hwreg should use HW_REG_HW_ID1 for all gfx10/11/12
diff --git a/src/device/common.h b/src/device/common.h
index c6c61021..742885f4 100644
--- a/src/device/common.h
+++ b/src/device/common.h
@@ -26,8 +26,9 @@
   { __atomic_store_n((DST), (SRC), __ATOMIC_SEQ_CST); }
 #endif
 
-#if defined(__gfx1100__) || defined(__gfx1101__) || defined(__gfx1102__) || defined(__gfx1200__) || defined(__gfx1201__)
-#define __trace_hwreg()
+#if defined(__GFX10__) || defined(__GFX11__) || defined(__GFX12__)
+#define __trace_hwreg() \
+  asm volatile ("s_getreg_b32 %0, hwreg(HW_REG_HW_ID1)" : "=s" (collTrace->data_0));
 #else
 #define __trace_hwreg() \
   asm volatile ("s_getreg_b32 %0, hwreg(HW_REG_HW_ID)" : "=s" (collTrace->data_0));
diff --git a/tools/JitterBench/Common.hpp b/tools/JitterBench/Common.hpp
index bad12a1b..b59856a8 100644
--- a/tools/JitterBench/Common.hpp
+++ b/tools/JitterBench/Common.hpp
@@ -43,9 +43,9 @@ THE SOFTWARE.
 #endif
 
 // Macro for collecting HW_REG_HW_ID
-#if defined(__gfx1100__) || defined(__gfx1101__) || defined(__gfx1102__) || defined(__NVCC__)
+#if defined(__GFX10__) || defined(__GFX11__) || defined(__GFX12__)
 #define GetHwId(val) \
-  val = 0
+  asm volatile ("s_getreg_b32 %0, hwreg(HW_REG_HW_ID1)" : "=s" (val));
 #else
 #define GetHwId(val) \
   asm volatile ("s_getreg_b32 %0, hwreg(HW_REG_HW_ID)" : "=s" (val));
```

It might be more futureproof to do something like the following pseudocode:

```
if __GFX9__ HW_REG_HW_ID
elseif __GFX10/11/2__ HW_REG_HW_ID1
else warn and noop
```

## 评论 (4)

### thananon · 2025-08-17

This is somewhat expected. RCCL does not support generic kernels. 

### LunNova · 2025-08-17

Any plans to change that in the future or is RCCL always going to be intended to be compiled against an exhaustive individual arch target list?

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2784

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
