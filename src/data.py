"""I/O utilities: download and load datasets.
Functions:
- download_data(output_dir='data', url=None): download and extract dataset
- load_csv(path): load CSV as pandas.DataFrame
"""
import os
import shutil
from pathlib import Path
import requests
import zipfile
import pandas as pd


def download_from_url(url: str, dest: str) -> str:
    """Download a file from URL to dest path. Returns path to downloaded file."""
    dest_path = Path(dest)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return str(dest_path)


def extract_if_archive(path: str, dest_dir: str):
    p = Path(path)
    if zipfile.is_zipfile(p):
        with zipfile.ZipFile(p, "r") as z:
            z.extractall(dest_dir)
        return True
    return False


def download_data(output_dir: str = "data", url: str = None) -> str:
    """Download dataset into output_dir.

    If url is None, this function creates the folder structure and returns the data path.
    Replace url with a dataset link or implement Kaggle download if needed.
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    if url:
        filename = url.split("/")[-1]
        dl_path = out / filename
        print(f"Downloading {url} -> {dl_path}")
        download_from_url(url, str(dl_path))
        if extract_if_archive(str(dl_path), str(out)):
            print("Archive extracted")
    else:
        print(f"No URL provided. Create dataset folder at {out.resolve()}")
    return str(out.resolve())


def load_csv(path: str, **kwargs) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, **kwargs)
