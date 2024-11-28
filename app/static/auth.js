document.addEventListener('DOMContentLoaded', function() {
    // Get references to the buttons and modals
    const loginButton = document.getElementById('login-button');
    const signupButton = document.getElementById('signup-button');
    const logoutButton = document.getElementById('logout-button');
    const loginModal = document.getElementById('login-modal');
    const signupModal = document.getElementById('signup-modal');
    const modalOverlay = document.getElementById('modal-overlay');

    // Open Login Modal
    if (loginButton) {
        loginButton.addEventListener('click', function(e) {
            e.preventDefault();
            loginModal.style.display = 'block';
            modalOverlay.style.display = 'block';
        });
    }

    // Open Sign Up Modal
    if (signupButton) {
        signupButton.addEventListener('click', function(e) {
            e.preventDefault();
            signupModal.style.display = 'block';
            modalOverlay.style.display = 'block';
        });
    }

    // Close Modals when clicking on the close button
    const closeButtons = document.querySelectorAll('.close');
    closeButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const modalId = btn.getAttribute('data-modal');
            document.getElementById(modalId).style.display = 'none';
            modalOverlay.style.display = 'none';
        });
    });

    // Close Modals when clicking on the overlay
    modalOverlay.addEventListener('click', function() {
        loginModal.style.display = 'none';
        signupModal.style.display = 'none';
        modalOverlay.style.display = 'none';
    });

    // Handle Login Form Submission
    document.getElementById('login-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;

        fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = '/cars';
            } else {
                alert('Login failed: ' + data.message);
            }
        });
    });

    // Handle Sign Up Form Submission
    document.getElementById('signup-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const full_name = document.getElementById('signup-full-name').value;
        const email = document.getElementById('signup-email').value;
        const password = document.getElementById('signup-password').value;

        fetch('/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ full_name, email, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                // Close Sign Up Modal and Open Login Modal
                document.getElementById('signup-modal').style.display = 'none';
                document.getElementById('login-modal').style.display = 'block';
            } else {
                alert('Registration failed: ' + data.message);
            }
        });
    });

    // Handle Logout
    if (logoutButton) {
        logoutButton.addEventListener('click', function(e) {
            e.preventDefault();
            fetch('/auth/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Logout successful!');
                    window.location.href = '/'; // Redirect to home page
                } else {
                    alert('Logout failed: ' + data.message);
                }
            });
        });
    }
});
