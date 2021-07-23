import requests
import json
import os.path

"""
abc = requests.get('https://www.universal-tutorial.com/api/getaccesstoken', headers={"Accept": "application/json",
                                                                                     "api-token": "cp-Z_uaVye2fFIaB2Cel7babsmUvhvdmRVOj9ak1J4V_BtZhURAVCmaRG62v2j_csa0",
                                                                                     "user-email": "jenny@bestcookieco.coms"})
print(abc.text)
"""

def GetAPIUrl(args):
    mainurl = 'https://www.universal-tutorial.com/api/'
    return requests.get(mainurl + args, headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJqZW5ueUBiZXN0Y29va2llY28uY29tcyIsImFwaV90b2tlbiI6ImNwLVpfdWFWeWUyZkZJYUIyQ2VsN2JhYnNtVXZodmRtUlZPajlhazFKNFZfQnRaaFVSQVZDbWFSRzYydjJqX2NzYTAifSwiZXhwIjoxNjI2NzU1MDgyfQ.lLBDAFiRKZDbcd26vfs-YsRBpCzUre1yz2I6mFZY8As'})


countryGet = json.dumps(json.loads(GetAPIUrl('countries/').text), indent=4)
def fileCheck():
    if os.path.exists('country.json') == False:
        saveFile(countryGet)

def saveFile(resource):
    f = open("country.json", 'w')
    f.write(resource)
    f.close()

fileCheck()
