import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests
import app


def create_path_rule(api_auth, parameters):
    """
    :param api_auth: SteelConnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """


    # Call create_path_rule in SteelConnectAPI
    res = api_auth.create_path_rule()

    if res.status_code == 200:
        speech = "Path Rule Created".format()
    elif res.status_code == 400:
        speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
    elif res.status_code == 404:
        speech = "Error: Organization with given id does not exist"
    elif res.status_code == 500:
        speech = "Error: Could not create Path Rule"
    else:
        speech = "Error: Could not connect to SteelConnect"

    logging.debug(speech)

    return speech


# auth = app.SteelConnectAPI("Anthony", "Anthony", "monash.riverbed.cc", "org-Monash-d388075e40cf1bfd")
# param = {}
# print(create_path_rule(api_auth=auth, parameters=param))
