from flask import Flask, request, jsonify, redirect
from dotenv import load_dotenv
import requests
import json
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from flask_seeder import FlaskSeeder
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
app.config["DEBUG"] = True

port = int(os.environ.get("PORT", 5000))

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)

ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    medicines = db.relationship("Medicine", backref="user")

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

# User Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'email')

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

    def __init__(self, name, generic_name, dosage_amt, with_food, frequency, user_id):
        self.name = name
        self.generic_name = generic_name
        self.dosage_amt = dosage_amt
        self.with_food = with_food
        self.frequency = frequency
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

# Medicines Schema
class MedicineSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'generic_name', 'dosage_amt', 'with_food', 'frequency', 'user_id')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

medicine_schema = MedicineSchema()
medicines_schema = MedicineSchema(many=True)

# Endpoints
@app.route('/', methods=['GET'])
def home():
    return "<h1>TravelRx</h1><p>This site is the homepage for the back end of TravelRx.  Please visit our search endpoint at /api/v1/search?drug=<drug_name or a user's medicine cabinet at /api/v1/medicines.</p>"

# Search for generic name of a Medicine
@app.route('/api/v1/search', methods=['GET'])
def medicine_search():
    drug = request.args.get('drug', '')
    response = requests.get('https://api.fda.gov/drug/label.json?search=openfda.brand_name:' + drug)
    json_response = response.json()
    brand_name = json_response['results'][0]['openfda']['brand_name'][0]
    generic_name = json_response['results'][0]['openfda']['generic_name'][0]
    return jsonify({"name": brand_name, "generic_name": generic_name})

# Get all medicines
@app.route('/api/v1/user/<user_id>/medicines', methods=['GET'])
def get_medicines(user_id):
  all_meds = Medicine.query.all()
  result = medicines_schema.dump(all_meds)
  return jsonify(result)

# Get single medicine
@app.route('/api/v1/user/<user_id>/medicines/<id>', methods=['GET'])
def get_medicine(user_id, id):
    user = User.query.get(user_id)
    med = Medicine.query.get(id)
    result = medicine_schema.dump(med)
    return jsonify(result)

# Add new medicine to user's medicine cabinet
@app.route('/api/v1/user/<user_id>/medicines', methods=['POST'])
def add_medicine(user_id):
    name = request.json['name']
    generic_name = request.json['generic_name']
    dosage_amt = request.json['dosage_amt']
    with_food = request.json['with_food']
    frequency = request.json['frequency']
    user_id = user_id

    new_medicine = Medicine(name, generic_name, dosage_amt, with_food, frequency, user_id)
    db.session.add(new_medicine)
    db.session.commit()

    user = User.query.get(user_id)
    return redirect(f'/api/v1/user/{user}/medicines')

# Delete single medicine
@app.route('/api/v1/user/<user_id>/medicines/<id>', methods=['DELETE'])
def delete_medicine(user_id, id):
    user = User.query.get(user_id)
    med = Medicine.query.get(id)
    db.session.delete(med)
    db.session.commit()
    return redirect(f'/api/v1/user/{user}/medicines')

if __name__ == "main":
    # app.run()
    app.run(debug=True, host='0.0.0.0', port=port)
