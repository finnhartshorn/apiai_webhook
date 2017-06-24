import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests

def create_uplink(api_auth, parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        site_type = parameters["SiteTypes"]
        city = parameters["City"]
        uplink_name = parameters["Uplinks"]

    except KeyError as e:

        error_string = "Error processing createUplink intent. {0}".format(e)

        logging.error(error_string)

        return error_string

    # Get all the sites and check whether there is a site match given city and site type
    res = api_auth.list_sites()
    data= res.json()
    site = ""
    for  item in data['items']:
        if (city+site_type in item['id']):
            site = item['id']

    if (site != ""):
        res = api_auth.create_uplink(site, uplink_name)
        logging.debug(res)

        if res.status_code == 200:
            speech = "An uplink had created in site {}_{}".format(city, site_type)
        elif res.status_code == 400:
            speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
        elif res.status_code == 500:
            speech = "Error: Could not create uplink"
        else:
            speech = "Error: Could not connect to Steelconnect"

        logging.debug(speech)
    else:
        speech = "Invalid site {}_{}".format(city, site_type)
    return speech



