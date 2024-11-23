from run import create_app, db
from app.user import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Example user
    user1 = User(
        full_name="John Doe",
        email="johndoe@example.com",
        password=generate_password_hash("password123", method='pbkdf2:sha256')
    )

    db.session.add(user1)
    db.session.commit()

    print("User added!")
