# Ruslan Israfilov BS18-SB-01 DevOps Labs

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