Write-Host "Running all pytest tests..."
$env:PYTHONPATH = ".\src"
pytest tests/ --maxfail=1 --disable-warnings -q