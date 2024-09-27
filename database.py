from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
USERNAME = os.getenv('POSTGRES_USERNAME')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')
DATABASE = os.getenv('POSTGRES_DATABASE')

DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as connection:
            # Test a simple query
            result = connection.execute(text("SELECT 1"))
            print("Database connection successful!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

def get_data_length():
    # Use text() for SQL query execution
    query = text("SELECT COUNT(*) FROM passengers")
    try:
        with engine.connect() as connection:
            result = connection.execute(query)
            row_count = result.scalar()
    except Exception as e:
        print(f"Error executing query: {e}")
        row_count = None
    return row_count

def load_data_from_postgres():
    # Load data from PostgreSQL
    query = text("SELECT * FROM passengers")
    try:
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
            # df = df.drop('age', axis=1)
    except Exception as e:
        print(f"Error loading data from PostgreSQL: {e}")
        df = pd.DataFrame()
    return df

print(load_data_from_postgres())