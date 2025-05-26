# Disclaimer: This output contains AI-generated content; user is advised to review it before consumption.
#*Start of AI Generated Content*

python
# *****************************************
# *                                       *
# *  Constants and Static String Values  *
# *                                       *
# *****************************************

# Database Constants
DB_HOST = 'localhost'
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'

# SQL Queries
SUM_VALUES_QUERY = "SELECT SUM({column_name}) FROM {table_name}"
CALCULATE_AGE_QUERY = "SELECT AGE({birthdate_column}) FROM {table_name} WHERE id = {person_id}"

# Error Messages
DB_CONNECTION_ERROR = "Failed to connect to the database"
INVALID_TABLE_ERROR = "Invalid table name"
INVALID_COLUMN_ERROR = "Invalid column name"


# *****************************************
# *                                       *
# *  PostgreSQL Database Connection      *
# *                                       *
# *****************************************

import psycopg2
from psycopg2 import Error

def establish_db_connection():
    """
    Establish a connection to the PostgreSQL database.

    Returns:
        connection (psycopg2.extensions.connection): Database connection object
    """
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        return connection
    except Error as e:
        print(DB_CONNECTION_ERROR, e)
        return None


# *****************************************
# *                                       *
# *  PostgreSQL Function 1: Sum of Values *
# *                                       *
# *****************************************

def sum_of_values(table_name, column_name):
    """
    Calculate the sum of a group of values in a specified column.

    Args:
        table_name (str): Name of the table
        column_name (str): Name of the column

    Returns:
        sum_of_values (float): Sum of the values in the specified column
    """
    try:
        connection = establish_db_connection()
        if connection:
            cursor = connection.cursor()
            query = SUM_VALUES_QUERY.format(column_name=column_name, table_name=table_name)
            cursor.execute(query)
            sum_of_values = cursor.fetchone()[0]
            connection.close()
            return sum_of_values
    except Error as e:
        print(INVALID_TABLE_ERROR if "relation" in str(e) else INVALID_COLUMN_ERROR, e)
        return None


# *****************************************
# *                                       *
# *  PostgreSQL Function 2: Calculate Age *
# *                                       *
# *****************************************

def calculate_age(table_name, birthdate_column, person_id):
    """
    Calculate the age of a person based on their birthdate.

    Args:
        table_name (str): Name of the table
        birthdate_column (str): Name of the birthdate column
        person_id (int): ID of the person

    Returns:
        age (str): Age of the person
    """
    try:
        connection = establish_db_connection()
        if connection:
            cursor = connection.cursor()
            query = CALCULATE_AGE_QUERY.format(table_name=table_name, birthdate_column=birthdate_column, person_id=person_id)
            cursor.execute(query)
            age = cursor.fetchone()[0]
            connection.close()
            return str(age)
    except Error as e:
        print(INVALID_TABLE_ERROR if "relation" in str(e) else INVALID_COLUMN_ERROR, e)
        return None


# *****************************************
# *                                       *
# *  Example Usage                       *
# *****************************************

if __name__ == "__main__":
    table_name = "employees"
    column_name = "salary"
    birthdate_column = "birthdate"
    person_id = 1

    sum_result = sum_of_values(table_name, column_name)
    print(f"Sum of {column_name} in {table_name}: {sum_result}")

    age_result = calculate_age(table_name, birthdate_column, person_id)
    print(f"Age of person with ID {person_id} in {table_name}: {age_result}")


#*End of AI Generated Content*