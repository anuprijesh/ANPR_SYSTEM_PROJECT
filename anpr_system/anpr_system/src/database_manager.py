import pandas as pd
from .config import DATABASE_PATH

class DatabaseManager:
    def __init__(self):
        self.db = pd.read_csv(DATABASE_PATH)

    def get_vehicle_info(self, plate_number):
        match = self.db[self.db['plate_number'] == plate_number]
        if not match.empty:
            return match.iloc[0].to_dict()
        return None