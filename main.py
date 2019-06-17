import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/new_donation', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        donor = request.form['donor']
        amount = int(request.form['amount'])
        saved_donor = Donor.select().where(Donor.name == donor).get()
        Donation(donor=saved_donor, value=amount).save()
        return redirect(url_for('home'))
    return render_template('new_donation.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

