from pymongo import MongoClient

# I choose to have a separate file for database connection
# so any changes to the database connection can be modified here in one place
'''
# the default format
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['db_name']
 return db_handle, client
'''


# I will be connecting to a local cluster
def get_db_handle(db_name):
    client = MongoClient(host="localhost",
                         port=int(27017),
                         )
    db_handle = client['db_name']
    return db_handle, client
