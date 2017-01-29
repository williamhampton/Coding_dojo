from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app,'email_val')
email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
@app.route('/')
def index():
    query = "SELECT * FROM email"
    emails = mysql.query_db(query)
    return render_template('index.html', all_email = emails )

@app.route("/submit", methods = ['POST'])
def submit():
    email1 = request.form['email']
    if email_re.match(email1):
        query = "INSERT INTO email (email_ad) VALUES (:email)"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/')
    if not email_re.match(email1):
        flash('Fill out a valid email please', 'email')
        return redirect('/')
app.run(debug=True)
