document.addEventListener('DOMContentLoaded', function() {
    const bookingForm = document.getElementById('booking-form');

    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const carId = document.getElementById('car').value;
            const rentalDate = document.getElementById('rental-date').value;
            const returnDate = document.getElementById('return-date').value;

            fetch('/api/bookings/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    car_id: carId,
                    rental_date: rentalDate,
                    return_date: returnDate
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Booking successful!');
                    // Optionally, close the modal or reset the form
                    document.getElementById('rental-form').style.display = 'none';
                    document.querySelector('.modal-overlay').style.display = 'none';
                    bookingForm.reset();
                } else {
                    alert('Booking failed: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while booking the car.');
            });
        });
    }
});