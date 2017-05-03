import logging
from requests.auth import HTTPBasicAuth
import requests

def create_site(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        site_type = parameters["SiteType"]
        city = parameters["City"]
        country = parameters["Country"]["alpha-2"]
        country_name = parameters["Country"]["name"]
        
        //API Call Here//
        url = 'https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/sites'
        data = {"id": "string", "name": "HQ", "org": "string", "longname": "string", "uplinks": ["string"], "networks": ["string"], "street_address": "Examplecorp, Root Road 14, 12345 Adminten", "city": city, "country": "DE", "timezone": "Europe/Berlin", "size": 0, "uid": "string"}
        res = requests.post(url, data = data, auth=HTTPBasicAuth('Shaylin', 'sche259'))
        
        //Ends Here//

        speech = "{} created in {}, {}".format(site_type.capitalize(), city, country_name)

        logging.debug(speech)

        return speech

    except KeyError as e:

        error_string = "Error processing createSite intent. {0}".format(e)

        logging.error()

        return error_string

