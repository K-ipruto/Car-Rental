# QuickCar Rentals

A web-based car rental system built with Flask and JavaScript that allows users to browse, rent, and manage car rentals.

## Features

- Browse available cars with details and images
- Real-time car booking system
- User authentication and authorization
- Interactive rental form with date validation
- Responsive design for all devices

## Tech Stack

- Backend:
  - Python 3.x
  - Flask
  - SQLAlchemy
  - JWT Authentication

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (Vanilla)

## Installation

1. Clone the repository:
    ``git clone <repository-url>``

2. Install Python dependencies:
``pip install -r requirements.txt``

3. Run the application:
``Run the application:``

## Project Structure
app/
├── __init__.py
├── models.py
├── database.json
├── auth_routes.py
├── car_routes.py
├── config.py
└── static/
    ├── index.html
    ├── car.html
    ├── index.css
    └── app.js


## API Endpoints:

- ``GET /api/cars`` - Get all available cars
- ``POST /api/cars`` - Add a new car
- ``PUT /api/cars/<car_id>`` - Update car details
- ``POST /reserve`` - Make a car reservation

## Contributing

to-do

## Licence

to-do
