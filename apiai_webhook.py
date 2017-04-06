from flask import Flask, request, make_response
import os
import json

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

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

    # res = processRequest(req)
    #
    # res = json.dumps(res, indent=4)
    # print(res)
    # r = make_response(res)
    # r.headers['Content-Type'] = 'application/json'
    # return r

    return


def processRequest(req):
    raise NotImplementedError


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
