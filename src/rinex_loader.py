# Install georinex if not already installed
# Uncomment the line below if you are running this for the first time:
# !pip install --upgrade georinex
import georinex as gr

def load_rinex(obs_path, interval=30):
    print("Reading RINEX header...")  
    header = gr.rinexheader(obs_path)     # Read the file header first (fast — no data loaded yet)

    print("FILE HEADER")
    print("=" * 60)
    for k, v in header.items():
        print(f"{k:<25}: {v}")

    print("Loading observation data...")
    obs = gr.load(obs_path, interval=30)  # Load all observation data (interval=30 means keep 30-sec rate)

    print("Loaded successfully")
    return obs, header
