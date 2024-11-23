from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.booking import Booking
from app.car import Car

booking_bp = Blueprint('booking', __name__, url_prefix='/bookings')

@booking_bp.route('/<int:car_id>', methods=['GET', 'POST'])
@login_required
def book_car(car_id):
    car = Car.query.get_or_404(car_id)
    if request.method == 'POST':
        booking_date = request.form['booking_date']
        return_date = request.form['return_date']

        new_booking = Booking(user_id=current_user.id, car_id=car_id, booking_date=booking_date, return_date=return_date)
        db.session.add(new_booking)
        db.session.commit()
        flash("Booking successful!")
        return redirect(url_for('booking.view_bookings'))

    return render_template('bookings/booking_form.html', car=car)

@booking_bp.route('/view', methods=['GET'])
@login_required
def view_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('bookings/booking_history.html', bookings=bookings)