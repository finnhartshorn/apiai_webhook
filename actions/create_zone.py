import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests


def create_zone(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        name = parameters["name"]
        site_name = parameters["site"]

        # Get all sites and check whether site exists
        res = requests.get('https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/sites', auth=HTTPBasicAuth('Anthony', 'Anthony'))
        data = res.json()
        site = ""
        for item in data['items']:
            if site_name in item['name']:
                site = item['id']

        if site != "":

            # API Call Here
            url = 'https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/zones'
            data = {
                    "name": name,
                    "site": site
            }

            request = json.dumps(data, indent=4)
            res = requests.post(url, data=request, auth=HTTPBasicAuth('Anthony', 'Anthony'))
            logging.debug(res)
            # Ends Here

            if res.status_code == 200:
                speech = "Zone: {} created for site: {}".format(name, site_name)
            elif res.status_code == 400:
                speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
            elif res.status_code == 500:
                speech = "Error: Could not create uplink"
            else:
                speech = "Error: Could not connect to Steelconnect"

            logging.debug(speech)
        else:
            speech = "Invalid site {}".format(site_name)
            return speech

    except KeyError as e:

        error_string = "Error processing create Zone intent. {0}".format(e)

        logging.error(error_string)

        return error_string