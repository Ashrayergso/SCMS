import pandas as pd
from backend_layer.database_connection import DatabaseConnection

class LoadShipSchedule:
    def __init__(self, ship_name, month):
        self.ship_name = ship_name
        self.month = month
        self.db = DatabaseConnection()

    def load_schedule(self):
        query = f"SELECT * FROM ship_port_schedule WHERE ship_name = '{self.ship_name}' AND strftime('%m', date) = '{self.month}'"
        result = self.db.execute_query(query)
        df = pd.DataFrame(result, columns=['id', 'ship_code', 'date', 'port_code'])
        return df