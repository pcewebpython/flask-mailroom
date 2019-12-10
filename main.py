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
    
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        # Handle the form submission
        # f_name = request.form['name']
        # amount = request.form['amount']
        query = Donor.select().where(Donor.name == request.form['name'])
        if query.exists():
            Donation(donor=request.form['name'], value=request.form['amount']).save()
        else:
            f_name = Donor(name=request.form['name'])
            f_name.save()
            Donation(donor=f_name, value=request.form['amount']).save()



        # if f_name == d_name:
        #     # existing_donation = Donation.select().where(Donor.name == request.form['name']).get()
        #     # updated_donation = existing_donation.value + int(amount)
        #     # Donation.update(value=updated_donation).where(Donor.name == request.form['name']).execute()
        #     Donor.create(name=f_name)
        #     Donation.
        return redirect(url_for('all'))

    else:
        return render_template('new_donations.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

