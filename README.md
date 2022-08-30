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

### Prerequisites
Python3, Docker

* Create a Redis-Stack Docker image. I developed the app by connecting to a local instance of a Redis Database, the link explains it better.
  - https://hub.docker.com/r/redis/redis-stack
* Setup a virtual environment for the project using pipenv, and activate it.
* Clone the repository
* The necessary packages should be installed automatically using the information from the PipFile
* Run the server using 
  * python manage.py runserver - Windows

## More Information about Redis Stack

Here some resources to help you quickly get started using Redis Stack. If you still have questions, feel free to ask them in the [Redis Discord](https://discord.gg/redis) or on [Twitter](https://twitter.com/redisinc).

### Getting Started

1. Sign up for a [free Redis Cloud account using this link](https://redis.info/try-free-dev-to) and use the [Redis Stack database in the cloud](https://developer.redis.com/create/rediscloud).
1. Based on the language/framework you want to use, you will find the following client libraries:
    - [Redis OM .NET (C#)](https://github.com/redis/redis-om-dotnet)
        - Watch this [getting started video](https://www.youtube.com/watch?v=ZHPXKrJCYNA)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-dotnet/)
    - [Redis OM Node (JS)](https://github.com/redis/redis-om-node)
        - Watch this [getting started video](https://www.youtube.com/watch?v=KUfufrwpBkM)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-node/)
    - [Redis OM Python](https://github.com/redis/redis-om-python)
        - Watch this [getting started video](https://www.youtube.com/watch?v=PPT1FElAS84)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-python/)
    - [Redis OM Spring (Java)](https://github.com/redis/redis-om-spring)
        - Watch this [getting started video](https://www.youtube.com/watch?v=YhQX8pHy3hk)
        - Follow this [getting started guide](https://redis.io/docs/stack/get-started/tutorials/stack-spring/)

The above videos and guides should be enough to get you started in your desired language/framework. From there you can expand and develop your app. Use the resources below to help guide you further:

1. [Developer Hub](https://redis.info/devhub) - The main developer page for Redis, where you can find information on building using Redis with sample projects, guides, and tutorials.
1. [Redis Stack getting started page](https://redis.io/docs/stack/) - Lists all the Redis Stack features. From there you can find relevant docs and tutorials for all the capabilities of Redis Stack.
1. [Redis Rediscover](https://redis.com/rediscover/) - Provides use-cases for Redis as well as real-world examples and educational material
1. [RedisInsight - Desktop GUI tool](https://redis.info/redisinsight) - Use this to connect to Redis to visually see the data. It also has a CLI inside it that lets you send Redis CLI commands. It also has a profiler so you can see commands that are run on your Redis instance in real-time
1. Youtube Videos
    - [Official Redis Youtube channel](https://redis.info/youtube)
    - [Redis Stack videos](https://www.youtube.com/watch?v=LaiQFZ5bXaM&list=PL83Wfqi-zYZFIQyTMUU6X7rPW2kVV-Ppb) - Help you get started modeling data, using Redis OM, and exploring Redis Stack
    - [Redis Stack Real-Time Stock App](https://www.youtube.com/watch?v=mUNFvyrsl8Q) from Ahmad Bazzi
    - [Build a Fullstack Next.js app](https://www.youtube.com/watch?v=DOIWQddRD5M) with Fireship.io
    - [Microservices with Redis Course](https://www.youtube.com/watch?v=Cy9fAvsXGZA) by Scalable Scripts on freeCodeCamp
