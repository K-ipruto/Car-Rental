from app import create_app

# Initialize the Flask application
app = create_app()

if __name__ == "__main__":
    # Run in debug mode for local development
    app.run(debug=True)
