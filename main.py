""" the server entry point """
import os

from flask import Flask, render_template, request, \
                redirect, url_for, session, flash
from passlib.hash import pbkdf2_sha256
from model import Donor, Donation, User

APP = Flask(__name__)
APP.secret_key = os.environ.get('SECRET_KEY').encode()


@APP.route('/')
def home():
    """ set the login page as the default """
    return redirect(url_for('login'))


@APP.route('/donations/')
def donations():
    """ list all the donations for all donors """
    _donations = Donation.select()
    return render_template('donations.jinja2', donations=_donations)


@APP.route('/donate/', methods=['POST', 'GET'])
def donate():
    """ let a user create a new donor / donation """
    if request.method == 'POST':
        donor_name = request.form['name']
        amount = request.form['value']
        if donor_name and amount:
            donor_count = Donor.select() \
                            .where(Donor.name == request.form['name']) \
                            .count()

            if donor_count == 0:
                donor = Donor.create(name=request.form['name'])
            else:
                donor = Donor.get(name=request.form['name'])

            if int(amount) <= 1000000 and int(amount) > 0:
                Donation.create(donor=donor, value=request.form['value'])
                _donations = Donation.select()
                return render_template('donations.jinja2',
                                       donations=_donations)

            flash('Input amount within an acceptable range (0 to 1000000)')
            return render_template('add_donation.jinja2')
    elif request.method == 'GET':
        if session.get('username'):
            return render_template('add_donation.jinja2')

    return render_template('login.jinja2')


@APP.route('/login', methods=['POST', 'GET'])
def login():
    """ login to the system """
    if request.method == 'POST':
        user = User.select().where(User.name == request.form['name']).get()

        if user is not None and pbkdf2_sha256.verify(request.form['password'],
                                                     user.password):
            session['username'] = request.form['name']
            return redirect(url_for('donate'))

        return render_template('login.jinja2',
                               error="Incorrect username or password.")

    return render_template('login.jinja2')


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 6738))
    APP.run(host='0.0.0.0', port=PORT)
