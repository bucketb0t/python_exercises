from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB server is running)
client = MongoClient('localhost', 27017)

# Create or select a database
database_name = 'test_1'
db = client[database_name]

# Create or select a collection
collection_handler = db['test_collection_1']


# CRUD operations
# De citit cum se face indexarea corecta in MongoDB
# De instalat NoSql booster, varianta free
# De citit metodele pymongo

class MongoDBHandler:
    def __init__(self, host='localhost', port=27017, database_name='test_1', collection_name='test_collection_1'):
        # Connect to MongoDB (make sure MongoDB server is running)
        self.client = MongoClient(host, port)

        # Create or select a database
        self.db = self.client[database_name]

        # Create or select a collection
        self.collection_handler = self.db[collection_name]

    def create_document(self, data):
        result_create = self.collection_handler.insert_one(data)
        print(f"Document inserted with ID: {result_create.inserted_id}")
        return result_create

    def create_documents(self, data_list):
        result_create_many = self.collection_handler.insert_many(data_list)
        print(f"{len(result_create_many.inserted_ids)} documents inserted with IDs: {result_create_many.inserted_ids}")
        return result_create_many

    def read_document(self, query=None):
        result_read = self.collection_handler.find(query or {})
        for document in result_read:
            print(document)
        return result_read

    def read_document_by_id(self, result_create):
        query = {"_id": result_create.inserted_id}
        result_read = self.collection_handler.find(query)
        for document in result_read:
            print(document)
        return result_read

    def read_one_document(self, query=None):
        result_read = self.collection_handler.find_one(query)
        if result_read:
            print(result_read)
        else:
            print("No matching document found.")
        return result_read

    def update_document(self, query, update_data):
        result_update = self.collection_handler.update_one(query, {'$set': update_data})
        print(
            f"Matched {result_update.matched_count} document(s) and modified {result_update.modified_count} document(s)")
        return result_update

    def delete_document(self, query):
        result_delete = self.collection_handler.delete_one(query)
        print(f"Deleted {result_delete.deleted_count} document(s)")


# Example usage
if __name__ == "__main__":
    # Example data for creating a document
    example_data = {
        "name": "John Doe",
        "age": 30,
        "city": "Example City"
    }

    # Instantiate the MongoDBHandler class
    mongo_handler = MongoDBHandler()

    # Create a document
    mongo_handler.create_document(example_data)

    # Read documents
    print("\nAll documents in the collection:")
    mongo_handler.read_document()

    # Update a document
    update_query = {"name": "John Doe"}
    update_data = {"age": 31}
    mongo_handler.update_document(update_query, update_data)

    # Read documents after update
    print("\nAll documents in the collection after update:")
    mongo_handler.read_document()

    # # Delete a document
    # delete_query = {"name": "John Doe"}
    # mongo_handler.delete_document(delete_query)

    # Read documents after delete
    print("\nAll documents in the collection after delete:")
    mongo_handler.read_document()
