# A To Do List

A "To Do List" web-app created using Python-Django framework, and Redis as a primary database using Redis OM for Python.

App Screenshots

### /home
![image](https://user-images.githubusercontent.com/43206308/187314705-8297d17d-59ef-4af6-8d36-6e0d68e5ab66.png)

### /login
![image](https://user-images.githubusercontent.com/43206308/187316578-b5efa3f7-65c5-4b46-b399-8e4b34b64e64.png)

### /register
![image](https://user-images.githubusercontent.com/43206308/187316659-fc40f4d5-e347-462e-b261-492d791af32d.png)

### /lists
![image](https://user-images.githubusercontent.com/43206308/187316817-b5d66005-5e2c-4d0d-8b50-bbc373dbff10.png)

### /tasks
![image](https://user-images.githubusercontent.com/43206308/187316895-82558e7d-e084-41ca-9ff5-f9867ba82c69.png)

## Data Models

1. List Data Model
  * username: string type -> indexed 
  * list_name: string type

2. Task Data Model
  * list_pk: string type -> indexed
  * task_name: string type
  * task_complete: Optional boolean type

## How it works

* The web-app uses SQLite3, the default django database for storing User models. I chose to do this in order to utilize the built-in django modules for User Creation & Authentication.
* The primary database is Redis with data models implemented using Redis OM in Python.
* The To Do Lists created by the user are tagged to them via their username and can be retrieved, hence the username field is indexed.
* The Tasks are tagged to the list by retriving the list's primary key and storing it along with the task.
* The primary key of the list is stored into list_pk inside the Task data model, and that field is indexed.
* Upon searching for the user's lists, they are authenticated and all the user's list are retrieved as links. 
* Accessing the Lists will lead to their individual tasks under them.
* The links for the lists are generated using their list's primary key.
<i>note - This caused errors inorder to access the other URLs, so I have unimplemented (commented out the URL in main/urls.py) it for now.</i>

## How to run it locally?

* Create a Redis-Stack Docker image. I developed the app by connecting to a local instance of a Redis Database, the link explains it better.
- https://hub.docker.com/r/redis/redis-stack
* Setup a virtual environment for the project using pipenv, and activate it.
* Clone the repository
* The necessary packages should be installed automatically using the information from the PipFile
* Run the server using 
  * python manage.py runserver - Windows
