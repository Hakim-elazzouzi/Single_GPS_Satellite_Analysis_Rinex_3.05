import numpy as np

def extract_observables(obs, sat):
    """
    Extracts pseudorange and SNR observables for a selected satellite.

    Selects L1 pseudorange (C1C or C1X) and corresponding SNR (S1C or S1X)
    from the RINEX dataset, returning clean time series for analysis.
    """
    # Pseudorange
    # C1C = L1 C/A code pseudorange (most common for GPS)
    # C1X = L1 combined pseudorange (used by some receivers)
    # We try C1C first, then fall back to C1X if not available.
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
