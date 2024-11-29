// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors'); // Import CORS middleware

// Initialize Express app
const app = express();
app.use(express.json());

// Enable CORS for frontend requests
app.use(cors({ origin: 'http://localhost:3000' })); // Update origin to match frontend URL if needed

// MongoDB Connection URI
const dbURI = 'mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/'; // Ensure `127.0.0.1` instead of `localhost` to avoid IPv6 issues

// Connect to MongoDB using Mongoose
mongoose.connect(dbURI)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define a sample schema and model (update with your actual schema)
const registrationSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String
});

const Registration = mongoose.model('Registration', registrationSchema);

// Define a POST route for registration
app.post('/api/register', async (req, res) => {
  try {
    const newRegistration = new Registration(req.body);
    const savedRegistration = await newRegistration.save();
    res.status(201).json(savedRegistration);
  } catch (error) {
    console.error('Error during registration:', error);
    res.status(500).json({ error: 'Registration failed' });
  }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
