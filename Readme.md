# Sarogya Aetu

Application to check slots for COVID vaccination in Bangalore region using pincodes for a given date using [API Setu](https://apisetu.gov.in/public/api/cowin#/Appointment%20Availability%20APIs/findByPin)

## Setting up app

```
virtualenv <env-name> -p python3.8
source <env-name>/bin/activate
pip install -r requirements.txt
```

## Running the application

Run  ``` python vaccinator.py ``` and then follow on-screen instructions.


## Running the tests

- Install docker([here](https://docs.docker.com/engine/install/))
- Run ```bash run_tests.sh```
- Alternatively, run ```pytest -vv```
