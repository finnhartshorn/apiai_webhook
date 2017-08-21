# from __future__ import print_function
# from future.standard_library import install_aliases
# install_aliases()

from flask import Flask


from actions.api import SteelConnectAPI


app = Flask(__name__)

app.secret_key = 'development'

# Setup up api authentication
app.config["SC_API"]  = SteelConnectAPI("Finn", "Kalapuikot", "monash.riverbed.cc", "org-Monash-d388075e40cf1bfd")

from views.oauth import *
from views.webhook import *
from views.form import *



if __name__ == '__main__':
    # Only used when running locally, uses entrypoint in app.yaml when run on google cloud
    app.run(debug=True, port=8080, host='127.0.0.1')
