from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import json
import logging

from actions import create_site

app = Flask(__name__)


@app.route('/')
def home():
    return "This app works"


@app.route('/webhook/createsite', methods=['POST'])
def create_site():
    """
    :return: Creates a site of the given type at the given location and returns a confirmation message to be read out to the user
    :rtype: json
    """
    req = request.get_json(silent=True, force=True)

    logging.debug("Request\n" + json.dumps(req, indent=4))

    parameters = check_request(req, "CreateSite")           # CreateSite is what the API.AI intent is called

    response = create_site.create_site(parameters)          # Pass the parameters to the function that handles the API calls

    return format_response(response)                        # Correctly format the text response into json for API.AI to read out to the user


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
