import redis

from main.redis_models import ToDoList, Task
from utils import get_db_handle

# setting up a redis connection
redis_db = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# setting up local MongoDB connection
mongo_db, mongo_db_client = get_db_handle("to_do_db_test")
print(mongo_db.name)
print(mongo_db.list_collection_names())


# CRUD operations
def create_new_list(username, list_name):
    new_list = ToDoList(
        username=str(username),
        list_name=str(list_name),
    )
    new_list.save()
    return new_list


def create_new_task(list_pk, task_name, task_complete):
    new_task = Task(
        list_pk=str(list_pk),
        task_name=str(task_name),
        task_complete=bool(task_complete),
    )
    new_task.save()
    return new_task


def find_lists_by_username(username):
    # returns a list of values
    return ToDoList.find(ToDoList.username == str(username)).all()


def find_list_by_pk(pk):
    return ToDoList.find(ToDoList.pk == pk).all()


def find_tasks_by_list_pk(list_pk):
    # returns a list of values
    return Task.find(Task.list_pk == str(list_pk)).all()


'''
def add_data(data, collection_name):
    # to ensure that the data is added to the collection that we require.
    # always specify the collection name mongo_db.<collection_name>.insert_one()
    current_collection = mongo_db.get_collection(collection_name)
    return current_collection.insert_one(data)


def find_user_data(collection_name):
    current_collection = mongo_db.get_collection(collection_name)
    return current_collection.find()
'''
