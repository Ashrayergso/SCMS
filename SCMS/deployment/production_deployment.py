import os
from backend_layer.database_connection import DatabaseConnection

def deploy_production():
    # Set up production database
    prod_db = DatabaseConnection(os.getenv('PROD_DB_URI'))

    # Create tables if they don't exist
    prod_db.create_tables()

    # Start the Streamlit server
    os.system("streamlit run SCMS/frontend_layer/dashboard.py")

if __name__ == "__main__":
    deploy_production()