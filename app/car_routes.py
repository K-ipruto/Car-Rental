from flask import Blueprint, request, jsonify
from app import db
from app.car import Car

car_bp = Blueprint('car_bp', __name__)

@car_bp.route('/cars', methods=['GET'])
def get_all_cars():
    cars = Car.query.all()
    cars_list = [
        {
            'id': car.id,
            'brand': car.brand,
            'make': car.make,
            'model': car.model,
            'year': car.year,
            'price': car.price,
            'availability': car.availability,
            'description': car.description,
            'image': car.image
        } for car in cars
    ]
    return jsonify(cars_list)

@car_bp.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    new_car = Car(
        brand=data['brand'],
        make=data['make'],
        model=data['model'],
        year=data['year'],
        price=data['price'],
        availability=data['availability'],
        description=data['description'],
        image=data['image']
    )
    db.session.add(new_car)
    db.session.commit()
    return jsonify({
        'id': new_car.id,
        'brand': new_car.brand,
        'make': new_car.make,
        'model': new_car.model,
        'year': new_car.year,
        'price': new_car.price,
        'availability': new_car.availability,
        'description': new_car.description,
        'image': new_car.image
    }), 201

@car_bp.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    car = Car.query.get(car_id)
    if car:
        car.brand = data.get('brand', car.brand)
        car.make = data.get('make', car.make)
        car.model = data.get('model', car.model)
        car.year = data.get('year', car.year)
        car.price = data.get('price', car.price)
        car.availability = data.get('availability', car.availability)
        car.description = data.get('description', car.description)
        car.image = data.get('image', car.image)
        db.session.commit()
        return jsonify({
            'id': car.id,
            'brand': car.brand,
            'make': car.make,
            'model': car.model,
            'year': car.year,
            'price': car.price,
            'availability': car.availability,
            'description': car.description,
            'image': car.image
        })
    return jsonify({'error': 'Car not found'}), 404