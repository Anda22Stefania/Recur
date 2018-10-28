import json, requests, random, os, time

# Hardcoded variables #

consMerch = ["utilities","streaming","transport","gas"]
variMerch = ["food","entertainment","game"]

chosenConsMerch = []
chosenVariMerch = []

# Variable inputs #

apiKey = "c4a0166d7cd592202bf2bd0bf909b21b" #input("Input API Key:\n")
accountId = "5bd44926322fa06b67793e7c" #input("Input account id:\n")
noConsMerch = int(input("Input number of desired constant merchants:\n"))
noVariMerch = int(input("Input number of desired variable merchants:\n"))
months = int(input("Number of months of purchase history:\n"))

## Functions ##

# Function to fill merchants JSON file with merchants listed in API #

def merchantsCall(apiKey):
    url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        with open('merchants.json', 'w') as outfile:
            json.dump(data, outfile)
        return "Success"
    else:
        return "Error"


# Function to find list of all merchants that match a given category #

def merchList( category ):
    i = 0
    list = []
    while i < len(data):
        try:
            dataCat = data[i]["category"]
            try:
                dataCat = "".join(dataCat)
            except:
                dataCat
        except:
            name = ""
        if category in dataCat.lower():
            list.append(data[i]["_id"])
        i += 1
    return list

# Select merchants of given type #

def chooseMerchants(type, number, list):
    merchants = []

    for x in type:
        merchants += merchList(x)

    for x in range(number):
        list.append(merchants[random.randint(0,len(merchants)-1)])

# Function to submit payments to API #

def submitPayment(merchant, date):
    url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(accountId,apiKey)
    payment = {
        "merchant_id": merchant,
        "medium": "balance",
        "purchase_date": date,
        "amount": random.randint(0,50)
    }
    response = requests.post(
        url,
        data=json.dumps(payment),
        headers={'content-type': 'application/json'},
    )
    if response.status_code == 201:
        print("good")
        return True
    else:
        print("bad")
        return False

## Program ##

# Update merchants JSON file if not updated in more than a week #

if os.path.getmtime("merchants.json") < time.time() - 7 * 86400:
    merchantsCall()

# Load JSON file of all merchants #

json_data = open("merchants.json")
data = json.load(json_data)

# Select merchants #

chooseMerchants(consMerch, noConsMerch, chosenConsMerch)

chooseMerchants(variMerch, noVariMerch, chosenVariMerch)

