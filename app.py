from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import os
import json

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

    print("Request:")
    print(json.dumps(req, indent=4))

    res = process_request(req)

    res = json.dumps(res, indent=4)
    print(res)
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
    # port = int(os.getenv('PORT', 5000))
    #
    # print("Starting app on port %d" % port)

    # Only used when running locally
    app.run(debug=True, port=8080, host='127.0.0.1')
