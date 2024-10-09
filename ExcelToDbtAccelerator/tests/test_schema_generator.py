import unittest
import os
import pandas as pd
import yaml
from etda.schema_generator import generate_schema

class TestSchemaGenerator(unittest.TestCase):
    def setUp(self):
        self.test_excel = 'test_data.xlsx'
        self.test_output = 'test_output'
        os.makedirs(self.test_output, exist_ok=True)

        # Create test Excel file
        data = {
            'Column_Name': ['id', 'name'],
            'Column_Description': ['User ID', 'User Name'],
            'Is_Key': ['Yes', 'No']
        }
        df = pd.DataFrame(data)
        with pd.ExcelWriter(self.test_excel) as writer:
            df.to_excel(writer, sheet_name='users', index=False)

    def test_generate_schema(self):
        generate_schema(self.test_excel, 'test_model', self.test_output)

        output_file = os.path.join(self.test_output, 'test_model_schema.yml')
        self.assertTrue(os.path.exists(output_file))

        with open(output_file, 'r') as f:
            schema = yaml.safe_load(f)

        self.assertEqual(schema['version'], 2)
        self.assertEqual(len(schema['models']), 1)
        self.assertEqual(schema['models'][0]['name'], 'users')
        self.assertEqual(len(schema['models'][0]['columns']), 2)
        self.assertEqual(schema['models'][0]['columns'][0]['name'], 'id')
        self.assertIn('unique', schema['models'][0]['columns'][0]['tests'])
        self.assertIn('not_null', schema['models'][0]['columns'][0]['tests'])

    def tearDown(self):
        os.remove(self.test_excel)
        for file in os.listdir(self.test_output):
            os.remove(os.path.join(self.test_output, file))
        os.rmdir(self.test_output)

if __name__ == '__main__':
    unittest.main()


