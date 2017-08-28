# from __future__ import print_function
# from future.standard_library import install_aliases
# install_aliases()

from flask import Flask, request, make_response, render_template, flash, redirect, url_for, session
import json
import logging

from flask_oauthlib.client import OAuth

from actions.create_uplink import create_uplink
from actions.create_site import create_site
from actions.list_sites import list_sites
from actions.list_sites_followup import list_sites_followup
from actions.create_wan import create_wan
from actions.create_WAN_new import create_WAN
from actions.add_site_to_wan import add_site_to_WAN
from actions.clear_sites import clear_sites
from actions.create_zone import create_zone

from forms import OrganisationForm
from decorators import login_required

from actions.api import SteelConnectAPI, SteelConnectAuthFactory

app = Flask(__name__)

app.secret_key = 'development'

# Setup up api authentication

app.config["SC_API"]  = SteelConnectAuthFactory("Finn", "Kalapuikot", "monash.riverbed.cc", "org-Monash-d388075e40cf1bfd")


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
        contexts = req["result"]["contexts"]
    except KeyError as e:
        logging.error("Error processing request {}".format(e))
        return format_response("There was an error processing your request")

    steelconnect_auth = app.config["SC_API"].make_auth()

    if action_type == "CreateSite":
        response = create_site(steelconnect_auth, parameters)
    elif action_type == "CreateUplink":
        response = create_uplink(parameters)
    elif action_type == "ListSites":
        response = list_sites(steelconnect_auth, parameters)
    elif action_type == "ListSites.ListSites-custom":
        response = list_sites_followup(steelconnect_auth, req["result"]["contexts"][0]["parameters"])
    elif action_type == "ListSites.ListSites-yes":
        parameters["position"] = "all"
        response = list_sites_followup(steelconnect_auth, None)
    elif action_type == "CreateWan":
        response = create_wan(parameters)
    elif action_type == "CreateWAN":
        response = create_WAN(steelconnect_auth, parameters, contexts)
    elif action_type == "AddSiteToWAN":
        response = add_site_to_WAN(steelconnect_auth, parameters, contexts)
    elif action_type == "ClearSites":
        response = clear_sites(parameters)
    elif action_type == "CreateZone":
        response = create_zone(steelconnect_auth, parameters)


    # elif action_type == "SomeOtherAction"            # Use elif to add extra functionality
    else:
        response = "Error: This feature has not been implemented yet"
        logging.error("Not implemented error action: {} intent: {}".format(action_type, intent_type))

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


@app.route('/auth/', methods=['GET', 'POST'])
@login_required
def auth_form():
    form = OrganisationForm(request.form)
    if form.validate_on_submit():
        flash("{} {}".format(request.form['org_id'], request.form['sc_url']))
        return redirect('/test')
    return render_template("details.html",
                           title="Authentication Details",
                           form=form)

@app.route('/test/')
@login_required
def test():
    return render_template("base.html", title="Test")


oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key="421857248544-mtkb30l1fm6o75pm84qpk3sd3s4027q0.apps.googleusercontent.com",
    consumer_secret="NuI3lwH8_vnS3ejw0HOIaEOr",
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth'
)

@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        if me.status == 401:
            return redirect(url_for('logout'))
        elif me.status == 200:
            return redirect(url_for('auth_form'))
        else:
            print(me.status)
            return me.data
    else:
        return redirect(url_for('login'))


@app.route('/login/')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout/')
def logout():
    session.pop('google_token', None)
    session.pop('user_email', None)
    return redirect(url_for('index'))


@app.route('/login/authorized/')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    info = google.get('userinfo')
    session['user_email'] = info.data['email']
    return redirect(url_for('index'))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


if __name__ == '__main__':
    # Only used when running locally, uses entrypoint in app.yaml when run on google cloud
    app.run(debug=True, port=8080, host='127.0.0.1')
