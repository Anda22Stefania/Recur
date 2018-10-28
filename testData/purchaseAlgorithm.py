import json, requests, random

# Hardcoded variables #

consMerch = ["utilities","streaming","transport","gas"]
vairMerch = ["food","entertainment","game"]

chosenConsMerch = []
chosenVariMerch = []

# Variable inputs #

apiKey = input("Input API Key:\n")
noConsMerch = int(input("Input number of desired constant merchants:\n"))
noVariMerch = int(input("Input number of desired variable merchants:\n"))
months = int(input("Number of months of purchase history:\n"))

# Load JSON file of all merchants #

json_data = open('merchants.json')
data = json.load(json_data)

# Function to find list of all merchants that match a given category #

def merchList( category ):
    i = 0
    list = []
    while i < len(data):
        try:
            dataCat = data[i]['category']
            try:
                dataCat = "".join(dataCat)
            except:
                dataCat
        except:
            name = ""
        if category in dataCat.lower():
            list.append(data[i]['_id'])
        i += 1
    return list

