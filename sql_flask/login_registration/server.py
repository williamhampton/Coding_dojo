from flask import Flask, request, redirect, render_template,flash, session
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt
email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
def containnumber(string):
    return bool(re.search(r'\d', string))
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'login_reg')
@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users )

@app.route('/error')
def error():
    return render_template('index.html', login_error = 'enter a valid email')

@app.route('/registration', methods = ['POST'])
def register():
    firstname = request.form['first']
    lastname = request.form['last']
    email = request.form['email']
    password = request.form['pass']
    passwordcon = request.form['passcon']
    pw_hash = bcrypt.generate_password_hash(password)
    error = False
    if len(firstname)<2:
        error= True
        flash('Fill out the first name', 'first_name')
    if containnumber(firstname)==True:
        error = True
        flash('Error name can not contain a number', 'first_name')
    if len(lastname)<2:
        error = True
        flash('Fill out the last name', 'last_name')
    if containnumber(lastname):
        error = True
        flash('Error name can not contain a number', 'last_name')
    if not email_re.match(email):
        error = True
        flash('Fill out a valid email please', 'email')
    if len(password)<9:
        error = True
        flash('Password must be longer than 8 digits', 'password')
    if len(passwordcon)<9:
        error = True
        flash('Password must be longer than 8 digits', 'confirm_password')
    if password != passwordcon:
        error = True
        flash('Passwords must match', 'match_password')
    if not error:
        query = 'INSERT INTO users (first,last, email, password) VALUES(:first, :last, :email, :pw_hash )'
        data = {
            'first': request.form['first'],
            'last': request.form['last'],
            'email': request.form['email'],
            'pw_hash': pw_hash
            }
        mysql.query_db(query,data)
        return redirect('/')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
#    password = request.form['pass']
#    if bcrypt.check_password_hash(pw_hash, password):
#        return render_template('user_id.html')
#    else:
#        return redirect('/')
    email = request.form['email_login']
    password_login = request.form['password_login']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if user != email:
        return redirect('/error')
    if bcrypt.check_password_hash(user[0]['password'], password_login):
        return render_template('user_id.html', worked = 'worked')
    else:
        return redirect('/')
app.run(debug=True)
