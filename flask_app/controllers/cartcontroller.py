from flask import Flask, render_template, request, redirect, session

from flask_app import app

from flask_app.models.cartmodel import Cart

@app.post('/addcart')
def updatecart():
    # session['cart'][f"request.form['id']"] = request.form['id']
    return redirect('/cart')