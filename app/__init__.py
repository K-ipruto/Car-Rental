from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///quickcar.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.auth_routes import auth_bp
    from app.car_routes import car_bp
    from app.booking_routes import booking_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(car_bp, url_prefix='/api')
    app.register_blueprint(booking_bp, url_prefix='/bookings')

    @app.route('/')
    def serve_index():
        return send_from_directory('static', 'index.html')

    @app.route('/cars')
    def serve_cars():
        return send_from_directory('static', 'car.html')

    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory('static', path)
    
    # Set up Flask-Admin
    admin = Admin(app, name='QuickCar Rentals Admin', template_mode='bootstrap3')
    from app.user import User
    from app.car import Car
    from app.booking import Booking
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Car, db.session))
    admin.add_view(ModelView(Booking, db.session))

    return app