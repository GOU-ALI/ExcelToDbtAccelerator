#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Print current directory
echo "Current directory: $(pwd)"

# List contents of current directory
echo "Directory contents:"
ls -la

# Check if virtual environment exists
if [ ! -d "etda_env" ]; then
    echo "Virtual environment 'etda_env' not found. Please create it first."
    exit 1
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source etda_env/bin/activate

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "pytest could not be found. Installing it now..."
    pip install pytest
fi

# Run the tests
echo "Running tests..."
python -m pytest tests/ || { echo "Tests failed"; exit 1; }

# Check if flake8 is installed
if ! command -v flake8 &> /dev/null; then
    echo "flake8 could not be found. Installing it now..."
    pip install flake8
fi

# Run flake8 for code style checking
echo "Running flake8..."
flake8 src/ tests/ || { echo "Flake8 check failed"; exit 1; }

# Check if mypy is installed
if ! command -v mypy &> /dev/null; then
    echo "mypy could not be found. Installing it now..."
    pip install mypy
fi

# Run mypy for type checking
echo "Running mypy..."
mypy src/ tests/ || { echo "Mypy check failed"; exit 1; }

# Deactivate the virtual environment
deactivate

echo "All tests and checks completed successfully!"