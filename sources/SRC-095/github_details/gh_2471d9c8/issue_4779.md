# [Issue #4779] [Bug] kubectl-plugin: Integer overflow (G115) and File Descriptor leak in `downloadRayLogFiles`

source: https://github.com/ray-project/kuberay/issues/4779
state: closed | updated: 2026-09-24T02:11:48Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

kubectl-plugin

### What happened + What you expected to happen

In `kubectl-plugin/pkg/cmd/log/log.go`, the `downloadRayLogFiles` function extracts a tar archive containing Ray logs. There are two critical bugs in the extraction loop:

#### 1. Integer Overflow (G115 / gosec)
The `tar.Header.Mode` is of type `int64`. However, `os.FileMode` is an alias for `uint32` on 32-bit platforms. If `header.Mode` is outside the valid range `[0, math.MaxUint32]`, casting it to `os.FileMode` causes a silent integer overflow, truncating the permission bits.
The existing code attempts to guard against this by printing a warning, but it **fails to skip the file** (missing a `continue` statement). It falls through and executes the dangerous cast anyway:

```go
// Existing buggy code:
if header.Mode < 0 || header.Mode > math.MaxUint32 {
    fmt.Fprintf(options.ioStreams.Out, "file mode out side of accceptable value %d skipping file", header.Mode)
    // BUG: Missing `continue` here!
}
// The cast still happens, causing overflow:
outFile, err := os.OpenFile(localFilePath, os.O_CREATE|os.O_RDWR, os.FileMode(header.Mode))
```


#### 2.File Descriptor Leak (FD Leak)
Inside the for loop that iterates over the tar entries, the code opens a file and defers its closure:
```go
// Existing buggy code:
outFile, err := os.OpenFile(...)
defer outFile.Close() // BUG: defers until downloadRayLogFiles returns!
```


### Reproduction script

1. Clone the repository:
   git clone https://github.com/ray-project/kuberay.git
   cd kuberay

2. Lower the process file descriptor limit to make the bug easier to trigger:
   ulimit -n 64

3. Run the following Go test to trigger the bug:
   go test ./kubectl-plugin/pkg/cmd/log/... -v -run TestDownloadRayLogFiles_NoFDLeakWithManyFiles

4. Observe that the test FAILS with the original code:
   - `defer outFile.Close( )` is placed inside a for-loop body
   - In Go, defer fires when the enclosing *function* returns,
     not when the loop iteration ends
   - All file descriptors accumulate until downloadRayLogFiles returns
   - With 300 files in the archive, the process hits the OS FD limit
   - Error: "too many open files" (EMFILE)

Expected: All 300 files extracted successfully with no error.
Actual:   Returns error: "Error creating file: open <path>: too many open files"

### Anything else

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
