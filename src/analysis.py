def summarize_observables(pr, snr):
    """
    Computes statistical summary of pseudorange and SNR measurements.

    Calculates minimum, maximum, and mean values for both observables,
    along with closest-approach epoch for pseudorange.
    Also prints GNSS-formatted interpretation in engineering units.
    """
    stats = {
        # Raw values (SI units)
        "pr_min": float(pr.min()),
        "pr_max": float(pr.max()),
        "pr_mean": float(pr.mean()),

        "snr_min": float(snr.min()),
        "snr_max": float(snr.max()),
        "snr_mean": float(snr.mean()),

        "closest_time": pr.idxmin(),
        "closest_value": float(pr.min()),
    }

    # --- GNSS formatted printout (analysis layer) ---
    print(f" Pseudorange statistics:")
    print(f"   Min  : {stats['pr_min']/1e6:.3f} Mm")
    print(f"   Max  : {stats['pr_max']/1e6:.3f} Mm")
    print(f"   Mean : {stats['pr_mean']/1e6:.3f} Mm")
    print()

    print(f" SNR statistics:")
    print(f"   Min  : {stats['snr_min']:.1f} dB-Hz")
    print(f"   Max  : {stats['snr_max']:.1f} dB-Hz")
    print(f"   Mean : {stats['snr_mean']:.1f} dB-Hz")
    print()

    return stats
