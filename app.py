import flask
from flask import request, jsonify
from dotenv import load_dotenv
import requests
import json

import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

port = int(os.environ.get("PORT", 5000))
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
