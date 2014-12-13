import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
	'secret_key': Oqu2VTvOtbqkwNZgcXAjJZ72myxVOrCh,
	'publishable_key': pk_X0j7NxbfNHQLwcVf6V5Q9UfJGvmia
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

    customer = stripe.Customer.create(
        email='customer@example.com',
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