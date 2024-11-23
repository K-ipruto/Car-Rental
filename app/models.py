import json
import os
from datetime import datetime

class Database:
    def __init__(self, file_path='app/database.json'):
        self.file_path = file_path
        self.ensure_database_exists()

    def ensure_database_exists(self):
        if not os.path.exists(self.file_path):
            self.save_data({
                'users': [],
                'cars': [],
                'rentals': []
            })

    def load_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

class CarManager:
    def __init__(self):
        self.db = Database()

    def add_car(self, make, model, year):
        data = self.db.load_data()
        car_id = len(data['cars']) + 1
        car = {
            'id': car_id,
            'make': make,
            'model': model,
            'year': year,
            'available': True
        }
        data['cars'].append(car)
        self.db.save_data(data)
        return car

    def get_all_cars(self):
        data = self.db.load_data()
        return data['cars']

    def get_car(self, car_id):
        data = self.db.load_data()
        return next((car for car in data['cars'] if car['id'] == car_id), None)

    def update_car(self, car_id, updates):
        data = self.db.load_data()
        for car in data['cars']:
            if car['id'] == car_id:
                car.update(updates)
                self.db.save_data(data)
                return car
        return None