import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests


def create_site(api_auth, parameters):
    """
    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
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

    except KeyError as e:

        error_string = "Error processing createSite intent. {0}".format(e)

        logging.error(error_string)

        return error_string

    res = api_auth.create_site(name, city, country_code)

    if res.status_code == 200:
        speech = "{} created in {}, {}".format(site_type.capitalize(), city, country_name)
    elif res.status_code == 400:
        speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
    elif res.status_code == 500:
        speech = "Error: Could not create site"
    else:
        speech = "Error: Could not connect to Steelconnect"

    logging.debug(speech)

    return speech

