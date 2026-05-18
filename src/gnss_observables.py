import numpy as np

def extract_observables(obs, sat):
    # Pseudorange
    if "C1C" in obs.data_vars:
        pr = obs["C1C"].sel(sv=sat).to_series().dropna()
        pr_label = "C1C"
    elif "C1X" in obs.data_vars:
        pr = obs["C1X"].sel(sv=sat).to_series().dropna()
        pr_label = "C1X"
    else:
        raise ValueError("No pseudorange observable found")

    # SNR
    if "S1C" in obs.data_vars:
        snr = obs["S1C"].sel(sv=sat).to_series().dropna()
        snr_label = "S1C"
    elif "S1X" in obs.data_vars:
        snr = obs["S1X"].sel(sv=sat).to_series().dropna()
        snr_label = "S1X"
    else:
        raise ValueError("No SNR observable found")

    return pr, snr, pr_label, snr_label
