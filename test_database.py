import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from database import load_data_from_postgres  # Adjust this import based on your file structure

class TestLoadDataFromPostgresQA(unittest.TestCase):

    @patch('database.pd.read_sql')
    @patch('database.engine.connect')
    def test_columns_exist(self, mock_connect, mock_read_sql):
        # Mock the connection and the DataFrame returned by read_sql
        mock_connection = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_connection

        # Create a sample DataFrame with the expected columns
        sample_data = {
            'passengerid': [1],
            'survived': [0],
            'pclass': [3],
            'name': ['Braund, Mr. Owen Harris'],
            'sex': ['male'],
            'age': [22.0],
            'sibsp': [1],
            'parch': [0],
            'ticket': ['A/5 21171'],
            'fare': [7.2500],
            'cabin': [None],
            'embarked': ['S']
        }
        mock_read_sql.return_value = pd.DataFrame(sample_data)

        # Call the function
        df = load_data_from_postgres()

        # Define the expected columns
        expected_columns = {'passengerid', 'survived', 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked'}

        # Check if all expected columns are in the DataFrame
        self.assertTrue(expected_columns.issubset(df.columns), "Not all expected columns are present in the DataFrame")

if __name__ == '__main__':
    unittest.main()
