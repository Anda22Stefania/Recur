from flask import Flask, jsonify
from flask_cors import CORS
import json, requests

# Program to pull merchant list and populate merchant JSON file #

apiKey = "c4a0166d7cd592202bf2bd0bf909b21b"

app = Flask(__name__)
CORS(app)

@app.route('/merchants')
def merchantsCall():
    url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        #with open('merchants.json', 'w') as outfile:
        #    json.dump(jsonify(data), outfile)
        return jsonify(data)#{
            #"code":200
        #})

    else:
        return jsonify({
            "code":500
        })

if __name__ == '__main__':
    app.run(debug=True)
