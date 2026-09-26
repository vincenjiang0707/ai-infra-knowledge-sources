source: https://docs.nvidia.com/deploy/mps/troubleshooting.html

# Troubleshooting Guide[#](https://docs.nvidia.com#troubleshooting-guide)

## MPS Server Not Accepting New Client Requests[#](https://docs.nvidia.com#mps-server-not-accepting-new-client-requests)

This error indicates that the MPS (Multi-Process Service) server is currently unable to accept new client connections. This is typically a temporary condition caused by one of the following reasons.

**Possible Causes and Recommended Actions**
Server Recovery or Automatic Restart

Cause: The MPS server is recovering from a previous error or automatically restarting due to a kernel-level application failure.

Action: Wait for the server to complete its recovery. If these errors occur repeatedly, investigate the client application for underlying issues.

**Server Initialization in Progress**

Cause: The server is performing initialization operations equivalent to `cuInit() --> cuCtxCreate()`

. On systems with multiple GPUs and no persistence daemon, this can take a significant amount of time. Any client connections attempted during this period will receive this error.

Action: Allow the initialization to complete. To speed up future startups, consider enabling the NVIDIA Persistence Daemon.

**Client Termination Cleanup**

Cause: A `terminate_client`

operation is in progress. During this time, the server restricts new connections to clean up resources from a specific client.

Action: Wait for the cleanup process to finish. This does not affect other connected clients.

**User ID Mismatch Without Multi-User Mode**

Cause: A client with a different user ID is attempting to connect while the server is not started with the `-multiuser-server`

flag.

Action: Either start the MPS server with the `-multiuser-server`

option or ensure that clients are using the same user ID. The default MPS behavior is to restart the server for each unique user ID.