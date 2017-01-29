from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/')
def index():
    x = 1
    session['counting']= session['counting'] + x
    return render_template("index.html")

@app.route('/+2')
def times():
    session['counting']= session['counting'] + 2
    return render_template('index.html')


@app.route('/reset')
def counting():
    session['counting'] = 1
    return render_template('index.html')
app.run(debug = True)
