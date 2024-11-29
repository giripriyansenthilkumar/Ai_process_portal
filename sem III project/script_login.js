// Login Function
function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const loginStatus = document.getElementById("loginStatus");

    if (username === "admin" && password === "password123") {
        loginStatus.style.color = "green";
        loginStatus.innerText = "Login Successful!";
        setTimeout(() => {
            window.location.href = "home_ai.html"; // Redirect after successful login
        }, 1000);
    } else {
        loginStatus.style.color = "red";
        loginStatus.innerText = "Invalid Username or Password!";
    }
}
