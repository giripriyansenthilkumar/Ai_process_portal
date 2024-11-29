const express = require('express');
const multer = require('multer');
const { MongoClient } = require('mongodb');
const pdfParse = require('pdf-parse');
const fs = require('fs');

const app = express();
const PORT = 3000;

// MongoDB connection
const uri = 'mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/'; // Change if using a remote MongoDB instance
const dbName = 'text_extraction';

// Configure Multer for file uploads
const upload = multer({
    dest: 'uploads/', // Temporary folder for uploads
});

// Endpoint for root route
app.get('/', (req, res) => {
    res.send('Welcome to the AI Approval Process Portal');
});

// Endpoint to handle file uploads
app.post('/upload/:collection', upload.single('document_file'), async (req, res) => {
    const { collection } = req.params; // Get the collection name from URL
    const documentNumber = req.body.document_number; // Get document number
    const file = req.file; // Uploaded file

    if (!file || !documentNumber) {
        return res.status(400).json({ error: 'Document number and file are required' });
    }

    try {
        // Read the uploaded file
        const fileData = fs.readFileSync(file.path);

        // Extract text from PDF
        const extractedText = await pdfParse(fileData);

        // Connect to MongoDB
        const client = new MongoClient(uri);
        await client.connect();
        const db = client.db(dbName);

        // Insert into the specific collection
        const result = await db.collection(collection).insertOne({
            documentNumber,
            extractedText: extractedText.text, // Store extracted text
            uploadedAt: new Date(),
        });

        // Clean up the uploaded file
        fs.unlinkSync(file.path);

        // Send success response
        res.json({ message: 'Document uploaded and text extracted successfully', result });

        // Close DB connection
        await client.close();
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to upload and process document' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
