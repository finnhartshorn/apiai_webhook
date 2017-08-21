from flask import redirect, url_for, session, request
from flask_oauthlib.client import OAuth
from app import app

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
            return redirect(url_for('org_form'))
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