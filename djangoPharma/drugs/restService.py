import json
from urllib.request import urlopen
from django.conf import settings

# get rest endpoint from settings
rest_api = settings.DJANGOPHARMA_REST_URL

# get all data from rest service
def get_drugs():
    json_data = json.load(urlopen(rest_api))
    return json_data


# returns a drug dict (drug id , drug , name)
# by removing unwanted fields
def get_drugs_index():
    json_data = get_drugs()
    for drug in json_data:
        del drug['barcode']
        del drug['producer']
        del drug['price_wholesale']
        del drug['price_retail']
    return json_data


# get a drug by id (from REST API)
def get_drug_by_id(drug_id):
    urlpath = rest_api + '/' + drug_id
    rest_result = urlopen(urlpath)
    resp = json.load(rest_result)
    return resp
