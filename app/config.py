import os
from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager


class Config:
    SECRET_KEY = '4dm1n!P@ssword'
    SQLALCHEMY_DATABASE_URI = "sqlite:///quickcar.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///quickcar.db"

app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.user import User
from app.car import Car
from app.booking import Booking

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    with app.app_context():
        db.create_all()  # Create tables

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.auth_routes import auth_bp
    from app.car_routes import car_bp
    app.register_blueprint(auth_bp, url_prefix='/auth') 
    app.register_blueprint(car_bp, url_prefix='/api')

    @app.route('/')
    def serve_index():
        return render_template('index.html')

    @app.route('/cars')
    def serve_cars():
        return render_template('car.html')

    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory('static', path)

    return app