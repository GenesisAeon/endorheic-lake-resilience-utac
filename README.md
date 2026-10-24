# endorheic-lake-resilience-utac

**Status: scaffold (v0.0.1) — no analysis, no results.** Nothing in this repository is a finding yet.

Author: Johann Benjamin Römer, Independent researcher, Kirchhain, Germany
Register: P134 · class KLIMA-LAND-09 · `-utac` family (GenesisAeon, decided 2026-10-24)

## Motivation
Tuz Gölü (Central Anatolia, Türkiye) is a shallow (< 0.5 m in most places), hypersaline terminal lake and the main breeding site of the Greater Flamingo in Türkiye. August Landsat classifications show water covering > 20 % of the lake bed in most years 1985–2000 but < 20 % in almost every August 2001–2016, with complete desiccation in 2008 and 2016. The correlation between salt-covered area and an aridity index strengthened from r = −0.46 (before 2000) to r = −0.88 (after 2000) (Aydın, Erlat & Türkeş 2020). The authors attribute this rising drought sensitivity to groundwater abstraction, warming and more frequent droughts. In the surrounding Konya Closed Basin (~50,000 km²), GRACE and well data show declining groundwater storage, InSAR shows subsidence of up to 90 mm/yr, and sinkhole (obruk) formation has accelerated (Orhan et al. 2024; Gökkaya, Gutiérrez & Tunçel 2026).

This project asks whether the lake's loss of resilience can be quantified reproducibly from open data, and whether climate forcing and abstraction can be separated honestly.

## Narrow entry point: M1
Reproduce the August surface-area series (water / salt / marsh, 1985–2016) of

> Aydın, F., Erlat, E., & Türkeş, M. (2020). *Regional Environmental Change* 20:68. https://doi.org/10.1007/s10113-020-01656-z

from Landsat Collection 2 and JRC Global Surface Water. Only once that classification is reproduced, build our own monthly series 1984–2026. The water/salt-crust classification on a lake this shallow is the main bottleneck.

## Hypotheses (testable; analysis protocol fixed before any run)
- **H1 — rising sensitivity.** The sensitivity of Tuz Gölü water area to climate anomalies (SPEI, ERA5-Land) increased significantly. The breakpoint is *estimated* (structural-break test, rolling regression) and only afterwards compared with the published ~2000; fixing it at 2000 would be circular.
- **H2 — abstraction residual.** GRACE terrestrial water storage decline in the Konya Closed Basin exceeds what P − E explains; the residual correlates with irrigated area. Caveat: the basin is at or below GRACE's effective resolution, so leakage/scaling analysis is mandatory before any interpretation.
- **H3 — early-warning signals (exploratory).** Rolling AR1/variance of the deseasonalised area series rise before desiccation years. Flagged exploratory: the series is bounded at 0 % water, an externally forced trend raises AR1 without critical slowing down, and series are short and gappy. Requires detrending, surrogate tests, negative-control lakes, and a signal criterion fixed in advance. EWS statistics should reuse resilience-memory-utac (P97) rather than reimplement them.
- **H4 — hysteresis.** Recovery after wet years (e.g. 2025/26) is weaker/shorter than before 2000. Deferred until post-2026 data exist.

## Comparison lakes (after M1 only)
Lake Urmia, Aral Sea, Great Salt Lake, Lake Poopó, Dead Sea; controls without transition: Lake Chad (post-2000), Qinghai Lake, Mono Lake. See `docs/DOSSIER_de.md` §2.

## Data sources and licence status
| Dataset | Use | Licence |
|---|---|---|
| Landsat Collection 2 L2 (USGS) | surface classification 1984– | Public domain |
| JRC Global Surface Water v1.4+ | monthly water maps | CC BY 4.0 — **TODO: verify version/licence** |
| Sentinel-2 L2A / Sentinel-1 | 10 m optics / InSAR | Copernicus open licence |
| GRACE/GRACE-FO mascons (JPL, CSR) | water storage | NASA open data |
| ERA5 / ERA5-Land (Copernicus CDS) | P, T, E, PET | Copernicus licence (free, attribution) |
| CHIRPS v2/v3 | precipitation | Public domain |
| MODIS (MOD09A1, MOD13, MOD16) | reflectance, NDVI, ET | NASA open data |
| DAHITI (DGFI-TUM) | lake level/area | **TODO: verify licence; check Tuz coverage** |
| Hydroweb (Theia/CNES) | altimetry levels | **TODO: verify licence** |
| HydroLAKES / Yao et al. 2023 data | lake polygons, storage | CC BY 4.0 — TODO: verify |
| GBIF / eBird | flamingo records | CC BY / CC0 per record |
| DSİ / MGM (Türkiye) | wells, stations | restrictive — **not to be stored in this public repo** |

## Package layout
`src/endorheic_lake_resilience_utac/`: `ingest` (download/STAC), `surface` (water/salt classification), `waterbalance` (budget residual, attribution), `ews` (early-warning statistics, via P97), `compare` (multi-lake), `report` (figures). All modules are empty stubs.

## Milestones
- **M1** Tuz surface series; reproduce Aydın et al. (2020) August values; H1 with estimated breakpoint; pre-registered protocol.
- **M2** Basin water balance (ERA5-Land, CHIRPS); GRACE only with leakage analysis.
- **M3** H3 exploratory; comparison lakes with negative controls.
- **M4** Preprint (archiving decided later; no DOI yet).

## Risks
- Water vs. salt-crust misclassification on a < 0.5 m deep lake.
- GRACE resolution vs. basin size (leakage from neighbouring regions).
- EWS false positives (lower bound at 0 %, forced trends, seasonality, short series).
- Collinearity of climate and abstraction drivers; no access to DSİ well data.
- Unverified dataset licences (see TODOs above).

## Background
`docs/DOSSIER_de.md` — German research dossier (v3, reviewed), with unverified items marked [U].

## Licence
Code: MIT (see `LICENSE`). Third-party data keep their own licences.
