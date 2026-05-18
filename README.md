# Project 1 — Single GPS Satellite Analysis

> **Pseudorange Arc & SNR Heatmap | 24-Hour Tracking | Auckland, NZ**

**Station:** AUCK00NZL | Auckland, New Zealand |
**Receiver:** TRIMBLE ALLOY |
**Antenna:** TRM115000.00 | 
**File:** `AUCK00NZL_R_20260010000_01D_30S_MO.rnx` |  
**Format:** RINEX 3.05 | Mixed Constellations | 30-second sampling | 2026-01-01

---

## Overview

This project parses a **RINEX 3 GNSS observation file** and focuses on a **single GPS satellite** tracked continuously over a full 24-hour period from the **AUCK00NZL** geodetic reference station in Auckland, New Zealand.

From the raw RINEX data we extract two fundamental observables and visualise them in publication-quality plots:

| Plot | What It Shows |
|------|--------------|
| Pseudorange Arc | How the receiver-to-satellite distance evolves as the satellite rises, passes overhead, and sets |
| SNR Heatmap | How signal strength varies throughout the tracking arc |

---

## Output Plots

### Plot 1 — Pseudorange & SNR Time Series

Two-panel figure with a shared time axis:

- **Top panel:** Pseudorange (C1C or C1X) in million metres — the orbital arc of the satellite
- **Bottom panel:** Signal-to-Noise Ratio in dB-Hz — with quality threshold lines at 25, 35, and 40 dB-Hz

### Plot 2 — SNR Heatmap

Single-row heatmap showing the satellite's signal quality over 24 hours using a custom GNSS colour scale:

```
Black        → satellite below horizon (no data)
Blue/Purple  → weak signal (low elevation)
Green        → good signal quality
Yellow/Orange → excellent signal (satellite overhead)
```

---

## File Structure

```
project1-single-gps-satellite/
├── Outputs/
│   ├── plot1_pseudorange_snr_arc.png
│   ├── plot2_snr_heatmap.png
├── src/
│   ├── config.py
│   ├── rinex_loader.py
│   ├── satellite_selection.py
│   ├── gnss_observables.py
│   ├── analysis.py
│   ├── visualization.py
│   └── main.py
├── requirements.txt                          ← Python dependencies
├── LICENSE                                   ← MIT License
└── README.md                                 ← This file
```

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your RINEX file

Place your RINEX 3 observation file anywhere accessible and update the path in the notebook:

```python
obs_path = "/path/to/your/file.rnx"   # ← update this line in Step 2
```

### 3. Choose your satellite

In **Step 3** of the notebook, change:

```python
SAT = 'G05'   # ← any GPS satellite PRN (G01–G32)
```

### 4. Run all cells

```bash
jupyter notebook project1_single_gps_satellite.ipynb
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `georinex` | Parse RINEX 3 observation and navigation files |
| `xarray` | N-dimensional array handling (time × satellite data) |
| `pandas` | Time series manipulation |
| `numpy` | Numerical computations |
| `matplotlib` | Publication-quality plotting |

---

## RINEX File Format

This project was developed using:

```
File   : AUCK00NZL_R_20260010000_01D_30S_MO.rnx
Station: AUCK00NZL — Auckland, New Zealand (GeoNet / LINZ Network)
Format : RINEX 3.05
Date   : 2026-01-01 (Day-of-Year 001)
Rate   : 30-second sampling
```

The project is compatible with **any RINEX 3 observation file** from any station worldwide.

---

## Observables Used

| Code | Description |
|------|-------------|
| `C1C` | Pseudorange on L1 C/A code [metres] |
| `C1X` | Pseudorange on L1 combined [metres] (fallback) |
| `S1C` | Signal-to-Noise Ratio on L1 C/A [dB-Hz] |
| `S1X` | Signal-to-Noise Ratio on L1 combined [dB-Hz] (fallback) |

---

## Author

**Hakim El Azzouzi**  
MSc Global Navigation Satellite Systems  
Mohammed First University, Oujda, Morocco  
📧 elazzouzihakim10@gmail.com  
🔗 [linkedin.com/in/Hakim-El-Azzouzi](https://linkedin.com/in/Hakim-El-Azzouzi)  
📍 Luxembourg 🇱🇺

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## Part of the GNSS RINEX Analysis Series

| # | Project |
|---|---------|
| **1** | **Single GPS Satellite — Pseudorange & SNR Heatmap** ← You are here |
| 2 | All GPS Satellites — Fleet Pseudorange & SNR Heatmap |
| 3 | Multi-Constellation GNSS — Single Satellite per System |
| 4 | Pseudorange vs Carrier-Phase Comparison |
| 5 | Constellation Summary — Pie Chart & Histogram |
| 6 | Ionospheric Delay — Geometry-Free Combination |
| 7 | Data Quality Report |
