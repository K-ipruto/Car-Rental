from run import create_app, db
from app.car import Car
from app.booking import Booking
from app.user import User
from datetime import datetime

app = create_app()

with app.app_context():
    # Example booking details
    user = User.query.filter_by(email="johndoe@example.com").first()
    car = Car.query.filter_by(model="Malibu").first()

    if user and car:
        booking = Booking(
            user_id=user.id,
            car_id=car.id,
            booking_date=datetime(2023, 10, 1, 10, 0),  # Example booking date and time
            return_date=datetime(2023, 10, 5, 10, 0)    # Example return date and time
        )

        db.session.add(booking)
        db.session.commit()

        print("Booking added!")
    else:
        print("User or Car not found!")
