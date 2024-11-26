from run import create_app
from app.car import Car

app = create_app()

with app.app_context():
    cars = Car.query.all()
    if cars:
        for car in cars:
            print(f"Car ID: {car.id}, Model: {car.model}, Make: {car.make}, Brand: {car.brand}")
    else:
        print("No cars found in the database.")