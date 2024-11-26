from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.car import Car
from app.booking import Booking

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book', methods=['POST'])
@login_required
def book_car():
    data = request.get_json()
    car_id = data.get('car_id')
    rental_date = data.get('rental_date')
    return_date = data.get('return_date')

    car = Car.query.get(car_id)
    if not car:
        return jsonify({'success': False, 'message': 'Car not found.'})

    # Check availability
    existing_booking = Booking.query.filter(
        Booking.car_id == car_id,
        Booking.rental_date <= return_date,
        Booking.return_date >= rental_date
    ).first()

    if existing_booking:
        return jsonify({'success': False, 'message': 'Car is not available for the selected dates.'})

    # Create new booking
    new_booking = Booking(
        user_id=current_user.id,
        car_id=car_id,
        rental_date=rental_date,
        return_date=return_date
    )
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Booking successful!'})