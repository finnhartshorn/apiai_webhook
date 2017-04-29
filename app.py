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


# https://github.com/api-ai/apiai-weather-webhook-sample/blob/master/app.py

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    :return: Returns a json formatted response containing the speech to be read back to the user, giving details on the result of the request
    :rtype: json
    """
    req = request.get_json(silent=True, force=True)

    logging.debug("Request\n" + json.dumps(req, indent=4))

    response_message = process_request(req)

    return response_message


def process_request(req):
    """
    Determines the intent of the request and passes its parameters to the relevant method
    :param req: json request from API.AI
    :type req: json
    :return: json formatted response
    :rtype: json
    """
    try:
        action_type = req["result"]["action"]
        parameters = req["result"]["parameters"]
    except KeyError as e:
        logging.error("Error accessing action type {0}".format(e))
        return format_response("Unknown error occurred, please try again.")

    if action_type == "CreateSite":
        response = create_site.create_site(parameters)

    elif action_type == "DeleteSite":
        raise NotImplementedError

    else:
        error = "Error unknown action {}".format(action_type)
        logging.error(error)
        response = error

    return format_response(response)


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
