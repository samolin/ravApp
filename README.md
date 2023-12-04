# ravApp
Test task showing django-rest-framework features. There is an item model supporting CRUD operations using DRF generic classes. Routers have permissions isAuthenticated. Once you logged in as user you can use them. Django user model is used as the user model for authentication. A route http://localhost:8000/api/items/ might be cached, in case something has been changed into the database cache will be invalidated. Backup scheduled in every 12 hours implemented using celery-beats. All routes are covered with tests using pytest. Async is implemented by http://localhost:8000/api/async_download/ route.

## Routers

- http://localhost:8000/api/register/ - user register
- http://localhost:8000/api/login/ - user login, get tokens
- http://localhost:8000/api/items/ - [get] list items, [post] create an item
- http://localhost:8000/api/items/{id} - [get] get an item,  [put] update an item, [delete] delete an item
- http://localhost:8000/api/async_download/ - download python docs using async

## Technologies

- [Django Rest Framework] - The Web browsable API is a huge usability win for your developers. 
- [Redis] - Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.
- [Docker] - Docker is a platform designed to help developers build, share, and run container applications. 
- [JWT] - JSON Web Token (JWT) is a compact URL-safe means of representing claims to be transferred between two parties.
- [Celery] - It's a task queue with focus on real-time processing, while also supporting task scheduling.

## Installation

```sh
git clone https://github.com/samolin/ravApp
cd ravApp
make up
```
#### Stop containers
```sh
make stop
```
#### Test app
```sh
poetry install --with tests
make tests
```


   [Django Rest Framework]: <https://www.django-rest-framework.org/>
   [Redis]: <https://redis.com>
   [Docker]: <https://www.docker.com>
   [JWT]: <https://www.docker.com>
   [Celery]: <https://docs.celeryq.dev/en/stable/>