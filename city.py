from country import GetAPIUrl, fileCheck, saveFile
import json
import argparse
parsers = argparse.ArgumentParser()

parsers.add_argument("country")
parsers.add_argument("state")
args = parsers.parse_args()

fileCheck()
with open("country.json", 'r') as f:
    getAPIJson = json.load(f)

countryIndex = getAPIJson.index(next(item for item in getAPIJson if item["country_name"].lower() == args.country.lower()))
def citySave():
    for item in getAPIJson[countryIndex]['state']:
        if item['state_name'] == args.state:
            item.update({"city": GetAPIUrl("cities/" + args.state).json()})

if 'state' in getAPIJson[countryIndex]:
    citySave()
else:
    getAPIJson[countryIndex].update({"state": GetAPIUrl("states/" + args.country).json()})
    citySave()

with open("country.json", 'w') as f:
    json.dump(getAPIJson, f, indent=4)
