<?php
// Database configuration
$host = 'localhost';
$dbname = 'ai_approval';
$username = 'root';
$password = '';

// Establish database connection
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


// Process registration request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $inputUsername = $_POST['username'];
    $inputEmail = $_POST['email'];
    $inputPhone = $_POST['phone'];
    $inputDob = $_POST['dob'];
    $inputPassword = $_POST['password'];
    $confirmPassword = $_POST['confirmPassword'];
    

    // Verify Google reCAPTCHA
    $response = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=$recaptchaSecret&response=$recaptchaResponse");
    $responseKeys = json_decode($response, true);
    if (!$responseKeys["success"]) {
        echo json_encode(['status' => 'error', 'message' => 'reCAPTCHA validation failed.']);
        exit;
    }

    // Check if passwords match
    if ($inputPassword !== $confirmPassword) {
        echo json_encode(['status' => 'error', 'message' => 'Passwords do not match.']);
        exit;
    }

    // Check if username or email already exists
    $stmt = $conn->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
    $stmt->bind_param("ss", $inputUsername, $inputEmail);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        echo json_encode(['status' => 'error', 'message' => 'Username or email already exists.']);
    } else {
        // Hash the password
        $hashedPassword = password_hash($inputPassword, PASSWORD_DEFAULT);

        // Insert new user into the database
        $stmt = $conn->prepare("INSERT INTO users (username, email, phone, dob, password) VALUES (?, ?, ?, ?, ?)");
        $stmt->bind_param("sssss", $inputUsername, $inputEmail, $inputPhone, $inputDob, $hashedPassword);

        if ($stmt->execute()) {
            echo json_encode(['status' => 'success', 'message' => 'Registration successful!']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Error registering user.']);
        }
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}
?>