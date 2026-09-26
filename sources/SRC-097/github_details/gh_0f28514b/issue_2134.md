# [Issue #2134] [FEATURE][plugin] Add an IBM Storage Scale (GPFS) backend plugin

source: https://github.com/ai-dynamo/nixl/issues/2134
state: open | updated: 2026-08-20T18:47:19Z
labels: 

## 正文

<html><head></head><body>
<h2>Summary</h2>
<p>I'd like to contribute a NIXL backend plugin for <strong>IBM Storage Scale</strong> (formerly GPFS),
exposed as <code>libplugin_IBM_SCALE.so</code> / backend name <code>IBM_SCALE</code>. It supports
<code>DRAM_SEG</code> &lt;-&gt; <code>FILE_SEG</code> transfers over a Storage Scale mount and issues
Storage Scale-specific <code>gpfs_fcntl()</code> hints around registration and transfer so
the filesystem can prefetch, pin, and release cache for exactly the byte ranges
NIXL has registered.</p>
<p>A working implementation exists out-of-tree and I'm ready to open a PR. Filing
this first per the contribution flow (issue -&gt; maintainer approval -&gt; PR) and to
get agreement on naming, build integration, and CI strategy before I send code.</p>
<h2>Motivation</h2>
<p>Disaggregated inference deployments that offload KV cache to shared storage
frequently sit on Storage Scale — it's the dominant parallel filesystem in
HPC and large enterprise AI clusters, and it's what's underneath a lot of
existing GPU cluster storage tiers.</p>
<p>Today those deployments can use the POSIX plugin, which works but treats the
mount as an opaque POSIX filesystem. That leaves the filesystem-specific
controls unused:</p>
<ul>
<li><strong>No access hints.</strong> Storage Scale can't distinguish a NIXL registration from
any other <code>open()</code>, so it can't prefetch the registered range or size its
buffer pool for the access pattern NIXL already knows about.</li>
<li><strong>No scoped cache release.</strong> When a range is deregistered, the pagepool keeps
it resident until normal eviction pressure removes it, competing with ranges
that are still hot.</li>
<li><strong>No write-sharing hint.</strong> Multiple agents writing disjoint offsets in the
same file fall into byte-range token ping-pong instead of fine-grain write
sharing.</li>
</ul>
<p><code>gpfs_fcntl()</code> addresses all three, and NIXL's <code>registerMem</code> / <code>deregisterMem</code> /
<code>postXfer</code> lifecycle maps onto those hints almost exactly — NIXL already knows
the range, the direction, and when the range goes cold.</p>
&lt;!-- TODO: drop in your measured numbers here. Something like:
     "On &lt;cluster description&gt;, &lt;workload&gt;, the plugin sustains X GB/s read vs
     Y GB/s for the POSIX plugin on the same mount (N runs, &lt;transfer size&gt;)."
     Even one honest benchmark line moves this issue a long way. --&gt;
<h2>Proposed scope</h2>
<p><strong>In scope for the first PR — <code>IBM_SCALE</code>:</strong></p>

Item | Detail
-- | --
Shared library | libplugin_IBM_SCALE.so
Engine class | nixlScaleEngine
Base class | nixlBackendEngine
Memory types | DRAM_SEG, FILE_SEG
I/O path | Synchronous pread/pwrite with EINTR and short-I/O retry
Hints | GPFS_ACCESS_RANGE on register, GPFS_FREE_RANGE on deregister, fine-grain write sharing hint
Notifications | Not supported (supportsNotif() returns false)
Progress thread | Not required

<h2>Implementation notes</h2>
<p>A few decisions I'd like maintainer input on before they're baked into a PR.</p>
<h3>1. <code>nixlScaleEngine</code> inherits <code>nixlBackendEngine</code> directly, not <code>nixlPosixEngine</code></h3>
<p>The obvious factoring is to subclass <code>nixlPosixEngine</code> and add hints. I did not,
for a reason that may itself be a bug worth fixing upstream:</p>
<p><code>nixlPosixEngine</code> has a private <code>nixlLock io_queue_lock_</code> member whose size
depends on whether <code>absl::Mutex</code> was available at compile time — roughly 200
bytes with abseil present, zero with the stub. Building a plugin against the
NIXL headers without <code>libabsl-dev</code> installed yields a stub <code>nixlLock</code>, so the
plugin's <code>sizeof(nixlPosixEngine)</code> disagrees with the real object inside
<code>libplugin_POSIX.so</code>. The result is a corrupted object layout and a crash on any
call reaching the base engine's private members. It fails at runtime, not at
link time, which makes it unpleasant to diagnose.</p>
<p>Inheriting <code>nixlBackendEngine</code> directly avoids the abseil dependency entirely
and gives a stable layout. This also matches the structural pattern of the
merged Infinia plugin (#1569), so it isn't a novel shape for the tree.</p>
<p><strong>Questions:</strong> Is direct <code>nixlBackendEngine</code> inheritance the pattern you want
for filesystem backends, or would you prefer this plugin sit on <code>nixlPosixEngine</code>
once the layout issue is resolved? And should the abseil-conditional <code>nixlLock</code>
ABI mismatch be split into its own bug report? Happy to file it separately.</p>
<h3>2. <code>nixl::FileFd</code> and abseil</h3>
<p>The plugin needs <code>nixl::FileFd</code> from <code>file_path_mode.h</code> to own file descriptors
the way <code>nixlPosixEngine::registerMem</code> does, but the upstream
<code>file_path_mode.cpp</code> uses <code>absl::StrSplit</code>. My out-of-tree build reimplements
the same parsing with <code>std::string::find</code> to stay abseil-free.</p>
<p>That duplication is fine out-of-tree and clearly wrong in-tree. Preference?
Options as I see them: (a) make <code>file_path_mode.cpp</code>'s path parsing abseil-free
upstream so all plugins share it, (b) make abseil a hard build dependency and
have the plugin use the existing implementation as-is, or (c) something else.
I'm happy to do (a) as a separate prerequisite PR if that's the direction.</p>
<h3>3. Hint failures are counted, never fatal</h3>
<p>Every hint call returns <code>{rc, saved_errno}</code>, with <code>errno</code> captured immediately
after <code>gpfs_fcntl()</code> before anything can clobber it. Results feed atomic
counters split by outcome (ok / <code>ENOTSUP</code> / other), and the engine destructor
dumps the totals. <code>ENOTSUP</code> — the expected result when the plugin runs against a
non-Scale mount or an older release — is counted and ignored, never propagated
as a transfer error. Transfers degrade to plain <code>pread</code>/<code>pwrite</code> rather than
failing.</p>
<p>This means the plugin is functionally safe on a non-Scale filesystem, which
matters for CI (see below), but it does mean a misconfigured deployment silently
loses the optimization. The destructor counter dump is the mitigation. If NIXL's
telemetry interface is the better home for these counters, point me at it and
I'll wire them through instead.</p>
<h3>4. Deregistration frees the registered range only</h3>
<p>Registration metadata carries <code>reg_offset</code> / <code>reg_length</code> so <code>deregisterMem</code> can
issue <code>GPFS_FREE_RANGE</code> for exactly the registered window. Passing
<code>offset=0, length=0</code> would evict the whole file's cache and clobber other
concurrently-registered ranges in the same file, which is a realistic layout for
KV cache.</p>
<h2>Willing to contribute</h2>
<p>Yes — implementation exists and is running out-of-tree; I can open a PR as soon. </p></body></html>

## 评论 (2)

### lluki · 2026-08-20

As GPFS is POSIX compatible (path, permissions, ...), I would prefer it to be an engine that inherits `nixlPosixEngine` . It will help us keep common file related code paths (pathmode for example) in one place.

I'm not sure I'm following your reasoning regarding Abseil - once your plugin is merged, it will be built together with NIXL and these issues should vanish, right? As far as i know absl is required to build NIXL, it just is not required for clients using the NIXL northbound API - the public API should stay free of absl types.


### Anthony24601 · 2026-08-20

Ah yes I think you're right

