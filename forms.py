from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class OrganisationForm(FlaskForm):
    org_id = StringField("org_id", validators=[DataRequired()])
    org_name = StringField("org_name", validators=[DataRequired()])