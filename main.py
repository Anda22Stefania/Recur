from flask import Flask, render_template, jsonify
#from flask_cors import CORS
import json, requests

app = Flask(__name__)
#CORS(app)

apiKey = "c4a0166d7cd592202bf2bd0bf909b21b"

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
            "status_code": 500
        })

@app.route('/api/subscriptions/<id>', methods=['GET'])
def getSubscriptionsForUser(id):
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(id, apiKey)
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"status_code: 500"})
    content = json.loads(response.text)
    merchants = []
    x = 0
    while x < len(content):
        merchants.append(content[x]["merchant_id"])
        x += 1
    categories = []
    x = 0
    while x < len(merchants):
        url = "http://api.reimaginebanking.com/merchants/{}?key={}".format(merchants[x], apiKey)
        if response.status_code != 200:
            return jsonify({"status_code: 500"})
        response = requests.get(url)
        data = json.loads(response.text)
        categories.append(data["category"])
        x += 1
    x = 0
    subscriptions = []
    while x < len(merchants):
        if "utilities" in map(str.lower,categories[x]):
            subscriptions.append(content[x])
        elif "streaming" in map(str.lower,categories[x]):
            subscriptions.append(content[x])
        elif "transport" in map(str.lower,categories[x]):
            subscriptions.append(content[x])
        elif "gas" in map(str.lower,categories[x]):
            subscriptions.append(content[x])
        x += 1
    return jsonify(subscriptions)

@app.route('/api/irregular/<id>', methods=['GET'])
def getIrregularRecurringPurchases(id):
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(id, apiKey)
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"status_code: 500"})
    content = json.loads(response.text)
    merchants = []
    x = 0
    while x < len(content):
        merchants.append(content[x]["merchant_id"])
        x += 1
    categories = []
    x = 0
    while x < len(merchants):
        url = "http://api.reimaginebanking.com/merchants/{}?key={}".format(merchants[x], apiKey)
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"status_code: 500"})
        data = json.loads(response.text)
        categories.append(data["category"])
        x += 1
    x = 0
    purchases = []
    while x < len(merchants):
        if "game" in map(str.lower, categories[x]):
            purchases.append(content[x])
        elif "food" in map(str.lower, categories[x]):
            purchases.append(content[x])
        elif "entertainment" in map(str.lower, categories[x]):
            purchases.append(content[x])
        x += 1
    return jsonify(purchases)

if __name__ == '__main__':
    app.run(debug=True)
