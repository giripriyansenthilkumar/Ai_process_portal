from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pdf2image import convert_from_path
import easyocr
from PIL import Image
import numpy as np
from pymongo import MongoClient
import os

# MongoDB setup
client = MongoClient('mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/')
db = client['text_extraction']  # Base database

# List of valid collections
valid_collections = [
    "Aadhaar_card",
    "Admission_Letter",
    "Allotment_Order",
    "Bank_Statement",
    "Community_Certificate",
    "Course_Fee_Structure",
    "Income_Certificate",
    "Pan_card"
]

# Specify the Poppler bin folder path
poppler_path = r"C:\Program Files\poppler\Library\bin"  # Update to match your Poppler installation path

@csrf_exempt
def upload_and_store(request):
    if request.method == "POST":
        try:
            # Get form data
            document_type = request.POST.get('document_type')  # Aadhaar, PAN, etc.
            document_number = request.POST.get('document_number')
            document_file = request.FILES.get('document_file')

            if not (document_type and document_number and document_file):
                return JsonResponse({"error": "Missing required fields!"}, status=400)

            # Validate document type
            if document_type not in valid_collections:
                return JsonResponse({"error": "Invalid document type!"}, status=400)

            # Save the file temporarily
            save_dir = "uploaded_files"
            os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists
            file_path = os.path.join(save_dir, document_file.name)

            with open(file_path, "wb+") as destination:
                for chunk in document_file.chunks():
                    destination.write(chunk)

            # Process the file and store in the correct collection
            process_and_store(file_path, document_type, document_number)

            return JsonResponse({"message": "Document uploaded and processed successfully!"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method!"}, status=400)


def process_and_store(file_path, document_type, document_number):
    # Get the target collection
    collection = db[document_type]

    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    if file_path.lower().endswith('.pdf'):
        # Process PDF
        pages = convert_from_path(file_path, poppler_path=poppler_path)
        for page_number, page in enumerate(pages):
            page_np = np.array(page)  # Convert PIL image to NumPy array
            text = reader.readtext(page_np, detail=0)
            page_text = "\n".join(text)

            # Store extracted text and metadata
            document = {
                'document_number': document_number,
                'file_path': file_path,
                'page_number': page_number + 1,
                'text': page_text,
            }
            collection.insert_one(document)

    else:
        # Process image
        with Image.open(file_path) as image:
            image_np = np.array(image)
            text = reader.readtext(image_np, detail=0)
            image_text = "\n".join(text)

            # Store extracted text and metadata
            document = {
                'document_number': document_number,
                'file_path': file_path,
                'text': image_text,
            }
            collection.insert_one(document)
