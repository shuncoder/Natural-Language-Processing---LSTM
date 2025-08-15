# PowerShell script to run notebooks sequentially using papermill
# Usage: ./run_notebooks.ps1

if (-not (Get-Command papermill -ErrorAction SilentlyContinue)) {
    Write-Host "papermill not found. Install with: pip install papermill"
    exit 1
}

papermill 01_download_data.ipynb 01_download_data.out.ipynb
if ($LASTEXITCODE -ne 0) { throw "01_download_data failed" }

papermill 02_train.ipynb 02_train.out.ipynb
if ($LASTEXITCODE -ne 0) { throw "02_train failed" }

Write-Host "Notebooks executed successfully."
