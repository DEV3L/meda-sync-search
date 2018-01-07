[![Build Status](https://travis-ci.org/DEV3L/prescription-drug-search.svg?branch=master)](https://travis-ci.org/DEV3L/prescription-drug-search)
[![Coverage Status](https://coveralls.io/repos/github/DEV3L/prescription-drug-search/badge.svg)](https://coveralls.io/github/DEV3L/prescription-drug-search)
[![Code Climate](https://codeclimate.com/github/DEV3L/prescription-drug-search/badges/gpa.svg)](https://codeclimate.com/github/DEV3L/prescription-drug-search)


# prescription-drug-search
Python Flask App to Phonetically Search Prescription Drugs by Name on Heroku


# Prerequisites
* Python 3.6+ installed
    * <https://www.python.org/downloads/>
* Virtualenv installed
    * <https://virtualenv.pypa.io/en/latest/>
    * sudo pip install --upgrade pip virtualenv virtualenvwrapper


## Run

```bash
mkvirtualenv prescription-drug-search
python setup.py develop

python server.py runserver --port 5006
python server.py runserver --port 5005
```


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-prescription-drug-search`
3. Commit your changes: `git commit -am 'Add something'`
4. Push to the branch: `git push origin my-prescription-drug-search`
5. Submit a pull request :D
