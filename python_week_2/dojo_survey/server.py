from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/result', methods = ['post'])
def results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html',name1 = name, location1 = location, language1 = language, comment1 = comment)

app.run(debug=True)
