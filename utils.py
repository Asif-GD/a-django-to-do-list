import random
from random import randint

from pymongo import MongoClient

# I choose to have a separate file for database connection
# so any changes to the database connection can be modified in one place
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
    db_handle = client[db_name]
    return db_handle, client


# an RNG for creating unique slug for user's list.
def random_number_generator_6():
    slug_list = []
    while True:
        slug = random.randint(1, 999999)
        # to ensure the slug is always 6 integers long
        str(slug).zfill(6)
        if slug not in slug_list:
            break
    slug_list.append(int(slug))
    print(slug_list)
    return int(slug)

