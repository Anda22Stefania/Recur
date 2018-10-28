from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json, requests

app = Flask(__name__)
CORS(app)

apiKey = "351388794358970b8ed7ec1790b2004a"

@app.route('/')
def index():
    return "hi"

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

@app.route('/api/subscriptions/<id>', methods=['GET'])
def getSubscriptionsForUser(id):
    subscriptions = []
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(id, apiKey)
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"status_code: 500"})
    content = json.loads(response.text)
    subscriptions = [s for s in content if s['description'] == "recur"]
    for s in subscriptions:
        merchant = getMerchant(s['merchant_id'])
        s.update({'merchant': merchant})
    return jsonify(subscriptions)

@app.route('/api/irregular/<id>', methods=['GET'])
def getIrregularRecurringPurchases(id):
    purchases = []
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(id, apiKey)
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"status_code: 500"})
    content = json.loads(response.text)
    purchases = [p for p in content if p['description'] == "irregular"]
    for p in purchases:
        merchant = getMerchant(p['merchant_id'])
        p.update({'merchant': merchant})
    return jsonify(purchases)

def getMerchant(id):
    url = "http://api.reimaginebanking.com/merchants/{}?key={}".format(id, apiKey)
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"status_code: 500"})
    return json.loads(response.text)

if __name__ == '__main__':
    app.run(debug=True)
