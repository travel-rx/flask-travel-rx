# TravelRx

TravelRx is a traveller’s favorite medication-tracking companion! With TravelRx, you don’t need to worry about getting sick while travelling and needing to find the proper medication on your own, losing your everyday medications, or being able to find medical assistance in an area where you don’t speak the language. 

Our app provides a traveller with the ability to look up a medication’s generic name from its American brand name, as pharmacies worldwide use the generic medication name rather than brand names.  It also provides you with access to a personalized “medicine cabinet,” where you can store information about the medications you take, including their name (brand and generic), time of day you take the medicine, frequency of dosage, as well as the dosage amount.

Lastly, if you are in an area where Spanish, French, Mandarin, German, or Arabic are spoken, TravelRx provides you with popular emergency medical phrases to assist you in getting the help you need.

TravelRx project was completed in 13 days by a team comprised of two front end and two back end developers. This was our first  cross-pollination project where members of the two distinct programs at Turing School of Software and Design worked together to produce one app using an idea pitched by one of the members.

### Area of Focus
* Quickly learning a new language (Python), framework (Flask) and testing suite (Unittest) in less than a week
* Agility/adaptability in switching language/framework to deliver a good developer experience to our Front End team
* Building from ideation to app
* Agile methodologies utilized to manage project across multiple teams
* Clear communication and directives
* Clear vision for MVP, this was treated as a contract amongst the members of the team

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
* After entering `psql` into terminal: `CREATE DATABASE DATABASE_NAME_dev;`

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

### Known Issues
The test file is accessible only via the testing branch.  The developers are aware that separate testing, production, staging and development environments need to be configured.
This repo will be updated and testing branch will be merged as soon as the environments are configured.
