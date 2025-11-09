# bakingtray
Templates used for my projects

# Requirements
`pip install -r requirements.txt`
* Flask: used for the web app
* pytest: used for running tests

# Running tests
* Ensure you are in project root directory
```
ls

bakingtray
  commonlib/
    ...
  misc/
    ...
  tests/
    commonlibtest.ini
    test_commonlib.py
  WebApp.ini
  WebApp.py
  ...
```
* Run `pytest`

# Running the Flask web app
`python WebApp.py`
* Configure application properties in `WebApp.ini`