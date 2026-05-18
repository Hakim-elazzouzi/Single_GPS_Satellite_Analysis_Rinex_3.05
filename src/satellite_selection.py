def get_gps_satellites(obs):
    all_sv = obs.sv.values
    return sorted([s for s in all_sv if s.startswith("G")])


def select_satellite(gps_sats, sat="G05"):
    if sat not in gps_sats:
        raise ValueError(f"{sat} not found in dataset")
    return sat
