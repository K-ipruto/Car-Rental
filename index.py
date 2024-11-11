from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route to display the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the reservation form submission
@app.route('/reserve', methods=['POST'])
def reserve():
    # Get form data
    car_type = request.form['car-type']
    pickup_date = request.form['pickup-date']
    dropoff_date = request.form['dropoff-date']

    # Check date validity (simple example, could be more complex)
    if pickup_date > dropoff_date:
        return "Error: Drop-off date must be after pick-up date."

    # Redirect to confirmation page with reservation details
    return render_template('confirmation.html', car_type=car_type, pickup_date=pickup_date, dropoff_date=dropoff_date)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route to display the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the reservation form submission
@app.route('/reserve', methods=['POST'])
def reserve():
    # Get form data
    car_type = request.form['car-type']
    pickup_date = request.form['pickup-date']
    dropoff_date = request.form['dropoff-date']

    # Check date validity (simple example, could be more complex)
    if pickup_date > dropoff_date:
        return "Error: Drop-off date must be after pick-up date."

    # Redirect to confirmation page with reservation details
    return render_template('confirmation.html', car_type=car_type, pickup_date=pickup_date, dropoff_date=dropoff_date)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
