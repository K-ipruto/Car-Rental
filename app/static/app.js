document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('car-list')) {
        fetch('/api/cars')
            .then(response => response.json())
            .then(data => {
                const carList = document.getElementById('car-list');
                carList.innerHTML = ''; // Clear existing content
                data.forEach(car => {
                    const carItem = document.createElement('div');
                    carItem.className = 'car';
                    carItem.innerHTML = `
                        <img src="/static/images/${car.image}" alt="${car.make} ${car.model}">
                        <h3>${car.make} ${car.model} (${car.year})</h3>
                        <p>Brand: ${car.brand}</p>
                        <p>Price: ${car.price}/day</p>
                        <button class="rent-now btn" data-car-id="${car.id}">Rent Now</button>
                    `;

                    // Add event listener to rent button
                    const rentButton = carItem.querySelector('.rent-now');
                    rentButton.addEventListener('click', () => showRentalForm(car));

                    carList.appendChild(carItem);
                });
            })
            .catch(error => {
                console.error('Error fetching cars:', error);
                document.getElementById('car-list').innerHTML = '<p>Error loading cars. Please try again later.</p>';
            });
    }
});

function showRentalForm(car) {
    const rentalForm = document.getElementById('rental-form');
    document.querySelector('.modal-overlay').style.display = 'block';
    rentalForm.style.display = 'block';

    // Reset form fields
    document.getElementById('booking-form').reset();

    // Display car details in form
    const carDetails = document.createElement('div');
    carDetails.innerHTML = `
        <p>Selected Car: ${car.make} ${car.model}</p>
        <p>Price per day: $${car.price}</p>
    `;
    
    const existingDetails = rentalForm.querySelector('.car-details');
    if (existingDetails) {
        existingDetails.remove();
    }
    
    carDetails.className = 'car-details';
    rentalForm.insertBefore(carDetails, document.getElementById('booking-form'));
}

// Add close functionality
document.querySelector('.close-button').addEventListener('click', () => {
    document.querySelector('.modal-overlay').style.display = 'none';
    document.getElementById('rental-form').style.display = 'none';
});

// Close modal when clicking overlay
document.querySelector('.modal-overlay').addEventListener('click', () => {
    document.querySelector('.modal-overlay').style.display = 'none';
    document.getElementById('rental-form').style.display = 'none';
});

// Handle form submission
document.getElementById('booking-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const rentalDate = new Date(document.getElementById('rental-date').value);
    const today = new Date();
    const twoWeeks = new Date();
    twoWeeks.setDate(today.getDate() + 14);
    
    if (rentalDate > twoWeeks) {
        alert('You can only book up to 2 weeks in advance.');
        return;
    }
    
    const bookingDetails = {
        car: document.getElementById('car').value,
        rentalDate: document.getElementById('rental-date').value,
        duration: document.getElementById('duration').value,
        driver: document.getElementById('driver').checked
    };
    
    console.log('Booking Details:', bookingDetails);
    alert('Booking successful!');
    document.getElementById('rental-form').style.display = 'none';
});

// // Handle Login Form Submission
// document.getElementById('login-form').addEventListener('submit', function(e) {
//     e.preventDefault();
//     const email = document.getElementById('login-email').value;
//     const password = document.getElementById('login-password').value;

//     fetch('/auth/login', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ email, password })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             alert('Login successful!');
//             location.reload();
//         } else {
//             alert('Login failed: ' + data.message);
//         }
//     });
// });

// // Handle Register Form Submission
// document.getElementById('register-form').addEventListener('submit', function(e) {
//     e.preventDefault();
//     const full_name = document.getElementById('register-full-name').value;
//     const email = document.getElementById('register-email').value;
//     const password = document.getElementById('register-password').value;

//     fetch('/auth/register', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ full_name, email, password })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             alert('Registration successful! Please log in.');
//             // Close register modal and open login modal
//             document.getElementById('register-modal').style.display = 'none';
//             document.getElementById('login-modal').style.display = 'block';
//         } else {
//             alert('Registration failed: ' + data.message);
//         }
//     });
// });

// Modal functionality
document.addEventListener('DOMContentLoaded', () => {
    const loginModal = document.getElementById('login-modal');
    const registerModal = document.getElementById('register-modal');
    const modalOverlay = document.getElementById('modal-overlay');

    const openLoginBtn = document.getElementById('open-login-modal');
    const openRegisterBtn = document.getElementById('open-register-modal');

    // // Open Login Modal
    // openLoginBtn.addEventListener('click', (e) => {
    //     e.preventDefault();
    //     loginModal.style.display = 'block';
    //     modalOverlay.style.display = 'block';
    // });

    // // Open Register Modal
    // openRegisterBtn.addEventListener('click', (e) => {
    //     e.preventDefault();
    //     registerModal.style.display = 'block';
    //     modalOverlay.style.display = 'block';
    // });

    // Close Modals
    const closeButtons = document.querySelectorAll('.close');
    closeButtons.forEach((btn) => {
        btn.addEventListener('click', () => {
            const modalId = btn.getAttribute('data-modal');
            document.getElementById(modalId).style.display = 'none';
            modalOverlay.style.display = 'none';
        });
    });

    // Close Modals by clicking on overlay
    modalOverlay.addEventListener('click', () => {
        // loginModal.style.display = 'none';
        // registerModal.style.display = 'none';
        modalOverlay.style.display = 'none';
    });
});
