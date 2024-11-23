from .. import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default="Pending")
