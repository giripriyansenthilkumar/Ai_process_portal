// Login functionality
function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const loginMessage = document.getElementById("loginMessage");

    // Placeholder login credentials
    if (username === "admin" && password === "1234") {
        loginMessage.innerText = "Login successful!";
        
        // Show main content and navigation
        document.getElementById("loginSection").style.display = "none";
        document.getElementById("mainHeader").style.display = "block";
        document.getElementById("statusSection").style.display = "block";
        document.getElementById("footer").style.display = "block";
    } else {
        loginMessage.innerText = "Invalid login credentials. Please try again.";
    }
    return false; // Prevent form submission to stay on the same page
}
