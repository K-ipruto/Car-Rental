from flask import Blueprint, request, jsonify
from app.models import CarManager

car_bp = Blueprint('car_bp', __name__)
car_manager = CarManager()

@car_bp.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(car_manager.get_all_cars())

@car_bp.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    car = car_manager.add_car(
        make=data['make'],
        model=data['model'],
        year=data['year']
    )
    return jsonify(car), 201

@car_bp.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    car = car_manager.update_car(car_id, data)
    if car:
        return jsonify(car)
    return jsonify({'error': 'Car not found'}), 404