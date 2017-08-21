import logging

from flask import json
from actions import create_uplink

def add_site_to_WAN(api_auth, parameters, contexts):
    """
    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :param contexts: json contexts from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        wan_context = api_auth.find_context_by_name(contexts, "wan_created")["parameters"]
        site_context = api_auth.find_context_by_name(contexts, "sitecreated")["parameters"]

        new_parameters = {"SiteTypes": site_context["SiteType"],
                          "City": site_context["City"],
                          "Wans": wan_context["WANType"],
                          "Uplinks": ""}


    except KeyError as e:

        error_string = "Error processing addSitesToWAN intent. {0}".format(e)

        logging.error(error_string)

        return error_string

    speech = create_uplink(api_auth, new_parameters)

    logging.debug(speech)

    return speech

