from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import json
import logging

from actions.create_uplink import create_uplink
from actions.create_site import create_site
from actions.list_sites import list_sites

app = Flask(__name__)


@app.route('/')
def home():
    return "This app works"


@app.route('/webhook/', methods=['POST'])
def webhook():
    """
    Extracts the intent, action and paramaters and passes them to the handling method.
    :return: Returns a json formatted response containing the text to be read back to the user
    :rtype: json
    """
    req = request.get_json(silent=True, force=True)

    logging.debug("Request\n" + json.dumps(req, indent=4))

    try:
        action_type = req["result"]["action"]
        intent_type = req["result"]["metadata"]["intentName"]
        parameters = req["result"]["parameters"]
        if action_type == "CreateSite":
            response = create_site(parameters)
        elif action_type == "CreateUplink":
            response = create_uplink(parameters)
        elif action_type == "ListSites":
            response = list_sites(parameters)
        # elsif action_type == "SomeOtherAction"            # Use elsif to add extra functionality
        else:
            response = "Error: This feature has not been implemented yet"
            logging.error("Not implemented error action: {} intent: {}".format(action_type, intent_type))

    except KeyError as e:
        logging.error("Error processing request {0}".format(e))
        response = "There was an error processing your request"

    return format_response(response)                        # Correctly format the text response into json for API.AI to read out to the user


def format_response(speech):
    """
    :param speech: A text string to be read out to the user
    :type speech: string
    :return: Returns a json formatted response
    :rtype: json
    """
    response = {
        "speech": speech,
        "displayText": speech,
        "source": "steelconnect"
    }

    response = json.dumps(response, indent=4)
    logging.debug(response)
    r = make_response(response)
    r.headers['Content-Type'] = 'application/json'

    return r


if __name__ == '__main__':
    # Only used when running locally, uses entrypoint in app.yaml when run on google cloud
    app.run(debug=True, port=8080, host='127.0.0.1')
