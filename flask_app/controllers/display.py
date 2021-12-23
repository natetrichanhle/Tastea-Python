from flask import render_template,url_for
from flask_app import app

from flask_app.models import productsmodel

@app.route('/')
def startOrder():
    return render_template('start_order.html')

@app.route('/categories')
def nav():
    return render_template('navigator.html')

@app.route('/hotties')
def hotties():
    # items = productsmodel.Product.get_all_category()
    return render_template('hotties.html')

@app.route('/exit')
def exit():
    return render_template('start_order.html')

@app.route('/stevia')
def stevia():
    return render_template('stevia.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/purchase')
def purchase():
    return render_template('thankyou.html')

@app.route('/startover')
def startOver():
    return render_template('navigator.html')
