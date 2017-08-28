from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    """
    A decorator to check if a user is logged in
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'google_token' not in session or not session['google_token']:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function