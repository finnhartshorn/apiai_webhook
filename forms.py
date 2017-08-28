from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, URL

class OrganisationForm(FlaskForm):
    org_id = StringField("org_id", validators=[DataRequired()])
    sc_url = StringField("sc_url", validators=[DataRequired(), URL(require_tld=False, message="Invalid URL")])
    sc_username = StringField("sc_username", validators=[DataRequired()])
    sc_password = PasswordField("sc_password", validators=[DataRequired()])