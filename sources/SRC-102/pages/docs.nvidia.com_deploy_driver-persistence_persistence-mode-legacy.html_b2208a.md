source: https://docs.nvidia.com/deploy/driver-persistence/persistence-mode-legacy.html

# Persistence Mode (Legacy)[#](https://docs.nvidia.com#persistence-mode-legacy)

Persistence Mode is the term for a user-settable driver property that keeps a target GPU initialized even
when no clients are connected to it. This solution is near end-of-life and will be eventually deprecated
in favor of the [Persistence Daemon](https://docs.nvidia.com/persistence-daemon.html#persistence-daemon).

Persistence mode can be set using `nvidia-smi`

or programmaticaly via the NVML API.

To enable persistence mode using `nvidia-smi`

(as root):

```
nvidia-smi -i <target gpu> -pm ENABLED
Enabled persistence mode for GPU <target gpu>.
All done.
```

To view current persistence mode using `nvidia-smi`

:

```
nvidia-smi -i <target gpu> - q
==============NVSMI LOG==============
Timestamp : ----
Driver Version : ----
Attached GPUs : ----
GPU 0000:01:00.0
Product Name : ----
Display Mode : ----
Display Active : ----
Persistence Mode : Enabled
Accounting Mode : ----
...
```

## Supported Environments[#](https://docs.nvidia.com#supported-environments)

Drivers: All shipping driver versions

OSes: All standard driver-supported Linux platforms

GPUs: All shipping Data Center, Quadro and GRID products