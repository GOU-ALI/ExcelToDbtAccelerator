import pandas as pd
import os

def generate_md(excel_file, model_name, output_dir="./output"):
    df = pd.read_excel(excel_file, sheet_name=None)

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{model_name}_columns.md")

    with open(output_file, 'w') as f:
        f.write(f"# {model_name} Columns\n\n")

        for sheet_name, sheet_df in df.items():
            if sheet_name != 'Table_Descriptions':
                f.write(f"## {sheet_name}\n\n")

                for _, row in sheet_df.iterrows():
                    f.write(f"### {row['Column_Name']}\n")
                    f.write(f"{row['Column_Description']}\n\n")
                    if 'Is_Key' in row and row['Is_Key'] == 'Yes':
                        f.write("- This is a key column (unique and not null)\n\n")

# Add a newline at the end of the file