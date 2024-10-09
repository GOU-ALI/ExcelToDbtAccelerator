#!/bin/bash

# Set strict mode
set -euo pipefail

# Configuration
PROJECT_ROOT=$(dirname "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)")
EXCEL_FILE="$PROJECT_ROOT/tests/test_dbt_spark_accelerator.xlsx"
OUTPUT_DIR="$PROJECT_ROOT/output"
MODEL_NAME="test_model"
VENV_DIR="$PROJECT_ROOT/etda_env"

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Function to check if a directory is empty
is_directory_empty() {
    [ -z "$(ls -A "$1")" ]
}

# Check if Excel file exists
if [ ! -f "$EXCEL_FILE" ]; then
    echo "Error: Excel file not found at $EXCEL_FILE"
    exit 1
fi

# Check if output directory exists, if not create it
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
    echo "Created output directory: $OUTPUT_DIR"
else
    # Check if output directory is not empty
    if ! is_directory_empty "$OUTPUT_DIR"; then
        echo "Warning: Output directory is not empty. Existing files may be overwritten."
        read -p "Do you want to continue? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Operation cancelled by user."
            exit 1
        fi
    fi
fi

# Run the Python script to generate files
echo "Generating files..."
python3 -c "
import sys
sys.path.append('$PROJECT_ROOT')
from etda.md_generator import generate_md
from etda.schema_generator import generate_schema

generate_md('$EXCEL_FILE', '$MODEL_NAME', '$OUTPUT_DIR')
generate_schema('$EXCEL_FILE', '$MODEL_NAME', '$OUTPUT_DIR')
"

# Check if files were generated
MD_FILE="$OUTPUT_DIR/${MODEL_NAME}_columns.md"
SCHEMA_FILE="$OUTPUT_DIR/${MODEL_NAME}_schema.yml"

if [ -f "$MD_FILE" ] && [ -f "$SCHEMA_FILE" ]; then
    echo "Success: Files generated successfully!"
    echo "Markdown file: $MD_FILE"
    echo "Schema file: $SCHEMA_FILE"
else
    echo "Error: File generation failed. Please check the Python scripts for errors."
    exit 1
fi

# Deactivate virtual environment
deactivate

echo "Test completed successfully!"