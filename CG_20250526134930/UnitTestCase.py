# Disclaimer: This output contains AI-generated content; user is advised to review it before consumption.
#*Start of AI Generated Content*

python
# *****************************************
# *                                       *
# *  Unit Test Cases for PostgreSQL DB   *
# *                                       *
# *****************************************

python
import unittest
from unittest.mock import patch, MagicMock
from your_module import (  # Replace 'your_module' with the actual module name
    establish_db_connection,
    sum_of_values,
    calculate_age,
    DB_HOST, DB_NAME, DB_USER, DB_PASSWORD,
    DB_CONNECTION_ERROR, INVALID_TABLE_ERROR, INVALID_COLUMN_ERROR
)


class TestPostgreSQLDBFunctions(unittest.TestCase):

    # *****************************************
    # *                                       *
    # *  Test Database Connection            *
    # *                                       *
    # *****************************************

    def test_establish_db_connection_success(self):
        """
        Test successful database connection establishment.
        
        Verifies:
            - Connection object is returned when credentials are correct.
        """
        with patch('psycopg2.connect') as mock_connect:
            mock_connect.return_value = MagicMock()
            connection = establish_db_connection()
            self.assertIsNotNone(connection)

    def test_establish_db_connection_failure(self):
        """
        Test failed database connection establishment.
        
        Verifies:
            - None is returned when connection fails (e.g., incorrect credentials).
            - Error message is printed.
        """
        with patch('psycopg2.connect') as mock_connect:
            mock_connect.side_effect = Exception('Mocked connection error')
            with patch('builtins.print') as mock_print:
                connection = establish_db_connection()
                self.assertIsNone(connection)
                mock_print.assert_called_once_with(DB_CONNECTION_ERROR, 'Mocked connection error')


    # *****************************************
    # *                                       *
    # *  Test Sum of Values Function         *
    # *                                       *
    # *****************************************

    def test_sum_of_values_valid_input(self):
        """
        Test sum of values with valid table and column names.
        
        Verifies:
            - Correct sum is returned for existing table and column.
        """
        table_name = 'employees'
        column_name = 'salary'
        mock_sum_value = 1000.0  # Example sum value
        with patch('psycopg2.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_connection.cursor().fetchone.return_value = [mock_sum_value]
            mock_connect.return_value = mock_connection
            result = sum_of_values(table_name, column_name)
            self.assertAlmostEqual(result, mock_sum_value)

    def test_sum_of_values_invalid_table(self):
        """
        Test sum of values with an invalid table name.
        
        Verifies:
            - None is returned for non-existent table.
            - Error message for invalid table is printed.
        """
        table_name = 'non_existent_table'
        column_name = 'salary'
        with patch('psycopg2.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_connection.cursor().execute.side_effect = Exception('relation "non_existent_table" does not exist')
            mock_connect.return_value = mock_connection
            with patch('builtins.print') as mock_print:
                result = sum_of_values(table_name, column_name)
                self.assertIsNone(result)
                mock_print.assert_called_once_with(INVALID_TABLE_ERROR, mock_connection.cursor().execute.side_effect)

    def test_sum_of_values_invalid_column(self):
        """
        Test sum of values with an invalid column name.
        
        Verifies:
            - None is returned for non-existent column.
            - Error message for invalid column is printed.
        """
        table_name = 'employees'
        column_name = 'non_existent_column'
        with patch('psycopg2.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_connection.cursor().execute.side_effect = Exception('column "non_existent_column" does not exist')
            mock_connect.return_value = mock_connection
            with patch('builtins.print') as mock_print:
                result = sum_of_values(table_name, column_name)
                self.assertIsNone(result)
                mock_print.assert_called_once_with(INVALID_COLUMN_ERROR, mock_connection.cursor().execute.side_effect)


    # *****************************************
    # *                                       *
    # *  Test Calculate Age Function         *
    # *                                       *
    # *****************************************

    def test_calculate_age_valid_input(self):
        """
        Test calculate age with valid table, birthdate column, and person ID.
        
        Verifies:
            - Correct age is returned for existing inputs.
        """
        table_name = 'employees'
        birthdate_column = 'birthdate'
        person_id = 1
        mock_age = '30 years'  # Example age string
        with patch('psycopg2.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_connection.cursor().fetchone.return_value = [mock_age]
            mock_connect.return_value = mock_connection
            result = calculate_age(table_name, birthdate_column, person_id)
            self.assertEqual(result, mock_age)

    def test_calculate_age_invalid_table(self):
        """
        Test calculate age with an invalid table name.
        
        Verifies:
            - None is returned for non-existent table.
            - Error message for invalid table is printed.
        """
        table_name = 'non_existent_table'
        birthdate_column = 'birthdate'
        person_id = 1
        with patch('psycopg2.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_connection.cursor().execute.side_effect = Exception('relation "non_existent_table" does not exist')
            mock_connect.return_value = mock_connection
            with patch('builtins.print') as mock_print:
                result = calculate_age(table_name, birthdate_column, person_id)
                self.assertIsNone(result)
                mock_print.assert_called_once_with(INVALID_TABLE_ERROR, mock_connection.cursor().execute.side_effect)

    def test_calculate_age_invalid_column(self):
        """
        Test calculate age with an invalid birthdate column name.
        
        Verifies:
            - None is returned for non-existent column.
            - Error message for invalid column is printed.
        """
        table_name = 'employees'
        birthdate_column = 'non_existent_column'
        person_id = 1
        with patch('psycopg2.connect') as mock_connect:
            mock_connection = MagicMock()
            mock_connection.cursor().execute.side_effect = Exception('column "non_existent_column" does not exist')
            mock_connect.return_value = mock_connection
            with patch('builtins.print') as mock_print:
                result = calculate_age(table_name, birthdate_column, person_id)
                self.assertIsNone(result)
                mock_print.assert_called_once_with(INVALID_COLUMN_ERROR, mock_connection.cursor().execute.side_effect)


if __name__ == "__main__":
    unittest.main()


#*End of AI Generated Content*