from run import create_app, db
from app.car import Car

app = create_app()

with app.app_context():
    cars = Car.query.all()
    for car in cars:
        print(car.brand, car.model, car.year)
