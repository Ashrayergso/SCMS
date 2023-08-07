import pandas as pd
from backend_layer.database_connection import DatabaseConnection

class PandasIntegration:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def load_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        data = self.db_connection.execute_query(query)
        df = pd.DataFrame(data)
        return df

    def filter_data(self, df, column_name, value):
        filtered_df = df[df[column_name] == value]
        return filtered_df

    def analyze_data(self, df):
        # This is a placeholder for any specific analysis required
        analysis_result = df.describe()
        return analysis_result
