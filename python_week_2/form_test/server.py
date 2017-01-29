from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/users",methods = ['post'])
def creat_user():
    print 'Got Post Info'
    name = request.form['name']
    email = request.form['email']
    return render_template('form1.html', name1 = name, email1 = email)

app.run(debug=True)
