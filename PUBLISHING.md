# Publishing codicent-py to PyPI

## Step-by-Step Guide

### Prerequisites
1. Create accounts on both [TestPyPI](https://test.pypi.org/account/register/) and [PyPI](https://pypi.org/account/register/)
2. Generate API tokens for both accounts (recommended over passwords)

### 1. Build the Package
```bash
# Install build tools
pip install --upgrade build twine

# Clean any previous builds
rmdir /s dist build codicent_py.egg-info

# Build the package
python -m build
```

### 2. Test Upload (Optional but Recommended)
```bash
# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install -i https://test.pypi.org/simple/ codicent-py
```

### 3. Production Upload
```bash
# Upload to PyPI
python -m twine upload dist/*
```

### 4. Verify Installation
```bash
# Test that users can install your package
pip install codicent-py
```

## Using the Publish Script

You can also use the included `publish.py` script:

```bash
# Build the package
python publish.py build

# Test upload to TestPyPI
python publish.py test

# Production upload to PyPI
python publish.py prod
```

## Authentication

When uploading, you'll be prompted for credentials. You can either:

1. **Use username/password** (less secure)
2. **Use API tokens** (recommended):
   - Username: `__token__`
   - Password: Your API token (starts with `pypi-`)

## Configuration for API Tokens

Create a `.pypirc` file in your home directory:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-testpypi-api-token-here
```

## Important Notes

- **Package name uniqueness**: The name `codicent-py` must be unique on PyPI
- **Version updates**: Increment the version in `pyproject.toml` and `setup.py` for each release
- **Testing**: Always test with TestPyPI first before publishing to production PyPI
- **Documentation**: Your README.md will be displayed on the PyPI page

## Troubleshooting

### Common Issues:
1. **Package name already exists**: Choose a different name or add a suffix
2. **Version already exists**: Increment the version number
3. **Authentication failed**: Check your API tokens or credentials
4. **Build errors**: Check that all files are properly included in MANIFEST.in

### Package Structure Validation:
```bash
# Check the built package contents
tar -tzf dist/codicent-py-1.3.5.tar.gz
```

## Post-Publication

After successful publication:
1. Update your GitHub repository with tags
2. Update the README installation instructions
3. Consider setting up automated publishing with GitHub Actions

Your package will be available at: https://pypi.org/project/codicent-py/
