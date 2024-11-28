# QuickCar Rentals

This application is a Car Rental System that allows users to browse available cars, create accounts, log in, make bookings, and manage their reservations. The system includes both frontend and backend components, providing a seamless user experience for renting cars online.

## Features

- Browse available cars with details and images
- Real-time car booking system
- User authentication and authorization
- Interactive rental form with date validation
- Responsive design for all devices

## Installation

1. Clone the repository:
    ``git clone <repository-url>``

2. Install Python dependencies:
``pip install -r requirements.txt``

3. Run the application:
``flask run``

## Tech Stack:

- **Backend:** Flask (Python) with SQLAlchemy for database and ORM management.
- **Frontend:** HTML, CSS, JavaScript.
- **Database:** SQLite/PostgreSQL (or mention what you use).
- **Production Setup:** Gunicorn with WSGI.
- **Authentication & Security:** flask-login, flask-Bcrypt


## API Endpoints:

- ``GET /api/cars`` - Get all available cars
- ``POST /api/cars`` - Add a new car
- ``PUT /api/cars/<car_id>`` - Update car details
- ``POST /reserve`` - Make a car reservation

## Contributing

to-do

## Licence

to-do
