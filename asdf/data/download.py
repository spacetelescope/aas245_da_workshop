from pathlib import Path
from urllib.request import urlretrieve


REMOTE_URL = "https://data.science.stsci.edu/redirect/Roman/Roman_Data_Workshop/"
REMOTE_PATHS = [
    "ADASS2024/jwst.asdf",
    "ExampleData/Build16/r0000101001001001001_0001_wfi01_cal.asdf",
    "ExampleData/Build16/r00001_p_v01001001001_r274dp63x31y80_f158_coadd_i2d.asdf",
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
