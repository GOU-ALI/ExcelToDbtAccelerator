import unittest
import os
import pandas as pd
from etda.md_generator import generate_md

class TestMdGenerator(unittest.TestCase):
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

    def test_generate_md(self):
        generate_md(self.test_excel, 'test_model', self.test_output)

        output_file = os.path.join(self.test_output, 'test_model_columns.md')
        self.assertTrue(os.path.exists(output_file))

        with open(output_file, 'r') as f:
            content = f.read()

        self.assertIn("# test_model Columns", content)
        self.assertIn("## users", content)
        self.assertIn("### id", content)
        self.assertIn("User ID", content)
        self.assertIn("This is a key column (unique and not null)", content)

    def tearDown(self):
        os.remove(self.test_excel)
        for file in os.listdir(self.test_output):
            os.remove(os.path.join(self.test_output, file))
        os.rmdir(self.test_output)

if __name__ == '__main__':
    unittest.main()

