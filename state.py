from country import GetAPIUrl, fileCheck
import json
import argparse
parsers = argparse.ArgumentParser()

parsers.add_argument("country")
args = parsers.parse_args()

fileCheck()

with open("country.json", 'r') as f:
    getCountryJson = json.load(f)
countryList = []
for cou in getCountryJson:
    countryList.append(cou['country_name'].lower())

def saveState():
    if args.country.lower() in countryList:
        getIndexNumber = getCountryJson.index(next(item for item in getCountryJson if item["country_name"].lower() == args.country.lower()))
        getCountryJson[getIndexNumber].update({"state": GetAPIUrl("states/" + args.country).json()})
    else:
        print("Country name is Not Valid")
    
saveState()
with open("country.json", 'w') as f:
    json.dump(getCountryJson, f, indent=4)

