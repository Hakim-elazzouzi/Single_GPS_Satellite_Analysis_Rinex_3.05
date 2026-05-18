import matplotlib.pyplot as plt

from config import OBS_PATH, SATELLITE, PLOT_STYLE
from rinex_loader import load_rinex
from satellite_selection import get_gps_satellites, select_satellite
from gnss_observables import extract_observables
from analysis import summarize_observables
from visualization import plot_pseudorange_snr, plot_snr_heatmap


plt.rcParams.update(PLOT_STYLE)

# 1. Load data
obs, header = load_rinex(OBS_PATH)

# 2. Get satellites
gps_sats = get_gps_satellites(obs)
sat = select_satellite(gps_sats, SATELLITE)

# 3. Extract observables
pr, snr, pr_label, snr_label = extract_observables(obs, sat)

# 4. Analysis
stats = summarize_observables(pr, snr)

print(stats)

# 5. Plots
plot_pseudorange_snr(pr, snr, pr_label, snr_label, sat)
plot_snr_heatmap(obs, sat)
