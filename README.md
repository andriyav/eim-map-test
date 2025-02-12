# SLPUI
The test framework has three main functionalities:
* Validating source mapping according to the Pre-Promotion Checklist by testing the SLP UI.
* Validating morphed source data by testing the Dashboard UI before source promotion to prod.
* Automation mass mapping and testing source mapping.


# Required tools
1. Python: https://www.python.org/downloads/
2. Access to stage mls_admin database via tunnels.
3. Access to stage SLP UI.

# Installation
1. Install the Python3 using the links provided above.
2. Clone the repository using `git clone`.
3. Create a virtual environment: `python -m venv venv`.
4. Activate the virtual environment: `venv\Scripts\activate`.
5. Install the requirements: `pip install -r requirements.txt`.
6. Create `.env` with credentials to get access to MLS Admin in prod and stage. 

`HOST_STAGE=Host of MLSAdmin db on stage`

`PORT=5432`

`DATABASE=DB name`

`USER_STAGE=user`

`PASSWORD_STAGE=password on stage`

`HOST_PROD=Host of MLSAdmin db on stage`

`USER_PROD=user`

`PASSWORD_PROD=password on prod`


# Running
* Validating source mapping according to the Pre-Promotion Checklist by testing the SLP UI.
```shell
pytest --capture=no --alluredir=allure-results tests/test_checklist.py
```
* Validating morphed source data by testing the Dashboard UI before source promotion to prod.
```shell
pytest --capture=no --alluredir=allure-results --reruns 3 tests/test_dash_board.py
```

```shell
allure serve allure-results
```

