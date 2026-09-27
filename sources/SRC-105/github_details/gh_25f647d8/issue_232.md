# [Issue #232] problem to start dcgm_exporter and get metrics

source: https://github.com/NVIDIA/DCGM/issues/232
state: open | updated: 2025-05-22T05:07:38Z
labels: 

## 正文

hi,

i use a nvidia a10 on aws ec2 and run docker compose for dcgm_exporter and the following error. also how can i enable DCGM_FI_PROF_PIPE_FP64_ACTIVE and DCGM_FI_PROF_SM_ACTIVE? do i need to enable some profiling - if so how?

./etc/dcp-metrics-included.csv is from here: https://github.com/NVIDIA/dcgm-exporter/blob/main/etc/dcp-metrics-included.csv

error:
```
docker compose logs dcgm_exporter
dcgm_exporter  | time="2025-05-22T03:57:31Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:31Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:31Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:31Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:31Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:31Z" level=fatal msg="record on line 3: wrong number of fields"
dcgm_exporter  | time="2025-05-22T03:57:32Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:32Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:32Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:32Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:32Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:32Z" level=fatal msg="record on line 3: wrong number of fields"
dcgm_exporter  | time="2025-05-22T03:57:33Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:33Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:33Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:33Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:33Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:33Z" level=fatal msg="record on line 3: wrong number of fields"
dcgm_exporter  | time="2025-05-22T03:57:34Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:34Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:35Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:35Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:35Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:35Z" level=fatal msg="record on line 3: wrong number of fields"
dcgm_exporter  | time="2025-05-22T03:57:36Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:36Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:36Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:36Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:36Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:36Z" level=fatal msg="record on line 3: wrong number of fields"
dcgm_exporter  | time="2025-05-22T03:57:38Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:39Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:39Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:39Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:39Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:39Z" level=fatal msg="record on line 3: wrong number of fields"
dcgm_exporter  | time="2025-05-22T03:57:42Z" level=info msg="Starting dcgm-exporter"
dcgm_exporter  | time="2025-05-22T03:57:43Z" level=info msg="DCGM successfully initialized!"
dcgm_exporter  | time="2025-05-22T03:57:43Z" level=info msg="Collecting DCP Metrics"
dcgm_exporter  | time="2025-05-22T03:57:43Z" level=info msg="No configmap data specified, falling back to metric file /etc/dcp-metrics-included.csv"
dcgm_exporter  | time="2025-05-22T03:57:43Z" level=error msg="Could not read metrics file '/etc/dcp-metrics-included.csv': record on line 3: wrong number of fields\n"
dcgm_exporter  | time="2025-05-22T03:57:43Z" level=fatal msg="record on line 3: wrong number of fields"
```

docker-compose.yaml:
```
services:
  dcgm_exporter:
    image: nvcr.io/nvidia/k8s/dcgm-exporter:latest
    container_name: dcgm_exporter
    restart: unless-stopped
    ports:
      - "9400:9400"
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
    cap_add:
      - SYS_ADMIN
    runtime: nvidia
    volumes:
      - ./etc/dcp-metrics-included.csv:/etc/dcp-metrics-included.csv:ro
    command:
      - "-f"
      - "/etc/dcp-metrics-included.csv"
```

nvidia-smi dmon:
```
nvidia-smi dmon
# gpu    pwr  gtemp  mtemp     sm    mem    enc    dec    jpg    ofa   mclk   pclk 
# Idx      W      C      C      %      %      %      %      %      %    MHz    MHz 
    0     86     33      -     30     27      0      0      0      0   6250   1710 
    0    267     39      -    100     95      0      0      0      0   6250   1710 
    0    280     41      -     85     80      0      0      0      0   6250   1710 
    0    284     42      -     98     93      0      0      0      0   6250   1710 
```

available metrics:
```
dcgmi dmon -l
________________________________________________________________________________________________________________________
Long Name                                                                                 Short Name          Field ID  
________________________________________________________________________________________________________________________
driver_version                                                                             DRVER               1
nvml_version                                                                               NVVER               2
process_name                                                                               PRNAM               3
device_count                                                                               DVCNT               4
cuda_driver_version                                                                        CDVER               5
name                                                                                       DVNAM               50
brand                                                                                      DVBRN               51
nvml_index                                                                                 NVIDX               52
serial_number                                                                              SRNUM               53
uuid                                                                                       UUID#               54
minor_number                                                                               MNNUM               55
oem_inforom_version                                                                        OEMVR               56
pci_busid                                                                                  PCBID               57
pci_combined_id                                                                            PCCID               58
pci_subsys_id                                                                              PCSID               59
system_topology_pci                                                                        STVCI               60
system_topology_nvlink                                                                     STNVL               61
system_affinity                                                                            SYSAF               62
cuda_compute_capability                                                                    DVCCC               63
compute_mode                                                                               CMMOD               65
persistance_mode                                                                           PMMOD               66
mig_mode                                                                                   MGMOD               67
cuda_visible_devices                                                                       CUVID               68
mig_max_slices                                                                             MIGMS               69
cpu_affinity_0                                                                             CAFF0               70
cpu_affinity_1                                                                             CAFF1               71
cpu_affinity_2                                                                             CAFF2               72
cpu_affinity_3                                                                             CAFF3               73
cc_mode                                                                                    CCMOD               74
mig_attributes                                                                             MIGATT              75
mig_gi_info                                                                                MIGGIINFO           76
mig_ci_info                                                                                MIGCIINFO           77
ecc_inforom_version                                                                        EIVER               80
power_inforom_version                                                                      PIVER               81
inforom_image_version                                                                      IIVER               82
inforom_config_checksum                                                                    CCSUM               83
inforom_config_valid                                                                       ICVLD               84
vbios_version                                                                              VBVER               85
mem_affinity_0                                                                             MAFF0               86
mem_affinity_1                                                                             MAFF1               87
mem_affinity_2                                                                             MAFF2               88
mem_affinity_3                                                                             MAFF3               89
bar1_total                                                                                 B1TTL               90
sync_boost                                                                                 SYBST               91
bar1_used                                                                                  B1USE               92
bar1_free                                                                                  B1FRE               93
sm_clock                                                                                   SMCLK               100
memory_clock                                                                               MMCLK               101
video_clock                                                                                VICLK               102
sm_app_clock                                                                               SACLK               110
mem_app_clock                                                                              MACLK               111
current_clock_throttle_reasons                                                             DVCCTR              112
sm_max_clock                                                                               SMMAX               113
memory_max_clock                                                                           MMMAX               114
video_max_clock                                                                            VIMAX               115
autoboost                                                                                  ATBST               120
supported_clocks                                                                           SPCLK               130
memory_temp                                                                                MMTMP               140
gpu_temp                                                                                   TMPTR               150
gpu_mem_max_op_temp                                                                        GMMOT               151
gpu_max_op_temp                                                                            GGMOT               152
power_usage                                                                                POWER               155
total_energy_consumption                                                                   TOTEC               156
power_usage_instant                                                                        POWINST             157
slowdown_temp                                                                              SDTMP               158
shutdown_temp                                                                              SHTMP               159
power_management_limit                                                                     PMLMT               160
power_management_limit_min                                                                 PMMIN               161
power_management_limit_max                                                                 PMMAX               162
power_management_limit_default                                                             PMDEF               163
enforced_power_limit                                                                       EPLMT               164
pstate                                                                                     PSTAT               190
fan_speed                                                                                  FANSP               191
pcie_tx_throughput                                                                         TXTPT               200
pcie_rx_throughput                                                                         RXTPT               201
pcie_replay_counter                                                                        RPCTR               202
gpu_utilization                                                                            GPUTL               203
mem_copy_utilization                                                                       MCUTL               204
accounting_data                                                                            ACCDT               205
enc_utilization                                                                            ECUTL               206
dec_utilization                                                                            DCUTL               207
mem_util_samples                                                                           MUSAM               210
gpu_util_samples                                                                           GUSAM               211
graphics_pids                                                                              GPIDS               220
compute_pids                                                                               CMPID               221
xid_errors                                                                                 XIDER               230
pcie_max_link_gen                                                                          PCIMG               235
pcie_max_link_width                                                                        PCIMW               236
pcie_link_gen                                                                              PCILG               237
pcie_link_width                                                                            PCILW               238
power_violation                                                                            PVIOL               240
thermal_violation                                                                          TVIOL               241
sync_boost_violation                                                                       SBVIO               242
board_limit_violation                                                                      BLVIO               243
low_util_violation                                                                         LUVIO               244
reliability_violation                                                                      RVIOL               245
app_clock_violation                                                                        TAPCV               246
base_clock_violation                                                                       TAPBC               247
fb_total                                                                                   FBTTL               250
fb_free                                                                                    FBFRE               251
fb_used                                                                                    FBUSD               252
fb_resv                                                                                    FBRSV               253
fb_USDP                                                                                    FBUSP               254
c2c_link_count                                                                             C2CLC               285
c2c_link_status                                                                            C2CST               286
c2c_max_bandwidth                                                                          C2CMAXBW            287
ecc                                                                                        ECCUR               300
ecc_pending                                                                                ECPEN               301
ecc_sbe_volatile_total                                                                     ESVTL               310
ecc_dbe_volatile_total                                                                     EDVTL               311
ecc_sbe_aggregate_total                                                                    ESATL               312
ecc_dbe_aggregate_total                                                                    EDATL               313
ecc_sbe_volatile_l1                                                                        ESVL1               314
ecc_dbe_volatile_l1                                                                        EDVL1               315
ecc_sbe_volatile_l2                                                                        ESVL2               316
ecc_dbe_volatile_l2                                                                        EDVL2               317
ecc_sbe_volatile_device                                                                    ESVDV               318
ecc_dbe_volatile_device                                                                    EDVDV               319
ecc_sbe_volatile_register                                                                  ESVRG               320
ecc_dbe_volatile_register                                                                  EDVRG               321
ecc_sbe_volatile_texture                                                                   ESVTX               322
ecc_dbe_volatile_texture                                                                   EDVTX               323
ecc_sbe_aggregate_l1                                                                       ESAL1               324
ecc_dbe_aggregate_l1                                                                       EDAL1               325
ecc_sbe_aggregate_l2                                                                       ESAL2               326
ecc_dbe_aggregate_l2                                                                       EDAL2               327
ecc_sbe_aggregate_device                                                                   ESADV               328
ecc_dbe_aggregate_device                                                                   EDADV               329
ecc_sbe_aggregate_register                                                                 ESARG               330
ecc_dbe_aggregate_register                                                                 EDARG               331
ecc_sbe_aggregate_texture                                                                  ESATX               332
ecc_dbe_aggregate_texture                                                                  EDATX               333
remap_rows_avail_max                                                                       RRAM                385
remap_rows_avail_high                                                                      RRAH                386
remap_rows_avail_partial                                                                   RRAP                387
remap_rows_avail_low                                                                       RRAL                388
remap_rows_avail_none                                                                      RRAN                389
retired_pages_sbe                                                                          RPSBE               390
retired_pages_dbe                                                                          RPDBE               391
retired_pages_pending                                                                      RPPEN               392
uncorrectable_remapped_rows                                                                URMPS               393
correctable_remapped_rows                                                                  CRMPS               394
row_remap_failure                                                                          RRF                 395
row_remap_pending                                                                          RRP                 396
nvlink_flit_crc_error_count_l0                                                             NFEL0               400
nvlink_flit_crc_error_count_l1                                                             NFEL1               401
nvlink_flit_crc_error_count_l2                                                             NFEL2               402
nvlink_flit_crc_error_count_l3                                                             NFEL3               403
nvlink_flit_crc_error_count_l4                                                             NFEL4               404
nvlink_flit_crc_error_count_l5                                                             NFEL5               405
nvlink_flit_crc_error_count_l12                                                            NFEL12              406
nvlink_flit_crc_error_count_l13                                                            NFEL13              407
nvlink_flit_crc_error_count_l14                                                            NFEL14              408
nvlink_flit_crc_error_count_total                                                          NFELT               409
nvlink_data_crc_error_count_l0                                                             NDEL0               410
nvlink_data_crc_error_count_l1                                                             NDEL1               411
nvlink_data_crc_error_count_l2                                                             NDEL2               412
nvlink_data_crc_error_count_l3                                                             NDEL3               413
nvlink_data_crc_error_count_l4                                                             NDEL4               414
nvlink_data_crc_error_count_l5                                                             NDEL5               415
nvlink_data_crc_error_count_l12                                                            NDEL12              416
nvlink_data_crc_error_count_l13                                                            NDEL13              417
nvlink_data_crc_error_count_l14                                                            NDEL14              418
nvlink_data_crc_error_count_total                                                          NDELT               419
nvlink_replay_error_count_l0                                                               NREL0               420
nvlink_replay_error_count_l1                                                               NREL1               421
nvlink_replay_error_count_l2                                                               NREL2               422
nvlink_replay_error_count_l3                                                               NREL3               423
nvlink_replay_error_count_l4                                                               NREL4               424
nvlink_replay_error_count_l5                                                               NREL5               425
nvlink_replay_error_count_l12                                                              NREL12              426
nvlink_replay_error_count_l13                                                              NREL13              427
nvlink_replay_error_count_l14                                                              NREL14              428
nvlink_replay_error_count_total                                                            NRELT               429
nvlink_recovery_error_count_l0                                                             NRCL0               430
nvlink_recovery_error_count_l1                                                             NRCL1               431
nvlink_recovery_error_count_l2                                                             NRCL2               432
nvlink_recovery_error_count_l3                                                             NRCL3               433
nvlink_recovery_error_count_l4                                                             NRCL4               434
nvlink_recovery_error_count_l5                                                             NRCL5               435
nvlink_recovery_error_count_l12                                                            NRCL12              436
nvlink_recovery_error_count_l13                                                            NRCL13              437
nvlink_recovery_error_count_l14                                                            NRCL14              438
nvlink_recovery_error_count_total                                                          NRCLT               439
nvlink_bandwidth_l0                                                                        NBWL0               440
nvlink_bandwidth_l1                                                                        NBWL1               441
nvlink_bandwidth_l2                                                                        NBWL2               442
nvlink_bandwidth_l3                                                                        NBWL3               443
nvlink_bandwidth_l4                                                                        NBWL4               444
nvlink_bandwidth_l5                                                                        NBWL5               445
nvlink_bandwidth_l12                                                                       NBWL12              446
nvlink_bandwidth_l13                                                                       NBWL13              447
nvlink_bandwidth_l14                                                                       NBWL14              448
nvlink_bandwidth_total                                                                     NBWLT               449
gpu_nvlink_errors                                                                          GNVERR              450
nvlink_flit_crc_error_count_l6                                                             NFEL6               451
nvlink_flit_crc_error_count_l7                                                             NFEL7               452
nvlink_flit_crc_error_count_l8                                                             NFEL8               453
nvlink_flit_crc_error_count_l9                                                             NFEL9               454
nvlink_flit_crc_error_count_l10                                                            NFEL10              455
nvlink_flit_crc_error_count_l11                                                            NFEL11              456
nvlink_data_crc_error_count_l6                                                             NDEL6               457
nvlink_data_crc_error_count_l7                                                             NDEL7               458
nvlink_data_crc_error_count_l8                                                             NDEL8               459
nvlink_data_crc_error_count_l9                                                             NDEL9               460
nvlink_data_crc_error_count_l10                                                            NDEL10              461
nvlink_data_crc_error_count_l11                                                            NDEL11              462
nvlink_replay_error_count_l6                                                               NREL6               463
nvlink_replay_error_count_l7                                                               NREL7               464
nvlink_replay_error_count_l8                                                               NREL8               465
nvlink_replay_error_count_l9                                                               NREL9               466
nvlink_replay_error_count_l10                                                              NREL10              467
nvlink_replay_error_count_l11                                                              NREL11              468
nvlink_recovery_error_count_l6                                                             NRCL6               469
nvlink_recovery_error_count_l7                                                             NRCL7               470
nvlink_recovery_error_count_l8                                                             NRCL8               471
nvlink_recovery_error_count_l9                                                             NRCL9               472
nvlink_recovery_error_count_l10                                                            NRCL10              473
nvlink_recovery_error_count_l11                                                            NRCL11              474
nvlink_bandwidth_l6                                                                        NBWL6               475
nvlink_bandwidth_l7                                                                        NBWL7               476
nvlink_bandwidth_l8                                                                        NBWL8               477
nvlink_bandwidth_l9                                                                        NBWL9               478
nvlink_bandwidth_l10                                                                       NBWL10              479
nvlink_bandwidth_l11                                                                       NBWL11              480
nvlink_flit_crc_error_count_l15                                                            NFEL15              481
nvlink_flit_crc_error_count_l16                                                            NFEL16              482
nvlink_flit_crc_error_count_l17                                                            NFEL17              483
nvlink_data_crc_error_count_l15                                                            NDEL15              484
nvlink_data_crc_error_count_l16                                                            NDEL16              485
nvlink_data_crc_error_count_l17                                                            NDEL17              486
nvlink_replay_error_count_l15                                                              NREL15              487
nvlink_replay_error_count_l16                                                              NREL16              488
nvlink_replay_error_count_l17                                                              NREL17              489
nvlink_recovery_error_count_l15                                                            NRCL15              491
nvlink_recovery_error_count_l16                                                            NRCL16              492
nvlink_recovery_error_count_l17                                                            NRCL17              493
nvlink_bandwidth_l15                                                                       NBWL15              494
nvlink_bandwidth_l16                                                                       NBWL16              495
nvlink_bandwidth_l17                                                                       NBWL17              496
virtualization_mode                                                                        VMODE               500
supported_type_info                                                                        SPINF               501
creatable_vgpu_type_ids                                                                    CGPID               502
active_vgpu_instance_ids                                                                   VGIID               503
vgpu_instance_utilizations                                                                 VIUTL               504
vgpu_instance_per_process_utilization                                                      VIPPU               505
enc_stats                                                                                  ENSTA               506
fbc_stats                                                                                  FBCSTA              507
fbc_sessions_info                                                                          FBCINF              508
vgpu_type_ids                                                                              VTID                509
vgpu_type_info                                                                             VTPINF              510
vgpu_type_name                                                                             VTPNM               511
vgpu_type_class                                                                            VTPCLS              512
vgpu_type_license                                                                          VTPLC               513
vgpu_instance_vm_id                                                                        VVMID               520
vgpu_instance_vm_name                                                                      VMNAM               521
vgpu_instance_type                                                                         VITYP               522
vgpu_instance_uuid                                                                         VUUID               523
vgpu_instance_driver_version                                                               VDVER               524
vgpu_instance_memory_usage                                                                 VMUSG               525
vgpu_instance_license_status                                                               VLCST               526
vgpu_instance_frame_rate_limit                                                             VFLIM               527
vgpu_instance_enc_stats                                                                    VSTAT               528
vgpu_instance_enc_sessions_info                                                            VSINF               529
vgpu_instance_fbc_stats                                                                    VFSTAT              530
vgpu_instance_fbc_sessions_info                                                            VFINF               531
vgpu_instance_license_state                                                                VLCIST              532
vgpu_instance_pci_id                                                                       VPCIID              533
vgpu_instance_gpu_instance_id                                                              VGII                534
nvswitch_voltage_mvolt                                                                     SWVOLT              701
nvswitch_current_iddq                                                                      SWCUR               702
nvswitch_current_iddq_rev                                                                  SCIDDQ              703
nvswitch_current_iddq_dvdd                                                                 SCDVDD              704
nvswitch_power_vdd                                                                         SWPOWV              705
nvswitch_power_dvdd                                                                        SWPOWD              706
nvswitch_power_hvdd                                                                        SWPOWH              707
nvswitch_link_bandwidth_tx                                                                 SWLNKTX             780
nvswitch_link_bandwidth_rx                                                                 SWLNKRX             781
nvswitch_link_fatal_errors                                                                 SWLNKFE             782
nvswitch_link_non_fatal_errors                                                             SWLNKNF             783
nvswitch_link_replay_errors                                                                SWLNKRP             784
nvswitch_link_recovery_errors                                                              SWLNKRC             785
nvswitch_link_flit_errors                                                                  SWLNKFL             786
nvswitch_link_crc_errors                                                                   SWLNKCR             787
nvswitch_link_ecc_errors                                                                   SWLNKEC             788
nvswitch_link_latency_low_vc0                                                              SWVCLL0             789
nvswitch_link_latency_low_vc1                                                              SWVCLL1             790
nvswitch_link_latency_low_vc2                                                              SWVCLL2             791
nvswitch_link_latency_low_vc                                                               SWVCLL3             792
nvswitch_link_latency_medium_vc0                                                           SWVCLM0             793
nvswitch_link_latency_medium_vc1                                                           SWVCLM1             794
nvswitch_link_latency_medium_vc2                                                           SWVCLM2             795
nvswitch_link_latency_medium_vc3                                                           SWVCLM3             796
nvswitch_link_latency_high_vc0                                                             SWVCLH0             797
nvswitch_link_latency_high_vc1                                                             SWVCLH1             798
nvswitch_link_latency_high_vc2                                                             SWVCLH2             799
nvswitch_link_latency_high_vc3                                                             SWVCLH3             800
nvswitch_link_latency_panic_vc0                                                            SWVCLP0             801
nvswitch_link_latency_panic_vc1                                                            SWVCLP1             802
nvswitch_link_latency_panic_vc2                                                            SWVCLP2             803
nvswitch_link_latency_panic_vc3                                                            SWVCLP3             804
nvswitch_link_latency_count_vc0                                                            SWVCLC0             805
nvswitch_link_latency_count_vc1                                                            SWVCLC1             806
nvswitch_link_latency_count_vc2                                                            SWVCLC2             807
nvswitch_link_latency_count_vc3                                                            SWVCLC3             808
nvswitch_link_crc_errors_lane0                                                             SWLACR0             809
nvswitch_link_crc_errors_lane1                                                             SWLACR1             810
nvswitch_link_crc_errors_lane2                                                             SWLACR2             811
nvswitch_link_crc_errors_lane3                                                             SWLACR3             812
nvswitch_link_ecc_errors_lane0                                                             SWLAEC0             813
nvswitch_link_ecc_errors_lane1                                                             SWLAEC1             814
nvswitch_link_ecc_errors_lane2                                                             SWLAEC2             815
nvswitch_link_ecc_errors_lane3                                                             SWLAEC3             816
nvswitch_fatal_error                                                                       SEN00               856
nvswitch_non_fatal_error                                                                   SEN01               857
nvswitch_current_temperature                                                               TMP01               858
nvswitch_slowdown_temperature                                                              TMP02               859
nvswitch_shutdown_temperature                                                              TMP03               860
nvswitch_bandwidth_tx                                                                      SWTX                861
nvswitch_bandwidth_rx                                                                      SWRX                862
nvswitch_physical_id                                                                       SWPHID              863
nvswitch_reset_required                                                                    SWFRMVER            864
nvlink_id                                                                                  LNKID               865
nvswitch_pcie_dom                                                                          SWPCIEDOM           866
nvswitch_pcie_bus                                                                          SWPCIEBUS           867
nvswitch_pcie_dev                                                                          SWPCIEDEV           868
nvswitch_pcie_fun                                                                          SWPCIEFUN           869
nvswitch_nvlink_status                                                                     SWNVLNKST           870
nvswitch_nvlink_dev_type                                                                   SWNVLNKDT           871
link_pcie_remote_dom                                                                       LNKDOM              872
link_pcie_remote_bus                                                                       LNKBUS              873
link_pcie_remote_dev                                                                       LNKDEV              874
link_pcie_remote_func                                                                      LNKFNC              875
link_dev_link_id                                                                           SWNVLNKID           876
link_dev_link_sid                                                                          SWNVLNSID           877
link_dev_link_uuid                                                                         SWNVLNUID           878
gr_engine_active                                                                           GRACT               1001
sm_active                                                                                  SMACT               1002
sm_occupancy                                                                               SMOCC               1003
tensor_active                                                                              TENSO               1004
dram_active                                                                                DRAMA               1005
fp64_active                                                                                FP64A               1006
fp32_active                                                                                FP32A               1007
fp16_active                                                                                FP16A               1008
pcie_tx_bytes                                                                              PCITX               1009
pcie_rx_bytes                                                                              PCIRX               1010
nvlink_tx_bytes                                                                            NVLTX               1011
nvlink_rx_bytes                                                                            NVLRX               1012
tensor_imma_active                                                                         TIMMA               1013
tensor_hmma_active                                                                         THMMA               1014
tensor_dfma_active                                                                         TDFMA               1015
integer_active                                                                             INTAC               1016
nvdec0_active                                                                              NVDEC0              1017
nvdec1_active                                                                              NVDEC1              1018
nvdec2_active                                                                              NVDEC2              1019
nvdec3_active                                                                              NVDEC3              1020
nvdec4_active                                                                              NVDEC4              1021
nvdec5_active                                                                              NVDEC5              1022
nvdec6_active                                                                              NVDEC6              1023
nvdec7_active                                                                              NVDEC7              1024
nvjpg0_active                                                                              NVJPG0              1025
nvjpg1_active                                                                              NVJPG1              1026
nvjpg2_active                                                                              NVJPG2              1027
nvjpg3_active                                                                              NVJPG3              1028
nvjpg4_active                                                                              NVJPG4              1029
nvjpg5_active                                                                              NVJPG5              1030
nvjpg6_active                                                                              NVJPG6              1031
nvjpg7_active                                                                              NVJPG7              1032
nvofa0_active                                                                              NVOFA0              1033
nvlink_l0_tx_bytes                                                                         NVL0T               1040
nvlink_l0_rx_bytes                                                                         NVL0R               1041
nvlink_l1_tx_bytes                                                                         NVL1T               1042
nvlink_l1_rx_bytes                                                                         NVL1R               1043
nvlink_l2_tx_bytes                                                                         NVL2T               1044
nvlink_l2_rx_bytes                                                                         NVL2R               1045
nvlink_l3_tx_bytes                                                                         NVL3T               1046
nvlink_l3_rx_bytes                                                                         NVL3R               1047
nvlink_l4_tx_bytes                                                                         NVL4T               1048
nvlink_l4_rx_bytes                                                                         NVL4R               1049
nvlink_l5_tx_bytes                                                                         NVL5T               1050
nvlink_l5_rx_bytes                                                                         NVL5R               1051
nvlink_l6_tx_bytes                                                                         NVL6T               1052
nvlink_l6_rx_bytes                                                                         NVL6R               1053
nvlink_l7_tx_bytes                                                                         NVL7T               1054
nvlink_l7_rx_bytes                                                                         NVL7R               1055
nvlink_l8_tx_bytes                                                                         NVL8T               1056
nvlink_l8_rx_bytes                                                                         NVL8R               1057
nvlink_l9_tx_bytes                                                                         NVL9T               1058
nvlink_l9_rx_bytes                                                                         NVL9R               1059
nvlink_l10_tx_bytes                                                                        NVL10T              1060
nvlink_l10_rx_bytes                                                                        NVL10R              1061
nvlink_l11_tx_bytes                                                                        NVL11T              1062
nvlink_l11_rx_bytes                                                                        NVL11R              1063
nvlink_l12_tx_bytes                                                                        NVL12T              1064
nvlink_l12_rx_bytes                                                                        NVL12R              1065
nvlink_l13_tx_bytes                                                                        NVL13T              1066
nvlink_l13_rx_bytes                                                                        NVL13R              1067
nvlink_l14_tx_bytes                                                                        NVL14T              1068
nvlink_l14_rx_bytes                                                                        NVL14R              1069
nvlink_l15_tx_bytes                                                                        NVL15T              1070
nvlink_l15_rx_bytes                                                                        NVL15R              1071
nvlink_l16_tx_bytes                                                                        NVL16T              1072
nvlink_l16_rx_bytes                                                                        NVL16R              1073
nvlink_l17_tx_bytes                                                                        NVL17T              1074
nvlink_l17_rx_bytes                                                                        NVL17R              1075
cpu_utilization_total                                                                      CPUUT               1100
cpu_utilization_user                                                                       CPUUU               1101
cpu_utilization_nice                                                                       CPUUN               1102
cpu_utilization_sys                                                                        CPUUS               1103
cpu_utilization_irq                                                                        CPUUI               1104
cpu_temp                                                                                   CPUTP               1110
cpu_temp_warn                                                                              CPUTW               1111
cpu_temp_crit                                                                              CPUTC               1112
cpu_clock                                                                                  CPUCL               1120
cpu_power_utilization                                                                      CPUPU               1130
cpu_power_limit                                                                            CPUPL               1131
sysio_power_utilization                                                                    SIOPU               1132
module_power_utilization                                                                   MODPU               1133
cpu_vendor_name                                                                            CPUVN               1140
cpu_model_name                                                                             CPUMN               1141
```

nvidia-smi -q output:
```
nvidia-smi -q

==============NVSMI LOG==============

Timestamp                                 : Thu May 22 04:10:23 2025
Driver Version                            : 535.247.01
CUDA Version                              : 12.2

Attached GPUs                             : 1
GPU 00000000:00:1E.0
    Product Name                          : NVIDIA A10G
    Product Brand                         : NVIDIA
    Product Architecture                  : Ampere
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Disabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1654321021062
    GPU UUID                              : GPU-5468ba27-3fa8-325a-92f3-2fb0645c07cf
    Minor Number                          : 0
    VBIOS Version                         : 94.02.75.00.01
    MultiGPU Board                        : No
    Board ID                              : 0x1e
    Board Part Number                     : 900-2G133-A840-000
    GPU Part Number                       : 2237-892-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0210.00.04
        OEM Object                        : 2.0
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GSP Firmware Version                  : N/A
    GPU Virtualization Mode
        Virtualization Mode               : Pass-Through
        Host VGPU Mode                    : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x1E
        Domain                            : 0x0000
        Device Id                         : 0x223710DE
        Bus Id                            : 00000000:00:1E.0
        Sub System Id                     : 0x152F10DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 4
                Device Current            : 4
                Device Max                : 4
                Host Max                  : N/A
            Link Width
                Max                       : 16x
                Current                   : 8x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s

        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 0 %
    Performance State                     : P0
    Clocks Event Reasons
        Idle                              : Not Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Not Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 23028 MiB
        Reserved                          : 304 MiB
        Used                              : 8722 MiB
        Free                              : 14001 MiB
    BAR1 Memory Usage
        Total                             : 32768 MiB
        Used                              : 4 MiB
        Free                              : 32764 MiB
    Conf Compute Protected Memory Usage
        Total                             : 0 MiB
        Used                              : 0 MiB
        Free                              : 0 MiB
    Compute Mode                          : Default
    Utilization
        Gpu                               : 0 %
        Memory                            : 0 %
        Encoder                           : 0 %
        Decoder                           : 0 %
        JPEG                              : 0 %
        OFA                               : 0 %
    Encoder Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    FBC Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    ECC Mode
        Current                           : Enabled
        Pending                           : Enabled
    ECC Errors
        Volatile
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
        Aggregate
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 1
            DRAM Uncorrectable            : 0
            SRAM Threshold Exceeded       : No
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : 0
            SRAM SM                       : 0
            SRAM Microcontroller          : 0
            SRAM PCIE                     : 0
            SRAM Other                    : 0
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows
        Correctable Error                 : 0
        Uncorrectable Error               : 0
        Pending                           : No
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 27 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 88 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 60.30 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
    Module Power Readings
        Power Draw                        : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : 1710 MHz
        SM                                : 1710 MHz
        Memory                            : 6250 MHz
        Video                             : 1500 MHz
    Applications Clocks
        Graphics                          : 1710 MHz
        Memory                            : 6251 MHz
    Default Applications Clocks
        Graphics                          : 1710 MHz
        Memory                            : 6251 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1710 MHz
        SM                                : 1710 MHz
        Memory                            : 6251 MHz
        Video                             : 1500 MHz
    Max Customer Boost Clocks
        Graphics                          : 1710 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 956.250 mV
    Fabric
        State                             : N/A
        Status                            : N/A
    Processes
        GPU instance ID                   : N/A
        Compute instance ID               : N/A
        Process ID                        : 3402470
            Type                          : C
            Name                          : 
            Used GPU Memory               : 8716 MiB
```

cc @nikkon-dev 

## 评论 (1)

### geraldstanje1 · 2025-05-22

and here is :nvidia-smi:
```
nvidia-smi
Thu May 22 04:11:56 2025       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.247.01             Driver Version: 535.247.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A10G                    Off | 00000000:00:1E.0 Off |                    0 |
|  0%   26C    P0              60W / 300W |   8722MiB / 23028MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
```

and also see:
```
dcgmi profile --list       
+----------------+----------+------------------------------------------------------+
| Group.Subgroup | Field ID | Field Tag                                            |
+----------------+----------+------------------------------------------------------+
| A.1            | 1002     | sm_active                                            |
| A.1            | 1003     | sm_occupancy                                         |
| A.1            | 1004     | tensor_active                                        |
| A.1            | 1007     | fp32_active                                          |
| A.3            | 1008     | fp16_active                                          |
| B.0            | 1005     | dram_active                                          |
| C.0            | 1009     | pcie_tx_bytes                                        |
| C.0            | 1010     | pcie_rx_bytes                                        |
| D.0            | 1001     | gr_engine_active                                     |
| E.0            | 1011     | nvlink_tx_bytes                                      |
| E.0            | 1012     | nvlink_rx_bytes                                      |
+----------------+----------+------------------------------------------------------+
```

started:
```
dcgmi stats --host localhost -g 1 -e
Successfully started process watches.
```

triton inference server running in a docker container (here the ps axnn output on the host):
```
2122779 pts/0    Ssl+   2:36 tritonserver --model-repository=/models --model-control-mode=EXPLICIT --load-model ensemble-model --log-warning=1 --log-error=1 --metrics-config histogram_latencies=true --metrics-config summary_latencies=true --allow-metrics=true --allow-gpu-metrics=true --allow-cpu-metrics=true
2123443 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_4cba150c-9445-4220-a202-8af0160a14f1 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_5 DEFAULT
2123444 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_18d909fc-d9c4-477f-ae92-c2c7c3d7383f 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_7 DEFAULT
2123445 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_da508b70-8538-4a92-9c6e-c27f1aaec908 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_9 DEFAULT
2123450 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_a6502a0c-1130-46b1-bb5a-a7346d147160 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_0 DEFAULT
2123460 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_68242f99-ee3e-4b58-a698-b9db9e5daf8b 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_8 DEFAULT
2123483 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_5d617adf-f888-40a2-9bff-04a3f35b53a5 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_2 DEFAULT
2123499 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_4db563c4-568d-4f59-9408-5b7de707f892 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_6 DEFAULT
2123507 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_d1a08521-af8e-4f97-8577-fd1ca0e33f5e 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_1 DEFAULT
2123515 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_ece31581-a576-4ed1-8bc1-3087349a1505 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_3 DEFAULT
2123540 pts/0    Sl+    0:03 /opt/tritonserver/backends/python/triton_python_backend_stub /models/post-processing/1/model.py triton_python_backend_shm_region_352209e0-d897-405a-b32c-5358116efadb 1048576 1048576 1 /opt/tritonserver/backends/python 336 post-processing_0_4 DEFAULT
2124073 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_33c18d21-5138-43e1-886a-48ffeadd4357 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_0 DEFAULT
2124083 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_0f88db6c-7670-4c13-99de-f0d02cedc38a 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_3 DEFAULT
2124091 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_cbbc3c10-6331-470a-b231-c669ef78009b 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_5 DEFAULT
2124092 pts/0    Sl+    0:11 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_5b419ec5-9f19-417a-bbd9-7306cc72a96e 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_1 DEFAULT
2124093 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_5eca62c3-dccd-47ff-9da6-8f7662429f85 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_2 DEFAULT
2124095 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_b70530e9-92d6-4f5f-bb1d-34d97481bdf2 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_6 DEFAULT
2124104 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_57097799-e550-4424-b8cb-92a9d9955b4d 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_4 DEFAULT
2124116 pts/0    Sl+    0:11 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_c6a0036f-99c8-4f09-9884-d45b8a09a8b9 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_7 DEFAULT
2124134 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_c513ddef-cac0-4911-9043-a6bbf6c363f3 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_9 DEFAULT
2124144 pts/0    Sl+    0:10 /opt/tritonserver/backends/python/triton_python_backend_stub /models/tokenize/1/model.py triton_python_backend_shm_region_c9bca646-4a6a-4077-b12d-68060abc6f7e 1048576 1048576 1 /opt/tritonserver/backends/python 336 tokenize_0_8 DEFAULT
```

```
dcgmi stats --host localhost -g 1 -p 2122651 -v 
Error: Unable to get information for process with PID 2122651. Return: No data is available.
```
