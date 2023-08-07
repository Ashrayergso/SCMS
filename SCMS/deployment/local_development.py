import os
from backend_layer.database_connection import DatabaseConnection
from frontend_layer.streamlit import run_streamlit_app

def run_local_development():
    # Set up database connection
    db_connection = DatabaseConnection()
    db_connection.setup()

    # Run Streamlit app
    run_streamlit_app()

if __name__ == "__main__":
    run_local_development()