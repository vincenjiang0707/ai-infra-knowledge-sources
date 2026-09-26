# turn-your-latest-observations-into-timely-weather-decisions-with-nvidia-earth-2

source: https://developer.nvidia.com/blog/turn-your-latest-observations-into-timely-weather-decisions-with-nvidia-earth-2/

Weather-sensitive industries increasingly have access to observations that offer an earlier, more local view of changing conditions. Energy companies collect measurements across wind and solar assets, emergency management teams rely on radar and local sensors, and satellite providers continuously observe the Earth. This data helps organizations understand and manage physical risk across sectors such as capital markets, insurance, agriculture, and logistics.

With the AI data assimilation tools in NVIDIA Earth-2, you can process these observations more efficiently. By incorporating proprietary or third-party data, you can use these tools to issue forecasts more frequently, keep estimates aligned with real-time conditions, and tailor your forecasting pipeline to specific regions and applications.

This tutorial covers two techniques:

- Constraining diffusion models with point observations, typically used for regional models.
- Assimilating disparate datasets into a consistent state, typically used for global models.

## Prerequisites

For this tutorial, you will need:

- A development environment with
[Earth2Studio](https://nvidia.github.io/earth2studio/main/)installed - An NVIDIA RTX PRO or data center GPU
- A basic knowledge of Python
- Approximately 30 minutes

## Improve regional forecasts with observations

You might run a regional weather forecasting pipeline for managing energy production and demand, drawing observations from wind and solar parks, transmission corridors, or densely populated areas. With AI data assimilation, you can use these observations to constrain your forecast where local accuracy matters most, helping you improve operational decisions. The same techniques can support other sectors using observations from production sites, event venues, logistics networks, or other assets where local conditions directly drive decisions.

You can use [Score-Based Data Assimilation](https://arxiv.org/abs/2406.16947) (SDA) to incorporate observations into diffusion-based AI downscaling and forecasting models such as CorrDiff and StormCast. SDA guides the model toward predictions that are consistent with your observations without requiring to retrain the model.

Figure 1, below, shows how the process works under the hood. Diffusion models generate high-resolution predictions through a sequence of denoising steps. At each step, SDA compares the intermediate prediction with your observations and nudges the model in the right direction. The output of SDA is probabilistic, with less uncertainty near observation locations and a wider spread further away, where predictions are increasingly governed by the other model inputs and the underlying AI simulations.

To nudge the model, you define an observation operator, which maps the model output to the quantity you would expect to observe at each measurement location. This is particularly straightforward for in situ measurements of physical quantities such as temperature or wind speed. In this case, the simplest form of an operator interpolates nearby grid values to each observation location. It is also possible to create operators for proxy measurements or observed impacts. For example, the power output of a wind turbine can act as a proxy measurement of wind speed.

SDA unlocks two major capabilities:

- Update forecasts more rapidly. Numerical analyses require substantial processing time and are released on fixed schedules. SDA enables you to incorporate observations continuously. Figure 2, below, shows a concrete example of a pipeline forecasting at one-hour intervals and depending on a global analysis with a six-hour dissemination schedule.
- Incorporate proprietary, regional or domain-specific observations. Numerical analyses draw on a broad range of observations. SDA lets you incorporate data from your own sources to focus your forecast on specific asset locations or downstream applications.

The effectiveness of SDA depends on several factors: the number, spatial distribution, and accuracy of your observations; the characteristic length scales of the field you are predicting; and the quality and well-posedness of the observation operator.

## How to run CorrDiff-SDA in Earth2Studio

CorrDiff is a technique for AI-based downscaling. Earth2Studio provides a CorrDiff model pretrained over Europe that turns 0.25° weather fields into 2.2-km predictions. Using AI data assimilation, you can improve these predictions with observations where local accuracy matters. With the refined outputs, you can then initialize a regional forecast or create a reanalysis dataset for calibrating downstream models.

Start by loading the pretrained model. We limit the domain to a part of the Netherlands and northwestern Germany and choose to assimilate 10-meter wind speeds.

`from` `datetime ` `import` `datetime` `from` `earth2studio.data ` `import` `GHCNHourly` `from` `earth2studio.models.da ` `import` `CorrDiffCosmoEra5SDA` `domain ` `=` `dict` `(lat_min` `=` `50.2` `, lat_max` `=` `53.8` `, lon_min` `=` `4.6` `, lon_max` `=` `10.4` `)` `sda ` `=` `CorrDiffCosmoEra5SDA.load_model(` ` ` `CorrDiffCosmoEra5SDA.load_default_package(),` ` ` `assimilate_variables` `=` `(` `"u10m"` `, ` `"v10m"` `),` ` ` `resolution` `=` `"rea2"` `,` ` ` `domain` `=` `domain,` ` ` `number_of_samples` `=` `1` `,` ` ` `sampler_steps` `=` `12` `,` ` ` `amp` `=` `True` `, ` `).to(` `"cuda"` `)` |

Fetch the ERA5 data for low-resolution conditioning and GHCN wind observations over the domain.

`# Fetch and regrid ERA5 inputs onto the high resolution regional grid` `# Follow the link to the example below for the full implementation` `init_time ` `=` `datetime(` `2024` `, ` `1` `, ` `26` `)` `x ` `=` `fetch_and_regrid_era5(init_time, domain)` `# Fetch GHCN hourly 10-m wind observations over the model domain` `lat, lon ` `=` `sda.model.lat_output_numpy, sda.model.lon_output_numpy` `bbox ` `=` `lat.` `min` `(), lon.` `min` `(), lat.` `max` `(), lon.` `max` `()` `ghcn ` `=` `GHCNHourly(stations` `=` `GHCNHourly.get_stations_bbox(bbox))` `obs ` `=` `ghcn(init_time, [` `"u10m"` `, ` `"v10m"` `]).dropna(subset` `=` `[` `"observation"` `])` |

Lastly, run the model with the input data. We perform two runs to measure how the additional observations affect the results.

`prior ` `=` `sda(x) ` `# free downscaling, no observations` `analysis ` `=` `sda(x, obs) ` `# guide the diffusion toward the observations` |

For a complete implementation, [see the example in Earth2Studio](https://nvidia.github.io/earth2studio/main/examples/05_data_assimilation/03_corrdiff_cosmo_sda/), from which the code above was adapted.

## How to run StormCast-SDA in Earth2Studio

StormCast is a technique similar to CorrDiff but designed for high-resolution, regional forecasting. Earth2Studio includes a [StormCast](https://nvidia.github.io/earth2studio/main/modules/generated/models/px/StormCastCONUS/) model pretrained over the contiguous U.S. (CONUS) that is initialized with HRRR and makes predictions at a 3-km resolution. The computation and dissemination of a new HRRR analysis takes some time, but you can use SDA to combine the currently available analysis with the latest observations to update your forecast.

Start by loading the pretrained model. We limit the domain to the central U.S.

`import` `numpy as np` `from` `earth2studio.data ` `import` `GHCNHourly` `from` `earth2studio.models.px ` `import` `StormCastCONUS` `# Limit the domain to the central U.S.` `hrrr_lat_lim, hrrr_lon_lim ` `=` `(` `305` `, ` `785` `), (` `595` `, ` `1203` `)` `model ` `=` `StormCastCONUS.load_model(` ` ` `StormCastCONUS.load_default_package(),` ` ` `hrrr_lat_lim` `=` `hrrr_lat_lim, ` `# comment out for full CONUS domain` ` ` `hrrr_lon_lim` `=` `hrrr_lon_lim, ` `# comment out for full CONUS domain` ` ` `num_diffusion_steps` `=` `18` `,` ` ` `num_sda_diffusion_steps` `=` `96` `, ` `# more steps for SDA for better stability` ` ` `sda_std_obs` `=` `0.15` `,` ` ` `sda_gamma` `=` `1e` `-` `3` `,` `).to(` `"cuda"` `)` |

Next, fetch the HRRR analysis for model initialization and define the observation data source over the model domain.

`# Fetch HRRR initial conditions` `# Follow the link to the example below for the full implementation` `init_time ` `=` `datetime(` `2026` `, ` `4` `, ` `17` `, ` `18` `)` `x, coords ` `=` `fetch_hrrr(init_time)` `# Define GHCN hourly data source for the model domain` `lat, lon ` `=` `model.lat, model.lon` `bbox ` `=` `lat.` `min` `(), lon.` `min` `(), lat.` `max` `(), lon.` `max` `()` `ghcn ` `=` `GHCNHourly(` ` ` `stations` `=` `GHCNHourly.get_stations_bbox(bbox),` ` ` `time_tolerance` `=` `timedelta(minutes` `=` `15` `),` `)` |

We can now run the model using observations during the initial rollout steps before transitioning to forecasting without additional observations. Similar to the illustration in Figure 2, above, this approach uses observations to bridge the gap between the latest analysis and current conditions, after which the forecast proceeds independently.

For a pipeline initialized with HRRR, only one SDA-informed step is typically relevant before a new analysis arrives. When using a global analysis for initialization, multiple rollout steps can benefit from SDA.

`# Initialize generator and get the first output (analysis passthrough)` `gen ` `=` `model.create_generator(x.clone(), coords.copy())` `x, coords ` `=` `next` `(gen)` `# Run the first part of the rollout with SDA` `for` `step ` `in` `range` `(nsteps_sda):` ` ` `valid_time ` `=` `np.array(` ` ` `[coords[` `"time"` `][` `0` `] ` `+` `coords[` `"lead_time"` `][` `0` `] ` `+` `np.timedelta64(` `1` `, ` `"h"` `)]` ` ` `)` ` ` `obs ` `=` `ghcn(valid_time, [` `"u10m"` `, ` `"v10m"` `, ` `"t2m"` `])` ` ` `x, coords ` `=` `gen.send(obs) ` `# advance one step with observations` `# Run the remaining rollout without SDA` `for` `step ` `in` `range` `(nsteps_non_sda):` ` ` `x, coords ` `=` `next` `(gen) ` `# advance one step without observations` |

You can find a [full implementation of the example](https://nvidia.github.io/earth2studio/main/examples/05_data_assimilation/01_stormcast_sda/) in the Earth2Studio example library.

## How to use SDA with your own model

You can assimilate observations with a custom model by extending its Earth2Studio model wrapper. To do this, use the diffusion utilities in PhysicsNeMo. We start with `x0_predictor`

, a pre-trained denoising diffusion model that takes a noisy sample and its noise level as inputs and predicts a noise-free sample. Without SDA, the diffusion sampling for the model would be implemented like this:

`from` `physicsnemo.diffusion.noise_schedulers ` `import` `EDMNoiseScheduler` `from` `physicsnemo.diffusion.samplers ` `import` `sample` `# Construct diffusion scheduler` `sigma_min, sigma_max ` `=` `0.01` `, ` `100` `scheduler ` `=` `EDMNoiseScheduler(sigma_min` `=` `sigma_min, sigma_max` `=` `sigma_max)` `# Get denoiser from scheduler` `denoiser ` `=` `scheduler.get_denoiser(x0_predictor` `=` `x0_predictor)` `# Generate sample` `latents ` `=` `sigma_max ` `*` `torch.randn(shape)` `sample(denoiser, latents, noise_scheduler` `=` `scheduler, num_steps` `=` `num_steps)` |

To use SDA, we transform the `x0_predictor`

into a score-predicting model with SDA guidance. We use `DataConsistencyDPSGuidance`

, which associates each masked pixel with a corresponding observed value. You can use it to assimilate observations from weather stations, proprietary sensors, or similar point-based sources.

`from` `physicsnemo.diffusion.guidance ` `import` `(` ` ` `DataConsistencyDPSGuidance,` ` ` `DPSScorePredictor,` `)` `# Setup SDA guidance` `guidance ` `=` `DataConsistencyDPSGuidance(` ` ` `mask` `=` `mask, ` `# binary mask that identifies pixels with observations` ` ` `y` `=` `y_obs, ` `# gridded observations` ` ` `std_y` `=` `sda_std_obs, ` `# the remaining parameters are SDA settings` ` ` `norm` `=` `sda_dps_norm,` ` ` `gamma` `=` `sda_gamma,` ` ` `sigma_fn` `=` `scheduler.sigma,` ` ` `alpha_fn` `=` `scheduler.alpha,` `)` `# Convert x0_predictor to score predictor` `score_predictor ` `=` `DPSScorePredictor( ` ` ` `x0_predictor` `=` `x0_predictor,` ` ` `x0_to_score_fn` `=` `scheduler.x0_to_score,` ` ` `guidances` `=` `guidance,` `)` `denoiser ` `=` `scheduler.get_denoiser(score_predictor` `=` `score_predictor)` `# Generate sample (identical to non-SDA example)` `latents ` `=` `sigma_max ` `*` `torch.randn(shape)` `sample(denoiser, latents, noise_scheduler` `=` `scheduler, num_steps` `=` `num_steps)` |

For more advanced SDA pipelines, use ModelConsistencyDPSGuidance to derive simulated observations from multiple grid points. This approach requires you to provide a PyTorch model that maps each sample to the corresponding simulated observations. With a custom PyTorch model, you can also assimilate observed impacts. For example, you can use a wind power model to assimilate turbine output measurements.

For a complete implementation, have a look at the [StormCast CONUS wrapper in Earth2Studio](https://github.com/NVIDIA/earth2studio/blob/main/earth2studio/models/px/stormcastconus.py), on which the example above is based.

## Compute the global weather from observations

Most global weather forecasting pipelines are initialized with an estimate of the current weather derived through numerical data assimilation. Numerical data assimilation is computationally demanding, which reduces the timeliness and refresh rate of forecasts and makes it harder to integrate custom observations.

With an AI-based technique called [HealDA](https://arxiv.org/abs/2601.17636), you can estimate the state of the global atmosphere in a matter of seconds. This allows you to issue forecasts closer to current conditions or compute a custom reanalysis.

HealDA maps remote-sensing and in situ observations within a time window to a global gridded atmospheric state. It consists of two main components: an observation encoder and a vision transformer (ViT) backbone. The encoder ingests heterogeneous observations as point clouds, embedding each scalar value into a token together with metadata such as geolocation and time. These tokens are then aggregated onto the target grid and processed by the ViT backbone.

You can use a pretrained global data assimilation model as a starting point. If you have custom conventional observations, you can typically incorporate them without modifying the model.

For proprietary satellite data, you can adapt the encoder to support your data sources. This flexibility lets you tailor the data assimilation system to your region or application. You can use the same technique to train a regional instead of a global system. To get started, see the HealDA training pipeline in the open-source Python library [PhysicsNeMo](https://github.com/NVIDIA/physicsnemo).

## How to run HealDA in Earth2Studio

Earth2Studio provides a pretrained global data assimilation model for research purposes. It integrates data from microwave sounders, radio occultation, surface stations, aircraft, buoys, and other sources onto a 1° HEALPix grid (HPX64).

First, load the model.

`from` `datetime ` `import` `timedelta` `import` `numpy as np` `from` `earth2studio.data ` `import` `UFSObsConv, UFSObsSat, fetch_dataframe` `from` `earth2studio.models.da ` `import` `HealDA` `model ` `=` `HealDA.load_model(` ` ` `HealDA.load_default_package(),` ` ` `lat_lon` `=` `True` `, ` `# regrid from HEALPix to regular lat/lon` `).to(` `"cuda"` `)` |

Next, fetch the input observations from the NOAA UFS replay repository. We use conventional and satellite observations.

`# HealDA was trained on the UFS replay window: 21h before to 3h after analysis time` `time_tolerance ` `=` `(timedelta(hours` `=` `-` `21` `), timedelta(hours` `=` `3` `))` `analysis_time ` `=` `np.array([np.datetime64(` `"2024-01-01T00:00"` `)])` `# input_coords() returns the schemas the two observation DataFrames must satisfy` `conv_schema, sat_schema ` `=` `model.input_coords()` `# fetch_dataframe attaches the request_time metadata the model needs` `conv_df ` `=` `fetch_dataframe(` ` ` `UFSObsConv(time_tolerance` `=` `time_tolerance),` ` ` `time` `=` `analysis_time,` ` ` `variable` `=` `np.array(conv_schema[` `"variable"` `]),` ` ` `fields` `=` `np.array(` `list` `(conv_schema.keys())),` `)` `sat_df ` `=` `fetch_dataframe(` ` ` `UFSObsSat(time_tolerance` `=` `time_tolerance),` ` ` `time` `=` `analysis_time,` ` ` `variable` `=` `np.array(sat_schema[` `"variable"` `]),` ` ` `fields` `=` `np.array(` `list` `(sat_schema.keys())),` `)` |

Then call the model with the observation data frames.

`# stateless model - call it directly for a one-shot analysis, or use` `# create_generator for cycled assimilation` `analysis ` `=` `model(conv_obs` `=` `conv_df, sat_obs` `=` `sat_df)` |

You can find an extended [example for running HealDA](https://nvidia.github.io/earth2studio/main/examples/05_data_assimilation/02_healda/) in the Earth2Studio example library.

## Access observational data with Earth2Studio

Earth2Studio gives you access to a broad range of data sources for developing, initializing, and validating weather models, including observations from different platforms and sensor types.

Among these are gridded data from geostationary satellites (GOES, Himawari, Meteosat) and radar networks (MRMS, OPERA), which you can use directly to train and rapidly update regional, high-resolution forecasting models such as [StormScope](https://nvidia.github.io/earth2studio/modules/generated/models/px/earth2studio.models.px.StormScopeGOES.html). These sources are especially useful when you want to forecast quantities that depend on insolation or precipitation, like solar power production, cooling processes, and reservoir inflows.

For developing and benchmarking a data assimilation system, Earth2Studio also lets you access archives of conventional observations like GHCN/ISD, NNJA, and UFS, as well as operational observations from GDAS and ASOS. These sources provide variables such as temperature and wind speed as data frames. Observations from polar-orbiting satellite systems, including MetOp and JPSS, are also available.

Earth2Studio provides a unified interface across all data sources. You instantiate a data source object and call it with a list of timesteps and variable names. Forecast data sources also accept a list of lead times. This consistent interface makes it easy to combine multiple data sources within the same workflow or connect your own observations to a pipeline.

`era5 ` `=` `NCAR_ERA5()` `da_era5 ` `=` `era5(datetime(` `2025` `, ` `7` `, ` `15` `), [` `"t2m"` `, ` `"z500"` `])` `print` `(da_era5.shape) ` `# (1, 2, 721, 1440)` `ifs ` `=` `IFS_FX()` `da_ifs ` `=` `ifs(datetime(` `2026` `, ` `7` `, ` `15` `), timedelta(hours` `=` `48` `), [` `"t2m"` `])` `print` `(da_ifs.shape) ` `# (1, 1, 1, 721, 1440)` `goes ` `=` `GOES(satellite` `=` `"goes19"` `, scan_mode` `=` `"C"` `)` `da_goes ` `=` `goes(datetime(` `2026` `, ` `7` `, ` `15` `), [` `"abi01c"` `, ` `"abi02c"` `, ` `"abi03c"` `])` `print` `(da_goes.shape) ` `# (1, 3, 1500, 2500)` `ghcn ` `=` `GHCNHourly(stations` `=` `[` `"USW00013301"` `])` `df_ghcn ` `=` `ghcn(datetime(` `2026` `, ` `6` `, ` `15` `), [` `"t2m"` `, ` `"ws10m"` `])` `print` `(df_ghcn.shape) ` `# (10, 7)` |

For the full list of supported data sources, see the [API reference in the user guide](https://nvidia.github.io/earth2studio/main/modules/datasources_analysis/).

## Get started with Earth2Studio

Explore [end-to-end AI data assimilation examples](https://nvidia.github.io/earth2studio/main/examples/#data-assimilation) in the Earth2Studio example library. To connect your own observations to a pipeline, follow the [custom data source example](https://nvidia.github.io/earth2studio/main/examples/08_extend/03_custom_datasource/).

AI data assimilation lets you issue more accurate, timely forecasts by incorporating the observations that matter to your region or organization.

Visit the [Earth2Studio user guide](https://nvidia.github.io/earth2studio/main/) to get started with AI data assimilation and explore the broader capabilities of AI weather models.

## Start the discussion at forums.developer.nvidia.com
