def get_gps_satellites(obs):
    """
    Extracts GPS satellites from multi-constellation RINEX dataset.

    Filters satellite identifiers and returns only GPS PRNs (G01–G32)
    for further single-satellite analysis.
    """
    all_sv = obs.sv.values          # List all GPS satellites present in the file
    return sorted([s for s in all_sv if s.startswith("G")])
    print(f"🛰️  GPS satellites in this file ({len(gps_sats)} total):")
    print("   " + "  ".join(gps_sats))
    print()

def select_satellite(gps_sats, sat="G05"):
    """
    Selects a specific GPS satellite from available dataset.

    Validates that the requested satellite exists in the observation file
    and prepares it for pseudorange and SNR analysis.
    """
    if sat not in gps_sats:
        raise ValueError(f"{sat} not found in dataset")
    return sat
