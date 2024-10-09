import argparse
from .schema_generator import generate_schema
from .md_generator import generate_md



def main():
    parser = argparse.ArgumentParser(description="ETDA - Excel To DBT Accelerator")
    parser.add_argument("excel_file", help="Path to the Excel file containing table definitions")
    parser.add_argument("model_name", help="Name of the DBT model")
    parser.add_argument("--output-dir", default="./output", help="Directory to output generated files")

    args = parser.parse_args()

    generate_schema(args.excel_file, args.model_name, args.output_dir)
    generate_md(args.excel_file, args.model_name, args.output_dir)

    print(f"Files generated successfully in {args.output_dir}")



if __name__ == "__main__":
    main()