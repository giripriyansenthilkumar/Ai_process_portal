function handleRegister(event) {
    event.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const registerMessage = document.getElementById('registerMessage');

    if (password !== confirmPassword) {
        registerMessage.style.color = 'red';
        registerMessage.textContent = 'Passwords do not match.';
        return;
    }

    const formData = new FormData(document.getElementById('registerForm'));
    fetch('register.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            registerMessage.style.color = 'green';
            registerMessage.textContent = data.message;
            // Optionally, redirect to login page
            // window.location.href = 'login.html';
        } else {
            registerMessage.style.color = 'red';
            registerMessage.textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
