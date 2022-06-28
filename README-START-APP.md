# Bulelani python-the-shortest-url Assessment 

##  Docker Installation recommended

Installation will require [Docker](https://www.docker.com/)  and Docker Compose to be installed 

Build the docker container and start the container.

```sh
docker-compose up -d --build
```
Run the Tests ...

```sh
docker-compose exec web python -m pytest
```

API Docs 
```sh
http://127.0.0.1:8000/docs#
```


## None Docker installation

Make sure you have python3.8+  and pip installed
Create and activate a python  virtual enviroment 

Make sure you are inside the python-the-shortest-url-qnlkvi directory 

Install requirements:
```sh
pip install -r requirements.txt
```

Start application:

```sh
 uvicorn backend.main:app --reload
```

API Docs 
```sh
http://127.0.0.1:8000/docs#
```