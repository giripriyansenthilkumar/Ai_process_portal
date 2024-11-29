from pymongo import MongoClient

# Connect to MongoDB (assuming it's running locally on the default port)
client = MongoClient("mongodb://localhost:27017/text_extraction")  # Adjust if MongoDB is hosted elsewhere

# Specify the database and collection
db = client["text_extraction"]       # Database name
collection = db["extracted_texts"]   # Collection name

# Sample document to insert
document = {
    "name": "Example Document",
    "content": "This is an example text content to be stored in MongoDB.",
    "status": "success"
}

# Insert the document
insert_result = collection.insert_one(document)

# Print the ID of the inserted document
print("Document inserted with ID:", insert_result.inserted_id)
