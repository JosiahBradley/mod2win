Write-Host "Creating python environment..." 
python -m venv venv | Out-Null

Write-Host "Entering python environment..."
./venv/Scripts/activate.ps1

Write-Host "Installing requirements..."
pip install setuptools wheel | Out-Null
pip install -r requirements.txt | Out-Null

Write-Host "Building mod2win..."
Remove-Item -Force -Recurse build/* | Out-null
python setup.py sdist bdist_wheel | Out-Null
python setup.py build | Out-Null
python setup.py install | Out-Null
python setup.py develop | Out-Null

Write-Host "Cleanup..."
scrub
