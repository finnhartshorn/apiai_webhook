from flask import Flask, request, make_response
import json
import logging

app = Flask(__name__)

from actions.create_uplink import create_uplink

def check_request(req, expected_action_type):
    """
    Checks whether the request has the correct action type and extracts the parameters
    :param expected_action_type: The action string expected
    :type expected_action_type: string
    :param req: json request from API.AI
    :type req: json
    :return: parameters
    :rtype: python dictionary of the parameters passed in from the API.AI call
    """
    try:
        action_type = req["result"]["action"]
        parameters = req["result"]["parameters"]
    except KeyError as e:
        logging.error("Error accessing action type {0}".format(e))
        return {}

    if action_type == expected_action_type:
        return parameters

req = {
  "id": "cc96c1c2-a738-4e3d-8764-83ec0a05e30d",
  "timestamp": "2017-05-17T13:02:48.827Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "create a link in geelong branch",
    "action": "CreateUplink",
    "actionIncomplete": False,
    "parameters": {
      "City": "Melbourne",
      "geo-city": "",
      "SiteTypes": "shop",
      "Uplinks": "uplink"
    },
    "contexts": [],
    "metadata": {
      "intentId": "f47796b8-5382-453e-be83-4afaaf0efd33",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 49,
      "intentName": "CreateUplinkIntent"
    },
    "fulfillment": {
      "speech": "Error: This feature has not been implemented yet",
      "source": "steelconnect",
      "displayText": "Error: This feature has not been implemented yet",
      "messages": [
        {
          "type": 0,
          "speech": "Error: This feature has not been implemented yet"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "781b0f15-ed6f-461a-8cb0-7cbf2fd85f0b"
}

logging.debug("Request\n" + json.dumps(req, indent=4))

parameters = check_request(req, "CreateUplink")

response = create_uplink(parameters)          # Pass the parameters to the function that handles the API calls

print(response)