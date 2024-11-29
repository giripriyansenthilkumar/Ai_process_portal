const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors'); // Import CORS

// Connect to MongoDB
mongoose.connect('mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/Applicant_person_details', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('MongoDB connection error:', err));

// Define a schema for registration with unique constraints
const registrationSchema = new mongoose.Schema({
    email: { type: String, unique: true, required: true },
    phone: { type: String, required: true },
    username: { type: String, unique: true, required: true },
    dob: { type: Date, required: true },
    password: { type: String, required: true },
});

const Registration = mongoose.model('Registration', registrationSchema);

const app = express();
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON bodies

// Route to handle form submission
app.post('/register', async (req, res) => {
    const { email, phone, username, dob, password } = req.body;

    console.log("Received data:", req.body); // Log incoming data

    const newRegistration = new Registration({ email, phone, username, dob, password });

    try {
        const savedRegistration = await newRegistration.save();
        console.log("Data saved to MongoDB"); // Confirm save
        res.status(200).send('Registration successful!');
    } catch (error) {
        console.error('Database error:', error); // Detailed error log

        if (error.name === 'ValidationError') {
            res.status(400).send('Validation error: ' + error.message);
        } else if (error.code === 11000) {
            res.status(400).send('Duplicate entry error: Email or username already exists.');
        } else {
            res.status(500).send('Database save error');
        }
    }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
