# TravelRx

TravelRx is a mobile application that helps you search for and track your medication on-the-go. Additionally, the application comes with a translation feature, allowing the user to translate frequently-used emergency phrases in five of the most commonly-spoken languages: French, Spanish, German, Mandarin, and Arabic.

#### [Front End Repository](https://github.com/travel-rx/fe-travel-rx)
#### [Organization](https://github.com/travel-rx)

## Setup
* Ensure you are using Python 3.0 or higher: `python3 --version`
* Ensure you have postgresql installed. If you are using Homebrew: `brew install postgresql`
* Enter virtual environment: `python3 -m venv venv`
* `pip install flask`
* `gem install travis`
* `pip install coverage`
* `pip install python-dotenv`
* `pip install requests`
* `pip install gunicorn`
* `pip install flask-sqlalchemy`
* `pip install flask-marshmallow`
* `pip install marshmallow-sqlalchemy`
* ```psql
CREATE DATABASE DATABASE_NAME_dev;
\q```

## To Run
* `flask run`

## Test Coverage
* `coverage run test_app.py`
* `coverage report -m`

## Travel Rx - Backend

### Endpoint Documentation
* Local server: `http://localhost:5000`
* Production site: `https://flask-travel-rx.herokuapp.com`

#### Running in Postman
In Postman, append the url to expose the below endpoints or click the `Run in Postman` button to import a collection of the endpoints.

Postman collection for production site endpoints: [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/79d38c30ad43c49ba9e6)

* GET /api/v1/search?drug=xanax
```
Expected response:

status: 200 
{
   "name": "Xanax",
   "generic_name": "Alprazolam"
}
```

* POST /api/v1/user/:user_id/medicines
```
Request body:

{
  "dosage_amt": "2mg",
  "frequency": 1,
  "generic_name": "Pseudoephedrine",
  "name": "sudafed",
  "user_id": 1,
  "with_food": true
}
```

```
Expected response:

[
  {
    "dosage_amt": "3mg",
    "frequency": 1,
    "generic_name": "SERTRALINE HYDROCHLORIDE",
    "id": 2,
    "name": "zoloft",
    "user_id": 1,
    "with_food": false
  },
  {
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "ALPRAZOLAM",
    "id": 1,
    "name": "xanax",
    "user_id": 1,
    "with_food": true
  },
  {
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "ACETAMINOPHEN",
    "id": 3,
    "name": "TYLENOL Extra Strength",
    "user_id": 1,
    "with_food": true
  },
  {
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "Pseudoephedrine",
    "id": 6,
    "name": "sudafed",
    "user_id": 1,
    "with_food": true
  }
]
```

* GET /api/v1/user/:user_id/medicines
```
Expected response:

[
  {
    "dosage_amt": "3mg",
    "frequency": 1,
    "generic_name": "SERTRALINE HYDROCHLORIDE",
    "id": 2,
    "name": "zoloft",
    "user_id": 1,
    "with_food": false
  },
  {
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "ALPRAZOLAM",
    "id": 1,
    "name": "xanax",
    "user_id": 1,
    "with_food": true
  },
  {
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "ACETAMINOPHEN",
    "id": 3,
    "name": "TYLENOL Extra Strength",
    "user_id": 1,
    "with_food": true
  },
  {
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "Pseudoephedrine",
    "id": 6,
    "name": "sudafed",
    "user_id": 1,
    "with_food": true
  }
]
```

* GET /api/v1/user/:user_id/medicines/3
```
Expected response:

{
    "dosage_amt": "2mg",
    "frequency": 1,
    "generic_name": "ACETAMINOPHEN",
    "id": 3,
    "name": "TYLENOL Extra Strength",
    "user_id": 1,
    "with_food": true
 }
```

* DELETE /api/v1/user/:user_id/medicine/6
```
Expected response:

status code: 204
```

### Tech Stack
* Python (Flask)
* Unittest 

### Schema:
![Database Schema](https://user-images.githubusercontent.com/45922590/71044601-53988b00-20ef-11ea-9f6d-84cdc4d071e5.png)

## Contributors
#### Backend Engineers
[Leiya Kenney](https://github.com/leiyakenney)
[Smitha Hosmani](https://github.com/hsmitha26)

#### Frontend Engineers
[Amy Rippeto](https://github.com/aripp2)
[Jeannie Evans](https://github.com/jmevans0211)
