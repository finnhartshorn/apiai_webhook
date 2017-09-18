import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests
# import app

org = "Monash"


def list_sites(api_auth, parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        site_type = parameters["SiteTypes"]

    except KeyError as e:
        error_string = "Error processing List Sites by Type intent. {0}".format(e)
        logging.error(error_string)
        return error_string

    # Get all sites and check whether site exists
    data_sites = api_auth.list_sites().json()
    sites = []
    for item in data_sites["items"]:
        site = item["id"]
        # Substring of site is used as first 5 letters of substring contain site- which is a type of site
        if site_type in site[5:]:
            sites.append(item["id"])

    if len(sites) > 0:

        speech = "Sites with type {}: {}".format(site_type, sites)
        logging.debug(speech)
    else:
        speech = "No sites could be found with name: {}".format( site_type)
    return speech


# auth = app.SteelConnectAPI("Anthony", "Anthony", "monash.riverbed.cc", "org-Monash-d388075e40cf1bfd")
# param = {"SiteTypes": "site"}
# print(list_sites(api_auth=auth, parameters=param))
