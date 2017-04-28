from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import os
import json
import logging

from actions import createSite

# Not needed yet
# from urllib.parse import urlparse, urlencode
# from urllib.request import urlopen, Request
# from urllib.error import HTTPError

app = Flask(__name__)


@app.route('/')
def home():
    return "This app works"


# https://github.com/api-ai/apiai-weather-webhook-sample/blob/master/app.py

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    logging.debug("Request\n" + json.dumps(req, indent=4))

    try:
        action_type = req["result"]["action"]
        parameters = req["result"]["parameters"]
    except KeyError as e:
        logging.error("Error accessing action type {0}".format(e))

    if action_type == "CreateSite":
        res = createSite.createSite(parameters)

    elif action_type == "DeleteSite":
        raise NotImplementedError

    else:
        logging.error("Error unknown action {}".format(action_type))
        #TODO: change to send error back
        res = process_request(req)

    res = json.dumps(res, indent=4)
    logging.debug(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def process_request(req):
    speech = "Your request has been successful"
    return {
        "speech": speech,
        "displayText": speech,
        "source": "steelconnect"
    }


if __name__ == '__main__':
    # Only used when running locally, uses entrypoint in app.yaml when run on google cloud
    app.run(debug=True, port=8080, host='127.0.0.1')
