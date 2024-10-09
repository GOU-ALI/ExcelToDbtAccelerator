import pandas as pd
import yaml
import os

def generate_schema(excel_file, model_name, output_dir="./output"):
    df = pd.read_excel(excel_file, sheet_name=None)

    schema = {
        'version': 2,
        'models': []
    }

    for sheet_name, sheet_df in df.items():
        if sheet_name != 'Table_Descriptions':
            model = {
                'name': sheet_name,
                'columns': []
            }

            for _, row in sheet_df.iterrows():
                column = {
                    'name': row['Column_Name'],
                    'description': row['Column_Description'],
                    'tests': []
                }

                if 'Is_Key' in row and row['Is_Key'] == 'Yes':
                    column['tests'].extend(['unique', 'not_null'])

                model['columns'].append(column)

            schema['models'].append(model)

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{model_name}_schema.yml")
    with open(output_file, 'w') as f:
        yaml.dump(schema, f, sort_keys=False)