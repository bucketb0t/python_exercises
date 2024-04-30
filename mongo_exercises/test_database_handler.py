import uuid
from database_handler import MongoDBHandler
import pytest
from pymongo import MongoClient


class TestFixture:
    @pytest.fixture(scope="class")
    def mongo_setup(self):
        client = MongoClient('localhost', 27017)
        database_name = 'test_1'
        db = client[database_name]
        collection = db['test_collection_1']
        mongo_handler = MongoDBHandler()
        try:
            yield mongo_handler
        finally:
            client.close()

    @pytest.fixture()
    def pet_data(self):
        yield {
            "name": "Kiba",
            "family_name": "Plushky",
            "age": 4,
            "breed": "Husky",
            "city": "Chitila",
            "nicknames": {
                "1": "Grasan",
                "2": "Panda",
                "3": "Mohican",
                "4": ("Taran", "Tractor"),
                "5": "Hitleras",
            }
        }

    def test_create_document(self, mongo_setup, pet_data):
        document_create = mongo_setup.create_document(pet_data)
        print(f"Id test_create1 {document_create.inserted_id}")
        assert document_create is not None

    def test_read_document(self, mongo_setup, pet_data):

        document_create = mongo_setup.create_document(pet_data)
        document_read = mongo_setup.read_document({"_id": document_create.inserted_id})

        # Assuming read_document returns a cursor, extract the first document
        document_read = next(document_read, None)

        if document_read is not None:
            assert document_read['_id'] == document_create.inserted_id
            assert document_read == document_create.inserted_id

    def test_update_document_with_additional_field(self, mongo_setup, pet_data):
        document_create = mongo_setup.create_document(pet_data)

        # Insert initial data into the collection
        assert document_create.inserted_id is not None

        # Define the query to find the inserted document
        query = {"_id": document_create.inserted_id}

        # Define the data to update the document
        update_data = {"age": 5, "nicknames.5": "Fluffy", "nicknames.6": "Botoxat"}

        # Call the update_document function
        result_update = mongo_setup.update_document(query, update_data)

        # Check if the update was successful
        assert result_update.matched_count == 1
        assert result_update.modified_count == 1

        # Retrieve the updated document
        updated_document = mongo_setup.collection_handler.find_one(query)

        # Check if the document was updated as expected
        assert updated_document["age"] == 5
        assert updated_document["nicknames"]["5"] == "Fluffy"
        assert updated_document["nicknames"]["6"] == "Botoxat"

    def test_delete_document(self, mongo_setup, pet_data):
        document_create = mongo_setup.create_document(pet_data)

        # Get the count before deletion
        before_delete_count = mongo_setup.collection_handler.count_documents({})

        # Delete the document
        query = {"_id": document_create.inserted_id}
        mongo_setup.delete_document(query)

        print(f"query = {query}")
        # Get the count after deletion
        after_delete_count = mongo_setup.collection_handler.count_documents({})

        # Assert that the collection is not None
        assert mongo_setup.collection_handler is not None, "Collection is None or not an instance of pymongo.collection.Collection"

        # Assert that the count decreased by 1 after deletion
        assert after_delete_count == before_delete_count - 1


"""Cu setup_method"""


class TestSetupMethod:
    def setup_method(self):
        self.client = MongoClient('localhost', 27017)
        self.database_name = 'test_1'
        self.db = self.client[self.database_name]
        self.pet = {"name": "Kiba",
                    "family_name": "Plushky",
                    "age": 4,
                    "breed": "Husky",
                    "city": "Chitila",
                    "nicknames": {
                        "1": "Grasan",
                        "2": "Panda",
                        "3": "Mohican",
                        "4": ("Taran", "Tractor"),
                        "5": "Hitleras",
                    }}
        self.collection = self.db['test_collection_1']

    def test_create_document(self):
        document_create = MongoDBHandler.create_document(self.pet)
        assert document_create is not None
        return document_create

    def test_read_document(self):
        document_read = MongoDBHandler.read_document({"_id": self.test_create_document().inserted_id}, )
        document_read = next(document_read, None)

        if document_read is not None:
            assert document_read['_id'] == self.test_create_document().inserted_id
            assert document_read == self.test_create_document()

    def test_update_document_with_additional_field(self):
        initial_result = self.collection.insert_one(self.pet)
        assert initial_result.inserted_id is not None
        query = {"_id": initial_result.inserted_id}
        update_data = {"age": 5, "nicknames.5": "Fluffy", "nicknames.6": "Botoxat"}
        result_update = MongoDBHandler.update_document(query, update_data)
        assert result_update.matched_count == 1
        assert result_update.modified_count == 1
        updated_document = self.collection.find_one(query)
        assert updated_document["age"] == 5
        assert updated_document["nicknames"]["5"] == "Fluffy"
        assert updated_document["nicknames"]["6"] == "Botoxat"

    def test_delete_document(self):
        document_to_delete = self.test_create_document()
        before_delete_count = self.collection.count_documents({})
        MongoDBHandler.delete_document({"_id": document_to_delete.inserted_id})
        after_delete_count = self.collection.count_documents({})
        assert self.collection is not None, "Collection is None or not an instance of pymongo.collection.Collection"
        assert after_delete_count == before_delete_count - 1
