from flask import Flask, render_template, jsonify
import json, requests

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

@app.route('/')
def index():
    return "hi"

@app.route('/api/subscriptions/<id>', methods=['GET'])
def getSubscriptionsForUser(id):
    subscriptions = []
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(id, key)
    content = json.loads(requests.get(url).text)
    subscriptions = [s for s in content if s['description'] == "recur"]
    return jsonify(subscriptions)

@app.route('/api/irregular/<id>', methods=['GET'])
def getIrregularRecurringPurchases(id):
    purchases = []
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(id, key)
    content = json.loads(requests.get(url).text)
    purchases = [p for p in content if p['description'] == "irregular"]
    return jsonify(purchases)

if __name__ == '__main__':
    app.run(debug=True)
