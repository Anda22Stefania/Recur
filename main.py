from flask import Flask, render_template, jsonify
import json, requests

app = Flask(__name__)

key = "351388794358970b8ed7ec1790b2004a"

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
