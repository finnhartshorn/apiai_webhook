from flask import render_template, flash, redirect
from app import app
from forms import OrganisationForm

@app.route('/orgID/', methods=['GET', 'POST'])
def org_form():
    form = OrganisationForm()
    if form.validate_on_submit():
        # print form.org_id + " : " + form.org_name
        flash("{} {}".format(form.org_id, form.org_name))
        return redirect('/test')
    return render_template("details.html",
                           title="Organisation Details",
                           form=form)

@app.route('/test/')
def test():
    return("Test")