import flask
from flask import request, jsonify
from dotenv import load_dotenv
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/search', methods=['GET'])
def medicines_index():
    # search = 'openfda.brand_name:xanax'
    # api_key = 'FDA_API_KEY'
    # params = {
    # 'api_key': '{FDA_API_KEY}',
    # 'search': 'openfda.brand_name:xanax'
    # }
    response = requests.get('https://api.fda.gov/drug/label.json?search=openfda.brand_name:xanax&api_key=n5fe5G1BTGmOwMglgvku6uQpa67LURmUEiMpv2VV')
    json_response = response.json()
    brand_name = json_response['results'][0]['openfda']['brand_name'][0]
    generic_name = json_response['results'][0]['openfda']['generic_name'][0]
    return jsonify({"name": brand_name, "generic_name": generic_name})
    # return json_response

app.run()
