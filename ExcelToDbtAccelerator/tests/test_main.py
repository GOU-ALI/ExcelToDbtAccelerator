import unittest
from unittest.mock import patch
from io import StringIO
import sys
from etda.main import main

class TestMain(unittest.TestCase):
    @patch('etda.main.generate_schema')
    @patch('etda.main.generate_md')
    def test_main(self, mock_generate_md, mock_generate_schema):
        test_args = ['main.py', 'test.xlsx', 'test_model', '--output-dir', 'test_output']
        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            sys.stdout = captured_output
            main()
            sys.stdout = sys.__stdout__

        mock_generate_schema.assert_called_once_with('test.xlsx', 'test_model', 'test_output')
        mock_generate_md.assert_called_once_with('test.xlsx', 'test_model', 'test_output')
        self.assertIn("Files generated successfully in test_output", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()