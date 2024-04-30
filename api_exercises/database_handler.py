from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB server is running)
client = MongoClient('localhost', 27017)

# Create or select a database
database_name = 'test_1'
db = client[database_name]

# Create or select a collection
collection = db['test_collection_1']

#Partea de client database collection necesita in testare fie fixture fie setup_method --> ChatGPT
# CRUD operations

# Create
def create_document(data):
    result = collection.insert_one(data)
    print(f"Document inserted with ID: {result.inserted_id}")



# Read
def read_documents(query=None):
    documents = collection.find(query or {})
    for document in documents:
        print(document)


# Update
def update_document(query, update_data):
    result = collection.update_one(query, {'$set': update_data})
    print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s)")


# Delete
def delete_document(query):
    result = collection.delete_one(query)
    print(f"Deleted {result.deleted_count} document(s)")


# Example usage
if __name__ == "__main__":
    # Example data for creating a document
    example_data = {
        "name": "John Doe",
        "age": 30,
        "city": "Example City"
    }

    # Create a document
    create_document(example_data)

    # Read documents
    print("\nAll documents in the collection:")
    read_documents()

    # Update a document
    update_query = {"name": "John Doe"}
    update_data = {"age": 31}
    update_document(update_query, update_data)

    # Read documents after update
    print("\nAll documents in the collection after update:")
    read_documents()

    # # Delete a document
    # delete_query = {"name": "John Doe"}
    # delete_document(delete_query)

    # Read documents after delete
    print("\nAll documents in the collection after delete:")
    read_documents()


#Tema
# Scenarii de testare pentru CRUD MongoDB--handler