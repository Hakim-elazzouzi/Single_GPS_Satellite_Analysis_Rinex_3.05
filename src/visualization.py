# ─────────────────────────────────────────────
# Plot 1: Pseudorange Arc + SNR Time Series
# ─────────────────────────────────────────────
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

GPS_COLOR = "#2196F3"

def plot_pseudorange_snr(pr, snr, pr_label, snr_label, sat):
    """
    Visualizes pseudorange variation and signal quality over time.

    Top panel shows satellite range evolution (rise, zenith, set).
    Bottom panel shows SNR variations with quality thresholds.
    Highlights closest approach and low-signal regions.
    """
    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True, facecolor="#0d1117")

    fig.suptitle(f'GPS Satellite {sat} — Auckland (AUCK00NZL), 2026-01-01',
    fontsize=14, fontweight='bold', color="#ffffff")

    # Apply dark background to both panels
    for ax in axes:
        ax.set_facecolor("#111827")
        ax.tick_params(colors="#aaaaaa")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333333")
    ax.grid(True, color="#222222", linewidth=0.5)

    # --- Pseudorange ---
    axes[0].plot(pr.index, pr.values / 1e6, color=GPS_COLOR, lw=1.8, label=f'Pseudorange ({pr_label})')
    axes[0].set_ylabel('Pseudorange [Mm]', color="#aaaaaa", fontsize=11)
    axes[0].set_title(
    f'Pseudorange {pr_label} — distance from receiver to satellite (in million metres)',
    fontsize=10, color="#ffffff"
    )
    # Annotate the closest approach (smallest pseudorange = satellite highest in sky)
    idx_min = pr.idxmin()
    axes[0].annotate(
    f'Closest approach\n{pr[idx_min]/1e6:.2f} Mm',
    xy=(idx_min, pr[idx_min]/1e6),
    xytext=(30, 20),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->', color="#F44336"),
    fontsize=9,
    color="#F44336"
    )

    # --- SNR ---
    axes[1].plot(snr.index, snr.values, color="#FFEB3B", lw=1.8, label=f'SNR ({snr_label})')

    # Quality threshold lines
    axes[1].axhline(40, color="#00e676", ls='--', lw=1.2, alpha=0.8, label='Excellent (40 dB-Hz)')
    axes[1].axhline(35, color="#4CAF50", ls='--', lw=1.0, alpha=0.8, label='Good (35 dB-Hz)')
    axes[1].axhline(25, color="#F44336", ls='--', lw=1.0, alpha=0.8, label='Poor (25 dB-Hz)')

    # Shade low-SNR regions (poor quality)
    axes[1].fill_between(
    snr.index, snr.values, 25,
    where=(snr.values < 25),
    color="#F44336", alpha=0.25, label='Low SNR zone'
    )

    axes[1].set_ylabel('SNR [dB-Hz]', color="#aaaaaa", fontsize=11)
    axes[1].set_xlabel('UTC Time (HH:MM)', color="#aaaaaa", fontsize=11)
    axes[1].set_title(
        'Signal-to-Noise Ratio — higher = better signal quality',
        fontsize=10, color="#ffffff"
    )
    axes[1].legend(
        fontsize=9, ncol=2,
        framealpha=0.3, facecolor="#1a1a2e", edgecolor="#444444", labelcolor="#e0e0e0"
    )
    axes[1].set_ylim(0, 60)
    
    # Time axis formatting
    
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    axes[1].xaxis.set_major_locator(mdates.HourLocator(interval=2))
    plt.xticks(rotation=30, color="#aaaaaa")
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('plot1_pseudorange_snr_arc.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.show()

# ─────────────────────────────────────────────
# Plot 2: SNR Heatmap (Satellite Availability)
# ─────────────────────────────────────────────
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.colors import LinearSegmentedColormap

def plot_snr_heatmap(obs, sat):
    """
    Displays SNR heatmap representing satellite visibility and signal strength.

    Uses full observation timeline to highlight tracking gaps,
    signal quality transitions, and satellite availability over time.
    """
    # Getting full time series including NaN (= satellite not visible)
    snr_full = obs["S1C"].sel(sv=sat).to_series()
    # Replace NaN with 5 (below vmin=15) so gaps render as dark background
    snr_display = np.where(np.isnan(snr_full.values), 5, snr_full.values)
    # Custom GNSS colormap
    gnss_cmap = LinearSegmentedColormap.from_list(
        "gnss_snr",
        [
        "#0d1117",  # background / no data
        "#1a0533",  # deep purple (very weak)
        "#2c3e8c",  # blue (low)
        "#0099cc",  # cyan (moderate)
        "#00e676",  # green (good)
        "#ffeb3b",  # yellow (strong)
        "#ff6f00",  # orange (excellent)
    ],
    N=256
    )

    fig, ax = plt.subplots(figsize=(16, 3), facecolor="#0d1117")
    ax.set_facecolor("#0d1117")

    ax.imshow(
        snr_display.reshape(1, -1),
        aspect="auto",
        cmap=gnss_cmap,
        vmin=15,
        vmax=55,
        extent=[
            mdates.date2num(snr_full.index[0]),  # x left  = first epoch
            mdates.date2num(snr_full.index[-1]), # x right = last epoch
            -0.5,                                # y bottom
            0.5                                  # y top
        ]
    )

    # Tell matplotlib the X axis contains date numbers
    ax.xaxis_date()
    
    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=gnss_cmap,
                                norm=plt.Normalize(vmin=15, vmax=55))
    cbar = plt.colorbar(sm, ax=ax, pad=0.01)
    cbar.set_label('SNR [dB-Hz]', color="#e0e0e0")
    cbar.ax.yaxis.set_tick_params(color="#aaaaaa")
    plt.setp(cbar.ax.get_yticklabels(), color="#aaaaaa")
    
    # Y axis — satellite label centred in the band
    ax.set_yticks([0])
    ax.set_yticklabels([sat], fontsize=11, color="#e0e0e0", fontweight='bold')
    ax.set_ylim(-0.5, 0.5)
    
    ax.set_title(
        f'SNR Heatmap — GPS {sat} | AUCK00NZL | 2026-01-01\n'
        'Green/Yellow = strong signal  |  Blue/Purple = weak  |  Black = not visible',
        fontsize=12, fontweight='bold', color="#ffffff"
    )
    ax.set_xlabel('UTC Time (HH:MM)', fontsize=11, color="#e0e0e0")
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    plt.xticks(rotation=30, color="#aaaaaa")
    
    for spine in ax.spines.values():
        spine.set_edgecolor("#333333")
    
    plt.tight_layout()
    plt.savefig('plot2_snr_heatmap.png', dpi=150, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.show()
