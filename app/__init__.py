from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///quickcar.db"

    db.init_app(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'

    from app.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.auth_routes import auth_bp
    from app.car_routes import car_bp
    from app.booking_routes import booking_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(car_bp, url_prefix='/api')
    app.register_blueprint(booking_bp)

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