# ETDA (Excel To DBT Accelerator)

ETDA is a powerful Python tool designed to accelerate the process of creating DBT (Data Build Tool) models and documentation from Excel-based table definitions. By automating the generation of DBT schema files and markdown documentation, ETDA significantly reduces setup time and ensures consistency in data modeling practices.

## Features

- Automatically generates DBT schema YAML files from Excel inputs
- Creates markdown documentation for easy reference
- Streamlines the process of setting up DBT projects
- Ensures consistency between data definitions and DBT configurations

## Installation

```bash
pip install etda
```

## Quick Start

```python
from etda import generate_schema, generate_md

# Generate schema and documentation
generate_schema("path/to/your/excel_file.xlsx", "your_model_name")
generate_md("path/to/your/excel_file.xlsx", "your_model_name")
```

For more detailed usage instructions, please refer to the [documentation](docs/usage.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.