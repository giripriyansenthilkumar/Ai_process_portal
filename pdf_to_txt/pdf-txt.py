from pdf2image import convert_from_path
import easyocr
import numpy as np

# Specify the path to the poppler bin folder
poppler_path = r"C:\\Program Files\\poppler\\Library\\bin"  # Update this to match your Poppler installation path

def extract_text_from_handwritten_pdf(pdf_path):
    # Convert each page of the PDF to an image with poppler_path specified
    pages = convert_from_path(pdf_path, poppler_path=poppler_path)
    
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    text_output = []
    for page_number, page in enumerate(pages):
        # Convert PIL image to a NumPy array
        page_np = np.array(page)
        
        # Use EasyOCR to read text from the NumPy array
        text = reader.readtext(page_np, detail=0)
        
        text_output.append(f"Page {page_number + 1}:\n" + "\n".join(text) + "\n")
        print(f"Extracted text from page {page_number + 1}")

    full_text = "\n".join(text_output)
    return full_text

# Example usage
pdf_path = "C:\\Users\\HP\\OneDrive\\Documents\\sample.pdf"
extracted_text = extract_text_from_handwritten_pdf(pdf_path)
print("Extracted Text:\n", extracted_text)