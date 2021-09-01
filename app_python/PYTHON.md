## Practices
1. Used different routers for the different api routes (Currently have only one, but can be very useful for the future app development)
2. Used pycharm with the build-in linters with PEP8 formatting
3. Used `pip3 freeze > requirements.txt` to have all the requirements for the developers to not have troubles with the dependencies
4. Used separate functions for app creation and startup + shutdown event handlers
5. Used comments for the developers to understand what's happening
6. Used good-looking and convenient file structure with separate directories for the different routes, tasks, and testing
7. Used Automated testing with the pytest

## Unit tests
1. First one tests if endpoint is accessible (returns 200 response code)
2. Second one tests if time is correct (within 5 second range to the current time on the hardware)

### practices
1. Used pytest library, specifically designed for testing python apps
2. Used fastAPI TestClient, which is designed for testing fastAPI applications with pytest
