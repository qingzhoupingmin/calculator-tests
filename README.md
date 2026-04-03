# Calculator Tests Project

This project contains automated tests for a simple calculator.

## Project Structure
- `test_logic.py` - Logic layer unit tests
- `test_ui.py` - User interface tests
- `conftest.py` - Pytest fixtures and configuration
- `fixtures/` - Test data in YAML format
- `Dockerfile` - Docker configuration for running tests

## Running Tests

### Using Docker (Recommended)
```bash
docker run --rm \
  -v "${PWD}:/app/tests" \
  -v "../calculator:/app/calculator" \
  -e PYTHONPATH=/app \
  calculator-tests:latest pytest -v
```

### Using Local Python
```bash
pip install -r requirement.txt
pytest -v
```

## CI/CD
Tests are automatically run via GitHub Actions on every push to the `main` branch.

You can also manually trigger the workflow from the Actions tab.
