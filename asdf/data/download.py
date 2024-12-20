from pathlib import Path
from urllib.request import urlretrieve


REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/AAS245/"
REMOTE_PATHS = [
    "jwst.fits",
    "roman.asdf",
]

LOCAL_DIRECTORY = Path(__file__).parent


def download_data():
    for remote_path in REMOTE_PATHS:
        url = REMOTE_URL + remote_path
        local_path = LOCAL_DIRECTORY / Path(url).name
        if local_path.exists():
            print(f"Skipping {local_path} (file exists)")
        else:
            print(f"Downloading {url} to {local_path}...")
            urlretrieve(url, local_path)


if __name__ == "__main__":
    download_data()
