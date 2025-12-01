# bakingtray
Templates used for my projects

# Quick Start
* Visit: http://migz.xyz

# Requirements
`pip install -r requirements.txt`
* Flask: used for the web app
* pytest: used for running tests

# Running tests
* Ensure you are in project root directory
```
ls

bakingtray/
├── commonlib/
│   └── ...
├── misc/
│   └── ...
├── tests/
│   ├── commonlibtest.ini
│   └── test_commonlib.py
├── WebApp.ini
├── WebApp.py
└── ...
```
* Run `pytest`

# Running the Flask web app
`python WebApp.py`
* Configure application properties in `WebApp.ini`

# Running via wsgi
`uwsgi --http 127.0.0.1:8000 --master -p 4 -w wsgi:app`