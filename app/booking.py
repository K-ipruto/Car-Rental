from . import db
from flask_login import UserMixin

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default="Pending")

    def __repr__(self):
        return f"<Booking {self.id} - User {self.user_id}, Car {self.car_id}>"
