from pdf2image import convert_from_path
import easyocr
from PIL import Image
import numpy as np
from pymongo import MongoClient
import os

# Specify the path to the Poppler bin folder
poppler_path = r"C:\Program Files\poppler\Library\bin"  # Update this to match your Poppler installation path

# MongoDB connection setup
client = MongoClient('mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/')  # Replace with your MongoDB URI if different
db = client['text_extraction']  # Database name
collection = db['extracted_texts']  # Collection name

def extract_text_from_file(file_path):
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Check if the file is a PDF
    if file_path.lower().endswith('.pdf'):
        try:
            # Convert PDF pages to images
            pages = convert_from_path(file_path, poppler_path=poppler_path)
            for page_number, page in enumerate(pages):
                # Convert PIL image to a NumPy array
                page_np = np.array(page)
                
                # Extract text using EasyOCR
                text = reader.readtext(page_np, detail=0)
                page_text = "\n".join(text)
                
                print(f"Extracted text from page {page_number + 1}:\n{page_text}\n")
                
                # Store the extracted text in MongoDB
                document = {
                    'file_path': file_path,
                    'page_number': page_number + 1,
                    'text': page_text
                }
                collection.insert_one(document)
                print(f"Stored text from page {page_number + 1} in MongoDB.")
        except Exception as e:
            print(f"An error occurred while processing the PDF: {e}")
    else:
        try:
            # Process as an image
            with Image.open(file_path) as image:
                image_np = np.array(image)
                text = reader.readtext(image_np, detail=0)
                image_text = "\n".join(text)
                
                print(f"Extracted text from image:\n{image_text}\n")
                
                # Store the extracted text in MongoDB
                document = {
                    'file_path': file_path,
                    'text': image_text
                }
                collection.insert_one(document)
                print("Stored text from image in MongoDB.")
        except Exception as e:
            print(f"An error occurred while processing the image: {e}")

# Example usage
file_path = r'C:\Users\nisahakar T\Downloads\SATURADAY PROJECT\final1\final\database\WhatsApp Image 2024-11-26 at 08.51.43_f7f7598e.jpg'
extract_text_from_file(file_path)
print("Text extraction and storage in MongoDB complete.")
