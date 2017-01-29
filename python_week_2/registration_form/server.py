from flask import Flask,render_template,redirect, request, session, flash
import re
email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
def containnumber(string):
    return bool(re.search(r'\d', string))
app = Flask(__name__)
app.secret_key = "secret"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    passwordcon = request.form['confirm_password']
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
        return redirect('/', thankyou = 'Thanks for submitting your information')
    return redirect('/')
app.run(debug = True)
