from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from booking import Booking
from car import Car
from .. import db

booking_bp = Blueprint('booking', __name__, url_prefix='/bookings')

@booking_bp.route('/<int:car_id>', methods=['GET', 'POST'])
def book_car(car_id):
    if 'user_id' not in session:
        flash("Please log in to book a car.")
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        booking_date = request.form['booking_date']
        return_date = request.form['return_date']
        user_id = session['user_id']

        new_booking = Booking(user_id=user_id, car_id=car_id, booking_date=booking_date, return_date=return_date)
        db.session.add(new_booking)
        db.session.commit()
        flash("Booking successful!")
        return redirect(url_for('booking.view_bookings'))

    car = Car.query.get_or_404(car_id)
    return render_template('bookings/booking_form.html', car=car)

@booking_bp.route('/')
def view_bookings():
    if 'user_id' not in session:
        flash("Please log in to view your bookings.")
        return redirect(url_for('auth.login'))
    
    bookings = Booking.query.filter_by(user_id=session['user_id']).all()
    return render_template('bookings/booking_history.html', bookings=bookings)
