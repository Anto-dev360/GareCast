Write-Host "Running all pytest tests..."
pytest tests/ --maxfail=1 --disable-warnings -q