# Ruslan Israfilov BS18-SB-01 DevOps Labs

> All .md files for the first 3 labs are in the app_python (except README.md)

# Lab 1-2
## Web Application
Application is coded with prod. ready framework - FastAPI.

It uses timeapi.io API to get current time in the 
Europe/Moscow timezone and return the time in the JSON format (simply speaking my application works as a simple proxy
for the timeapi.io API only for the Europe/Moscow timezone current time).

Testing was performed using the pytest library.

Endpoint is in `/app_python/api/routes/time.py`

### How to start
Clone the repository:

`git clone "link to repo"`

Install the requirements:

`pip3 install -r requirementss.txt`

Start the application:

`uvicorn app_python.api.server:app --reload --workers 1 --host 0.0.0.0 --port 8000`

### How to use
Go to the browser and put:

`http://localhost:8000/api/time/moscow`

You will see the json string with the info about current time in Moscow.

You also can go to the Swagger documentation:

`http://localhost:8000/docs`

### How to test
In the project directory go to the terminal and put:

` python -m pytest ./app_python/tests/test.py`

It will perform 2 tests:
1. Test of the endpoint (pass if response code == 200)
2. Test of the time (pass if the current time on the server hardware in the Europe/Moscow
timezone is within 5 second range to the endpoint time)

## Docker

### How to start the app with docker

1. From Dockerfile
   1. In the project directory build the image: \
   `docker build -t webapp .`
   2. Run docker container: \
   `docker run --name webapp1 -d -p 8000:8000 webapp`
   3. Go to the browser with the same link as in the case without docker.
2. From Dockerhub image
   1. Run docker container from the dockerhub image: \
   `docker run --name webapp1 -d -p 8000:8000 cendien/webapp:latest`
   2. Go to the browser with the same link as in the case without docker.

### How to test

After running the container you can execute: \
`docker exec webapp1 python -m pytest ./app_python/tests/test.py` \
and check if all tests were passed

# Lab 3
### Unit tests
You can read about my tests in the `Lab 1-2 How to test` sections

### Git Actions CI
main.yml 

### Jenkins
Jenkinsfile

# Lab 4

I used Vagrant instead of Terraform (because terraform doesn't work with vbox) for the first part of the lab.
So folder is called vagrant, and not terraform.

Second part of the lab is in terraform folder.