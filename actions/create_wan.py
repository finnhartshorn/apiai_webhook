import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests


def create_wan(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        wan = parameters["WAN"]
        orgid = parameters["Organisation"]
        
        # API Call Here
        url = 'https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/wans'
        data = {
          "id": "",
          "org": orgid,
          "uplinks": [
            ""
          ],
          "nets": [
            ""
          ],
          "name": "",
          "longname": "",
          "uid": "",
          "internet": true,
          "sitelink": true,
          "pingcheck_ips": "",
          "dcuplink": [
            ""
          ],
          "breakout": true,
          "breakout_sites": [
            ""
          ],
          "xfer_networks": "string"
        }
        request = json.dumps(data, indent=4)
        res = requests.post(url, data=request, auth=HTTPBasicAuth('Denver', 'Denver'))
        logging.debug(res)
        # Ends Here

        if res.status_code == 200:
            speech = "{} created in {}".format(wan.capitalize(), orgid)
        elif res.status_code == 400:
            speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
        elif res.status_code == 500:
            speech = "Error: Could not create wan"
        else:
            speech = "Error: Could not connect to Steelconnect"

        logging.debug(speech)

        return speech

    except KeyError as e:

        error_string = "Error processing createWan intent. {0}".format(e)

        logging.error(error_string)

        return error_string

