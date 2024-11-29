// Toggle Sidebar Menu
function toggleMenu() {
    const sidebar = document.getElementById('sidebarMenu');
    sidebar.classList.toggle('active');
    document.getElementById('mainContent').classList.toggle('centered');
}

// Close sidebar when clicking outside of it
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebarMenu');
    const menuIcon = document.querySelector('.menu-icon');
    const isClickInside = sidebar.contains(event.target) || menuIcon.contains(event.target);

    if (!isClickInside) {
        sidebar.classList.remove('active');
        document.getElementById('mainContent').classList.remove('centered');
    }
});

// Close the login popup
document.getElementById('closePopup').addEventListener('click', function() {
    document.getElementById('loginPopup').style.display = 'none';
});

// Show login popup when login link is clicked
function showLoginPopup() {
    document.getElementById('loginPopup').style.display = 'flex';
}

// Check login state on page load
window.onload = function() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');

    // Show login popup if the user is not logged in
    if (!isLoggedIn) {
        document.getElementById('loginPopup').style.display = 'flex';
    } else {
        document.getElementById('loginLink').style.display = 'none'; // Hide login link
        document.getElementById('logoutLink').style.display = 'block'; // Show logout link
        document.getElementById('profileIcon').style.display = 'block'; // Show profile icon
    }
};

// Simulate login
function login() {
    localStorage.setItem('isLoggedIn', 'true');
    document.getElementById('loginLink').style.display = 'none'; // Hide login link
    document.getElementById('logoutLink').style.display = 'block'; // Show logout link
    document.getElementById('profileIcon').style.display = 'block'; // Show profile icon
    document.getElementById('loginPopup').style.display = 'none'; // Close login popup
}

// Simulate logout
function logout() {
    localStorage.removeItem('isLoggedIn');
    document.getElementById('loginLink').style.display = 'block'; // Show login link
    document.getElementById('logoutLink').style.display = 'none'; // Hide logout link
    document.getElementById('profileIcon').style.display = 'none'; // Hide profile icon
}
