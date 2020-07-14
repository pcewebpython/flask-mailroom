import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all_donations'))


@app.route('/create/', methods=['Get','POST'])
def create():
    if request.method == 'POST':
        donor = Donor()
        donor.donor(name=request.form['name'])
        value = Donor(value=request.form['value'])
        donor.save()
        value.save()
    else:
        return render_template('donations.jinja2')


@app.route('/donations/', methods=['GET', 'POST'])
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donations/<name>', methods=['GET', 'POST'])
def donations_for(name):
    if request.method == 'GET':
        return redirect(url_for('all_donations'))

    elif request.method == 'POST':
        session['donor_name'] = request.form['name']
        session['donor_amount'] = request.form['value']
        donations = Donation.select().join(Donor).where(Donor.name == name)

        if donations is True:
            create()
            return redirect(url_for('all_donations'))

        return render_template('create.jinja2', error="Incorrect donor name.")

    else:
        return render_template('donations.jinja2', donations=donations)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

