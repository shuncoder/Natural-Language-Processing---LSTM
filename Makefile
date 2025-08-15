# Simple Makefile (may be used in CI/Linux). On Windows use the PowerShell script or run commands manually.
.PHONY: setup download train notebooks

setup:
	python -m pip install -r requirements.txt

download:
	python -c "from src.data import download_data; download_data()"

train:
	python -c "from src.train import run_training; run_training()"

notebooks:
	papermill 01_download_data.ipynb 01_download_data.out.ipynb && papermill 02_train.ipynb 02_train.out.ipynb
