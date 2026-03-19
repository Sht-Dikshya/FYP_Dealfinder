const API_BASE_URL = 'http://127.0.0.1:8000/api/';

document.addEventListener('DOMContentLoaded', () => {
    
    // Toggle Password Visibility
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    togglePasswordButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const input = this.previousElementSibling;
            if (input.type === 'password') {
                input.type = 'text';
                this.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                input.type = 'password';
                this.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });
    });

    // Handle Wishlist Toggle
    const wishlistButtons = document.querySelectorAll('.btn-wishlist');
    wishlistButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent navigating if wrapped in a link
            this.classList.toggle('active');
            this.classList.toggle('fas'); // solid heart
            this.classList.toggle('far'); // regular heart
            
            if (this.classList.contains('active')) {
                console.log('Added to wishlist');
                alert('Item added to wishlist (Simulation)');
                // Normally an API call here: fetch('/api/users/wishlist/', {method: 'POST'...})
            } else {
                console.log('Removed from wishlist');
                alert('Item removed from wishlist (Simulation)');
                // API call here: fetch('/api/users/wishlist/<id>/', {method: 'DELETE'...})
            }
        });
    });

    // Handle Login
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = loginForm.querySelector('input[type="text"]').value;
            const password = loginForm.querySelector('input[type="password"]').value;
            
            try {
                const response = await fetch(`${API_BASE_URL}users/login/`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({username, password})
                });
                const data = await response.json();
                if (response.ok) {
                    localStorage.setItem('token', data.token);
                    alert("Login successful!");
                    window.location.href = 'index.html';
                } else {
                    alert('Login failed: ' + JSON.stringify(data));
                }
            } catch (err) {
                console.error(err);
                alert("Error connecting to server.");
            }
        });
    }

    // Handle Signup
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const inputs = signupForm.querySelectorAll('input');
            const username = inputs[0].value;
            const email = inputs[1].value;
            const password = inputs[2].value;
            const confirmPassword = inputs[3].value;

            if (password !== confirmPassword) {
                alert("Passwords do not match!");
                return;
            }
            
            try {
                const response = await fetch(`${API_BASE_URL}users/register/`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({username, email, password})
                });
                if (response.ok) {
                    alert("Registration successful! Please login.");
                    window.location.href = 'login.html';
                } else {
                    const data = await response.json();
                    alert('Signup failed: ' + JSON.stringify(data));
                }
            } catch (err) {
                console.error(err);
                alert("Error connecting to server.");
            }
        });
    }

    /* 
     * In a real environment with backend running, the products would be populated like this:
     * fetch(`${API_BASE_URL}products/`)
     *   .then(res => res.json())
     *   .then(data => renderProducts(data));
     */

});
