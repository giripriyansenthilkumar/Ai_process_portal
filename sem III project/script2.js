// Open Login Modal
function openLoginModal() {
    document.getElementById("loginModal").style.display = "flex";
}

// Close Login Modal
function closeLoginModal() {
    document.getElementById("loginModal").style.display = "none";
    document.getElementById("loginStatus").innerText = ""; // Clear status on close
}

// Login Function
function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const loginStatus = document.getElementById("loginStatus");

    if (username === "admin" && password === "password123") {
        loginStatus.style.color = "green";
        loginStatus.innerText = "Login Successful!";
        setTimeout(closeLoginModal, 1000); // Close modal after success
    } else {
        loginStatus.style.color = "red";
        loginStatus.innerText = "Invalid Username or Password!";
    }
}
