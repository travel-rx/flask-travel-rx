import flask
from flask import request, jsonify
from dotenv import load_dotenv
import requests
import json
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

# Init app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

port = int(os.environ.get("PORT", 5000))

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Class/Model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    medicines = relationship("Medicine", back_populates="user")

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

# Medicines Class/Model
class Medicine(db.Model):
    __tablename__ = 'medicine'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    generic_name = db.Column(db.String())
    dosage_amt = db.Column(db.String())
    with_food = db.Column(db.Boolean)
    frequency = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", back_populates="medicine")

    def __init__(self, name, generic_name, dosage_amt, with_food, frequency, user_id):
        self.name = name
        self.generic_name = generic_name
        self.dosage_amt = dosage_amt
        self.with_food = with_food
        self.frequency = frequency
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

@app.route('/', methods=['GET'])
def home():
    return "<h1>TravelRx</h1><p>This site is the homepage for the back end of TravelRx. Please visit our search endpoint at /api/v1/search or a user’s medicine cabinet at /api/v1/medicines.</p>"

@app.route('/api/v1/search', methods=['GET'])
def medicine_search():
    drug = request.args.get('drug', '')
    response = requests.get('https://api.fda.gov/drug/label.json?search=openfda.brand_name:' + drug)
    json_response = response.json()
    brand_name = json_response['results'][0]['openfda']['brand_name'][0]
    generic_name = json_response['results'][0]['openfda']['generic_name'][0]
    # import pdb; pdb.set_trace()
    return jsonify({"name": brand_name, "generic_name": generic_name})

if __name__ == "main":
    app.run(debug=True, host='0.0.0.0', port=port)
