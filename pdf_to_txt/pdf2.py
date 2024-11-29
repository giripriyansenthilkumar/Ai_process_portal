from pdf2image import convert_from_path
import easyocr
import numpy as np
from PIL import Image
import os
import pymongo
import datetime

# Set up the path to your Poppler installation (necessary for pdf2image on Windows)
poppler_path = r"C:\\Program Files\\poppler\\Library\\bin"  # Update this path as needed

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/")  # Change the connection string if using MongoDB Atlas or other configurations
db = client["text_extraction_db"]  # Database name
collection = db["extracted_texts"]  # Collection name

# Function to extract text from either an image or a PDF file
def extract_text(file_path):
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])
    
    # Check file extension to determine if it's a PDF or an image
    file_extension = os.path.splitext(file_path)[1].lower()
    
    text_output = []
    
    if file_extension == ".pdf":
        # Convert each page of the PDF to an image
        try:
            pages = convert_from_path(file_path, poppler_path=poppler_path)
            
            for page_number, page in enumerate(pages):
                # Convert page to a NumPy array
                page_np = np.array(page)
                
                # Extract text from the page image
                text = reader.readtext(page_np, detail=0)
                
                # Append the text from each page
                text_output.append(f"Page {page_number + 1}:\n" + "\n".join(text) + "\n")
                print(f"Extracted text from page {page_number + 1}")
        
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return ""
    
    else:
        # Handle image files
        try:
            # Load the image
            image = Image.open(file_path)
            
            # Convert the image to a NumPy array
            image_np = np.array(image)
            
            # Extract text from the image
            text = reader.readtext(image_np, detail=0)
            
            # Append the extracted text
            text_output.append("\n".join(text))
            print("Extracted text from image")
        
        except Exception as e:
            print(f"Error opening image file: {e}")
            return ""
    
    # Combine all extracted text into a single string
    full_text = "\n".join(text_output)
    print("Extracted Text:\n", full_text)
    
    # Store the extracted text in MongoDB
    store_text_in_mongodb(file_path, full_text)
    
    return full_text

# Function to store extracted text in MongoDB
def store_text_in_mongodb(file_path, text):
    # Prepare data to be inserted
    document = {
        "file_path": file_path,
        "extracted_text": text,
        "extraction_time": datetime.time()
    }
    
    # Insert the data into MongoDB collection
    collection.insert_one(document)
    print(f"Text from {file_path} has been stored in MongoDB.")

# Example usage
file_path = r"C:\\Users\\HP\\OneDrive\\Documents\\sample.pdf"  # Can be a PDF or an image

# Check if the file exists before proceeding
if not os.path.exists(file_path):
    print(f"File does not exist: {file_path}")
else:
    # Extract text from the file and store it in MongoDB
    extracted_text = extract_text(file_path)
