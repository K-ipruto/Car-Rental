from run import create_app
from app.user import User

app = create_app()

with app.app_context():
    users = User.query.all()
    if users:
        for user in users:
            print(f"User ID: {user.id}, Email: {user.email}, Name: {user.full_name}")
    else:
        print("No users found in the database.")