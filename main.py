import os
import base64
from pprint import pprint
from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor
from peewee import DoesNotExist


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all_donations'))


@app.route('/donations/')
def all_donations():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/add/', methods=['GET', 'POST'])
def add_donation():
    # if 'username' not in session:
    #     return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            existing_donor = Donor.get(Donor.name == request.form['donor'])
            Donation(donor=existing_donor, value=request.form['value']).save()

        except DoesNotExist:
            new_donor = Donor(name=request.form['donor'].title())
            new_donor.save()
            Donation(donor=new_donor, value=request.form['value']).save()
        return redirect(url_for('all_donations'))
    else:
        return render_template('add.jinja2')


def main():
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
