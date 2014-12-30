import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/tools')
def tools():
	return render_template('tools.html', key=stripe_keys['publishable_key'])

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/charge', methods=['POST'])


def charge():
    # Amount in cents
    amount = 500

    # Need to check if the inputted email exists. How to retreive by email?
    existing_customer = stripe.Customer.retrieve('cus_5QOfskKQ1bn2H9')

    if existing_customer:
        charge = stripe.Charge.create(
        customer=existing_customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    else:

        customer = stripe.Customer.create(
            email=request.form['stripeEmail'],
            card=request.form['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='Flask Charge'
        )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)