import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session,jsonify

from model import Donation, Donor,Login

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route('/')
def home():
    return render_template('all_donations.jinja2')


@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['name']
        password = request.form['password']
        login_check=Login.select().where(Login.username == username,Login.password==password)
        if login_check:
            return render_template('base.jinja2')
        else:
            return render_template('login.jinja2',error='no usrename')
    else:
        return render_template('login.jinja2')


@app.route('/create/', methods=['POST','GET'])
def create():
    if request.method=='POST':
        donor = Donor()
        donor.name=request.form['name']
        donor.save()
        donations=Donation()
        donations.value = request.form['value']
        donations.donor = donor.id
        donations.save()
        return jsonify({"data":"add success!"})
    else:
        return render_template('create.jinja2')


@app.route('/donations/', methods=['GET', 'POST'])
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/donations2/', methods=['GET', 'POST'])
def donations_for():
    if request.method == 'GET':
        return render_template('all_donations.jinja2')

    elif request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        donations = Donation.select().join(Donor).where(Donor.name == name)

        if donations:
            donor = Donor()
            donor.name = name
            donor.save()
            donations2 = Donation()
            donations2.value = value
            donations2.donor = donor.id
            donations2.save()
            return render_template('donations.jinja2',donations=donations)
        else:
            return render_template('donations.jinja2', error='wrong!')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port,debug=True)

