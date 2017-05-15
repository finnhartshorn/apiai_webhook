import logging

from flask import json
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
        country_code = parameters["Country"]["alpha-2"]
        country_name = parameters["Country"]["name"]
        name = city+"_"+site_type
        
        # API Call Here
        url = 'https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/sites'
        data = {"id": "", "name": name, "org": "Monash", "longname": name, "uplinks": [""], "networks": [""], "street_address": "", "city": city, "country": country_code, "timezone": "", "size": 0, "uid": ""}
        request = json.dumps(data, indent=4)
        res = requests.post(url, data=request, auth=HTTPBasicAuth('Shaylin', 'sche259'))
        logging.debug(res)
        # Ends Here

        speech = "{} created in {}, {}".format(site_type.capitalize(), city, country_name)

        logging.debug(speech)

        return speech

    except KeyError as e:

        error_string = "Error processing createSite intent. {0}".format(e)

        logging.error(error_string)

        return error_string

