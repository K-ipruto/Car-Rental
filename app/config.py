import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.car_routes import car_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(car_bp, url_prefix='/api')

    return app