from utils import get_db_handle

# setting up local MongoDB connection
db, db_client = get_db_handle("to_do_db_test")
print(db.name)
print(db.list_collection_names())


# CRUD operations
def create_list(data, collection_name):
    # to ensure that the data is added to the collection that we require.
    # always specify the collection name db.<collection_name>.insert_one()
    current_collection = db.get_collection(collection_name)
    return current_collection.insert_one(data)

# def get_object_id():
