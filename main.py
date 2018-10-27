from flask import Flask, render_template,jsonify, request
import requests
import json

from requests import Response

app = Flask(__name__)

apiKey = "c4a0166d7cd592202bf2bd0bf909b21b"

@app.route('/api/accounts/<custId>')
def userAccountsRoute(custId):
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(custId,apiKey)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return jsonify(data)
    else:
        return jsonify({
            "code":500
        })

@app.route('/api/customer/<custId>')
def userInfoRoute(custId):
    url = 'http://api.reimaginebanking.com/customer/{}?key={}'.format(custId,apiKey)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return jsonify(data)
    else:
        return jsonify({
            "code": 500
        })


if __name__ == '__main__':
    app.run()
