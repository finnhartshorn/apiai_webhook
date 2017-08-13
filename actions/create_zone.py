import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests


def create_zone(api_auth, parameters):
    """
    :param api_auth: SteelConnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        name = parameters["name"]
        site_name = parameters["site"]

    except KeyError as e:
        error_string = "Error processing create Zone intent. {0}".format(e)
        logging.error(error_string)
        return error_string

    # Get all sites and check whether site exists
    data_sites = api_auth.list_sites().json()
    site = ""
    for item in data_sites['items']:
        if site_name in item['name']:
            site = item['id']
            break

    if site != "":

        # Call create_zone in SteelConnectAPI
        res = api_auth.create_zone(name=name, site=site)

        if res.status_code == 200:
            speech = "Zone: {} created for site: {}".format(name, site_name)
        elif res.status_code == 400:
            speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
        elif res.status_code == 500:
            speech = "Error: Could not create Zone"
        else:
            speech = "Error: Could not connect to SteelConnect"

        logging.debug(speech)
    else:
        speech = "Invalid site {}".format(site_name)
    return speech
