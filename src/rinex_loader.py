import georinex as gr

def load_rinex(obs_path, interval=30):
    print("Reading RINEX header...")
    header = gr.rinexheader(obs_path)

    print("FILE HEADER")
    print("=" * 60)
    for k, v in header.items():
        print(f"{k:<25}: {v}")

    print("Loading observation data...")
    obs = gr.load(obs_path, interval=30)

    print("Loaded successfully")
    return obs, header
