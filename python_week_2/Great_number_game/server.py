from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "stupidpaininthe..."
import random
@app.route('/')
def main():
    session['number'] = random.randrange(0,101)
    return render_template('main.html')

@app.route('/results', methods = ['post'])
def results():
    number = int(request.form['guess'])
    x = session['number']
    if number == x:
        return render_template('main.html', result = 'YAY!! You win!!',reset = 'Reset ME!!')
    elif number < x:
        return render_template('main.html', result = 'Too Low...')
    else:
        return render_template('main.html', result = "Too High")

app.run(debug = True)
