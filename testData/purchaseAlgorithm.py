from datetime import datetime, timedelta
import json, requests, random, os, time

# Hardcoded variables #

consMerch = ["utilities","streaming","transport","gas"]
variMerch = ["food","entertainment","game"]
apiKey = "c4a0166d7cd592202bf2bd0bf909b21b"

chosenConsMerch = []
chosenVariMerch = []

apiKey = "c4a0166d7cd592202bf2bd0bf909b21b"
accountId = input("Input account id:\n")
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
        return True
    else:
        print(response.text)
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

for x in range(months):

    for y in range(28):

        date = datetime.today() - timedelta(days=((x*28)+y))

        if y == 1:

            for z in range(noConsMerch):
                print(submitPayment(chosenConsMerch[z - 1], date.strftime('%Y-%m-%d')))
        elif random.randint(0,100) > random.randint(0,85):
            print(submitPayment(chosenVariMerch[random.randint(0, noVariMerch - 1)], date.strftime('%Y-%m-%d')))
            print(submitPayment(chosenVariMerch[random.randint(0, noVariMerch - 1)], date.strftime('%Y-%m-%d')))
        elif random.randint(0,100) > random.randint(0,55):
            print(submitPayment(chosenVariMerch[random.randint(0, noVariMerch - 1)], date.strftime('%Y-%m-%d')))