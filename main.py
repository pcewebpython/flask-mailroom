#!/usr/bin/env python3
""" Flask app for mailroom donations """
#pylint: disable=E0401

import os
from flask import Flask, render_template, request, redirect, url_for, session
from peewee import DoesNotExist
from passlib.hash import pbkdf2_sha256
from model import Donation, Donor, User


app = Flask(__name__)
app.secret_key = b'\x8d\xe5\xdf\x08L\xda<\x06S\xca\xab:\x8a\xee\xef\xfa\xfedV\xa84b\x06j\xd7N\xbf;\xe7\x174\x1a'
# app.secret_key = os.environ.get('SECRET_KEY').encode()



@app.route('/')
def home():
    """ Returns the homepage for mailroom """
    return redirect(url_for('all_donations'))


@app.route('/donations/')
def all_donations():
    """ Gets all donations from database and returns page with donations """
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/add/', methods=['GET', 'POST'])
def add_donation():
    """ Adds new donations to database.

    Requires user to be logged in (session['logged_in']==True)
    If users not logged in, returns login page.
    """
    try:
        if session['logged_in'] is not True:
            return redirect(url_for('login'))
    except KeyError:
        session['logged_in'] = False
        return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            existing_donor = Donor.get(Donor.name == request.form['donor'].title())
            Donation(donor=existing_donor, value=request.form['value']).save()
        except DoesNotExist:
            new_donor = Donor(name=request.form['donor'].title())
            new_donor.save()
            Donation(donor=new_donor, value=request.form['value']).save()
        return redirect(url_for('all_donations'))
    return render_template('add.jinja2')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login page for users, required to add donation """
    if request.method == 'POST':
        user = User.select().where(User.name == request.form['name']).get()
        if user and pbkdf2_sha256.verify(request.form['password'], user.password):
            session['logged_in'] = True
            return redirect(url_for('all_donations'))
        return render_template('login.jinja2', error="Incorrect username or password.")
    return render_template('login.jinja2')


@app.route('/logout')
def logout():
    """ Logout page.

    Sets session['logged_in'] = False and returns all_donation page
    """
    session['logged_in'] = False
    return redirect(url_for('all_donations'))


def main():
    """ We Wuz Main """
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
