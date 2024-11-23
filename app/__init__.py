from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SECRET_KEY'] = 'your-secret-key'

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # from app.auth_routes import auth_bp
    from app.car_routes import car_bp
    
    # app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(car_bp, url_prefix='/api')

    @app.route('/')
    def serve_index():
        return send_from_directory('static', 'index.html')

    @app.route('/cars')
    def serve_cars():
        return send_from_directory('static', 'car.html')

    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory('static', path)

    return app