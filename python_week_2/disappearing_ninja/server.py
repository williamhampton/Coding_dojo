from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def index():
    return render_template('index.html', main = True)
@app.route('/ninja')
def ninja():
    return render_template("index.html", picture = True)
@app.route('/ninja/<color>')
def appear(color):
    if color == 'blue':
        return render_template('ninja.html',color ='leonardo.jpg' )
    if color == 'red':
        return render_template('ninja.html', color = 'raphael.jpg')
    if color == 'orange':
        return render_template('ninja.html', color = 'michelangelo.jpg')
    if color == 'purple':
        return render_template('ninja.html', color = 'donatello.jpg')
    else:
        return render_template('ninja.html', color = 'notapril.jpg')

app.run(debug = True)
