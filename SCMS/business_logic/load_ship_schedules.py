import pandas as pd
from backend_layer.database_connection import DatabaseConnection

class LoadShipSchedules:
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def load_schedules(self, ship_name=None, month=None):
        query = "SELECT * FROM Ship_Port_Schedule"
        params = {}

        if ship_name:
            query += " WHERE ship_name = :ship_name"
            params['ship_name'] = ship_name

        if month:
            query += " AND strftime('%m', arrival_time) = :month"
            params['month'] = month

        result = self.db_connection.execute_query(query, params)
        return pd.DataFrame(result)

    def close_connection(self):
        self.db_connection.close_connection()