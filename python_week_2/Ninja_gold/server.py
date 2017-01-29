from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ShhItsASecret"
import random
@app.route('/')
def main():
    session['number'] = 0
    return render_template('main.html', gold = session['number'])

@app.route('/process_money', methods = ['post'])
def process():
    if request.form['action'] == "farmmoney":
        session['number']= session['number']+random.randrange(10,20)
        return render_template('main.html', gold = session['number'])
    if request.form['action'] == "cavemoney":
        session['number']= session['number']+random.randrange(5,10)
        return render_template('main.html', gold = session['number'])
    if request.form['action'] == "housemoney":
        session['number']= session['number']+random.randrange(2,5)
        return render_template('main.html', gold = session['number'])
    else:
        session['number']= session['number']+random.randrange(-50,50)
        return render_template('main.html', gold = session['number'])
app.run(debug = True)
