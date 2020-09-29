import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = b'/\x17\x1c\xef\xd0\x80\xfd\xb0j\xf2\x88\xbdZ\r\xb8^\x9b\n1E\xf3@\xd4\xb3'
#app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        Donation.insert(donor=request.form['donor'], value=request.form['number']).execute()
        return redirect(url_for('all'))
    else:
        return render_template('create.jinja2', donors=Donor.select().distinct())

@app.route('/donations/')
def all():
    Tot_Donor_List = []
    donors = Donor.select()

    for donor in donors:
        donations = Donation.select().where(Donation.donor == donor)
        don_tot = 0
        for donation in donations:
            don_tot += int(donation.value)
        Tot_Donor_List.append({"Name": donor.name, "Amount": '{:,.2f}'.format(don_tot)})
    return render_template('donations.jinja2', donations=Tot_Donor_List)

@app.route('/all_donations')
def all_donations():
    all_donations = Donation.select().where(Donation.donor).order_by(Donation.donor, Donation.value)
    return render_template('all_donations.jinja2', all_donations=all_donations)

@app.route('/lookup', methods=['GET', 'POST'])
def donor_lookup():
    # I need some help with this
    # if request.method == 'GET':
    #     donor_name = request.form['name']
    #     try:
    #         print("Made it here try")
    #         Test_attr = Donation.select().where(Donation.donor.name == donor_name)
    #         print("try the Test!")
    #         if request.form['name']  in Test_attr :
    #             print("Made it here2")
    #             all_donations = Donation.select().where(Donation.donor==request.form['name']).order_by(Donation.value)
    #             return render_template('lookup.jinja2', all_donations=all_donations)
    #         raise ValueError
    #     except ValueError:
    #         return render_template('lookup.jinja2', error="Name not found.")

    return render_template('lookup.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

