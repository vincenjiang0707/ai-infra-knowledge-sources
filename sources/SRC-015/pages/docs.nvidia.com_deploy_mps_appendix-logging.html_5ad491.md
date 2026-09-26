source: https://docs.nvidia.com/deploy/mps/appendix-logging.html

# Appendix: Logging[#](https://docs.nvidia.com#appendix-logging)

The MPS control daemon maintains a `control.log`

file which contains the status of its
MPS servers, user commands issued and their result, and startup and shutdown notices for
the daemon. Each MPS server maintains a `server.log`

file containing its startup and
shutdown information and the status of its clients.

## Log File Locations[#](https://docs.nvidia.com#log-file-locations)

By default, these log files are stored in `/var/log/nvidia-mps`

. The
`CUDA_MPS_LOG_DIRECTORY`

environment variable can be used to override the location; it
should be set in the MPS control daemon’s environment and is automatically inherited by
any MPS servers it launches. Refer to [Appendix: Environment Variables](https://docs.nvidia.com/appendix-environment-variables.html#environment-variables) for details.

```
$CUDA_MPS_LOG_DIRECTORY/control.log
$CUDA_MPS_LOG_DIRECTORY/server.log
```

```
$CUDA_MPS_LOG_DIRECTORY/control.log
$CUDA_MPS_LOG_DIRECTORY/<server-name>/server.log
```

These log files are typically only visible to users with administrative privileges unless
`CUDA_MPS_LOG_DIRECTORY`

was set up elsewhere.

On Tegra platforms, there is no default directory setting for storing the log files. MPS
will remain operational without the user setting `CUDA_MPS_LOG_DIRECTORY`

; however, in
such instances, MPS logs will not be available.