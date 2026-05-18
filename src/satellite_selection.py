def get_gps_satellites(obs):
    all_sv = obs.sv.values          # List all GPS satellites present in the file
    return sorted([s for s in all_sv if s.startswith("G")])
    print(f"🛰️  GPS satellites in this file ({len(gps_sats)} total):")
    print("   " + "  ".join(gps_sats))
    print()

def select_satellite(gps_sats, sat="G05"):
    if sat not in gps_sats:
        raise ValueError(f"{sat} not found in dataset")
    return sat
